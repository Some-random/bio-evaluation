# transmembrane_0034

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/transmembrane_0034.txt)

**Task:** `transmembrane`  
**Expected answer:** **D** — 47..71; 139..171; 196..220; 421..450; 466..495; 500..536; 560..592; 613..631; 635..659; 667..695; 701..721

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MLPYVIATLGSAGSTCKASTCSNSTKDYCYSARIRSTVLQGLPFGGVPTVLALDFMCFLALLFVFSILRKVAWDYGRLALVTDADSIASALHSDNHDRYERLTSVSSSVDFDQRDNGFCSWLTAIFRIKDDEIRDKCGGDAVHYLSFQRHIIGLLVAVGVLSVGIVLPVNFSGDLLENNAYSFGRTTIANLNSGNNLLWLHTSFAFLYLLLTVYSMRRHTSKMRYKEDDLVKRTLFINGISKYAEPEKIKKHFEEAYANCTVLEARPCYDVARLMFLDAERRKAERGRIYFTNLQSKENTPSMINPKPCGHLCCCVIRGCEEVEAIEYYTKLEEKLKDDYKREKEKVNEKPLGMAFVTFHNETITAIILKDFNACKCQGCACRGEPRASSCSESLHVSNWTVSYAPDPQNIYWEHLSIRGFIWWIRCLVINVVLFILLFFLTTPAIIITTMDKFNVTKPVEYLNNPIITQFFPTLLLWCFSALLPTIVYYSAFFEAHWTRSGENRTTMHKCYTFLIFMVLLLPSLGLSSLDVFFRWLFDKKFLAEAAVRFECVFLPDNGAFFVNYVIASAFIGNAMDLLRIPGLLMYMIRLCLARSAAERRNVKRHQAYEFQFGAAYAWMMCVFTVVMTYSITCPIIVPFGLMYMLLKHLVDRYNLYYAYLPAKLDKKIHSGAVNQVVAAPILCLFWLLFFSTMRTGFLAPTSMFTFVVLVITIVICLCHVCFGHFKYLSAHNYKIEHTEVDTTESRQNGRPATNLPAPKSAKYIAQVLQDSSPEGEATESEEQGSQDEELITTDGMNDTDFQSCEDSLIENEIRQ

[Multiple Choices]
A. 47..71; 139..171; 196..220; 421..450; 466..495; 500..536; 613..631; 635..659; 667..695; 701..721
B. 47..71; 139..171; 196..220; 421..450; 466..495; 500..536; 560..592; 613..631; 635..659; 669..693; 701..721
C. 27..47; 78..98; 108..128; 136..156; 173..193; 209..229; 337..357; 366..386; 400..420; 432..452; 465..485
D. 47..71; 139..171; 196..220; 421..450; 466..495; 500..536; 560..592; 613..631; 635..659; 667..695; 701..721
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

> The matched UniProt sequence annotation lists the transmembrane segments in choice D. These annotations are supported by similarity evidence to another UniProt entry, so they support the key as database annotation but are not direct experimental validation for this sequence.

