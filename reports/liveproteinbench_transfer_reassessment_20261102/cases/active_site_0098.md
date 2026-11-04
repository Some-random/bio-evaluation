# active_site_0098

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/active_site_0098.txt)

**Task:** `active_site`  
**Expected answer:** **D** — Position 166 (Proton donor)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MRFSASLLLALTGSAAASPIRAEEEIRVYDLPISLFDDLQGLDAAMKAAGREYIGTSLTVRNDFQEQNIIRTEFGSITPENAQKWDATEPNRGQFTFGSADQHMDWARQNGKHVRCHTLVWYSQLPGWVSNSGFNNATLQQVMQNHINQVMGRYRGRCNHWDVVNEAPRLMAMRLQIGEAYIPIAFRMAAQADPSAKLYYNDYNLEYLGPKVEGAARIVRLVKQYGARIDGVGYQAHLVTEPTPTQSTPTPSEEDLIKALRITADLGVDVAYTEIDIRMRTPSNAQKLQQLADAYYRVARSCMKVPRCVGMTIWGVTDRYSWVPNTFRGEGDALLWDSNYQRKAAYNAFLRGIQEPVN

[Multiple Choices]
A. Position 538 (Proton acceptor)
B. Position 67 (Proton acceptor)
C. Position 2153 (For beta-ketoacyl synthase 2 activity)
D. Position 166 (Proton donor)
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzyme Active Site Prediction, which is to identify the key amino acid residues that form the active site of an enzyme. The active site is the specific region on the enzyme where a substrate binds and the chemical reaction is catalyzed. Based on the full protein sequence provided, you must select the option that correctly lists the amino acid residues (by their type and position) that constitute the enzyme's catalytic center.. The inputs provided by the user for this task include:

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

> The sequence-matched UniProt annotation identifies residue 166 as the proton donor. This annotation is based on a PROSITE-ProRule computational inference, not direct experimental evidence in the supplied excerpts.

