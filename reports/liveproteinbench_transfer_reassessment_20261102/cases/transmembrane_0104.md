# transmembrane_0104

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/transmembrane_0104.txt)

**Task:** `transmembrane`  
**Expected answer:** **B** — 36..56; 494..514; 525..549; 555..582; 588..619; 623..659; 1075..1098; 1301..1334; 1338..1361; 1368..1394; 1400..1431; 1435..1466

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MFVKNFIHKLKELKQKSLDKFANLLYDYGGYVYDRPCTFIICSLICCLLLTCGFYFKEHEKDIYKLYSISNSYAYETNETINDFFYKSRRCFILVESNVNLLKPKILRELQKFEEGTKDIEVDLSEINECKTNSELPPEQSHVAKELYKTLIQRSEENLKSGKINGSLFDYSDLDENGKSVLSLAGKENNDDTLIEGDNKNDEETSANNNNNEDDNNEDDNNEDDNNEDDNNENDNNNNNEDDNNNDDDDDEDNEEEDEEKQKSLREKLYRKIYEMLKKKKENIVLDENNPNVNFTDYKDDVFYPYQYIPPMLIKADRCKLQNVFGDKNLNIDLREASDGLKKQITYTLEDICEKKYGDCNFSSLFLYYEKGNGYIDYPIKVDNLDFYVNRRTYKEMMFKGILGNMVYEKSGSKYIIKSANAIMTVIPLLNSHTYEPYALAYEKKLIDYVRFYNLDDIIQDEETNDDNDPFIRFHVFTDRSLEDEVDRISKIDNLTRLLLLIGVLLIFMYALFNNVTSVLYRSKPLCAVMGIFCGFLGFLSGSGFLYFLGVKSVPPAETVPFLVIGVGVDDVFVILNSYSLLFMVKDNKKRIQMCLKDSALAITVTTLTNIIAFLISAISPFYSICAFSLFTASSLFFGYLMVLTFLLSFLCIEAKLEKKKRNIFTGTFHLFRSIFMKSSKKNKKENKENNIHDDGDNDNDEKKKDLSLEVKNNEDDYENISIYEWIHNLYLFEESINKKKKNAALVYASNNGMSSNLNNVNEDGFPNPSKIVSMEDVKKRNIKKDDAYINKEDEEGGGYYNKDDNKKKDILGKKQKKNNNNVTLVSKKGEDNELDVYYENLDEKTNDKYKMNNIKSSKLKYDNDKKDGAIINNRPSSDEEYKEEKDKNKINILNDVFNDITIKPNENILLDRGDVIKSSGYDSSYNDLQSSSLPNPSSNEVLNKTTMVYNETDLKDNKKEIKSSKKNVKDIKKSDMIHDDTYDIINSNNKNILLSSNEINNNSNNTNKFNNNSTELATKDTQQFINGHDKNIYLLSSHDNALFYKYIYEEPKGNIGKYFRSLVKNYYVPFLSSRFGKTIVYIMFTIIIAMSIYGCTLMKKGIKYDKAFPVDSYVRRFTTAKIKYFPDFGDFIEVYYFDKHFINKYRGLEKNTKEAASSFLYSDLTDRQIMNSPKINKNVHWENTNLQEELINMHNTLESQEFVTSVANGFTFFLNKNKSSLRKENPQEFYEIFANWLKKDFVGNLFKNDFVFLNGKLVAWRFHYFQKNVDDSEISSKWLKACKQITKLENHNVQMVCFHLSSIFNETDESIIEVTLINLGITILTILVVTAYIIKGFYSCVIIALIIFLIDLCIFGFMCLCGITMNIISMVILVLSVGFSIDHTSHIVQAFSHSMGRTRDEKMKESLHLMIGPVLHSGLSTWFVISTLFFSNKDFTVIFFQTLSLVLFFSITFSSMFLPVLLSSFGPLH

[Multiple Choices]
A. 36..56; 494..514; 525..549; 588..619; 623..659; 1075..1098; 1301..1334; 1338..1361; 1368..1394; 1400..1431; 1435..1466
B. 36..56; 494..514; 525..549; 555..582; 588..619; 623..659; 1075..1098; 1301..1334; 1338..1361; 1368..1394; 1400..1431; 1435..1466
C. 36..56; 494..514; 525..549; 555..582; 593..624; 623..659; 1075..1098; 1301..1334; 1338..1361; 1368..1394; 1400..1431; 1435..1466
D. 13..35
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

> The sequence-matched historical UniProt record annotates the listed transmembrane spans in B, including the 555..582 and 588..619 helices that distinguish B from A and C. Those feature annotations cite PubMed and PDB structural evidence. This supports the key, though the source record is an annotation rather than an independent assessment of the underlying experiments.

