# catalytic_activity_0145

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/catalytic_activity_0145.txt)

**Task:** `catalytic_activity`  
**Expected answer:** **D** — UDP-2-acetamido-2-deoxy-alpha-D-glucuronate = UDP-2-acetamido-2-deoxy-alpha-D-galacturonate

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MMSRYEELRKELPAQPKVWLITGVAGFIGSNLLETLLKLDQKVVGLDNFATGHQRNLDEVRSLVSEKQWSNFKFIQGDIRNLDDCNNACAGVDYVLHQAALGSVPRSINDPITSNATNIDGFLNMLIAARDAKVQSFTYAASSSTYGDHPGLPKVEDTIGKPLSPYAVTKYVNELYADVFSRCYGFSTIGLRYFNVFGRRQDPNGAYAAVIPKWTSSMIQGDDVYINGDGETSRDFCYIENTVQANLLAATAGLDARNQVYNIAVGGRTSLNQLFFALRDGLAENGVSYHREPVYRDFREGDVRHSLADISKAAKLLGYAPKYDVSAGVALAMPWYIMFLK

[Multiple Choices]
A. 17-O-acetylnorajmaline + NADP(+) = (2R)-1,2-dihydrovomilenine + NADPH + 2 H(+)
B. L-galactose + NAD(+) = L-galactono-1,5-lactone + NADH + H(+)
C. Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.
D. UDP-2-acetamido-2-deoxy-alpha-D-glucuronate = UDP-2-acetamido-2-deoxy-alpha-D-galacturonate
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzymatic Reaction Prediction, which is to identify the specific chemical reaction catalyzed by a given enzyme. This involves understanding the enzyme's function based on its amino acid sequence and then selecting the correct transformation of substrates into products from a list of possible reactions.. The inputs provided by the user for this task include:

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

> The sequence-matched UniProt annotation reports the exact reaction in D, with experimental evidence attributed to a publication. The key is supported, although the record also lists another catalytic activity that is not among the choices.