Citations as saved: [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [C14](#evidence-c14), [C16](#evidence-c16), [C18](#evidence-c18), [C20](#evidence-c20), [C22](#evidence-c22), [C24](#evidence-c24), [C26](#evidence-c26).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence has repeated hydrophobic stretches consistent with a multi-pass membrane protein, which helps distinguish the membrane-spanning choices from C and favors choices that include the segment around 560–592. But this does not reliably resolve the two-residue boundary differences between B and D at the later helix.


**Missing item-specific fact**

> The reference-specific or convention-specific boundary for the helix around 667–695 is needed to select D over B as the exact keyed coordinate range.


**Reason**

> Transferable knowledge supports identifying the overall membrane topology, but B and D both mark the same strongly hydrophobic helix and differ only slightly in its endpoints. The sequence and general membrane-protein principles do not provide a dependable basis for the exact boundary distinction.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> Both options identify the same hydrophobic membrane-spanning helix; the small endpoint difference is not clearly resolvable from the wording or sequence alone.


### Important caveats

- The supporting transmembrane annotations use similarity evidence; they should not be described as experimentally established for this exact protein.
- The reviewer-only source identity and annotations were not original inputs and are not used as transferable knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has repeated hydrophobic stretches consistent with a multi-pass membrane protein, which helps distinguish the membrane-spanning choices from C and favors choices that include the segment around 560–592. But this does not reliably resolve the two-residue boundary differences between B and D at the later helix.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The reference-specific or convention-specific boundary for the helix around 667–695 is needed to select D over B as the exact keyed coordinate range.",
    "reason": "Transferable knowledge supports identifying the overall membrane topology, but B and D both mark the same strongly hydrophobic helix and differ only slightly in its endpoints. The sequence and general membrane-protein principles do not provide a dependable basis for the exact boundary distinction."
  },
  "case_id": "transmembrane_0034",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "C8",
      "C10",
      "C12",
      "C14",
      "C16",
      "C18",
      "C20",
      "C22",
      "C24",
      "C26"
    ],
    "judgment": "supported",
    "reason": "The matched UniProt sequence annotation lists the transmembrane segments in choice D. These annotations are supported by similarity evidence to another UniProt entry, so they support the key as database annotation but are not direct experimental validation for this sequence."
  },
  "important_caveats": [
    "The supporting transmembrane annotations use similarity evidence; they should not be described as experimentally established for this exact protein.",
    "The reviewer-only source identity and annotations were not original inputs and are not used as transferable knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "Both options identify the same hydrophobic membrane-spanning helix; the small endpoint difference is not clearly resolvable from the wording or sequence alone."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0034",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched UniProt sequence annotation lists the transmembrane segments in choice D. These annotations are supported by similarity evidence to another UniProt entry, so they support the key as database annotation but are not direct experimental validation for this sequence.",
    "evidence_ids": ["C6", "C8", "C10", "C12", "C14", "C16", "C18", "C20", "C22", "C24", "C26"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence has repeated hydrophobic stretches consistent with a multi-pass membrane protein, which helps distinguish the membrane-spanning choices from C and favors choices that include the segment around 560–592. But this does not reliably resolve the two-residue boundary differences between B and D at the later helix.",
    "missing_item_specific_fact": "The reference-specific or convention-specific boundary for the helix around 667–695 is needed to select D over B as the exact keyed coordinate range.",
    "reason": "Transferable knowledge supports identifying the overall membrane topology, but B and D both mark the same strongly hydrophobic helix and differ only slightly in its endpoints. The sequence and general membrane-protein principles do not provide a dependable basis for the exact boundary distinction."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "Both options identify the same hydrophobic membrane-spanning helix; the small endpoint difference is not clearly resolvable from the wording or sequence alone."
  },
  "important_caveats": [
    "The supporting transmembrane annotations use similarity evidence; they should not be described as experimentally established for this exact protein.",
    "The reviewer-only source identity and annotations were not original inputs and are not used as transferable knowledge."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A8V0ZB02 (TMEM63B, Gallus gallus) annotates exactly 11 transmembrane helices at the positions listed in option D: TM0 47-71, TM1 139-171, TM2 196-220, TM3 421-450, TM4 466-495, TM5 500-536, TM6 560-592, TM7 613-631, TM8 635-659, TM9 667-695, TM10 701-721. The evidence codes are ECO:0000250 (similarity-based annotation from human ortholog Q3TWI9), so this is computational inference by homology rather than direct experimental determination, but the annotation is internally consistent and matches the sequence. Option D matches the annotation exactly.

Citations as saved: [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [C14](#evidence-c14), [C16](#evidence-c16), [C18](#evidence-c18), [C20](#evidence-c20), [C22](#evidence-c22), [C24](#evidence-c24), [C26](#evidence-c26).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Option C uses uniformly 20-residue windows at roughly regular intervals, which contradicts the well-known variability in TM helix lengths (typically 18-30+ residues) and the irregular spacing dictated by actual hydrophobic stretches; a sliding-window hydrophobicity analysis immediately eliminates C. Option A omits the TM6 region at 560-592; examining the sequence between the end of TM5 (~536) and the cytoplasmic loop at 593-612 reveals a clearly hydrophobic stretch of ~33 residues consistent with a membrane-spanning helix, so a model performing hydrophobicity profiling can identify this region and eliminate A. The remaining distinction between B and D is a 2-residue boundary shift in TM9 (669-693 vs 667-695). A model examining the hydrophobicity profile at those exact boundaries could note whether residues at positions 667-668 and 694-695 are hydrophobic (supporting D's wider helix) or hydrophilic (supporting B's narrower helix). While this 2-residue difference is within the typical uncertainty of TM boundary prediction, the overall reasoning path—identifying 11 hydrophobic segments of varying lengths at approximately the right positions—meaningfully distinguishes D from A and C, and provides a defensible (if not certain) basis for preferring D over B.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The primary reasoning path (hydrophobicity analysis to identify ~11 TM segments of varying length, eliminating C's uniform windows and A's missing TM6) is well-supported by transferable knowledge of membrane protein topology. The B-vs-D distinction involves only a 2-residue boundary shift in TM9, which is subtle but can be approached by examining local hydrophobicity at those positions. The question is answerable through sequence-based reasoning without needing to recall this protein's specific database record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> Options B and D differ only in the TM9 boundaries: B gives 669-693 (25 residues) while D gives 667-695 (29 residues). A 2-residue shift at each boundary is within the typical uncertainty of TM helix boundary prediction from sequence alone. Without precise knowledge of where the hydrophobic stretch begins and ends at those exact positions, a model could reasonably select either option. The UniProt annotation supports D, but the sequence-based reasoning margin between B and D is very narrow.


### Important caveats

- All UniProt TM annotations for this entry carry evidence code ECO:0000250 (similarity to Q3TWI9, human TMEM63B), meaning they are computational inferences by homology rather than experimentally determined boundaries.
- The 2-residue boundary difference between options B and D (TM9: 669-693 vs 667-695) is within the typical error range of TM prediction algorithms, making this the weakest point of the question's discriminability.
- The reviewer-only evidence was not available to the evaluated model; the reasoning assessment is based solely on the original sequence and answer choices.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Option C uses uniformly 20-residue windows at roughly regular intervals, which contradicts the well-known variability in TM helix lengths (typically 18-30+ residues) and the irregular spacing dictated by actual hydrophobic stretches; a sliding-window hydrophobicity analysis immediately eliminates C. Option A omits the TM6 region at 560-592; examining the sequence between the end of TM5 (~536) and the cytoplasmic loop at 593-612 reveals a clearly hydrophobic stretch of ~33 residues consistent with a membrane-spanning helix, so a model performing hydrophobicity profiling can identify this region and eliminate A. The remaining distinction between B and D is a 2-residue boundary shift in TM9 (669-693 vs 667-695). A model examining the hydrophobicity profile at those exact boundaries could note whether residues at positions 667-668 and 694-695 are hydrophobic (supporting D's wider helix) or hydrophilic (supporting B's narrower helix). While this 2-residue difference is within the typical uncertainty of TM boundary prediction, the overall reasoning path—identifying 11 hydrophobic segments of varying lengths at approximately the right positions—meaningfully distinguishes D from A and C, and provides a defensible (if not certain) basis for preferring D over B.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The primary reasoning path (hydrophobicity analysis to identify ~11 TM segments of varying length, eliminating C's uniform windows and A's missing TM6) is well-supported by transferable knowledge of membrane protein topology. The B-vs-D distinction involves only a 2-residue boundary shift in TM9, which is subtle but can be approached by examining local hydrophobicity at those positions. The question is answerable through sequence-based reasoning without needing to recall this protein's specific database record."
  },
  "case_id": "transmembrane_0034",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "C8",
      "C10",
      "C12",
      "C14",
      "C16",
      "C18",
      "C20",
      "C22",
      "C24",
      "C26"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A8V0ZB02 (TMEM63B, Gallus gallus) annotates exactly 11 transmembrane helices at the positions listed in option D: TM0 47-71, TM1 139-171, TM2 196-220, TM3 421-450, TM4 466-495, TM5 500-536, TM6 560-592, TM7 613-631, TM8 635-659, TM9 667-695, TM10 701-721. The evidence codes are ECO:0000250 (similarity-based annotation from human ortholog Q3TWI9), so this is computational inference by homology rather than direct experimental determination, but the annotation is internally consistent and matches the sequence. Option D matches the annotation exactly."
  },
  "important_caveats": [
    "All UniProt TM annotations for this entry carry evidence code ECO:0000250 (similarity to Q3TWI9, human TMEM63B), meaning they are computational inferences by homology rather than experimentally determined boundaries.",
    "The 2-residue boundary difference between options B and D (TM9: 669-693 vs 667-695) is within the typical error range of TM prediction algorithms, making this the weakest point of the question's discriminability.",
    "The reviewer-only evidence was not available to the evaluated model; the reasoning assessment is based solely on the original sequence and answer choices."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "Options B and D differ only in the TM9 boundaries: B gives 669-693 (25 residues) while D gives 667-695 (29 residues). A 2-residue shift at each boundary is within the typical uncertainty of TM helix boundary prediction from sequence alone. Without precise knowledge of where the hydrophobic stretch begins and ends at those exact positions, a model could reasonably select either option. The UniProt annotation supports D, but the sequence-based reasoning margin between B and D is very narrow."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0034",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A8V0ZB02 (TMEM63B, Gallus gallus) annotates exactly 11 transmembrane helices at the positions listed in option D: TM0 47-71, TM1 139-171, TM2 196-220, TM3 421-450, TM4 466-495, TM5 500-536, TM6 560-592, TM7 613-631, TM8 635-659, TM9 667-695, TM10 701-721. The evidence codes are ECO:0000250 (similarity-based annotation from human ortholog Q3TWI9), so this is computational inference by homology rather than direct experimental determination, but the annotation is internally consistent and matches the sequence. Option D matches the annotation exactly.",
    "evidence_ids": ["C6", "C8", "C10", "C12", "C14", "C16", "C18", "C20", "C22", "C24", "C26"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Option C uses uniformly 20-residue windows at roughly regular intervals, which contradicts the well-known variability in TM helix lengths (typically 18-30+ residues) and the irregular spacing dictated by actual hydrophobic stretches; a sliding-window hydrophobicity analysis immediately eliminates C. Option A omits the TM6 region at 560-592; examining the sequence between the end of TM5 (~536) and the cytoplasmic loop at 593-612 reveals a clearly hydrophobic stretch of ~33 residues consistent with a membrane-spanning helix, so a model performing hydrophobicity profiling can identify this region and eliminate A. The remaining distinction between B and D is a 2-residue boundary shift in TM9 (669-693 vs 667-695). A model examining the hydrophobicity profile at those exact boundaries could note whether residues at positions 667-668 and 694-695 are hydrophobic (supporting D's wider helix) or hydrophilic (supporting B's narrower helix). While this 2-residue difference is within the typical uncertainty of TM boundary prediction, the overall reasoning path—identifying 11 hydrophobic segments of varying lengths at approximately the right positions—meaningfully distinguishes D from A and C, and provides a defensible (if not certain) basis for preferring D over B.",
    "missing_item_specific_fact": "",
    "reason": "The primary reasoning path (hydrophobicity analysis to identify ~11 TM segments of varying length, eliminating C's uniform windows and A's missing TM6) is well-supported by transferable knowledge of membrane protein topology. The B-vs-D distinction involves only a 2-residue boundary shift in TM9, which is subtle but can be approached by examining local hydrophobicity at those positions. The question is answerable through sequence-based reasoning without needing to recall this protein's specific database record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "Options B and D differ only in the TM9 boundaries: B gives 669-693 (25 residues) while D gives 667-695 (29 residues). A 2-residue shift at each boundary is within the typical uncertainty of TM helix boundary prediction from sequence alone. Without precise knowledge of where the hydrophobic stretch begins and ends at those exact positions, a model could reasonably select either option. The UniProt annotation supports D, but the sequence-based reasoning margin between B and D is very narrow."
  },
  "important_caveats": [
    "All UniProt TM annotations for this entry carry evidence code ECO:0000250 (similarity to Q3TWI9, human TMEM63B), meaning they are computational inferences by homology rather than experimentally determined boundaries.",
    "The 2-residue boundary difference between options B and D (TM9: 669-693 vs 667-695) is within the typical error range of TM prediction algorithms, making this the weakest point of the question's discriminability.",
    "The reviewer-only evidence was not available to the evaluated model; the reasoning assessment is based solely on the original sequence and answer choices."
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
  "benchmark_sequence_length": 816,
  "benchmark_sequence_sha256": "78ed17aad829cd9ff2c762ae9fcbd73ccfa275b6ddb7d47e552a86dc2ac5e435",
  "current_entry_audit": {
    "entryVersion": 18,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2022-12-14",
    "sequenceVersion": 1
  },
  "current_record_sha256": "2a70bd6be844793f85a89646f4b0890123b0430bff08bb408f761d9ee7d44c74",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 816,
  "current_source_sequence_sha256": "78ed17aad829cd9ff2c762ae9fcbd73ccfa275b6ddb7d47e552a86dc2ac5e435",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 16,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A8V0ZB02",
  "selected_historical_entry_version": 16,
  "selected_historical_record_sha256": "098fa8177aa78ced176ae350c71e2c32a9c01620a23e7c5f32ac21455a5f8704",
  "selected_historical_source_sequence_length": 816,
  "selected_historical_source_sequence_sha256": "78ed17aad829cd9ff2c762ae9fcbd73ccfa275b6ddb7d47e552a86dc2ac5e435",
  "selected_historical_version": {
    "accession": "A0A8V0ZB02",
    "database": "Swiss-Prot",
    "entryVersion": 16,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "TM63B_CHICK",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A8V0ZB02\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:24:51.590118+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2a70bd6be844793f85a89646f4b0890123b0430bff08bb408f761d9ee7d44c74",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":18,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2022-12-14\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:24:51.590118+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2a70bd6be844793f85a89646f4b0890123b0430bff08bb408f761d9ee7d44c74",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Chicken\",\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Chordata\",\"Craniata\",\"Vertebrata\",\"Euteleostomi\",\"Archelosauria\",\"Archosauria\",\"Dinosauria\",\"Saurischia\",\"Theropoda\",\"Coelurosauria\",\"Aves\",\"Neognathae\",\"Galloanserae\",\"Galliformes\",\"Phasianidae\",\"Phasianinae\",\"Gallus\"],\"scientificName\":\"Gallus gallus\",\"taxonId\":9031}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:24:51.590118+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2a70bd6be844793f85a89646f4b0890123b0430bff08bb408f761d9ee7d44c74",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39716028\",\"source\":\"PubMed\"}],\"value\":\"Transmembrane protein 63B\"}}],\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Mechanosensitive cation channel TMEM63B\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:24:51.590118+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2a70bd6be844793f85a89646f4b0890123b0430bff08bb408f761d9ee7d44c74",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Extracellular\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q3TWI9\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":46},\"start\":{\"modifier\":\"EXACT\",\"value\":1}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-01T06:24:51.590118+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2a70bd6be844793f85a89646f4b0890123b0430bff08bb408f761d9ee7d44c74",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"Helical; Name=TM0\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q3TWI9\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":71},\"start\":{\"modifier\":\"EXACT\",\"value\":47}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-01T06:24:51.590118+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2a70bd6be844793f85a89646f4b0890123b0430bff08bb408f761d9ee7d44c74",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q3TWI9\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":138},\"start\":{\"modifier\":\"EXACT\",\"value\":72}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-01T06:24:51.590118+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2a70bd6be844793f85a89646f4b0890123b0430bff08bb408f761d9ee7d44c74",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"Helical; Name=TM1\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q3TWI9\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":171},\"start\":{\"modifier\":\"EXACT\",\"value\":139}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-01T06:24:51.590118+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2a70bd6be844793f85a89646f4b0890123b0430bff08bb408f761d9ee7d44c74",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"Extracellular\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q3TWI9\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":195},\"start\":{\"modifier\":\"EXACT\",\"value\":172}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
  "retrieved_utc": "2026-11-01T06:24:51.590118+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2a70bd6be844793f85a89646f4b0890123b0430bff08bb408f761d9ee7d44c74",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"description\":\"Helical; Name=TM2\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q3TWI9\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":220},\"start\":{\"modifier\":\"EXACT\",\"value\":196}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/6",
  "retrieved_utc": "2026-11-01T06:24:51.590118+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2a70bd6be844793f85a89646f4b0890123b0430bff08bb408f761d9ee7d44c74",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q3TWI9\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":420},\"start\":{\"modifier\":\"EXACT\",\"value\":221}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/7",
  "retrieved_utc": "2026-11-01T06:24:51.590118+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2a70bd6be844793f85a89646f4b0890123b0430bff08bb408f761d9ee7d44c74",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json)

