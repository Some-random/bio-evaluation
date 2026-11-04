# transmembrane_0046

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/transmembrane_0046.txt)

**Task:** `transmembrane`  
**Expected answer:** **C** — 606..628

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MRAGRVRPLRASDMKKDVRILLVGEPRVGKTSLIMSLVSEEFPEEVPPRAEEITIPADVTPERVPTHIVDYSEAEQSDEQLHQEISQANVICIVYAVNNKHSIDKVTSRWIPLINERTDKDSRLPLILVGNKSDLVEYSSMETILPIMNQYTEIETCVECSAKNLKNISELFYYAQKAVLHPTGPLYCPEEKEMKPACIKALTRIFKISDQDNDGTLNDAELNFFQRICFNTPLAPQALEDVKNVVRKHLSDGVADSGLTLRGFLFLHTLFIQRGRHETTWTVLRRFGYDDDLDLTPEYLFPLLKIPPDCTTELNHHAYLFLQSTFDKHDLDRDCALSPDELKDLFQVFPYIPWGPDVNNTVCTNESGWITYQGFLSQWTLTTYLDVQRCLEYLGYLGYSILTEQESQASAITVTRDKKIDLQKKQTQRNVFRCNVIGVKGCGKTGVLQSLLGRNLMRQKKIRDDHKSYYAINTVYVYGQEKYLLLHDISESEFLTEAEIVCDVVCLVYDVTNPKSFEYCARIFKQHFMDSRIPCLIVAAKSDLHEVKQEHSVSPTDFCRKHKMPPPQAFTCNTADAPSKDIFVKLTTMAMYPHVTQADLKSSTFWLRASFGATVFAVVGFAMYRALLKQR

[Multiple Choices]
A. 606..628; 456..476
B. 607..624
C. 606..628
D. 3..23
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

> The sequence-matched UniProt annotation identifies 606..628 as a transmembrane helix. This is computationally supported annotation (ECO:0000255), not experimental proof in the supplied evidence.

