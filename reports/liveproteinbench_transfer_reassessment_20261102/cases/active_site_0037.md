# active_site_0037

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/active_site_0037.txt)

**Task:** `active_site`  
**Expected answer:** **B** — Position 139 (Proton donor/acceptor)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MASENNKRKASEEALSPDSQLQSKKARTDSPEREPKSEGGPLGKPPLRIVPFPEKPAVLEERRGEIEFRVVNNDGSRDSFVVLTGLKCIFQKQLPKMPKDYIARLVYDRSHLSIAIVKHPLEVVGGITYRPFNSRRFAEIVFCAISSDQQVKGYGAHLMSHLKDYVKATSPIMHFLTYADNYAIGYFKKQGFTKEITLDKSIWMGYIKDYEGGTIMQCTMLPKIRYLEIGRMLLKQKEAVHAKIRAFSRSHIIHAPPKEWKNGACKIDPLSIPAIKQSGWSPDMDELARQPRHGPNYNQLLHLLNDMQNHSAAWPFTQPVNRDEVPDYYEVIKEPMDLSTMEEKHEKDMYPTPQDFIKDAMLIFDNCRRYNNENTPYAKSANKLEKFMWQQIRNIPEWSVST

[Multiple Choices]
A. Position 331 (Proton acceptor)
B. Position 139 (Proton donor/acceptor)
C. Position 131 (Charge relay)
D. Position 4094 (For beta-ketoacyl synthase 3 activity)
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

> The sequence-matched UniProt annotation identifies residue 139 as the active-site proton donor/acceptor, with experimental evidence cited to PubMed 39601562. The archived annotation also records this feature. This supports the keyed answer, though the source excerpt does not independently establish the underlying experiment's details.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 402-residue sequence contains a conserved-looking enzymatic region consistent with a GNAT-family acetyltransferase rather than a beta-ketoacyl synthase, and residue 139 is a glutamate in the sequence. Transferable knowledge of GNAT-family histone acetyltransferases supports a catalytic glutamate acting as a proton acceptor during acetyl transfer, favoring B over the proposed charge-relay residue at 131 or position 331. Position 4094 is outside the sequence.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level acetyltransferase mechanism and the sequence's residue identity and numbering give a meaningful basis for choosing B; this does not require knowing the target's database record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The alternatives distinguish a plausible catalytic glutamate from a different position and an unrelated activity; no second option is comparably supported by the sequence and transferable family knowledge.


### Important caveats

