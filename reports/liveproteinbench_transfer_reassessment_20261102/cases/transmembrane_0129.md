# transmembrane_0129

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/transmembrane_0129.txt)

**Task:** `transmembrane`  
**Expected answer:** **A** — 406..426; 574..594; 653..673; 678..698; 761..781; 791..811

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MQPPTRAPFFPFSLLRGRKARETCTCRSVASTEGPNTFGPRARPGCHAHQVAPSKESFHSSAFQLVSASRLSPLMSSCFVSFLRYPSFRPSAPFSAPPSSSTVPISTPSDFSHSAPASWRCVPTAPSALHAPFSFTTQAAHLSSCVFDGCSRLPCSEPGSPQTLQRALATTSATAFLRTACMSHRLRRRPDAWTSGCSGQTDNATASPCVRPLLRPPVDTASRAAANDKDAPQPTCFWRNARTSRAVHRNQTDMNFSSFSCSLRPCRHTLAKAAGHHAPLSRHSLQSLPESRIRGGTVSRGDSPGSLTLSPRNMSSDAMPVHPLYFPSAVPFSTTSGSNSSTFSCPSPSSSTSSTSSTSSTSSTSSTSSTSSTSSTSSTSSTSSPFLLSRSHSVDCRACPVSRAPPNPTSLQLLFSLFPFLWPTALKDRLRVLGSVACLVTAKVLTIQAPLLLANLVDAFQVLPHNSPLSPSGASPSSGDTSLLASSGETSSSLSPSAAPAEGAREAGKSGESAGRERRDEGSTVRLSPLAEGPASPATEERTAAGKAGTSVGGRDAGAVHALDTEHLRNTAQIVSVPLGVVCGFPVARIAATGFNELRSTLFTRVSQNASCDFSCHAFLHLHALALFHDKRAGELSVLISRGMKSVTALLNVLLFQMVPTALEFALVLYLLGSKVGGPVACITSLTMAVYVAFTAAVTARRTKIRKEMIAAEQQSVGLLVDSLANAEAVRFFTAEKGELSRFEAVQRRYAEKHVSVNQSLAFLNFGQQLIFNVGVLGSLAYTASQVAAGLLPVGHIVLVSSLLLQLAVPLNFVGTIYRETSLNLADLEKLYELMNHHPPIVNPPDARPFVLKGGAVAFENVRFAYPPSPLRPGSLPSKTGDDEKPEASRMLLDDVSFSVDAGKKVAIVGPSGVGKSTLIKLLFRMFDPASGTVRIDDQDVKELDLHSFRRQIGVVPQDMVLFNDTIEFNIKYGCPSATDEEMRAAAKQAEIDDVIMRMPQGYSTVVGERGLKLSGGERQRIGIARCLLRNPAIAVFDEATSALDSHTEQKILKAFRAMARGRTTLVIAHRLSTISDADKIIYLKEGKIAEMGTHAELLEKERGLYRALWESQQHQEQEEAVSTPDLTLS

[Multiple Choices]
A. 406..426; 574..594; 653..673; 678..698; 761..781; 791..811
B. 406..426; 574..594; 653..673; 678..698; 761..781
C. 406..426; 574..595; 653..673; 678..698; 761..781; 791..811
D. 65..85; 137..157; 158..178; 187..207; 216..236; 250..270; 334..354; 367..387; 392..412; 423..443; 455..475; 489..509
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

> The sequence-matched UniProt annotation lists all six transmembrane spans in choice A. These are computational helical annotations (ECO:0000255), not evidence of experimental determination of the exact boundaries.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence has a recognizable ABC-transporter nucleotide-binding region and a hydrophobic membrane-domain region, supporting a multi-pass transporter and making the many proposed spans in D implausible. The hydrophobic spans also support the six-span topology shared by A and C, and argue against B's omission of the final span. But transferable topology and hydropathy do not robustly choose between A and C's one-residue difference at the end of the 574 span.


