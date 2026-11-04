# active_site_0070

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/active_site_0070.txt)

**Task:** `active_site`  
**Expected answer:** **B** — Position 186 (Proton donor)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MSSVLPTPVLPTPGRNINRGHFPDDFIFGAGTSSYQIEGAAREGGRGPSIWDTFTHTHPELIQDGSNGDTAINSYNLYKEDIKIVKLMGLDAYRFSISWPRILPGGSINAGINQEGIKYYNNLIDELLANDIVPYVTLFHWDVPQALQDQYDGFLSDKIVDDFRDFAELCFWEFGDRVKNWITINEPQSYSDFFGVAYDTPPKAHALKASRLLVPTTVARPSKPVRVFASTADPGTTTADQVYKVGHNLLLAHAAAIQVYRDKFQNTQEGTFGMALVTQWMKPLNENNPADVEAASRAFDFKFGWFMQPLITGEYPKSMRQLLGPRLREFTPDQKKLLIGSYDYVGVNYYTATYVSSAQPPHDKKKAVFHTDGNFYTTDSKDGVLIGPLAGPAWLNIVPEGIYHVLHDIKENYEDPVIYITENGVYEVNDTAKTLSEARVDTTRLHYLQDHLSKVLEARHQGVRVQGYLVWSLMDNWELRAGYTSRFGLIHVDYYNNFARYPKDSAIWFRNAFHKRLRIHVNKARPQEDDGAFDTPRKRLRKY

[Multiple Choices]
A. Position 116 (Charge relay)
B. Position 186 (Proton donor)
C. Position 341 (For beta-ketoacyl synthase activity)
D. Position 156 (Acyl-thioester intermediate)
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

> The sequence-matched UniProt record annotates position 186 as the proton donor, supporting choice B. This annotation is transferred by similarity from another UniProt entry (ECO:0000250), rather than shown here as a direct experiment on this exact protein.