- The reviewer-only annotations support the key but were not available as original model input.
- The family identification and catalytic-residue inference are probabilistic, not a substitute for direct structural or experimental evidence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 402-residue sequence contains a conserved-looking enzymatic region consistent with a GNAT-family acetyltransferase rather than a beta-ketoacyl synthase, and residue 139 is a glutamate in the sequence. Transferable knowledge of GNAT-family histone acetyltransferases supports a catalytic glutamate acting as a proton acceptor during acetyl transfer, favoring B over the proposed charge-relay residue at 131 or position 331. Position 4094 is outside the sequence.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level acetyltransferase mechanism and the sequence's residue identity and numbering give a meaningful basis for choosing B; this does not require knowing the target's database record."
  },
  "case_id": "active_site_0037",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies residue 139 as the active-site proton donor/acceptor, with experimental evidence cited to PubMed 39601562. The archived annotation also records this feature. This supports the keyed answer, though the source excerpt does not independently establish the underlying experiment's details."
  },
  "important_caveats": [
    "The reviewer-only annotations support the key but were not available as original model input.",
    "The family identification and catalytic-residue inference are probabilistic, not a substitute for direct structural or experimental evidence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives distinguish a plausible catalytic glutamate from a different position and an unrelated activity; no second option is comparably supported by the sequence and transferable family knowledge."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0037",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies residue 139 as the active-site proton donor/acceptor, with experimental evidence cited to PubMed 39601562. The archived annotation also records this feature. This supports the keyed answer, though the source excerpt does not independently establish the underlying experiment's details.",
    "evidence_ids": ["C5", "H3", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 402-residue sequence contains a conserved-looking enzymatic region consistent with a GNAT-family acetyltransferase rather than a beta-ketoacyl synthase, and residue 139 is a glutamate in the sequence. Transferable knowledge of GNAT-family histone acetyltransferases supports a catalytic glutamate acting as a proton acceptor during acetyl transfer, favoring B over the proposed charge-relay residue at 131 or position 331. Position 4094 is outside the sequence.",
    "missing_item_specific_fact": "",
    "reason": "Family-level acetyltransferase mechanism and the sequence's residue identity and numbering give a meaningful basis for choosing B; this does not require knowing the target's database record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives distinguish a plausible catalytic glutamate from a different position and an unrelated activity; no second option is comparably supported by the sequence and transferable family knowledge."
  },
  "important_caveats": [
    "The reviewer-only annotations support the key but were not available as original model input.",
    "The family identification and catalytic-residue inference are probabilistic, not a substitute for direct structural or experimental evidence."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A7U2QYM2 (Histone acetyltransferase gcnE, EC 2.3.1.48) annotates position 139 as 'Active site: Proton donor/acceptor' with experimental evidence (ECO:0000269, PubMed:39601562). The reference explicitly mentions 'MUTAGENESIS OF GLU-139', confirming Glu-139 as the catalytic residue. The sequence at position 139 is indeed E (Glutamic acid), verified by counting the provided 402-residue sequence. The expected answer B matches the annotated active site.

Citations as saved: [C5](#evidence-c5), [C10](#evidence-c10), [H3](#evidence-h3), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> A knowledgeable model can eliminate options through multiple independent lines of transferable reasoning: (1) Position 4094 is impossible in a 402-residue protein — immediate elimination of D. (2) Counting the sequence reveals position 331 is Isoleucine (I), which cannot function as a 'proton acceptor' — eliminates A. (3) Position 131 is Proline (P), which cannot serve as a 'charge relay' residue — eliminates C. (4) Position 139 is Glutamic acid (E), which is the canonical catalytic proton donor/acceptor in GCN5-related N-acetyltransferase (GNAT) family histone acetyltransferases. The GNAT fold's conserved Glu in the 'PxxxQ' or 'FAE' region activates the lysine ε-amino group for nucleophilic attack on acetyl-CoA. The sequence context around 139 ('PFNSRRFAEI') is consistent with the GNAT catalytic region. This family-level mechanistic knowledge (HATs use a conserved Glu as proton shuttle) combined with residue-identity checks on the provided sequence meaningfully distinguishes B from the other options.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The answer is reachable through: (a) simple arithmetic eliminating D (4094 > 402), (b) residue identity checks at positions 331 (Ile) and 131 (Pro) that are incompatible with the stated catalytic roles, and (c) family-level knowledge that GCN5-related HATs employ a conserved Glutamate as the catalytic proton donor/acceptor, which matches position 139 (E). No fact specific to this exact protein's experimental record is needed beyond what is derivable from the sequence and general HAT/GNAT mechanism knowledge.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A, C, and D are clearly eliminable: D references a nonexistent position, A and C assign impossible roles to Ile and Pro respectively. Only B (Glu-139 as proton donor/acceptor) is consistent with both the residue identity and HAT catalytic mechanism.


### Important caveats

- The UniProt annotation at position 139 carries experimental evidence (ECO:0000269) from a 2025 MBio paper, making it well-supported rather than purely computational.
- The protein is annotated as both a histone acetyltransferase (EC 2.3.1.48) and a benzoyltransferase (EC 2.3.1.-); the catalytic Glu-139 role as proton donor/acceptor applies to both activities.
- The model is not given the protein name or organism; recognition of the GNAT/HAT fold must rely on sequence features or general knowledge, but the residue-identity elimination strategy (checking what amino acid is actually at each position) does not require fold recognition.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A knowledgeable model can eliminate options through multiple independent lines of transferable reasoning: (1) Position 4094 is impossible in a 402-residue protein — immediate elimination of D. (2) Counting the sequence reveals position 331 is Isoleucine (I), which cannot function as a 'proton acceptor' — eliminates A. (3) Position 131 is Proline (P), which cannot serve as a 'charge relay' residue — eliminates C. (4) Position 139 is Glutamic acid (E), which is the canonical catalytic proton donor/acceptor in GCN5-related N-acetyltransferase (GNAT) family histone acetyltransferases. The GNAT fold's conserved Glu in the 'PxxxQ' or 'FAE' region activates the lysine ε-amino group for nucleophilic attack on acetyl-CoA. The sequence context around 139 ('PFNSRRFAEI') is consistent with the GNAT catalytic region. This family-level mechanistic knowledge (HATs use a conserved Glu as proton shuttle) combined with residue-identity checks on the provided sequence meaningfully distinguishes B from the other options.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The answer is reachable through: (a) simple arithmetic eliminating D (4094 > 402), (b) residue identity checks at positions 331 (Ile) and 131 (Pro) that are incompatible with the stated catalytic roles, and (c) family-level knowledge that GCN5-related HATs employ a conserved Glutamate as the catalytic proton donor/acceptor, which matches position 139 (E). No fact specific to this exact protein's experimental record is needed beyond what is derivable from the sequence and general HAT/GNAT mechanism knowledge."
  },
  "case_id": "active_site_0037",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C10",
      "H3",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A7U2QYM2 (Histone acetyltransferase gcnE, EC 2.3.1.48) annotates position 139 as 'Active site: Proton donor/acceptor' with experimental evidence (ECO:0000269, PubMed:39601562). The reference explicitly mentions 'MUTAGENESIS OF GLU-139', confirming Glu-139 as the catalytic residue. The sequence at position 139 is indeed E (Glutamic acid), verified by counting the provided 402-residue sequence. The expected answer B matches the annotated active site."
  },
  "important_caveats": [
    "The UniProt annotation at position 139 carries experimental evidence (ECO:0000269) from a 2025 MBio paper, making it well-supported rather than purely computational.",
    "The protein is annotated as both a histone acetyltransferase (EC 2.3.1.48) and a benzoyltransferase (EC 2.3.1.-); the catalytic Glu-139 role as proton donor/acceptor applies to both activities.",
    "The model is not given the protein name or organism; recognition of the GNAT/HAT fold must rely on sequence features or general knowledge, but the residue-identity elimination strategy (checking what amino acid is actually at each position) does not require fold recognition."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, C, and D are clearly eliminable: D references a nonexistent position, A and C assign impossible roles to Ile and Pro respectively. Only B (Glu-139 as proton donor/acceptor) is consistent with both the residue identity and HAT catalytic mechanism."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0037",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A7U2QYM2 (Histone acetyltransferase gcnE, EC 2.3.1.48) annotates position 139 as 'Active site: Proton donor/acceptor' with experimental evidence (ECO:0000269, PubMed:39601562). The reference explicitly mentions 'MUTAGENESIS OF GLU-139', confirming Glu-139 as the catalytic residue. The sequence at position 139 is indeed E (Glutamic acid), verified by counting the provided 402-residue sequence. The expected answer B matches the annotated active site.",
    "evidence_ids": ["C5", "C10", "H3", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "A knowledgeable model can eliminate options through multiple independent lines of transferable reasoning: (1) Position 4094 is impossible in a 402-residue protein — immediate elimination of D. (2) Counting the sequence reveals position 331 is Isoleucine (I), which cannot function as a 'proton acceptor' — eliminates A. (3) Position 131 is Proline (P), which cannot serve as a 'charge relay' residue — eliminates C. (4) Position 139 is Glutamic acid (E), which is the canonical catalytic proton donor/acceptor in GCN5-related N-acetyltransferase (GNAT) family histone acetyltransferases. The GNAT fold's conserved Glu in the 'PxxxQ' or 'FAE' region activates the lysine ε-amino group for nucleophilic attack on acetyl-CoA. The sequence context around 139 ('PFNSRRFAEI') is consistent with the GNAT catalytic region. This family-level mechanistic knowledge (HATs use a conserved Glu as proton shuttle) combined with residue-identity checks on the provided sequence meaningfully distinguishes B from the other options.",
    "missing_item_specific_fact": "",
    "reason": "The answer is reachable through: (a) simple arithmetic eliminating D (4094 > 402), (b) residue identity checks at positions 331 (Ile) and 131 (Pro) that are incompatible with the stated catalytic roles, and (c) family-level knowledge that GCN5-related HATs employ a conserved Glutamate as the catalytic proton donor/acceptor, which matches position 139 (E). No fact specific to this exact protein's experimental record is needed beyond what is derivable from the sequence and general HAT/GNAT mechanism knowledge."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, C, and D are clearly eliminable: D references a nonexistent position, A and C assign impossible roles to Ile and Pro respectively. Only B (Glu-139 as proton donor/acceptor) is consistent with both the residue identity and HAT catalytic mechanism."
  },
  "important_caveats": [
    "The UniProt annotation at position 139 carries experimental evidence (ECO:0000269) from a 2025 MBio paper, making it well-supported rather than purely computational.",
    "The protein is annotated as both a histone acetyltransferase (EC 2.3.1.48) and a benzoyltransferase (EC 2.3.1.-); the catalytic Glu-139 role as proton donor/acceptor applies to both activities.",
    "The model is not given the protein name or organism; recognition of the GNAT/HAT fold must rely on sequence features or general knowledge, but the residue-identity elimination strategy (checking what amino acid is actually at each position) does not require fold recognition."
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
  "benchmark_sequence_length": 402,
  "benchmark_sequence_sha256": "98f104b9c1052647fe3ad81fec046783468f372eba17bee1bf0a42e9d10f7d90",
  "current_entry_audit": {
    "entryVersion": 22,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2021-06-02",
    "sequenceVersion": 1
  },
  "current_record_sha256": "62832be697e21c858f10966f2857a43e5cbc83ed896c702c9eaf6b22d957a2f7",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 402,
  "current_source_sequence_sha256": "98f104b9c1052647fe3ad81fec046783468f372eba17bee1bf0a42e9d10f7d90",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 21,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A7U2QYM2",
  "selected_historical_entry_version": 21,
  "selected_historical_record_sha256": "36f550ae7bc08c06f607864032c4242543bb45af90f57f1b6319f8ebe893703c",
  "selected_historical_source_sequence_length": 402,
  "selected_historical_source_sequence_sha256": "98f104b9c1052647fe3ad81fec046783468f372eba17bee1bf0a42e9d10f7d90",
  "selected_historical_version": {
    "accession": "A0A7U2QYM2",
    "database": "Swiss-Prot",
    "entryVersion": 21,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "GCNE_ASPFN",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7U2QYM2.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A7U2QYM2\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:24:51.100326+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "62832be697e21c858f10966f2857a43e5cbc83ed896c702c9eaf6b22d957a2f7",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7U2QYM2.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7U2QYM2.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":22,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2021-06-02\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:24:51.100326+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "62832be697e21c858f10966f2857a43e5cbc83ed896c702c9eaf6b22d957a2f7",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7U2QYM2.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7U2QYM2.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Eurotiomycetes\",\"Eurotiomycetidae\",\"Eurotiales\",\"Aspergillaceae\",\"Aspergillus\",\"Circumdati\"],\"scientificName\":\"Aspergillus flavus (strain ATCC 200026 / FGSC A1120 / IAM 13836 / NRRL 3357 / JCM 12722 / SRRC 167)\",\"taxonId\":332952}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:24:51.100326+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "62832be697e21c858f10966f2857a43e5cbc83ed896c702c9eaf6b22d957a2f7",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7U2QYM2.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7U2QYM2.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39601562\",\"source\":\"PubMed\"}],\"value\":\"2.3.1.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39601562\",\"source\":\"PubMed\"}],\"value\":\"Benzoyltransferase gcnE\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39601562\",\"source\":\"PubMed\"}],\"value\":\"2.3.1.48\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q03330\",\"source\":\"UniProtKB\"}],\"value\":\"Histone acetyltransferase gcnE\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:24:51.100326+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "62832be697e21c858f10966f2857a43e5cbc83ed896c702c9eaf6b22d957a2f7",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7U2QYM2.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7U2QYM2.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Proton donor/acceptor\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39601562\",\"source\":\"PubMed\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":139},\"start\":{\"modifier\":\"EXACT\",\"value\":139}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/6",
  "retrieved_utc": "2026-11-01T06:24:51.100326+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "62832be697e21c858f10966f2857a43e5cbc83ed896c702c9eaf6b22d957a2f7",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7U2QYM2.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7U2QYM2.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q92830\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:57288\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:57288\",\"name\":\"acetyl-CoA\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":145},\"start\":{\"modifier\":\"EXACT\",\"value\":143}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/7",
  "retrieved_utc": "2026-11-01T06:24:51.100326+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "62832be697e21c858f10966f2857a43e5cbc83ed896c702c9eaf6b22d957a2f7",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7U2QYM2.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7U2QYM2.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q92830\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:57288\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:57288\",\"name\":\"acetyl-CoA\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":156},\"start\":{\"modifier\":\"EXACT\",\"value\":150}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/8",
  "retrieved_utc": "2026-11-01T06:24:51.100326+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "62832be697e21c858f10966f2857a43e5cbc83ed896c702c9eaf6b22d957a2f7",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7U2QYM2.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7U2QYM2.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q92830\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:57288\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:57288\",\"name\":\"acetyl-CoA\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":185},\"start\":{\"modifier\":\"EXACT\",\"value\":182}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/9",
  "retrieved_utc": "2026-11-01T06:24:51.100326+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "62832be697e21c858f10966f2857a43e5cbc83ed896c702c9eaf6b22d957a2f7",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7U2QYM2.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7U2QYM2.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"Important for catalytic activity\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q03330\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":139},\"start\":{\"modifier\":\"EXACT\",\"value\":139}},\"type\":\"Site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/10",
  "retrieved_utc": "2026-11-01T06:24:51.100326+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "62832be697e21c858f10966f2857a43e5cbc83ed896c702c9eaf6b22d957a2f7",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7U2QYM2.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7U2QYM2.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"citation\":{\"authors\":[\"Chen X.\",\"Wu L.\",\"Zhang Y.\",\"Wang S.\",\"Wang S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39601562\"},{\"database\":\"DOI\",\"id\":\"10.1128/mbio.02665-24\"}],\"citationType\":\"journal article\",\"firstPage\":\"e0266524\",\"id\":\"39601562\",\"journal\":\"MBio\",\"lastPage\":\"e0266524\",\"publicationDate\":\"2025\",\"title\":\"Importance of benzoyltransferase GcnE and lysine benzoylation of alcohol dehydrogenase AdhB in pathogenesis and aflatoxin production in Aspergillus flavus.\",\"volume\":\"16\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"DISRUPTION PHENOTYPE\",\"CATALYTIC ACTIVITY\",\"DOMAIN\",\"ACTIVE SITE\",\"MUTAGENESIS OF GLU-139\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-01T06:24:51.100326+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "62832be697e21c858f10966f2857a43e5cbc83ed896c702c9eaf6b22d957a2f7",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7U2QYM2.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7U2QYM2?format=txt&versions=21)

