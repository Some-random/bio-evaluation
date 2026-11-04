# transmembrane_0087

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/transmembrane_0087.txt)

**Task:** `transmembrane`  
**Expected answer:** **D** — 1599..1619; 1662..1682; 1704..1724; 1763..1783; 1796..1816

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MKFKKELINILALIFVLKKNIFAQSICPTGYQMTQGSCTAIQCPNGQYYDSNLGLCANCDQACSACNYYPTYCTQCQNGFYLYQNQCLTQCPQAQTYVSCSGSSCICQACDSSCTQCFGNKNTQCLACSVGFYYNQINSSCLKQCEDGYTQQIVNIGASQQLLCIPCDNNCRTCSQTNAQQCLTCKDNMYLNTATNQCVSTCPQLQYKINGICKICPTGCQTCYNTNPSNPSTVESCLSCVSGYFLDIENQLCVKNCVSGYVVDAATQRCLPCNATCKNCSDQTNQGCLQCQNGYSLTSGSPSSCQNNCPNGNYQNSSLCLSCNTACSECFGADNQQCTACKTGYYLYKTQCLVICPVGFYTFARQYADPLKQPICDYCPNEMEQCEQDKSNFDLIKPILCKRGYYLYNGTCVKTCPDQTYYQDEATRSCLPCVFPCQTCLSASVCLTCATYTPNGQVQGQTYIFAQITYNGPQGTVFQQNCVPACPKGFYQNSKNNSCQVCNQQCQTCQGPAQTDCITCQIYDSNNMLFKYNNQCYYTCPSSQNNPMYGDKTTQACLPCSQECSSCFNGNNKSCYSCMNGYFLEYLKPECKSFCASDGTYMNSSTNQCSLCGFGCSSCTNGTFNSCISCLNGYYLQQNYNVCYPCPQQCASCTDMNTCQSCNQGYFLYSQTNSCVQQCPLIGFYVDTTQQACIPCDASCLECYGGANNQCISCPKGSYLKTDGTCQQCSQCSSNNECLGPNITDCLNQPICKPGQYLYDGQCLTCFPYCSTCSGTTYDSCISCQTTTDYTLLFDVCKKKVSQTDTQCDIGFYYDSVNKQCYSCHQNCIQCFGKSSSQCTKCSSGYLLHLDITTCSSTCLDGYYQQDPSIPQCSPCLYNCINGCSSGYQFLLGLCFTQCPFGTTAQKENCSFNSKPSIQFAQNLGNSVNNNSQTISLQLLVYSKNLFSIKWRLFTGNTDISNGPIQSYIQNRFDYIVFPPKSLQSNTQYTIQASILDLANNCQNENDCMVQQTFQTMNAITKGNFNIEINSAYLQLTLIISGWLFNSVPDNISFDLYVKLTGNDYFFFDKGQNYQDGRFTYLIPNLSYDLQDNKAQFFLVIYNDFDVQIQQLLIALNLNLQQTTISIDEFLDSVYSKITTLQQIQSLSYQFYSQMQNLMSSQTTSQTIFNRHLFYQVYSSLKGVQIPCDSNINCSGNGKCLWSQDNYNEILCICNINYAGRYCEFQSYQLDIARQHLIALTDLISNIPLNKSSDLFFTIEVLLELTYFYSIFDEFTLNTLINVYFQVFNQLQRVQSNISDEKILFKISKLTSQLINLINEDQTLSYNDQQSLLMKTMNDFDSQINLYLQNFAKSFDDLKSQEQVQTSFQTDISNINLNLIYQNDLLDAFMSNNGASDGQQQTPIVFYGDQISYTFDITQFSPKSSLSTAVIKWNSNPFLSQSQYQAPFISCITELVIYSQQTEIQISTVSQIVEIAIPKILPTPILSVIRPFYQPYTCIYFDSVSQVYKQDGVQYLRENSTHVICGSEQISGNYGVIVNQEYIDPNLSLTVIWNATQQIYANDQQFINFINQLINSNNNNGTNENPQVSQSSFNPNLSLLYALLIYIIFITIFIVISIIRDRKDQETYIKESDSYWLVHPIYSLIFGPYSSFFPRLQRSINYAQLIINLFLYNAIFVLVYSLPSEQELQQNVGKRQIISIQISSTSVACSIVTYYLTICMVNLFKMKWYIKQKWLDFKQDKITTEIVEQVTKSLKIFHLMNYGLVFMLQAGMGIPIIILILSFNSQQNQFFFTSVFASFVIDNILDIIILISFCFIKIFSQSEKSKIILLFTLRGFYYPVYEFLDIEDKIKEYQQKGEVLPAEEANNQSDDEDIFEINDHMNTPKRIFKKNEEKIDKAQEEIQLNEFVNNLKTNQ

