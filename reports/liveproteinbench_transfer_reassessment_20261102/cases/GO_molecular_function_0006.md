# GO_molecular_function_0006

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_molecular_function_0006.txt)

**Task:** `GO_molecular_function`  
**Expected answer:** **C** — mitochondrion autophagosome adaptor activity

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MNVPTAPTPNKHLNIPDLRFEKVFKKALHRELAPSSSLSRKAGVITKVVVRDVLLMPLLQSFVLSLALMGVKEWLSYIRLKGRTLGDRIRQRLFPI

[Multiple Choices]
A. host cell surface receptor binding
B. ubiquitin-like protein transferase activity
C. mitochondrion autophagosome adaptor activity
D. 3-keto-5-aminohexanoate cleavage activity
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Molecular Function Prediction, which is to predict the fundamental activity of a protein at the molecular level, as defined by the Gene Ontology (GO) 'Molecular Function' branch. This describes the elemental tasks a protein performs, such as catalysis, transport, or binding to specific molecules. Based on the protein's amino acid sequence, you are to select the option that best describes its primary molecular function.. The inputs provided by the user for this task include:

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

> The matched sequence has a UniProt GO annotation for mitochondrion autophagosome adaptor activity, but its evidence code is IEA:InterPro, so this supports the key as a computational annotation rather than an experimentally established function. The entry still describes the protein as uncharacterized.