```json
{
  "entry_version": 21,
  "evidence_id": "H1",
  "excerpt": "ID   GCNE_ASPFN              Reviewed;         402 AA.\nAC   A0A7U2QYM2;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   02-JUN-2021, sequence version 1.\nDT   28-JAN-2026, entry version 21.\nDE   RecName: Full=Histone acetyltransferase gcnE {ECO:0000250|UniProtKB:Q03330};\nDE            EC=2.3.1.48 {ECO:0000269|PubMed:39601562};\nDE   AltName: Full=Benzoyltransferase gcnE {ECO:0000303|PubMed:39601562};\nDE            EC=2.3.1.- {ECO:0000269|PubMed:39601562};\nGN   Name=gcnE {ECO:0000303|PubMed:39601562}; ORFNames=F9C07_11133;\nOS   Aspergillus flavus (strain ATCC 200026 / FGSC A1120 / IAM 13836 / NRRL 3357\nOS   / JCM 12722 / SRRC 167).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;\nOC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Aspergillus;\nOC   Aspergillus subgen. Circumdati.\nOX   NCBI_TaxID=332952;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:33.661793+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "36f550ae7bc08c06f607864032c4242543bb45af90f57f1b6319f8ebe893703c",
  "url": "https://rest.uniprot.org/unisave/A0A7U2QYM2?format=txt&versions=21"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7U2QYM2?format=txt&versions=21)

```json
{
  "entry_version": 21,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION, DISRUPTION PHENOTYPE, CATALYTIC ACTIVITY, DOMAIN, ACTIVE SITE,\nRP   AND MUTAGENESIS OF GLU-139.\nRX   PubMed=39601562; DOI=10.1128/mbio.02665-24;\nRA   Chen X., Wu L., Zhang Y., Wang S., Wang S.;\nRT   \"Importance of benzoyltransferase GcnE and lysine benzoylation of alcohol\nRT   dehydrogenase AdhB in pathogenesis and aflatoxin production in Aspergillus\nRT   flavus.\";\nRL   MBio 16:e0266524-e0266524(2025).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:33.661793+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 27-35",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "36f550ae7bc08c06f607864032c4242543bb45af90f57f1b6319f8ebe893703c",
  "url": "https://rest.uniprot.org/unisave/A0A7U2QYM2?format=txt&versions=21"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7U2QYM2?format=txt&versions=21)