[Multiple Choices]
A. 1599..1619; 1704..1724; 1763..1783; 1796..1816
B. 1599..1619; 1662..1682; 1704..1724; 1758..1784; 1796..1816
C. 25..45; 55..75; 80..100; 116..136; 175..195; 211..231
D. 1599..1619; 1662..1682; 1704..1724; 1763..1783; 1796..1816
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Transmembrane Region Prediction, which is to predict a region of the protein that spans across a cell membrane. These transmembrane domains are typically hydrophobic alpha-helices that anchor the protein within the lipid bilayer or form channels. Based on the provided amino acid sequence, you must select the option that correctly identifies the start and end positions of a segment that crosses the membrane.. The inputs provided by the user for this task include:

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

> The sequence-matched UniProt record annotates the five helical transmembrane segments listed in D. These annotations carry computational evidence code ECO:0000255, so they support the key as a computational annotation, not as direct experimental confirmation.

Citations as saved: [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a cluster of long hydrophobic stretches in its C-terminal portion, consistent with multiple membrane-spanning alpha helices; the cysteine-rich, mostly nonhydrophobic N-terminal region in C is not similarly supported. The hydrophobic-segment pattern supports the five-span set in D over A, which omits one span. D's final span is also a typical roughly 20-residue membrane helix, while B extends that interval by several residues.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable knowledge of membrane-protein sequence patterns gives a concrete basis for identifying the C-terminal spans and preferring D, although exact helix boundaries are less certain than the presence of the spans.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> B and D identify the same apparent set of five spans and differ only in the endpoints of one interval. Transmembrane boundaries are not intrinsically sharp, so the longer interval in B could be defensible as a boundary choice even though D is better aligned with the supplied computational annotation.


### Important caveats

- The source annotation is computational rather than direct experimental evidence.
- Predicted transmembrane boundaries can vary by a few residues.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a cluster of long hydrophobic stretches in its C-terminal portion, consistent with multiple membrane-spanning alpha helices; the cysteine-rich, mostly nonhydrophobic N-terminal region in C is not similarly supported. The hydrophobic-segment pattern supports the five-span set in D over A, which omits one span. D's final span is also a typical roughly 20-residue membrane helix, while B extends that interval by several residues.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge of membrane-protein sequence patterns gives a concrete basis for identifying the C-terminal spans and preferring D, although exact helix boundaries are less certain than the presence of the spans."
  },
  "case_id": "transmembrane_0087",
  "expected_answer_check": {
    "evidence_ids": [
      "H3",
      "H4",
      "H5",
      "H6",
      "H7"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates the five helical transmembrane segments listed in D. These annotations carry computational evidence code ECO:0000255, so they support the key as a computational annotation, not as direct experimental confirmation."
  },
  "important_caveats": [
    "The source annotation is computational rather than direct experimental evidence.",
    "Predicted transmembrane boundaries can vary by a few residues."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "B and D identify the same apparent set of five spans and differ only in the endpoints of one interval. Transmembrane boundaries are not intrinsically sharp, so the longer interval in B could be defensible as a boundary choice even though D is better aligned with the supplied computational annotation."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0087",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates the five helical transmembrane segments listed in D. These annotations carry computational evidence code ECO:0000255, so they support the key as a computational annotation, not as direct experimental confirmation.",
    "evidence_ids": ["H3", "H4", "H5", "H6", "H7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a cluster of long hydrophobic stretches in its C-terminal portion, consistent with multiple membrane-spanning alpha helices; the cysteine-rich, mostly nonhydrophobic N-terminal region in C is not similarly supported. The hydrophobic-segment pattern supports the five-span set in D over A, which omits one span. D's final span is also a typical roughly 20-residue membrane helix, while B extends that interval by several residues.",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge of membrane-protein sequence patterns gives a concrete basis for identifying the C-terminal spans and preferring D, although exact helix boundaries are less certain than the presence of the spans."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "B and D identify the same apparent set of five spans and differ only in the endpoints of one interval. Transmembrane boundaries are not intrinsically sharp, so the longer interval in B could be defensible as a boundary choice even though D is better aligned with the supplied computational annotation."
  },
  "important_caveats": [
    "The source annotation is computational rather than direct experimental evidence.",
    "Predicted transmembrane boundaries can vary by a few residues."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q22HI5 annotates exactly five transmembrane helices at 1599-1619, 1662-1682, 1704-1724, 1763-1783, and 1796-1816 (all ECO:0000255, inferred by electronic annotation). Choice D matches these five regions exactly. The annotations are computational predictions rather than experimental determinations, but they are the recorded annotation consistent with the expected answer.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The protein has a clear two-domain architecture: an N-terminal region (~1-1500) dominated by cysteine-rich EGF-like repeats (abundant C-x-x-x-x-x-x-C motifs with polar residues Q, N, Y, T, S, P, G) and a C-terminal region (~1500-1915) containing hydrophobic stretches. This immediately eliminates option C, which places TM helices in the cysteine-rich extracellular domain. For the C-terminal region, a knowledgeable model can identify hydrophobic segments of ~20-25 residues consistent with TM helices. The presence of a hydrophobic stretch around 1662-1682 distinguishes D from A (which omits it). The B vs D distinction (1758-1784, 27 residues, vs 1763-1783, 21 residues) can be argued from general TM biology: canonical TM helices are 18-25 residues with ~21 being most common, making the 27-residue option atypical. Additionally, if residues 1758-1762 contain any polar/charged residues (common in inter-helix loops), they would be energetically unfavorable in the lipid bilayer core, favoring the later start at 1763. A model applying standard hydrophobicity window analysis and TM helix length statistics would plausibly favor D over B.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The overall TM region location (C-terminal, not N-terminal cysteine-rich domain) is identifiable from sequence composition. The number of TM helices and approximate boundaries can be inferred from hydrophobicity analysis. The B vs D boundary distinction (5-residue shift) is fine-grained but can be addressed by applying general knowledge that canonical TM helices are ~21 residues and that charged/polar residues at the edges disfavor membrane insertion. While not mathematically certain, this constitutes a defensible probabilistic inference from transferable TM biology knowledge.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Option C is clearly eliminated by the cysteine-rich extracellular domain composition. Option A is eliminated by the presence of a hydrophobic segment at ~1662-1682. Option B's 27-residue helix is atypical compared to the 21-residue helix in D. While the B vs D boundary is fine-grained, the standard TM helix length argument provides a reasonable basis for preferring D. No two options are equally defensible given the sequence evidence and general TM biology.


### Important caveats

- The UniProt TM annotations carry evidence code ECO:0000255 (inferred by electronic annotation), meaning they are computational predictions, not experimentally validated boundaries.
- The B vs D distinction (1758-1784 vs 1763-1783) is within the typical ±5 residue uncertainty of sequence-based TM prediction tools; the argument for D relies on helix-length statistics and possible polar residue exclusion rather than a definitive structural determination.
- The protein is from Tetrahymena thermophila (a ciliate), which has unusual membrane biology, but the fundamental hydrophobic-helix TM principle still applies.
- The reviewer-only evidence confirms sequence match and annotation consistency but was not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The protein has a clear two-domain architecture: an N-terminal region (~1-1500) dominated by cysteine-rich EGF-like repeats (abundant C-x-x-x-x-x-x-C motifs with polar residues Q, N, Y, T, S, P, G) and a C-terminal region (~1500-1915) containing hydrophobic stretches. This immediately eliminates option C, which places TM helices in the cysteine-rich extracellular domain. For the C-terminal region, a knowledgeable model can identify hydrophobic segments of ~20-25 residues consistent with TM helices. The presence of a hydrophobic stretch around 1662-1682 distinguishes D from A (which omits it). The B vs D distinction (1758-1784, 27 residues, vs 1763-1783, 21 residues) can be argued from general TM biology: canonical TM helices are 18-25 residues with ~21 being most common, making the 27-residue option atypical. Additionally, if residues 1758-1762 contain any polar/charged residues (common in inter-helix loops), they would be energetically unfavorable in the lipid bilayer core, favoring the later start at 1763. A model applying standard hydrophobicity window analysis and TM helix length statistics would plausibly favor D over B.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The overall TM region location (C-terminal, not N-terminal cysteine-rich domain) is identifiable from sequence composition. The number of TM helices and approximate boundaries can be inferred from hydrophobicity analysis. The B vs D boundary distinction (5-residue shift) is fine-grained but can be addressed by applying general knowledge that canonical TM helices are ~21 residues and that charged/polar residues at the edges disfavor membrane insertion. While not mathematically certain, this constitutes a defensible probabilistic inference from transferable TM biology knowledge."
  },
  "case_id": "transmembrane_0087",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "C8",
      "C9",
      "H3",
      "H4",
      "H5",
      "H6",
      "H7"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q22HI5 annotates exactly five transmembrane helices at 1599-1619, 1662-1682, 1704-1724, 1763-1783, and 1796-1816 (all ECO:0000255, inferred by electronic annotation). Choice D matches these five regions exactly. The annotations are computational predictions rather than experimental determinations, but they are the recorded annotation consistent with the expected answer."
  },
  "important_caveats": [
    "The UniProt TM annotations carry evidence code ECO:0000255 (inferred by electronic annotation), meaning they are computational predictions, not experimentally validated boundaries.",
    "The B vs D distinction (1758-1784 vs 1763-1783) is within the typical ±5 residue uncertainty of sequence-based TM prediction tools; the argument for D relies on helix-length statistics and possible polar residue exclusion rather than a definitive structural determination.",
    "The protein is from Tetrahymena thermophila (a ciliate), which has unusual membrane biology, but the fundamental hydrophobic-helix TM principle still applies.",
    "The reviewer-only evidence confirms sequence match and annotation consistency but was not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option C is clearly eliminated by the cysteine-rich extracellular domain composition. Option A is eliminated by the presence of a hydrophobic segment at ~1662-1682. Option B's 27-residue helix is atypical compared to the 21-residue helix in D. While the B vs D boundary is fine-grained, the standard TM helix length argument provides a reasonable basis for preferring D. No two options are equally defensible given the sequence evidence and general TM biology."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0087",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q22HI5 annotates exactly five transmembrane helices at 1599-1619, 1662-1682, 1704-1724, 1763-1783, and 1796-1816 (all ECO:0000255, inferred by electronic annotation). Choice D matches these five regions exactly. The annotations are computational predictions rather than experimental determinations, but they are the recorded annotation consistent with the expected answer.",
    "evidence_ids": ["C5", "C6", "C7", "C8", "C9", "H3", "H4", "H5", "H6", "H7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The protein has a clear two-domain architecture: an N-terminal region (~1-1500) dominated by cysteine-rich EGF-like repeats (abundant C-x-x-x-x-x-x-C motifs with polar residues Q, N, Y, T, S, P, G) and a C-terminal region (~1500-1915) containing hydrophobic stretches. This immediately eliminates option C, which places TM helices in the cysteine-rich extracellular domain. For the C-terminal region, a knowledgeable model can identify hydrophobic segments of ~20-25 residues consistent with TM helices. The presence of a hydrophobic stretch around 1662-1682 distinguishes D from A (which omits it). The B vs D distinction (1758-1784, 27 residues, vs 1763-1783, 21 residues) can be argued from general TM biology: canonical TM helices are 18-25 residues with ~21 being most common, making the 27-residue option atypical. Additionally, if residues 1758-1762 contain any polar/charged residues (common in inter-helix loops), they would be energetically unfavorable in the lipid bilayer core, favoring the later start at 1763. A model applying standard hydrophobicity window analysis and TM helix length statistics would plausibly favor D over B.",
    "missing_item_specific_fact": "",
    "reason": "The overall TM region location (C-terminal, not N-terminal cysteine-rich domain) is identifiable from sequence composition. The number of TM helices and approximate boundaries can be inferred from hydrophobicity analysis. The B vs D boundary distinction (5-residue shift) is fine-grained but can be addressed by applying general knowledge that canonical TM helices are ~21 residues and that charged/polar residues at the edges disfavor membrane insertion. While not mathematically certain, this constitutes a defensible probabilistic inference from transferable TM biology knowledge."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option C is clearly eliminated by the cysteine-rich extracellular domain composition. Option A is eliminated by the presence of a hydrophobic segment at ~1662-1682. Option B's 27-residue helix is atypical compared to the 21-residue helix in D. While the B vs D boundary is fine-grained, the standard TM helix length argument provides a reasonable basis for preferring D. No two options are equally defensible given the sequence evidence and general TM biology."
  },
  "important_caveats": [
    "The UniProt TM annotations carry evidence code ECO:0000255 (inferred by electronic annotation), meaning they are computational predictions, not experimentally validated boundaries.",
    "The B vs D distinction (1758-1784 vs 1763-1783) is within the typical ±5 residue uncertainty of sequence-based TM prediction tools; the argument for D relies on helix-length statistics and possible polar residue exclusion rather than a definitive structural determination.",
    "The protein is from Tetrahymena thermophila (a ciliate), which has unusual membrane biology, but the fundamental hydrophobic-helix TM principle still applies.",
    "The reviewer-only evidence confirms sequence match and annotation consistency but was not available to the evaluated model."
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
  "benchmark_sequence_length": 1915,
  "benchmark_sequence_sha256": "8f785de6bcc79dea51b5253339455fef1619f83907ec0a29c45e2b6b8b99a56d",
  "current_entry_audit": {
    "entryVersion": 84,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2014-04-16",
    "sequenceVersion": 2
  },
  "current_record_sha256": "dc1f846b407808b67ec8d77878a374ea9f0a7831736157eda370af6dc71ce78d",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 1915,
  "current_source_sequence_sha256": "8f785de6bcc79dea51b5253339455fef1619f83907ec0a29c45e2b6b8b99a56d",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 82,
      "exact_sequence_comparison": "matched",
      "sequence_version": 2
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q22HI5",
  "selected_historical_entry_version": 82,
  "selected_historical_record_sha256": "5b8287201ed2b14e65eebd69b4f7c01951e7aaf9c65caf0968e3ae2c42261ab5",
  "selected_historical_source_sequence_length": 1915,
  "selected_historical_source_sequence_sha256": "8f785de6bcc79dea51b5253339455fef1619f83907ec0a29c45e2b6b8b99a56d",
  "selected_historical_version": {
    "accession": "Q22HI5",
    "database": "Swiss-Prot",
    "entryVersion": 82,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "CRMP2_TETTS",
    "sequenceVersion": 2
  }
}
```

**Qualifications:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q22HI5.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q22HI5\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:20.342521+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "dc1f846b407808b67ec8d77878a374ea9f0a7831736157eda370af6dc71ce78d",
  "url": "https://rest.uniprot.org/uniprotkb/Q22HI5.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q22HI5.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":84,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2014-04-16\",\"sequenceVersion\":2}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:20.342521+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "dc1f846b407808b67ec8d77878a374ea9f0a7831736157eda370af6dc71ce78d",
  "url": "https://rest.uniprot.org/uniprotkb/Q22HI5.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q22HI5.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000009168\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Sar\",\"Alveolata\",\"Ciliophora\",\"Intramacronucleata\",\"Oligohymenophorea\",\"Hymenostomatida\",\"Tetrahymenina\",\"Tetrahymenidae\",\"Tetrahymena\"],\"scientificName\":\"Tetrahymena thermophila (strain SB210)\",\"taxonId\":312017}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:20.342521+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "dc1f846b407808b67ec8d77878a374ea9f0a7831736157eda370af6dc71ce78d",
  "url": "https://rest.uniprot.org/uniprotkb/Q22HI5.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q22HI5.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"EAR84716.2\",\"source\":\"EMBL\"}],\"value\":\"EGF-like domain protein\"}}],\"flag\":\"Precursor\",\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"36245278\",\"source\":\"PubMed\"}],\"value\":\"Cysteine repeat modular protein 2\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"36245278\",\"source\":\"PubMed\"}],\"value\":\"TtCRMP2\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:20.342521+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "dc1f846b407808b67ec8d77878a374ea9f0a7831736157eda370af6dc71ce78d",
  "url": "https://rest.uniprot.org/uniprotkb/Q22HI5.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q22HI5.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":1619},\"start\":{\"modifier\":\"EXACT\",\"value\":1599}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-01T06:25:20.342521+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "dc1f846b407808b67ec8d77878a374ea9f0a7831736157eda370af6dc71ce78d",
  "url": "https://rest.uniprot.org/uniprotkb/Q22HI5.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q22HI5.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":1682},\"start\":{\"modifier\":\"EXACT\",\"value\":1662}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-01T06:25:20.342521+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "dc1f846b407808b67ec8d77878a374ea9f0a7831736157eda370af6dc71ce78d",
  "url": "https://rest.uniprot.org/uniprotkb/Q22HI5.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q22HI5.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":1724},\"start\":{\"modifier\":\"EXACT\",\"value\":1704}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-01T06:25:20.342521+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "dc1f846b407808b67ec8d77878a374ea9f0a7831736157eda370af6dc71ce78d",
  "url": "https://rest.uniprot.org/uniprotkb/Q22HI5.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q22HI5.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":1783},\"start\":{\"modifier\":\"EXACT\",\"value\":1763}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
  "retrieved_utc": "2026-11-01T06:25:20.342521+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "dc1f846b407808b67ec8d77878a374ea9f0a7831736157eda370af6dc71ce78d",
  "url": "https://rest.uniprot.org/uniprotkb/Q22HI5.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q22HI5.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":1816},\"start\":{\"modifier\":\"EXACT\",\"value\":1796}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/6",
  "retrieved_utc": "2026-11-01T06:25:20.342521+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "dc1f846b407808b67ec8d77878a374ea9f0a7831736157eda370af6dc71ce78d",
  "url": "https://rest.uniprot.org/uniprotkb/Q22HI5.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q22HI5.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"citation\":{\"authors\":[\"Sparvoli D.\",\"Delabre J.\",\"Penarete-Vargas D.M.\",\"Kumar Mageswaran S.\",\"Tsypin L.M.\",\"Heckendorn J.\",\"Theveny L.\",\"Maynadier M.\",\"Mendonca Cova M.\",\"Berry-Sterkers L.\",\"Guerin A.\",\"Dubremetz J.F.\",\"Urbach S.\",\"Striepen B.\",\"Turkewitz A.P.\",\"Chang Y.W.\",\"Lebrun M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"36245278\"},{\"database\":\"DOI\",\"id\":\"10.15252/embj.2022111158\"}],\"citationType\":\"journal article\",\"firstPage\":\"e111158\",\"id\":\"36245278\",\"journal\":\"EMBO J.\",\"lastPage\":\"e111158\",\"publicationDate\":\"2022\",\"title\":\"An apical membrane complex for triggering rhoptry exocytosis and invasion in Toxoplasma.\",\"volume\":\"41\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-01T06:25:20.342521+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "dc1f846b407808b67ec8d77878a374ea9f0a7831736157eda370af6dc71ce78d",
  "url": "https://rest.uniprot.org/uniprotkb/Q22HI5.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q22HI5?format=txt&versions=82)

```json
{
  "entry_version": 82,
  "evidence_id": "H1",
  "excerpt": "ID   CRMP2_TETTS             Reviewed;        1915 AA.\nAC   Q22HI5;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   16-APR-2014, sequence version 2.\nDT   28-JAN-2026, entry version 82.\nDE   RecName: Full=Cysteine repeat modular protein 2 {ECO:0000303|PubMed:36245278};\nDE            Short=TtCRMP2 {ECO:0000303|PubMed:36245278};\nDE   AltName: Full=EGF-like domain protein {ECO:0000312|EMBL:EAR84716.2};\nDE   Flags: Precursor;\nGN   ORFNames=TTHERM_00637180 {ECO:0000312|EMBL:EAR84716.2};\nOS   Tetrahymena thermophila (strain SB210).\nOC   Eukaryota; Sar; Alveolata; Ciliophora; Intramacronucleata;\nOC   Oligohymenophorea; Hymenostomatida; Tetrahymenina; Tetrahymenidae;\nOC   Tetrahymena.\nOX   NCBI_TaxID=312017 {ECO:0000312|Proteomes:UP000009168};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:29.712799+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5b8287201ed2b14e65eebd69b4f7c01951e7aaf9c65caf0968e3ae2c42261ab5",
  "url": "https://rest.uniprot.org/unisave/Q22HI5?format=txt&versions=82"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q22HI5?format=txt&versions=82)

```json
{
  "entry_version": 82,
  "evidence_id": "H2",
  "excerpt": "RN   [2] {ECO:0000305}\nRP   FUNCTION, AND DISRUPTION PHENOTYPE.\nRX   PubMed=36245278; DOI=10.15252/embj.2022111158;\nRA   Sparvoli D., Delabre J., Penarete-Vargas D.M., Kumar Mageswaran S.,\nRA   Tsypin L.M., Heckendorn J., Theveny L., Maynadier M., Mendonca Cova M.,\nRA   Berry-Sterkers L., Guerin A., Dubremetz J.F., Urbach S., Striepen B.,\nRA   Turkewitz A.P., Chang Y.W., Lebrun M.;\nRT   \"An apical membrane complex for triggering rhoptry exocytosis and invasion\nRT   in Toxoplasma.\";\nRL   EMBO J. 41:e111158-e111158(2022).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:29.712799+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 33-42",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5b8287201ed2b14e65eebd69b4f7c01951e7aaf9c65caf0968e3ae2c42261ab5",
  "url": "https://rest.uniprot.org/unisave/Q22HI5?format=txt&versions=82"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q22HI5?format=txt&versions=82)

```json
{
  "entry_version": 82,
  "evidence_id": "H3",
  "excerpt": "FT   TRANSMEM        1599..1619\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:29.712799+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 88-90",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5b8287201ed2b14e65eebd69b4f7c01951e7aaf9c65caf0968e3ae2c42261ab5",
  "url": "https://rest.uniprot.org/unisave/Q22HI5?format=txt&versions=82"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q22HI5?format=txt&versions=82)

```json
{
  "entry_version": 82,
  "evidence_id": "H4",
  "excerpt": "FT   TRANSMEM        1662..1682\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:29.712799+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 91-93",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5b8287201ed2b14e65eebd69b4f7c01951e7aaf9c65caf0968e3ae2c42261ab5",
  "url": "https://rest.uniprot.org/unisave/Q22HI5?format=txt&versions=82"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q22HI5?format=txt&versions=82)

```json
{
  "entry_version": 82,
  "evidence_id": "H5",
  "excerpt": "FT   TRANSMEM        1704..1724\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:29.712799+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 94-96",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5b8287201ed2b14e65eebd69b4f7c01951e7aaf9c65caf0968e3ae2c42261ab5",
  "url": "https://rest.uniprot.org/unisave/Q22HI5?format=txt&versions=82"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q22HI5?format=txt&versions=82)

```json
{
  "entry_version": 82,
  "evidence_id": "H6",
  "excerpt": "FT   TRANSMEM        1763..1783\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:29.712799+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 97-99",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5b8287201ed2b14e65eebd69b4f7c01951e7aaf9c65caf0968e3ae2c42261ab5",
  "url": "https://rest.uniprot.org/unisave/Q22HI5?format=txt&versions=82"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q22HI5?format=txt&versions=82)

```json
{
  "entry_version": 82,
  "evidence_id": "H7",
  "excerpt": "FT   TRANSMEM        1796..1816\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:29.712799+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 100-102",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5b8287201ed2b14e65eebd69b4f7c01951e7aaf9c65caf0968e3ae2c42261ab5",
  "url": "https://rest.uniprot.org/unisave/Q22HI5?format=txt&versions=82"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 87. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
