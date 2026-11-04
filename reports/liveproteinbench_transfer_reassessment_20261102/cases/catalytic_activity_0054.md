# catalytic_activity_0054

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/catalytic_activity_0054.txt)

**Task:** `catalytic_activity`  
**Expected answer:** **A** — inosine(in) + H(+)(in) = inosine(out) + H(+)(out)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MTGQSAAVEGSNSALPWYRMGFHTLAEFNTYVTFVLLGMSIMMVTSAVTSAPDFVTKYFIYATGDPDAVAETPLFWNNANTFYNAGTYAMQVVTEIASLTPFMRSIPLGIRLFLGLGIPFVELVVIIAVPAATIPTQNGAIAVIMVVAMMGGLSKALCDSCTNALVGPFPTKFMNGAQWGLTVIALFMSIIQIILQVSMGSTFQDVLTISRIYFGIGIGIQVMAIAALVLLRYNPFAQKYIAEFRAAALRRRGHVEPEESQDSKEPATGDVAEAPKAGEKEVTLDAMEEADEVRAVPSDAFVAKSGAVLQATGDADRMVDLDQTKNITSTEQMLRASVWSVFKRIYPMLLCAFTIFFTTLLVFPGVFFLVPARSGWYMTIIVTLFNAGDFVARVLLMIRVLRPSPKLVIVGTFGRLAVIPLIVLCVRGFIPGVALPYVLIFLFGLTNGYFGTMSCIHCPRTPTLHYAGERSVAAMLAGISLMLGLCFGSNMSLAITLTY

[Multiple Choices]
A. inosine(in) + H(+)(in) = inosine(out) + H(+)(out)
B. selenite + a quinone + H2O = selenate + a quinol
C. aminoacetaldehyde + 2 oxidized [4Fe-4S]-[ferredoxin] + H2O = 2 reduced [4Fe-4S]-[ferredoxin] + glycine + 3 H(+)
D. 3-oxoadipate + acetyl-CoA = acetoacetate + succinyl-CoA
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

> The source record matches the supplied sequence and reports the inosine transport reaction with experimental evidence codes, supporting choice A.