```json
{
  "entry_version": 21,
  "evidence_id": "H3",
  "excerpt": "FT   ACT_SITE        139\nFT                   /note=\"Proton donor/acceptor\"\nFT                   /evidence=\"ECO:0000269|PubMed:39601562\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:33.661793+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 141-143",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "36f550ae7bc08c06f607864032c4242543bb45af90f57f1b6319f8ebe893703c",
  "url": "https://rest.uniprot.org/unisave/A0A7U2QYM2?format=txt&versions=21"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7U2QYM2?format=txt&versions=21)

```json
{
  "entry_version": 21,
  "evidence_id": "H4",
  "excerpt": "FT   BINDING         143..145\nFT                   /ligand=\"acetyl-CoA\"\nFT                   /ligand_id=\"ChEBI:CHEBI:57288\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q92830\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:33.661793+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 144-147",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "36f550ae7bc08c06f607864032c4242543bb45af90f57f1b6319f8ebe893703c",
  "url": "https://rest.uniprot.org/unisave/A0A7U2QYM2?format=txt&versions=21"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7U2QYM2?format=txt&versions=21)

```json
{
  "entry_version": 21,
  "evidence_id": "H5",
  "excerpt": "FT   BINDING         150..156\nFT                   /ligand=\"acetyl-CoA\"\nFT                   /ligand_id=\"ChEBI:CHEBI:57288\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q92830\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:33.661793+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 148-151",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "36f550ae7bc08c06f607864032c4242543bb45af90f57f1b6319f8ebe893703c",
  "url": "https://rest.uniprot.org/unisave/A0A7U2QYM2?format=txt&versions=21"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7U2QYM2?format=txt&versions=21)

```json
{
  "entry_version": 21,
  "evidence_id": "H6",
  "excerpt": "FT   BINDING         182..185\nFT                   /ligand=\"acetyl-CoA\"\nFT                   /ligand_id=\"ChEBI:CHEBI:57288\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q92830\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:33.661793+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 152-155",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "36f550ae7bc08c06f607864032c4242543bb45af90f57f1b6319f8ebe893703c",
  "url": "https://rest.uniprot.org/unisave/A0A7U2QYM2?format=txt&versions=21"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7U2QYM2?format=txt&versions=21)

```json
{
  "entry_version": 21,
  "evidence_id": "H7",
  "excerpt": "FT   SITE            139\nFT                   /note=\"Important for catalytic activity\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q03330\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:33.661793+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 156-158",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "36f550ae7bc08c06f607864032c4242543bb45af90f57f1b6319f8ebe893703c",
  "url": "https://rest.uniprot.org/unisave/A0A7U2QYM2?format=txt&versions=21"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 37. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
