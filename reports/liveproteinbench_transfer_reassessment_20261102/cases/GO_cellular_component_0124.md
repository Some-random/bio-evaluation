# GO_cellular_component_0124

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_cellular_component_0124.txt)

**Task:** `GO_cellular_component`  
**Expected answer:** **C** — peroxisomal membrane

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | uncertain | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MESMVNNLWSSWDTLSQATASTGGDMDAASVASKQSPQESKMAASSMIWSSFSEPQKTPPTKRASSSFFDDMFTSSKDHSTTLTDKMFERFLSMALPTTTTQDGEELQSILERIEMQKSRPQLSLNVMSKNAIQLLSRLSVPFVLIDQVIIIFSWSKPLYTLTFLNVATLLILKPILLLSLPFFYTCFEIIVPAYMKRHPPDKHTILQNRNPIPAEGPSVSHVDVPRPVPELSREFVLNSTDLQNHMLLYVMSYDFVTSLIVKYLYFKDENITIFIFVALLTSGTLLTLFGAQVLSAMLPFIKVTLSVGLWAATIAMHPNYRSTLLDMLYSEDTRLRLLMMSNRLELWLNKELNLREQKEVKETEIFELQHLDPETHNWQLICFSSDPYPANSHARLNNLPLLGTLHLSQVKPPEGWKFVDVETAVNTRSVDGWLLDLTPEGWIKENFLNETMDIDEDEKWCYDLVTKFSYQAGLTTNEKKTRGEVRRRRWIRYCVRDIWDEDDQMEETVAHRRNKSMESSNSLHPVKSIDSVDG

[Multiple Choices]
A. actin cytoskeleton
B. cytosol
C. peroxisomal membrane
D. virus tail, tube
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Cellular Component Prediction, which is to predict the primary Cellular Component where a protein is located, according to the Gene Ontology (GO) framework. A protein's location within a cell (e.g., Nucleus, Mitochondria, Cytoplasm) is critical for its function and is often determined by specific targeting signals in its amino acid sequence. Based on the provided sequence, you must identify the most likely compartment where the protein resides.. The inputs provided by the user for this task include:

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

### Expected-answer support: uncertain

