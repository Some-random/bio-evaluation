# EC_number_0112: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/EC_number_0112.txt)

**Task:** `EC_number`  
**Author key, unchanged:** **B** — 5.6.2.4

| Round | Reviewer | Key support | Transfer / lookup | Output usability (canonical status) |
|---|---|---|---|---|
| before | GPT-6 Luna | supported | lookup-dependent | usable output (valid_review) |
| before | Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | usable output (valid_review) |
| after | GPT-6 Luna | supported | reasoning-supported | usable output (valid_review) |
| after | Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | usable output (valid_review) |

**Usable output means format-valid review, not reasoning-supported or biologically correct.** A usable output can classify the question as reasoning-supported, lookup-dependent or uncertain. An output error is a problem with the saved model response; it does not count a defective benchmark question or wrong key. Each saved review is retained in full below. Labels from output errors are displayed as saved and excluded from label statistics. The author key and reviewer evidence were visible to reviewers; this is a review of answerability and key support, not a benchmark-solving score.

## Complete original question

```text
[Protein Sequence]
MDINTLLNTPDEDVLSLFTPQVARWFKEKYKVFTPPQKGAIPLIKKGKNVLVSSPTGSGKTLAAFLGILDTLIDLGYKNELNKQIYAIYISPLRALNNDMRRNLIEPLTELRNLYPDLPEISIGVRTSDTSSYEKQKMLKKPPHILITTPESFGISLVSPKFREKLSDVKWVIVDEIHELANSKRGAYLAGLLELYKSFIAKNNFVRIGLSATISPLEEVAKFLVGGNGDYEIIDARFVKPTDIQVVSPVKDLVHATEEEVNIGIYSYLVDEIKKHKTTLIFTNTRHAAERVAYKLRKMFEDQNIFDSDLVAAHHSSLSRDVRLEVEEKLKRGELKVVVSSTSLELGIDIGYIDLVTLLSSPKSVSRLLQRVGRAGHHIREVSKGRVVVVDRDDLVECTVLAKLAIDRKIDNIHVPENPLDVLTQLIVAASLITPIEKDKLYEIIKNVYNFRSLSYDEYNNVAEYLAGNYGLDSNKVYAKIRIKDGMISPKRGTRMIFFLNSGTIPDEAMIPVKMENGGYVGNLEEEFVEILAPGDIFVLAGKTYEFIRSEGNSVIVKKSEGQRPTVPSWFSEMLPLAFDSAIEIGKFRGKIAEAIMNEVPKDEVISSIMSEYNLSRFAALSIYNYVKEELLFTGGIVPTDKLLLIEVYDDDDQNRNFIFHGLYGRRTVDALSRAIAYIISKDLNMDVRIAITDNGFAITVPGKQEYEISKVFDKLEPDKMYEILSDVILRTEMIKRRFRHCAERSFMLLKRYKGRETSIDRRQINSEVLLGVVRQIEHFPVLKETVREILEDYMDIKRAIEIVEKIRNGDIKVATIGPNQVPSPFAHNILVKQYTDVVLAEDKRELLKELHNKVIEFLRNKGIDIDLEYTEAGIK

[Multiple Choices]
A. 5.6.1.1
B. 5.6.2.4
C. 3.2.2.19
D. 5.6.2.1
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

## Four saved visible reviews

## Before: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The exact sequence matches the UniProt entry for Sulfolobus acidocaldarius Lhr-Core. That entry assigns EC 5.6.2.4 and reports ATP-coupled duplex-DNA unwinding, citing experimental evidence (PubMed 26148716). The primary paper was not independently reviewed here.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence’s nucleotide-binding/helicase features can support an ATP-dependent helicase inference and favor the helicase-class choices over unrelated enzyme classes, but they do not establish the exact EC subclass.


**Missing item-specific fact**

> The protein-specific evidence that this Lhr-Core helicase couples ATP hydrolysis to duplex-DNA unwinding, assigned EC 5.6.2.4, rather than the alternative helicase EC 5.6.2.1.


**Reason**

> The exact four-part EC choice depends on the specific substrate/activity classification, which is not supplied in the question. Recognizing the sequence or retrieving its annotation would supply that missing fact.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> Both are helicase-class EC choices; the sequence supports a helicase inference but, without protein-specific functional information, does not distinguish these precise subclasses. The reviewer-only evidence supports B for this protein.


### Important caveats

- The sequence-to-entry match is exact, but the accession and database annotation were not supplied to the evaluated model.
- The supporting annotation cites experimental evidence; the cited primary study was not independently assessed.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence’s nucleotide-binding/helicase features can support an ATP-dependent helicase inference and favor the helicase-class choices over unrelated enzyme classes, but they do not establish the exact EC subclass.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific evidence that this Lhr-Core helicase couples ATP hydrolysis to duplex-DNA unwinding, assigned EC 5.6.2.4, rather than the alternative helicase EC 5.6.2.1.",
    "reason": "The exact four-part EC choice depends on the specific substrate/activity classification, which is not supplied in the question. Recognizing the sequence or retrieving its annotation would supply that missing fact."
  },
  "case_id": "EC_number_0112",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry for Sulfolobus acidocaldarius Lhr-Core. That entry assigns EC 5.6.2.4 and reports ATP-coupled duplex-DNA unwinding, citing experimental evidence (PubMed 26148716). The primary paper was not independently reviewed here."
  },
  "important_caveats": [
    "The sequence-to-entry match is exact, but the accession and database annotation were not supplied to the evaluated model.",
    "The supporting annotation cites experimental evidence; the cited primary study was not independently assessed."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "Both are helicase-class EC choices; the sequence supports a helicase inference but, without protein-specific functional information, does not distinguish these precise subclasses. The reviewer-only evidence supports B for this protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0112",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry for Sulfolobus acidocaldarius Lhr-Core. That entry assigns EC 5.6.2.4 and reports ATP-coupled duplex-DNA unwinding, citing experimental evidence (PubMed 26148716). The primary paper was not independently reviewed here.",
    "evidence_ids": ["C1", "C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence’s nucleotide-binding/helicase features can support an ATP-dependent helicase inference and favor the helicase-class choices over unrelated enzyme classes, but they do not establish the exact EC subclass.",
    "missing_item_specific_fact": "The protein-specific evidence that this Lhr-Core helicase couples ATP hydrolysis to duplex-DNA unwinding, assigned EC 5.6.2.4, rather than the alternative helicase EC 5.6.2.1.",
    "reason": "The exact four-part EC choice depends on the specific substrate/activity classification, which is not supplied in the question. Recognizing the sequence or retrieving its annotation would supply that missing fact."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "Both are helicase-class EC choices; the sequence supports a helicase inference but, without protein-specific functional information, does not distinguish these precise subclasses. The reviewer-only evidence supports B for this protein."
  },
  "important_caveats": [
    "The sequence-to-entry match is exact, but the accession and database annotation were not supplied to the evaluated model.",
    "The supporting annotation cites experimental evidence; the cited primary study was not independently assessed."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q4J8R1 (LHRC_SULAC) assigns EC 5.6.2.4 to this exact 876-aa sequence (SHA256 match confirmed) with evidence code ECO:0000269 (inferred from direct assay) from PubMed:26148716 (van Wolferen et al., J. Bacteriol. 2015). The catalytic activity is described as coupling ATP hydrolysis with unwinding of duplex DNA in the 3'→5' direction. The Swiss-Prot reviewed annotation and experimental evidence code strongly support the expected answer.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains a clear Walker A / P-loop motif (GSGKTLAAFLGILDT), which supports classification as an ATP-dependent helicase and effectively eliminates choice C (3.2.2.19, a glycosylase that lacks P-loop motifs). However, the remaining choices A (5.6.1.1, 5'→3' DNA helicase), B (5.6.2.4, 3'→5' DNA helicase of a specific subfamily), and D (5.6.2.1, 3'→5' DNA helicase of another subfamily) all describe ATP-dependent DNA helicases. Distinguishing among them requires knowing the specific helicase superfamily/subfamily assignment and translocation polarity, which is not derivable from general sequence features alone.


**Missing item-specific fact**

> The specific helicase subfamily identity (Lhr-Core, an archaeal 3'→5' DNA helicase) and the EC classification boundary between 5.6.2.1 and 5.6.2.4, which depends on knowing that this particular protein belongs to the subfamily assigned EC 5.6.2.4 rather than 5.6.2.1. This is a database annotation fact not inferable from the sequence by general biological reasoning.


**Reason**

> While the Walker A motif permits elimination of the glycosylase option (C), the critical discrimination among the three helicase EC numbers (A, B, D) depends on identifying the exact helicase subfamily and its assigned EC number. The EC 5.6.2.4 vs 5.6.2.1 distinction is a fine-grained taxonomic assignment within the 3'→5' DNA helicase class that requires item-specific database knowledge rather than general biochemical reasoning from the sequence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Choice C is clearly eliminable by the presence of the Walker A P-loop motif. Choices A, B, and D are all helicase EC numbers but differ in directionality and subfamily assignment. Without database knowledge, a solver cannot reliably distinguish 5.6.2.4 from 5.6.2.1 or from 5.6.1.1 based on sequence alone, but the author's key is uniquely correct per the experimental annotation.


### Important caveats

- The identity of the protein (Q4J8R1, Lhr-Core) was inferred from reviewer-only metadata and was not provided to the evaluated model.
- The EC 5.6.2.4 annotation carries evidence code ECO:0000269 (direct assay), indicating experimental support rather than purely computational transfer.
- The Walker A motif provides partial reasoning (eliminating the glycosylase), but the precise 4-digit EC number assignment among helicase subfamilies remains lookup-dependent.
- EC 5.6.2.4 is a relatively recently defined EC number; its boundaries with 5.6.2.1 may reflect taxonomic curation decisions not obvious from sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a clear Walker A / P-loop motif (GSGKTLAAFLGILDT), which supports classification as an ATP-dependent helicase and effectively eliminates choice C (3.2.2.19, a glycosylase that lacks P-loop motifs). However, the remaining choices A (5.6.1.1, 5'→3' DNA helicase), B (5.6.2.4, 3'→5' DNA helicase of a specific subfamily), and D (5.6.2.1, 3'→5' DNA helicase of another subfamily) all describe ATP-dependent DNA helicases. Distinguishing among them requires knowing the specific helicase superfamily/subfamily assignment and translocation polarity, which is not derivable from general sequence features alone.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific helicase subfamily identity (Lhr-Core, an archaeal 3'→5' DNA helicase) and the EC classification boundary between 5.6.2.1 and 5.6.2.4, which depends on knowing that this particular protein belongs to the subfamily assigned EC 5.6.2.4 rather than 5.6.2.1. This is a database annotation fact not inferable from the sequence by general biological reasoning.",
    "reason": "While the Walker A motif permits elimination of the glycosylase option (C), the critical discrimination among the three helicase EC numbers (A, B, D) depends on identifying the exact helicase subfamily and its assigned EC number. The EC 5.6.2.4 vs 5.6.2.1 distinction is a fine-grained taxonomic assignment within the 3'→5' DNA helicase class that requires item-specific database knowledge rather than general biochemical reasoning from the sequence."
  },
  "case_id": "EC_number_0112",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "H1",
      "H2",
      "H3",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q4J8R1 (LHRC_SULAC) assigns EC 5.6.2.4 to this exact 876-aa sequence (SHA256 match confirmed) with evidence code ECO:0000269 (inferred from direct assay) from PubMed:26148716 (van Wolferen et al., J. Bacteriol. 2015). The catalytic activity is described as coupling ATP hydrolysis with unwinding of duplex DNA in the 3'→5' direction. The Swiss-Prot reviewed annotation and experimental evidence code strongly support the expected answer."
  },
  "important_caveats": [
    "The identity of the protein (Q4J8R1, Lhr-Core) was inferred from reviewer-only metadata and was not provided to the evaluated model.",
    "The EC 5.6.2.4 annotation carries evidence code ECO:0000269 (direct assay), indicating experimental support rather than purely computational transfer.",
    "The Walker A motif provides partial reasoning (eliminating the glycosylase), but the precise 4-digit EC number assignment among helicase subfamilies remains lookup-dependent.",
    "EC 5.6.2.4 is a relatively recently defined EC number; its boundaries with 5.6.2.1 may reflect taxonomic curation decisions not obvious from sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choice C is clearly eliminable by the presence of the Walker A P-loop motif. Choices A, B, and D are all helicase EC numbers but differ in directionality and subfamily assignment. Without database knowledge, a solver cannot reliably distinguish 5.6.2.4 from 5.6.2.1 or from 5.6.1.1 based on sequence alone, but the author's key is uniquely correct per the experimental annotation."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0112",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q4J8R1 (LHRC_SULAC) assigns EC 5.6.2.4 to this exact 876-aa sequence (SHA256 match confirmed) with evidence code ECO:0000269 (inferred from direct assay) from PubMed:26148716 (van Wolferen et al., J. Bacteriol. 2015). The catalytic activity is described as coupling ATP hydrolysis with unwinding of duplex DNA in the 3'→5' direction. The Swiss-Prot reviewed annotation and experimental evidence code strongly support the expected answer.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H1", "H2", "H3", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains a clear Walker A / P-loop motif (GSGKTLAAFLGILDT), which supports classification as an ATP-dependent helicase and effectively eliminates choice C (3.2.2.19, a glycosylase that lacks P-loop motifs). However, the remaining choices A (5.6.1.1, 5'→3' DNA helicase), B (5.6.2.4, 3'→5' DNA helicase of a specific subfamily), and D (5.6.2.1, 3'→5' DNA helicase of another subfamily) all describe ATP-dependent DNA helicases. Distinguishing among them requires knowing the specific helicase superfamily/subfamily assignment and translocation polarity, which is not derivable from general sequence features alone.",
    "missing_item_specific_fact": "The specific helicase subfamily identity (Lhr-Core, an archaeal 3'→5' DNA helicase) and the EC classification boundary between 5.6.2.1 and 5.6.2.4, which depends on knowing that this particular protein belongs to the subfamily assigned EC 5.6.2.4 rather than 5.6.2.1. This is a database annotation fact not inferable from the sequence by general biological reasoning.",
    "reason": "While the Walker A motif permits elimination of the glycosylase option (C), the critical discrimination among the three helicase EC numbers (A, B, D) depends on identifying the exact helicase subfamily and its assigned EC number. The EC 5.6.2.4 vs 5.6.2.1 distinction is a fine-grained taxonomic assignment within the 3'→5' DNA helicase class that requires item-specific database knowledge rather than general biochemical reasoning from the sequence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choice C is clearly eliminable by the presence of the Walker A P-loop motif. Choices A, B, and D are all helicase EC numbers but differ in directionality and subfamily assignment. Without database knowledge, a solver cannot reliably distinguish 5.6.2.4 from 5.6.2.1 or from 5.6.1.1 based on sequence alone, but the author's key is uniquely correct per the experimental annotation."
  },
  "important_caveats": [
    "The identity of the protein (Q4J8R1, Lhr-Core) was inferred from reviewer-only metadata and was not provided to the evaluated model.",
    "The EC 5.6.2.4 annotation carries evidence code ECO:0000269 (direct assay), indicating experimental support rather than purely computational transfer.",
    "The Walker A motif provides partial reasoning (eliminating the glycosylase), but the precise 4-digit EC number assignment among helicase subfamilies remains lookup-dependent.",
    "EC 5.6.2.4 is a relatively recently defined EC number; its boundaries with 5.6.2.1 may reflect taxonomic curation decisions not obvious from sequence."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched UniProt entry reports EC 5.6.2.4 and cites experimental evidence for coupling ATP hydrolysis to duplex-DNA unwinding. This supports the keyed answer for the supplied sequence.

Citations as saved: [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a P-loop NTPase motif (including a GxxxxGKT pattern) and additional conserved ATPase/helicase-like features, supporting an ATP-dependent nucleic-acid motor rather than the unrelated isomerase or nucleoside hydrolase choices. Transferable recognition of helicase-family sequence features favors the DNA-helicase EC choice, 5.6.2.4, over the other 5.6.2 option.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level inference from conserved sequence motifs meaningfully distinguishes the offered DNA-helicase classification. The sequence alone may not establish every biochemical detail, but the alternatives do not require that degree of certainty.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The offered alternatives do not present multiple comparably defensible classifications given the sequence's ATPase/helicase-like features.


### Important caveats

- The reviewer-only record provides stronger, experimental support for the EC assignment than sequence analysis alone; the sequence-based inference is probabilistic.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a P-loop NTPase motif (including a GxxxxGKT pattern) and additional conserved ATPase/helicase-like features, supporting an ATP-dependent nucleic-acid motor rather than the unrelated isomerase or nucleoside hydrolase choices. Transferable recognition of helicase-family sequence features favors the DNA-helicase EC choice, 5.6.2.4, over the other 5.6.2 option.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from conserved sequence motifs meaningfully distinguishes the offered DNA-helicase classification. The sequence alone may not establish every biochemical detail, but the alternatives do not require that degree of certainty."
  },
  "case_id": "EC_number_0112",
  "expected_answer_check": {
    "evidence_ids": [
      "C5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry reports EC 5.6.2.4 and cites experimental evidence for coupling ATP hydrolysis to duplex-DNA unwinding. This supports the keyed answer for the supplied sequence."
  },
  "important_caveats": [
    "The reviewer-only record provides stronger, experimental support for the EC assignment than sequence analysis alone; the sequence-based inference is probabilistic."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The offered alternatives do not present multiple comparably defensible classifications given the sequence's ATPase/helicase-like features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0112",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry reports EC 5.6.2.4 and cites experimental evidence for coupling ATP hydrolysis to duplex-DNA unwinding. This supports the keyed answer for the supplied sequence.",
    "evidence_ids": ["C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a P-loop NTPase motif (including a GxxxxGKT pattern) and additional conserved ATPase/helicase-like features, supporting an ATP-dependent nucleic-acid motor rather than the unrelated isomerase or nucleoside hydrolase choices. Transferable recognition of helicase-family sequence features favors the DNA-helicase EC choice, 5.6.2.4, over the other 5.6.2 option.",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from conserved sequence motifs meaningfully distinguishes the offered DNA-helicase classification. The sequence alone may not establish every biochemical detail, but the alternatives do not require that degree of certainty."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The offered alternatives do not present multiple comparably defensible classifications given the sequence's ATPase/helicase-like features."
  },
  "important_caveats": [
    "The reviewer-only record provides stronger, experimental support for the EC assignment than sequence analysis alone; the sequence-based inference is probabilistic."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt Q4J8R1 (LHRC_SULAC, 876 AA, sequence matched) annotates EC 5.6.2.4 with ECO:0000269 (in vitro experimental evidence from PubMed:26148716). The catalytic activity is 'Couples ATP hydrolysis with the unwinding of duplex DNA by translocating in the 3'-5' direction,' which is the definition of EC 5.6.2.4. The protein is named 'ATP-dependent helicase Lhr-Core' / 'DNA 3'-5' helicase.' The experimental evidence code and the specific 3'-5' translocation direction confirm the EC assignment.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a canonical Walker A motif (SSPTGSGKTLAAFLGILDTL, ~residues 55-75) and Walker B-like motifs (VVSSTSLELGIDIGYIDL, ~residues 460-480), plus multiple RecA-like domains and an overall ~876 AA architecture. This multi-domain RecA-fold arrangement with the specific GSGKT Walker A and the characteristic domain spacing is consistent with the RecQ superfamily of helicases. RecQ-family helicases are well-established 3'-5' DNA translocases (EC 5.6.2.4), in contrast to PcrA/UvrD-type helicases (EC 5.6.2.1, 5'-3'). The Walker A/B motifs and RecA-like architecture eliminate EC 3.2.2.19 (NAD+ glycohydrolase, a hydrolase with no helicase motifs). The topoisomerase EC 5.6.1.1 is eliminated because topoisomerases use a TOPRIM/active-site-tyrosine mechanism rather than the Walker A/B ATPase architecture seen here. The remaining distinction between B (3'-5') and D (5'-3') rests on the RecQ-family assignment: the GSGKT Walker A embedded in a 'SSPTGSGKT' context, the multiple RecA-like domains, the ~876 AA size, and the archaeal context are all hallmarks of RecQ-like helicases, which are characteristically 3'-5' DNA helicases.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can identify the Walker A/B motifs and multi-RecA-domain architecture to classify this as a superfamily helicase, then recognize the specific motif arrangement (GSGKT Walker A, multiple RecA-like domains, ~876 AA) as RecQ-family. The well-established family-level regularity that RecQ helicases translocate 3'-5' distinguishes EC 5.6.2.4 from EC 5.6.2.1 (5'-3'). While the B-vs-D distinction is the hardest part and relies on family-level inference rather than a single unambiguous sequence feature, the RecQ assignment is a transferable, well-supported pattern from many characterized homologs.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The Walker A/B motifs and RecA-like architecture clearly eliminate C (hydrolase) and A (topoisomerase). The B-vs-D distinction is the primary challenge, but the RecQ-family architecture provides a credible inference toward 3'-5' directionality. No other option is equally well-supported by the sequence features.


### Important caveats

- Distinguishing 3'-5' (EC 5.6.2.4) from 5'-3' (EC 5.6.2.1) DNA helicases purely from sequence is inherently difficult; the argument relies on RecQ-family assignment, which is a probabilistic family-level inference rather than a direct readout of translocation polarity.
- The Lhr-Core protein is an archaeal RecQ-like helicase; the RecQ-to-3'-5' association is well-established in eukaryotic and bacterial homologs but the specific archaeal Lhr family may have nuances.
- The experimental evidence (ECO:0000269) for the 3'-5' direction was established in vitro (PubMed:26148716); a model working from sequence alone must rely on family analogy.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a canonical Walker A motif (SSPTGSGKTLAAFLGILDTL, ~residues 55-75) and Walker B-like motifs (VVSSTSLELGIDIGYIDL, ~residues 460-480), plus multiple RecA-like domains and an overall ~876 AA architecture. This multi-domain RecA-fold arrangement with the specific GSGKT Walker A and the characteristic domain spacing is consistent with the RecQ superfamily of helicases. RecQ-family helicases are well-established 3'-5' DNA translocases (EC 5.6.2.4), in contrast to PcrA/UvrD-type helicases (EC 5.6.2.1, 5'-3'). The Walker A/B motifs and RecA-like architecture eliminate EC 3.2.2.19 (NAD+ glycohydrolase, a hydrolase with no helicase motifs). The topoisomerase EC 5.6.1.1 is eliminated because topoisomerases use a TOPRIM/active-site-tyrosine mechanism rather than the Walker A/B ATPase architecture seen here. The remaining distinction between B (3'-5') and D (5'-3') rests on the RecQ-family assignment: the GSGKT Walker A embedded in a 'SSPTGSGKT' context, the multiple RecA-like domains, the ~876 AA size, and the archaeal context are all hallmarks of RecQ-like helicases, which are characteristically 3'-5' DNA helicases.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can identify the Walker A/B motifs and multi-RecA-domain architecture to classify this as a superfamily helicase, then recognize the specific motif arrangement (GSGKT Walker A, multiple RecA-like domains, ~876 AA) as RecQ-family. The well-established family-level regularity that RecQ helicases translocate 3'-5' distinguishes EC 5.6.2.4 from EC 5.6.2.1 (5'-3'). While the B-vs-D distinction is the hardest part and relies on family-level inference rather than a single unambiguous sequence feature, the RecQ assignment is a transferable, well-supported pattern from many characterized homologs."
  },
  "case_id": "EC_number_0112",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H2",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "UniProt Q4J8R1 (LHRC_SULAC, 876 AA, sequence matched) annotates EC 5.6.2.4 with ECO:0000269 (in vitro experimental evidence from PubMed:26148716). The catalytic activity is 'Couples ATP hydrolysis with the unwinding of duplex DNA by translocating in the 3'-5' direction,' which is the definition of EC 5.6.2.4. The protein is named 'ATP-dependent helicase Lhr-Core' / 'DNA 3'-5' helicase.' The experimental evidence code and the specific 3'-5' translocation direction confirm the EC assignment."
  },
  "important_caveats": [
    "Distinguishing 3'-5' (EC 5.6.2.4) from 5'-3' (EC 5.6.2.1) DNA helicases purely from sequence is inherently difficult; the argument relies on RecQ-family assignment, which is a probabilistic family-level inference rather than a direct readout of translocation polarity.",
    "The Lhr-Core protein is an archaeal RecQ-like helicase; the RecQ-to-3'-5' association is well-established in eukaryotic and bacterial homologs but the specific archaeal Lhr family may have nuances.",
    "The experimental evidence (ECO:0000269) for the 3'-5' direction was established in vitro (PubMed:26148716); a model working from sequence alone must rely on family analogy."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The Walker A/B motifs and RecA-like architecture clearly eliminate C (hydrolase) and A (topoisomerase). The B-vs-D distinction is the primary challenge, but the RecQ-family architecture provides a credible inference toward 3'-5' directionality. No other option is equally well-supported by the sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0112",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt Q4J8R1 (LHRC_SULAC, 876 AA, sequence matched) annotates EC 5.6.2.4 with ECO:0000269 (in vitro experimental evidence from PubMed:26148716). The catalytic activity is 'Couples ATP hydrolysis with the unwinding of duplex DNA by translocating in the 3'-5' direction,' which is the definition of EC 5.6.2.4. The protein is named 'ATP-dependent helicase Lhr-Core' / 'DNA 3'-5' helicase.' The experimental evidence code and the specific 3'-5' translocation direction confirm the EC assignment.",
    "evidence_ids": ["C4", "C5", "C6", "H2", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a canonical Walker A motif (SSPTGSGKTLAAFLGILDTL, ~residues 55-75) and Walker B-like motifs (VVSSTSLELGIDIGYIDL, ~residues 460-480), plus multiple RecA-like domains and an overall ~876 AA architecture. This multi-domain RecA-fold arrangement with the specific GSGKT Walker A and the characteristic domain spacing is consistent with the RecQ superfamily of helicases. RecQ-family helicases are well-established 3'-5' DNA translocases (EC 5.6.2.4), in contrast to PcrA/UvrD-type helicases (EC 5.6.2.1, 5'-3'). The Walker A/B motifs and RecA-like architecture eliminate EC 3.2.2.19 (NAD+ glycohydrolase, a hydrolase with no helicase motifs). The topoisomerase EC 5.6.1.1 is eliminated because topoisomerases use a TOPRIM/active-site-tyrosine mechanism rather than the Walker A/B ATPase architecture seen here. The remaining distinction between B (3'-5') and D (5'-3') rests on the RecQ-family assignment: the GSGKT Walker A embedded in a 'SSPTGSGKT' context, the multiple RecA-like domains, the ~876 AA size, and the archaeal context are all hallmarks of RecQ-like helicases, which are characteristically 3'-5' DNA helicases.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can identify the Walker A/B motifs and multi-RecA-domain architecture to classify this as a superfamily helicase, then recognize the specific motif arrangement (GSGKT Walker A, multiple RecA-like domains, ~876 AA) as RecQ-family. The well-established family-level regularity that RecQ helicases translocate 3'-5' distinguishes EC 5.6.2.4 from EC 5.6.2.1 (5'-3'). While the B-vs-D distinction is the hardest part and relies on family-level inference rather than a single unambiguous sequence feature, the RecQ assignment is a transferable, well-supported pattern from many characterized homologs."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The Walker A/B motifs and RecA-like architecture clearly eliminate C (hydrolase) and A (topoisomerase). The B-vs-D distinction is the primary challenge, but the RecQ-family architecture provides a credible inference toward 3'-5' directionality. No other option is equally well-supported by the sequence features."
  },
  "important_caveats": [
    "Distinguishing 3'-5' (EC 5.6.2.4) from 5'-3' (EC 5.6.2.1) DNA helicases purely from sequence is inherently difficult; the argument relies on RecQ-family assignment, which is a probabilistic family-level inference rather than a direct readout of translocation polarity.",
    "The Lhr-Core protein is an archaeal RecQ-like helicase; the RecQ-to-3'-5' association is well-established in eukaryotic and bacterial homologs but the specific archaeal Lhr family may have nuances.",
    "The experimental evidence (ECO:0000269) for the 3'-5' direction was established in vitro (PubMed:26148716); a model working from sequence alone must rely on family analogy."
  ]
}
```