Citations as saved: [C5](#evidence-c5), [H9](#evidence-h9).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 341-aa soluble sequence is consistent with the NAD-dependent nucleotide-sugar epimerase family, including a glycine-rich cofactor-binding region and the broader epimerase architecture. Transferable family knowledge makes a UDP-sugar epimerization reaction a meaningful match for D, unlike the alkaloid and free-sugar redox reactions in A and B or the xylan hydrolase reaction in C.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence and family-level features provide a credible basis to distinguish D among these alternatives. They do not by themselves establish the exact substrate specificity with certainty, but the alternatives are sufficiently different that exact-record lookup is not necessary for a meaningful inference.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only D describes nucleotide-sugar epimerization; the other choices describe different reaction classes.


### Important caveats

- The source annotation also reports a second epimerase activity, but that reaction is not an offered option.
- The reviewer-only annotation supports the key but is not evidence available to the original model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 341-aa soluble sequence is consistent with the NAD-dependent nucleotide-sugar epimerase family, including a glycine-rich cofactor-binding region and the broader epimerase architecture. Transferable family knowledge makes a UDP-sugar epimerization reaction a meaningful match for D, unlike the alkaloid and free-sugar redox reactions in A and B or the xylan hydrolase reaction in C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence and family-level features provide a credible basis to distinguish D among these alternatives. They do not by themselves establish the exact substrate specificity with certainty, but the alternatives are sufficiently different that exact-record lookup is not necessary for a meaningful inference."
  },
  "case_id": "catalytic_activity_0145",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H9"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation reports the exact reaction in D, with experimental evidence attributed to a publication. The key is supported, although the record also lists another catalytic activity that is not among the choices."
  },
  "important_caveats": [
    "The source annotation also reports a second epimerase activity, but that reaction is not an offered option.",
    "The reviewer-only annotation supports the key but is not evidence available to the original model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only D describes nucleotide-sugar epimerization; the other choices describe different reaction classes."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0145",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation reports the exact reaction in D, with experimental evidence attributed to a publication. The key is supported, although the record also lists another catalytic activity that is not among the choices.",
    "evidence_ids": ["C5", "H9"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 341-aa soluble sequence is consistent with the NAD-dependent nucleotide-sugar epimerase family, including a glycine-rich cofactor-binding region and the broader epimerase architecture. Transferable family knowledge makes a UDP-sugar epimerization reaction a meaningful match for D, unlike the alkaloid and free-sugar redox reactions in A and B or the xylan hydrolase reaction in C.",
    "missing_item_specific_fact": "",
    "reason": "The sequence and family-level features provide a credible basis to distinguish D among these alternatives. They do not by themselves establish the exact substrate specificity with certainty, but the alternatives are sufficiently different that exact-record lookup is not necessary for a meaningful inference."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only D describes nucleotide-sugar epimerization; the other choices describe different reaction classes."
  },
  "important_caveats": [
    "The source annotation also reports a second epimerase activity, but that reaction is not an offered option.",
    "The reviewer-only annotation supports the key but is not evidence available to the original model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q8KN66 (sequence matched, 341 aa) lists the recommended name as UDP-N-acetyl-alpha-D-glucosaminouronate 4-epimerase (EC 5.1.3.45) with the catalytic activity 'UDP-2-acetamido-2-deoxy-alpha-D-glucuronate = UDP-2-acetamido-2-deoxy-alpha-D-galacturonate,' supported by experimental evidence (ECO:0000269, PubMed:18065759). This exactly matches choice D.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H9](#evidence-h9).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a clear Rossmann-fold NAD(P)-binding motif ('ITGVAGFIGS' with GxGxxG pattern), indicating an NAD-dependent enzyme. This eliminates choice C (xylanase, a glycoside hydrolase that does not use NAD). The protein lacks any chloroplast transit peptide, mitochondrial targeting sequence, or other eukaryotic/organelle targeting features, and its overall composition is consistent with a bacterial protein. Choices A (vomilenine reductase, a Catharanthus roseus monoterpene alkaloid enzyme) and B (L-galactose dehydrogenase, a plant ascorbate-biosynthesis enzyme) are both plant-specific SDR enzymes; their absence of targeting signals and plant-pathway context makes them implausible for this sequence. Among the remaining choices, D (UDP-sugar 4-epimerase) is a well-known bacterial enzyme class (WecG/WbpP family) involved in O-antigen and capsule biosynthesis, with typical length ~340-380 aa and the observed SDR-type NAD-binding architecture. The combination of NAD-dependence, bacterial character, and SDR epimerase family architecture (WecG/WbpP-type UDP-sugar 4-epimerases) meaningfully distinguishes D from the other three options.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A model can use the NAD-binding Rossmann motif to eliminate the hydrolase (C), recognize the absence of plant targeting signals to disfavor the plant-specific enzymes (A, B), and identify the remaining option as consistent with the well-studied bacterial WecG/WbpP family of UDP-sugar 4-epimerases. This is a chain of transferable family-level and organismal inference, not a lookup of this specific protein's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Once the NAD-binding motif eliminates C and the bacterial (non-plant) character disfavors A and B, only D remains as a viable option. The four choices span three different enzyme classes (alkaloid reductase, sugar dehydrogenase, glycoside hydrolase, UDP-sugar epimerase), so the elimination logic is fairly clean.


### Important caveats

- The SDR superfamily is very large and includes both dehydrogenases and epimerases; distinguishing an SDR epimerase from an SDR dehydrogenase purely by sequence can be subtle. The argument here relies on the specific plant-origin of options A and B rather than a detailed active-site-level discrimination within the SDR family.
- The WbpP/WecG family assignment is a family-level inference; a model that has learned the general features of bacterial UDP-sugar 4-epimerases (length, NAD-binding motif, bacterial context) can make this call, but the argument is probabilistic rather than a unique-sequence proof.
- The UniProt entry also lists EC 5.1.3.7 (UDP-GlcNAc C4 epimerase) as an alternative activity for this protein, but that reaction is not among the offered choices, so it does not create ambiguity within this question.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a clear Rossmann-fold NAD(P)-binding motif ('ITGVAGFIGS' with GxGxxG pattern), indicating an NAD-dependent enzyme. This eliminates choice C (xylanase, a glycoside hydrolase that does not use NAD). The protein lacks any chloroplast transit peptide, mitochondrial targeting sequence, or other eukaryotic/organelle targeting features, and its overall composition is consistent with a bacterial protein. Choices A (vomilenine reductase, a Catharanthus roseus monoterpene alkaloid enzyme) and B (L-galactose dehydrogenase, a plant ascorbate-biosynthesis enzyme) are both plant-specific SDR enzymes; their absence of targeting signals and plant-pathway context makes them implausible for this sequence. Among the remaining choices, D (UDP-sugar 4-epimerase) is a well-known bacterial enzyme class (WecG/WbpP family) involved in O-antigen and capsule biosynthesis, with typical length ~340-380 aa and the observed SDR-type NAD-binding architecture. The combination of NAD-dependence, bacterial character, and SDR epimerase family architecture (WecG/WbpP-type UDP-sugar 4-epimerases) meaningfully distinguishes D from the other three options.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A model can use the NAD-binding Rossmann motif to eliminate the hydrolase (C), recognize the absence of plant targeting signals to disfavor the plant-specific enzymes (A, B), and identify the remaining option as consistent with the well-studied bacterial WecG/WbpP family of UDP-sugar 4-epimerases. This is a chain of transferable family-level and organismal inference, not a lookup of this specific protein's annotation."
  },
  "case_id": "catalytic_activity_0145",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H9"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q8KN66 (sequence matched, 341 aa) lists the recommended name as UDP-N-acetyl-alpha-D-glucosaminouronate 4-epimerase (EC 5.1.3.45) with the catalytic activity 'UDP-2-acetamido-2-deoxy-alpha-D-glucuronate = UDP-2-acetamido-2-deoxy-alpha-D-galacturonate,' supported by experimental evidence (ECO:0000269, PubMed:18065759). This exactly matches choice D."
  },
  "important_caveats": [
    "The SDR superfamily is very large and includes both dehydrogenases and epimerases; distinguishing an SDR epimerase from an SDR dehydrogenase purely by sequence can be subtle. The argument here relies on the specific plant-origin of options A and B rather than a detailed active-site-level discrimination within the SDR family.",
    "The WbpP/WecG family assignment is a family-level inference; a model that has learned the general features of bacterial UDP-sugar 4-epimerases (length, NAD-binding motif, bacterial context) can make this call, but the argument is probabilistic rather than a unique-sequence proof.",
    "The UniProt entry also lists EC 5.1.3.7 (UDP-GlcNAc C4 epimerase) as an alternative activity for this protein, but that reaction is not among the offered choices, so it does not create ambiguity within this question."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Once the NAD-binding motif eliminates C and the bacterial (non-plant) character disfavors A and B, only D remains as a viable option. The four choices span three different enzyme classes (alkaloid reductase, sugar dehydrogenase, glycoside hydrolase, UDP-sugar epimerase), so the elimination logic is fairly clean."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0145",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q8KN66 (sequence matched, 341 aa) lists the recommended name as UDP-N-acetyl-alpha-D-glucosaminouronate 4-epimerase (EC 5.1.3.45) with the catalytic activity 'UDP-2-acetamido-2-deoxy-alpha-D-glucuronate = UDP-2-acetamido-2-deoxy-alpha-D-galacturonate,' supported by experimental evidence (ECO:0000269, PubMed:18065759). This exactly matches choice D.",
    "evidence_ids": ["C4", "C5", "H2", "H9"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a clear Rossmann-fold NAD(P)-binding motif ('ITGVAGFIGS' with GxGxxG pattern), indicating an NAD-dependent enzyme. This eliminates choice C (xylanase, a glycoside hydrolase that does not use NAD). The protein lacks any chloroplast transit peptide, mitochondrial targeting sequence, or other eukaryotic/organelle targeting features, and its overall composition is consistent with a bacterial protein. Choices A (vomilenine reductase, a Catharanthus roseus monoterpene alkaloid enzyme) and B (L-galactose dehydrogenase, a plant ascorbate-biosynthesis enzyme) are both plant-specific SDR enzymes; their absence of targeting signals and plant-pathway context makes them implausible for this sequence. Among the remaining choices, D (UDP-sugar 4-epimerase) is a well-known bacterial enzyme class (WecG/WbpP family) involved in O-antigen and capsule biosynthesis, with typical length ~340-380 aa and the observed SDR-type NAD-binding architecture. The combination of NAD-dependence, bacterial character, and SDR epimerase family architecture (WecG/WbpP-type UDP-sugar 4-epimerases) meaningfully distinguishes D from the other three options.",
    "missing_item_specific_fact": "",
    "reason": "A model can use the NAD-binding Rossmann motif to eliminate the hydrolase (C), recognize the absence of plant targeting signals to disfavor the plant-specific enzymes (A, B), and identify the remaining option as consistent with the well-studied bacterial WecG/WbpP family of UDP-sugar 4-epimerases. This is a chain of transferable family-level and organismal inference, not a lookup of this specific protein's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Once the NAD-binding motif eliminates C and the bacterial (non-plant) character disfavors A and B, only D remains as a viable option. The four choices span three different enzyme classes (alkaloid reductase, sugar dehydrogenase, glycoside hydrolase, UDP-sugar epimerase), so the elimination logic is fairly clean."
  },
  "important_caveats": [
    "The SDR superfamily is very large and includes both dehydrogenases and epimerases; distinguishing an SDR epimerase from an SDR dehydrogenase purely by sequence can be subtle. The argument here relies on the specific plant-origin of options A and B rather than a detailed active-site-level discrimination within the SDR family.",
    "The WbpP/WecG family assignment is a family-level inference; a model that has learned the general features of bacterial UDP-sugar 4-epimerases (length, NAD-binding motif, bacterial context) can make this call, but the argument is probabilistic rather than a unique-sequence proof.",
    "The UniProt entry also lists EC 5.1.3.7 (UDP-GlcNAc C4 epimerase) as an alternative activity for this protein, but that reaction is not among the offered choices, so it does not create ambiguity within this question."
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
  "benchmark_sequence_length": 341,
  "benchmark_sequence_sha256": "89a20333193e2023e3eb938fc67c5a1fcdbb1a54c07d86617c4a4c0b17109406",
  "current_entry_audit": {
    "entryVersion": 89,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2002-10-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "f67b2500389a81025c9be1998ba5bdf0c0e6d0d7f2971007bc6e11f741355b05",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 341,
  "current_source_sequence_sha256": "89a20333193e2023e3eb938fc67c5a1fcdbb1a54c07d86617c4a4c0b17109406",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 87,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q8KN66",
  "selected_historical_entry_version": 87,
  "selected_historical_record_sha256": "d549ed0cf621d2667a5b18f1c61cab90f3244af9d4301b29345d83da21267e72",
  "selected_historical_source_sequence_length": 341,
  "selected_historical_source_sequence_sha256": "89a20333193e2023e3eb938fc67c5a1fcdbb1a54c07d86617c4a4c0b17109406",
  "selected_historical_version": {
    "accession": "Q8KN66",
    "database": "Swiss-Prot",
    "entryVersion": 87,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "WBPP_PSEAI",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8KN66.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q8KN66\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:25.367428+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f67b2500389a81025c9be1998ba5bdf0c0e6d0d7f2971007bc6e11f741355b05",
  "url": "https://rest.uniprot.org/uniprotkb/Q8KN66.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8KN66.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":89,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2002-10-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:25.367428+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f67b2500389a81025c9be1998ba5bdf0c0e6d0d7f2971007bc6e11f741355b05",
  "url": "https://rest.uniprot.org/uniprotkb/Q8KN66.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8KN66.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Pseudomonadota\",\"Gammaproteobacteria\",\"Pseudomonadales\",\"Pseudomonadaceae\",\"Pseudomonas\"],\"scientificName\":\"Pseudomonas aeruginosa\",\"taxonId\":287}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:25.367428+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f67b2500389a81025c9be1998ba5bdf0c0e6d0d7f2971007bc6e11f741355b05",
  "url": "https://rest.uniprot.org/uniprotkb/Q8KN66.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8KN66.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"10747995\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"15016816\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"15752069\",\"source\":\"PubMed\"}],\"value\":\"5.1.3.7\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"15752069\",\"source\":\"PubMed\"}],\"value\":\"UDP-N-acetylglucosamine C4 epimerase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"10747995\",\"source\":\"PubMed\"}],\"value\":\"UDP-GlcNAc C4 epimerase\"}]}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18065759\",\"source\":\"PubMed\"}],\"value\":\"5.1.3.45\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"UDP-N-acetyl-alpha-D-glucosaminouronate 4-epimerase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"UDP-GlcNAcA 4-epimerase\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:25.367428+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f67b2500389a81025c9be1998ba5bdf0c0e6d0d7f2971007bc6e11f741355b05",
  "url": "https://rest.uniprot.org/uniprotkb/Q8KN66.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8KN66.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18065759\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:81512\"}}],\"reaction\":{\"ecNumber\":\"5.1.3.45\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18065759\",\"source\":\"PubMed\"}],\"name\":\"UDP-2-acetamido-2-deoxy-alpha-D-glucuronate = UDP-2-acetamido-2-deoxy-alpha-D-galacturonate\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:81511\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:65040\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231899\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-01T06:25:25.367428+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f67b2500389a81025c9be1998ba5bdf0c0e6d0d7f2971007bc6e11f741355b05",
  "url": "https://rest.uniprot.org/uniprotkb/Q8KN66.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8KN66.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"5.1.3.7\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"10747995\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"15016816\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"15752069\",\"source\":\"PubMed\"}],\"name\":\"UDP-N-acetyl-alpha-D-glucosamine = UDP-N-acetyl-alpha-D-galactosamine\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:20517\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57705\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:67138\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-01T06:25:25.367428+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f67b2500389a81025c9be1998ba5bdf0c0e6d0d7f2971007bc6e11f741355b05",
  "url": "https://rest.uniprot.org/uniprotkb/Q8KN66.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8KN66.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Creuzenet C.\",\"Belanger M.\",\"Wakarchuk W.W.\",\"Lam J.S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"10747995\"},{\"database\":\"DOI\",\"id\":\"10.1074/jbc.m001171200\"}],\"citationType\":\"journal article\",\"firstPage\":\"19060\",\"id\":\"10747995\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"19067\",\"publicationDate\":\"2000\",\"title\":\"Expression, purification, and biochemical characterization of WbpP, a new UDP-GlcNAc C4 epimerase from Pseudomonas aeruginosa serotype O6.\",\"volume\":\"275\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"Serotype O6\"}],\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"COFACTOR\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"SUBUNIT\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-01T06:25:25.367428+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f67b2500389a81025c9be1998ba5bdf0c0e6d0d7f2971007bc6e11f741355b05",
  "url": "https://rest.uniprot.org/uniprotkb/Q8KN66.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8KN66.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Demendi M.\",\"Ishiyama N.\",\"Lam J.S.\",\"Berghuis A.M.\",\"Creuzenet C.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"15752069\"},{\"database\":\"DOI\",\"id\":\"10.1042/bj20050263\"}],\"citationType\":\"journal article\",\"firstPage\":\"173\",\"id\":\"15752069\",\"journal\":\"Biochem. J.\",\"lastPage\":\"180\",\"publicationDate\":\"2005\",\"title\":\"Towards a better understanding of the substrate specificity of the UDP-N-acetylglucosamine C4 epimerase WbpP.\",\"volume\":\"389\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"Serotype O6\"}],\"referenceNumber\":4,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"MUTAGENESIS OF GLY-102; SER-143; SER-144; GLN-201 AND ALA-209\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-01T06:25:25.367428+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f67b2500389a81025c9be1998ba5bdf0c0e6d0d7f2971007bc6e11f741355b05",
  "url": "https://rest.uniprot.org/uniprotkb/Q8KN66.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8KN66.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"citation\":{\"authors\":[\"Miller W.L.\",\"Matewish M.J.\",\"McNally D.J.\",\"Ishiyama N.\",\"Anderson E.M.\",\"Brewer D.\",\"Brisson J.R.\",\"Berghuis A.M.\",\"Lam J.S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"18065759\"},{\"database\":\"DOI\",\"id\":\"10.1074/jbc.m708894200\"}],\"citationType\":\"journal article\",\"firstPage\":\"3507\",\"id\":\"18065759\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"3518\",\"publicationDate\":\"2008\",\"title\":\"Flagellin glycosylation in Pseudomonas aeruginosa PAK requires the O-antigen biosynthesis enzyme WbpO.\",\"volume\":\"283\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"PAK / Serotype O6\"}],\"referenceNumber\":5,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/4",
  "retrieved_utc": "2026-11-01T06:25:25.367428+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f67b2500389a81025c9be1998ba5bdf0c0e6d0d7f2971007bc6e11f741355b05",
  "url": "https://rest.uniprot.org/uniprotkb/Q8KN66.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8KN66.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"citation\":{\"authors\":[\"Ishiyama N.\",\"Creuzenet C.\",\"Lam J.S.\",\"Berghuis A.M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"15016816\"},{\"database\":\"DOI\",\"id\":\"10.1074/jbc.m401642200\"}],\"citationType\":\"journal article\",\"firstPage\":\"22635\",\"id\":\"15016816\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"22642\",\"publicationDate\":\"2004\",\"title\":\"Crystal structure of WbpP, a genuine UDP-N-acetylglucosamine 4-epimerase from Pseudomonas aeruginosa: substrate specificity in UDP-hexose 4-epimerases.\",\"volume\":\"279\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"1SB8\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"1SB9\",\"source\":\"PDB\"}],\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"Serotype O6\"}],\"referenceNumber\":6,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (2.10 ANGSTROMS) IN COMPLEXES WITH NAD(+); UDP-N-ACETYL-ALPHA-D-GALACTOSAMINE AND UDP-GLUCOSE\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"COFACTOR\",\"SUBUNIT\",\"MUTAGENESIS OF ALA-209 AND SER-306\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/5",
  "retrieved_utc": "2026-11-01T06:25:25.367428+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f67b2500389a81025c9be1998ba5bdf0c0e6d0d7f2971007bc6e11f741355b05",
  "url": "https://rest.uniprot.org/uniprotkb/Q8KN66.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8KN66?format=txt&versions=87)

```json
{
  "entry_version": 87,
  "evidence_id": "H1",
  "excerpt": "ID   WBPP_PSEAI              Reviewed;         341 AA.\nAC   Q8KN66; Q9RHD6;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-OCT-2002, sequence version 1.\nDT   28-JAN-2026, entry version 87.\nDE   RecName: Full=UDP-N-acetyl-alpha-D-glucosaminouronate 4-epimerase {ECO:0000305};\nDE            Short=UDP-GlcNAcA 4-epimerase {ECO:0000305};\nDE            EC=5.1.3.45 {ECO:0000269|PubMed:18065759};\nDE   AltName: Full=UDP-N-acetylglucosamine C4 epimerase {ECO:0000303|PubMed:15752069};\nDE            Short=UDP-GlcNAc C4 epimerase {ECO:0000303|PubMed:10747995};\nDE            EC=5.1.3.7 {ECO:0000269|PubMed:10747995, ECO:0000269|PubMed:15016816, ECO:0000269|PubMed:15752069};\nGN   Name=wbpP {ECO:0000303|PubMed:10627048, ECO:0000303|PubMed:12057956};\nOS   Pseudomonas aeruginosa.\nOC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria;\nOC   Pseudomonadales; Pseudomonadaceae; Pseudomonas.\nOX   NCBI_TaxID=287;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:41.451179+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d549ed0cf621d2667a5b18f1c61cab90f3244af9d4301b29345d83da21267e72",
  "url": "https://rest.uniprot.org/unisave/Q8KN66?format=txt&versions=87"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8KN66?format=txt&versions=87)

```json
{
  "entry_version": 87,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=UDP-N-acetyl-alpha-D-glucosaminouronate 4-epimerase {ECO:0000305};\nDE            Short=UDP-GlcNAcA 4-epimerase {ECO:0000305};\nDE            EC=5.1.3.45 {ECO:0000269|PubMed:18065759};\nDE   AltName: Full=UDP-N-acetylglucosamine C4 epimerase {ECO:0000303|PubMed:15752069};\nDE            Short=UDP-GlcNAc C4 epimerase {ECO:0000303|PubMed:10747995};\nDE            EC=5.1.3.7 {ECO:0000269|PubMed:10747995, ECO:0000269|PubMed:15016816, ECO:0000269|PubMed:15752069};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:41.451179+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-11",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d549ed0cf621d2667a5b18f1c61cab90f3244af9d4301b29345d83da21267e72",
  "url": "https://rest.uniprot.org/unisave/Q8KN66?format=txt&versions=87"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8KN66?format=txt&versions=87)

```json
{
  "entry_version": 87,
  "evidence_id": "H3",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:AAF23998.1}\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, PATHWAY, AND DISRUPTION\nRP   PHENOTYPE.\nRC   STRAIN=ATCC 33354 / Serotype O6;\nRX   PubMed=10627048; DOI=10.1099/00221287-145-12-3505;\nRA   Belanger M., Burrows L.L., Lam J.S.;\nRT   \"Functional analysis of genes responsible for the synthesis of the B-band O\nRT   antigen of Pseudomonas aeruginosa serotype O6 lipopolysaccharide.\";\nRL   Microbiology 145:3505-3521(1999).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:41.451179+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 17-25",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d549ed0cf621d2667a5b18f1c61cab90f3244af9d4301b29345d83da21267e72",
  "url": "https://rest.uniprot.org/unisave/Q8KN66?format=txt&versions=87"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8KN66?format=txt&versions=87)

```json
{
  "entry_version": 87,
  "evidence_id": "H4",
  "excerpt": "RN   [2] {ECO:0000312|EMBL:AAM27817.1}\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA].\nRC   STRAIN=Serotype O6;\nRX   PubMed=12057956; DOI=10.1128/jb.184.13.3614-3622.2002;\nRA   Raymond C.K., Sims E.H., Kas A., Spencer D.H., Kutyavin T.V., Ivey R.G.,\nRA   Zhou Y., Kaul R., Clendenning J.B., Olson M.V.;\nRT   \"Genetic variation at the O-antigen biosynthetic locus in Pseudomonas\nRT   aeruginosa.\";\nRL   J. Bacteriol. 184:3614-3622(2002).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:41.451179+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 26-34",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d549ed0cf621d2667a5b18f1c61cab90f3244af9d4301b29345d83da21267e72",
  "url": "https://rest.uniprot.org/unisave/Q8KN66?format=txt&versions=87"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8KN66?format=txt&versions=87)

```json
{
  "entry_version": 87,
  "evidence_id": "H5",
  "excerpt": "RN   [3]\nRP   FUNCTION, CATALYTIC ACTIVITY, COFACTOR, BIOPHYSICOCHEMICAL PROPERTIES, AND\nRP   SUBUNIT.\nRC   STRAIN=Serotype O6;\nRX   PubMed=10747995; DOI=10.1074/jbc.m001171200;\nRA   Creuzenet C., Belanger M., Wakarchuk W.W., Lam J.S.;\nRT   \"Expression, purification, and biochemical characterization of WbpP, a new\nRT   UDP-GlcNAc C4 epimerase from Pseudomonas aeruginosa serotype O6.\";\nRL   J. Biol. Chem. 275:19060-19067(2000).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:41.451179+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 35-43",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d549ed0cf621d2667a5b18f1c61cab90f3244af9d4301b29345d83da21267e72",
  "url": "https://rest.uniprot.org/unisave/Q8KN66?format=txt&versions=87"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8KN66?format=txt&versions=87)

```json
{
  "entry_version": 87,
  "evidence_id": "H6",
  "excerpt": "RN   [4]\nRP   FUNCTION, CATALYTIC ACTIVITY, AND MUTAGENESIS OF GLY-102; SER-143; SER-144;\nRP   GLN-201 AND ALA-209.\nRC   STRAIN=Serotype O6;\nRX   PubMed=15752069; DOI=10.1042/bj20050263;\nRA   Demendi M., Ishiyama N., Lam J.S., Berghuis A.M., Creuzenet C.;\nRT   \"Towards a better understanding of the substrate specificity of the UDP-N-\nRT   acetylglucosamine C4 epimerase WbpP.\";\nRL   Biochem. J. 389:173-180(2005).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:41.451179+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 44-52",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d549ed0cf621d2667a5b18f1c61cab90f3244af9d4301b29345d83da21267e72",
  "url": "https://rest.uniprot.org/unisave/Q8KN66?format=txt&versions=87"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8KN66?format=txt&versions=87)

```json
{
  "entry_version": 87,
  "evidence_id": "H7",
  "excerpt": "RN   [5]\nRP   FUNCTION, CATALYTIC ACTIVITY, AND DISRUPTION PHENOTYPE.\nRC   STRAIN=PAK / Serotype O6;\nRX   PubMed=18065759; DOI=10.1074/jbc.m708894200;\nRA   Miller W.L., Matewish M.J., McNally D.J., Ishiyama N., Anderson E.M.,\nRA   Brewer D., Brisson J.R., Berghuis A.M., Lam J.S.;\nRT   \"Flagellin glycosylation in Pseudomonas aeruginosa PAK requires the O-\nRT   antigen biosynthesis enzyme WbpO.\";\nRL   J. Biol. Chem. 283:3507-3518(2008).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:41.451179+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 53-61",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d549ed0cf621d2667a5b18f1c61cab90f3244af9d4301b29345d83da21267e72",
  "url": "https://rest.uniprot.org/unisave/Q8KN66?format=txt&versions=87"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8KN66?format=txt&versions=87)

```json
{
  "entry_version": 87,
  "evidence_id": "H8",
  "excerpt": "RN   [6] {ECO:0007744|PDB:1SB8, ECO:0007744|PDB:1SB9}\nRP   X-RAY CRYSTALLOGRAPHY (2.10 ANGSTROMS) IN COMPLEXES WITH NAD(+);\nRP   UDP-N-ACETYL-ALPHA-D-GALACTOSAMINE AND UDP-GLUCOSE, FUNCTION, CATALYTIC\nRP   ACTIVITY, COFACTOR, SUBUNIT, AND MUTAGENESIS OF ALA-209 AND SER-306.\nRC   STRAIN=Serotype O6;\nRX   PubMed=15016816; DOI=10.1074/jbc.m401642200;\nRA   Ishiyama N., Creuzenet C., Lam J.S., Berghuis A.M.;\nRT   \"Crystal structure of WbpP, a genuine UDP-N-acetylglucosamine 4-epimerase\nRT   from Pseudomonas aeruginosa: substrate specificity in UDP-hexose 4-\nRT   epimerases.\";\nRL   J. Biol. Chem. 279:22635-22642(2004).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:41.451179+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 62-72",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d549ed0cf621d2667a5b18f1c61cab90f3244af9d4301b29345d83da21267e72",
  "url": "https://rest.uniprot.org/unisave/Q8KN66?format=txt&versions=87"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8KN66?format=txt&versions=87)

```json
{
  "entry_version": 87,
  "evidence_id": "H9",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=UDP-2-acetamido-2-deoxy-alpha-D-glucuronate = UDP-2-acetamido-\nCC         2-deoxy-alpha-D-galacturonate; Xref=Rhea:RHEA:81511,\nCC         ChEBI:CHEBI:65040, ChEBI:CHEBI:231899; EC=5.1.3.45;\nCC         Evidence={ECO:0000269|PubMed:18065759};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:81512;\nCC         Evidence={ECO:0000269|PubMed:18065759};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:41.451179+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 85-91",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d549ed0cf621d2667a5b18f1c61cab90f3244af9d4301b29345d83da21267e72",
  "url": "https://rest.uniprot.org/unisave/Q8KN66?format=txt&versions=87"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8KN66?format=txt&versions=87)

```json
{
  "entry_version": 87,
  "evidence_id": "H10",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=UDP-N-acetyl-alpha-D-glucosamine = UDP-N-acetyl-alpha-D-\nCC         galactosamine; Xref=Rhea:RHEA:20517, ChEBI:CHEBI:57705,\nCC         ChEBI:CHEBI:67138; EC=5.1.3.7; Evidence={ECO:0000269|PubMed:10747995,\nCC         ECO:0000269|PubMed:15016816, ECO:0000269|PubMed:15752069};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:41.451179+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 92-96",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d549ed0cf621d2667a5b18f1c61cab90f3244af9d4301b29345d83da21267e72",
  "url": "https://rest.uniprot.org/unisave/Q8KN66?format=txt&versions=87"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 145. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