Citations as saved: [C5](#evidence-c5), [C4](#evidence-c4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains motifs characteristic of glycoside hydrolase family 1 beta-glucosidases, including the conserved NEP-region catalytic glutamate around position 186. In this enzyme family, a conserved glutamate serves as the proton donor, making B meaningfully distinguishable from the unrelated charge-relay, acyl-thioester, and beta-ketoacyl-synthase alternatives.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family recognition and the conserved catalytic motif provide a transferable basis for identifying the proton-donor option without needing the exact protein's recorded annotation. The inference is strong but does not independently establish the experimental role of this residue.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the offered choices, only B describes the conserved proton-donor role expected for the family; the other listed roles do not fit this sequence's enzyme family.


### Important caveats

- The supplied evidence supports the key through a homology-based annotation, not direct experimental evidence for residue 186 in this exact protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains motifs characteristic of glycoside hydrolase family 1 beta-glucosidases, including the conserved NEP-region catalytic glutamate around position 186. In this enzyme family, a conserved glutamate serves as the proton donor, making B meaningfully distinguishable from the unrelated charge-relay, acyl-thioester, and beta-ketoacyl-synthase alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family recognition and the conserved catalytic motif provide a transferable basis for identifying the proton-donor option without needing the exact protein's recorded annotation. The inference is strong but does not independently establish the experimental role of this residue."
  },
  "case_id": "active_site_0070",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates position 186 as the proton donor, supporting choice B. This annotation is transferred by similarity from another UniProt entry (ECO:0000250), rather than shown here as a direct experiment on this exact protein."
  },
  "important_caveats": [
    "The supplied evidence supports the key through a homology-based annotation, not direct experimental evidence for residue 186 in this exact protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, only B describes the conserved proton-donor role expected for the family; the other listed roles do not fit this sequence's enzyme family."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0070",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates position 186 as the proton donor, supporting choice B. This annotation is transferred by similarity from another UniProt entry (ECO:0000250), rather than shown here as a direct experiment on this exact protein.",
    "evidence_ids": ["C5", "C4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains motifs characteristic of glycoside hydrolase family 1 beta-glucosidases, including the conserved NEP-region catalytic glutamate around position 186. In this enzyme family, a conserved glutamate serves as the proton donor, making B meaningfully distinguishable from the unrelated charge-relay, acyl-thioester, and beta-ketoacyl-synthase alternatives.",
    "missing_item_specific_fact": "",
    "reason": "Family recognition and the conserved catalytic motif provide a transferable basis for identifying the proton-donor option without needing the exact protein's recorded annotation. The inference is strong but does not independently establish the experimental role of this residue."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, only B describes the conserved proton-donor role expected for the family; the other listed roles do not fit this sequence's enzyme family."
  },
  "important_caveats": [
    "The supplied evidence supports the key through a homology-based annotation, not direct experimental evidence for residue 186 in this exact protein."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation (evidence C5/H3) records position 186 as an Active site with description 'Proton donor'. The residue at position 186 in the supplied sequence is Glutamic acid (E), embedded in the N185-E186-P187 (NEP) motif, which is the canonical proton-donor triad of glycoside hydrolase family 1 (GH1) beta-glucosidases. The annotation evidence code is ECO:0000250 (inferred by similarity to Q7XSK0), so it is a computational transfer rather than direct experimental data, but the sequence context is fully consistent with the assigned role. The answer is supported by the database annotation and the sequence chemistry.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence around position 186 reads ...W-I-T-I-N(185)-E(186)-P(187)-Q-S-Y..., containing the NEP (Asn-Glu-Pro) motif. The NEP motif is the single most recognized proton-donor signature of GH1 glycosidases (e.g., beta-glucosidases, beta-galactosidases, beta-mannosidases), learned from dozens of structurally and mechanistically characterized family members. A knowledgeable model can recognize this motif and assign E186 as the proton donor. The distractors are eliminable by transferable knowledge: (C) 'beta-ketoacyl synthase activity' describes a fatty-acid-synthase condensation mechanism, entirely incompatible with a glycosidase; (D) 'Acyl-thioester intermediate' is the hallmark of serine proteases or acyltransferases, not glycosidases; (A) 'Charge relay' at position 116, which is Glycine, is chemically nonsensical because Gly has no side-chain functional group to participate in charge relay. Thus, family-level pattern recognition (NEP motif) plus elimination of mechanistically incompatible choices distinguishes B without needing the specific UniProt record for this protein.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The NEP motif at positions 185-187 is a well-established, transferable family-level feature of GH1 glycosidases. Recognizing this motif from the raw sequence and applying general knowledge of glycosidase catalytic mechanisms allows a model to identify E186 as the proton donor. The three distractors are eliminable because they invoke enzyme classes or chemical mechanisms (fatty-acid synthase, serine-protease thioester, Gly charge relay) that are incompatible with the sequence context and glycosidase biochemistry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Option B is uniquely consistent with the NEP proton-donor motif present in the sequence. Options C and D invoke mechanisms belonging to entirely different enzyme classes (fatty-acid synthase, serine protease), and option A assigns a charge-relay role to Glycine, which lacks a functional side chain. No ambiguity among the offered choices.


### Important caveats

- The UniProt active-site annotation is by similarity (ECO:0000250, from Q7XSK0), not direct experimental mutagenesis or crystallographic proof for this specific protein.
- The nucleophile at position 422 (also E, in the GH1 'ITENGE' context) is annotated but not offered as a choice, so it does not create ambiguity.
- The reviewer-only evidence confirms the sequence match (SHA-256 identical) and that the annotation has been stable across entry versions 51 and 53.
- The model is not told the protein is a beta-glucosidase or GH1 family member; identification must come from sequence pattern recognition and elimination of mechanistically incompatible distractors.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence around position 186 reads ...W-I-T-I-N(185)-E(186)-P(187)-Q-S-Y..., containing the NEP (Asn-Glu-Pro) motif. The NEP motif is the single most recognized proton-donor signature of GH1 glycosidases (e.g., beta-glucosidases, beta-galactosidases, beta-mannosidases), learned from dozens of structurally and mechanistically characterized family members. A knowledgeable model can recognize this motif and assign E186 as the proton donor. The distractors are eliminable by transferable knowledge: (C) 'beta-ketoacyl synthase activity' describes a fatty-acid-synthase condensation mechanism, entirely incompatible with a glycosidase; (D) 'Acyl-thioester intermediate' is the hallmark of serine proteases or acyltransferases, not glycosidases; (A) 'Charge relay' at position 116, which is Glycine, is chemically nonsensical because Gly has no side-chain functional group to participate in charge relay. Thus, family-level pattern recognition (NEP motif) plus elimination of mechanistically incompatible choices distinguishes B without needing the specific UniProt record for this protein.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The NEP motif at positions 185-187 is a well-established, transferable family-level feature of GH1 glycosidases. Recognizing this motif from the raw sequence and applying general knowledge of glycosidase catalytic mechanisms allows a model to identify E186 as the proton donor. The three distractors are eliminable because they invoke enzyme classes or chemical mechanisms (fatty-acid synthase, serine-protease thioester, Gly charge relay) that are incompatible with the sequence context and glycosidase biochemistry."
  },
  "case_id": "active_site_0070",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation (evidence C5/H3) records position 186 as an Active site with description 'Proton donor'. The residue at position 186 in the supplied sequence is Glutamic acid (E), embedded in the N185-E186-P187 (NEP) motif, which is the canonical proton-donor triad of glycoside hydrolase family 1 (GH1) beta-glucosidases. The annotation evidence code is ECO:0000250 (inferred by similarity to Q7XSK0), so it is a computational transfer rather than direct experimental data, but the sequence context is fully consistent with the assigned role. The answer is supported by the database annotation and the sequence chemistry."
  },
  "important_caveats": [
    "The UniProt active-site annotation is by similarity (ECO:0000250, from Q7XSK0), not direct experimental mutagenesis or crystallographic proof for this specific protein.",
    "The nucleophile at position 422 (also E, in the GH1 'ITENGE' context) is annotated but not offered as a choice, so it does not create ambiguity.",
    "The reviewer-only evidence confirms the sequence match (SHA-256 identical) and that the annotation has been stable across entry versions 51 and 53.",
    "The model is not told the protein is a beta-glucosidase or GH1 family member; identification must come from sequence pattern recognition and elimination of mechanistically incompatible distractors."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option B is uniquely consistent with the NEP proton-donor motif present in the sequence. Options C and D invoke mechanisms belonging to entirely different enzyme classes (fatty-acid synthase, serine protease), and option A assigns a charge-relay role to Glycine, which lacks a functional side chain. No ambiguity among the offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0070",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation (evidence C5/H3) records position 186 as an Active site with description 'Proton donor'. The residue at position 186 in the supplied sequence is Glutamic acid (E), embedded in the N185-E186-P187 (NEP) motif, which is the canonical proton-donor triad of glycoside hydrolase family 1 (GH1) beta-glucosidases. The annotation evidence code is ECO:0000250 (inferred by similarity to Q7XSK0), so it is a computational transfer rather than direct experimental data, but the sequence context is fully consistent with the assigned role. The answer is supported by the database annotation and the sequence chemistry.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence around position 186 reads ...W-I-T-I-N(185)-E(186)-P(187)-Q-S-Y..., containing the NEP (Asn-Glu-Pro) motif. The NEP motif is the single most recognized proton-donor signature of GH1 glycosidases (e.g., beta-glucosidases, beta-galactosidases, beta-mannosidases), learned from dozens of structurally and mechanistically characterized family members. A knowledgeable model can recognize this motif and assign E186 as the proton donor. The distractors are eliminable by transferable knowledge: (C) 'beta-ketoacyl synthase activity' describes a fatty-acid-synthase condensation mechanism, entirely incompatible with a glycosidase; (D) 'Acyl-thioester intermediate' is the hallmark of serine proteases or acyltransferases, not glycosidases; (A) 'Charge relay' at position 116, which is Glycine, is chemically nonsensical because Gly has no side-chain functional group to participate in charge relay. Thus, family-level pattern recognition (NEP motif) plus elimination of mechanistically incompatible choices distinguishes B without needing the specific UniProt record for this protein.",
    "missing_item_specific_fact": "",
    "reason": "The NEP motif at positions 185-187 is a well-established, transferable family-level feature of GH1 glycosidases. Recognizing this motif from the raw sequence and applying general knowledge of glycosidase catalytic mechanisms allows a model to identify E186 as the proton donor. The three distractors are eliminable because they invoke enzyme classes or chemical mechanisms (fatty-acid synthase, serine-protease thioester, Gly charge relay) that are incompatible with the sequence context and glycosidase biochemistry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option B is uniquely consistent with the NEP proton-donor motif present in the sequence. Options C and D invoke mechanisms belonging to entirely different enzyme classes (fatty-acid synthase, serine protease), and option A assigns a charge-relay role to Glycine, which lacks a functional side chain. No ambiguity among the offered choices."
  },
  "important_caveats": [
    "The UniProt active-site annotation is by similarity (ECO:0000250, from Q7XSK0), not direct experimental mutagenesis or crystallographic proof for this specific protein.",
    "The nucleophile at position 422 (also E, in the GH1 'ITENGE' context) is annotated but not offered as a choice, so it does not create ambiguity.",
    "The reviewer-only evidence confirms the sequence match (SHA-256 identical) and that the annotation has been stable across entry versions 51 and 53.",
    "The model is not told the protein is a beta-glucosidase or GH1 family member; identification must come from sequence pattern recognition and elimination of mechanistically incompatible distractors."
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
  "benchmark_sequence_length": 543,
  "benchmark_sequence_sha256": "8141756119b0e8092bcefac767f6861053ab97e59d37a7ab570496a465d1b713",
  "current_entry_audit": {
    "entryVersion": 53,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2009-02-10",
    "sequenceVersion": 1
  },
  "current_record_sha256": "9ce8751c9b282900ae1cfa7efc22995f02ca697466197dd0e4f4ff630319c00a",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 543,
  "current_source_sequence_sha256": "8141756119b0e8092bcefac767f6861053ab97e59d37a7ab570496a465d1b713",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 51,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "B6ZKM5",
  "selected_historical_entry_version": 51,
  "selected_historical_record_sha256": "d374cbcc14c195ce5c51c5fdab5300bf13d9a704c2f014bd237f3c23f917e6a7",
  "selected_historical_source_sequence_length": 543,
  "selected_historical_source_sequence_sha256": "8141756119b0e8092bcefac767f6861053ab97e59d37a7ab570496a465d1b713",
  "selected_historical_version": {
    "accession": "B6ZKM5",
    "database": "Swiss-Prot",
    "entryVersion": 51,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "GLU3_CARIP",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B6ZKM5.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"B6ZKM5\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:27:24.045505+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9ce8751c9b282900ae1cfa7efc22995f02ca697466197dd0e4f4ff630319c00a",
  "url": "https://rest.uniprot.org/uniprotkb/B6ZKM5.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B6ZKM5.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":53,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2009-02-10\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:27:24.045505+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9ce8751c9b282900ae1cfa7efc22995f02ca697466197dd0e4f4ff630319c00a",
  "url": "https://rest.uniprot.org/uniprotkb/B6ZKM5.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B6ZKM5.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Ipecac\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"asterids\",\"lamiids\",\"Gentianales\",\"Rubiaceae\",\"Rubioideae\",\"Palicoureeae\",\"Carapichea\"],\"scientificName\":\"Carapichea ipecacuanha\",\"synonyms\":[\"Callicocca ipecacuanha\"],\"taxonId\":77880}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:27:24.045505+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9ce8751c9b282900ae1cfa7efc22995f02ca697466197dd0e4f4ff630319c00a",
  "url": "https://rest.uniprot.org/uniprotkb/B6ZKM5.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B6ZKM5.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18927081\",\"source\":\"PubMed\"}],\"value\":\"3.2.1.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"18927081\",\"source\":\"PubMed\"}],\"value\":\"Ipecac alkaloid beta-glucosidase 3\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"18927081\",\"source\":\"PubMed\"}],\"value\":\"IpeGLU3\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:27:24.045505+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9ce8751c9b282900ae1cfa7efc22995f02ca697466197dd0e4f4ff630319c00a",
  "url": "https://rest.uniprot.org/uniprotkb/B6ZKM5.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B6ZKM5.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Proton donor\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q7XSK0\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":186},\"start\":{\"modifier\":\"EXACT\",\"value\":186}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-02T04:27:24.045505+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9ce8751c9b282900ae1cfa7efc22995f02ca697466197dd0e4f4ff630319c00a",
  "url": "https://rest.uniprot.org/uniprotkb/B6ZKM5.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B6ZKM5.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"Nucleophile\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q7XSK0\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":422},\"start\":{\"modifier\":\"EXACT\",\"value\":422}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-02T04:27:24.045505+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9ce8751c9b282900ae1cfa7efc22995f02ca697466197dd0e4f4ff630319c00a",
  "url": "https://rest.uniprot.org/uniprotkb/B6ZKM5.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B6ZKM5.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9SPP9\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:22798\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:22798\",\"name\":\"a beta-D-glucoside\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":36},\"start\":{\"modifier\":\"EXACT\",\"value\":36}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-02T04:27:24.045505+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9ce8751c9b282900ae1cfa7efc22995f02ca697466197dd0e4f4ff630319c00a",
  "url": "https://rest.uniprot.org/uniprotkb/B6ZKM5.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B6ZKM5.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9SPP9\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:22798\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:22798\",\"name\":\"a beta-D-glucoside\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":140},\"start\":{\"modifier\":\"EXACT\",\"value\":140}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-02T04:27:24.045505+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9ce8751c9b282900ae1cfa7efc22995f02ca697466197dd0e4f4ff630319c00a",
  "url": "https://rest.uniprot.org/uniprotkb/B6ZKM5.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B6ZKM5.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9SPP9\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:22798\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:22798\",\"name\":\"a beta-D-glucoside\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":186},\"start\":{\"modifier\":\"EXACT\",\"value\":185}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
  "retrieved_utc": "2026-11-02T04:27:24.045505+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9ce8751c9b282900ae1cfa7efc22995f02ca697466197dd0e4f4ff630319c00a",
  "url": "https://rest.uniprot.org/uniprotkb/B6ZKM5.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B6ZKM5.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8L7J2\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:22798\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:22798\",\"name\":\"a beta-D-glucoside\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":350},\"start\":{\"modifier\":\"EXACT\",\"value\":350}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/6",
  "retrieved_utc": "2026-11-02T04:27:24.045505+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9ce8751c9b282900ae1cfa7efc22995f02ca697466197dd0e4f4ff630319c00a",
  "url": "https://rest.uniprot.org/uniprotkb/B6ZKM5.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B6ZKM5.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9SPP9\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:22798\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:22798\",\"name\":\"a beta-D-glucoside\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":422},\"start\":{\"modifier\":\"EXACT\",\"value\":422}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/7",
  "retrieved_utc": "2026-11-02T04:27:24.045505+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9ce8751c9b282900ae1cfa7efc22995f02ca697466197dd0e4f4ff630319c00a",
  "url": "https://rest.uniprot.org/uniprotkb/B6ZKM5.json"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B6ZKM5.json)

