# catalytic_activity_0106

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/catalytic_activity_0106.txt)

**Task:** `catalytic_activity`  
**Expected answer:** **D** — folate(in) + H(+)(in) = folate(out) + H(+)(out)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MIEKSNNPFLSIDPIVERTKSNGEGLPLLSEKTKKGFDFTQIVVYLVGLSDGLTHLASLAIYYLFKDYFRLTPYQVSLILMYPYIPFILKPVIALITDSFSIFGMRRKPYLFLFSLFQSLNFLALAFLNLSVIQASLILFFISLCASFCTTVAEALVVESSMGQTYSQGTNKVTEFIASKAIGSLSVAYFSGYFLEKMPREYIFIATSIFPLIISLSCLFLKEKEYSTNRNIFNQLSDLIKFINTPIFLGPFLYIFVYMSGPDYDDAFFFFCTNKLGFRPSFMGTLRLTYGIASLIGIIIYRVFLKNCSLRKTLIITTLVSFPIYISPIILTEHINKFLGISNELFVLSGGFLIEAITEIQLLPLFILTANICQPGLEASVFATILSVKNLGSLTKKGTSSFITYLMKIDSYNFDNLSLYILTCGFFLLFSLTLVPLLPNEEHIEKLKNKETSKG

[Multiple Choices]
A. dopamine + S-adenosyl-L-methionine = 3-methoxytyramine + S-adenosyl-L-homocysteine + H(+)
B. mescaline + S-adenosyl-L-methionine = N-methylmescaline + S-adenosyl-L-homocysteine + H(+)
C. cholesterol(in) = cholesterol(out)
D. folate(in) + H(+)(in) = folate(out) + H(+)(out)
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

> The sequence-matched UniProt record annotates folate transport with the reaction in D, citing a publication; the archived record available by the historical cutoff gives the same annotation. This supports the key, though the annotation is literature-curated evidence rather than an independently assessed experiment here.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is a highly hydrophobic multipass membrane protein, consistent with a transporter rather than either SAM-dependent methyltransferase in A or B. More specifically, sequence-family/homology recognition can connect it to folate transporter proteins; transferable knowledge that this family transports folates distinguishes D from the cholesterol-transport alternative C. The topology alone would not establish the substrate, so the inference depends on family-level sequence recognition, not just hydrophobicity.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A credible transferable inference is available from transporter-family recognition and the known substrate of related proteins. This does not require knowing this exact protein's database entry, although substrate assignment from topology alone would be underdetermined.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The source also annotates transport of a methylated folate species, but no separate option for that reaction is offered; it does not make the cholesterol or methyltransferase choices equally defensible.


### Important caveats