</details>

## Existing project source checks of the old Luna review only

These unchanged notes concern the earlier Luna claims. They do not validate either new review or the old Qwen review. No new scientific adjudication was performed.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Complete reviewer-only evidence and qualifications

All excerpts supplied in the original and revised reviewer user message follow. This material was not available to the original evaluated model. Accession identity came from dataset image-path metadata. Source support and transferable discrimination are separate judgments.

**Applicability metadata, unchanged:**

```json
{
  "requested_accession": "Q4J8R1",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "599d79310ec23c778d237f1bab50ccc689a4391422729c4b4332423238d84095",
  "benchmark_sequence_length": 876,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 120,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2005-08-02",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "5ddd2fdfa837dd562dc14520d20c460d760536e004fc18e055f36fb419e215a4",
  "current_source_sequence_sha256": "599d79310ec23c778d237f1bab50ccc689a4391422729c4b4332423238d84095",
  "current_source_sequence_length": 876,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 118,
  "selected_historical_version": {
    "accession": "Q4J8R1",
    "database": "Swiss-Prot",
    "entryVersion": 118,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "LHRC_SULAC",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "e13a189773cd9bc8187d4ff73efc59a3b0cfa535f19e4a03d9e5c43501c05855",
  "selected_historical_source_sequence_sha256": "599d79310ec23c778d237f1bab50ccc689a4391422729c4b4332423238d84095",
  "selected_historical_source_sequence_length": 876,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 118,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "actual_author_source_snapshot": "unknown",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed."
}
```