```json
{
  "evidence_id": "C12",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9SPP9\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:22798\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:22798\",\"name\":\"a beta-D-glucoside\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":471},\"start\":{\"modifier\":\"EXACT\",\"value\":471}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/8",
  "retrieved_utc": "2026-11-02T04:27:24.045505+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9ce8751c9b282900ae1cfa7efc22995f02ca697466197dd0e4f4ff630319c00a",
  "url": "https://rest.uniprot.org/uniprotkb/B6ZKM5.json"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B6ZKM5.json)

```json
{
  "evidence_id": "C13",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q1XH05\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:22798\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:22798\",\"name\":\"a beta-D-glucoside\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":487},\"start\":{\"modifier\":\"EXACT\",\"value\":487}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/9",
  "retrieved_utc": "2026-11-02T04:27:24.045505+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9ce8751c9b282900ae1cfa7efc22995f02ca697466197dd0e4f4ff630319c00a",
  "url": "https://rest.uniprot.org/uniprotkb/B6ZKM5.json"
}
```

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B6ZKM5.json)

```json
{
  "evidence_id": "C14",
  "excerpt": "{\"description\":\"Controls the gate shape and acceptance of substrates\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9SPP9\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":394},\"start\":{\"modifier\":\"EXACT\",\"value\":394}},\"type\":\"Site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/10",
  "retrieved_utc": "2026-11-02T04:27:24.045505+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9ce8751c9b282900ae1cfa7efc22995f02ca697466197dd0e4f4ff630319c00a",
  "url": "https://rest.uniprot.org/uniprotkb/B6ZKM5.json"
}
```

### Evidence C15

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B6ZKM5.json)

```json
{
  "evidence_id": "C15",
  "excerpt": "{\"citation\":{\"authors\":[\"Nomura T.\",\"Quesada A.L.\",\"Kutchan T.M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"18927081\"},{\"database\":\"DOI\",\"id\":\"10.1074/jbc.m806953200\"}],\"citationType\":\"journal article\",\"firstPage\":\"34650\",\"id\":\"18927081\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"34659\",\"publicationDate\":\"2008\",\"title\":\"The new beta-D-glucosidase in terpenoid-isoquinoline alkaloid biosynthesis in Psychotria ipecacuanha.\",\"volume\":\"283\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"BAH02546.1\",\"source\":\"EMBL\"},{\"evidenceCode\":\"ECO:0000312\",\"id\":\"BAH02553.1\",\"source\":\"EMBL\"}],\"referenceComments\":[{\"type\":\"TISSUE\",\"value\":\"Root\"},{\"type\":\"TISSUE\",\"value\":\"Shoot\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:27:24.045505+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9ce8751c9b282900ae1cfa7efc22995f02ca697466197dd0e4f4ff630319c00a",
  "url": "https://rest.uniprot.org/uniprotkb/B6ZKM5.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B6ZKM5?format=txt&versions=51)

```json
{
  "entry_version": 51,
  "evidence_id": "H1",
  "excerpt": "ID   GLU3_CARIP              Reviewed;         543 AA.\nAC   B6ZKM5;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   10-FEB-2009, sequence version 1.\nDT   28-JAN-2026, entry version 51.\nDE   RecName: Full=Ipecac alkaloid beta-glucosidase 3 {ECO:0000303|PubMed:18927081};\nDE            Short=IpeGLU3 {ECO:0000303|PubMed:18927081};\nDE            EC=3.2.1.- {ECO:0000269|PubMed:18927081};\nGN   Name=GLU3 {ECO:0000303|PubMed:18927081};\nOS   Carapichea ipecacuanha (Ipecac) (Callicocca ipecacuanha).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   asterids; lamiids; Gentianales; Rubiaceae; Rubioideae; Palicoureeae;\nOC   Carapichea.\nOX   NCBI_TaxID=77880;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:26.233250+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d374cbcc14c195ce5c51c5fdab5300bf13d9a704c2f014bd237f3c23f917e6a7",
  "url": "https://rest.uniprot.org/unisave/B6ZKM5?format=txt&versions=51"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B6ZKM5?format=txt&versions=51)

```json
{
  "entry_version": 51,
  "evidence_id": "H2",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:BAH02546.1, ECO:0000312|EMBL:BAH02553.1}\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY, AND PATHWAY.\nRC   TISSUE=Root, and Shoot;\nRX   PubMed=18927081; DOI=10.1074/jbc.m806953200;\nRA   Nomura T., Quesada A.L., Kutchan T.M.;\nRT   \"The new beta-D-glucosidase in terpenoid-isoquinoline alkaloid biosynthesis\nRT   in Psychotria ipecacuanha.\";\nRL   J. Biol. Chem. 283:34650-34659(2008).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:26.233250+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 16-23",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d374cbcc14c195ce5c51c5fdab5300bf13d9a704c2f014bd237f3c23f917e6a7",
  "url": "https://rest.uniprot.org/unisave/B6ZKM5?format=txt&versions=51"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B6ZKM5?format=txt&versions=51)