- The sequence and source identity match, but the cited literature was not independently reviewed here.
- The source also lists transport of (6S)-5-methyl-tetrahydrofolate, so D represents a broad folate transport reaction rather than the only annotated folate substrate.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is a highly hydrophobic multipass membrane protein, consistent with a transporter rather than either SAM-dependent methyltransferase in A or B. More specifically, sequence-family/homology recognition can connect it to folate transporter proteins; transferable knowledge that this family transports folates distinguishes D from the cholesterol-transport alternative C. The topology alone would not establish the substrate, so the inference depends on family-level sequence recognition, not just hydrophobicity.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A credible transferable inference is available from transporter-family recognition and the known substrate of related proteins. This does not require knowing this exact protein's database entry, although substrate assignment from topology alone would be underdetermined."
  },
  "case_id": "catalytic_activity_0106",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates folate transport with the reaction in D, citing a publication; the archived record available by the historical cutoff gives the same annotation. This supports the key, though the annotation is literature-curated evidence rather than an independently assessed experiment here."
  },
  "important_caveats": [
    "The sequence and source identity match, but the cited literature was not independently reviewed here.",
    "The source also lists transport of (6S)-5-methyl-tetrahydrofolate, so D represents a broad folate transport reaction rather than the only annotated folate substrate."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The source also annotates transport of a methylated folate species, but no separate option for that reaction is offered; it does not make the cholesterol or methyltransferase choices equally defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0106",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates folate transport with the reaction in D, citing a publication; the archived record available by the historical cutoff gives the same annotation. This supports the key, though the annotation is literature-curated evidence rather than an independently assessed experiment here.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is a highly hydrophobic multipass membrane protein, consistent with a transporter rather than either SAM-dependent methyltransferase in A or B. More specifically, sequence-family/homology recognition can connect it to folate transporter proteins; transferable knowledge that this family transports folates distinguishes D from the cholesterol-transport alternative C. The topology alone would not establish the substrate, so the inference depends on family-level sequence recognition, not just hydrophobicity.",
    "missing_item_specific_fact": "",
    "reason": "A credible transferable inference is available from transporter-family recognition and the known substrate of related proteins. This does not require knowing this exact protein's database entry, although substrate assignment from topology alone would be underdetermined."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The source also annotates transport of a methylated folate species, but no separate option for that reaction is offered; it does not make the cholesterol or methyltransferase choices equally defensible."
  },
  "important_caveats": [
    "The sequence and source identity match, but the cited literature was not independently reviewed here.",
    "The source also lists transport of (6S)-5-methyl-tetrahydrofolate, so D represents a broad folate transport reaction rather than the only annotated folate substrate."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q8IIK1 (FT2_PLAF7, Folate transporter 2 from Plasmodium falciparum) is annotated with the exact catalytic activity 'folate(in) + H(+)(in) = folate(out) + H(+)(out)' (RHEA:70159), supported by experimental evidence (ECO:0000305, PubMed:21998306). The benchmark sequence (455 aa) matches the source sequence exactly. The annotation is backed by a 2011 JBC functional characterization paper.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4), [C7](#evidence-c7), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 455-aa sequence is dominated by numerous hydrophobic stretches (~10-12+ transmembrane helices), clearly identifying it as a polytopic membrane transporter rather than a soluble enzyme. This immediately eliminates choices A and B, which describe soluble methyltransferase (COMT-type) reactions on small molecules. Between C (cholesterol transport) and D (folate transport): major cholesterol transporters (NPC1 ~1300 aa, ABCA1 ~2261 aa, ABCG5/8 ~651 aa) are substantially larger than 455 aa, whereas the MFS (Major Facilitator Superfamily) fold—which includes folate transporters such as RFC/SLC19A1, PCFT/SLC46A1, and microbial folate transporters—typically comprises ~400-500 aa with 11-12 TM helices in a characteristic 6+6 inverted-repeat topology. The observed sequence length and TM topology are highly consistent with an MFS-type folate transporter. The proton-coupled nature of the reaction in D (H+ co-transport) is also a hallmark of MFS folate transporters (e.g., PCFT), whereas simple cholesterol equilibration (choice C) does not involve a proton gradient. Thus, transferable knowledge of MFS family architecture, size constraints of known cholesterol transporters, and proton-coupled transport mechanisms meaningfully distinguishes D from the other three options.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can use (1) membrane topology to eliminate soluble-enzyme options A and B, (2) protein size (~455 aa) and MFS-fold topology to favor folate transport over cholesterol transport (which requires much larger proteins), and (3) the proton-coupled reaction format to further support MFS folate transporter identity. These are standard transferable inferences from protein-family knowledge.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> A and B are clearly eliminated by the polytopic membrane topology. C is disfavored by the size constraint (455 aa is far too small for known cholesterol transporters) and the proton-coupled reaction format. D is the only option consistent with the observed MFS-like architecture, size, and proton-coupled transport mechanism.


### Important caveats

- The reviewer-only evidence confirms the target as Plasmodium falciparum Folate transporter 2 (PfFT2), but organism identity was not provided to the evaluated model. The reasoning above relies only on sequence features and general family knowledge.
- The MFS folate transporter inference is probabilistic: the sequence length and topology are consistent with MFS but do not constitute a definitive fold prediction without structural data. However, among the four offered choices, this inference meaningfully and credibly selects D.
- The annotation evidence code is ECO:0000305 (inferred from direct assay), indicating experimental support from the 2011 JBC paper, not merely computational transfer.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 455-aa sequence is dominated by numerous hydrophobic stretches (~10-12+ transmembrane helices), clearly identifying it as a polytopic membrane transporter rather than a soluble enzyme. This immediately eliminates choices A and B, which describe soluble methyltransferase (COMT-type) reactions on small molecules. Between C (cholesterol transport) and D (folate transport): major cholesterol transporters (NPC1 ~1300 aa, ABCA1 ~2261 aa, ABCG5/8 ~651 aa) are substantially larger than 455 aa, whereas the MFS (Major Facilitator Superfamily) fold—which includes folate transporters such as RFC/SLC19A1, PCFT/SLC46A1, and microbial folate transporters—typically comprises ~400-500 aa with 11-12 TM helices in a characteristic 6+6 inverted-repeat topology. The observed sequence length and TM topology are highly consistent with an MFS-type folate transporter. The proton-coupled nature of the reaction in D (H+ co-transport) is also a hallmark of MFS folate transporters (e.g., PCFT), whereas simple cholesterol equilibration (choice C) does not involve a proton gradient. Thus, transferable knowledge of MFS family architecture, size constraints of known cholesterol transporters, and proton-coupled transport mechanisms meaningfully distinguishes D from the other three options.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use (1) membrane topology to eliminate soluble-enzyme options A and B, (2) protein size (~455 aa) and MFS-fold topology to favor folate transport over cholesterol transport (which requires much larger proteins), and (3) the proton-coupled reaction format to further support MFS folate transporter identity. These are standard transferable inferences from protein-family knowledge."
  },
  "case_id": "catalytic_activity_0106",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4",
      "C7",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q8IIK1 (FT2_PLAF7, Folate transporter 2 from Plasmodium falciparum) is annotated with the exact catalytic activity 'folate(in) + H(+)(in) = folate(out) + H(+)(out)' (RHEA:70159), supported by experimental evidence (ECO:0000305, PubMed:21998306). The benchmark sequence (455 aa) matches the source sequence exactly. The annotation is backed by a 2011 JBC functional characterization paper."
  },
  "important_caveats": [
    "The reviewer-only evidence confirms the target as Plasmodium falciparum Folate transporter 2 (PfFT2), but organism identity was not provided to the evaluated model. The reasoning above relies only on sequence features and general family knowledge.",
    "The MFS folate transporter inference is probabilistic: the sequence length and topology are consistent with MFS but do not constitute a definitive fold prediction without structural data. However, among the four offered choices, this inference meaningfully and credibly selects D.",
    "The annotation evidence code is ECO:0000305 (inferred from direct assay), indicating experimental support from the 2011 JBC paper, not merely computational transfer."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "A and B are clearly eliminated by the polytopic membrane topology. C is disfavored by the size constraint (455 aa is far too small for known cholesterol transporters) and the proton-coupled reaction format. D is the only option consistent with the observed MFS-like architecture, size, and proton-coupled transport mechanism."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0106",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q8IIK1 (FT2_PLAF7, Folate transporter 2 from Plasmodium falciparum) is annotated with the exact catalytic activity 'folate(in) + H(+)(in) = folate(out) + H(+)(out)' (RHEA:70159), supported by experimental evidence (ECO:0000305, PubMed:21998306). The benchmark sequence (455 aa) matches the source sequence exactly. The annotation is backed by a 2011 JBC functional characterization paper.",
    "evidence_ids": ["C5", "H4", "C7", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 455-aa sequence is dominated by numerous hydrophobic stretches (~10-12+ transmembrane helices), clearly identifying it as a polytopic membrane transporter rather than a soluble enzyme. This immediately eliminates choices A and B, which describe soluble methyltransferase (COMT-type) reactions on small molecules. Between C (cholesterol transport) and D (folate transport): major cholesterol transporters (NPC1 ~1300 aa, ABCA1 ~2261 aa, ABCG5/8 ~651 aa) are substantially larger than 455 aa, whereas the MFS (Major Facilitator Superfamily) fold—which includes folate transporters such as RFC/SLC19A1, PCFT/SLC46A1, and microbial folate transporters—typically comprises ~400-500 aa with 11-12 TM helices in a characteristic 6+6 inverted-repeat topology. The observed sequence length and TM topology are highly consistent with an MFS-type folate transporter. The proton-coupled nature of the reaction in D (H+ co-transport) is also a hallmark of MFS folate transporters (e.g., PCFT), whereas simple cholesterol equilibration (choice C) does not involve a proton gradient. Thus, transferable knowledge of MFS family architecture, size constraints of known cholesterol transporters, and proton-coupled transport mechanisms meaningfully distinguishes D from the other three options.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use (1) membrane topology to eliminate soluble-enzyme options A and B, (2) protein size (~455 aa) and MFS-fold topology to favor folate transport over cholesterol transport (which requires much larger proteins), and (3) the proton-coupled reaction format to further support MFS folate transporter identity. These are standard transferable inferences from protein-family knowledge."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "A and B are clearly eliminated by the polytopic membrane topology. C is disfavored by the size constraint (455 aa is far too small for known cholesterol transporters) and the proton-coupled reaction format. D is the only option consistent with the observed MFS-like architecture, size, and proton-coupled transport mechanism."
  },
  "important_caveats": [
    "The reviewer-only evidence confirms the target as Plasmodium falciparum Folate transporter 2 (PfFT2), but organism identity was not provided to the evaluated model. The reasoning above relies only on sequence features and general family knowledge.",
    "The MFS folate transporter inference is probabilistic: the sequence length and topology are consistent with MFS but do not constitute a definitive fold prediction without structural data. However, among the four offered choices, this inference meaningfully and credibly selects D.",
    "The annotation evidence code is ECO:0000305 (inferred from direct assay), indicating experimental support from the 2011 JBC paper, not merely computational transfer."
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
  "benchmark_sequence_length": 455,
  "benchmark_sequence_sha256": "6872668a1169d79c41e0e3217c7a0afaf399201ad1db1edc0cc760ca366b5635",
  "current_entry_audit": {
    "entryVersion": 109,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2003-03-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "8631bdcc6b7274da8651ba15077787a2ccc347d9d53951e8b63a7d9807d07940",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 455,
  "current_source_sequence_sha256": "6872668a1169d79c41e0e3217c7a0afaf399201ad1db1edc0cc760ca366b5635",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 107,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q8IIK1",
  "selected_historical_entry_version": 107,
  "selected_historical_record_sha256": "c315cecd25012a01e06e0aefb68dd205d1cf053c48966bc36b4c33d3c6385707",
  "selected_historical_source_sequence_length": 455,
  "selected_historical_source_sequence_sha256": "6872668a1169d79c41e0e3217c7a0afaf399201ad1db1edc0cc760ca366b5635",
  "selected_historical_version": {
    "accession": "Q8IIK1",
    "database": "Swiss-Prot",
    "entryVersion": 107,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "FT2_PLAF7",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IIK1.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q8IIK1\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:24.989052+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8631bdcc6b7274da8651ba15077787a2ccc347d9d53951e8b63a7d9807d07940",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IIK1.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IIK1.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":109,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2003-03-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:24.989052+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8631bdcc6b7274da8651ba15077787a2ccc347d9d53951e8b63a7d9807d07940",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IIK1.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IIK1.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000001450\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Sar\",\"Alveolata\",\"Apicomplexa\",\"Aconoidasida\",\"Haemosporida\",\"Plasmodiidae\",\"Plasmodium\",\"Laverania\"],\"scientificName\":\"Plasmodium falciparum (isolate 3D7)\",\"taxonId\":36329}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:24.989052+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8631bdcc6b7274da8651ba15077787a2ccc347d9d53951e8b63a7d9807d07940",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IIK1.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IIK1.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"21998306\",\"source\":\"PubMed\"}],\"value\":\"Folate transporter 2\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"21998306\",\"source\":\"PubMed\"}],\"value\":\"PfFT2\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:24.989052+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8631bdcc6b7274da8651ba15077787a2ccc347d9d53951e8b63a7d9807d07940",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IIK1.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IIK1.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"21998306\",\"source\":\"PubMed\"}],\"name\":\"folate(in) + H(+)(in) = folate(out) + H(+)(out)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:70159\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:62501\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-01T06:25:24.989052+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8631bdcc6b7274da8651ba15077787a2ccc347d9d53951e8b63a7d9807d07940",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IIK1.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IIK1.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"21998306\",\"source\":\"PubMed\"}],\"name\":\"(6S)-5-methyl-5,6,7,8-tetrahydrofolate(in) + H(+)(in) = (6S)-5-methyl-5,6,7,8-tetrahydrofolate(out) + H(+)(out)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:70167\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:18608\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-01T06:25:24.989052+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8631bdcc6b7274da8651ba15077787a2ccc347d9d53951e8b63a7d9807d07940",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IIK1.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IIK1.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Salcedo-Sora J.E.\",\"Ochong E.\",\"Beveridge S.\",\"Johnson D.\",\"Nzila A.\",\"Biagini G.A.\",\"Stocks P.A.\",\"O'Neill P.M.\",\"Krishna S.\",\"Bray P.G.\",\"Ward S.A.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"21998306\"},{\"database\":\"DOI\",\"id\":\"10.1074/jbc.m111.286054\"}],\"citationType\":\"journal article\",\"firstPage\":\"44659\",\"id\":\"21998306\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"44668\",\"publicationDate\":\"2011\",\"title\":\"The molecular basis of folate salvage in Plasmodium falciparum: characterization of two folate transporters.\",\"volume\":\"286\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"TRANSPORTER ACTIVITY\",\"ACTIVITY REGULATION\",\"SUBCELLULAR LOCATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-01T06:25:24.989052+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8631bdcc6b7274da8651ba15077787a2ccc347d9d53951e8b63a7d9807d07940",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IIK1.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IIK1?format=txt&versions=107)

```json
{
  "entry_version": 107,
  "evidence_id": "H1",
  "excerpt": "ID   FT2_PLAF7               Reviewed;         455 AA.\nAC   Q8IIK1;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-MAR-2003, sequence version 1.\nDT   28-JAN-2026, entry version 107.\nDE   RecName: Full=Folate transporter 2 {ECO:0000303|PubMed:21998306};\nDE            Short=PfFT2 {ECO:0000303|PubMed:21998306};\nGN   ORFNames=PF3D7_1116500 {ECO:0000312|EMBL:CZT98826.1};\nOS   Plasmodium falciparum (isolate 3D7).\nOC   Eukaryota; Sar; Alveolata; Apicomplexa; Aconoidasida; Haemosporida;\nOC   Plasmodiidae; Plasmodium; Plasmodium (Laverania).\nOX   NCBI_TaxID=36329 {ECO:0000312|Proteomes:UP000001450};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:40.005689+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-12",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c315cecd25012a01e06e0aefb68dd205d1cf053c48966bc36b4c33d3c6385707",
  "url": "https://rest.uniprot.org/unisave/Q8IIK1?format=txt&versions=107"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IIK1?format=txt&versions=107)

```json
{
  "entry_version": 107,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Folate transporter 2 {ECO:0000303|PubMed:21998306};\nDE            Short=PfFT2 {ECO:0000303|PubMed:21998306};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:40.005689+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-7",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c315cecd25012a01e06e0aefb68dd205d1cf053c48966bc36b4c33d3c6385707",
  "url": "https://rest.uniprot.org/unisave/Q8IIK1?format=txt&versions=107"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IIK1?format=txt&versions=107)

```json
{
  "entry_version": 107,
  "evidence_id": "H3",
  "excerpt": "RN   [2] {ECO:0000305}\nRP   FUNCTION, TRANSPORTER ACTIVITY, ACTIVITY REGULATION, AND SUBCELLULAR\nRP   LOCATION.\nRX   PubMed=21998306; DOI=10.1074/jbc.m111.286054;\nRA   Salcedo-Sora J.E., Ochong E., Beveridge S., Johnson D., Nzila A.,\nRA   Biagini G.A., Stocks P.A., O'Neill P.M., Krishna S., Bray P.G., Ward S.A.;\nRT   \"The molecular basis of folate salvage in Plasmodium falciparum:\nRT   characterization of two folate transporters.\";\nRL   J. Biol. Chem. 286:44659-44668(2011).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:40.005689+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 27-35",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c315cecd25012a01e06e0aefb68dd205d1cf053c48966bc36b4c33d3c6385707",
  "url": "https://rest.uniprot.org/unisave/Q8IIK1?format=txt&versions=107"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IIK1?format=txt&versions=107)

```json
{
  "entry_version": 107,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=folate(in) + H(+)(in) = folate(out) + H(+)(out);\nCC         Xref=Rhea:RHEA:70159, ChEBI:CHEBI:15378, ChEBI:CHEBI:62501;\nCC         Evidence={ECO:0000305|PubMed:21998306};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:40.005689+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 42-45",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c315cecd25012a01e06e0aefb68dd205d1cf053c48966bc36b4c33d3c6385707",
  "url": "https://rest.uniprot.org/unisave/Q8IIK1?format=txt&versions=107"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IIK1?format=txt&versions=107)

```json
{
  "entry_version": 107,
  "evidence_id": "H5",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=(6S)-5-methyl-5,6,7,8-tetrahydrofolate(in) + H(+)(in) = (6S)-\nCC         5-methyl-5,6,7,8-tetrahydrofolate(out) + H(+)(out);\nCC         Xref=Rhea:RHEA:70167, ChEBI:CHEBI:15378, ChEBI:CHEBI:18608;\nCC         Evidence={ECO:0000305|PubMed:21998306};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:40.005689+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 46-50",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c315cecd25012a01e06e0aefb68dd205d1cf053c48966bc36b4c33d3c6385707",
  "url": "https://rest.uniprot.org/unisave/Q8IIK1?format=txt&versions=107"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 106. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