```json
{
  "evidence_id": "C12",
  "excerpt": "{\"description\":\"Helical; Name=TM3\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q3TWI9\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":450},\"start\":{\"modifier\":\"EXACT\",\"value\":421}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/8",
  "retrieved_utc": "2026-11-01T06:24:51.590118+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2a70bd6be844793f85a89646f4b0890123b0430bff08bb408f761d9ee7d44c74",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json)

```json
{
  "evidence_id": "C13",
  "excerpt": "{\"description\":\"Extracellular\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q3TWI9\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":465},\"start\":{\"modifier\":\"EXACT\",\"value\":451}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/9",
  "retrieved_utc": "2026-11-01T06:24:51.590118+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2a70bd6be844793f85a89646f4b0890123b0430bff08bb408f761d9ee7d44c74",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json"
}
```

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json)

```json
{
  "evidence_id": "C14",
  "excerpt": "{\"description\":\"Helical; Name=TM4\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q3TWI9\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":495},\"start\":{\"modifier\":\"EXACT\",\"value\":466}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/10",
  "retrieved_utc": "2026-11-01T06:24:51.590118+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2a70bd6be844793f85a89646f4b0890123b0430bff08bb408f761d9ee7d44c74",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json"
}
```

### Evidence C15

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json)

```json
{
  "evidence_id": "C15",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q3TWI9\",\"source\":\"UniProtKB\"},{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":499},\"start\":{\"modifier\":\"EXACT\",\"value\":496}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/11",
  "retrieved_utc": "2026-11-01T06:24:51.590118+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2a70bd6be844793f85a89646f4b0890123b0430bff08bb408f761d9ee7d44c74",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json"
}
```

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json)

```json
{
  "evidence_id": "C16",
  "excerpt": "{\"description\":\"Helical; Name=TM5\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q3TWI9\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":536},\"start\":{\"modifier\":\"EXACT\",\"value\":500}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/12",
  "retrieved_utc": "2026-11-01T06:24:51.590118+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2a70bd6be844793f85a89646f4b0890123b0430bff08bb408f761d9ee7d44c74",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json"
}
```

### Evidence C17

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json)

```json
{
  "evidence_id": "C17",
  "excerpt": "{\"description\":\"Extracellular\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q3TWI9\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":559},\"start\":{\"modifier\":\"EXACT\",\"value\":537}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/13",
  "retrieved_utc": "2026-11-01T06:24:51.590118+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2a70bd6be844793f85a89646f4b0890123b0430bff08bb408f761d9ee7d44c74",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json"
}
```

### Evidence C18

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json)

```json
{
  "evidence_id": "C18",
  "excerpt": "{\"description\":\"Helical; Name=TM6\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q3TWI9\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":592},\"start\":{\"modifier\":\"EXACT\",\"value\":560}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/14",
  "retrieved_utc": "2026-11-01T06:24:51.590118+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2a70bd6be844793f85a89646f4b0890123b0430bff08bb408f761d9ee7d44c74",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json"
}
```

### Evidence C19

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json)

```json
{
  "evidence_id": "C19",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q3TWI9\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":612},\"start\":{\"modifier\":\"EXACT\",\"value\":593}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/15",
  "retrieved_utc": "2026-11-01T06:24:51.590118+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2a70bd6be844793f85a89646f4b0890123b0430bff08bb408f761d9ee7d44c74",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json"
}
```

### Evidence C20

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json)

```json
{
  "evidence_id": "C20",
  "excerpt": "{\"description\":\"Helical; Name=TM7\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q3TWI9\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":631},\"start\":{\"modifier\":\"EXACT\",\"value\":613}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/16",
  "retrieved_utc": "2026-11-01T06:24:51.590118+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2a70bd6be844793f85a89646f4b0890123b0430bff08bb408f761d9ee7d44c74",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json"
}
```

### Evidence C21

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json)

```json
{
  "evidence_id": "C21",
  "excerpt": "{\"description\":\"Extracellular\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q3TWI9\",\"source\":\"UniProtKB\"},{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":634},\"start\":{\"modifier\":\"EXACT\",\"value\":632}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/17",
  "retrieved_utc": "2026-11-01T06:24:51.590118+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2a70bd6be844793f85a89646f4b0890123b0430bff08bb408f761d9ee7d44c74",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json"
}
```

### Evidence C22

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json)

```json
{
  "evidence_id": "C22",
  "excerpt": "{\"description\":\"Helical; Name=TM8\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q3TWI9\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":659},\"start\":{\"modifier\":\"EXACT\",\"value\":635}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/18",
  "retrieved_utc": "2026-11-01T06:24:51.590118+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2a70bd6be844793f85a89646f4b0890123b0430bff08bb408f761d9ee7d44c74",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json"
}
```

### Evidence C23

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json)

```json
{
  "evidence_id": "C23",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q3TWI9\",\"source\":\"UniProtKB\"},{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":666},\"start\":{\"modifier\":\"EXACT\",\"value\":660}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/19",
  "retrieved_utc": "2026-11-01T06:24:51.590118+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2a70bd6be844793f85a89646f4b0890123b0430bff08bb408f761d9ee7d44c74",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json"
}
```

### Evidence C24

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json)

```json
{
  "evidence_id": "C24",
  "excerpt": "{\"description\":\"Helical; Name=TM9\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q3TWI9\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":695},\"start\":{\"modifier\":\"EXACT\",\"value\":667}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/20",
  "retrieved_utc": "2026-11-01T06:24:51.590118+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2a70bd6be844793f85a89646f4b0890123b0430bff08bb408f761d9ee7d44c74",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json"
}
```

### Evidence C25

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json)

```json
{
  "evidence_id": "C25",
  "excerpt": "{\"description\":\"Extracellular\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q3TWI9\",\"source\":\"UniProtKB\"},{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":700},\"start\":{\"modifier\":\"EXACT\",\"value\":696}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/21",
  "retrieved_utc": "2026-11-01T06:24:51.590118+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2a70bd6be844793f85a89646f4b0890123b0430bff08bb408f761d9ee7d44c74",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json"
}
```

### Evidence C26

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json)

```json
{
  "evidence_id": "C26",
  "excerpt": "{\"description\":\"Helical; Name=TM10\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q3TWI9\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":721},\"start\":{\"modifier\":\"EXACT\",\"value\":701}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/22",
  "retrieved_utc": "2026-11-01T06:24:51.590118+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2a70bd6be844793f85a89646f4b0890123b0430bff08bb408f761d9ee7d44c74",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json"
}
```

### Evidence C27

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json)

```json
{
  "evidence_id": "C27",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q3TWI9\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":816},\"start\":{\"modifier\":\"EXACT\",\"value\":722}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/23",
  "retrieved_utc": "2026-11-01T06:24:51.590118+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2a70bd6be844793f85a89646f4b0890123b0430bff08bb408f761d9ee7d44c74",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json"
}
```

### Evidence C28

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json)

```json
{
  "evidence_id": "C28",
  "excerpt": "{\"citation\":{\"authors\":[\"Miyata Y.\",\"Nishimura M.\",\"Nagata A.\",\"Jing X.\",\"Sultan C.S.\",\"Kuribayashi R.\",\"Takahashi K.\",\"Lee Y.\",\"Nishizawa T.\",\"Segawa K.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39716028\"},{\"database\":\"DOI\",\"id\":\"10.1002/1873-3468.15084\"}],\"citationType\":\"journal article\",\"firstPage\":\"0\",\"id\":\"39716028\",\"journal\":\"FEBS Lett.\",\"lastPage\":\"0\",\"publicationDate\":\"2024\",\"title\":\"Membrane structure-responsive lipid scramblase activity of the TMEM63/OSCA family.\",\"volume\":\"0\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-01T06:24:51.590118+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2a70bd6be844793f85a89646f4b0890123b0430bff08bb408f761d9ee7d44c74",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16)

