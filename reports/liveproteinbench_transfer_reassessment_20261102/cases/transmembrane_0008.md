# transmembrane_0008

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/transmembrane_0008.txt)

**Task:** `transmembrane`  
**Expected answer:** **A** — 157..177; 412..432; 448..468; 478..498; 516..536; 545..565; 789..809; 986..1006; 1013..1033; 1037..1057; 1080..1100; 1114..1134

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | uncertain |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MEKNCNSVAGHAGTLVKASSRQADDKAGSRVPPGGHLLQTNKTESQLLPCASPSDPVHWTNEIVPVVADTSAPAEAAPDQTVSDGEQLTRAPDETYYQRSESLAEPPAENELPAGRSRRRRSRWCLGCGCFEQVKTVVLRMLMTGFEKYAGVVYDHPWLFIMVSLLATAGMSVGIFLRTPESDVYTLYSLSGSPSQVTKEHLLDVLPPDRLLFVLLTGTSNLVTRETVTRIDSLLQGIESITLRRDSVTTDEFNHRLVSHDRSPFPETITFQDICAKDGSGKCQVQSILDLYPSSSAWGVMPIASASWPVVTNPVTHKVSRLDAILGKITTSVRLAEQGSGRPALTVVEEAEAMLMRIDLRGETIWKPYTAAFEKLVLDYVLGQDFGPDISVTAKAERSSYDELKRVSTLDVVEWLRLCAAVLVVFLYTSVVNSSKTHRTKLVPSAMGALASLLGYLGGAGLVYLCGVRHTTPAEATPFLAIGIGVDDLFVIINAYSLTYLHPNPKERVVDAIRDAGLSITITTLTNVITFIIGALSPYYSISMFCIITAGALTWGYVLCLTFFLAGLSLDARREARKEPLSYSLFWRFMPRCCRKSSYEPQLSPPLPLTAAASGLEEMRNESEEIVTADQTPPTHGGDLLTTYQLAALMVLYKKHTCQSRSSQPARRLFDRRDGTGTEETMSTPVPEDSERDRTNQKSCGTQVSTGIVDVRETGQDAASQRRLSSHIRDMTTQESIMLLKNFEKEMEQNPEKLLKLYHPEPLGNPGRGSRRFFRDYYGRFLGNTFVKATVLVIFAAVTALAIYGATTLKFGLSLKNITPQASYLRDFYSLHEDLFPSYGDEVTVFFAENDRWEDREVQMRYLQMVKELSEQEWAVVVTDGMSLFLQHAMPSLHSGNRKEFLALLKTWLEGDPIGQNFSTFFKFSFDNLIVWQFRYWMPHRDNTTTLYYWLKEGKDIVSAGKPYFHGEVHTALAVIWESDPKILPFTLTNLSIALVCILAISLLLIPDLTSAIIVVLVVSLVDLWLFGFMALIDLPLSMISMVNLLISIGYSVDFTIHVAHTFTHCVGASRKDRMVETMIVMGAPVTHGMLSTLLSILALAGSPKYILEVFFKMMFMVIVFAYTAGMVLLPVVLTLLGPFHPHGKRESGKAIACDSSAQLIDMEPLHGTGKEEHGVGV

[Multiple Choices]
A. 157..177; 412..432; 448..468; 478..498; 516..536; 545..565; 789..809; 986..1006; 1013..1033; 1037..1057; 1080..1100; 1114..1134
B. 157..177; 412..432; 448..468; 478..498; 516..536; 545..565; 789..809; 988..1007; 1013..1033; 1037..1057; 1080..1100; 1114..1134
C. 308..328; 344..364; 474..494; 533..553; 640..660; 670..690; 731..751; 771..791; 807..827; 851..871; 937..957; 1162..1182; 1209..1229; 1244..1264; 1306..1326; 1381..1401; 1422..1442; 1498..1518; 1532..1552; 1561..1581; 1633..1653; 1671..1691; 1722..1742
D. 157..177; 448..468; 478..498; 516..536; 545..565; 789..809; 986..1006; 1013..1033; 1037..1057; 1080..1100; 1114..1134
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

> The sequence-matched historical UniProt record annotates all 12 regions listed in A as transmembrane helices. These annotations carry evidence code ECO:0000255, indicating computational annotation rather than direct experimental confirmation.