Citations as saved: [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The strongly hydrophobic C-terminal stretch is a credible membrane-spanning helix, distinguishing this region from the N-terminus and the 456..476 region. But both 606..628 and its 607..624 subsegment could plausibly span a membrane; sequence principles do not fix the exact boundaries.


**Missing item-specific fact**

> The exact annotated start and end of the transmembrane feature for this protein.


**Reason**

> Transferable sequence knowledge locates the likely C-terminal membrane anchor, but does not meaningfully distinguish the full interval in C from the shorter plausible interval in B. Selecting the keyed coordinates requires exact boundary information not present in the original input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "C"
]
```

> Both intervals lie within the same hydrophobic C-terminal stretch, and the question gives no boundary convention that would rule out the shorter interval as a membrane-spanning segment.


### Important caveats

- The reviewer-only annotation matches the supplied sequence, but its evidence code indicates computational support rather than direct experimental validation.
- Option A also includes 456..476, which is not a comparable hydrophobic membrane-spanning segment.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The strongly hydrophobic C-terminal stretch is a credible membrane-spanning helix, distinguishing this region from the N-terminus and the 456..476 region. But both 606..628 and its 607..624 subsegment could plausibly span a membrane; sequence principles do not fix the exact boundaries.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The exact annotated start and end of the transmembrane feature for this protein.",
    "reason": "Transferable sequence knowledge locates the likely C-terminal membrane anchor, but does not meaningfully distinguish the full interval in C from the shorter plausible interval in B. Selecting the keyed coordinates requires exact boundary information not present in the original input."
  },
  "case_id": "transmembrane_0046",
  "expected_answer_check": {
    "evidence_ids": [
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies 606..628 as a transmembrane helix. This is computationally supported annotation (ECO:0000255), not experimental proof in the supplied evidence."
  },
  "important_caveats": [
    "The reviewer-only annotation matches the supplied sequence, but its evidence code indicates computational support rather than direct experimental validation.",
    "Option A also includes 456..476, which is not a comparable hydrophobic membrane-spanning segment."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "C"
    ],
    "reason": "Both intervals lie within the same hydrophobic C-terminal stretch, and the question gives no boundary convention that would rule out the shorter interval as a membrane-spanning segment."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0046",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies 606..628 as a transmembrane helix. This is computationally supported annotation (ECO:0000255), not experimental proof in the supplied evidence.",
    "evidence_ids": ["H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The strongly hydrophobic C-terminal stretch is a credible membrane-spanning helix, distinguishing this region from the N-terminus and the 456..476 region. But both 606..628 and its 607..624 subsegment could plausibly span a membrane; sequence principles do not fix the exact boundaries.",
    "missing_item_specific_fact": "The exact annotated start and end of the transmembrane feature for this protein.",
    "reason": "Transferable sequence knowledge locates the likely C-terminal membrane anchor, but does not meaningfully distinguish the full interval in C from the shorter plausible interval in B. Selecting the keyed coordinates requires exact boundary information not present in the original input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "C"],
    "reason": "Both intervals lie within the same hydrophobic C-terminal stretch, and the question gives no boundary convention that would rule out the shorter interval as a membrane-spanning segment."
  },
  "important_caveats": [
    "The reviewer-only annotation matches the supplied sequence, but its evidence code indicates computational support rather than direct experimental validation.",
    "Option A also includes 456..476, which is not a comparable hydrophobic membrane-spanning segment."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A1L1L6 (MIRO1_RAT) annotates a single transmembrane helix at positions 606-628 as 'Helical; Anchor for type IV membrane protein' (evidence code ECO:0000255, PIRNR computational prediction). The topological domains confirm: cytoplasmic 1-605, TM 606-628, mitochondrial intermembrane 629-631. The sequence at 606-628 (TFWLRASFGATVFAVVGFAMYRALL) is predominantly hydrophobic, consistent with a single-pass TM anchor. The annotation is computational (PIRNR) rather than experimentally determined, but it is the canonical database annotation.

Citations as saved: [C6](#evidence-c6), [C5](#evidence-c5), [C7](#evidence-c7), [H3](#evidence-h3), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The protein is 631 residues with a clear C-terminal hydrophobic stretch. Option D (3-23) is the N-terminus containing charged residues (R, D, K) incompatible with a TM helix. Option A adds a second region (456-476) that falls within the EF-hand/GTPase domain region rich in charged residues (R, K, D, E) and is clearly not transmembrane. Between B (607-624) and C (606-628): the hydrophobic core FWLRASFGATVFAVVGFAMY extends from ~607 to ~624, but general TM helix boundary principles indicate that (1) the helix typically extends to the nearest strongly polar boundary—K629 (lysine) clearly terminates the TM, so the helix should extend past 624 through M625, Y626, R627, A628, L628 (aromatic Y and charged R are commonly found at TM-water interfaces); (2) T606 is a typical boundary residue for TM helices; (3) the 23-residue span (606-628) is within the expected 20-25 residue range for a single-pass TM helix in a lipid bilayer, while B's 18 residues is at the short end. The presence of Y and R at positions 626-627 (aromatic/charged interface residues) and the clear polar break at K629 supports the wider boundary of C.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can identify the C-terminal hydrophobic stretch as the sole TM region, eliminate options A and D based on domain architecture and charge content, and use general TM helix boundary principles (aromatic/charged residues at interfaces, hydrophobic core extent, polar residue boundaries) to favor the 23-residue span C over the 18-residue subset B. The reasoning is probabilistic but concrete and grounded in transferable TM biology.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "C"
]
```

> The distinction between B (607-624) and C (606-628) depends on exact boundary determination, which is inherently algorithm-dependent. The UniProt annotation (computational PIRNR) chose 606-628, but a hydrophobicity-based analysis could reasonably argue for 607-624 as the 'core' hydrophobic segment. However, the presence of K629 as a clear polar boundary and the general principle that TM helices extend to interface residues (Y, R) makes C more defensible than B, though B is not unreasonable.


### Important caveats