Citations as saved: [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is strongly hydrophobic and consistent with a multipass membrane protein. Such architecture supports a membrane-transport function, matching choice A's movement of inosine and H+ across a membrane; the other choices describe oxidation or soluble metabolic transformations rather than transport.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable knowledge about multipass membrane transporters meaningfully distinguishes the transport reaction from the three enzyme-reaction alternatives. The sequence alone may not establish inosine as the substrate, but among the offered choices A is strongly indicated.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only choice A describes transmembrane transport; none of the other options is a comparable alternative for this sequence.


### Important caveats

- The specific substrate assignment is more securely supported by the matched source record than by sequence architecture alone.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is strongly hydrophobic and consistent with a multipass membrane protein. Such architecture supports a membrane-transport function, matching choice A's movement of inosine and H+ across a membrane; the other choices describe oxidation or soluble metabolic transformations rather than transport.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge about multipass membrane transporters meaningfully distinguishes the transport reaction from the three enzyme-reaction alternatives. The sequence alone may not establish inosine as the substrate, but among the offered choices A is strongly indicated."
  },
  "case_id": "catalytic_activity_0054",
  "expected_answer_check": {
    "evidence_ids": [
      "C5"
    ],
    "judgment": "supported",
    "reason": "The source record matches the supplied sequence and reports the inosine transport reaction with experimental evidence codes, supporting choice A."
  },
  "important_caveats": [
    "The specific substrate assignment is more securely supported by the matched source record than by sequence architecture alone."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only choice A describes transmembrane transport; none of the other options is a comparable alternative for this sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0054",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The source record matches the supplied sequence and reports the inosine transport reaction with experimental evidence codes, supporting choice A.",
    "evidence_ids": ["C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is strongly hydrophobic and consistent with a multipass membrane protein. Such architecture supports a membrane-transport function, matching choice A's movement of inosine and H+ across a membrane; the other choices describe oxidation or soluble metabolic transformations rather than transport.",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge about multipass membrane transporters meaningfully distinguishes the transport reaction from the three enzyme-reaction alternatives. The sequence alone may not establish inosine as the substrate, but among the offered choices A is strongly indicated."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only choice A describes transmembrane transport; none of the other options is a comparable alternative for this sequence."
  },
  "important_caveats": [
    "The specific substrate assignment is more securely supported by the matched source record than by sequence architecture alone."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q9NBV4 (Nucleoside transporter 2 / LdNT2 from Leishmania donovani) explicitly lists 'inosine(in) + H(+)(in) = inosine(out) + H(+)(out)' as a CATALYTIC ACTIVITY with ECO:0000269 (direct assay evidence) supported by five independent PubMed references (10783393, 12807872, 12835315, 15501825, 16464630). The protein is annotated as an equilibrative nucleoside transporter / inosine-guanosine nucleoside transporter. The sequence in the question matches the UniProt entry exactly (SHA-256 confirmed). The reaction is well-established experimentally.

Citations as saved: [C5](#evidence-c5), [H9](#evidence-h9).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains multiple long hydrophobic stretches (~11 TM helices) characteristic of a membrane transport protein, immediately distinguishing it from the three distractor enzymes (B: a soluble selenite oxidoreductase; C: a ferredoxin-dependent dehydrogenase with 4Fe-4S clusters; D: a soluble CoA-transferase/thiolase). None of B, C, or D would possess the multi-TM topology evident here. Within the membrane-transporter class, the sequence displays hallmark features of the equilibrative nucleoside transporter (ENT) family: glycine-rich motifs (e.g., 'GIGIGIQVMAIAALVLLRYNPFAQ', 'GTFGRLAVIPLIVLCVRGFIPGVALPYVLIFLFGLTNGYFGTMSCIHCPRTPTLHYAGERSVAAMLAGISLMLGLCFGSNMSLAITLTY'), the 11-TM topology, and the overall hydrophobicity pattern shared with well-characterized ENT members (human ENT1-4, yeast ENT, etc.). Transferable knowledge from the ENT family establishes that these are proton-coupled nucleoside symporters, matching the reaction 'inosine(in) + H(+)(in) = inosine(out) + H(+)(out)'. The model need not identify the exact substrate (inosine vs. guanosine vs. xanthosine) because only inosine transport is offered among the choices; the other three options are entirely different enzyme classes that the TM-domain pattern eliminates.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can recognize the multi-TM architecture as a membrane transporter, identify ENT-family sequence signatures (GxxxG motifs, 11-TM topology), and apply the well-established family-level fact that ENT members are proton-coupled nucleoside symporters. This reasoning eliminates B (soluble oxidoreductase), C (Fe-S dehydrogenase), and D (CoA-transferase) based on protein class, and selects A as the only transport-type reaction consistent with the ENT family. No target-specific database lookup is required.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent fundamentally different protein classes: A is a proton-coupled nucleoside transport reaction (membrane transporter), B is a soluble oxidoreductase reaction, C is a ferredoxin-dependent dehydrogenase reaction with 4Fe-4S clusters, and D is a CoA-transferase reaction. The multi-TM sequence pattern unambiguously points to a membrane transporter, eliminating B, C, and D. Although the UniProt entry also annotates guanosine and xanthosine transport, neither is offered as a choice, so no ambiguity exists among the presented alternatives.


### Important caveats

- The UniProt entry flags the protein as a 'Fragment' (499 AA), meaning the full-length transporter may have additional TM domains not present in the supplied sequence. However, the fragment still retains sufficient ENT-family topology to be recognizable.
- The reaction is labeled 'catalytic activity' in UniProt, but it is mechanistically a transport (translocation) reaction, not a chemical transformation. This is standard UniProt convention for transporters.
- The ENT family in trypanosomatids is known to be proton-coupled (electrogenic proton symporters, per PubMed 12835315), which is a family-level feature transferable from other members, not unique to this protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains multiple long hydrophobic stretches (~11 TM helices) characteristic of a membrane transport protein, immediately distinguishing it from the three distractor enzymes (B: a soluble selenite oxidoreductase; C: a ferredoxin-dependent dehydrogenase with 4Fe-4S clusters; D: a soluble CoA-transferase/thiolase). None of B, C, or D would possess the multi-TM topology evident here. Within the membrane-transporter class, the sequence displays hallmark features of the equilibrative nucleoside transporter (ENT) family: glycine-rich motifs (e.g., 'GIGIGIQVMAIAALVLLRYNPFAQ', 'GTFGRLAVIPLIVLCVRGFIPGVALPYVLIFLFGLTNGYFGTMSCIHCPRTPTLHYAGERSVAAMLAGISLMLGLCFGSNMSLAITLTY'), the 11-TM topology, and the overall hydrophobicity pattern shared with well-characterized ENT members (human ENT1-4, yeast ENT, etc.). Transferable knowledge from the ENT family establishes that these are proton-coupled nucleoside symporters, matching the reaction 'inosine(in) + H(+)(in) = inosine(out) + H(+)(out)'. The model need not identify the exact substrate (inosine vs. guanosine vs. xanthosine) because only inosine transport is offered among the choices; the other three options are entirely different enzyme classes that the TM-domain pattern eliminates.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the multi-TM architecture as a membrane transporter, identify ENT-family sequence signatures (GxxxG motifs, 11-TM topology), and apply the well-established family-level fact that ENT members are proton-coupled nucleoside symporters. This reasoning eliminates B (soluble oxidoreductase), C (Fe-S dehydrogenase), and D (CoA-transferase) based on protein class, and selects A as the only transport-type reaction consistent with the ENT family. No target-specific database lookup is required."
  },
  "case_id": "catalytic_activity_0054",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H9"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q9NBV4 (Nucleoside transporter 2 / LdNT2 from Leishmania donovani) explicitly lists 'inosine(in) + H(+)(in) = inosine(out) + H(+)(out)' as a CATALYTIC ACTIVITY with ECO:0000269 (direct assay evidence) supported by five independent PubMed references (10783393, 12807872, 12835315, 15501825, 16464630). The protein is annotated as an equilibrative nucleoside transporter / inosine-guanosine nucleoside transporter. The sequence in the question matches the UniProt entry exactly (SHA-256 confirmed). The reaction is well-established experimentally."
  },
  "important_caveats": [
    "The UniProt entry flags the protein as a 'Fragment' (499 AA), meaning the full-length transporter may have additional TM domains not present in the supplied sequence. However, the fragment still retains sufficient ENT-family topology to be recognizable.",
    "The reaction is labeled 'catalytic activity' in UniProt, but it is mechanistically a transport (translocation) reaction, not a chemical transformation. This is standard UniProt convention for transporters.",
    "The ENT family in trypanosomatids is known to be proton-coupled (electrogenic proton symporters, per PubMed 12835315), which is a family-level feature transferable from other members, not unique to this protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent fundamentally different protein classes: A is a proton-coupled nucleoside transport reaction (membrane transporter), B is a soluble oxidoreductase reaction, C is a ferredoxin-dependent dehydrogenase reaction with 4Fe-4S clusters, and D is a CoA-transferase reaction. The multi-TM sequence pattern unambiguously points to a membrane transporter, eliminating B, C, and D. Although the UniProt entry also annotates guanosine and xanthosine transport, neither is offered as a choice, so no ambiguity exists among the presented alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0054",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q9NBV4 (Nucleoside transporter 2 / LdNT2 from Leishmania donovani) explicitly lists 'inosine(in) + H(+)(in) = inosine(out) + H(+)(out)' as a CATALYTIC ACTIVITY with ECO:0000269 (direct assay evidence) supported by five independent PubMed references (10783393, 12807872, 12835315, 15501825, 16464630). The protein is annotated as an equilibrative nucleoside transporter / inosine-guanosine nucleoside transporter. The sequence in the question matches the UniProt entry exactly (SHA-256 confirmed). The reaction is well-established experimentally.",
    "evidence_ids": ["C5", "H9"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains multiple long hydrophobic stretches (~11 TM helices) characteristic of a membrane transport protein, immediately distinguishing it from the three distractor enzymes (B: a soluble selenite oxidoreductase; C: a ferredoxin-dependent dehydrogenase with 4Fe-4S clusters; D: a soluble CoA-transferase/thiolase). None of B, C, or D would possess the multi-TM topology evident here. Within the membrane-transporter class, the sequence displays hallmark features of the equilibrative nucleoside transporter (ENT) family: glycine-rich motifs (e.g., 'GIGIGIQVMAIAALVLLRYNPFAQ', 'GTFGRLAVIPLIVLCVRGFIPGVALPYVLIFLFGLTNGYFGTMSCIHCPRTPTLHYAGERSVAAMLAGISLMLGLCFGSNMSLAITLTY'), the 11-TM topology, and the overall hydrophobicity pattern shared with well-characterized ENT members (human ENT1-4, yeast ENT, etc.). Transferable knowledge from the ENT family establishes that these are proton-coupled nucleoside symporters, matching the reaction 'inosine(in) + H(+)(in) = inosine(out) + H(+)(out)'. The model need not identify the exact substrate (inosine vs. guanosine vs. xanthosine) because only inosine transport is offered among the choices; the other three options are entirely different enzyme classes that the TM-domain pattern eliminates.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the multi-TM architecture as a membrane transporter, identify ENT-family sequence signatures (GxxxG motifs, 11-TM topology), and apply the well-established family-level fact that ENT members are proton-coupled nucleoside symporters. This reasoning eliminates B (soluble oxidoreductase), C (Fe-S dehydrogenase), and D (CoA-transferase) based on protein class, and selects A as the only transport-type reaction consistent with the ENT family. No target-specific database lookup is required."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent fundamentally different protein classes: A is a proton-coupled nucleoside transport reaction (membrane transporter), B is a soluble oxidoreductase reaction, C is a ferredoxin-dependent dehydrogenase reaction with 4Fe-4S clusters, and D is a CoA-transferase reaction. The multi-TM sequence pattern unambiguously points to a membrane transporter, eliminating B, C, and D. Although the UniProt entry also annotates guanosine and xanthosine transport, neither is offered as a choice, so no ambiguity exists among the presented alternatives."
  },
  "important_caveats": [
    "The UniProt entry flags the protein as a 'Fragment' (499 AA), meaning the full-length transporter may have additional TM domains not present in the supplied sequence. However, the fragment still retains sufficient ENT-family topology to be recognizable.",
    "The reaction is labeled 'catalytic activity' in UniProt, but it is mechanistically a transport (translocation) reaction, not a chemical transformation. This is standard UniProt convention for transporters.",
    "The ENT family in trypanosomatids is known to be proton-coupled (electrogenic proton symporters, per PubMed 12835315), which is a family-level feature transferable from other members, not unique to this protein."
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
  "benchmark_sequence_length": 499,
  "benchmark_sequence_sha256": "99913046670b07d17f5e37245b365956cb766f4099d4fd004331889bf4858b34",
  "current_entry_audit": {
    "entryVersion": 62,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2025-06-18",
    "lastSequenceUpdateDate": "2000-10-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "c697205f4abb5ea257a73dd7fa21fb4c3b73a4a657a46f316a07d193e5c8a325",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 499,
  "current_source_sequence_sha256": "99913046670b07d17f5e37245b365956cb766f4099d4fd004331889bf4858b34",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 62,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q9NBV4",
  "selected_historical_entry_version": 62,
  "selected_historical_record_sha256": "c6f3ea767f28b291172d1bff1e34f97db01c5d476a90a59f7196e827ba0e0fa9",
  "selected_historical_source_sequence_length": 499,
  "selected_historical_source_sequence_sha256": "99913046670b07d17f5e37245b365956cb766f4099d4fd004331889bf4858b34",
  "selected_historical_version": {
    "accession": "Q9NBV4",
    "database": "Swiss-Prot",
    "entryVersion": 62,
    "firstRelease": "2025_03/2025_03",
    "firstReleaseDate": "18-Jun-2025",
    "lastRelease": "2026_03/2026_03",
    "lastReleaseDate": "02-Sep-2026",
    "name": "NT2_LEIDO",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9NBV4.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q9NBV4\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:33:10.554926+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c697205f4abb5ea257a73dd7fa21fb4c3b73a4a657a46f316a07d193e5c8a325",
  "url": "https://rest.uniprot.org/uniprotkb/Q9NBV4.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9NBV4.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":62,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2025-06-18\",\"lastSequenceUpdateDate\":\"2000-10-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:33:10.554926+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c697205f4abb5ea257a73dd7fa21fb4c3b73a4a657a46f316a07d193e5c8a325",
  "url": "https://rest.uniprot.org/uniprotkb/Q9NBV4.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9NBV4.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"AAF74264.1\",\"source\":\"EMBL\"}],\"lineage\":[\"Eukaryota\",\"Discoba\",\"Euglenozoa\",\"Kinetoplastea\",\"Metakinetoplastina\",\"Trypanosomatida\",\"Trypanosomatidae\",\"Leishmaniinae\",\"Leishmania\"],\"scientificName\":\"Leishmania donovani\",\"taxonId\":5661}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:33:10.554926+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c697205f4abb5ea257a73dd7fa21fb4c3b73a4a657a46f316a07d193e5c8a325",
  "url": "https://rest.uniprot.org/uniprotkb/Q9NBV4.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9NBV4.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"12835315\",\"source\":\"PubMed\"}],\"value\":\"Equilibrative nucleoside transporter 2\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"AAF74264.1\",\"source\":\"EMBL\"}],\"value\":\"Inosine-guanosine nucleoside transporter\"}}],\"flag\":\"Fragment\",\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"10783393\",\"source\":\"PubMed\"}],\"value\":\"Nucleoside transporter 2\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"10783393\",\"source\":\"PubMed\"}],\"value\":\"LdNT2\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:33:10.554926+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c697205f4abb5ea257a73dd7fa21fb4c3b73a4a657a46f316a07d193e5c8a325",
  "url": "https://rest.uniprot.org/uniprotkb/Q9NBV4.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9NBV4.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"10783393\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"12807872\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"12835315\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"15501825\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"16464630\",\"source\":\"PubMed\"}],\"name\":\"inosine(in) + H(+)(in) = inosine(out) + H(+)(out)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:29963\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:17596\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:33:10.554926+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c697205f4abb5ea257a73dd7fa21fb4c3b73a4a657a46f316a07d193e5c8a325",
  "url": "https://rest.uniprot.org/uniprotkb/Q9NBV4.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9NBV4.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"10783393\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"12807872\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"12835315\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"15501825\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"16464630\",\"source\":\"PubMed\"}],\"name\":\"guanosine(in) + H(+)(in) = guanosine(out) + H(+)(out)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:70915\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:16750\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:33:10.554926+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c697205f4abb5ea257a73dd7fa21fb4c3b73a4a657a46f316a07d193e5c8a325",
  "url": "https://rest.uniprot.org/uniprotkb/Q9NBV4.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9NBV4.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"17050001\",\"source\":\"PubMed\"}],\"name\":\"xanthosine(in) + H(+)(in) = xanthosine(out) + H(+)(out)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:28939\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:18107\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-02T04:33:10.554926+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c697205f4abb5ea257a73dd7fa21fb4c3b73a4a657a46f316a07d193e5c8a325",
  "url": "https://rest.uniprot.org/uniprotkb/Q9NBV4.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9NBV4.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Carter N.S.\",\"Drew M.E.\",\"Sanchez M.\",\"Vasudevan G.\",\"Landfear S.M.\",\"Ullman B.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"10783393\"},{\"database\":\"DOI\",\"id\":\"10.1074/jbc.m002418200\"}],\"citationType\":\"journal article\",\"firstPage\":\"20935\",\"id\":\"10783393\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"20941\",\"publicationDate\":\"2000\",\"title\":\"Cloning of a novel inosine-guanosine transporter gene from Leishmania donovani by functional rescue of a transport-deficient mutant.\",\"volume\":\"275\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"AAF74264.1\",\"source\":\"EMBL\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"FUNCTION\",\"TRANSPORTER ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:33:10.554926+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c697205f4abb5ea257a73dd7fa21fb4c3b73a4a657a46f316a07d193e5c8a325",
  "url": "https://rest.uniprot.org/uniprotkb/Q9NBV4.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9NBV4.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"citation\":{\"authors\":[\"Arastu-Kapur S.\",\"Ford E.\",\"Ullman B.\",\"Carter N.S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"12807872\"},{\"database\":\"DOI\",\"id\":\"10.1074/jbc.m305141200\"}],\"citationType\":\"journal article\",\"firstPage\":\"33327\",\"id\":\"12807872\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"33333\",\"publicationDate\":\"2003\",\"title\":\"Functional analysis of an inosine-guanosine transporter from Leishmania donovani. The role of conserved residues, aspartate 389 and arginine 393.\",\"volume\":\"278\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"TRANSPORTER ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"SUBCELLULAR LOCATION\",\"DISRUPTION PHENOTYPE\",\"TOPOLOGY\",\"MUTAGENESIS OF ASP-389 AND ARG-393\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:33:10.554926+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c697205f4abb5ea257a73dd7fa21fb4c3b73a4a657a46f316a07d193e5c8a325",
  "url": "https://rest.uniprot.org/uniprotkb/Q9NBV4.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9NBV4.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"citation\":{\"authors\":[\"Stein A.\",\"Vaseduvan G.\",\"Carter N.S.\",\"Ullman B.\",\"Landfear S.M.\",\"Kavanaugh M.P.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"12835315\"},{\"database\":\"DOI\",\"id\":\"10.1074/jbc.m306188200\"}],\"citationType\":\"journal article\",\"firstPage\":\"35127\",\"id\":\"12835315\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"35134\",\"publicationDate\":\"2003\",\"title\":\"Equilibrative nucleoside transporter family members from Leishmania donovani are electrogenic proton symporters.\",\"volume\":\"278\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"TRANSPORTER ACTIVITY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-02T04:33:10.554926+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c697205f4abb5ea257a73dd7fa21fb4c3b73a4a657a46f316a07d193e5c8a325",
  "url": "https://rest.uniprot.org/uniprotkb/Q9NBV4.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9NBV4.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"citation\":{\"authors\":[\"Arastu-Kapur S.\",\"Arendt C.S.\",\"Purnat T.\",\"Carter N.S.\",\"Ullman B.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"15501825\"},{\"database\":\"DOI\",\"id\":\"10.1074/jbc.m408224200\"}],\"citationType\":\"journal article\",\"firstPage\":\"2213\",\"id\":\"15501825\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"2219\",\"publicationDate\":\"2005\",\"title\":\"Second-site suppression of a nonfunctional mutation within the Leishmania donovani inosine-guanosine transporter.\",\"volume\":\"280\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":4,\"referencePositions\":[\"TRANSPORTER ACTIVITY\",\"SUBCELLULAR LOCATION\",\"MUTAGENESIS OF ASN-175 AND ASP-389\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-02T04:33:10.554926+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c697205f4abb5ea257a73dd7fa21fb4c3b73a4a657a46f316a07d193e5c8a325",
  "url": "https://rest.uniprot.org/uniprotkb/Q9NBV4.json"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9NBV4.json)

```json
{
  "evidence_id": "C12",
  "excerpt": "{\"citation\":{\"authors\":[\"Galazka J.\",\"Carter N.S.\",\"Bekhouche S.\",\"Arastu-Kapur S.\",\"Ullman B.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"16464630\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.biocel.2005.12.016\"}],\"citationType\":\"journal article\",\"firstPage\":\"1221\",\"id\":\"16464630\",\"journal\":\"Int. J. Biochem. Cell Biol.\",\"lastPage\":\"1229\",\"publicationDate\":\"2006\",\"title\":\"Point mutations within the LdNT2 nucleoside transporter gene from Leishmania donovani confer drug resistance and transport deficiency.\",\"volume\":\"38\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":5,\"referencePositions\":[\"FUNCTION\",\"TRANSPORTER ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"SUBCELLULAR LOCATION\",\"MUTAGENESIS OF SER-189 AND 376-TRP--TYR-499\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/4",
  "retrieved_utc": "2026-11-02T04:33:10.554926+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c697205f4abb5ea257a73dd7fa21fb4c3b73a4a657a46f316a07d193e5c8a325",
  "url": "https://rest.uniprot.org/uniprotkb/Q9NBV4.json"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9NBV4.json)

```json
{
  "evidence_id": "C13",
  "excerpt": "{\"citation\":{\"authors\":[\"Liu W.\",\"Boitz J.M.\",\"Galazka J.\",\"Arendt C.S.\",\"Carter N.S.\",\"Ullman B.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"17050001\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.molbiopara.2006.09.002\"}],\"citationType\":\"journal article\",\"firstPage\":\"300\",\"id\":\"17050001\",\"journal\":\"Mol. Biochem. Parasitol.\",\"lastPage\":\"307\",\"publicationDate\":\"2006\",\"title\":\"Functional characterization of nucleoside transporter gene replacements in Leishmania donovani.\",\"volume\":\"150\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":6,\"referencePositions\":[\"FUNCTION\",\"TRANSPORTER ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/5",
  "retrieved_utc": "2026-11-02T04:33:10.554926+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c697205f4abb5ea257a73dd7fa21fb4c3b73a4a657a46f316a07d193e5c8a325",
  "url": "https://rest.uniprot.org/uniprotkb/Q9NBV4.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9NBV4?format=txt&versions=62)

```json
{
  "entry_version": 62,
  "evidence_id": "H1",
  "excerpt": "ID   NT2_LEIDO               Reviewed;         499 AA.\nAC   Q9NBV4;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-OCT-2000, sequence version 1.\nDT   18-JUN-2025, entry version 62.\nDE   RecName: Full=Nucleoside transporter 2 {ECO:0000303|PubMed:10783393};\nDE            Short=LdNT2 {ECO:0000303|PubMed:10783393};\nDE   AltName: Full=Equilibrative nucleoside transporter 2 {ECO:0000303|PubMed:12835315};\nDE   AltName: Full=Inosine-guanosine nucleoside transporter {ECO:0000312|EMBL:AAF74264.1};\nDE   Flags: Fragment;\nGN   Name=NT2 {ECO:0000312|EMBL:AAF74264.1};\nOS   Leishmania donovani.\nOC   Eukaryota; Discoba; Euglenozoa; Kinetoplastea; Metakinetoplastina;\nOC   Trypanosomatida; Trypanosomatidae; Leishmaniinae; Leishmania.\nOX   NCBI_TaxID=5661 {ECO:0000312|EMBL:AAF74264.1};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:13.069958+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c6f3ea767f28b291172d1bff1e34f97db01c5d476a90a59f7196e827ba0e0fa9",
  "url": "https://rest.uniprot.org/unisave/Q9NBV4?format=txt&versions=62"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9NBV4?format=txt&versions=62)

```json
{
  "entry_version": 62,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Nucleoside transporter 2 {ECO:0000303|PubMed:10783393};\nDE            Short=LdNT2 {ECO:0000303|PubMed:10783393};\nDE   AltName: Full=Equilibrative nucleoside transporter 2 {ECO:0000303|PubMed:12835315};\nDE   AltName: Full=Inosine-guanosine nucleoside transporter {ECO:0000312|EMBL:AAF74264.1};\nDE   Flags: Fragment;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:13.069958+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-10",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c6f3ea767f28b291172d1bff1e34f97db01c5d476a90a59f7196e827ba0e0fa9",
  "url": "https://rest.uniprot.org/unisave/Q9NBV4?format=txt&versions=62"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9NBV4?format=txt&versions=62)

```json
{
  "entry_version": 62,
  "evidence_id": "H3",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:AAF74264.1}\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, TRANSPORTER ACTIVITY, AND\nRP   BIOPHYSICOCHEMICAL PROPERTIES.\nRX   PubMed=10783393; DOI=10.1074/jbc.m002418200;\nRA   Carter N.S., Drew M.E., Sanchez M., Vasudevan G., Landfear S.M., Ullman B.;\nRT   \"Cloning of a novel inosine-guanosine transporter gene from Leishmania\nRT   donovani by functional rescue of a transport-deficient mutant.\";\nRL   J. Biol. Chem. 275:20935-20941(2000).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:13.069958+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 16-23",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c6f3ea767f28b291172d1bff1e34f97db01c5d476a90a59f7196e827ba0e0fa9",
  "url": "https://rest.uniprot.org/unisave/Q9NBV4?format=txt&versions=62"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9NBV4?format=txt&versions=62)

```json
{
  "entry_version": 62,
  "evidence_id": "H4",
  "excerpt": "RN   [2] {ECO:0000305}\nRP   FUNCTION, TRANSPORTER ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, SUBCELLULAR\nRP   LOCATION, DISRUPTION PHENOTYPE, TOPOLOGY, AND MUTAGENESIS OF ASP-389 AND\nRP   ARG-393.\nRX   PubMed=12807872; DOI=10.1074/jbc.m305141200;\nRA   Arastu-Kapur S., Ford E., Ullman B., Carter N.S.;\nRT   \"Functional analysis of an inosine-guanosine transporter from Leishmania\nRT   donovani. The role of conserved residues, aspartate 389 and arginine 393.\";\nRL   J. Biol. Chem. 278:33327-33333(2003).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:13.069958+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 24-32",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c6f3ea767f28b291172d1bff1e34f97db01c5d476a90a59f7196e827ba0e0fa9",
  "url": "https://rest.uniprot.org/unisave/Q9NBV4?format=txt&versions=62"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9NBV4?format=txt&versions=62)

```json
{
  "entry_version": 62,
  "evidence_id": "H5",
  "excerpt": "RN   [3] {ECO:0000305}\nRP   FUNCTION, AND TRANSPORTER ACTIVITY.\nRX   PubMed=12835315; DOI=10.1074/jbc.m306188200;\nRA   Stein A., Vaseduvan G., Carter N.S., Ullman B., Landfear S.M.,\nRA   Kavanaugh M.P.;\nRT   \"Equilibrative nucleoside transporter family members from Leishmania\nRT   donovani are electrogenic proton symporters.\";\nRL   J. Biol. Chem. 278:35127-35134(2003).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:13.069958+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 33-40",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c6f3ea767f28b291172d1bff1e34f97db01c5d476a90a59f7196e827ba0e0fa9",
  "url": "https://rest.uniprot.org/unisave/Q9NBV4?format=txt&versions=62"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9NBV4?format=txt&versions=62)

```json
{
  "entry_version": 62,
  "evidence_id": "H6",
  "excerpt": "RN   [4] {ECO:0000305}\nRP   TRANSPORTER ACTIVITY, SUBCELLULAR LOCATION, AND MUTAGENESIS OF ASN-175 AND\nRP   ASP-389.\nRX   PubMed=15501825; DOI=10.1074/jbc.m408224200;\nRA   Arastu-Kapur S., Arendt C.S., Purnat T., Carter N.S., Ullman B.;\nRT   \"Second-site suppression of a nonfunctional mutation within the Leishmania\nRT   donovani inosine-guanosine transporter.\";\nRL   J. Biol. Chem. 280:2213-2219(2005).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:13.069958+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 41-48",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c6f3ea767f28b291172d1bff1e34f97db01c5d476a90a59f7196e827ba0e0fa9",
  "url": "https://rest.uniprot.org/unisave/Q9NBV4?format=txt&versions=62"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9NBV4?format=txt&versions=62)

```json
{
  "entry_version": 62,
  "evidence_id": "H7",
  "excerpt": "RN   [5] {ECO:0000305}\nRP   FUNCTION, TRANSPORTER ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, SUBCELLULAR\nRP   LOCATION, AND MUTAGENESIS OF SER-189 AND 376-TRP--TYR-499.\nRX   PubMed=16464630; DOI=10.1016/j.biocel.2005.12.016;\nRA   Galazka J., Carter N.S., Bekhouche S., Arastu-Kapur S., Ullman B.;\nRT   \"Point mutations within the LdNT2 nucleoside transporter gene from\nRT   Leishmania donovani confer drug resistance and transport deficiency.\";\nRL   Int. J. Biochem. Cell Biol. 38:1221-1229(2006).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:13.069958+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 49-56",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c6f3ea767f28b291172d1bff1e34f97db01c5d476a90a59f7196e827ba0e0fa9",
  "url": "https://rest.uniprot.org/unisave/Q9NBV4?format=txt&versions=62"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9NBV4?format=txt&versions=62)

```json
{
  "entry_version": 62,
  "evidence_id": "H8",
  "excerpt": "RN   [6] {ECO:0000305}\nRP   FUNCTION, TRANSPORTER ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, AND\nRP   DISRUPTION PHENOTYPE.\nRX   PubMed=17050001; DOI=10.1016/j.molbiopara.2006.09.002;\nRA   Liu W., Boitz J.M., Galazka J., Arendt C.S., Carter N.S., Ullman B.;\nRT   \"Functional characterization of nucleoside transporter gene replacements in\nRT   Leishmania donovani.\";\nRL   Mol. Biochem. Parasitol. 150:300-307(2006).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:13.069958+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 57-64",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c6f3ea767f28b291172d1bff1e34f97db01c5d476a90a59f7196e827ba0e0fa9",
  "url": "https://rest.uniprot.org/unisave/Q9NBV4?format=txt&versions=62"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9NBV4?format=txt&versions=62)

```json
{
  "entry_version": 62,
  "evidence_id": "H9",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=inosine(in) + H(+)(in) = inosine(out) + H(+)(out);\nCC         Xref=Rhea:RHEA:29963, ChEBI:CHEBI:15378, ChEBI:CHEBI:17596;\nCC         Evidence={ECO:0000269|PubMed:10783393, ECO:0000269|PubMed:12807872,\nCC         ECO:0000269|PubMed:12835315, ECO:0000269|PubMed:15501825,\nCC         ECO:0000269|PubMed:16464630};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:13.069958+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 71-76",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c6f3ea767f28b291172d1bff1e34f97db01c5d476a90a59f7196e827ba0e0fa9",
  "url": "https://rest.uniprot.org/unisave/Q9NBV4?format=txt&versions=62"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9NBV4?format=txt&versions=62)

```json
{
  "entry_version": 62,
  "evidence_id": "H10",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=guanosine(in) + H(+)(in) = guanosine(out) + H(+)(out);\nCC         Xref=Rhea:RHEA:70915, ChEBI:CHEBI:15378, ChEBI:CHEBI:16750;\nCC         Evidence={ECO:0000269|PubMed:10783393, ECO:0000269|PubMed:12807872,\nCC         ECO:0000269|PubMed:12835315, ECO:0000269|PubMed:15501825,\nCC         ECO:0000269|PubMed:16464630};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:13.069958+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 77-82",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c6f3ea767f28b291172d1bff1e34f97db01c5d476a90a59f7196e827ba0e0fa9",
  "url": "https://rest.uniprot.org/unisave/Q9NBV4?format=txt&versions=62"
}
```

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9NBV4?format=txt&versions=62)

```json
{
  "entry_version": 62,
  "evidence_id": "H11",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=xanthosine(in) + H(+)(in) = xanthosine(out) + H(+)(out);\nCC         Xref=Rhea:RHEA:28939, ChEBI:CHEBI:15378, ChEBI:CHEBI:18107;\nCC         Evidence={ECO:0000305|PubMed:17050001};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:13.069958+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 83-86",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c6f3ea767f28b291172d1bff1e34f97db01c5d476a90a59f7196e827ba0e0fa9",
  "url": "https://rest.uniprot.org/unisave/Q9NBV4?format=txt&versions=62"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 54. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