```json
{
  "entry_version": 51,
  "evidence_id": "H3",
  "excerpt": "FT   ACT_SITE        186\nFT                   /note=\"Proton donor\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q7XSK0\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:26.233250+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 73-75",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d374cbcc14c195ce5c51c5fdab5300bf13d9a704c2f014bd237f3c23f917e6a7",
  "url": "https://rest.uniprot.org/unisave/B6ZKM5?format=txt&versions=51"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B6ZKM5?format=txt&versions=51)

```json
{
  "entry_version": 51,
  "evidence_id": "H4",
  "excerpt": "FT   ACT_SITE        422\nFT                   /note=\"Nucleophile\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q7XSK0\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:26.233250+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 76-78",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d374cbcc14c195ce5c51c5fdab5300bf13d9a704c2f014bd237f3c23f917e6a7",
  "url": "https://rest.uniprot.org/unisave/B6ZKM5?format=txt&versions=51"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B6ZKM5?format=txt&versions=51)

```json
{
  "entry_version": 51,
  "evidence_id": "H5",
  "excerpt": "FT   BINDING         36\nFT                   /ligand=\"a beta-D-glucoside\"\nFT                   /ligand_id=\"ChEBI:CHEBI:22798\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9SPP9\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:26.233250+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 79-82",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d374cbcc14c195ce5c51c5fdab5300bf13d9a704c2f014bd237f3c23f917e6a7",
  "url": "https://rest.uniprot.org/unisave/B6ZKM5?format=txt&versions=51"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B6ZKM5?format=txt&versions=51)

```json
{
  "entry_version": 51,
  "evidence_id": "H6",
  "excerpt": "FT   BINDING         140\nFT                   /ligand=\"a beta-D-glucoside\"\nFT                   /ligand_id=\"ChEBI:CHEBI:22798\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9SPP9\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:26.233250+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 83-86",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d374cbcc14c195ce5c51c5fdab5300bf13d9a704c2f014bd237f3c23f917e6a7",
  "url": "https://rest.uniprot.org/unisave/B6ZKM5?format=txt&versions=51"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B6ZKM5?format=txt&versions=51)