> The sequence-matched record has an experimentally supported ER-membrane localization (C5, C6; also H3), while peroxisomal membrane is listed only as a computational GO annotation (C7; H5). The experimental evidence does not rule out additional peroxisomal localization, but the supplied evidence does not establish peroxisomal membrane as the primary location.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H3](#evidence-h3), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains multiple long hydrophobic stretches consistent with a multipass integral membrane protein. Among the choices, peroxisomal membrane is the only membrane compartment; a cytosolic or actin-cytoskeleton protein would not fit that sequence pattern, and a virus-tail tube protein is also implausible for this eukaryotic-looking multipass protein.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable sequence knowledge meaningfully favors C over the offered alternatives, though it supports membrane association more strongly than peroxisome-specific localization.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No second offered option is comparably supported by the multipass membrane sequence pattern. However, the evidence points to ER membrane, which is not an option, and does not establish that peroxisomal membrane is the primary location.


### Important caveats

- The peroxisomal membrane annotation is computational, whereas the cited ER-membrane localization is experimentally supported.
- A general membrane-protein inference cannot by itself distinguish ER from peroxisomal membrane.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains multiple long hydrophobic stretches consistent with a multipass integral membrane protein. Among the choices, peroxisomal membrane is the only membrane compartment; a cytosolic or actin-cytoskeleton protein would not fit that sequence pattern, and a virus-tail tube protein is also implausible for this eukaryotic-looking multipass protein.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable sequence knowledge meaningfully favors C over the offered alternatives, though it supports membrane association more strongly than peroxisome-specific localization."
  },
  "case_id": "GO_cellular_component_0124",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "H3",
      "H5"
    ],
    "judgment": "cannot_determine",
    "reason": "The sequence-matched record has an experimentally supported ER-membrane localization (C5, C6; also H3), while peroxisomal membrane is listed only as a computational GO annotation (C7; H5). The experimental evidence does not rule out additional peroxisomal localization, but the supplied evidence does not establish peroxisomal membrane as the primary location."
  },
  "important_caveats": [
    "The peroxisomal membrane annotation is computational, whereas the cited ER-membrane localization is experimentally supported.",
    "A general membrane-protein inference cannot by itself distinguish ER from peroxisomal membrane."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No second offered option is comparably supported by the multipass membrane sequence pattern. However, the evidence points to ER membrane, which is not an option, and does not establish that peroxisomal membrane is the primary location."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0124",
  "expected_answer_check": {
    "judgment": "cannot_determine",
    "reason": "The sequence-matched record has an experimentally supported ER-membrane localization (C5, C6; also H3), while peroxisomal membrane is listed only as a computational GO annotation (C7; H5). The experimental evidence does not rule out additional peroxisomal localization, but the supplied evidence does not establish peroxisomal membrane as the primary location.",
    "evidence_ids": ["C5", "C6", "C7", "H3", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains multiple long hydrophobic stretches consistent with a multipass integral membrane protein. Among the choices, peroxisomal membrane is the only membrane compartment; a cytosolic or actin-cytoskeleton protein would not fit that sequence pattern, and a virus-tail tube protein is also implausible for this eukaryotic-looking multipass protein.",
    "missing_item_specific_fact": "",
    "reason": "Transferable sequence knowledge meaningfully favors C over the offered alternatives, though it supports membrane association more strongly than peroxisome-specific localization."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No second offered option is comparably supported by the multipass membrane sequence pattern. However, the evidence points to ER membrane, which is not an option, and does not establish that peroxisomal membrane is the primary location."
  },
  "important_caveats": [
    "The peroxisomal membrane annotation is computational, whereas the cited ER-membrane localization is experimentally supported.",
    "A general membrane-protein inference cannot by itself distinguish ER from peroxisomal membrane."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein is annotated as 'Peroxisomal membrane protein PEX29' (C4/H1), a peroxin family member involved in peroxisome biogenesis. A GO annotation for peroxisomal membrane (GO:0005778) exists (C7/H5), though at IEA level. The experimental subcellular localization (C5/H3, ECO:0000269 from PubMed:32665322) actually places it at the ER membrane, which is a known transit station for peroxisomal membrane proteins during biogenesis. The protein's name, peroxin family membership, and the peroxisomal membrane GO annotation collectively support the author's key, even though the primary experimental localization evidence is for ER membrane.

Citations as saved: [C4](#evidence-c4), [C7](#evidence-c7), [H1](#evidence-h1), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains numerous long hydrophobic stretches (e.g., 'MSKNAIQLLSRLSVPFVLIDQVIIIFSWSKPLYTLTFLNVATLLILKPILLLSLPFFYTCFEIIVPAYM', 'IFIFVALLTSGTLLTLFGAQVLSAMLPFIKVTLSVGLWAATIAMHPNYRSTLLDMLYSEDTRLRLLMMSNRLELWLNKELNLREQKEVKETEIFELQHLDPETHNWQLICFSSDPYPANSHARLNNLPLLGTLHLSQVKPPEGWKFVDVETAVNTRSVDGWLLDLTPEGWIKENFLNETMDIDEDEKWCYDLVTKFSYQAGLTTNEKKTRGEVRRRRWIRYCVRDIWDEDDQMEETVAHRRNKSMESSNSLHPVKSIDSVDG') indicating a multi-pass transmembrane protein. This immediately eliminates cytosol (B) and actin cytoskeleton (A), which are soluble compartments. The eukaryotic context and protein size (~535 aa) make virus tail tube (D) implausible. Among the four choices, peroxisomal membrane (C) is the only membrane compartment offered. Furthermore, family-level knowledge of peroxins (PEX3, PEX16, PEX25, PEX29, etc.) as multi-pass membrane proteins localized to the peroxisomal membrane provides a positive inference: the multi-TM architecture with basic clusters (RRRRWIRY) is characteristic of peroxisomal membrane peroxins. A knowledgeable model can eliminate A, B, and D and select C by recognizing the multi-pass membrane topology and applying general knowledge that such proteins in eukaryotes localize to membrane compartments, with peroxisomal membrane being the only membrane option provided.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The elimination reasoning is strong: a multi-pass membrane eukaryotic protein cannot be in the cytosol, on the actin cytoskeleton, or be a virus tail tube. Peroxisomal membrane is the sole membrane compartment among the choices. Additionally, the multi-TM architecture with basic residue clusters matches the known pattern of peroxisomal membrane peroxins learned from other PEX proteins.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices are well-separated: two are soluble compartments (A, B), one is a viral structure (D), and one is a membrane compartment (C). A multi-pass membrane protein in a eukaryote is incompatible with A, B, and D, leaving C unambiguous among the offered alternatives.


### Important caveats

- The experimental (EXP) subcellular localization evidence actually places this protein at the ER membrane, not the peroxisomal membrane. The peroxisomal membrane annotation is IEA-level. The ER-to-peroxisome transit is a known phenomenon for peroxisomal membrane proteins.
- The author's key relies on the protein's identity as a peroxin (PEX29) and its peroxisomal membrane GO annotation rather than the primary experimental localization data.
- The reviewer-only evidence confirms sequence match to W1QL91 (PEX29_OGAPD), but this accession was not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains numerous long hydrophobic stretches (e.g., 'MSKNAIQLLSRLSVPFVLIDQVIIIFSWSKPLYTLTFLNVATLLILKPILLLSLPFFYTCFEIIVPAYM', 'IFIFVALLTSGTLLTLFGAQVLSAMLPFIKVTLSVGLWAATIAMHPNYRSTLLDMLYSEDTRLRLLMMSNRLELWLNKELNLREQKEVKETEIFELQHLDPETHNWQLICFSSDPYPANSHARLNNLPLLGTLHLSQVKPPEGWKFVDVETAVNTRSVDGWLLDLTPEGWIKENFLNETMDIDEDEKWCYDLVTKFSYQAGLTTNEKKTRGEVRRRRWIRYCVRDIWDEDDQMEETVAHRRNKSMESSNSLHPVKSIDSVDG') indicating a multi-pass transmembrane protein. This immediately eliminates cytosol (B) and actin cytoskeleton (A), which are soluble compartments. The eukaryotic context and protein size (~535 aa) make virus tail tube (D) implausible. Among the four choices, peroxisomal membrane (C) is the only membrane compartment offered. Furthermore, family-level knowledge of peroxins (PEX3, PEX16, PEX25, PEX29, etc.) as multi-pass membrane proteins localized to the peroxisomal membrane provides a positive inference: the multi-TM architecture with basic clusters (RRRRWIRY) is characteristic of peroxisomal membrane peroxins. A knowledgeable model can eliminate A, B, and D and select C by recognizing the multi-pass membrane topology and applying general knowledge that such proteins in eukaryotes localize to membrane compartments, with peroxisomal membrane being the only membrane option provided.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The elimination reasoning is strong: a multi-pass membrane eukaryotic protein cannot be in the cytosol, on the actin cytoskeleton, or be a virus tail tube. Peroxisomal membrane is the sole membrane compartment among the choices. Additionally, the multi-TM architecture with basic residue clusters matches the known pattern of peroxisomal membrane peroxins learned from other PEX proteins."
  },
  "case_id": "GO_cellular_component_0124",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C7",
      "H1",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The protein is annotated as 'Peroxisomal membrane protein PEX29' (C4/H1), a peroxin family member involved in peroxisome biogenesis. A GO annotation for peroxisomal membrane (GO:0005778) exists (C7/H5), though at IEA level. The experimental subcellular localization (C5/H3, ECO:0000269 from PubMed:32665322) actually places it at the ER membrane, which is a known transit station for peroxisomal membrane proteins during biogenesis. The protein's name, peroxin family membership, and the peroxisomal membrane GO annotation collectively support the author's key, even though the primary experimental localization evidence is for ER membrane."
  },
  "important_caveats": [
    "The experimental (EXP) subcellular localization evidence actually places this protein at the ER membrane, not the peroxisomal membrane. The peroxisomal membrane annotation is IEA-level. The ER-to-peroxisome transit is a known phenomenon for peroxisomal membrane proteins.",
    "The author's key relies on the protein's identity as a peroxin (PEX29) and its peroxisomal membrane GO annotation rather than the primary experimental localization data.",
    "The reviewer-only evidence confirms sequence match to W1QL91 (PEX29_OGAPD), but this accession was not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices are well-separated: two are soluble compartments (A, B), one is a viral structure (D), and one is a membrane compartment (C). A multi-pass membrane protein in a eukaryote is incompatible with A, B, and D, leaving C unambiguous among the offered alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0124",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein is annotated as 'Peroxisomal membrane protein PEX29' (C4/H1), a peroxin family member involved in peroxisome biogenesis. A GO annotation for peroxisomal membrane (GO:0005778) exists (C7/H5), though at IEA level. The experimental subcellular localization (C5/H3, ECO:0000269 from PubMed:32665322) actually places it at the ER membrane, which is a known transit station for peroxisomal membrane proteins during biogenesis. The protein's name, peroxin family membership, and the peroxisomal membrane GO annotation collectively support the author's key, even though the primary experimental localization evidence is for ER membrane.",
    "evidence_ids": ["C4", "C7", "H1", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains numerous long hydrophobic stretches (e.g., 'MSKNAIQLLSRLSVPFVLIDQVIIIFSWSKPLYTLTFLNVATLLILKPILLLSLPFFYTCFEIIVPAYM', 'IFIFVALLTSGTLLTLFGAQVLSAMLPFIKVTLSVGLWAATIAMHPNYRSTLLDMLYSEDTRLRLLMMSNRLELWLNKELNLREQKEVKETEIFELQHLDPETHNWQLICFSSDPYPANSHARLNNLPLLGTLHLSQVKPPEGWKFVDVETAVNTRSVDGWLLDLTPEGWIKENFLNETMDIDEDEKWCYDLVTKFSYQAGLTTNEKKTRGEVRRRRWIRYCVRDIWDEDDQMEETVAHRRNKSMESSNSLHPVKSIDSVDG') indicating a multi-pass transmembrane protein. This immediately eliminates cytosol (B) and actin cytoskeleton (A), which are soluble compartments. The eukaryotic context and protein size (~535 aa) make virus tail tube (D) implausible. Among the four choices, peroxisomal membrane (C) is the only membrane compartment offered. Furthermore, family-level knowledge of peroxins (PEX3, PEX16, PEX25, PEX29, etc.) as multi-pass membrane proteins localized to the peroxisomal membrane provides a positive inference: the multi-TM architecture with basic clusters (RRRRWIRY) is characteristic of peroxisomal membrane peroxins. A knowledgeable model can eliminate A, B, and D and select C by recognizing the multi-pass membrane topology and applying general knowledge that such proteins in eukaryotes localize to membrane compartments, with peroxisomal membrane being the only membrane option provided.",
    "missing_item_specific_fact": "",
    "reason": "The elimination reasoning is strong: a multi-pass membrane eukaryotic protein cannot be in the cytosol, on the actin cytoskeleton, or be a virus tail tube. Peroxisomal membrane is the sole membrane compartment among the choices. Additionally, the multi-TM architecture with basic residue clusters matches the known pattern of peroxisomal membrane peroxins learned from other PEX proteins."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices are well-separated: two are soluble compartments (A, B), one is a viral structure (D), and one is a membrane compartment (C). A multi-pass membrane protein in a eukaryote is incompatible with A, B, and D, leaving C unambiguous among the offered alternatives."
  },
  "important_caveats": [
    "The experimental (EXP) subcellular localization evidence actually places this protein at the ER membrane, not the peroxisomal membrane. The peroxisomal membrane annotation is IEA-level. The ER-to-peroxisome transit is a known phenomenon for peroxisomal membrane proteins.",
    "The author's key relies on the protein's identity as a peroxin (PEX29) and its peroxisomal membrane GO annotation rather than the primary experimental localization data.",
    "The reviewer-only evidence confirms sequence match to W1QL91 (PEX29_OGAPD), but this accession was not available to the evaluated model."
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
  "benchmark_sequence_length": 535,
  "benchmark_sequence_sha256": "74b2e779608146cca51114d9d1190337b5a9ad8a1f8c3db747e0491092d1ea4d",
  "current_entry_audit": {
    "entryVersion": 43,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2014-03-19",
    "sequenceVersion": 1
  },
  "current_record_sha256": "82521092a67ef997abdc31799f3577764b26227f0c47f2c09c813128fc009f23",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 535,
  "current_source_sequence_sha256": "74b2e779608146cca51114d9d1190337b5a9ad8a1f8c3db747e0491092d1ea4d",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 41,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "W1QL91",
  "selected_historical_entry_version": 41,
  "selected_historical_record_sha256": "2b59cad336a5f0f970c7aa6c93d04cd1ad5885189ae5de312c6383b733a569b7",
  "selected_historical_source_sequence_length": 535,
  "selected_historical_source_sequence_sha256": "74b2e779608146cca51114d9d1190337b5a9ad8a1f8c3db747e0491092d1ea4d",
  "selected_historical_version": {
    "accession": "W1QL91",
    "database": "Swiss-Prot",
    "entryVersion": 41,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "PEX29_OGAPD",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/W1QL91.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"W1QL91\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:34:09.919107+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "82521092a67ef997abdc31799f3577764b26227f0c47f2c09c813128fc009f23",
  "url": "https://rest.uniprot.org/uniprotkb/W1QL91.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/W1QL91.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":43,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2014-03-19\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:34:09.919107+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "82521092a67ef997abdc31799f3577764b26227f0c47f2c09c813128fc009f23",
  "url": "https://rest.uniprot.org/uniprotkb/W1QL91.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/W1QL91.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Yeast\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Saccharomycotina\",\"Pichiomycetes\",\"Pichiales\",\"Pichiaceae\",\"Ogataea\"],\"scientificName\":\"Ogataea parapolymorpha (strain ATCC 26012 / BCRC 20466 / JCM 22074 / NRRL Y-7560 / DL-1)\",\"synonyms\":[\"Hansenula polymorpha\"],\"taxonId\":871575}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:34:09.919107+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "82521092a67ef997abdc31799f3577764b26227f0c47f2c09c813128fc009f23",
  "url": "https://rest.uniprot.org/uniprotkb/W1QL91.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/W1QL91.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Peroxin-29\"}}],\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"32665322\",\"source\":\"PubMed\"}],\"value\":\"Peroxisomal membrane protein PEX29\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:34:09.919107+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "82521092a67ef997abdc31799f3577764b26227f0c47f2c09c813128fc009f23",
  "url": "https://rest.uniprot.org/uniprotkb/W1QL91.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/W1QL91.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"SUBCELLULAR LOCATION\",\"note\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"32665322\",\"source\":\"PubMed\"}],\"value\":\"Localizes to multiple regions of the ER\"}]},\"subcellularLocations\":[{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"32665322\",\"source\":\"PubMed\"}],\"id\":\"SL-0097\",\"value\":\"Endoplasmic reticulum membrane\"},\"topology\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"id\":\"SL-9909\",\"value\":\"Multi-pass membrane protein\"}}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:34:09.919107+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "82521092a67ef997abdc31799f3577764b26227f0c47f2c09c813128fc009f23",
  "url": "https://rest.uniprot.org/uniprotkb/W1QL91.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/W1QL91.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"32665322\",\"source\":\"PubMed\"}],\"id\":\"GO:0005789\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:endoplasmic reticulum membrane\"},{\"key\":\"GoEvidenceType\",\"value\":\"EXP:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/11",
  "retrieved_utc": "2026-11-02T04:34:09.919107+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "82521092a67ef997abdc31799f3577764b26227f0c47f2c09c813128fc009f23",
  "url": "https://rest.uniprot.org/uniprotkb/W1QL91.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/W1QL91.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0005778\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:peroxisomal membrane\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:EnsemblFungi\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/12",
  "retrieved_utc": "2026-11-02T04:34:09.919107+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "82521092a67ef997abdc31799f3577764b26227f0c47f2c09c813128fc009f23",
  "url": "https://rest.uniprot.org/uniprotkb/W1QL91.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/W1QL91.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Wu F.\",\"de Boer R.\",\"Krikken A.M.\",\"Aksit A.\",\"Bordin N.\",\"Devos D.P.\",\"van der Klei I.J.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"32665322\"},{\"database\":\"DOI\",\"id\":\"10.1242/jcs.246983\"}],\"citationType\":\"journal article\",\"firstPage\":\"0\",\"id\":\"32665322\",\"journal\":\"J. Cell Sci.\",\"lastPage\":\"0\",\"publicationDate\":\"2020\",\"title\":\"Pex24 and Pex32 are required to tether peroxisomes to the ER for organelle biogenesis, positioning and segregation in yeast.\",\"volume\":\"133\"},\"referenceNumber\":2,\"referencePositions\":[\"DISRUPTION PHENOTYPE\",\"SUBCELLULAR LOCATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:34:09.919107+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "82521092a67ef997abdc31799f3577764b26227f0c47f2c09c813128fc009f23",
  "url": "https://rest.uniprot.org/uniprotkb/W1QL91.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/W1QL91?format=txt&versions=41)

```json
{
  "entry_version": 41,
  "evidence_id": "H1",
  "excerpt": "ID   PEX29_OGAPD             Reviewed;         535 AA.\nAC   W1QL91;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   19-MAR-2014, sequence version 1.\nDT   28-JAN-2026, entry version 41.\nDE   RecName: Full=Peroxisomal membrane protein PEX29 {ECO:0000303|PubMed:32665322};\nDE   AltName: Full=Peroxin-29 {ECO:0000305};\nGN   Name=PEX29 {ECO:0000303|PubMed:32665322}; ORFNames=HPODL_00080;\nOS   Ogataea parapolymorpha (strain ATCC 26012 / BCRC 20466 / JCM 22074 / NRRL\nOS   Y-7560 / DL-1) (Yeast) (Hansenula polymorpha).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Saccharomycotina; Pichiomycetes;\nOC   Pichiales; Pichiaceae; Ogataea.\nOX   NCBI_TaxID=871575;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:34:13.232116+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "2b59cad336a5f0f970c7aa6c93d04cd1ad5885189ae5de312c6383b733a569b7",
  "url": "https://rest.uniprot.org/unisave/W1QL91?format=txt&versions=41"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/W1QL91?format=txt&versions=41)

```json
{
  "entry_version": 41,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   DISRUPTION PHENOTYPE, AND SUBCELLULAR LOCATION.\nRX   PubMed=32665322; DOI=10.1242/jcs.246983;\nRA   Wu F., de Boer R., Krikken A.M., Aksit A., Bordin N., Devos D.P.,\nRA   van der Klei I.J.;\nRT   \"Pex24 and Pex32 are required to tether peroxisomes to the ER for organelle\nRT   biogenesis, positioning and segregation in yeast.\";\nRL   J. Cell Sci. 133:0-0(2020).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:34:13.232116+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 24-31",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "2b59cad336a5f0f970c7aa6c93d04cd1ad5885189ae5de312c6383b733a569b7",
  "url": "https://rest.uniprot.org/unisave/W1QL91?format=txt&versions=41"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/W1QL91?format=txt&versions=41)

```json
{
  "entry_version": 41,
  "evidence_id": "H3",
  "excerpt": "CC   -!- SUBCELLULAR LOCATION: Endoplasmic reticulum membrane\nCC       {ECO:0000269|PubMed:32665322}; Multi-pass membrane protein\nCC       {ECO:0000255}. Note=Localizes to multiple regions of the ER.\nCC       {ECO:0000269|PubMed:32665322}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:34:13.232116+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 43-46",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "2b59cad336a5f0f970c7aa6c93d04cd1ad5885189ae5de312c6383b733a569b7",
  "url": "https://rest.uniprot.org/unisave/W1QL91?format=txt&versions=41"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/W1QL91?format=txt&versions=41)

```json
{
  "entry_version": 41,
  "evidence_id": "H4",
  "excerpt": "DR   GO; GO:0005789; C:endoplasmic reticulum membrane; IEA:UniProtKB-SubCell.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:34:13.232116+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 70-70",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "2b59cad336a5f0f970c7aa6c93d04cd1ad5885189ae5de312c6383b733a569b7",
  "url": "https://rest.uniprot.org/unisave/W1QL91?format=txt&versions=41"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/W1QL91?format=txt&versions=41)

```json
{
  "entry_version": 41,
  "evidence_id": "H5",
  "excerpt": "DR   GO; GO:0005778; C:peroxisomal membrane; IEA:TreeGrafter.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:34:13.232116+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 71-71",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "2b59cad336a5f0f970c7aa6c93d04cd1ad5885189ae5de312c6383b733a569b7",
  "url": "https://rest.uniprot.org/unisave/W1QL91?format=txt&versions=41"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0005778\nname: peroxisomal membrane\nnamespace: cellular_component\ndef: \"The lipid bilayer surrounding a peroxisome.\" [GOC:mah]\nsynonym: \"peroxisome membrane\" EXACT []\nis_a: GO:0031903 ! microbody membrane\nrelationship: part_of GO:0005777 ! peroxisome\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005778",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 59400-59408",
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
  "excerpt": "[Term]\nid: GO:0005829\nname: cytosol\nnamespace: cellular_component\ndef: \"The part of the cytoplasm that does not contain organelles but which does contain other particulate matter, such as protein complexes.\" [GOC:hjd, GOC:jl]\nsubset: goslim_agr\nsubset: goslim_chembl\nsubset: goslim_drosophila\nsubset: goslim_euk_cellular_processes_ribbon\nsubset: goslim_flybase_ribbon\nsubset: goslim_generic\nsubset: goslim_mouse\nsubset: goslim_plant\nxref: NIF_Subcellular:sao101633890\nxref: Wikipedia:Cytosol\nis_a: GO:0110165 ! cellular anatomical structure\nrelationship: part_of GO:0005737 ! cytoplasm\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005829",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 59936-59953",
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
  "excerpt": "[Term]\nid: GO:0015629\nname: actin cytoskeleton\nnamespace: cellular_component\ndef: \"The part of the cytoskeleton (the internal framework of a cell) composed of actin and associated proteins. Includes actin cytoskeleton-associated complexes.\" [GOC:jl, ISBN:0395825172, ISBN:0815316194]\nis_a: GO:0005856 ! cytoskeleton\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0015629",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 119402-119408",
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
  "excerpt": "[Term]\nid: GO:0098026\nname: virus tail, tube\nnamespace: cellular_component\ndef: \"The internal tube of the tail of some viruses. The virus tail tube is the channel for DNA ejection into the host cytoplasm.\" [PMID:33188213, VZ:3960]\ncomment: Applies in particular the Myoviridae bacteriophages. Many bacteriophages with dsDNA genomes, or Caudovirales, have a tail. The viral tail can be short (Podoviridae), long and non-contractile (Siphoviridae) or long and contractile (Myoviridae). The tail is the channel through which the phage genome is injected into the host bacterial cell.\nsynonym: \"bacteriophage tail tube\" NARROW [GOC:bm]\nxref: VZ:3960 \"Viral tail tube protein\"\nis_a: GO:0044423 ! virion component\nrelationship: part_of GO:0098015 ! virus tail\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0098026",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 408367-408377",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 124. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