Citations as saved: [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with a fungal endo-xylanase, whose related enzymes use conserved catalytic glutamates. Residue 166 is glutamate in the supplied sequence, making the proton-donor choice plausible by transferable family knowledge. The other listed positions are less plausible: 538 and 2153 exceed the sequence length, and residue 67 is glutamine.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level catalytic-residue patterns, together with the sequence and the alternatives, provide a meaningful basis for selecting D without needing the target's database annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the offered choices, D is the only plausible in-range catalytic-residue option with the indicated donor role.


### Important caveats

- The supporting annotation is computationally assigned by a PROSITE rule; the excerpts do not establish direct experimental validation of residue 166's role.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a fungal endo-xylanase, whose related enzymes use conserved catalytic glutamates. Residue 166 is glutamate in the supplied sequence, making the proton-donor choice plausible by transferable family knowledge. The other listed positions are less plausible: 538 and 2153 exceed the sequence length, and residue 67 is glutamine.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level catalytic-residue patterns, together with the sequence and the alternatives, provide a meaningful basis for selecting D without needing the target's database annotation."
  },
  "case_id": "active_site_0098",
  "expected_answer_check": {
    "evidence_ids": [
      "C5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies residue 166 as the proton donor. This annotation is based on a PROSITE-ProRule computational inference, not direct experimental evidence in the supplied excerpts."
  },
  "important_caveats": [
    "The supporting annotation is computationally assigned by a PROSITE rule; the excerpts do not establish direct experimental validation of residue 166's role."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, D is the only plausible in-range catalytic-residue option with the indicated donor role."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0098",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies residue 166 as the proton donor. This annotation is based on a PROSITE-ProRule computational inference, not direct experimental evidence in the supplied excerpts.",
    "evidence_ids": ["C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with a fungal endo-xylanase, whose related enzymes use conserved catalytic glutamates. Residue 166 is glutamate in the supplied sequence, making the proton-donor choice plausible by transferable family knowledge. The other listed positions are less plausible: 538 and 2153 exceed the sequence length, and residue 67 is glutamine.",
    "missing_item_specific_fact": "",
    "reason": "Family-level catalytic-residue patterns, together with the sequence and the alternatives, provide a meaningful basis for selecting D without needing the target's database annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, D is the only plausible in-range catalytic-residue option with the indicated donor role."
  },
  "important_caveats": [
    "The supporting annotation is computationally assigned by a PROSITE rule; the excerpts do not establish direct experimental validation of residue 166's role."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry M4MLB5 (Endo-1,4-beta-xylanase B, EC 3.2.1.8) annotates position 166 as 'Proton donor' active site (evidence C5, H3). The sequence residue at position 166 is Glu (E), consistent with the canonical proton donor role in GH10 glycoside hydrolases. The annotation evidence code is ECO:0000255 (PROSITE-ProRule:PRU01096), indicating a computational/profile-based assignment rather than direct experimental mutagenesis, but it is the database annotation that supports the key. The sequence matches the source (358 AA, SHA256 match).

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C6](#evidence-c6), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Options A (position 538) and C (position 2153) can be immediately eliminated because the provided sequence is only 358 amino acids long—these positions do not exist. Additionally, option C references 'beta-ketoacyl synthase 2 activity,' an entirely unrelated enzyme function. Between the remaining options B (position 67, described as 'Proton acceptor') and D (position 166, described as 'Proton donor'), a model can count the sequence: position 67 is Gln (Q) and position 166 is Glu (E). From general knowledge of glycoside hydrolase catalytic mechanisms (GH10, GH11, GH43, etc.), the proton donor is invariably a Glu (or occasionally Asp) carboxylate, while Gln is not a typical catalytic acid/base residue. The 'Proton donor' label paired with Glu at position 166 is the mechanistically consistent choice, whereas a Gln labeled 'Proton acceptor' is atypical for glycosidic bond hydrolysis. This combination of length-based elimination and family-level mechanistic knowledge meaningfully distinguishes D.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The model can eliminate A and C by simple sequence-length arithmetic (positions exceed 358 AA). Between B and D, general knowledge of glycoside hydrolase catalytic chemistry (Glu as proton donor, not Gln) and the amino acid identity at each position (E at 166, Q at 67) provides a concrete, transferable basis for selecting D without needing to recall this specific protein's database record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A and C are physically impossible (positions beyond the 358-residue sequence). Option B pairs a non-catalytic Gln with a 'Proton acceptor' role inconsistent with glycoside hydrolase chemistry. Only D is both structurally possible and mechanistically consistent.


### Important caveats

- The active site annotation (position 166, proton donor) is derived from PROSITE-ProRule (ECO:0000255), a computational profile-based assignment, not direct site-directed mutagenesis or crystallographic proof for this specific enzyme.
- The protein is annotated as a precursor; position numbering refers to the full precursor sequence including the signal peptide.
- Options A and C are trivially eliminable by sequence length, making the question easier than it might appear; the real discrimination is between B and D.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Options A (position 538) and C (position 2153) can be immediately eliminated because the provided sequence is only 358 amino acids long—these positions do not exist. Additionally, option C references 'beta-ketoacyl synthase 2 activity,' an entirely unrelated enzyme function. Between the remaining options B (position 67, described as 'Proton acceptor') and D (position 166, described as 'Proton donor'), a model can count the sequence: position 67 is Gln (Q) and position 166 is Glu (E). From general knowledge of glycoside hydrolase catalytic mechanisms (GH10, GH11, GH43, etc.), the proton donor is invariably a Glu (or occasionally Asp) carboxylate, while Gln is not a typical catalytic acid/base residue. The 'Proton donor' label paired with Glu at position 166 is the mechanistically consistent choice, whereas a Gln labeled 'Proton acceptor' is atypical for glycosidic bond hydrolysis. This combination of length-based elimination and family-level mechanistic knowledge meaningfully distinguishes D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The model can eliminate A and C by simple sequence-length arithmetic (positions exceed 358 AA). Between B and D, general knowledge of glycoside hydrolase catalytic chemistry (Glu as proton donor, not Gln) and the amino acid identity at each position (E at 166, Q at 67) provides a concrete, transferable basis for selecting D without needing to recall this specific protein's database record."
  },
  "case_id": "active_site_0098",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C6",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry M4MLB5 (Endo-1,4-beta-xylanase B, EC 3.2.1.8) annotates position 166 as 'Proton donor' active site (evidence C5, H3). The sequence residue at position 166 is Glu (E), consistent with the canonical proton donor role in GH10 glycoside hydrolases. The annotation evidence code is ECO:0000255 (PROSITE-ProRule:PRU01096), indicating a computational/profile-based assignment rather than direct experimental mutagenesis, but it is the database annotation that supports the key. The sequence matches the source (358 AA, SHA256 match)."
  },
  "important_caveats": [
    "The active site annotation (position 166, proton donor) is derived from PROSITE-ProRule (ECO:0000255), a computational profile-based assignment, not direct site-directed mutagenesis or crystallographic proof for this specific enzyme.",
    "The protein is annotated as a precursor; position numbering refers to the full precursor sequence including the signal peptide.",
    "Options A and C are trivially eliminable by sequence length, making the question easier than it might appear; the real discrimination is between B and D."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and C are physically impossible (positions beyond the 358-residue sequence). Option B pairs a non-catalytic Gln with a 'Proton acceptor' role inconsistent with glycoside hydrolase chemistry. Only D is both structurally possible and mechanistically consistent."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0098",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry M4MLB5 (Endo-1,4-beta-xylanase B, EC 3.2.1.8) annotates position 166 as 'Proton donor' active site (evidence C5, H3). The sequence residue at position 166 is Glu (E), consistent with the canonical proton donor role in GH10 glycoside hydrolases. The annotation evidence code is ECO:0000255 (PROSITE-ProRule:PRU01096), indicating a computational/profile-based assignment rather than direct experimental mutagenesis, but it is the database annotation that supports the key. The sequence matches the source (358 AA, SHA256 match).",
    "evidence_ids": ["C5", "H3", "C6", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Options A (position 538) and C (position 2153) can be immediately eliminated because the provided sequence is only 358 amino acids long—these positions do not exist. Additionally, option C references 'beta-ketoacyl synthase 2 activity,' an entirely unrelated enzyme function. Between the remaining options B (position 67, described as 'Proton acceptor') and D (position 166, described as 'Proton donor'), a model can count the sequence: position 67 is Gln (Q) and position 166 is Glu (E). From general knowledge of glycoside hydrolase catalytic mechanisms (GH10, GH11, GH43, etc.), the proton donor is invariably a Glu (or occasionally Asp) carboxylate, while Gln is not a typical catalytic acid/base residue. The 'Proton donor' label paired with Glu at position 166 is the mechanistically consistent choice, whereas a Gln labeled 'Proton acceptor' is atypical for glycosidic bond hydrolysis. This combination of length-based elimination and family-level mechanistic knowledge meaningfully distinguishes D.",
    "missing_item_specific_fact": "",
    "reason": "The model can eliminate A and C by simple sequence-length arithmetic (positions exceed 358 AA). Between B and D, general knowledge of glycoside hydrolase catalytic chemistry (Glu as proton donor, not Gln) and the amino acid identity at each position (E at 166, Q at 67) provides a concrete, transferable basis for selecting D without needing to recall this specific protein's database record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and C are physically impossible (positions beyond the 358-residue sequence). Option B pairs a non-catalytic Gln with a 'Proton acceptor' role inconsistent with glycoside hydrolase chemistry. Only D is both structurally possible and mechanistically consistent."
  },
  "important_caveats": [
    "The active site annotation (position 166, proton donor) is derived from PROSITE-ProRule (ECO:0000255), a computational profile-based assignment, not direct site-directed mutagenesis or crystallographic proof for this specific enzyme.",
    "The protein is annotated as a precursor; position numbering refers to the full precursor sequence including the signal peptide.",
    "Options A and C are trivially eliminable by sequence length, making the question easier than it might appear; the real discrimination is between B and D."
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
  "benchmark_sequence_length": 358,
  "benchmark_sequence_sha256": "0e3a88e10bc9db802cafcf77a32ab155d7b9003c45924dd5d25ec8dc07d86905",
  "current_entry_audit": {
    "entryVersion": 33,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2013-05-29",
    "sequenceVersion": 1
  },
  "current_record_sha256": "9737e107c7508ede0abc7bd8c8f14f35fc885d5000f5778fdd13b8d4054f912f",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 358,
  "current_source_sequence_sha256": "0e3a88e10bc9db802cafcf77a32ab155d7b9003c45924dd5d25ec8dc07d86905",
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
  "requested_accession": "M4MLB5",
  "selected_historical_entry_version": 31,
  "selected_historical_record_sha256": "8a61ff0bb76d82894c8a3570170d306b45992420e142ae76129e353039c9cab6",
  "selected_historical_source_sequence_length": 358,
  "selected_historical_source_sequence_sha256": "0e3a88e10bc9db802cafcf77a32ab155d7b9003c45924dd5d25ec8dc07d86905",
  "selected_historical_version": {
    "accession": "M4MLB5",
    "database": "Swiss-Prot",
    "entryVersion": 31,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "XYNB_HUMIN",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/M4MLB5.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"M4MLB5\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:12.159556+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9737e107c7508ede0abc7bd8c8f14f35fc885d5000f5778fdd13b8d4054f912f",
  "url": "https://rest.uniprot.org/uniprotkb/M4MLB5.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/M4MLB5.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":33,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2013-05-29\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:12.159556+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9737e107c7508ede0abc7bd8c8f14f35fc885d5000f5778fdd13b8d4054f912f",
  "url": "https://rest.uniprot.org/uniprotkb/M4MLB5.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/M4MLB5.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Soft-rot fungus\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Sordariomycetes\",\"Sordariomycetidae\",\"Sordariales\",\"Chaetomiaceae\",\"Mycothermus\"],\"scientificName\":\"Humicola insolens\",\"taxonId\":85995}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:12.159556+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9737e107c7508ede0abc7bd8c8f14f35fc885d5000f5778fdd13b8d4054f912f",
  "url": "https://rest.uniprot.org/uniprotkb/M4MLB5.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/M4MLB5.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"1,4-beta-D-xylan xylanohydrolase B\"}}],\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"23306124\",\"source\":\"PubMed\"}],\"value\":\"3.2.1.8\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"23306124\",\"source\":\"PubMed\"}],\"value\":\"Endo-1,4-beta-xylanase B\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:12.159556+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9737e107c7508ede0abc7bd8c8f14f35fc885d5000f5778fdd13b8d4054f912f",
  "url": "https://rest.uniprot.org/uniprotkb/M4MLB5.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/M4MLB5.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Proton donor\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01096\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":166},\"start\":{\"modifier\":\"EXACT\",\"value\":166}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-01T06:25:12.159556+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9737e107c7508ede0abc7bd8c8f14f35fc885d5000f5778fdd13b8d4054f912f",
  "url": "https://rest.uniprot.org/uniprotkb/M4MLB5.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/M4MLB5.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"Nucleophile\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01096\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":274},\"start\":{\"modifier\":\"EXACT\",\"value\":274}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-01T06:25:12.159556+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9737e107c7508ede0abc7bd8c8f14f35fc885d5000f5778fdd13b8d4054f912f",
  "url": "https://rest.uniprot.org/uniprotkb/M4MLB5.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/M4MLB5.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Du Y.\",\"Shi P.\",\"Huang H.\",\"Zhang X.\",\"Luo H.\",\"Wang Y.\",\"Yao B.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"23306124\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.biortech.2012.12.067\"}],\"citationType\":\"journal article\",\"firstPage\":\"161\",\"id\":\"23306124\",\"journal\":\"Bioresour. Technol.\",\"lastPage\":\"167\",\"publicationDate\":\"2013\",\"title\":\"Characterization of three novel thermophilic xylanases from Humicola insolens Y1 with application potentials in the brewing industry.\",\"volume\":\"130\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"Y1\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"SUBSTRATE SPECIFICITY\",\"ACTIVITY REGULATION\",\"BIOTECHNOLOGY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-01T06:25:12.159556+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9737e107c7508ede0abc7bd8c8f14f35fc885d5000f5778fdd13b8d4054f912f",
  "url": "https://rest.uniprot.org/uniprotkb/M4MLB5.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/M4MLB5?format=txt&versions=31)

```json
{
  "entry_version": 31,
  "evidence_id": "H1",
  "excerpt": "ID   XYNB_HUMIN              Reviewed;         358 AA.\nAC   M4MLB5;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   29-MAY-2013, sequence version 1.\nDT   28-JAN-2026, entry version 31.\nDE   RecName: Full=Endo-1,4-beta-xylanase B {ECO:0000303|PubMed:23306124};\nDE            EC=3.2.1.8 {ECO:0000269|PubMed:23306124};\nDE   AltName: Full=1,4-beta-D-xylan xylanohydrolase B {ECO:0000305};\nDE   Flags: Precursor;\nGN   Name=XynB {ECO:0000303|PubMed:23306124};\nOS   Humicola insolens (Soft-rot fungus).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;\nOC   Sordariomycetidae; Sordariales; Chaetomiaceae; Mycothermus.\nOX   NCBI_TaxID=85995;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:16.229298+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8a61ff0bb76d82894c8a3570170d306b45992420e142ae76129e353039c9cab6",
  "url": "https://rest.uniprot.org/unisave/M4MLB5?format=txt&versions=31"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/M4MLB5?format=txt&versions=31)

```json
{
  "entry_version": 31,
  "evidence_id": "H2",
  "excerpt": "RN   [1]\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY,\nRP   BIOPHYSICOCHEMICAL PROPERTIES, SUBSTRATE SPECIFICITY, ACTIVITY REGULATION,\nRP   AND BIOTECHNOLOGY.\nRC   STRAIN=Y1;\nRX   PubMed=23306124; DOI=10.1016/j.biortech.2012.12.067;\nRA   Du Y., Shi P., Huang H., Zhang X., Luo H., Wang Y., Yao B.;\nRT   \"Characterization of three novel thermophilic xylanases from Humicola\nRT   insolens Y1 with application potentials in the brewing industry.\";\nRL   Bioresour. Technol. 130:161-167(2013).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:16.229298+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 15-24",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8a61ff0bb76d82894c8a3570170d306b45992420e142ae76129e353039c9cab6",
  "url": "https://rest.uniprot.org/unisave/M4MLB5?format=txt&versions=31"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/M4MLB5?format=txt&versions=31)

```json
{
  "entry_version": 31,
  "evidence_id": "H3",
  "excerpt": "FT   ACT_SITE        166\nFT                   /note=\"Proton donor\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU01096\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:16.229298+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 109-111",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8a61ff0bb76d82894c8a3570170d306b45992420e142ae76129e353039c9cab6",
  "url": "https://rest.uniprot.org/unisave/M4MLB5?format=txt&versions=31"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/M4MLB5?format=txt&versions=31)

```json
{
  "entry_version": 31,
  "evidence_id": "H4",
  "excerpt": "FT   ACT_SITE        274\nFT                   /note=\"Nucleophile\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU01096\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:16.229298+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 112-114",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8a61ff0bb76d82894c8a3570170d306b45992420e142ae76129e353039c9cab6",
  "url": "https://rest.uniprot.org/unisave/M4MLB5?format=txt&versions=31"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 98. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