**Qualifications, unchanged:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4J8R1.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q4J8R1.json",
  "source_sha256": "5ddd2fdfa837dd562dc14520d20c460d760536e004fc18e055f36fb419e215a4",
  "retrieved_utc": "2026-11-01T06:25:21.183785+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"Q4J8R1\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4J8R1.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q4J8R1.json",
  "source_sha256": "5ddd2fdfa837dd562dc14520d20c460d760536e004fc18e055f36fb419e215a4",
  "retrieved_utc": "2026-11-01T06:25:21.183785+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":120,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2005-08-02\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4J8R1.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q4J8R1.json",
  "source_sha256": "5ddd2fdfa837dd562dc14520d20c460d760536e004fc18e055f36fb419e215a4",
  "retrieved_utc": "2026-11-01T06:25:21.183785+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"lineage\":[\"Archaea\",\"Thermoproteota\",\"Thermoprotei\",\"Sulfolobales\",\"Sulfolobaceae\",\"Sulfolobus\"],\"scientificName\":\"Sulfolobus acidocaldarius (strain ATCC 33909 / DSM 639 / JCM 8929 / NBRC 15157 / NCIMB 11770)\",\"taxonId\":330779}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4J8R1.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q4J8R1.json",
  "source_sha256": "5ddd2fdfa837dd562dc14520d20c460d760536e004fc18e055f36fb419e215a4",
  "retrieved_utc": "2026-11-01T06:25:21.183785+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"DNA 3'-5' helicase Lhr-Core\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"26148716\",\"source\":\"PubMed\"}],\"value\":\"DNA 3'-5' helicase Saci_1500\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"26148716\",\"source\":\"PubMed\"}],\"value\":\"5.6.2.4\"}],\"fullName\":{\"value\":\"ATP-dependent helicase Lhr-Core\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4J8R1.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q4J8R1.json",
  "source_sha256": "5ddd2fdfa837dd562dc14520d20c460d760536e004fc18e055f36fb419e215a4",
  "retrieved_utc": "2026-11-01T06:25:21.183785+00:00",
  "json_pointer": "/comments/1",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"5.6.2.4\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"26148716\",\"source\":\"PubMed\"}],\"name\":\"Couples ATP hydrolysis with the unwinding of duplex DNA by translocating in the 3'-5' direction.\"}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4J8R1.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q4J8R1.json",
  "source_sha256": "5ddd2fdfa837dd562dc14520d20c460d760536e004fc18e055f36fb419e215a4",
  "retrieved_utc": "2026-11-01T06:25:21.183785+00:00",
  "json_pointer": "/comments/2",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"5.6.2.4\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"26148716\",\"source\":\"PubMed\"}],\"name\":\"ATP + H2O = ADP + phosphate + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:13065\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:30616\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:43474\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:456216\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4J8R1.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q4J8R1.json",
  "source_sha256": "5ddd2fdfa837dd562dc14520d20c460d760536e004fc18e055f36fb419e215a4",
  "retrieved_utc": "2026-11-01T06:25:21.183785+00:00",
  "json_pointer": "/references/1",
  "excerpt": "{\"citation\":{\"authors\":[\"van Wolferen M.\",\"Ma X.\",\"Albers S.V.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"26148716\"},{\"database\":\"DOI\",\"id\":\"10.1128/jb.00344-15\"}],\"citationType\":\"journal article\",\"firstPage\":\"2941\",\"id\":\"26148716\",\"journal\":\"J. Bacteriol.\",\"lastPage\":\"2951\",\"publicationDate\":\"2015\",\"title\":\"DNA Processing Proteins Involved in the UV-Induced Stress Response of Sulfolobales.\",\"volume\":\"197\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"ATCC 33909 / DSM 639 / JCM 8929 / NBRC 15157 / NCIMB 11770\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION AS A HELICASE\",\"CATALYTIC ACTIVITY\",\"DISRUPTION PHENOTYPE\",\"DNA-BINDING\",\"MUTAGENESIS OF LYS-60\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4J8R1?format=txt&versions=118)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q4J8R1?format=txt&versions=118",
  "source_sha256": "e13a189773cd9bc8187d4ff73efc59a3b0cfa535f19e4a03d9e5c43501c05855",
  "retrieved_utc": "2026-11-01T06:28:33.887619+00:00",
  "source_locator": "lines 1-15",
  "excerpt": "ID   LHRC_SULAC              Reviewed;         876 AA.\nAC   Q4J8R1;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   02-AUG-2005, sequence version 1.\nDT   28-JAN-2026, entry version 118.\nDE   RecName: Full=ATP-dependent helicase Lhr-Core;\nDE            EC=5.6.2.4 {ECO:0000269|PubMed:26148716};\nDE   AltName: Full=DNA 3'-5' helicase Lhr-Core {ECO:0000305};\nDE   AltName: Full=DNA 3'-5' helicase Saci_1500 {ECO:0000303|PubMed:26148716};\nGN   OrderedLocusNames=Saci_1500 {ECO:0000312|EMBL:AAY80821.1};\nOS   Sulfolobus acidocaldarius (strain ATCC 33909 / DSM 639 / JCM 8929 / NBRC\nOS   15157 / NCIMB 11770).\nOC   Archaea; Thermoproteota; Thermoprotei; Sulfolobales; Sulfolobaceae;\nOC   Sulfolobus.\nOX   NCBI_TaxID=330779;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 118,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4J8R1?format=txt&versions=118)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q4J8R1?format=txt&versions=118",
  "source_sha256": "e13a189773cd9bc8187d4ff73efc59a3b0cfa535f19e4a03d9e5c43501c05855",
  "retrieved_utc": "2026-11-01T06:28:33.887619+00:00",
  "source_locator": "lines 6-9",
  "excerpt": "DE   RecName: Full=ATP-dependent helicase Lhr-Core;\nDE            EC=5.6.2.4 {ECO:0000269|PubMed:26148716};\nDE   AltName: Full=DNA 3'-5' helicase Lhr-Core {ECO:0000305};\nDE   AltName: Full=DNA 3'-5' helicase Saci_1500 {ECO:0000303|PubMed:26148716};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 118,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4J8R1?format=txt&versions=118)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q4J8R1?format=txt&versions=118",
  "source_sha256": "e13a189773cd9bc8187d4ff73efc59a3b0cfa535f19e4a03d9e5c43501c05855",
  "retrieved_utc": "2026-11-01T06:28:33.887619+00:00",
  "source_locator": "lines 25-33",
  "excerpt": "RN   [2]\nRP   FUNCTION AS A HELICASE, CATALYTIC ACTIVITY, DISRUPTION PHENOTYPE,\nRP   DNA-BINDING, AND MUTAGENESIS OF LYS-60.\nRC   STRAIN=ATCC 33909 / DSM 639 / JCM 8929 / NBRC 15157 / NCIMB 11770;\nRX   PubMed=26148716; DOI=10.1128/jb.00344-15;\nRA   van Wolferen M., Ma X., Albers S.V.;\nRT   \"DNA Processing Proteins Involved in the UV-Induced Stress Response of\nRT   Sulfolobales.\";\nRL   J. Bacteriol. 197:2941-2951(2015).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 118,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4J8R1?format=txt&versions=118)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q4J8R1?format=txt&versions=118",
  "source_sha256": "e13a189773cd9bc8187d4ff73efc59a3b0cfa535f19e4a03d9e5c43501c05855",
  "retrieved_utc": "2026-11-01T06:28:33.887619+00:00",
  "source_locator": "lines 45-48",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=Couples ATP hydrolysis with the unwinding of duplex DNA by\nCC         translocating in the 3'-5' direction.; EC=5.6.2.4;\nCC         Evidence={ECO:0000269|PubMed:26148716};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 118,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4J8R1?format=txt&versions=118)

```json
{
  "evidence_id": "H5",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q4J8R1?format=txt&versions=118",
  "source_sha256": "e13a189773cd9bc8187d4ff73efc59a3b0cfa535f19e4a03d9e5c43501c05855",
  "retrieved_utc": "2026-11-01T06:28:33.887619+00:00",
  "source_locator": "lines 49-53",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=ATP + H2O = ADP + phosphate + H(+); Xref=Rhea:RHEA:13065,\nCC         ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:30616,\nCC         ChEBI:CHEBI:43474, ChEBI:CHEBI:456216; EC=5.6.2.4;\nCC         Evidence={ECO:0000305|PubMed:26148716};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 118,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 112. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