Citations as saved: [C5](#evidence-c5), [H2](#evidence-h2), [C4](#evidence-c4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is only 96 amino acids and contains a pronounced hydrophobic stretch consistent with a membrane-spanning segment, with no obvious catalytic motif. Transferable knowledge makes a small membrane-associated adaptor a more plausible fit than the catalytic activities in B or D; the sequence also lacks an evident secretion signal that would favor A. Among these options, C is a defensible probabilistic choice.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence and alternatives provide a meaningful, though not conclusive, basis to favor a membrane-associated adaptor over the enzyme choices and host-receptor binding. The inference does not establish mitochondrial localization or autophagosome binding specifically, but the choices do not require independent proof of every detail.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence does not uniquely establish the specific adaptor function, but no other offered option has comparable support from its length and hydrophobic segment.


### Important caveats

- The supplied GO annotation is computational (IEA:InterPro), not direct experimental confirmation.
- A hydrophobic segment supports membrane association but does not alone identify the membrane or prove mitophagy-adaptor activity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is only 96 amino acids and contains a pronounced hydrophobic stretch consistent with a membrane-spanning segment, with no obvious catalytic motif. Transferable knowledge makes a small membrane-associated adaptor a more plausible fit than the catalytic activities in B or D; the sequence also lacks an evident secretion signal that would favor A. Among these options, C is a defensible probabilistic choice.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence and alternatives provide a meaningful, though not conclusive, basis to favor a membrane-associated adaptor over the enzyme choices and host-receptor binding. The inference does not establish mitochondrial localization or autophagosome binding specifically, but the choices do not require independent proof of every detail."
  },
  "case_id": "GO_molecular_function_0006",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H2",
      "C4"
    ],
    "judgment": "supported",
    "reason": "The matched sequence has a UniProt GO annotation for mitochondrion autophagosome adaptor activity, but its evidence code is IEA:InterPro, so this supports the key as a computational annotation rather than an experimentally established function. The entry still describes the protein as uncharacterized."
  },
  "important_caveats": [
    "The supplied GO annotation is computational (IEA:InterPro), not direct experimental confirmation.",
    "A hydrophobic segment supports membrane association but does not alone identify the membrane or prove mitophagy-adaptor activity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence does not uniquely establish the specific adaptor function, but no other offered option has comparable support from its length and hydrophobic segment."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0006",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched sequence has a UniProt GO annotation for mitochondrion autophagosome adaptor activity, but its evidence code is IEA:InterPro, so this supports the key as a computational annotation rather than an experimentally established function. The entry still describes the protein as uncharacterized.",
    "evidence_ids": ["C5", "H2", "C4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is only 96 amino acids and contains a pronounced hydrophobic stretch consistent with a membrane-spanning segment, with no obvious catalytic motif. Transferable knowledge makes a small membrane-associated adaptor a more plausible fit than the catalytic activities in B or D; the sequence also lacks an evident secretion signal that would favor A. Among these options, C is a defensible probabilistic choice.",
    "missing_item_specific_fact": "",
    "reason": "The sequence and alternatives provide a meaningful, though not conclusive, basis to favor a membrane-associated adaptor over the enzyme choices and host-receptor binding. The inference does not establish mitochondrial localization or autophagosome binding specifically, but the choices do not require independent proof of every detail."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence does not uniquely establish the specific adaptor function, but no other offered option has comparable support from its length and hydrophobic segment."
  },
  "important_caveats": [
    "The supplied GO annotation is computational (IEA:InterPro), not direct experimental confirmation.",
    "A hydrophobic segment supports membrane association but does not alone identify the membrane or prove mitophagy-adaptor activity."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry P9WEJ4 (YFR035W-A, Saccharomyces cerevisiae) carries GO:0140580 (mitochondrion autophagosome adaptor activity) as its sole molecular-function annotation (evidence_id C5, H2). However, the evidence code is IEA:InterPro (Inferred from Electronic Annotation via InterPro domain matching), and the protein is explicitly labeled 'Uncharacterized protein YFR035W-A' (ECO:0000305). No experimental or direct evidence supports the annotation; it is purely computational. The key is supported by the database record but at the weakest annotation confidence level.

Citations as saved: [C5](#evidence-c5), [H2](#evidence-h2), [C4](#evidence-c4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 96-aa sequence contains two features characteristic of mitophagy receptors/adaptors: (1) a hydrophobic stretch (~residues 55–75: 'VVVRDVLLMPLLQSFVLSLALMGVKEWLSY') consistent with a transmembrane domain anchoring the protein to the mitochondrial outer membrane, and (2) a potential ATG8-interacting motif (AIM/LIR) 'YIRL' near the C-terminus, fitting the degenerate consensus &#91;W/F/Y&#93;-x-x-&#91;L/I/V&#93;. Family-level knowledge from Atg32 (yeast), FUNDC1, BNIP3, and BNIP3L/Nix (mammals) establishes that mitophagy adaptors are typically small proteins combining a mitochondrial TM anchor with an ATG8/LC3-interacting motif to bridge mitochondrial and autophagosome membranes. Against the other options: (A) host cell surface receptor binding is a viral/pathogen strategy, implausible for a small yeast protein; (B) ubiquitin-like protein transferase activity requires a catalytic fold (RING/HECT/U-box) and is far too large a machinery for a 96-aa protein; (D) 3-keto-5-aminohexanoate cleavage activity is a thiolase-like enzymatic reaction requiring a catalytic Cys and specific tertiary structure absent from this short sequence. The TM+AIM architecture meaningfully distinguishes C from A, B, and D using transferable knowledge of the mitophagy receptor family.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A model familiar with the architecture of mitophagy receptors (small TM-anchored proteins with LIR/AIM motifs) can recognize the hydrophobic membrane-anchoring segment and a plausible Y-x-x-L motif in this sequence, and can eliminate the enzymatic options (B, D) on size/fold grounds and the viral option (A) on organismal context. This is a family-level structural-mechanistic inference, not a lookup of this protein's specific annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The other three options are strongly disfavored: B and D require enzymatic catalytic machinery inconsistent with a 96-aa protein lacking any recognizable catalytic fold; A describes a pathogen–host interaction implausible for a yeast gene product. Only C is consistent with the observed sequence features (TM region + potential AIM) and the organismal context.


### Important caveats

- The GO annotation is IEA:InterPro only; the protein is explicitly 'Uncharacterized' in UniProt. No experimental mitophagy-adaptor evidence exists for YFR035W-A.
- The canonical yeast mitophagy receptor Atg32 is 341 aa; a 96-aa protein is unusually small, though smaller mammalian adaptors (e.g., ~150 aa FUNDC1) exist and the LIR-motif argument is degenerate.
- The 'YIRL' LIR identification is a probabilistic motif match, not a validated interaction; the InterPro-based annotation may reflect a broader domain family rather than a confirmed mitophagy role.
- The reviewer-only evidence (accession, organism, annotation) was not available to the evaluated model; the reasoning argument relies solely on sequence features and transferable family knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 96-aa sequence contains two features characteristic of mitophagy receptors/adaptors: (1) a hydrophobic stretch (~residues 55–75: 'VVVRDVLLMPLLQSFVLSLALMGVKEWLSY') consistent with a transmembrane domain anchoring the protein to the mitochondrial outer membrane, and (2) a potential ATG8-interacting motif (AIM/LIR) 'YIRL' near the C-terminus, fitting the degenerate consensus [W/F/Y]-x-x-[L/I/V]. Family-level knowledge from Atg32 (yeast), FUNDC1, BNIP3, and BNIP3L/Nix (mammals) establishes that mitophagy adaptors are typically small proteins combining a mitochondrial TM anchor with an ATG8/LC3-interacting motif to bridge mitochondrial and autophagosome membranes. Against the other options: (A) host cell surface receptor binding is a viral/pathogen strategy, implausible for a small yeast protein; (B) ubiquitin-like protein transferase activity requires a catalytic fold (RING/HECT/U-box) and is far too large a machinery for a 96-aa protein; (D) 3-keto-5-aminohexanoate cleavage activity is a thiolase-like enzymatic reaction requiring a catalytic Cys and specific tertiary structure absent from this short sequence. The TM+AIM architecture meaningfully distinguishes C from A, B, and D using transferable knowledge of the mitophagy receptor family.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A model familiar with the architecture of mitophagy receptors (small TM-anchored proteins with LIR/AIM motifs) can recognize the hydrophobic membrane-anchoring segment and a plausible Y-x-x-L motif in this sequence, and can eliminate the enzymatic options (B, D) on size/fold grounds and the viral option (A) on organismal context. This is a family-level structural-mechanistic inference, not a lookup of this protein's specific annotation."
  },
  "case_id": "GO_molecular_function_0006",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H2",
      "C4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry P9WEJ4 (YFR035W-A, Saccharomyces cerevisiae) carries GO:0140580 (mitochondrion autophagosome adaptor activity) as its sole molecular-function annotation (evidence_id C5, H2). However, the evidence code is IEA:InterPro (Inferred from Electronic Annotation via InterPro domain matching), and the protein is explicitly labeled 'Uncharacterized protein YFR035W-A' (ECO:0000305). No experimental or direct evidence supports the annotation; it is purely computational. The key is supported by the database record but at the weakest annotation confidence level."
  },
  "important_caveats": [
    "The GO annotation is IEA:InterPro only; the protein is explicitly 'Uncharacterized' in UniProt. No experimental mitophagy-adaptor evidence exists for YFR035W-A.",
    "The canonical yeast mitophagy receptor Atg32 is 341 aa; a 96-aa protein is unusually small, though smaller mammalian adaptors (e.g., ~150 aa FUNDC1) exist and the LIR-motif argument is degenerate.",
    "The 'YIRL' LIR identification is a probabilistic motif match, not a validated interaction; the InterPro-based annotation may reflect a broader domain family rather than a confirmed mitophagy role.",
    "The reviewer-only evidence (accession, organism, annotation) was not available to the evaluated model; the reasoning argument relies solely on sequence features and transferable family knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The other three options are strongly disfavored: B and D require enzymatic catalytic machinery inconsistent with a 96-aa protein lacking any recognizable catalytic fold; A describes a pathogen–host interaction implausible for a yeast gene product. Only C is consistent with the observed sequence features (TM region + potential AIM) and the organismal context."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0006",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry P9WEJ4 (YFR035W-A, Saccharomyces cerevisiae) carries GO:0140580 (mitochondrion autophagosome adaptor activity) as its sole molecular-function annotation (evidence_id C5, H2). However, the evidence code is IEA:InterPro (Inferred from Electronic Annotation via InterPro domain matching), and the protein is explicitly labeled 'Uncharacterized protein YFR035W-A' (ECO:0000305). No experimental or direct evidence supports the annotation; it is purely computational. The key is supported by the database record but at the weakest annotation confidence level.",
    "evidence_ids": ["C5", "H2", "C4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 96-aa sequence contains two features characteristic of mitophagy receptors/adaptors: (1) a hydrophobic stretch (~residues 55–75: 'VVVRDVLLMPLLQSFVLSLALMGVKEWLSY') consistent with a transmembrane domain anchoring the protein to the mitochondrial outer membrane, and (2) a potential ATG8-interacting motif (AIM/LIR) 'YIRL' near the C-terminus, fitting the degenerate consensus [W/F/Y]-x-x-[L/I/V]. Family-level knowledge from Atg32 (yeast), FUNDC1, BNIP3, and BNIP3L/Nix (mammals) establishes that mitophagy adaptors are typically small proteins combining a mitochondrial TM anchor with an ATG8/LC3-interacting motif to bridge mitochondrial and autophagosome membranes. Against the other options: (A) host cell surface receptor binding is a viral/pathogen strategy, implausible for a small yeast protein; (B) ubiquitin-like protein transferase activity requires a catalytic fold (RING/HECT/U-box) and is far too large a machinery for a 96-aa protein; (D) 3-keto-5-aminohexanoate cleavage activity is a thiolase-like enzymatic reaction requiring a catalytic Cys and specific tertiary structure absent from this short sequence. The TM+AIM architecture meaningfully distinguishes C from A, B, and D using transferable knowledge of the mitophagy receptor family.",
    "missing_item_specific_fact": "",
    "reason": "A model familiar with the architecture of mitophagy receptors (small TM-anchored proteins with LIR/AIM motifs) can recognize the hydrophobic membrane-anchoring segment and a plausible Y-x-x-L motif in this sequence, and can eliminate the enzymatic options (B, D) on size/fold grounds and the viral option (A) on organismal context. This is a family-level structural-mechanistic inference, not a lookup of this protein's specific annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The other three options are strongly disfavored: B and D require enzymatic catalytic machinery inconsistent with a 96-aa protein lacking any recognizable catalytic fold; A describes a pathogen–host interaction implausible for a yeast gene product. Only C is consistent with the observed sequence features (TM region + potential AIM) and the organismal context."
  },
  "important_caveats": [
    "The GO annotation is IEA:InterPro only; the protein is explicitly 'Uncharacterized' in UniProt. No experimental mitophagy-adaptor evidence exists for YFR035W-A.",
    "The canonical yeast mitophagy receptor Atg32 is 341 aa; a 96-aa protein is unusually small, though smaller mammalian adaptors (e.g., ~150 aa FUNDC1) exist and the LIR-motif argument is degenerate.",
    "The 'YIRL' LIR identification is a probabilistic motif match, not a validated interaction; the InterPro-based annotation may reflect a broader domain family rather than a confirmed mitophagy role.",
    "The reviewer-only evidence (accession, organism, annotation) was not available to the evaluated model; the reasoning argument relies solely on sequence features and transferable family knowledge."
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
  "benchmark_sequence_length": 96,
  "benchmark_sequence_sha256": "af9deaca53f1b7ad13d02bb00fcd3d88f84d31a2a38d6646a9176bba432113f6",
  "current_entry_audit": {
    "entryVersion": 5,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-06-10",
    "lastSequenceUpdateDate": "2025-02-05",
    "sequenceVersion": 1
  },
  "current_record_sha256": "334d652c31aa94671f71985d47556af600c64ebfe50ff82f67cec6a6220cb69c",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 96,
  "current_source_sequence_sha256": "af9deaca53f1b7ad13d02bb00fcd3d88f84d31a2a38d6646a9176bba432113f6",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 4,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "P9WEJ4",
  "selected_historical_entry_version": 4,
  "selected_historical_record_sha256": "620602a41d8671c8701df46a7d19236b30cfbea35740e43343f9e3862130e866",
  "selected_historical_source_sequence_length": 96,
  "selected_historical_source_sequence_sha256": "af9deaca53f1b7ad13d02bb00fcd3d88f84d31a2a38d6646a9176bba432113f6",
  "selected_historical_version": {
    "accession": "P9WEJ4",
    "database": "Swiss-Prot",
    "entryVersion": 4,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "YF035_YEAST",
    "sequenceVersion": 1
  }
}
```

**Qualifications:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEJ4.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"P9WEJ4\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:30:19.580713+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "334d652c31aa94671f71985d47556af600c64ebfe50ff82f67cec6a6220cb69c",
  "url": "https://rest.uniprot.org/uniprotkb/P9WEJ4.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEJ4.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":5,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-06-10\",\"lastSequenceUpdateDate\":\"2025-02-05\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:30:19.580713+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "334d652c31aa94671f71985d47556af600c64ebfe50ff82f67cec6a6220cb69c",
  "url": "https://rest.uniprot.org/uniprotkb/P9WEJ4.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEJ4.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Baker's yeast\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Saccharomycotina\",\"Saccharomycetes\",\"Saccharomycetales\",\"Saccharomycetaceae\",\"Saccharomyces\"],\"scientificName\":\"Saccharomyces cerevisiae (strain ATCC 204508 / S288c)\",\"taxonId\":559292}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:30:19.580713+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "334d652c31aa94671f71985d47556af600c64ebfe50ff82f67cec6a6220cb69c",
  "url": "https://rest.uniprot.org/uniprotkb/P9WEJ4.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEJ4.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Uncharacterized protein YFR035W-A\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:30:19.580713+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "334d652c31aa94671f71985d47556af600c64ebfe50ff82f67cec6a6220cb69c",
  "url": "https://rest.uniprot.org/uniprotkb/P9WEJ4.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEJ4.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0140580\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:mitochondrion autophagosome adaptor activity\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:InterPro\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/9",
  "retrieved_utc": "2026-11-02T04:30:19.580713+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "334d652c31aa94671f71985d47556af600c64ebfe50ff82f67cec6a6220cb69c",
  "url": "https://rest.uniprot.org/uniprotkb/P9WEJ4.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P9WEJ4?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H1",
  "excerpt": "ID   YF035_YEAST             Reviewed;          96 AA.\nAC   P9WEJ4; A0AAT9JB48;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-FEB-2025, sequence version 1.\nDT   28-JAN-2026, entry version 4.\nDE   RecName: Full=Uncharacterized protein YFR035W-A {ECO:0000305};\nGN   OrderedLocusNames=YFR035W-A {ECO:0000312|SGD:S000350095};\nOS   Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Saccharomycotina; Saccharomycetes;\nOC   Saccharomycetales; Saccharomycetaceae; Saccharomyces.\nOX   NCBI_TaxID=559292;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:21.235682+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-11",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "620602a41d8671c8701df46a7d19236b30cfbea35740e43343f9e3862130e866",
  "url": "https://rest.uniprot.org/unisave/P9WEJ4?format=txt&versions=4"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P9WEJ4?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H2",
  "excerpt": "DR   GO; GO:0140580; F:mitochondrion autophagosome adaptor activity; IEA:InterPro.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:21.235682+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 61-61",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "620602a41d8671c8701df46a7d19236b30cfbea35740e43343f9e3862130e866",
  "url": "https://rest.uniprot.org/unisave/P9WEJ4?format=txt&versions=4"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0019787\nname: ubiquitin-like protein transferase activity\nnamespace: molecular_function\nalt_id: GO:0008639\nalt_id: GO:0008640\ndef: \"Catalysis of the transfer of a ubiquitin-like from one protein to another via the reaction X-ULP + Y = Y-ULP + X, where both X-ULP and Y-ULP are covalent linkages. ULP represents a ubiquitin-like protein.\" [GOC:mah, GOC:rn, PMID:10806345, PMID:10884686]\nsubset: goslim_drosophila\nsubset: goslim_pir\nsynonym: \"E2\" BROAD []\nsynonym: \"E3\" RELATED [GOC:dph]\nsynonym: \"small conjugating protein ligase activity\" NARROW [GOC:dph]\nsynonym: \"small conjugating protein transferase activity\" EXACT [GOC:dph]\nsynonym: \"small protein conjugating enzyme activity\" NARROW []\nsynonym: \"ubiquitin-like conjugating enzyme activity\" NARROW []\nsynonym: \"ubiquitin-like-protein ligase activity\" NARROW []\nxref: Reactome:R-HSA-5678490 \"ATG16L1 complex transfers LC3 from ATG3 to PE\"\nxref: Reactome:R-HSA-688137 \"RIP2 is K63 polyubiquitinated\"\nis_a: GO:0016755 ! aminoacyltransferase activity\nis_a: GO:0140096 ! catalytic activity, acting on a protein\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0019787",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 153098-153118",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO2",
  "excerpt": "[Term]\nid: GO:0043720\nname: 3-keto-5-aminohexanoate cleavage activity\nnamespace: molecular_function\ndef: \"Catalysis of the reaction: 3-keto-5-aminohexanoate + acetyl-CoA = L-3-aminobutyryl-CoA + acetoacetate.\" [MetaCyc:R125-RXN, PMID:13064]\nsynonym: \"3-keto-5-aminohexanoate cleavage enzyme\" EXACT []\nxref: MetaCyc:R125-RXN\nxref: RHEA:31555\nis_a: GO:0016747 ! acyltransferase activity, transferring groups other than amino-acyl groups\nproperty_value: skos:exactMatch RHEA:31555\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0043720",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 250073-250083",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO3",
  "excerpt": "[Term]\nid: GO:0046789\nname: host cell surface receptor binding\nnamespace: molecular_function\ndef: \"Binding to a receptor on the host cell surface.\" [GOC:ai, PMID:11511370]\nsubset: goslim_chembl\nsynonym: \"cell surface antigen activity, host-interacting\" RELATED []\nsynonym: \"cell surface receptor ligand\" RELATED []\nis_a: GO:0046812 ! host cell surface binding\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0046789",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 280483-280492",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO4

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO4",
  "excerpt": "[Term]\nid: GO:0140580\nname: mitochondrion autophagosome adaptor activity\nnamespace: molecular_function\ndef: \"The binding activity of a molecule that brings together a mitochondrial membrane and an autophagosome membrane during mitophagy.\" [PMID:33138913]\nsynonym: \"mitophagy receptor\" EXACT []\nis_a: GO:0160183 ! autophagosome-membrane adaptor activity\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0140580",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 441562-441569",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 6. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