Citations as saved: [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8), [H9](#evidence-h9), [H10](#evidence-h10), [H11](#evidence-h11), [H12](#evidence-h12), [H13](#evidence-h13), [H14](#evidence-h14).

### Reasoning versus lookup: uncertain

**Discriminating biological argument**

> The sequence contains multiple strongly hydrophobic stretches, supporting a polytopic membrane protein and distinguishing the plausible multi-helix sets from C, whose coordinates exceed the 1178-residue sequence. But A and B differ only slightly in the boundaries of one hydrophobic helix.


**Missing item-specific fact**

> The exact boundary convention or annotation used to prefer A's coordinates over B's; that preference is not biologically distinguishable from the sequence alone.


**Reason**

> Transferable sequence and membrane-protein knowledge supports the general helix pattern, but does not meaningfully resolve the small boundary shift between A and B. That shift is also too minor to make one biologically incorrect; reproducing the key's exact preference would require its boundary annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> A and B identify nearly the same hydrophobic helix set and differ only by a small shift in one helix's endpoints. Such membrane-helix boundaries are not reliably distinguishable at this precision from the sequence and are both defensible.


### Important caveats

- The supplied evidence supports the key through a computational database annotation, not an independently verified experimental topology.
- The database annotation matches the supplied sequence, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains multiple strongly hydrophobic stretches, supporting a polytopic membrane protein and distinguishing the plausible multi-helix sets from C, whose coordinates exceed the 1178-residue sequence. But A and B differ only slightly in the boundaries of one hydrophobic helix.",
    "judgment": "cannot_determine",
    "missing_item_specific_fact": "The exact boundary convention or annotation used to prefer A's coordinates over B's; that preference is not biologically distinguishable from the sequence alone.",
    "reason": "Transferable sequence and membrane-protein knowledge supports the general helix pattern, but does not meaningfully resolve the small boundary shift between A and B. That shift is also too minor to make one biologically incorrect; reproducing the key's exact preference would require its boundary annotation."
  },
  "case_id": "transmembrane_0008",
  "expected_answer_check": {
    "evidence_ids": [
      "H3",
      "H4",
      "H5",
      "H6",
      "H7",
      "H8",
      "H9",
      "H10",
      "H11",
      "H12",
      "H13",
      "H14"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched historical UniProt record annotates all 12 regions listed in A as transmembrane helices. These annotations carry evidence code ECO:0000255, indicating computational annotation rather than direct experimental confirmation."
  },
  "important_caveats": [
    "The supplied evidence supports the key through a computational database annotation, not an independently verified experimental topology.",
    "The database annotation matches the supplied sequence, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "A and B identify nearly the same hydrophobic helix set and differ only by a small shift in one helix's endpoints. Such membrane-helix boundaries are not reliably distinguishable at this precision from the sequence and are both defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0008",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched historical UniProt record annotates all 12 regions listed in A as transmembrane helices. These annotations carry evidence code ECO:0000255, indicating computational annotation rather than direct experimental confirmation.",
    "evidence_ids": ["H3", "H4", "H5", "H6", "H7", "H8", "H9", "H10", "H11", "H12", "H13", "H14"]
  },
  "answerability_check": {
    "judgment": "cannot_determine",
    "discriminating_biological_argument": "The sequence contains multiple strongly hydrophobic stretches, supporting a polytopic membrane protein and distinguishing the plausible multi-helix sets from C, whose coordinates exceed the 1178-residue sequence. But A and B differ only slightly in the boundaries of one hydrophobic helix.",
    "missing_item_specific_fact": "The exact boundary convention or annotation used to prefer A's coordinates over B's; that preference is not biologically distinguishable from the sequence alone.",
    "reason": "Transferable sequence and membrane-protein knowledge supports the general helix pattern, but does not meaningfully resolve the small boundary shift between A and B. That shift is also too minor to make one biologically incorrect; reproducing the key's exact preference would require its boundary annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "A and B identify nearly the same hydrophobic helix set and differ only by a small shift in one helix's endpoints. Such membrane-helix boundaries are not reliably distinguishable at this precision from the sequence and are both defensible."
  },
  "important_caveats": [
    "The supplied evidence supports the key through a computational database annotation, not an independently verified experimental topology.",
    "The database annotation matches the supplied sequence, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A125YWU9 (NCR1_TOXGM, Niemann-Pick type C1-related protein from Toxoplasma gondii) annotates exactly 12 transmembrane helical regions at positions 157-177, 412-432, 448-468, 478-498, 516-536, 545-565, 789-809, 986-1006, 1013-1033, 1037-1057, 1080-1100, and 1114-1134, all with evidence code ECO:0000255 (inferred from electronic annotation). These match Choice A exactly. The sequence SHA256 confirms the benchmark sequence matches the UniProt sequence (1178 aa). The annotation is computational rather than experimental, but it is the recorded database annotation and fully supports the expected answer.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [C11](#evidence-c11), [C12](#evidence-c12), [C13](#evidence-c13), [C14](#evidence-c14), [C15](#evidence-c15), [C16](#evidence-c16), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8), [H9](#evidence-h9), [H10](#evidence-h10), [H11](#evidence-h11), [H12](#evidence-h12), [H13](#evidence-h13), [H14](#evidence-h14).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Choice C is immediately eliminable because it lists positions (e.g., 1209..1229, 1244..1264, up to 1722..1742) that exceed the 1178-residue sequence length, making them impossible. Choice D omits the 412..432 region, yielding only 11 TM segments. NPC1-family proteins (human NPC1 has 13 TM helices; NPC1-related proteins typically have 12-13) are characterized by a large N-terminal luminal domain followed by a multi-pass TM domain with a conserved number of helices; recognizing the NPC1-family fold from conserved sequence motifs and the overall hydrophobic pattern supports 12 TM helices rather than 11, favoring A/B over D. Between A and B, the only difference is the 8th TM region: 986..1006 vs 988..1007. This is a 1-2 residue boundary shift determined by where the contiguous hydrophobic stretch begins and ends in the sequence. A model applying the general principle of hydropathy-based TM boundary determination (a transferable skill learned from many proteins) could in principle examine residues at positions 986-987 and 1007 to decide whether they are sufficiently hydrophobic to belong to the helix. The NPC1-family topology and the hydrophobic-stretch principle together provide a credible, if not perfectly precise, route to Choice A.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The elimination of C (impossible positions) and D (NPC1-family TM count) relies on transferable family-level knowledge and sequence-length arithmetic. The A-vs-B distinction is a fine-grained boundary question resolvable in principle by hydropathy analysis of the supplied sequence, a general principle applicable to all TM proteins. While the 1-2 residue precision is challenging to achieve by mental counting in a 1178-aa sequence, the answer is derivable from the sequence itself and general TM-preduction principles rather than from a unique experimental measurement or a fact that exists only in this protein's database record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> The distinction between A (986..1006) and B (988..1007) is a 1-2 residue boundary shift within a hydrophobic stretch. Without precise residue-by-residue hydropathy analysis or access to the specific computational prediction, both boundaries are plausible TM helix endpoints. The UniProt annotation uses ECO:0000255 (electronic annotation), meaning these boundaries are computational predictions with inherent uncertainty at the 1-2 residue level. A knowledgeable model might reasonably select either boundary based on slightly different hydropathy window choices.


### Important caveats

- All 12 TM annotations carry evidence code ECO:0000255 (inferred from electronic annotation), meaning they are computational predictions, not experimentally validated membrane-spanning regions.
- The A-vs-B distinction (986..1006 vs 988..1007) is at the precision limit of hydropathy-based TM prediction; both are defensible boundaries for the same hydrophobic stretch.
- The UniProt entry was first public on 2025-06-18; the historical archived version (entry version 31, released 2026-01-28) contains the same TM annotations, confirming stability of the annotation.
- The reviewer identified the target protein via accession A0A125YWU9 inferred from dataset image-path metadata; this accession was not provided to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Choice C is immediately eliminable because it lists positions (e.g., 1209..1229, 1244..1264, up to 1722..1742) that exceed the 1178-residue sequence length, making them impossible. Choice D omits the 412..432 region, yielding only 11 TM segments. NPC1-family proteins (human NPC1 has 13 TM helices; NPC1-related proteins typically have 12-13) are characterized by a large N-terminal luminal domain followed by a multi-pass TM domain with a conserved number of helices; recognizing the NPC1-family fold from conserved sequence motifs and the overall hydrophobic pattern supports 12 TM helices rather than 11, favoring A/B over D. Between A and B, the only difference is the 8th TM region: 986..1006 vs 988..1007. This is a 1-2 residue boundary shift determined by where the contiguous hydrophobic stretch begins and ends in the sequence. A model applying the general principle of hydropathy-based TM boundary determination (a transferable skill learned from many proteins) could in principle examine residues at positions 986-987 and 1007 to decide whether they are sufficiently hydrophobic to belong to the helix. The NPC1-family topology and the hydrophobic-stretch principle together provide a credible, if not perfectly precise, route to Choice A.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The elimination of C (impossible positions) and D (NPC1-family TM count) relies on transferable family-level knowledge and sequence-length arithmetic. The A-vs-B distinction is a fine-grained boundary question resolvable in principle by hydropathy analysis of the supplied sequence, a general principle applicable to all TM proteins. While the 1-2 residue precision is challenging to achieve by mental counting in a 1178-aa sequence, the answer is derivable from the sequence itself and general TM-preduction principles rather than from a unique experimental measurement or a fact that exists only in this protein's database record."
  },
  "case_id": "transmembrane_0008",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "C8",
      "C9",
      "C10",
      "C11",
      "C12",
      "C13",
      "C14",
      "C15",
      "C16",
      "H3",
      "H4",
      "H5",
      "H6",
      "H7",
      "H8",
      "H9",
      "H10",
      "H11",
      "H12",
      "H13",
      "H14"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A125YWU9 (NCR1_TOXGM, Niemann-Pick type C1-related protein from Toxoplasma gondii) annotates exactly 12 transmembrane helical regions at positions 157-177, 412-432, 448-468, 478-498, 516-536, 545-565, 789-809, 986-1006, 1013-1033, 1037-1057, 1080-1100, and 1114-1134, all with evidence code ECO:0000255 (inferred from electronic annotation). These match Choice A exactly. The sequence SHA256 confirms the benchmark sequence matches the UniProt sequence (1178 aa). The annotation is computational rather than experimental, but it is the recorded database annotation and fully supports the expected answer."
  },
  "important_caveats": [
    "All 12 TM annotations carry evidence code ECO:0000255 (inferred from electronic annotation), meaning they are computational predictions, not experimentally validated membrane-spanning regions.",
    "The A-vs-B distinction (986..1006 vs 988..1007) is at the precision limit of hydropathy-based TM prediction; both are defensible boundaries for the same hydrophobic stretch.",
    "The UniProt entry was first public on 2025-06-18; the historical archived version (entry version 31, released 2026-01-28) contains the same TM annotations, confirming stability of the annotation.",
    "The reviewer identified the target protein via accession A0A125YWU9 inferred from dataset image-path metadata; this accession was not provided to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "The distinction between A (986..1006) and B (988..1007) is a 1-2 residue boundary shift within a hydrophobic stretch. Without precise residue-by-residue hydropathy analysis or access to the specific computational prediction, both boundaries are plausible TM helix endpoints. The UniProt annotation uses ECO:0000255 (electronic annotation), meaning these boundaries are computational predictions with inherent uncertainty at the 1-2 residue level. A knowledgeable model might reasonably select either boundary based on slightly different hydropathy window choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0008",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A125YWU9 (NCR1_TOXGM, Niemann-Pick type C1-related protein from Toxoplasma gondii) annotates exactly 12 transmembrane helical regions at positions 157-177, 412-432, 448-468, 478-498, 516-536, 545-565, 789-809, 986-1006, 1013-1033, 1037-1057, 1080-1100, and 1114-1134, all with evidence code ECO:0000255 (inferred from electronic annotation). These match Choice A exactly. The sequence SHA256 confirms the benchmark sequence matches the UniProt sequence (1178 aa). The annotation is computational rather than experimental, but it is the recorded database annotation and fully supports the expected answer.",
    "evidence_ids": ["C5", "C6", "C7", "C8", "C9", "C10", "C11", "C12", "C13", "C14", "C15", "C16", "H3", "H4", "H5", "H6", "H7", "H8", "H9", "H10", "H11", "H12", "H13", "H14"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Choice C is immediately eliminable because it lists positions (e.g., 1209..1229, 1244..1264, up to 1722..1742) that exceed the 1178-residue sequence length, making them impossible. Choice D omits the 412..432 region, yielding only 11 TM segments. NPC1-family proteins (human NPC1 has 13 TM helices; NPC1-related proteins typically have 12-13) are characterized by a large N-terminal luminal domain followed by a multi-pass TM domain with a conserved number of helices; recognizing the NPC1-family fold from conserved sequence motifs and the overall hydrophobic pattern supports 12 TM helices rather than 11, favoring A/B over D. Between A and B, the only difference is the 8th TM region: 986..1006 vs 988..1007. This is a 1-2 residue boundary shift determined by where the contiguous hydrophobic stretch begins and ends in the sequence. A model applying the general principle of hydropathy-based TM boundary determination (a transferable skill learned from many proteins) could in principle examine residues at positions 986-987 and 1007 to decide whether they are sufficiently hydrophobic to belong to the helix. The NPC1-family topology and the hydrophobic-stretch principle together provide a credible, if not perfectly precise, route to Choice A.",
    "missing_item_specific_fact": "",
    "reason": "The elimination of C (impossible positions) and D (NPC1-family TM count) relies on transferable family-level knowledge and sequence-length arithmetic. The A-vs-B distinction is a fine-grained boundary question resolvable in principle by hydropathy analysis of the supplied sequence, a general principle applicable to all TM proteins. While the 1-2 residue precision is challenging to achieve by mental counting in a 1178-aa sequence, the answer is derivable from the sequence itself and general TM-preduction principles rather than from a unique experimental measurement or a fact that exists only in this protein's database record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "The distinction between A (986..1006) and B (988..1007) is a 1-2 residue boundary shift within a hydrophobic stretch. Without precise residue-by-residue hydropathy analysis or access to the specific computational prediction, both boundaries are plausible TM helix endpoints. The UniProt annotation uses ECO:0000255 (electronic annotation), meaning these boundaries are computational predictions with inherent uncertainty at the 1-2 residue level. A knowledgeable model might reasonably select either boundary based on slightly different hydropathy window choices."
  },
  "important_caveats": [
    "All 12 TM annotations carry evidence code ECO:0000255 (inferred from electronic annotation), meaning they are computational predictions, not experimentally validated membrane-spanning regions.",
    "The A-vs-B distinction (986..1006 vs 988..1007) is at the precision limit of hydropathy-based TM prediction; both are defensible boundaries for the same hydrophobic stretch.",
    "The UniProt entry was first public on 2025-06-18; the historical archived version (entry version 31, released 2026-01-28) contains the same TM annotations, confirming stability of the annotation.",
    "The reviewer identified the target protein via accession A0A125YWU9 inferred from dataset image-path metadata; this accession was not provided to the evaluated model."
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
  "benchmark_sequence_length": 1178,
  "benchmark_sequence_sha256": "45cb3c3f1e942e9bc182cc3eca7ab3c17810c270b34e91f76b50b556cb5ff1fd",
  "current_entry_audit": {
    "entryVersion": 33,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2016-04-13",
    "sequenceVersion": 1
  },
  "current_record_sha256": "4257042342d9be27234f539e56a352f0531663813b7f4f5f3d705c7ea4125d1e",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 1178,
  "current_source_sequence_sha256": "45cb3c3f1e942e9bc182cc3eca7ab3c17810c270b34e91f76b50b556cb5ff1fd",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 31,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A125YWU9",
  "selected_historical_entry_version": 31,
  "selected_historical_record_sha256": "02466d6f81a11de5f5fc4f909cfcfa4d40fa693a54a63baf27d12b1ba64765a8",
  "selected_historical_source_sequence_length": 1178,
  "selected_historical_source_sequence_sha256": "45cb3c3f1e942e9bc182cc3eca7ab3c17810c270b34e91f76b50b556cb5ff1fd",
  "selected_historical_version": {
    "accession": "A0A125YWU9",
    "database": "Swiss-Prot",
    "entryVersion": 31,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "NCR1_TOXGM",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A125YWU9.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A125YWU9\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:24:42.732042+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4257042342d9be27234f539e56a352f0531663813b7f4f5f3d705c7ea4125d1e",
  "url": "https://rest.uniprot.org/uniprotkb/A0A125YWU9.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A125YWU9.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":33,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2016-04-13\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:24:42.732042+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4257042342d9be27234f539e56a352f0531663813b7f4f5f3d705c7ea4125d1e",
  "url": "https://rest.uniprot.org/uniprotkb/A0A125YWU9.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A125YWU9.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000001529\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Sar\",\"Alveolata\",\"Apicomplexa\",\"Conoidasida\",\"Coccidia\",\"Eucoccidiorida\",\"Eimeriorina\",\"Sarcocystidae\",\"Toxoplasma\"],\"scientificName\":\"Toxoplasma gondii (strain ATCC 50611 / Me49)\",\"taxonId\":508771}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:24:42.732042+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4257042342d9be27234f539e56a352f0531663813b7f4f5f3d705c7ea4125d1e",
  "url": "https://rest.uniprot.org/uniprotkb/A0A125YWU9.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A125YWU9.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"22174676\",\"source\":\"PubMed\"}],\"value\":\"NPC1-related protein\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"EPT28045.1\",\"source\":\"EMBL\"}],\"value\":\"Patched family protein\"}}],\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"22174676\",\"source\":\"PubMed\"}],\"value\":\"Niemann-Pick type C1-related protein\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"22174676\",\"source\":\"PubMed\"}],\"value\":\"TgNCR1\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:24:42.732042+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4257042342d9be27234f539e56a352f0531663813b7f4f5f3d705c7ea4125d1e",
  "url": "https://rest.uniprot.org/uniprotkb/A0A125YWU9.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A125YWU9.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":177},\"start\":{\"modifier\":\"EXACT\",\"value\":157}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-01T06:24:42.732042+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4257042342d9be27234f539e56a352f0531663813b7f4f5f3d705c7ea4125d1e",
  "url": "https://rest.uniprot.org/uniprotkb/A0A125YWU9.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A125YWU9.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":432},\"start\":{\"modifier\":\"EXACT\",\"value\":412}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-01T06:24:42.732042+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4257042342d9be27234f539e56a352f0531663813b7f4f5f3d705c7ea4125d1e",
  "url": "https://rest.uniprot.org/uniprotkb/A0A125YWU9.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A125YWU9.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":468},\"start\":{\"modifier\":\"EXACT\",\"value\":448}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-01T06:24:42.732042+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4257042342d9be27234f539e56a352f0531663813b7f4f5f3d705c7ea4125d1e",
  "url": "https://rest.uniprot.org/uniprotkb/A0A125YWU9.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A125YWU9.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":498},\"start\":{\"modifier\":\"EXACT\",\"value\":478}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-01T06:24:42.732042+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4257042342d9be27234f539e56a352f0531663813b7f4f5f3d705c7ea4125d1e",
  "url": "https://rest.uniprot.org/uniprotkb/A0A125YWU9.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A125YWU9.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":536},\"start\":{\"modifier\":\"EXACT\",\"value\":516}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
  "retrieved_utc": "2026-11-01T06:24:42.732042+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4257042342d9be27234f539e56a352f0531663813b7f4f5f3d705c7ea4125d1e",
  "url": "https://rest.uniprot.org/uniprotkb/A0A125YWU9.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A125YWU9.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":565},\"start\":{\"modifier\":\"EXACT\",\"value\":545}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/6",
  "retrieved_utc": "2026-11-01T06:24:42.732042+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4257042342d9be27234f539e56a352f0531663813b7f4f5f3d705c7ea4125d1e",
  "url": "https://rest.uniprot.org/uniprotkb/A0A125YWU9.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A125YWU9.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":809},\"start\":{\"modifier\":\"EXACT\",\"value\":789}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/7",
  "retrieved_utc": "2026-11-01T06:24:42.732042+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4257042342d9be27234f539e56a352f0531663813b7f4f5f3d705c7ea4125d1e",
  "url": "https://rest.uniprot.org/uniprotkb/A0A125YWU9.json"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A125YWU9.json)