Citations as saved: [H7](#evidence-h7), [H9](#evidence-h9), [H11](#evidence-h11), [H13](#evidence-h13), [H15](#evidence-h15), [H17](#evidence-h17), [H23](#evidence-h23), [H25](#evidence-h25), [H27](#evidence-h27), [H29](#evidence-h29), [H31](#evidence-h31), [H33](#evidence-h33).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has repeated long, strongly hydrophobic stretches characteristic of membrane-spanning helices in a multipass membrane protein. In particular, the hydrophobic stretch around 555..582 is present in B and C but omitted from A, while the subsequent strongly hydrophobic run supports a span beginning near 588 rather than the shifted range in C. The N-terminal 13..35 option contains several charged residues and is a poorer match for a membrane-crossing helix than the hydrophobic 36..56 region. These are transferable hydropathy and multipass-transporter patterns, not target-specific annotation recall.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence provides meaningful grounds to distinguish B from the alternatives using the shared biological pattern of hydrophobic membrane helices and intervening less-hydrophobic boundaries. Exact helix endpoints can be uncertain from sequence alone, but the offered alternatives include sufficiently different spans for the hydropathy pattern to favor B.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although exact transmembrane boundaries can be approximate, the alternatives differ in ways that the strong hydrophobic stretches and their boundaries meaningfully distinguish; no second option is comparably supported by the supplied sequence.


### Important caveats

- Reviewer-only evidence reports a sequence match to the cited historical database record, but the author's exact source snapshot is unknown.
- The supporting feature annotations cite PubMed and PDB evidence; this review does not independently reanalyze those experiments or establish every boundary de novo.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has repeated long, strongly hydrophobic stretches characteristic of membrane-spanning helices in a multipass membrane protein. In particular, the hydrophobic stretch around 555..582 is present in B and C but omitted from A, while the subsequent strongly hydrophobic run supports a span beginning near 588 rather than the shifted range in C. The N-terminal 13..35 option contains several charged residues and is a poorer match for a membrane-crossing helix than the hydrophobic 36..56 region. These are transferable hydropathy and multipass-transporter patterns, not target-specific annotation recall.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence provides meaningful grounds to distinguish B from the alternatives using the shared biological pattern of hydrophobic membrane helices and intervening less-hydrophobic boundaries. Exact helix endpoints can be uncertain from sequence alone, but the offered alternatives include sufficiently different spans for the hydropathy pattern to favor B."
  },
  "case_id": "transmembrane_0104",
  "expected_answer_check": {
    "evidence_ids": [
      "H7",
      "H9",
      "H11",
      "H13",
      "H15",
      "H17",
      "H23",
      "H25",
      "H27",
      "H29",
      "H31",
      "H33"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched historical UniProt record annotates the listed transmembrane spans in B, including the 555..582 and 588..619 helices that distinguish B from A and C. Those feature annotations cite PubMed and PDB structural evidence. This supports the key, though the source record is an annotation rather than an independent assessment of the underlying experiments."
  },
  "important_caveats": [
    "Reviewer-only evidence reports a sequence match to the cited historical database record, but the author's exact source snapshot is unknown.",
    "The supporting feature annotations cite PubMed and PDB evidence; this review does not independently reanalyze those experiments or establish every boundary de novo."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although exact transmembrane boundaries can be approximate, the alternatives differ in ways that the strong hydrophobic stretches and their boundaries meaningfully distinguish; no second option is comparably supported by the supplied sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0104",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched historical UniProt record annotates the listed transmembrane spans in B, including the 555..582 and 588..619 helices that distinguish B from A and C. Those feature annotations cite PubMed and PDB structural evidence. This supports the key, though the source record is an annotation rather than an independent assessment of the underlying experiments.",
    "evidence_ids": ["H7", "H9", "H11", "H13", "H15", "H17", "H23", "H25", "H27", "H29", "H31", "H33"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has repeated long, strongly hydrophobic stretches characteristic of membrane-spanning helices in a multipass membrane protein. In particular, the hydrophobic stretch around 555..582 is present in B and C but omitted from A, while the subsequent strongly hydrophobic run supports a span beginning near 588 rather than the shifted range in C. The N-terminal 13..35 option contains several charged residues and is a poorer match for a membrane-crossing helix than the hydrophobic 36..56 region. These are transferable hydropathy and multipass-transporter patterns, not target-specific annotation recall.",
    "missing_item_specific_fact": "",
    "reason": "The sequence provides meaningful grounds to distinguish B from the alternatives using the shared biological pattern of hydrophobic membrane helices and intervening less-hydrophobic boundaries. Exact helix endpoints can be uncertain from sequence alone, but the offered alternatives include sufficiently different spans for the hydropathy pattern to favor B."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although exact transmembrane boundaries can be approximate, the alternatives differ in ways that the strong hydrophobic stretches and their boundaries meaningfully distinguish; no second option is comparably supported by the supplied sequence."
  },
  "important_caveats": [
    "Reviewer-only evidence reports a sequence match to the cited historical database record, but the author's exact source snapshot is unknown.",
    "The supporting feature annotations cite PubMed and PDB evidence; this review does not independently reanalyze those experiments or establish every boundary de novo."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation for Q8I266 (PfNCR1), based on cryo-EM structures (8V0G, 8V12, 8V1G) and PubMed:39693420, lists exactly 12 TRANSMEM (Helical) regions: 36..56, 494..514, 525..549, 555..582, 588..619, 623..659, 1075..1098, 1301..1334, 1338..1361, 1368..1394, 1400..1431, 1435..1466. This matches option B exactly. The INTRAMEM regions (4..34, 664..673, 1058..1073) are correctly excluded from the TRANSMEM list in all options.

Citations as saved: [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [C14](#evidence-c14), [C16](#evidence-c16), [C18](#evidence-c18), [C24](#evidence-c24), [C26](#evidence-c26), [C28](#evidence-c28), [C30](#evidence-c30), [C32](#evidence-c32), [C34](#evidence-c34), [H7](#evidence-h7), [H9](#evidence-h9), [H11](#evidence-h11), [H13](#evidence-h13), [H15](#evidence-h15), [H17](#evidence-h17), [H23](#evidence-h23), [H25](#evidence-h25), [H27](#evidence-h27), [H29](#evidence-h29), [H31](#evidence-h31), [H33](#evidence-h33).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The NPC1/NCR1 transporter family (including human NPC1) is characterized by ~13 transmembrane helices forming a large membrane-embedded transporter. Option D (single 23-residue region) is inconsistent with a multi-pass membrane transporter of this size and family. Hydrophobicity analysis of the sequence should identify the 555..582 segment (a 28-residue hydrophobic stretch between the third and fourth annotated TM regions), eliminating option A which omits it. For the B vs C distinction (588..619 vs 593..624): the short cytoplasmic loop between the 4th and 5th TM helices is only 5 residues (583..587 per the annotation pattern of short inter-helix loops), so the 5th TM helix begins at 588. A hydrophobicity scan showing that residues at positions 588-592 are part of the hydrophobic helix (rather than the polar loop) supports B over C. The overall topology pattern—alternating TM helices separated by very short (3-5 residue) loops—is consistent with the NPC1 fold architecture known from structural studies of human NPC1 and related transporters.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A model can use: (1) family-level knowledge that NPC1/NCR1 is a ~13-TM transporter to eliminate D; (2) hydrophobicity analysis to identify the 555-582 region, eliminating A; (3) the pattern of very short inter-TM loops (3-5 residues typical of NPC1 architecture) to favor B over C. The B vs C boundary distinction (5-residue shift) is at the edge of sequence-based prediction accuracy, but the short-loop pattern (583-587 as the loop, TM starting at 588) provides a transferable structural principle from the NPC1 fold. This is a defensible probabilistic inference rather than exact lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While the B vs C boundary difference is small (5 residues), the overall reasoning path (family architecture, hydrophobicity, loop-length patterns) provides a credible basis for selecting B. Option A is eliminated by the identifiable 555-582 hydrophobic segment, and D is eliminated by the multi-TM family requirement. No two options are equally defensible given the available reasoning.


### Important caveats

- The exact TM boundary positions (e.g., 588 vs 593) are determined by cryo-EM structure at 2.98 Å resolution; sequence-based predictors typically have ±5 residue uncertainty at helix boundaries.
- The UniProt annotation includes INTRAMEM regions (4..34, 664..673, 1058..1073) that are membrane-embedded but not classified as TRANSMEM; none of the options include these, which is consistent with the question asking specifically about TRANSMEM regions.
- The B vs C distinction relies on the assumption that inter-TM loops in the NPC1 fold are very short (3-5 residues); while this is supported by the NPC1 structural family, a model without specific NPC1 fold knowledge might find this boundary genuinely ambiguous.
- The annotation evidence is experimental (cryo-EM + PubMed:39693420), not purely computational, lending high confidence to the ground-truth boundaries.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The NPC1/NCR1 transporter family (including human NPC1) is characterized by ~13 transmembrane helices forming a large membrane-embedded transporter. Option D (single 23-residue region) is inconsistent with a multi-pass membrane transporter of this size and family. Hydrophobicity analysis of the sequence should identify the 555..582 segment (a 28-residue hydrophobic stretch between the third and fourth annotated TM regions), eliminating option A which omits it. For the B vs C distinction (588..619 vs 593..624): the short cytoplasmic loop between the 4th and 5th TM helices is only 5 residues (583..587 per the annotation pattern of short inter-helix loops), so the 5th TM helix begins at 588. A hydrophobicity scan showing that residues at positions 588-592 are part of the hydrophobic helix (rather than the polar loop) supports B over C. The overall topology pattern—alternating TM helices separated by very short (3-5 residue) loops—is consistent with the NPC1 fold architecture known from structural studies of human NPC1 and related transporters.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A model can use: (1) family-level knowledge that NPC1/NCR1 is a ~13-TM transporter to eliminate D; (2) hydrophobicity analysis to identify the 555-582 region, eliminating A; (3) the pattern of very short inter-TM loops (3-5 residues typical of NPC1 architecture) to favor B over C. The B vs C boundary distinction (5-residue shift) is at the edge of sequence-based prediction accuracy, but the short-loop pattern (583-587 as the loop, TM starting at 588) provides a transferable structural principle from the NPC1 fold. This is a defensible probabilistic inference rather than exact lookup."
  },
  "case_id": "transmembrane_0104",
  "expected_answer_check": {
    "evidence_ids": [
      "C8",
      "C10",
      "C12",
      "C14",
      "C16",
      "C18",
      "C24",
      "C26",
      "C28",
      "C30",
      "C32",
      "C34",
      "H7",
      "H9",
      "H11",
      "H13",
      "H15",
      "H17",
      "H23",
      "H25",
      "H27",
      "H29",
      "H31",
      "H33"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation for Q8I266 (PfNCR1), based on cryo-EM structures (8V0G, 8V12, 8V1G) and PubMed:39693420, lists exactly 12 TRANSMEM (Helical) regions: 36..56, 494..514, 525..549, 555..582, 588..619, 623..659, 1075..1098, 1301..1334, 1338..1361, 1368..1394, 1400..1431, 1435..1466. This matches option B exactly. The INTRAMEM regions (4..34, 664..673, 1058..1073) are correctly excluded from the TRANSMEM list in all options."
  },
  "important_caveats": [
    "The exact TM boundary positions (e.g., 588 vs 593) are determined by cryo-EM structure at 2.98 Å resolution; sequence-based predictors typically have ±5 residue uncertainty at helix boundaries.",
    "The UniProt annotation includes INTRAMEM regions (4..34, 664..673, 1058..1073) that are membrane-embedded but not classified as TRANSMEM; none of the options include these, which is consistent with the question asking specifically about TRANSMEM regions.",
    "The B vs C distinction relies on the assumption that inter-TM loops in the NPC1 fold are very short (3-5 residues); while this is supported by the NPC1 structural family, a model without specific NPC1 fold knowledge might find this boundary genuinely ambiguous.",
    "The annotation evidence is experimental (cryo-EM + PubMed:39693420), not purely computational, lending high confidence to the ground-truth boundaries."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While the B vs C boundary difference is small (5 residues), the overall reasoning path (family architecture, hydrophobicity, loop-length patterns) provides a credible basis for selecting B. Option A is eliminated by the identifiable 555-582 hydrophobic segment, and D is eliminated by the multi-TM family requirement. No two options are equally defensible given the available reasoning."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0104",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation for Q8I266 (PfNCR1), based on cryo-EM structures (8V0G, 8V12, 8V1G) and PubMed:39693420, lists exactly 12 TRANSMEM (Helical) regions: 36..56, 494..514, 525..549, 555..582, 588..619, 623..659, 1075..1098, 1301..1334, 1338..1361, 1368..1394, 1400..1431, 1435..1466. This matches option B exactly. The INTRAMEM regions (4..34, 664..673, 1058..1073) are correctly excluded from the TRANSMEM list in all options.",
    "evidence_ids": ["C8", "C10", "C12", "C14", "C16", "C18", "C24", "C26", "C28", "C30", "C32", "C34", "H7", "H9", "H11", "H13", "H15", "H17", "H23", "H25", "H27", "H29", "H31", "H33"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The NPC1/NCR1 transporter family (including human NPC1) is characterized by ~13 transmembrane helices forming a large membrane-embedded transporter. Option D (single 23-residue region) is inconsistent with a multi-pass membrane transporter of this size and family. Hydrophobicity analysis of the sequence should identify the 555..582 segment (a 28-residue hydrophobic stretch between the third and fourth annotated TM regions), eliminating option A which omits it. For the B vs C distinction (588..619 vs 593..624): the short cytoplasmic loop between the 4th and 5th TM helices is only 5 residues (583..587 per the annotation pattern of short inter-helix loops), so the 5th TM helix begins at 588. A hydrophobicity scan showing that residues at positions 588-592 are part of the hydrophobic helix (rather than the polar loop) supports B over C. The overall topology pattern—alternating TM helices separated by very short (3-5 residue) loops—is consistent with the NPC1 fold architecture known from structural studies of human NPC1 and related transporters.",
    "missing_item_specific_fact": "",
    "reason": "A model can use: (1) family-level knowledge that NPC1/NCR1 is a ~13-TM transporter to eliminate D; (2) hydrophobicity analysis to identify the 555-582 region, eliminating A; (3) the pattern of very short inter-TM loops (3-5 residues typical of NPC1 architecture) to favor B over C. The B vs C boundary distinction (5-residue shift) is at the edge of sequence-based prediction accuracy, but the short-loop pattern (583-587 as the loop, TM starting at 588) provides a transferable structural principle from the NPC1 fold. This is a defensible probabilistic inference rather than exact lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While the B vs C boundary difference is small (5 residues), the overall reasoning path (family architecture, hydrophobicity, loop-length patterns) provides a credible basis for selecting B. Option A is eliminated by the identifiable 555-582 hydrophobic segment, and D is eliminated by the multi-TM family requirement. No two options are equally defensible given the available reasoning."
  },
  "important_caveats": [
    "The exact TM boundary positions (e.g., 588 vs 593) are determined by cryo-EM structure at 2.98 Å resolution; sequence-based predictors typically have ±5 residue uncertainty at helix boundaries.",
    "The UniProt annotation includes INTRAMEM regions (4..34, 664..673, 1058..1073) that are membrane-embedded but not classified as TRANSMEM; none of the options include these, which is consistent with the question asking specifically about TRANSMEM regions.",
    "The B vs C distinction relies on the assumption that inter-TM loops in the NPC1 fold are very short (3-5 residues); while this is supported by the NPC1 structural family, a model without specific NPC1 fold knowledge might find this boundary genuinely ambiguous.",
    "The annotation evidence is experimental (cryo-EM + PubMed:39693420), not purely computational, lending high confidence to the ground-truth boundaries."
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
  "benchmark_sequence_length": 1470,
  "benchmark_sequence_sha256": "07ace62be3d6e1b79adbe002f51a2784c4046a9b5a29e38e610e20b3ddca65a1",
  "current_entry_audit": {
    "entryVersion": 126,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2003-03-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "48e01533a9789c0a87e7d04e741324e48211158647115ac991ae6fe921695917",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 1470,
  "current_source_sequence_sha256": "07ace62be3d6e1b79adbe002f51a2784c4046a9b5a29e38e610e20b3ddca65a1",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 124,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q8I266",
  "selected_historical_entry_version": 124,
  "selected_historical_record_sha256": "5da276982e783be3920b7838caf1b7888eb5ee16832af6b303a9fbd38dd05eb7",
  "selected_historical_source_sequence_length": 1470,
  "selected_historical_source_sequence_sha256": "07ace62be3d6e1b79adbe002f51a2784c4046a9b5a29e38e610e20b3ddca65a1",
  "selected_historical_version": {
    "accession": "Q8I266",
    "database": "Swiss-Prot",
    "entryVersion": 124,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "NCR1_PLAF7",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I266.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q8I266\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:32:00.862431+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "48e01533a9789c0a87e7d04e741324e48211158647115ac991ae6fe921695917",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I266.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I266.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":126,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2003-03-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:32:00.862431+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "48e01533a9789c0a87e7d04e741324e48211158647115ac991ae6fe921695917",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I266.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I266.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000001450\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Sar\",\"Alveolata\",\"Apicomplexa\",\"Aconoidasida\",\"Haemosporida\",\"Plasmodiidae\",\"Plasmodium\",\"Laverania\"],\"scientificName\":\"Plasmodium falciparum (isolate 3D7)\",\"taxonId\":36329}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:32:00.862431+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "48e01533a9789c0a87e7d04e741324e48211158647115ac991ae6fe921695917",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I266.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I266.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30888318\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39693420\",\"source\":\"PubMed\"}],\"value\":\"Niemann-Pick type C1-related protein\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39693420\",\"source\":\"PubMed\"}],\"value\":\"NCR1 transporter\"},{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30888318\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39693420\",\"source\":\"PubMed\"}],\"value\":\"PfNCR1\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:32:00.862431+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "48e01533a9789c0a87e7d04e741324e48211158647115ac991ae6fe921695917",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I266.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I266.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":3},\"start\":{\"modifier\":\"EXACT\",\"value\":1}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-02T04:32:00.862431+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "48e01533a9789c0a87e7d04e741324e48211158647115ac991ae6fe921695917",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I266.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I266.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39693420\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8V0G\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8V12\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8V1G\",\"source\":\"PDB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":34},\"start\":{\"modifier\":\"EXACT\",\"value\":4}},\"type\":\"Intramembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-02T04:32:00.862431+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "48e01533a9789c0a87e7d04e741324e48211158647115ac991ae6fe921695917",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I266.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I266.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":35},\"start\":{\"modifier\":\"EXACT\",\"value\":35}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-02T04:32:00.862431+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "48e01533a9789c0a87e7d04e741324e48211158647115ac991ae6fe921695917",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I266.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I266.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39693420\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8V0G\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8V12\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8V1G\",\"source\":\"PDB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":56},\"start\":{\"modifier\":\"EXACT\",\"value\":36}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-02T04:32:00.862431+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "48e01533a9789c0a87e7d04e741324e48211158647115ac991ae6fe921695917",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I266.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I266.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"Extracellular\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":493},\"start\":{\"modifier\":\"EXACT\",\"value\":57}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
  "retrieved_utc": "2026-11-02T04:32:00.862431+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "48e01533a9789c0a87e7d04e741324e48211158647115ac991ae6fe921695917",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I266.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I266.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39693420\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8V0G\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8V12\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8V1G\",\"source\":\"PDB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":514},\"start\":{\"modifier\":\"EXACT\",\"value\":494}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/6",
  "retrieved_utc": "2026-11-02T04:32:00.862431+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "48e01533a9789c0a87e7d04e741324e48211158647115ac991ae6fe921695917",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I266.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I266.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":524},\"start\":{\"modifier\":\"EXACT\",\"value\":515}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/7",
  "retrieved_utc": "2026-11-02T04:32:00.862431+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "48e01533a9789c0a87e7d04e741324e48211158647115ac991ae6fe921695917",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I266.json"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I266.json)

```json
{
  "evidence_id": "C12",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39693420\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8V0G\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8V12\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8V1G\",\"source\":\"PDB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":549},\"start\":{\"modifier\":\"EXACT\",\"value\":525}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/8",
  "retrieved_utc": "2026-11-02T04:32:00.862431+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "48e01533a9789c0a87e7d04e741324e48211158647115ac991ae6fe921695917",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I266.json"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I266.json)

```json
{
  "evidence_id": "C13",
  "excerpt": "{\"description\":\"Extracellular\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":554},\"start\":{\"modifier\":\"EXACT\",\"value\":550}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/9",
  "retrieved_utc": "2026-11-02T04:32:00.862431+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "48e01533a9789c0a87e7d04e741324e48211158647115ac991ae6fe921695917",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I266.json"
}
```

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I266.json)

```json
{
  "evidence_id": "C14",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39693420\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8V0G\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8V12\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8V1G\",\"source\":\"PDB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":582},\"start\":{\"modifier\":\"EXACT\",\"value\":555}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/10",
  "retrieved_utc": "2026-11-02T04:32:00.862431+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "48e01533a9789c0a87e7d04e741324e48211158647115ac991ae6fe921695917",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I266.json"
}
```

### Evidence C15

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I266.json)

```json
{
  "evidence_id": "C15",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":587},\"start\":{\"modifier\":\"EXACT\",\"value\":583}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/11",
  "retrieved_utc": "2026-11-02T04:32:00.862431+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "48e01533a9789c0a87e7d04e741324e48211158647115ac991ae6fe921695917",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I266.json"
}
```

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I266.json)

```json
{
  "evidence_id": "C16",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39693420\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8V0G\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8V12\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8V1G\",\"source\":\"PDB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":619},\"start\":{\"modifier\":\"EXACT\",\"value\":588}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/12",
  "retrieved_utc": "2026-11-02T04:32:00.862431+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "48e01533a9789c0a87e7d04e741324e48211158647115ac991ae6fe921695917",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I266.json"
}
```

### Evidence C17

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I266.json)

```json
{
  "evidence_id": "C17",
  "excerpt": "{\"description\":\"Extracellular\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":622},\"start\":{\"modifier\":\"EXACT\",\"value\":620}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/13",
  "retrieved_utc": "2026-11-02T04:32:00.862431+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "48e01533a9789c0a87e7d04e741324e48211158647115ac991ae6fe921695917",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I266.json"
}
```

### Evidence C18

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I266.json)

```json
{
  "evidence_id": "C18",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39693420\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8V0G\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8V12\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8V1G\",\"source\":\"PDB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":659},\"start\":{\"modifier\":\"EXACT\",\"value\":623}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/14",
  "retrieved_utc": "2026-11-02T04:32:00.862431+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "48e01533a9789c0a87e7d04e741324e48211158647115ac991ae6fe921695917",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I266.json"
}
```

### Evidence C19

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I266.json)

```json
{
  "evidence_id": "C19",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":663},\"start\":{\"modifier\":\"EXACT\",\"value\":660}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/15",
  "retrieved_utc": "2026-11-02T04:32:00.862431+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "48e01533a9789c0a87e7d04e741324e48211158647115ac991ae6fe921695917",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I266.json"
}
```

### Evidence C20

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I266.json)

```json
{
  "evidence_id": "C20",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39693420\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8V0G\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8V12\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8V1G\",\"source\":\"PDB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":673},\"start\":{\"modifier\":\"EXACT\",\"value\":664}},\"type\":\"Intramembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/16",
  "retrieved_utc": "2026-11-02T04:32:00.862431+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "48e01533a9789c0a87e7d04e741324e48211158647115ac991ae6fe921695917",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I266.json"
}
```

### Evidence C21

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I266.json)

```json
{
  "evidence_id": "C21",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":1057},\"start\":{\"modifier\":\"EXACT\",\"value\":674}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/17",
  "retrieved_utc": "2026-11-02T04:32:00.862431+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "48e01533a9789c0a87e7d04e741324e48211158647115ac991ae6fe921695917",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I266.json"
}
```

### Evidence C22

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I266.json)

```json
{
  "evidence_id": "C22",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39693420\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8V0G\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8V12\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8V1G\",\"source\":\"PDB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":1073},\"start\":{\"modifier\":\"EXACT\",\"value\":1058}},\"type\":\"Intramembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/18",
  "retrieved_utc": "2026-11-02T04:32:00.862431+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "48e01533a9789c0a87e7d04e741324e48211158647115ac991ae6fe921695917",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I266.json"
}
```

### Evidence C23

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I266.json)

```json
{
  "evidence_id": "C23",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":1074},\"start\":{\"modifier\":\"EXACT\",\"value\":1074}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/19",
  "retrieved_utc": "2026-11-02T04:32:00.862431+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "48e01533a9789c0a87e7d04e741324e48211158647115ac991ae6fe921695917",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I266.json"
}
```

### Evidence C24

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I266.json)

```json
{
  "evidence_id": "C24",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39693420\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8V0G\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8V12\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8V1G\",\"source\":\"PDB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":1098},\"start\":{\"modifier\":\"EXACT\",\"value\":1075}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/20",
  "retrieved_utc": "2026-11-02T04:32:00.862431+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "48e01533a9789c0a87e7d04e741324e48211158647115ac991ae6fe921695917",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I266.json"
}
```

### Evidence C25

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I266.json)

```json
{
  "evidence_id": "C25",
  "excerpt": "{\"description\":\"Extracellular\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":1300},\"start\":{\"modifier\":\"EXACT\",\"value\":1099}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/21",
  "retrieved_utc": "2026-11-02T04:32:00.862431+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "48e01533a9789c0a87e7d04e741324e48211158647115ac991ae6fe921695917",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I266.json"
}
```

### Evidence C26

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I266.json)

```json
{
  "evidence_id": "C26",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39693420\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8V0G\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8V12\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8V1G\",\"source\":\"PDB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":1334},\"start\":{\"modifier\":\"EXACT\",\"value\":1301}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/22",
  "retrieved_utc": "2026-11-02T04:32:00.862431+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "48e01533a9789c0a87e7d04e741324e48211158647115ac991ae6fe921695917",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I266.json"
}
```

### Evidence C27

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I266.json)

```json
{
  "evidence_id": "C27",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":1337},\"start\":{\"modifier\":\"EXACT\",\"value\":1335}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/23",
  "retrieved_utc": "2026-11-02T04:32:00.862431+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "48e01533a9789c0a87e7d04e741324e48211158647115ac991ae6fe921695917",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I266.json"
}
```

### Evidence C28

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I266.json)

```json
{
  "evidence_id": "C28",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39693420\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8V0G\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8V12\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8V1G\",\"source\":\"PDB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":1361},\"start\":{\"modifier\":\"EXACT\",\"value\":1338}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/24",
  "retrieved_utc": "2026-11-02T04:32:00.862431+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "48e01533a9789c0a87e7d04e741324e48211158647115ac991ae6fe921695917",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I266.json"
}
```

### Evidence C29

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I266.json)

```json
{
  "evidence_id": "C29",
  "excerpt": "{\"description\":\"Extracellular\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":1367},\"start\":{\"modifier\":\"EXACT\",\"value\":1362}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/25",
  "retrieved_utc": "2026-11-02T04:32:00.862431+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "48e01533a9789c0a87e7d04e741324e48211158647115ac991ae6fe921695917",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I266.json"
}
```

### Evidence C30

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I266.json)

```json
{
  "evidence_id": "C30",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39693420\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8V0G\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8V12\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8V1G\",\"source\":\"PDB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":1394},\"start\":{\"modifier\":\"EXACT\",\"value\":1368}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/26",
  "retrieved_utc": "2026-11-02T04:32:00.862431+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "48e01533a9789c0a87e7d04e741324e48211158647115ac991ae6fe921695917",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I266.json"
}
```

### Evidence C31

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I266.json)

```json
{
  "evidence_id": "C31",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":1399},\"start\":{\"modifier\":\"EXACT\",\"value\":1395}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/27",
  "retrieved_utc": "2026-11-02T04:32:00.862431+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "48e01533a9789c0a87e7d04e741324e48211158647115ac991ae6fe921695917",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I266.json"
}
```

### Evidence C32

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I266.json)

```json
{
  "evidence_id": "C32",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39693420\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8V0G\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8V12\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8V1G\",\"source\":\"PDB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":1431},\"start\":{\"modifier\":\"EXACT\",\"value\":1400}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/28",
  "retrieved_utc": "2026-11-02T04:32:00.862431+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "48e01533a9789c0a87e7d04e741324e48211158647115ac991ae6fe921695917",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I266.json"
}
```

### Evidence C33

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I266.json)

```json
{
  "evidence_id": "C33",
  "excerpt": "{\"description\":\"Extracellular\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":1434},\"start\":{\"modifier\":\"EXACT\",\"value\":1432}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/29",
  "retrieved_utc": "2026-11-02T04:32:00.862431+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "48e01533a9789c0a87e7d04e741324e48211158647115ac991ae6fe921695917",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I266.json"
}
```

### Evidence C34

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I266.json)

```json
{
  "evidence_id": "C34",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39693420\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8V0G\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8V12\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8V1G\",\"source\":\"PDB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":1466},\"start\":{\"modifier\":\"EXACT\",\"value\":1435}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/30",
  "retrieved_utc": "2026-11-02T04:32:00.862431+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "48e01533a9789c0a87e7d04e741324e48211158647115ac991ae6fe921695917",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I266.json"
}
```

### Evidence C35

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I266.json)

```json
{
  "evidence_id": "C35",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":1470},\"start\":{\"modifier\":\"EXACT\",\"value\":1467}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/31",
  "retrieved_utc": "2026-11-02T04:32:00.862431+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "48e01533a9789c0a87e7d04e741324e48211158647115ac991ae6fe921695917",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I266.json"
}
```

### Evidence C36

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I266.json)

```json
{
  "evidence_id": "C36",
  "excerpt": "{\"citation\":{\"authors\":[\"Istvan E.S.\",\"Das S.\",\"Bhatnagar S.\",\"Beck J.R.\",\"Owen E.\",\"Llinas M.\",\"Ganesan S.M.\",\"Niles J.C.\",\"Winzeler E.\",\"Vaidya A.B.\",\"Goldberg D.E.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"30888318\"},{\"database\":\"DOI\",\"id\":\"10.7554/elife.40529\"}],\"citationType\":\"journal article\",\"firstPage\":\"0\",\"id\":\"30888318\",\"journal\":\"Elife\",\"lastPage\":\"0\",\"publicationDate\":\"2019\",\"title\":\"Plasmodium Niemann-Pick type C1-related protein is a druggable target required for parasite membrane homeostasis.\",\"volume\":\"8\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"SUBCELLULAR LOCATION\",\"DISRUPTION PHENOTYPE\",\"MUTAGENESIS OF ALA-1108; ALA-1208 AND PHE-1436\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-02T04:32:00.862431+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "48e01533a9789c0a87e7d04e741324e48211158647115ac991ae6fe921695917",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I266.json"
}
```

### Evidence C37

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I266.json)

```json
{
  "evidence_id": "C37",
  "excerpt": "{\"citation\":{\"authors\":[\"Zhang Z.\",\"Lyu M.\",\"Han X.\",\"Bandara S.\",\"Cui M.\",\"Istvan E.S.\",\"Geng X.\",\"Tringides M.L.\",\"Gregor W.D.\",\"Miyagi M.\",\"Oberstaller J.\",\"Adams J.H.\",\"Zhang Y.\",\"Nieman M.T.\",\"von Lintig J.\",\"Goldberg D.E.\",\"Yu E.W.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39693420\"},{\"database\":\"DOI\",\"id\":\"10.1126/sciadv.adq6651\"}],\"citationType\":\"journal article\",\"firstPage\":\"eadq6651\",\"id\":\"39693420\",\"journal\":\"Sci. Adv.\",\"lastPage\":\"eadq6651\",\"publicationDate\":\"2024\",\"title\":\"The Plasmodium falciparum NCR1 transporter is an antimalarial target that exports cholesterol from the parasite's plasma membrane.\",\"volume\":\"10\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8V0G\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8V12\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8V1G\",\"source\":\"PDB\"}],\"referenceNumber\":4,\"referencePositions\":[\"STRUCTURE BY ELECTRON MICROSCOPY (2.98 ANGSTROMS) IN COMPLEX WITH CHOLESTEROL AND SYNTHETIC INHIBITOR MMV009108\",\"FUNCTION\",\"TRANSPORTER ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"SUBCELLULAR LOCATION\",\"GLYCOSYLATION AT ASN-165 AND ASN-294\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-02T04:32:00.862431+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "48e01533a9789c0a87e7d04e741324e48211158647115ac991ae6fe921695917",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I266.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I266?format=txt&versions=124)

```json
{
  "entry_version": 124,
  "evidence_id": "H1",
  "excerpt": "ID   NCR1_PLAF7              Reviewed;        1470 AA.\nAC   Q8I266;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-MAR-2003, sequence version 1.\nDT   28-JAN-2026, entry version 124.\nDE   RecName: Full=Niemann-Pick type C1-related protein {ECO:0000303|PubMed:30888318, ECO:0000303|PubMed:39693420};\nDE            Short=NCR1 transporter {ECO:0000303|PubMed:39693420};\nDE            Short=PfNCR1 {ECO:0000303|PubMed:30888318, ECO:0000303|PubMed:39693420};\nGN   Name=NCR1 {ECO:0000305};\nGN   ORFNames=PF3D7_0107500 {ECO:0000312|EMBL:CAD49035.1};\nOS   Plasmodium falciparum (isolate 3D7).\nOC   Eukaryota; Sar; Alveolata; Apicomplexa; Aconoidasida; Haemosporida;\nOC   Plasmodiidae; Plasmodium; Plasmodium (Laverania).\nOX   NCBI_TaxID=36329 {ECO:0000312|Proteomes:UP000001450};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:03.056916+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5da276982e783be3920b7838caf1b7888eb5ee16832af6b303a9fbd38dd05eb7",
  "url": "https://rest.uniprot.org/unisave/Q8I266?format=txt&versions=124"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I266?format=txt&versions=124)

```json
{
  "entry_version": 124,
  "evidence_id": "H2",
  "excerpt": "RN   [3] {ECO:0000305}\nRP   FUNCTION, SUBCELLULAR LOCATION, DISRUPTION PHENOTYPE, AND MUTAGENESIS OF\nRP   ALA-1108; ALA-1208 AND PHE-1436.\nRX   PubMed=30888318; DOI=10.7554/elife.40529;\nRA   Istvan E.S., Das S., Bhatnagar S., Beck J.R., Owen E., Llinas M.,\nRA   Ganesan S.M., Niles J.C., Winzeler E., Vaidya A.B., Goldberg D.E.;\nRT   \"Plasmodium Niemann-Pick type C1-related protein is a druggable target\nRT   required for parasite membrane homeostasis.\";\nRL   Elife 8:0-0(2019).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:03.056916+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 49-57",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5da276982e783be3920b7838caf1b7888eb5ee16832af6b303a9fbd38dd05eb7",
  "url": "https://rest.uniprot.org/unisave/Q8I266?format=txt&versions=124"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I266?format=txt&versions=124)

```json
{
  "entry_version": 124,
  "evidence_id": "H3",
  "excerpt": "RN   [4] {ECO:0007744|PDB:8V0G, ECO:0007744|PDB:8V12, ECO:0007744|PDB:8V1G}\nRP   STRUCTURE BY ELECTRON MICROSCOPY (2.98 ANGSTROMS) IN COMPLEX WITH\nRP   CHOLESTEROL AND SYNTHETIC INHIBITOR MMV009108, FUNCTION, TRANSPORTER\nRP   ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, SUBCELLULAR LOCATION, AND\nRP   GLYCOSYLATION AT ASN-165 AND ASN-294.\nRX   PubMed=39693420; DOI=10.1126/sciadv.adq6651;\nRA   Zhang Z., Lyu M., Han X., Bandara S., Cui M., Istvan E.S., Geng X.,\nRA   Tringides M.L., Gregor W.D., Miyagi M., Oberstaller J., Adams J.H.,\nRA   Zhang Y., Nieman M.T., von Lintig J., Goldberg D.E., Yu E.W.;\nRT   \"The Plasmodium falciparum NCR1 transporter is an antimalarial target that\nRT   exports cholesterol from the parasite's plasma membrane.\";\nRL   Sci. Adv. 10:eadq6651-eadq6651(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:03.056916+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 58-69",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5da276982e783be3920b7838caf1b7888eb5ee16832af6b303a9fbd38dd05eb7",
  "url": "https://rest.uniprot.org/unisave/Q8I266?format=txt&versions=124"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I266?format=txt&versions=124)

```json
{
  "entry_version": 124,
  "evidence_id": "H4",
  "excerpt": "FT   TOPO_DOM        1..3\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:03.056916+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 146-148",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5da276982e783be3920b7838caf1b7888eb5ee16832af6b303a9fbd38dd05eb7",
  "url": "https://rest.uniprot.org/unisave/Q8I266?format=txt&versions=124"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I266?format=txt&versions=124)

```json
{
  "entry_version": 124,
  "evidence_id": "H5",
  "excerpt": "FT   INTRAMEM        4..34\nFT                   /evidence=\"ECO:0000269|PubMed:39693420,\nFT                   ECO:0007744|PDB:8V0G, ECO:0007744|PDB:8V12,\nFT                   ECO:0007744|PDB:8V1G\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:03.056916+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 149-152",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5da276982e783be3920b7838caf1b7888eb5ee16832af6b303a9fbd38dd05eb7",
  "url": "https://rest.uniprot.org/unisave/Q8I266?format=txt&versions=124"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I266?format=txt&versions=124)

```json
{
  "entry_version": 124,
  "evidence_id": "H6",
  "excerpt": "FT   TOPO_DOM        35\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:03.056916+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 153-155",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5da276982e783be3920b7838caf1b7888eb5ee16832af6b303a9fbd38dd05eb7",
  "url": "https://rest.uniprot.org/unisave/Q8I266?format=txt&versions=124"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I266?format=txt&versions=124)

```json
{
  "entry_version": 124,
  "evidence_id": "H7",
  "excerpt": "FT   TRANSMEM        36..56\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000269|PubMed:39693420,\nFT                   ECO:0007744|PDB:8V0G, ECO:0007744|PDB:8V12,\nFT                   ECO:0007744|PDB:8V1G\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:03.056916+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 156-160",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5da276982e783be3920b7838caf1b7888eb5ee16832af6b303a9fbd38dd05eb7",
  "url": "https://rest.uniprot.org/unisave/Q8I266?format=txt&versions=124"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I266?format=txt&versions=124)

```json
{
  "entry_version": 124,
  "evidence_id": "H8",
  "excerpt": "FT   TOPO_DOM        57..493\nFT                   /note=\"Extracellular\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:03.056916+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 161-163",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5da276982e783be3920b7838caf1b7888eb5ee16832af6b303a9fbd38dd05eb7",
  "url": "https://rest.uniprot.org/unisave/Q8I266?format=txt&versions=124"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I266?format=txt&versions=124)

```json
{
  "entry_version": 124,
  "evidence_id": "H9",
  "excerpt": "FT   TRANSMEM        494..514\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000269|PubMed:39693420,\nFT                   ECO:0007744|PDB:8V0G, ECO:0007744|PDB:8V12,\nFT                   ECO:0007744|PDB:8V1G\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:03.056916+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 164-168",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5da276982e783be3920b7838caf1b7888eb5ee16832af6b303a9fbd38dd05eb7",
  "url": "https://rest.uniprot.org/unisave/Q8I266?format=txt&versions=124"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I266?format=txt&versions=124)

```json
{
  "entry_version": 124,
  "evidence_id": "H10",
  "excerpt": "FT   TOPO_DOM        515..524\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:03.056916+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 169-171",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5da276982e783be3920b7838caf1b7888eb5ee16832af6b303a9fbd38dd05eb7",
  "url": "https://rest.uniprot.org/unisave/Q8I266?format=txt&versions=124"
}
```

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I266?format=txt&versions=124)

```json
{
  "entry_version": 124,
  "evidence_id": "H11",
  "excerpt": "FT   TRANSMEM        525..549\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000269|PubMed:39693420,\nFT                   ECO:0007744|PDB:8V0G, ECO:0007744|PDB:8V12,\nFT                   ECO:0007744|PDB:8V1G\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:03.056916+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 172-176",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5da276982e783be3920b7838caf1b7888eb5ee16832af6b303a9fbd38dd05eb7",
  "url": "https://rest.uniprot.org/unisave/Q8I266?format=txt&versions=124"
}
```

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I266?format=txt&versions=124)

```json
{
  "entry_version": 124,
  "evidence_id": "H12",
  "excerpt": "FT   TOPO_DOM        550..554\nFT                   /note=\"Extracellular\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:03.056916+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 177-179",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5da276982e783be3920b7838caf1b7888eb5ee16832af6b303a9fbd38dd05eb7",
  "url": "https://rest.uniprot.org/unisave/Q8I266?format=txt&versions=124"
}
```

### Evidence H13

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I266?format=txt&versions=124)

```json
{
  "entry_version": 124,
  "evidence_id": "H13",
  "excerpt": "FT   TRANSMEM        555..582\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000269|PubMed:39693420,\nFT                   ECO:0007744|PDB:8V0G, ECO:0007744|PDB:8V12,\nFT                   ECO:0007744|PDB:8V1G\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:03.056916+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 180-184",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5da276982e783be3920b7838caf1b7888eb5ee16832af6b303a9fbd38dd05eb7",
  "url": "https://rest.uniprot.org/unisave/Q8I266?format=txt&versions=124"
}
```

### Evidence H14

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I266?format=txt&versions=124)

```json
{
  "entry_version": 124,
  "evidence_id": "H14",
  "excerpt": "FT   TOPO_DOM        583..587\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:03.056916+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 185-187",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5da276982e783be3920b7838caf1b7888eb5ee16832af6b303a9fbd38dd05eb7",
  "url": "https://rest.uniprot.org/unisave/Q8I266?format=txt&versions=124"
}
```

### Evidence H15

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I266?format=txt&versions=124)

```json
{
  "entry_version": 124,
  "evidence_id": "H15",
  "excerpt": "FT   TRANSMEM        588..619\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000269|PubMed:39693420,\nFT                   ECO:0007744|PDB:8V0G, ECO:0007744|PDB:8V12,\nFT                   ECO:0007744|PDB:8V1G\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:03.056916+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 188-192",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5da276982e783be3920b7838caf1b7888eb5ee16832af6b303a9fbd38dd05eb7",
  "url": "https://rest.uniprot.org/unisave/Q8I266?format=txt&versions=124"
}
```

### Evidence H16

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I266?format=txt&versions=124)

```json
{
  "entry_version": 124,
  "evidence_id": "H16",
  "excerpt": "FT   TOPO_DOM        620..622\nFT                   /note=\"Extracellular\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:03.056916+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 193-195",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5da276982e783be3920b7838caf1b7888eb5ee16832af6b303a9fbd38dd05eb7",
  "url": "https://rest.uniprot.org/unisave/Q8I266?format=txt&versions=124"
}
```

### Evidence H17

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I266?format=txt&versions=124)

```json
{
  "entry_version": 124,
  "evidence_id": "H17",
  "excerpt": "FT   TRANSMEM        623..659\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000269|PubMed:39693420,\nFT                   ECO:0007744|PDB:8V0G, ECO:0007744|PDB:8V12,\nFT                   ECO:0007744|PDB:8V1G\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:03.056916+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 196-200",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5da276982e783be3920b7838caf1b7888eb5ee16832af6b303a9fbd38dd05eb7",
  "url": "https://rest.uniprot.org/unisave/Q8I266?format=txt&versions=124"
}
```

### Evidence H18

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I266?format=txt&versions=124)

```json
{
  "entry_version": 124,
  "evidence_id": "H18",
  "excerpt": "FT   TOPO_DOM        660..663\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:03.056916+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 201-203",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5da276982e783be3920b7838caf1b7888eb5ee16832af6b303a9fbd38dd05eb7",
  "url": "https://rest.uniprot.org/unisave/Q8I266?format=txt&versions=124"
}
```

### Evidence H19

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I266?format=txt&versions=124)

```json
{
  "entry_version": 124,
  "evidence_id": "H19",
  "excerpt": "FT   INTRAMEM        664..673\nFT                   /evidence=\"ECO:0000269|PubMed:39693420,\nFT                   ECO:0007744|PDB:8V0G, ECO:0007744|PDB:8V12,\nFT                   ECO:0007744|PDB:8V1G\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:03.056916+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 204-207",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5da276982e783be3920b7838caf1b7888eb5ee16832af6b303a9fbd38dd05eb7",
  "url": "https://rest.uniprot.org/unisave/Q8I266?format=txt&versions=124"
}
```

### Evidence H20

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I266?format=txt&versions=124)

```json
{
  "entry_version": 124,
  "evidence_id": "H20",
  "excerpt": "FT   TOPO_DOM        674..1057\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:03.056916+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 208-210",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5da276982e783be3920b7838caf1b7888eb5ee16832af6b303a9fbd38dd05eb7",
  "url": "https://rest.uniprot.org/unisave/Q8I266?format=txt&versions=124"
}
```

### Evidence H21

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I266?format=txt&versions=124)

```json
{
  "entry_version": 124,
  "evidence_id": "H21",
  "excerpt": "FT   INTRAMEM        1058..1073\nFT                   /evidence=\"ECO:0000269|PubMed:39693420,\nFT                   ECO:0007744|PDB:8V0G, ECO:0007744|PDB:8V12,\nFT                   ECO:0007744|PDB:8V1G\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:03.056916+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 211-214",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5da276982e783be3920b7838caf1b7888eb5ee16832af6b303a9fbd38dd05eb7",
  "url": "https://rest.uniprot.org/unisave/Q8I266?format=txt&versions=124"
}
```

### Evidence H22

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I266?format=txt&versions=124)

```json
{
  "entry_version": 124,
  "evidence_id": "H22",
  "excerpt": "FT   TOPO_DOM        1074\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:03.056916+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 215-217",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5da276982e783be3920b7838caf1b7888eb5ee16832af6b303a9fbd38dd05eb7",
  "url": "https://rest.uniprot.org/unisave/Q8I266?format=txt&versions=124"
}
```

### Evidence H23

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I266?format=txt&versions=124)

```json
{
  "entry_version": 124,
  "evidence_id": "H23",
  "excerpt": "FT   TRANSMEM        1075..1098\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000269|PubMed:39693420,\nFT                   ECO:0007744|PDB:8V0G, ECO:0007744|PDB:8V12,\nFT                   ECO:0007744|PDB:8V1G\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:03.056916+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 218-222",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5da276982e783be3920b7838caf1b7888eb5ee16832af6b303a9fbd38dd05eb7",
  "url": "https://rest.uniprot.org/unisave/Q8I266?format=txt&versions=124"
}
```

### Evidence H24

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I266?format=txt&versions=124)

```json
{
  "entry_version": 124,
  "evidence_id": "H24",
  "excerpt": "FT   TOPO_DOM        1099..1300\nFT                   /note=\"Extracellular\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:03.056916+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 223-225",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5da276982e783be3920b7838caf1b7888eb5ee16832af6b303a9fbd38dd05eb7",
  "url": "https://rest.uniprot.org/unisave/Q8I266?format=txt&versions=124"
}
```

### Evidence H25

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I266?format=txt&versions=124)

```json
{
  "entry_version": 124,
  "evidence_id": "H25",
  "excerpt": "FT   TRANSMEM        1301..1334\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000269|PubMed:39693420,\nFT                   ECO:0007744|PDB:8V0G, ECO:0007744|PDB:8V12,\nFT                   ECO:0007744|PDB:8V1G\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:03.056916+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 226-230",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5da276982e783be3920b7838caf1b7888eb5ee16832af6b303a9fbd38dd05eb7",
  "url": "https://rest.uniprot.org/unisave/Q8I266?format=txt&versions=124"
}
```

### Evidence H26

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I266?format=txt&versions=124)

```json
{
  "entry_version": 124,
  "evidence_id": "H26",
  "excerpt": "FT   TOPO_DOM        1335..1337\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:03.056916+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 231-233",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5da276982e783be3920b7838caf1b7888eb5ee16832af6b303a9fbd38dd05eb7",
  "url": "https://rest.uniprot.org/unisave/Q8I266?format=txt&versions=124"
}
```

### Evidence H27

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I266?format=txt&versions=124)

```json
{
  "entry_version": 124,
  "evidence_id": "H27",
  "excerpt": "FT   TRANSMEM        1338..1361\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000269|PubMed:39693420,\nFT                   ECO:0007744|PDB:8V0G, ECO:0007744|PDB:8V12,\nFT                   ECO:0007744|PDB:8V1G\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:03.056916+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 234-238",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5da276982e783be3920b7838caf1b7888eb5ee16832af6b303a9fbd38dd05eb7",
  "url": "https://rest.uniprot.org/unisave/Q8I266?format=txt&versions=124"
}
```

### Evidence H28

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I266?format=txt&versions=124)

```json
{
  "entry_version": 124,
  "evidence_id": "H28",
  "excerpt": "FT   TOPO_DOM        1362..1367\nFT                   /note=\"Extracellular\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:03.056916+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 239-241",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5da276982e783be3920b7838caf1b7888eb5ee16832af6b303a9fbd38dd05eb7",
  "url": "https://rest.uniprot.org/unisave/Q8I266?format=txt&versions=124"
}
```

### Evidence H29

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I266?format=txt&versions=124)

```json
{
  "entry_version": 124,
  "evidence_id": "H29",
  "excerpt": "FT   TRANSMEM        1368..1394\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000269|PubMed:39693420,\nFT                   ECO:0007744|PDB:8V0G, ECO:0007744|PDB:8V12,\nFT                   ECO:0007744|PDB:8V1G\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:03.056916+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 242-246",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5da276982e783be3920b7838caf1b7888eb5ee16832af6b303a9fbd38dd05eb7",
  "url": "https://rest.uniprot.org/unisave/Q8I266?format=txt&versions=124"
}
```

### Evidence H30

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I266?format=txt&versions=124)

```json
{
  "entry_version": 124,
  "evidence_id": "H30",
  "excerpt": "FT   TOPO_DOM        1395..1399\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:03.056916+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 247-249",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5da276982e783be3920b7838caf1b7888eb5ee16832af6b303a9fbd38dd05eb7",
  "url": "https://rest.uniprot.org/unisave/Q8I266?format=txt&versions=124"
}
```

### Evidence H31

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I266?format=txt&versions=124)

```json
{
  "entry_version": 124,
  "evidence_id": "H31",
  "excerpt": "FT   TRANSMEM        1400..1431\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000269|PubMed:39693420,\nFT                   ECO:0007744|PDB:8V0G, ECO:0007744|PDB:8V12,\nFT                   ECO:0007744|PDB:8V1G\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:03.056916+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 250-254",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5da276982e783be3920b7838caf1b7888eb5ee16832af6b303a9fbd38dd05eb7",
  "url": "https://rest.uniprot.org/unisave/Q8I266?format=txt&versions=124"
}
```

### Evidence H32

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I266?format=txt&versions=124)

```json
{
  "entry_version": 124,
  "evidence_id": "H32",
  "excerpt": "FT   TOPO_DOM        1432..1434\nFT                   /note=\"Extracellular\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:03.056916+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 255-257",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5da276982e783be3920b7838caf1b7888eb5ee16832af6b303a9fbd38dd05eb7",
  "url": "https://rest.uniprot.org/unisave/Q8I266?format=txt&versions=124"
}
```

### Evidence H33

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I266?format=txt&versions=124)

```json
{
  "entry_version": 124,
  "evidence_id": "H33",
  "excerpt": "FT   TRANSMEM        1435..1466\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000269|PubMed:39693420,\nFT                   ECO:0007744|PDB:8V0G, ECO:0007744|PDB:8V12,\nFT                   ECO:0007744|PDB:8V1G\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:03.056916+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 258-262",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5da276982e783be3920b7838caf1b7888eb5ee16832af6b303a9fbd38dd05eb7",
  "url": "https://rest.uniprot.org/unisave/Q8I266?format=txt&versions=124"
}
```

### Evidence H34

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I266?format=txt&versions=124)

```json
{
  "entry_version": 124,
  "evidence_id": "H34",
  "excerpt": "FT   TOPO_DOM        1467..1470\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:03.056916+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 263-265",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5da276982e783be3920b7838caf1b7888eb5ee16832af6b303a9fbd38dd05eb7",
  "url": "https://rest.uniprot.org/unisave/Q8I266?format=txt&versions=124"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 104. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