```json
{
  "entry_version": 51,
  "evidence_id": "H7",
  "excerpt": "FT   BINDING         185..186\nFT                   /ligand=\"a beta-D-glucoside\"\nFT                   /ligand_id=\"ChEBI:CHEBI:22798\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9SPP9\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:26.233250+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 87-90",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d374cbcc14c195ce5c51c5fdab5300bf13d9a704c2f014bd237f3c23f917e6a7",
  "url": "https://rest.uniprot.org/unisave/B6ZKM5?format=txt&versions=51"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B6ZKM5?format=txt&versions=51)

```json
{
  "entry_version": 51,
  "evidence_id": "H8",
  "excerpt": "FT   BINDING         350\nFT                   /ligand=\"a beta-D-glucoside\"\nFT                   /ligand_id=\"ChEBI:CHEBI:22798\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8L7J2\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:26.233250+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 91-94",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d374cbcc14c195ce5c51c5fdab5300bf13d9a704c2f014bd237f3c23f917e6a7",
  "url": "https://rest.uniprot.org/unisave/B6ZKM5?format=txt&versions=51"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B6ZKM5?format=txt&versions=51)

```json
{
  "entry_version": 51,
  "evidence_id": "H9",
  "excerpt": "FT   BINDING         422\nFT                   /ligand=\"a beta-D-glucoside\"\nFT                   /ligand_id=\"ChEBI:CHEBI:22798\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9SPP9\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:26.233250+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 95-98",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d374cbcc14c195ce5c51c5fdab5300bf13d9a704c2f014bd237f3c23f917e6a7",
  "url": "https://rest.uniprot.org/unisave/B6ZKM5?format=txt&versions=51"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B6ZKM5?format=txt&versions=51)

```json
{
  "entry_version": 51,
  "evidence_id": "H10",
  "excerpt": "FT   BINDING         471\nFT                   /ligand=\"a beta-D-glucoside\"\nFT                   /ligand_id=\"ChEBI:CHEBI:22798\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9SPP9\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:26.233250+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 99-102",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d374cbcc14c195ce5c51c5fdab5300bf13d9a704c2f014bd237f3c23f917e6a7",
  "url": "https://rest.uniprot.org/unisave/B6ZKM5?format=txt&versions=51"
}
```

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B6ZKM5?format=txt&versions=51)

```json
{
  "entry_version": 51,
  "evidence_id": "H11",
  "excerpt": "FT   BINDING         487\nFT                   /ligand=\"a beta-D-glucoside\"\nFT                   /ligand_id=\"ChEBI:CHEBI:22798\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q1XH05\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:26.233250+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 103-106",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d374cbcc14c195ce5c51c5fdab5300bf13d9a704c2f014bd237f3c23f917e6a7",
  "url": "https://rest.uniprot.org/unisave/B6ZKM5?format=txt&versions=51"
}
```

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B6ZKM5?format=txt&versions=51)

```json
{
  "entry_version": 51,
  "evidence_id": "H12",
  "excerpt": "FT   SITE            394\nFT                   /note=\"Controls the gate shape and acceptance of\nFT                   substrates\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9SPP9\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:26.233250+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 107-110",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d374cbcc14c195ce5c51c5fdab5300bf13d9a704c2f014bd237f3c23f917e6a7",
  "url": "https://rest.uniprot.org/unisave/B6ZKM5?format=txt&versions=51"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 70. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