```json
{
  "entry_version": 16,
  "evidence_id": "H1",
  "excerpt": "ID   TM63B_CHICK             Reviewed;         816 AA.\nAC   A0A8V0ZB02;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   14-DEC-2022, sequence version 1.\nDT   28-JAN-2026, entry version 16.\nDE   RecName: Full=Mechanosensitive cation channel TMEM63B {ECO:0000305};\nDE   AltName: Full=Transmembrane protein 63B {ECO:0000303|PubMed:39716028};\nGN   Name=TMEM63B {ECO:0000303|PubMed:39716028};\nOS   Gallus gallus (Chicken).\nOC   Eukaryota; Metazoa; Chordata; Craniata; Vertebrata; Euteleostomi;\nOC   Archelosauria; Archosauria; Dinosauria; Saurischia; Theropoda;\nOC   Coelurosauria; Aves; Neognathae; Galloanserae; Galliformes; Phasianidae;\nOC   Phasianinae; Gallus.\nOX   NCBI_TaxID=9031;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:36.055628+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "098fa8177aa78ced176ae350c71e2c32a9c01620a23e7c5f32ac21455a5f8704",
  "url": "https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16)

```json
{
  "entry_version": 16,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION.\nRX   PubMed=39716028; DOI=10.1002/1873-3468.15084;\nRA   Miyata Y., Nishimura M., Nagata A., Jing X., Sultan C.S., Kuribayashi R.,\nRA   Takahashi K., Lee Y., Nishizawa T., Segawa K.;\nRT   \"Membrane structure-responsive lipid scramblase activity of the TMEM63/OSCA\nRT   family.\";\nRL   FEBS Lett. 0:0-0(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:36.055628+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 55-62",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "098fa8177aa78ced176ae350c71e2c32a9c01620a23e7c5f32ac21455a5f8704",
  "url": "https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16)

```json
{
  "entry_version": 16,
  "evidence_id": "H3",
  "excerpt": "FT   TOPO_DOM        1..46\nFT                   /note=\"Extracellular\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q3TWI9\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:36.055628+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 134-136",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "098fa8177aa78ced176ae350c71e2c32a9c01620a23e7c5f32ac21455a5f8704",
  "url": "https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16)

```json
{
  "entry_version": 16,
  "evidence_id": "H4",
  "excerpt": "FT   TRANSMEM        47..71\nFT                   /note=\"Helical; Name=TM0\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q3TWI9\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:36.055628+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 137-139",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "098fa8177aa78ced176ae350c71e2c32a9c01620a23e7c5f32ac21455a5f8704",
  "url": "https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16)

```json
{
  "entry_version": 16,
  "evidence_id": "H5",
  "excerpt": "FT   TOPO_DOM        72..138\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q3TWI9\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:36.055628+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 140-142",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "098fa8177aa78ced176ae350c71e2c32a9c01620a23e7c5f32ac21455a5f8704",
  "url": "https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16)

```json
{
  "entry_version": 16,
  "evidence_id": "H6",
  "excerpt": "FT   TRANSMEM        139..171\nFT                   /note=\"Helical; Name=TM1\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q3TWI9\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:36.055628+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 143-145",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "098fa8177aa78ced176ae350c71e2c32a9c01620a23e7c5f32ac21455a5f8704",
  "url": "https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16)

```json
{
  "entry_version": 16,
  "evidence_id": "H7",
  "excerpt": "FT   TOPO_DOM        172..195\nFT                   /note=\"Extracellular\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q3TWI9\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:36.055628+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 146-148",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "098fa8177aa78ced176ae350c71e2c32a9c01620a23e7c5f32ac21455a5f8704",
  "url": "https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16)

```json
{
  "entry_version": 16,
  "evidence_id": "H8",
  "excerpt": "FT   TRANSMEM        196..220\nFT                   /note=\"Helical; Name=TM2\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q3TWI9\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:36.055628+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 149-151",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "098fa8177aa78ced176ae350c71e2c32a9c01620a23e7c5f32ac21455a5f8704",
  "url": "https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16)

```json
{
  "entry_version": 16,
  "evidence_id": "H9",
  "excerpt": "FT   TOPO_DOM        221..420\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q3TWI9\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:36.055628+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 152-154",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "098fa8177aa78ced176ae350c71e2c32a9c01620a23e7c5f32ac21455a5f8704",
  "url": "https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16)

```json
{
  "entry_version": 16,
  "evidence_id": "H10",
  "excerpt": "FT   TRANSMEM        421..450\nFT                   /note=\"Helical; Name=TM3\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q3TWI9\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:36.055628+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 155-157",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "098fa8177aa78ced176ae350c71e2c32a9c01620a23e7c5f32ac21455a5f8704",
  "url": "https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16"
}
```

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16)

```json
{
  "entry_version": 16,
  "evidence_id": "H11",
  "excerpt": "FT   TOPO_DOM        451..465\nFT                   /note=\"Extracellular\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q3TWI9\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:36.055628+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 158-160",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "098fa8177aa78ced176ae350c71e2c32a9c01620a23e7c5f32ac21455a5f8704",
  "url": "https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16"
}
```

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16)

```json
{
  "entry_version": 16,
  "evidence_id": "H12",
  "excerpt": "FT   TRANSMEM        466..495\nFT                   /note=\"Helical; Name=TM4\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q3TWI9\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:36.055628+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 161-163",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "098fa8177aa78ced176ae350c71e2c32a9c01620a23e7c5f32ac21455a5f8704",
  "url": "https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16"
}
```

### Evidence H13

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16)

```json
{
  "entry_version": 16,
  "evidence_id": "H13",
  "excerpt": "FT   TOPO_DOM        496..499\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q3TWI9, ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:36.055628+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 164-166",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "098fa8177aa78ced176ae350c71e2c32a9c01620a23e7c5f32ac21455a5f8704",
  "url": "https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16"
}
```

### Evidence H14

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16)

```json
{
  "entry_version": 16,
  "evidence_id": "H14",
  "excerpt": "FT   TRANSMEM        500..536\nFT                   /note=\"Helical; Name=TM5\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q3TWI9\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:36.055628+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 167-169",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "098fa8177aa78ced176ae350c71e2c32a9c01620a23e7c5f32ac21455a5f8704",
  "url": "https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16"
}
```

### Evidence H15

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16)

```json
{
  "entry_version": 16,
  "evidence_id": "H15",
  "excerpt": "FT   TOPO_DOM        537..559\nFT                   /note=\"Extracellular\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q3TWI9\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:36.055628+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 170-172",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "098fa8177aa78ced176ae350c71e2c32a9c01620a23e7c5f32ac21455a5f8704",
  "url": "https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16"
}
```

### Evidence H16

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16)

```json
{
  "entry_version": 16,
  "evidence_id": "H16",
  "excerpt": "FT   TRANSMEM        560..592\nFT                   /note=\"Helical; Name=TM6\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q3TWI9\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:36.055628+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 173-175",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "098fa8177aa78ced176ae350c71e2c32a9c01620a23e7c5f32ac21455a5f8704",
  "url": "https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16"
}
```

### Evidence H17

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16)

```json
{
  "entry_version": 16,
  "evidence_id": "H17",
  "excerpt": "FT   TOPO_DOM        593..612\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q3TWI9\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:36.055628+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 176-178",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "098fa8177aa78ced176ae350c71e2c32a9c01620a23e7c5f32ac21455a5f8704",
  "url": "https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16"
}
```

### Evidence H18

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16)

```json
{
  "entry_version": 16,
  "evidence_id": "H18",
  "excerpt": "FT   TRANSMEM        613..631\nFT                   /note=\"Helical; Name=TM7\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q3TWI9\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:36.055628+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 179-181",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "098fa8177aa78ced176ae350c71e2c32a9c01620a23e7c5f32ac21455a5f8704",
  "url": "https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16"
}
```

### Evidence H19

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16)

```json
{
  "entry_version": 16,
  "evidence_id": "H19",
  "excerpt": "FT   TOPO_DOM        632..634\nFT                   /note=\"Extracellular\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q3TWI9, ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:36.055628+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 182-184",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "098fa8177aa78ced176ae350c71e2c32a9c01620a23e7c5f32ac21455a5f8704",
  "url": "https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16"
}
```

### Evidence H20

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16)

```json
{
  "entry_version": 16,
  "evidence_id": "H20",
  "excerpt": "FT   TRANSMEM        635..659\nFT                   /note=\"Helical; Name=TM8\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q3TWI9\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:36.055628+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 185-187",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "098fa8177aa78ced176ae350c71e2c32a9c01620a23e7c5f32ac21455a5f8704",
  "url": "https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16"
}
```

### Evidence H21

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16)

```json
{
  "entry_version": 16,
  "evidence_id": "H21",
  "excerpt": "FT   TOPO_DOM        660..666\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q3TWI9, ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:36.055628+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 188-190",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "098fa8177aa78ced176ae350c71e2c32a9c01620a23e7c5f32ac21455a5f8704",
  "url": "https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16"
}
```

### Evidence H22

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16)

```json
{
  "entry_version": 16,
  "evidence_id": "H22",
  "excerpt": "FT   TRANSMEM        667..695\nFT                   /note=\"Helical; Name=TM9\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q3TWI9\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:36.055628+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 191-193",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "098fa8177aa78ced176ae350c71e2c32a9c01620a23e7c5f32ac21455a5f8704",
  "url": "https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16"
}
```

### Evidence H23

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16)

```json
{
  "entry_version": 16,
  "evidence_id": "H23",
  "excerpt": "FT   TOPO_DOM        696..700\nFT                   /note=\"Extracellular\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q3TWI9, ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:36.055628+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 194-196",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "098fa8177aa78ced176ae350c71e2c32a9c01620a23e7c5f32ac21455a5f8704",
  "url": "https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16"
}
```

### Evidence H24

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16)

```json
{
  "entry_version": 16,
  "evidence_id": "H24",
  "excerpt": "FT   TRANSMEM        701..721\nFT                   /note=\"Helical; Name=TM10\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q3TWI9\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:36.055628+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 197-199",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "098fa8177aa78ced176ae350c71e2c32a9c01620a23e7c5f32ac21455a5f8704",
  "url": "https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16"
}
```

### Evidence H25

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16)

```json
{
  "entry_version": 16,
  "evidence_id": "H25",
  "excerpt": "FT   TOPO_DOM        722..816\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q3TWI9\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:36.055628+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 200-202",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "098fa8177aa78ced176ae350c71e2c32a9c01620a23e7c5f32ac21455a5f8704",
  "url": "https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 34. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