- The UniProt TM annotation (606-628) is computational (ECO:0000255, PIRNR evidence), not experimentally validated. Exact TM boundaries from prediction algorithms can vary by 2-5 residues.
- The protein is MIRO-1 (Mitochondrial Rho GTPase), a single-pass type IV membrane protein with its TM anchor in the C-terminus. This family knowledge aids identification but the exact boundary numbers depend on the prediction method.
- Option A's inclusion of a second region (456-476) is clearly wrong as that region lies within the EF-hand calcium-binding domain with multiple charged residues.
- The sequence matches the UniProt entry exactly (SHA256 confirmed), so positional numbering is reliable.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The protein is 631 residues with a clear C-terminal hydrophobic stretch. Option D (3-23) is the N-terminus containing charged residues (R, D, K) incompatible with a TM helix. Option A adds a second region (456-476) that falls within the EF-hand/GTPase domain region rich in charged residues (R, K, D, E) and is clearly not transmembrane. Between B (607-624) and C (606-628): the hydrophobic core FWLRASFGATVFAVVGFAMY extends from ~607 to ~624, but general TM helix boundary principles indicate that (1) the helix typically extends to the nearest strongly polar boundary—K629 (lysine) clearly terminates the TM, so the helix should extend past 624 through M625, Y626, R627, A628, L628 (aromatic Y and charged R are commonly found at TM-water interfaces); (2) T606 is a typical boundary residue for TM helices; (3) the 23-residue span (606-628) is within the expected 20-25 residue range for a single-pass TM helix in a lipid bilayer, while B's 18 residues is at the short end. The presence of Y and R at positions 626-627 (aromatic/charged interface residues) and the clear polar break at K629 supports the wider boundary of C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can identify the C-terminal hydrophobic stretch as the sole TM region, eliminate options A and D based on domain architecture and charge content, and use general TM helix boundary principles (aromatic/charged residues at interfaces, hydrophobic core extent, polar residue boundaries) to favor the 23-residue span C over the 18-residue subset B. The reasoning is probabilistic but concrete and grounded in transferable TM biology."
  },
  "case_id": "transmembrane_0046",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "C5",
      "C7",
      "H3",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A1L1L6 (MIRO1_RAT) annotates a single transmembrane helix at positions 606-628 as 'Helical; Anchor for type IV membrane protein' (evidence code ECO:0000255, PIRNR computational prediction). The topological domains confirm: cytoplasmic 1-605, TM 606-628, mitochondrial intermembrane 629-631. The sequence at 606-628 (TFWLRASFGATVFAVVGFAMYRALL) is predominantly hydrophobic, consistent with a single-pass TM anchor. The annotation is computational (PIRNR) rather than experimentally determined, but it is the canonical database annotation."
  },
  "important_caveats": [
    "The UniProt TM annotation (606-628) is computational (ECO:0000255, PIRNR evidence), not experimentally validated. Exact TM boundaries from prediction algorithms can vary by 2-5 residues.",
    "The protein is MIRO-1 (Mitochondrial Rho GTPase), a single-pass type IV membrane protein with its TM anchor in the C-terminus. This family knowledge aids identification but the exact boundary numbers depend on the prediction method.",
    "Option A's inclusion of a second region (456-476) is clearly wrong as that region lies within the EF-hand calcium-binding domain with multiple charged residues.",
    "The sequence matches the UniProt entry exactly (SHA256 confirmed), so positional numbering is reliable."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "C"
    ],
    "reason": "The distinction between B (607-624) and C (606-628) depends on exact boundary determination, which is inherently algorithm-dependent. The UniProt annotation (computational PIRNR) chose 606-628, but a hydrophobicity-based analysis could reasonably argue for 607-624 as the 'core' hydrophobic segment. However, the presence of K629 as a clear polar boundary and the general principle that TM helices extend to interface residues (Y, R) makes C more defensible than B, though B is not unreasonable."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0046",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A1L1L6 (MIRO1_RAT) annotates a single transmembrane helix at positions 606-628 as 'Helical; Anchor for type IV membrane protein' (evidence code ECO:0000255, PIRNR computational prediction). The topological domains confirm: cytoplasmic 1-605, TM 606-628, mitochondrial intermembrane 629-631. The sequence at 606-628 (TFWLRASFGATVFAVVGFAMYRALL) is predominantly hydrophobic, consistent with a single-pass TM anchor. The annotation is computational (PIRNR) rather than experimentally determined, but it is the canonical database annotation.",
    "evidence_ids": ["C6", "C5", "C7", "H3", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The protein is 631 residues with a clear C-terminal hydrophobic stretch. Option D (3-23) is the N-terminus containing charged residues (R, D, K) incompatible with a TM helix. Option A adds a second region (456-476) that falls within the EF-hand/GTPase domain region rich in charged residues (R, K, D, E) and is clearly not transmembrane. Between B (607-624) and C (606-628): the hydrophobic core FWLRASFGATVFAVVGFAMY extends from ~607 to ~624, but general TM helix boundary principles indicate that (1) the helix typically extends to the nearest strongly polar boundary—K629 (lysine) clearly terminates the TM, so the helix should extend past 624 through M625, Y626, R627, A628, L628 (aromatic Y and charged R are commonly found at TM-water interfaces); (2) T606 is a typical boundary residue for TM helices; (3) the 23-residue span (606-628) is within the expected 20-25 residue range for a single-pass TM helix in a lipid bilayer, while B's 18 residues is at the short end. The presence of Y and R at positions 626-627 (aromatic/charged interface residues) and the clear polar break at K629 supports the wider boundary of C.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can identify the C-terminal hydrophobic stretch as the sole TM region, eliminate options A and D based on domain architecture and charge content, and use general TM helix boundary principles (aromatic/charged residues at interfaces, hydrophobic core extent, polar residue boundaries) to favor the 23-residue span C over the 18-residue subset B. The reasoning is probabilistic but concrete and grounded in transferable TM biology."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "C"],
    "reason": "The distinction between B (607-624) and C (606-628) depends on exact boundary determination, which is inherently algorithm-dependent. The UniProt annotation (computational PIRNR) chose 606-628, but a hydrophobicity-based analysis could reasonably argue for 607-624 as the 'core' hydrophobic segment. However, the presence of K629 as a clear polar boundary and the general principle that TM helices extend to interface residues (Y, R) makes C more defensible than B, though B is not unreasonable."
  },
  "important_caveats": [
    "The UniProt TM annotation (606-628) is computational (ECO:0000255, PIRNR evidence), not experimentally validated. Exact TM boundaries from prediction algorithms can vary by 2-5 residues.",
    "The protein is MIRO-1 (Mitochondrial Rho GTPase), a single-pass type IV membrane protein with its TM anchor in the C-terminus. This family knowledge aids identification but the exact boundary numbers depend on the prediction method.",
    "Option A's inclusion of a second region (456-476) is clearly wrong as that region lies within the EF-hand calcium-binding domain with multiple charged residues.",
    "The sequence matches the UniProt entry exactly (SHA256 confirmed), so positional numbering is reliable."
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
  "benchmark_sequence_length": 631,
  "benchmark_sequence_sha256": "a7756948eb1b32092363ec26631ecb58f113dac469b17c79f967f052e05b6ef8",
  "current_entry_audit": {
    "entryVersion": 149,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2007-02-06",
    "sequenceVersion": 1
  },
  "current_record_sha256": "c125ef86885e5aa234ab5686ffd7e9cc9805cc651f4aa85b1cf455ff62ee7ca3",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 631,
  "current_source_sequence_sha256": "a7756948eb1b32092363ec26631ecb58f113dac469b17c79f967f052e05b6ef8",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 147,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A1L1L6",
  "selected_historical_entry_version": 147,
  "selected_historical_record_sha256": "f2d4593a1952b2407eeaa23ae16f133c7086e78f4fa0cdc9464acd586d1a5a5e",
  "selected_historical_source_sequence_length": 631,
  "selected_historical_source_sequence_sha256": "a7756948eb1b32092363ec26631ecb58f113dac469b17c79f967f052e05b6ef8",
  "selected_historical_version": {
    "accession": "A1L1L6",
    "database": "Swiss-Prot",
    "entryVersion": 147,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "MIRO1_RAT",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A1L1L6.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A1L1L6\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:26:46.803603+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c125ef86885e5aa234ab5686ffd7e9cc9805cc651f4aa85b1cf455ff62ee7ca3",
  "url": "https://rest.uniprot.org/uniprotkb/A1L1L6.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A1L1L6.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":149,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2007-02-06\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:26:46.803603+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c125ef86885e5aa234ab5686ffd7e9cc9805cc651f4aa85b1cf455ff62ee7ca3",
  "url": "https://rest.uniprot.org/uniprotkb/A1L1L6.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A1L1L6.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Rat\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"AAI29124.1\",\"source\":\"EMBL\"}],\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Chordata\",\"Craniata\",\"Vertebrata\",\"Euteleostomi\",\"Mammalia\",\"Eutheria\",\"Euarchontoglires\",\"Glires\",\"Rodentia\",\"Myomorpha\",\"Muroidea\",\"Muridae\",\"Murinae\",\"Rattus\"],\"scientificName\":\"Rattus norvegicus\",\"taxonId\":10116}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:26:46.803603+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c125ef86885e5aa234ab5686ffd7e9cc9805cc651f4aa85b1cf455ff62ee7ca3",
  "url": "https://rest.uniprot.org/uniprotkb/A1L1L6.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A1L1L6.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"1307023\",\"source\":\"RGD\"}],\"value\":\"Ras homolog gene family member T1\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8IXI2\",\"source\":\"UniProtKB\"}],\"value\":\"3.6.5.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PIRNR037488\",\"source\":\"PIRNR\"}],\"value\":\"Mitochondrial Rho GTPase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"MIRO-1\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:26:46.803603+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c125ef86885e5aa234ab5686ffd7e9cc9805cc651f4aa85b1cf455ff62ee7ca3",
  "url": "https://rest.uniprot.org/uniprotkb/A1L1L6.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A1L1L6.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":605},\"start\":{\"modifier\":\"EXACT\",\"value\":1}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-02T04:26:46.803603+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c125ef86885e5aa234ab5686ffd7e9cc9805cc651f4aa85b1cf455ff62ee7ca3",
  "url": "https://rest.uniprot.org/uniprotkb/A1L1L6.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A1L1L6.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"Helical; Anchor for type IV membrane protein\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":628},\"start\":{\"modifier\":\"EXACT\",\"value\":606}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-02T04:26:46.803603+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c125ef86885e5aa234ab5686ffd7e9cc9805cc651f4aa85b1cf455ff62ee7ca3",
  "url": "https://rest.uniprot.org/uniprotkb/A1L1L6.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A1L1L6.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"Mitochondrial intermembrane\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":631},\"start\":{\"modifier\":\"EXACT\",\"value\":629}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-02T04:26:46.803603+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c125ef86885e5aa234ab5686ffd7e9cc9805cc651f4aa85b1cf455ff62ee7ca3",
  "url": "https://rest.uniprot.org/uniprotkb/A1L1L6.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A1L1L6?format=txt&versions=147)

```json
{
  "entry_version": 147,
  "evidence_id": "H1",
  "excerpt": "ID   MIRO1_RAT               Reviewed;         631 AA.\nAC   A1L1L6;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   06-FEB-2007, sequence version 1.\nDT   28-JAN-2026, entry version 147.\nDE   RecName: Full=Mitochondrial Rho GTPase {ECO:0000255|PIRNR:PIRNR037488};\nDE            Short=MIRO-1 {ECO:0000305};\nDE            EC=3.6.5.- {ECO:0000250|UniProtKB:Q8IXI2};\nDE   AltName: Full=Ras homolog gene family member T1 {ECO:0000312|RGD:1307023};\nGN   Name=Rhot1 {ECO:0000312|RGD:1307023};\nGN   Synonyms=Rnf135 {ECO:0000312|RGD:1307023};\nOS   Rattus norvegicus (Rat).\nOC   Eukaryota; Metazoa; Chordata; Craniata; Vertebrata; Euteleostomi; Mammalia;\nOC   Eutheria; Euarchontoglires; Glires; Rodentia; Myomorpha; Muroidea; Muridae;\nOC   Murinae; Rattus.\nOX   NCBI_TaxID=10116 {ECO:0000312|EMBL:AAI29124.1};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:49.663865+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f2d4593a1952b2407eeaa23ae16f133c7086e78f4fa0cdc9464acd586d1a5a5e",
  "url": "https://rest.uniprot.org/unisave/A1L1L6?format=txt&versions=147"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A1L1L6?format=txt&versions=147)

```json
{
  "entry_version": 147,
  "evidence_id": "H2",
  "excerpt": "FT   TOPO_DOM        1..605\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:49.663865+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 187-189",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f2d4593a1952b2407eeaa23ae16f133c7086e78f4fa0cdc9464acd586d1a5a5e",
  "url": "https://rest.uniprot.org/unisave/A1L1L6?format=txt&versions=147"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A1L1L6?format=txt&versions=147)

```json
{
  "entry_version": 147,
  "evidence_id": "H3",
  "excerpt": "FT   TRANSMEM        606..628\nFT                   /note=\"Helical; Anchor for type IV membrane protein\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:49.663865+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 190-192",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f2d4593a1952b2407eeaa23ae16f133c7086e78f4fa0cdc9464acd586d1a5a5e",
  "url": "https://rest.uniprot.org/unisave/A1L1L6?format=txt&versions=147"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A1L1L6?format=txt&versions=147)

```json
{
  "entry_version": 147,
  "evidence_id": "H4",
  "excerpt": "FT   TOPO_DOM        629..631\nFT                   /note=\"Mitochondrial intermembrane\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:49.663865+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 193-195",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f2d4593a1952b2407eeaa23ae16f133c7086e78f4fa0cdc9464acd586d1a5a5e",
  "url": "https://rest.uniprot.org/unisave/A1L1L6?format=txt&versions=147"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 46. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