**Missing item-specific fact**

> The exact annotated boundary at residue 594 rather than 595.


**Reason**

> Family architecture and sequence hydrophobicity provide meaningful generalization about the number and approximate locations of membrane helices, but the keyed distinction from C depends on a one-residue boundary choice that is not reliably established by those transferable clues.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "C"
]
```

> A and C specify the same six spans except that C extends one span by one residue. Since membrane-span boundaries are approximate and the extra residue does not change the predicted crossing, both are biologically defensible as region predictions, although only A matches the cited annotation.


### Important caveats

- The supplied sequence matches the reviewed source sequence, but the source's transmembrane evidence is computational rather than experimental.
- The exact author source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a recognizable ABC-transporter nucleotide-binding region and a hydrophobic membrane-domain region, supporting a multi-pass transporter and making the many proposed spans in D implausible. The hydrophobic spans also support the six-span topology shared by A and C, and argue against B's omission of the final span. But transferable topology and hydropathy do not robustly choose between A and C's one-residue difference at the end of the 574 span.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The exact annotated boundary at residue 594 rather than 595.",
    "reason": "Family architecture and sequence hydrophobicity provide meaningful generalization about the number and approximate locations of membrane helices, but the keyed distinction from C depends on a one-residue boundary choice that is not reliably established by those transferable clues."
  },
  "case_id": "transmembrane_0129",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "C8",
      "C9",
      "C10"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation lists all six transmembrane spans in choice A. These are computational helical annotations (ECO:0000255), not evidence of experimental determination of the exact boundaries."
  },
  "important_caveats": [
    "The supplied sequence matches the reviewed source sequence, but the source's transmembrane evidence is computational rather than experimental.",
    "The exact author source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "C"
    ],
    "reason": "A and C specify the same six spans except that C extends one span by one residue. Since membrane-span boundaries are approximate and the extra residue does not change the predicted crossing, both are biologically defensible as region predictions, although only A matches the cited annotation."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0129",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation lists all six transmembrane spans in choice A. These are computational helical annotations (ECO:0000255), not evidence of experimental determination of the exact boundaries.",
    "evidence_ids": ["C5", "C6", "C7", "C8", "C9", "C10"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence has a recognizable ABC-transporter nucleotide-binding region and a hydrophobic membrane-domain region, supporting a multi-pass transporter and making the many proposed spans in D implausible. The hydrophobic spans also support the six-span topology shared by A and C, and argue against B's omission of the final span. But transferable topology and hydropathy do not robustly choose between A and C's one-residue difference at the end of the 574 span.",
    "missing_item_specific_fact": "The exact annotated boundary at residue 594 rather than 595.",
    "reason": "Family architecture and sequence hydrophobicity provide meaningful generalization about the number and approximate locations of membrane helices, but the keyed distinction from C depends on a one-residue boundary choice that is not reliably established by those transferable clues."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "C"],
    "reason": "A and C specify the same six spans except that C extends one span by one residue. Since membrane-span boundaries are approximate and the extra residue does not change the predicted crossing, both are biologically defensible as region predictions, although only A matches the cited annotation."
  },
  "important_caveats": [
    "The supplied sequence matches the reviewed source sequence, but the source's transmembrane evidence is computational rather than experimental.",
    "The exact author source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation for S8EXU2 (ATM1_TOXGM) lists exactly six transmembrane helical regions at 406-426, 574-594, 653-673, 678-698, 761-781, and 791-811, matching option A precisely. The annotations are based on ECO:0000255 (similarity-based inference) and PROSITE-ProRule PRU00441 (ABC transporter transmembrane domain pattern), which are computational/predictive rather than experimentally determined, but they are consistent with the protein's identified function as a mitochondrial ABC transporter (ATM1/ABCB7-like). The sequence match is confirmed (SHA256 identical).

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8), [H9](#evidence-h9).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> This protein is an ABC transporter (half-transporter architecture: one TMD + one NBD). The C-terminal region (~850-1130) contains a clear Walker A motif (GPSGVGKST), Walker B, and ABC signature motifs, confirming the NBD location. ABC transporter TMDs canonically contain 6 transmembrane helices per domain. Option D (12 TMs at positions 65-509) is eliminated because the N-terminal region is overwhelmingly hydrophilic (Ser/Thr/Pro/Arg-rich with no 20-residue hydrophobic stretches) and the TMD must precede the NBD, not occupy the N-terminus. Option B (only 5 TMs) is atypical for ABC transporters, which canonically have 6 TMs per TMD; the missing 791-811 segment corresponds to the 6th TM. Option A provides exactly 6 TMs in the region between the long N-terminal extension and the NBD, consistent with half-transporter architecture seen in ABCB7/ABCB8/ABCB10 family members. The A-vs-C distinction (574-594 vs 574-595, a single-residue boundary) is the weakest point but can be approached by hydrophobicity analysis of the segment end.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The ABC transporter family-level knowledge of 6 canonical TM helices per TMD, combined with identification of the NBD (Walker A motif) in the C-terminal region and the hydrophilic nature of the N-terminal extension, provides a credible transferable inference that meaningfully distinguishes option A from B (5 TMs, atypical) and D (wrong topology and composition). The A-vs-C single-residue boundary is the most challenging distinction but does not undermine the overall reasoning path.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While the A-vs-C distinction (one residue at the boundary of the second TM) is subtle, the ABC transporter 6-TM canonical architecture and overall topology reasoning provide a clear path to A. Option B is eliminated by the 6-TM requirement, D by sequence composition and topology. C differs from A by a single residue boundary, which is unlikely to be independently resolved but does not create a second equally defensible full answer given the family-level constraints.


### Important caveats

- The UniProt transmembrane annotations are computational predictions (ECO:0000255 similarity-based and PROSITE-ProRule PRU00441 pattern matching), not experimentally determined structures.
- The A-vs-C distinction (574-594 vs 574-595) is a single-residue boundary difference that is very difficult to resolve by sequence analysis alone; a model might choose C over A based on a slightly different hydrophobicity cutoff.
- The protein has an unusually long N-terminal extension (~400 residues) with extensive Ser/Thr/Pro-rich regions, which is atypical for canonical ABC transporters and may complicate topology assignment.
- The source annotations were retrieved from a 2026 snapshot; the exact author source snapshot is unknown, though the sequence and annotation positions are consistent across versions 59-60.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "This protein is an ABC transporter (half-transporter architecture: one TMD + one NBD). The C-terminal region (~850-1130) contains a clear Walker A motif (GPSGVGKST), Walker B, and ABC signature motifs, confirming the NBD location. ABC transporter TMDs canonically contain 6 transmembrane helices per domain. Option D (12 TMs at positions 65-509) is eliminated because the N-terminal region is overwhelmingly hydrophilic (Ser/Thr/Pro/Arg-rich with no 20-residue hydrophobic stretches) and the TMD must precede the NBD, not occupy the N-terminus. Option B (only 5 TMs) is atypical for ABC transporters, which canonically have 6 TMs per TMD; the missing 791-811 segment corresponds to the 6th TM. Option A provides exactly 6 TMs in the region between the long N-terminal extension and the NBD, consistent with half-transporter architecture seen in ABCB7/ABCB8/ABCB10 family members. The A-vs-C distinction (574-594 vs 574-595, a single-residue boundary) is the weakest point but can be approached by hydrophobicity analysis of the segment end.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The ABC transporter family-level knowledge of 6 canonical TM helices per TMD, combined with identification of the NBD (Walker A motif) in the C-terminal region and the hydrophilic nature of the N-terminal extension, provides a credible transferable inference that meaningfully distinguishes option A from B (5 TMs, atypical) and D (wrong topology and composition). The A-vs-C single-residue boundary is the most challenging distinction but does not undermine the overall reasoning path."
  },
  "case_id": "transmembrane_0129",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "C8",
      "C9",
      "C10",
      "H4",
      "H5",
      "H6",
      "H7",
      "H8",
      "H9"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation for S8EXU2 (ATM1_TOXGM) lists exactly six transmembrane helical regions at 406-426, 574-594, 653-673, 678-698, 761-781, and 791-811, matching option A precisely. The annotations are based on ECO:0000255 (similarity-based inference) and PROSITE-ProRule PRU00441 (ABC transporter transmembrane domain pattern), which are computational/predictive rather than experimentally determined, but they are consistent with the protein's identified function as a mitochondrial ABC transporter (ATM1/ABCB7-like). The sequence match is confirmed (SHA256 identical)."
  },
  "important_caveats": [
    "The UniProt transmembrane annotations are computational predictions (ECO:0000255 similarity-based and PROSITE-ProRule PRU00441 pattern matching), not experimentally determined structures.",
    "The A-vs-C distinction (574-594 vs 574-595) is a single-residue boundary difference that is very difficult to resolve by sequence analysis alone; a model might choose C over A based on a slightly different hydrophobicity cutoff.",
    "The protein has an unusually long N-terminal extension (~400 residues) with extensive Ser/Thr/Pro-rich regions, which is atypical for canonical ABC transporters and may complicate topology assignment.",
    "The source annotations were retrieved from a 2026 snapshot; the exact author source snapshot is unknown, though the sequence and annotation positions are consistent across versions 59-60."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While the A-vs-C distinction (one residue at the boundary of the second TM) is subtle, the ABC transporter 6-TM canonical architecture and overall topology reasoning provide a clear path to A. Option B is eliminated by the 6-TM requirement, D by sequence composition and topology. C differs from A by a single residue boundary, which is unlikely to be independently resolved but does not create a second equally defensible full answer given the family-level constraints."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0129",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation for S8EXU2 (ATM1_TOXGM) lists exactly six transmembrane helical regions at 406-426, 574-594, 653-673, 678-698, 761-781, and 791-811, matching option A precisely. The annotations are based on ECO:0000255 (similarity-based inference) and PROSITE-ProRule PRU00441 (ABC transporter transmembrane domain pattern), which are computational/predictive rather than experimentally determined, but they are consistent with the protein's identified function as a mitochondrial ABC transporter (ATM1/ABCB7-like). The sequence match is confirmed (SHA256 identical).",
    "evidence_ids": ["C5", "C6", "C7", "C8", "C9", "C10", "H4", "H5", "H6", "H7", "H8", "H9"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "This protein is an ABC transporter (half-transporter architecture: one TMD + one NBD). The C-terminal region (~850-1130) contains a clear Walker A motif (GPSGVGKST), Walker B, and ABC signature motifs, confirming the NBD location. ABC transporter TMDs canonically contain 6 transmembrane helices per domain. Option D (12 TMs at positions 65-509) is eliminated because the N-terminal region is overwhelmingly hydrophilic (Ser/Thr/Pro/Arg-rich with no 20-residue hydrophobic stretches) and the TMD must precede the NBD, not occupy the N-terminus. Option B (only 5 TMs) is atypical for ABC transporters, which canonically have 6 TMs per TMD; the missing 791-811 segment corresponds to the 6th TM. Option A provides exactly 6 TMs in the region between the long N-terminal extension and the NBD, consistent with half-transporter architecture seen in ABCB7/ABCB8/ABCB10 family members. The A-vs-C distinction (574-594 vs 574-595, a single-residue boundary) is the weakest point but can be approached by hydrophobicity analysis of the segment end.",
    "missing_item_specific_fact": "",
    "reason": "The ABC transporter family-level knowledge of 6 canonical TM helices per TMD, combined with identification of the NBD (Walker A motif) in the C-terminal region and the hydrophilic nature of the N-terminal extension, provides a credible transferable inference that meaningfully distinguishes option A from B (5 TMs, atypical) and D (wrong topology and composition). The A-vs-C single-residue boundary is the most challenging distinction but does not undermine the overall reasoning path."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While the A-vs-C distinction (one residue at the boundary of the second TM) is subtle, the ABC transporter 6-TM canonical architecture and overall topology reasoning provide a clear path to A. Option B is eliminated by the 6-TM requirement, D by sequence composition and topology. C differs from A by a single residue boundary, which is unlikely to be independently resolved but does not create a second equally defensible full answer given the family-level constraints."
  },
  "important_caveats": [
    "The UniProt transmembrane annotations are computational predictions (ECO:0000255 similarity-based and PROSITE-ProRule PRU00441 pattern matching), not experimentally determined structures.",
    "The A-vs-C distinction (574-594 vs 574-595) is a single-residue boundary difference that is very difficult to resolve by sequence analysis alone; a model might choose C over A based on a slightly different hydrophobicity cutoff.",
    "The protein has an unusually long N-terminal extension (~400 residues) with extensive Ser/Thr/Pro-rich regions, which is atypical for canonical ABC transporters and may complicate topology assignment.",
    "The source annotations were retrieved from a 2026 snapshot; the exact author source snapshot is unknown, though the sequence and annotation positions are consistent across versions 59-60."
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
  "benchmark_sequence_length": 1130,
  "benchmark_sequence_sha256": "daba902a243edc1bc02b2eb767e57c10754863d7c3580600dfa56175853247ac",
  "current_entry_audit": {
    "entryVersion": 60,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2013-10-16",
    "sequenceVersion": 1
  },
  "current_record_sha256": "3c83d344f397e32f2e3203caf9b9d84cd10eaa76ba1ff03d22e5572308e0add9",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 1130,
  "current_source_sequence_sha256": "daba902a243edc1bc02b2eb767e57c10754863d7c3580600dfa56175853247ac",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 59,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "S8EXU2",
  "selected_historical_entry_version": 59,
  "selected_historical_record_sha256": "04a3f19563f6135254ffb6c7af171b94f9aa3d04e072b07ad86e250f49183933",
  "selected_historical_source_sequence_length": 1130,
  "selected_historical_source_sequence_sha256": "daba902a243edc1bc02b2eb767e57c10754863d7c3580600dfa56175853247ac",
  "selected_historical_version": {
    "accession": "S8EXU2",
    "database": "Swiss-Prot",
    "entryVersion": 59,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "ATM1_TOXGM",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/S8EXU2.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"S8EXU2\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:33:58.976860+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3c83d344f397e32f2e3203caf9b9d84cd10eaa76ba1ff03d22e5572308e0add9",
  "url": "https://rest.uniprot.org/uniprotkb/S8EXU2.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/S8EXU2.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":60,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2013-10-16\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:33:58.976860+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3c83d344f397e32f2e3203caf9b9d84cd10eaa76ba1ff03d22e5572308e0add9",
  "url": "https://rest.uniprot.org/uniprotkb/S8EXU2.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/S8EXU2.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000001529\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Sar\",\"Alveolata\",\"Apicomplexa\",\"Conoidasida\",\"Coccidia\",\"Eucoccidiorida\",\"Eimeriorina\",\"Sarcocystidae\",\"Toxoplasma\"],\"scientificName\":\"Toxoplasma gondii (strain ATCC 50611 / Me49)\",\"taxonId\":508771}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:33:58.976860+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3c83d344f397e32f2e3203caf9b9d84cd10eaa76ba1ff03d22e5572308e0add9",
  "url": "https://rest.uniprot.org/uniprotkb/S8EXU2.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/S8EXU2.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39207139\",\"source\":\"PubMed\"}],\"value\":\"ABCB7-like\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39207139\",\"source\":\"PubMed\"}],\"value\":\"ABCB7L\"},{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39207139\",\"source\":\"PubMed\"}],\"value\":\"TgABCB7L\"}]}],\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8IDH9\",\"source\":\"UniProtKB\"}],\"value\":\"7.-.-.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"ABC transporter ATM1\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39348385\",\"source\":\"PubMed\"}],\"value\":\"TgATM1\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:33:58.976860+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3c83d344f397e32f2e3203caf9b9d84cd10eaa76ba1ff03d22e5572308e0add9",
  "url": "https://rest.uniprot.org/uniprotkb/S8EXU2.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/S8EXU2.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":426},\"start\":{\"modifier\":\"EXACT\",\"value\":406}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-02T04:33:58.976860+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3c83d344f397e32f2e3203caf9b9d84cd10eaa76ba1ff03d22e5572308e0add9",
  "url": "https://rest.uniprot.org/uniprotkb/S8EXU2.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/S8EXU2.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":594},\"start\":{\"modifier\":\"EXACT\",\"value\":574}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-02T04:33:58.976860+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3c83d344f397e32f2e3203caf9b9d84cd10eaa76ba1ff03d22e5572308e0add9",
  "url": "https://rest.uniprot.org/uniprotkb/S8EXU2.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/S8EXU2.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"},{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU00441\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":673},\"start\":{\"modifier\":\"EXACT\",\"value\":653}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-02T04:33:58.976860+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3c83d344f397e32f2e3203caf9b9d84cd10eaa76ba1ff03d22e5572308e0add9",
  "url": "https://rest.uniprot.org/uniprotkb/S8EXU2.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/S8EXU2.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"},{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU00441\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":698},\"start\":{\"modifier\":\"EXACT\",\"value\":678}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
  "retrieved_utc": "2026-11-02T04:33:58.976860+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3c83d344f397e32f2e3203caf9b9d84cd10eaa76ba1ff03d22e5572308e0add9",
  "url": "https://rest.uniprot.org/uniprotkb/S8EXU2.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/S8EXU2.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"},{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU00441\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":781},\"start\":{\"modifier\":\"EXACT\",\"value\":761}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/6",
  "retrieved_utc": "2026-11-02T04:33:58.976860+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3c83d344f397e32f2e3203caf9b9d84cd10eaa76ba1ff03d22e5572308e0add9",
  "url": "https://rest.uniprot.org/uniprotkb/S8EXU2.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/S8EXU2.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"},{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU00441\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":811},\"start\":{\"modifier\":\"EXACT\",\"value\":791}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/7",
  "retrieved_utc": "2026-11-02T04:33:58.976860+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3c83d344f397e32f2e3203caf9b9d84cd10eaa76ba1ff03d22e5572308e0add9",
  "url": "https://rest.uniprot.org/uniprotkb/S8EXU2.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/S8EXU2.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"citation\":{\"authors\":[\"Maclean A.E.\",\"Sloan M.A.\",\"Renaud E.A.\",\"Argyle B.E.\",\"Lewis W.H.\",\"Ovciarikova J.\",\"Demolombe V.\",\"Waller R.F.\",\"Besteiro S.\",\"Sheiner L.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39207139\"},{\"database\":\"DOI\",\"id\":\"10.1128/mbio.00872-24\"}],\"citationType\":\"journal article\",\"firstPage\":\"e0087224\",\"id\":\"39207139\",\"journal\":\"MBio\",\"lastPage\":\"e0087224\",\"publicationDate\":\"2024\",\"title\":\"The Toxoplasma gondii mitochondrial transporter ABCB7L is essential for the biogenesis of cytosolic and nuclear iron-sulfur cluster proteins and cytosolic translation.\",\"volume\":\"15\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"SUBUNIT\",\"SUBCELLULAR LOCATION\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:33:58.976860+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3c83d344f397e32f2e3203caf9b9d84cd10eaa76ba1ff03d22e5572308e0add9",
  "url": "https://rest.uniprot.org/uniprotkb/S8EXU2.json"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/S8EXU2.json)

```json
{
  "evidence_id": "C12",
  "excerpt": "{\"citation\":{\"authors\":[\"Shrivastava D.\",\"Abboud E.\",\"Ramchandra J.P.\",\"Jha A.\",\"Marq J.B.\",\"Chaurasia A.\",\"Mitra K.\",\"Sadik M.\",\"Siddiqi M.I.\",\"Soldati-Favre D.\",\"Kloehn J.\",\"Habib S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39348385\"},{\"database\":\"DOI\",\"id\":\"10.1371/journal.ppat.1012593\"}],\"citationType\":\"journal article\",\"firstPage\":\"e1012593\",\"id\":\"39348385\",\"journal\":\"PLoS Pathog.\",\"lastPage\":\"e1012593\",\"publicationDate\":\"2024\",\"title\":\"ATM1, an essential conserved transporter in Apicomplexa, bridges mitochondrial and cytosolic [Fe-S] biogenesis.\",\"volume\":\"20\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"SUBUNIT\",\"SUBCELLULAR LOCATION\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-02T04:33:58.976860+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3c83d344f397e32f2e3203caf9b9d84cd10eaa76ba1ff03d22e5572308e0add9",
  "url": "https://rest.uniprot.org/uniprotkb/S8EXU2.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/S8EXU2?format=txt&versions=59)

```json
{
  "entry_version": 59,
  "evidence_id": "H1",
  "excerpt": "ID   ATM1_TOXGM              Reviewed;        1130 AA.\nAC   S8EXU2;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   16-OCT-2013, sequence version 1.\nDT   28-JAN-2026, entry version 59.\nDE   RecName: Full=ABC transporter ATM1 {ECO:0000305};\nDE            Short=TgATM1 {ECO:0000303|PubMed:39348385};\nDE            EC=7.-.-.- {ECO:0000250|UniProtKB:Q8IDH9};\nDE   AltName: Full=ABCB7-like {ECO:0000303|PubMed:39207139};\nDE            Short=ABCB7L {ECO:0000303|PubMed:39207139};\nDE            Short=TgABCB7L {ECO:0000303|PubMed:39207139};\nDE   Flags: Precursor;\nGN   ORFNames=TGME49_269000 {ECO:0000312|EMBL:EPT28291.1};\nOS   Toxoplasma gondii (strain ATCC 50611 / Me49).\nOC   Eukaryota; Sar; Alveolata; Apicomplexa; Conoidasida; Coccidia;\nOC   Eucoccidiorida; Eimeriorina; Sarcocystidae; Toxoplasma.\nOX   NCBI_TaxID=508771 {ECO:0000312|Proteomes:UP000001529};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:34:03.453043+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-17",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "04a3f19563f6135254ffb6c7af171b94f9aa3d04e072b07ad86e250f49183933",
  "url": "https://rest.uniprot.org/unisave/S8EXU2?format=txt&versions=59"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/S8EXU2?format=txt&versions=59)

```json
{
  "entry_version": 59,
  "evidence_id": "H2",
  "excerpt": "RN   [2] {ECO:0000305}\nRP   FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, AND DISRUPTION PHENOTYPE.\nRX   PubMed=39207139; DOI=10.1128/mbio.00872-24;\nRA   Maclean A.E., Sloan M.A., Renaud E.A., Argyle B.E., Lewis W.H.,\nRA   Ovciarikova J., Demolombe V., Waller R.F., Besteiro S., Sheiner L.;\nRT   \"The Toxoplasma gondii mitochondrial transporter ABCB7L is essential for\nRT   the biogenesis of cytosolic and nuclear iron-sulfur cluster proteins and\nRT   cytosolic translation.\";\nRL   MBio 15:e0087224-e0087224(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:34:03.453043+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 24-32",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "04a3f19563f6135254ffb6c7af171b94f9aa3d04e072b07ad86e250f49183933",
  "url": "https://rest.uniprot.org/unisave/S8EXU2?format=txt&versions=59"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/S8EXU2?format=txt&versions=59)

```json
{
  "entry_version": 59,
  "evidence_id": "H3",
  "excerpt": "RN   [3] {ECO:0000305}\nRP   FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, AND DISRUPTION PHENOTYPE.\nRX   PubMed=39348385; DOI=10.1371/journal.ppat.1012593;\nRA   Shrivastava D., Abboud E., Ramchandra J.P., Jha A., Marq J.B.,\nRA   Chaurasia A., Mitra K., Sadik M., Siddiqi M.I., Soldati-Favre D.,\nRA   Kloehn J., Habib S.;\nRT   \"ATM1, an essential conserved transporter in Apicomplexa, bridges\nRT   mitochondrial and cytosolic [Fe-S] biogenesis.\";\nRL   PLoS Pathog. 20:e1012593-e1012593(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:34:03.453043+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 33-41",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "04a3f19563f6135254ffb6c7af171b94f9aa3d04e072b07ad86e250f49183933",
  "url": "https://rest.uniprot.org/unisave/S8EXU2?format=txt&versions=59"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/S8EXU2?format=txt&versions=59)

```json
{
  "entry_version": 59,
  "evidence_id": "H4",
  "excerpt": "FT   TRANSMEM        406..426\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:34:03.453043+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 118-120",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "04a3f19563f6135254ffb6c7af171b94f9aa3d04e072b07ad86e250f49183933",
  "url": "https://rest.uniprot.org/unisave/S8EXU2?format=txt&versions=59"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/S8EXU2?format=txt&versions=59)

```json
{
  "entry_version": 59,
  "evidence_id": "H5",
  "excerpt": "FT   TRANSMEM        574..594\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:34:03.453043+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 121-123",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "04a3f19563f6135254ffb6c7af171b94f9aa3d04e072b07ad86e250f49183933",
  "url": "https://rest.uniprot.org/unisave/S8EXU2?format=txt&versions=59"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/S8EXU2?format=txt&versions=59)

```json
{
  "entry_version": 59,
  "evidence_id": "H6",
  "excerpt": "FT   TRANSMEM        653..673\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255, ECO:0000255|PROSITE-\nFT                   ProRule:PRU00441\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:34:03.453043+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 124-127",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "04a3f19563f6135254ffb6c7af171b94f9aa3d04e072b07ad86e250f49183933",
  "url": "https://rest.uniprot.org/unisave/S8EXU2?format=txt&versions=59"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/S8EXU2?format=txt&versions=59)

```json
{
  "entry_version": 59,
  "evidence_id": "H7",
  "excerpt": "FT   TRANSMEM        678..698\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255, ECO:0000255|PROSITE-\nFT                   ProRule:PRU00441\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:34:03.453043+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 128-131",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "04a3f19563f6135254ffb6c7af171b94f9aa3d04e072b07ad86e250f49183933",
  "url": "https://rest.uniprot.org/unisave/S8EXU2?format=txt&versions=59"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/S8EXU2?format=txt&versions=59)

```json
{
  "entry_version": 59,
  "evidence_id": "H8",
  "excerpt": "FT   TRANSMEM        761..781\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255, ECO:0000255|PROSITE-\nFT                   ProRule:PRU00441\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:34:03.453043+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 132-135",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "04a3f19563f6135254ffb6c7af171b94f9aa3d04e072b07ad86e250f49183933",
  "url": "https://rest.uniprot.org/unisave/S8EXU2?format=txt&versions=59"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/S8EXU2?format=txt&versions=59)

```json
{
  "entry_version": 59,
  "evidence_id": "H9",
  "excerpt": "FT   TRANSMEM        791..811\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255, ECO:0000255|PROSITE-\nFT                   ProRule:PRU00441\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:34:03.453043+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 136-139",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "04a3f19563f6135254ffb6c7af171b94f9aa3d04e072b07ad86e250f49183933",
  "url": "https://rest.uniprot.org/unisave/S8EXU2?format=txt&versions=59"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 129. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