```json
{
  "evidence_id": "C12",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":1006},\"start\":{\"modifier\":\"EXACT\",\"value\":986}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/8",
  "retrieved_utc": "2026-11-01T06:24:42.732042+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4257042342d9be27234f539e56a352f0531663813b7f4f5f3d705c7ea4125d1e",
  "url": "https://rest.uniprot.org/uniprotkb/A0A125YWU9.json"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A125YWU9.json)

```json
{
  "evidence_id": "C13",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":1033},\"start\":{\"modifier\":\"EXACT\",\"value\":1013}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/9",
  "retrieved_utc": "2026-11-01T06:24:42.732042+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4257042342d9be27234f539e56a352f0531663813b7f4f5f3d705c7ea4125d1e",
  "url": "https://rest.uniprot.org/uniprotkb/A0A125YWU9.json"
}
```

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A125YWU9.json)

```json
{
  "evidence_id": "C14",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":1057},\"start\":{\"modifier\":\"EXACT\",\"value\":1037}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/10",
  "retrieved_utc": "2026-11-01T06:24:42.732042+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4257042342d9be27234f539e56a352f0531663813b7f4f5f3d705c7ea4125d1e",
  "url": "https://rest.uniprot.org/uniprotkb/A0A125YWU9.json"
}
```

### Evidence C15

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A125YWU9.json)

```json
{
  "evidence_id": "C15",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":1100},\"start\":{\"modifier\":\"EXACT\",\"value\":1080}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/11",
  "retrieved_utc": "2026-11-01T06:24:42.732042+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4257042342d9be27234f539e56a352f0531663813b7f4f5f3d705c7ea4125d1e",
  "url": "https://rest.uniprot.org/uniprotkb/A0A125YWU9.json"
}
```

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A125YWU9.json)

```json
{
  "evidence_id": "C16",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":1134},\"start\":{\"modifier\":\"EXACT\",\"value\":1114}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/12",
  "retrieved_utc": "2026-11-01T06:24:42.732042+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4257042342d9be27234f539e56a352f0531663813b7f4f5f3d705c7ea4125d1e",
  "url": "https://rest.uniprot.org/uniprotkb/A0A125YWU9.json"
}
```

### Evidence C17

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A125YWU9.json)

```json
{
  "evidence_id": "C17",
  "excerpt": "{\"citation\":{\"authors\":[\"Lige B.\",\"Romano J.D.\",\"Bandaru V.V.\",\"Ehrenman K.\",\"Levitskaya J.\",\"Sampels V.\",\"Haughey N.J.\",\"Coppens I.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"22174676\"},{\"database\":\"DOI\",\"id\":\"10.1371/journal.ppat.1002410\"}],\"citationType\":\"journal article\",\"firstPage\":\"e1002410\",\"id\":\"22174676\",\"journal\":\"PLoS Pathog.\",\"lastPage\":\"e1002410\",\"publicationDate\":\"2011\",\"title\":\"Deficiency of a Niemann-Pick, type C1-related protein in toxoplasma is associated with multiple lipidoses and increased pathogenicity.\",\"volume\":\"7\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"SUBCELLULAR LOCATION\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-01T06:24:42.732042+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4257042342d9be27234f539e56a352f0531663813b7f4f5f3d705c7ea4125d1e",
  "url": "https://rest.uniprot.org/uniprotkb/A0A125YWU9.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A125YWU9?format=txt&versions=31)

```json
{
  "entry_version": 31,
  "evidence_id": "H1",
  "excerpt": "ID   NCR1_TOXGM              Reviewed;        1178 AA.\nAC   A0A125YWU9;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   13-APR-2016, sequence version 1.\nDT   28-JAN-2026, entry version 31.\nDE   RecName: Full=Niemann-Pick type C1-related protein {ECO:0000303|PubMed:22174676};\nDE            Short=TgNCR1 {ECO:0000303|PubMed:22174676};\nDE   AltName: Full=NPC1-related protein {ECO:0000303|PubMed:22174676};\nDE   AltName: Full=Patched family protein {ECO:0000312|EMBL:EPT28045.1};\nGN   Name=NCR1 {ECO:0000305};\nGN   ORFNames=TGME49_290870 {ECO:0000312|EMBL:EPT28045.1};\nOS   Toxoplasma gondii (strain ATCC 50611 / Me49).\nOC   Eukaryota; Sar; Alveolata; Apicomplexa; Conoidasida; Coccidia;\nOC   Eucoccidiorida; Eimeriorina; Sarcocystidae; Toxoplasma.\nOX   NCBI_TaxID=508771 {ECO:0000312|Proteomes:UP000001529};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:21.678924+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "02466d6f81a11de5f5fc4f909cfcfa4d40fa693a54a63baf27d12b1ba64765a8",
  "url": "https://rest.uniprot.org/unisave/A0A125YWU9?format=txt&versions=31"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A125YWU9?format=txt&versions=31)

```json
{
  "entry_version": 31,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION, SUBCELLULAR LOCATION, AND DISRUPTION PHENOTYPE.\nRX   PubMed=22174676; DOI=10.1371/journal.ppat.1002410;\nRA   Lige B., Romano J.D., Bandaru V.V., Ehrenman K., Levitskaya J., Sampels V.,\nRA   Haughey N.J., Coppens I.;\nRT   \"Deficiency of a Niemann-Pick, type C1-related protein in toxoplasma is\nRT   associated with multiple lipidoses and increased pathogenicity.\";\nRL   PLoS Pathog. 7:e1002410-e1002410(2011).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:21.678924+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 22-29",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "02466d6f81a11de5f5fc4f909cfcfa4d40fa693a54a63baf27d12b1ba64765a8",
  "url": "https://rest.uniprot.org/unisave/A0A125YWU9?format=txt&versions=31"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A125YWU9?format=txt&versions=31)

```json
{
  "entry_version": 31,
  "evidence_id": "H3",
  "excerpt": "FT   TRANSMEM        157..177\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:21.678924+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 89-91",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "02466d6f81a11de5f5fc4f909cfcfa4d40fa693a54a63baf27d12b1ba64765a8",
  "url": "https://rest.uniprot.org/unisave/A0A125YWU9?format=txt&versions=31"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A125YWU9?format=txt&versions=31)

```json
{
  "entry_version": 31,
  "evidence_id": "H4",
  "excerpt": "FT   TRANSMEM        412..432\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:21.678924+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 92-94",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "02466d6f81a11de5f5fc4f909cfcfa4d40fa693a54a63baf27d12b1ba64765a8",
  "url": "https://rest.uniprot.org/unisave/A0A125YWU9?format=txt&versions=31"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A125YWU9?format=txt&versions=31)

```json
{
  "entry_version": 31,
  "evidence_id": "H5",
  "excerpt": "FT   TRANSMEM        448..468\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:21.678924+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 95-97",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "02466d6f81a11de5f5fc4f909cfcfa4d40fa693a54a63baf27d12b1ba64765a8",
  "url": "https://rest.uniprot.org/unisave/A0A125YWU9?format=txt&versions=31"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A125YWU9?format=txt&versions=31)

```json
{
  "entry_version": 31,
  "evidence_id": "H6",
  "excerpt": "FT   TRANSMEM        478..498\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:21.678924+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 98-100",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "02466d6f81a11de5f5fc4f909cfcfa4d40fa693a54a63baf27d12b1ba64765a8",
  "url": "https://rest.uniprot.org/unisave/A0A125YWU9?format=txt&versions=31"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A125YWU9?format=txt&versions=31)

```json
{
  "entry_version": 31,
  "evidence_id": "H7",
  "excerpt": "FT   TRANSMEM        516..536\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:21.678924+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 101-103",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "02466d6f81a11de5f5fc4f909cfcfa4d40fa693a54a63baf27d12b1ba64765a8",
  "url": "https://rest.uniprot.org/unisave/A0A125YWU9?format=txt&versions=31"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A125YWU9?format=txt&versions=31)

```json
{
  "entry_version": 31,
  "evidence_id": "H8",
  "excerpt": "FT   TRANSMEM        545..565\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:21.678924+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 104-106",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "02466d6f81a11de5f5fc4f909cfcfa4d40fa693a54a63baf27d12b1ba64765a8",
  "url": "https://rest.uniprot.org/unisave/A0A125YWU9?format=txt&versions=31"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A125YWU9?format=txt&versions=31)

```json
{
  "entry_version": 31,
  "evidence_id": "H9",
  "excerpt": "FT   TRANSMEM        789..809\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:21.678924+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 107-109",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "02466d6f81a11de5f5fc4f909cfcfa4d40fa693a54a63baf27d12b1ba64765a8",
  "url": "https://rest.uniprot.org/unisave/A0A125YWU9?format=txt&versions=31"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A125YWU9?format=txt&versions=31)

```json
{
  "entry_version": 31,
  "evidence_id": "H10",
  "excerpt": "FT   TRANSMEM        986..1006\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:21.678924+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 110-112",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "02466d6f81a11de5f5fc4f909cfcfa4d40fa693a54a63baf27d12b1ba64765a8",
  "url": "https://rest.uniprot.org/unisave/A0A125YWU9?format=txt&versions=31"
}
```

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A125YWU9?format=txt&versions=31)

```json
{
  "entry_version": 31,
  "evidence_id": "H11",
  "excerpt": "FT   TRANSMEM        1013..1033\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:21.678924+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 113-115",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "02466d6f81a11de5f5fc4f909cfcfa4d40fa693a54a63baf27d12b1ba64765a8",
  "url": "https://rest.uniprot.org/unisave/A0A125YWU9?format=txt&versions=31"
}
```

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A125YWU9?format=txt&versions=31)

```json
{
  "entry_version": 31,
  "evidence_id": "H12",
  "excerpt": "FT   TRANSMEM        1037..1057\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:21.678924+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 116-118",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "02466d6f81a11de5f5fc4f909cfcfa4d40fa693a54a63baf27d12b1ba64765a8",
  "url": "https://rest.uniprot.org/unisave/A0A125YWU9?format=txt&versions=31"
}
```

### Evidence H13

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A125YWU9?format=txt&versions=31)

```json
{
  "entry_version": 31,
  "evidence_id": "H13",
  "excerpt": "FT   TRANSMEM        1080..1100\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:21.678924+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 119-121",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "02466d6f81a11de5f5fc4f909cfcfa4d40fa693a54a63baf27d12b1ba64765a8",
  "url": "https://rest.uniprot.org/unisave/A0A125YWU9?format=txt&versions=31"
}
```

### Evidence H14

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A125YWU9?format=txt&versions=31)

```json
{
  "entry_version": 31,
  "evidence_id": "H14",
  "excerpt": "FT   TRANSMEM        1114..1134\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:21.678924+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 122-124",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "02466d6f81a11de5f5fc4f909cfcfa4d40fa693a54a63baf27d12b1ba64765a8",
  "url": "https://rest.uniprot.org/unisave/A0A125YWU9?format=txt&versions=31"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 8. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
