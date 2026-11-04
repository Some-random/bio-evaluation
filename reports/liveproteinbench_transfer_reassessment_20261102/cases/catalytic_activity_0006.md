# catalytic_activity_0006

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/catalytic_activity_0006.txt)

**Task:** `catalytic_activity`  
**Expected answer:** **B** — a CDP-1,2-diacyl-sn-glycerol + a 1,2-diacyl-sn-glycero-3-phospho-(1&#x27;-sn-glycerol) = a cardiolipin + CMP + H(+)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MASGQMAPSLLRRPITFVSSCPPALRSFGALCPPTGSTDLIGGTGRDILIAAAPARRAPLHATLPLLRSLHTSPAPQLSASHQHQAQQQQQQTKQPQQPYDPQQDQVPSTSTASSSKPAADPVYNLPNAVSVARLVSGPLIGYWLVQGHYEAATLALAVSGASDWLDGWLARRLGASSVFGSYLDPLADKVLIGCVAAALLMNGAMPGWVAGVVVGRDVLLVAGSFVFRLRGFGWRWPGAAAFFRTVDTSAAAAGAATGAANGVASGGGGGGEGVSFMRPLLISKANTVLQLLLLGGYLLRGMDGGAGLQLLLPGGGGEELIMGLELATAATTVASGLAYGTMAVQGKLFK

[Multiple Choices]
A. a (3E,5Z)-dienoyl-CoA = a (2E,4E)-(5,6-saturated)-dienoyl-CoA
B. a CDP-1,2-diacyl-sn-glycerol + a 1,2-diacyl-sn-glycero-3-phospho-(1'-sn-glycerol) = a cardiolipin + CMP + H(+)
C. (1S,4S)-4-[(4-methoxyphenyl)methyl]-2,5-diazaspiro[bicyclo[3.2.1]octane-6,1'-cyclohexan]-4'-one + S-adenosyl-L-methionine = (1S,4S)-4-[(4-methoxyphenyl)methyl]-2-methyl-2,5-diazaspiro[bicyclo[3.2.1]octane-6,1'-cyclohexan]-4'-one + S-adenosyl-L-homocysteine + H(+)
D. Hydrolysis of terminal, non-reducing (1->4)-linked alpha-D-glucose residues with release of alpha-D-glucose.
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzymatic Reaction Prediction, which is to identify the specific chemical reaction catalyzed by a given enzyme. This involves understanding the enzyme's function based on its amino acid sequence and then selecting the correct transformation of substrates into products from a list of possible reactions.. The inputs provided by the user for this task include:

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

> The reviewer-only UniProt records match the supplied sequence and annotate it as a CMP-forming cardiolipin synthase, with the catalytic reaction given in option B. The annotation cites a publication, but the excerpts do not independently establish the experimental details behind that annotation.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains several long hydrophobic regions, consistent with an integral membrane protein. A lipid-synthesis enzyme making cardiolipin, itself a membrane phospholipid, is a plausible family-level fit for option B. The other choices describe a CoA-reaction enzyme, a small-molecule methyltransferase, or a glucose-releasing hydrolase, which are less consistent with this strongly membrane-associated sequence. This is a transferable, probabilistic inference, not a sequence-only proof of the exact reaction.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence’s membrane-protein character and the lipid-synthesis reaction in option B meaningfully distinguish it from these alternatives without relying on the target’s database annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the offered reactions, B is the one that fits the sequence’s strong membrane-protein character and a membrane-lipid synthesis role.


### Important caveats

- The exact-sequence database annotations are reviewer-only evidence and were not part of the original input.
- The cited annotation has a curator-inference evidence code; the excerpts do not provide a direct account of experimental validation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains several long hydrophobic regions, consistent with an integral membrane protein. A lipid-synthesis enzyme making cardiolipin, itself a membrane phospholipid, is a plausible family-level fit for option B. The other choices describe a CoA-reaction enzyme, a small-molecule methyltransferase, or a glucose-releasing hydrolase, which are less consistent with this strongly membrane-associated sequence. This is a transferable, probabilistic inference, not a sequence-only proof of the exact reaction.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence’s membrane-protein character and the lipid-synthesis reaction in option B meaningfully distinguish it from these alternatives without relying on the target’s database annotation."
  },
  "case_id": "catalytic_activity_0006",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The reviewer-only UniProt records match the supplied sequence and annotate it as a CMP-forming cardiolipin synthase, with the catalytic reaction given in option B. The annotation cites a publication, but the excerpts do not independently establish the experimental details behind that annotation."
  },
  "important_caveats": [
    "The exact-sequence database annotations are reviewer-only evidence and were not part of the original input.",
    "The cited annotation has a curator-inference evidence code; the excerpts do not provide a direct account of experimental validation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered reactions, B is the one that fits the sequence’s strong membrane-protein character and a membrane-lipid synthesis role."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0006",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The reviewer-only UniProt records match the supplied sequence and annotate it as a CMP-forming cardiolipin synthase, with the catalytic reaction given in option B. The annotation cites a publication, but the excerpts do not independently establish the experimental details behind that annotation.",
    "evidence_ids": ["C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains several long hydrophobic regions, consistent with an integral membrane protein. A lipid-synthesis enzyme making cardiolipin, itself a membrane phospholipid, is a plausible family-level fit for option B. The other choices describe a CoA-reaction enzyme, a small-molecule methyltransferase, or a glucose-releasing hydrolase, which are less consistent with this strongly membrane-associated sequence. This is a transferable, probabilistic inference, not a sequence-only proof of the exact reaction.",
    "missing_item_specific_fact": "",
    "reason": "The sequence’s membrane-protein character and the lipid-synthesis reaction in option B meaningfully distinguish it from these alternatives without relying on the target’s database annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered reactions, B is the one that fits the sequence’s strong membrane-protein character and a membrane-lipid synthesis role."
  },
  "important_caveats": [
    "The exact-sequence database annotations are reviewer-only evidence and were not part of the original input.",
    "The cited annotation has a curator-inference evidence code; the excerpts do not provide a direct account of experimental validation."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A2K3D1C8 (CRLS1_CHLRE, Chlamydomonas reinhardtii) is annotated as 'Cardiolipin synthase (CMP-forming)' with EC 2.7.8.41, and the catalytic activity comment (evidence C5, H4) states the reaction text verbatim as in option B. The annotation is supported by PubMed:26793177 (Hung et al. 2015, Front Microbiol) with evidence code ECO:0000305 (inferred by similarity to a related protein, backed by a specific functional characterization paper). The benchmark sequence matches the source sequence (351 AA, SHA256 identical).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence (351 aa) contains multiple extended hydrophobic stretches (e.g., LLRRPITFVSSCPPALRSFGALCPPTGSTDLIGGTGRDILIAAAPARRAPLHATLPLLRSLHTS; VLIGCVAAALLMNGAMPGWVAGVVVGRDVLLVAGSFVFRLRGFGWRWPGAAAFFRTVDTS; VLQLLLLGGYLLRGMDGGAGLQLLLPGGGGEELIMGLELATAATTVASGLAYGTMAVQGKLFK) indicating a multi-pass membrane protein. This topology eliminates option D (glucoamylase/α-glucosidase, EC 3.2.1.3: a soluble GH-family enzyme with a characteristic (β/α)8 barrel fold and no TM helices) and option A (dienoyl-CoA isomerase, EC 5.3.3.9: a small ~230-aa soluble mitochondrial/peroxisomal enzyme). Option C involves a SAM-dependent methyltransferase acting on an extremely exotic spiro-bicyclic substrate; SAM-binding methyltransferases require a conserved Rossmann-fold motif (e.g., DxGxGxG or similar) which is absent from this sequence. Option B (cardiolipin synthase, CMP-forming, EC 2.7.8.41) is a phosphatidyltransferase-superfamily membrane enzyme of ~300-400 aa with 4-6 TM helices, consistent with the observed topology and size. The elimination of A, C, and D based on well-established structural requirements of those enzyme families (solubility, domain architecture, cofactor-binding motifs) leaves B as the only option compatible with a multi-TM membrane protein of this size lacking glycosidase or methyltransferase motifs.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can use general principles: (1) multi-TM topology is incompatible with soluble glycosidases (D) and small soluble isomerases (A); (2) absence of SAM-binding Rossmann motifs argues against methyltransferases (C); (3) phospholipid-biosynthesis enzymes (including CLS) are membrane-integrated proteins of this approximate size. The argument relies on family-level structural biology knowledge transferable across many proteins, not on recalling this specific UniProt entry's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent very different enzyme classes (isomerase, phosphatidyltransferase, methyltransferase, glycosidase) with distinct structural requirements. The membrane-protein topology and absence of diagnostic motifs for the other three classes make B the only consistent choice. No other option is defensible given the sequence features.


### Important caveats

- The UniProt annotation uses evidence code ECO:0000305 (inferred by similarity), though it is backed by a specific functional characterization paper (Hung et al. 2015). This is not direct experimental kinetics on this exact protein but is a well-supported annotation.
- The reasoning argument is primarily by elimination (ruling out A, C, D) rather than by positive identification of a CLS-specific catalytic motif in the sequence. The DxDTxxG phosphatidyltransferase motif is not unambiguously identifiable in this sequence by casual inspection, though the overall architecture is consistent.
- The poly-glutamine stretch (QQQQQQ) in the N-terminal region is unusual and its functional significance is unclear, but it does not conflict with the CLS assignment.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence (351 aa) contains multiple extended hydrophobic stretches (e.g., LLRRPITFVSSCPPALRSFGALCPPTGSTDLIGGTGRDILIAAAPARRAPLHATLPLLRSLHTS; VLIGCVAAALLMNGAMPGWVAGVVVGRDVLLVAGSFVFRLRGFGWRWPGAAAFFRTVDTS; VLQLLLLGGYLLRGMDGGAGLQLLLPGGGGEELIMGLELATAATTVASGLAYGTMAVQGKLFK) indicating a multi-pass membrane protein. This topology eliminates option D (glucoamylase/α-glucosidase, EC 3.2.1.3: a soluble GH-family enzyme with a characteristic (β/α)8 barrel fold and no TM helices) and option A (dienoyl-CoA isomerase, EC 5.3.3.9: a small ~230-aa soluble mitochondrial/peroxisomal enzyme). Option C involves a SAM-dependent methyltransferase acting on an extremely exotic spiro-bicyclic substrate; SAM-binding methyltransferases require a conserved Rossmann-fold motif (e.g., DxGxGxG or similar) which is absent from this sequence. Option B (cardiolipin synthase, CMP-forming, EC 2.7.8.41) is a phosphatidyltransferase-superfamily membrane enzyme of ~300-400 aa with 4-6 TM helices, consistent with the observed topology and size. The elimination of A, C, and D based on well-established structural requirements of those enzyme families (solubility, domain architecture, cofactor-binding motifs) leaves B as the only option compatible with a multi-TM membrane protein of this size lacking glycosidase or methyltransferase motifs.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use general principles: (1) multi-TM topology is incompatible with soluble glycosidases (D) and small soluble isomerases (A); (2) absence of SAM-binding Rossmann motifs argues against methyltransferases (C); (3) phospholipid-biosynthesis enzymes (including CLS) are membrane-integrated proteins of this approximate size. The argument relies on family-level structural biology knowledge transferable across many proteins, not on recalling this specific UniProt entry's annotation."
  },
  "case_id": "catalytic_activity_0006",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A2K3D1C8 (CRLS1_CHLRE, Chlamydomonas reinhardtii) is annotated as 'Cardiolipin synthase (CMP-forming)' with EC 2.7.8.41, and the catalytic activity comment (evidence C5, H4) states the reaction text verbatim as in option B. The annotation is supported by PubMed:26793177 (Hung et al. 2015, Front Microbiol) with evidence code ECO:0000305 (inferred by similarity to a related protein, backed by a specific functional characterization paper). The benchmark sequence matches the source sequence (351 AA, SHA256 identical)."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000305 (inferred by similarity), though it is backed by a specific functional characterization paper (Hung et al. 2015). This is not direct experimental kinetics on this exact protein but is a well-supported annotation.",
    "The reasoning argument is primarily by elimination (ruling out A, C, D) rather than by positive identification of a CLS-specific catalytic motif in the sequence. The DxDTxxG phosphatidyltransferase motif is not unambiguously identifiable in this sequence by casual inspection, though the overall architecture is consistent.",
    "The poly-glutamine stretch (QQQQQQ) in the N-terminal region is unusual and its functional significance is unclear, but it does not conflict with the CLS assignment."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent very different enzyme classes (isomerase, phosphatidyltransferase, methyltransferase, glycosidase) with distinct structural requirements. The membrane-protein topology and absence of diagnostic motifs for the other three classes make B the only consistent choice. No other option is defensible given the sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0006",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A2K3D1C8 (CRLS1_CHLRE, Chlamydomonas reinhardtii) is annotated as 'Cardiolipin synthase (CMP-forming)' with EC 2.7.8.41, and the catalytic activity comment (evidence C5, H4) states the reaction text verbatim as in option B. The annotation is supported by PubMed:26793177 (Hung et al. 2015, Front Microbiol) with evidence code ECO:0000305 (inferred by similarity to a related protein, backed by a specific functional characterization paper). The benchmark sequence matches the source sequence (351 AA, SHA256 identical).",
    "evidence_ids": ["C4", "C5", "C6", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence (351 aa) contains multiple extended hydrophobic stretches (e.g., LLRRPITFVSSCPPALRSFGALCPPTGSTDLIGGTGRDILIAAAPARRAPLHATLPLLRSLHTS; VLIGCVAAALLMNGAMPGWVAGVVVGRDVLLVAGSFVFRLRGFGWRWPGAAAFFRTVDTS; VLQLLLLGGYLLRGMDGGAGLQLLLPGGGGEELIMGLELATAATTVASGLAYGTMAVQGKLFK) indicating a multi-pass membrane protein. This topology eliminates option D (glucoamylase/α-glucosidase, EC 3.2.1.3: a soluble GH-family enzyme with a characteristic (β/α)8 barrel fold and no TM helices) and option A (dienoyl-CoA isomerase, EC 5.3.3.9: a small ~230-aa soluble mitochondrial/peroxisomal enzyme). Option C involves a SAM-dependent methyltransferase acting on an extremely exotic spiro-bicyclic substrate; SAM-binding methyltransferases require a conserved Rossmann-fold motif (e.g., DxGxGxG or similar) which is absent from this sequence. Option B (cardiolipin synthase, CMP-forming, EC 2.7.8.41) is a phosphatidyltransferase-superfamily membrane enzyme of ~300-400 aa with 4-6 TM helices, consistent with the observed topology and size. The elimination of A, C, and D based on well-established structural requirements of those enzyme families (solubility, domain architecture, cofactor-binding motifs) leaves B as the only option compatible with a multi-TM membrane protein of this size lacking glycosidase or methyltransferase motifs.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use general principles: (1) multi-TM topology is incompatible with soluble glycosidases (D) and small soluble isomerases (A); (2) absence of SAM-binding Rossmann motifs argues against methyltransferases (C); (3) phospholipid-biosynthesis enzymes (including CLS) are membrane-integrated proteins of this approximate size. The argument relies on family-level structural biology knowledge transferable across many proteins, not on recalling this specific UniProt entry's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent very different enzyme classes (isomerase, phosphatidyltransferase, methyltransferase, glycosidase) with distinct structural requirements. The membrane-protein topology and absence of diagnostic motifs for the other three classes make B the only consistent choice. No other option is defensible given the sequence features."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000305 (inferred by similarity), though it is backed by a specific functional characterization paper (Hung et al. 2015). This is not direct experimental kinetics on this exact protein but is a well-supported annotation.",
    "The reasoning argument is primarily by elimination (ruling out A, C, D) rather than by positive identification of a CLS-specific catalytic motif in the sequence. The DxDTxxG phosphatidyltransferase motif is not unambiguously identifiable in this sequence by casual inspection, though the overall architecture is consistent.",
    "The poly-glutamine stretch (QQQQQQ) in the N-terminal region is unusual and its functional significance is unclear, but it does not conflict with the CLS assignment."
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
  "benchmark_sequence_length": 351,
  "benchmark_sequence_sha256": "d5caa566c264b21e72ce662ef50949e75c0df2a96713facfc4330fbd74359ca1",
  "current_entry_audit": {
    "entryVersion": 33,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2018-03-28",
    "sequenceVersion": 1
  },
  "current_record_sha256": "26e9b73e0d86ca30bf42039424c27469e24cd0f504b95de4718d0e72ea3a9a16",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 351,
  "current_source_sequence_sha256": "d5caa566c264b21e72ce662ef50949e75c0df2a96713facfc4330fbd74359ca1",
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
  "requested_accession": "A0A2K3D1C8",
  "selected_historical_entry_version": 31,
  "selected_historical_record_sha256": "59f1e23ac2c4d5a40557e3d481dab63f297277a1a4b73ab6748fe911f7d4716c",
  "selected_historical_source_sequence_length": 351,
  "selected_historical_source_sequence_sha256": "d5caa566c264b21e72ce662ef50949e75c0df2a96713facfc4330fbd74359ca1",
  "selected_historical_version": {
    "accession": "A0A2K3D1C8",
    "database": "Swiss-Prot",
    "entryVersion": 31,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "CRLS1_CHLRE",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2K3D1C8.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A2K3D1C8\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:24:48.321314+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "26e9b73e0d86ca30bf42039424c27469e24cd0f504b95de4718d0e72ea3a9a16",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2K3D1C8.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2K3D1C8.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":33,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2018-03-28\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:24:48.321314+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "26e9b73e0d86ca30bf42039424c27469e24cd0f504b95de4718d0e72ea3a9a16",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2K3D1C8.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2K3D1C8.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Chlamydomonas smithii\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000006906\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Chlorophyta\",\"core chlorophytes\",\"Chlorophyceae\",\"CS clade\",\"Chlamydomonadales\",\"Chlamydomonadaceae\",\"Chlamydomonas\"],\"scientificName\":\"Chlamydomonas reinhardtii\",\"taxonId\":3055}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:24:48.321314+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "26e9b73e0d86ca30bf42039424c27469e24cd0f504b95de4718d0e72ea3a9a16",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2K3D1C8.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2K3D1C8.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"26793177\",\"source\":\"PubMed\"}],\"value\":\"2.7.8.41\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Cardiolipin synthase (CMP-forming)\"},\"shortNames\":[{\"value\":\"CLS\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:24:48.321314+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "26e9b73e0d86ca30bf42039424c27469e24cd0f504b95de4718d0e72ea3a9a16",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2K3D1C8.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2K3D1C8.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"2.7.8.41\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"26793177\",\"source\":\"PubMed\"}],\"name\":\"a CDP-1,2-diacyl-sn-glycerol + a 1,2-diacyl-sn-glycero-3-phospho-(1'-sn-glycerol) = a cardiolipin + CMP + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:32931\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58332\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:60377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:62237\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:64716\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:24:48.321314+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "26e9b73e0d86ca30bf42039424c27469e24cd0f504b95de4718d0e72ea3a9a16",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2K3D1C8.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2K3D1C8.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Hung C.H.\",\"Kobayashi K.\",\"Wada H.\",\"Nakamura Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"26793177\"},{\"database\":\"DOI\",\"id\":\"10.3389/fmicb.2015.01542\"}],\"citationType\":\"journal article\",\"firstPage\":\"1542\",\"id\":\"26793177\",\"journal\":\"Front. Microbiol.\",\"lastPage\":\"1542\",\"publicationDate\":\"2015\",\"title\":\"Functional Specificity of Cardiolipin Synthase Revealed by the Identification of a Cardiolipin Synthase CrCLS1 in Chlamydomonas reinhardtii.\",\"volume\":\"6\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:24:48.321314+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "26e9b73e0d86ca30bf42039424c27469e24cd0f504b95de4718d0e72ea3a9a16",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2K3D1C8.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2K3D1C8?format=txt&versions=31)

```json
{
  "entry_version": 31,
  "evidence_id": "H1",
  "excerpt": "ID   CRLS1_CHLRE             Reviewed;         351 AA.\nAC   A0A2K3D1C8;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   28-MAR-2018, sequence version 1.\nDT   28-JAN-2026, entry version 31.\nDE   RecName: Full=Cardiolipin synthase (CMP-forming) {ECO:0000305};\nDE            Short=CLS;\nDE            EC=2.7.8.41 {ECO:0000305|PubMed:26793177};\nDE   Flags: Precursor;\nGN   ORFNames=CHLRE_13g604700v5 {ECO:0000312|EMBL:PNW74341.1};\nOS   Chlamydomonas reinhardtii (Chlamydomonas smithii).\nOC   Eukaryota; Viridiplantae; Chlorophyta; core chlorophytes; Chlorophyceae;\nOC   CS clade; Chlamydomonadales; Chlamydomonadaceae; Chlamydomonas.\nOX   NCBI_TaxID=3055 {ECO:0000312|Proteomes:UP000006906};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:52.248527+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "59f1e23ac2c4d5a40557e3d481dab63f297277a1a4b73ab6748fe911f7d4716c",
  "url": "https://rest.uniprot.org/unisave/A0A2K3D1C8?format=txt&versions=31"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2K3D1C8?format=txt&versions=31)

```json
{
  "entry_version": 31,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Cardiolipin synthase (CMP-forming) {ECO:0000305};\nDE            Short=CLS;\nDE            EC=2.7.8.41 {ECO:0000305|PubMed:26793177};\nDE   Flags: Precursor;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:52.248527+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-9",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "59f1e23ac2c4d5a40557e3d481dab63f297277a1a4b73ab6748fe911f7d4716c",
  "url": "https://rest.uniprot.org/unisave/A0A2K3D1C8?format=txt&versions=31"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2K3D1C8?format=txt&versions=31)

```json
{
  "entry_version": 31,
  "evidence_id": "H3",
  "excerpt": "RN   [2] {ECO:0000305}\nRP   FUNCTION, AND CATALYTIC ACTIVITY.\nRX   PubMed=26793177; DOI=10.3389/fmicb.2015.01542;\nRA   Hung C.H., Kobayashi K., Wada H., Nakamura Y.;\nRT   \"Functional Specificity of Cardiolipin Synthase Revealed by the\nRT   Identification of a Cardiolipin Synthase CrCLS1 in Chlamydomonas\nRT   reinhardtii.\";\nRL   Front. Microbiol. 6:1542-1542(2015).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:52.248527+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 43-50",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "59f1e23ac2c4d5a40557e3d481dab63f297277a1a4b73ab6748fe911f7d4716c",
  "url": "https://rest.uniprot.org/unisave/A0A2K3D1C8?format=txt&versions=31"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2K3D1C8?format=txt&versions=31)

```json
{
  "entry_version": 31,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=a CDP-1,2-diacyl-sn-glycerol + a 1,2-diacyl-sn-glycero-3-\nCC         phospho-(1'-sn-glycerol) = a cardiolipin + CMP + H(+);\nCC         Xref=Rhea:RHEA:32931, ChEBI:CHEBI:15378, ChEBI:CHEBI:58332,\nCC         ChEBI:CHEBI:60377, ChEBI:CHEBI:62237, ChEBI:CHEBI:64716; EC=2.7.8.41;\nCC         Evidence={ECO:0000305|PubMed:26793177};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:52.248527+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 60-65",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "59f1e23ac2c4d5a40557e3d481dab63f297277a1a4b73ab6748fe911f7d4716c",
  "url": "https://rest.uniprot.org/unisave/A0A2K3D1C8?format=txt&versions=31"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 6. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
