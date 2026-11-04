# cofactor_0086

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/cofactor_0086.txt)

**Task:** `cofactor`  
**Expected answer:** **A** — heme

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | Unusable review | Unusable review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MSKPAAAAPSDPSKPSKPLKEVPGSYGLPVLGAVKDRLDFYWFQGDTEFFRIRMEQHKSTVFRVNYSPGPPGYPDSRGIILLDQKSFSVLLDNSKVDKSDTLLGPYIPNLAFTGGYRVLPYLDTSEAKHTAYKDLIFELLHVNSSRIIPEYNKVFAETAGSWEERIAKSGKAEVFASSDSMITKFLLRTIVHKDPAEPGPASLGPKFRDTYQLWTGVNFAGIAHTPLPHFLEELLFHTFRLPPFLVKKQYKALANFYRTHATEVLDLAEKKYGLDREETVHQLILILGINARLGLHKMIPALIYYLGLLGEDFQAKIAAEVRSAVHKNRAQGEEGVNITTQALLEMPLLRSTVLETLRLTPSIFYIYGRAREDMVIESHDAAFQIKKGELLGGHQYFVMRDPEVFEEPHKFVADRFLGERGKAVLPYLVWSNGRETESPSSSNKQCPAKDVAELITMQFVAEMFLRYDSFEITKDSFINTTELNVHLKSLKKRSV

[Multiple Choices]
A. heme
B. Mg(2+)
C. cob(II)alamin
D. Mn(2+)
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Predicting Protein Cofactor, which is to identify the specific cofactor required for a given protein's catalytic activity. A cofactor is a non-protein chemical compound or metallic ion that is essential for an enzyme's function. Based on the provided protein sequence, you will need to determine which of the multiple-choice options is the correct cofactor.. The inputs provided by the user for this task include:

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

**Saved status:** `invalid_review`.

**This response is not a usable structured review.** Its saved text is preserved below; any labels in that text are excluded from the summary counts.

**Validation errors:** `invalid_json:Expecting property name enclosed in double quotes: line 13 column 3 (char 1144)`.

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0086",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates heme as the cofactor, but the evidence is transferred by similarity from another UniProt entry (ECO:0000250), not direct experimental evidence for this exact protein in the excerpts. This supports the key with that qualification.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "A knowledgeable model could use sequence-profile or homology knowledge to recognize this as belonging to a plant cytochrome P450-type enzyme family. P450 enzymes use a heme catalytic center, making heme a meaningful choice over Mg(2+), Mn(2+), or cob(II)alamin. This is a family-level inference, not a guarantee based on an obvious single motif.",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge of P450-family sequences and their heme-dependent chemistry provides a credible basis for distinguishing heme among these options without recalling this exact protein's database record.",
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The offered alternatives distinguish heme from unrelated metal-ion and cobalamin cofactors; no second choice is comparably supported."
  },
  "important_caveats": [
    "The supplied source evidence supports heme by a similarity-based annotation; the excerpts do not establish direct experimental verification for this exact protein."
  ]
}
```

</details>

**Saved parsed visible review:** `null`.

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation (C5, H4) explicitly lists heme (ChEBI:CHEBI:30413) as the cofactor for this protein (Divinyl ether synthase CYP74M3, a cytochrome P450). The evidence code ECO:0000250 indicates transfer by similarity from Q96242, but this is entirely consistent with the universal, defining property of the cytochrome P450 superfamily: all P450 enzymes use heme (iron-protoporphyrin IX) as their prosthetic group. The protein is confirmed as a CYP74 family member (EC 4.2.1.183) by experimental characterization (PubMed:26776054, C6/H3).

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4), [C4](#evidence-c4), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence (~495 aa) exhibits hallmarks of the cytochrome P450 superfamily: appropriate length for a P450, conserved regions consistent with the P450 fold (e.g., the 'FAG' region in 'WTGVNFAGIAHTPLPHF' near the heme-binding pocket, the I-helix 'AG' motif, and the overall domain architecture). The CYP nomenclature and P450 sequence signature are among the most recognizable and universally conserved features in biochemistry. The defining, universal property of ALL cytochrome P450 enzymes is the use of heme (Fe-protoporphyrin IX) as their cofactor/prosthetic group — this is not a probabilistic association but a structural and mechanistic necessity (the heme iron performs substrate oxidation). The other options (Mg²⁺, cob(II)alamin, Mn²⁺) are cofactors for entirely different enzyme classes (kinases/polymerases, methyltransferases/isomerases, and certain oxidoreductases/SODs respectively) and are never associated with P450 enzymes. Thus, recognizing the P450 family from sequence features and applying the universal P450→heme rule meaningfully and decisively distinguishes option A from B, C, and D.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The inference relies on well-established, transferable family-level knowledge: (1) recognizing cytochrome P450 sequence features from the provided sequence, and (2) applying the universal, textbook fact that all P450 enzymes require heme. This does not require knowing the specific annotation for this exact Selaginella protein. The P450-heme connection is one of the most fundamental and universally taught facts in enzymology.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Once the protein is recognized as a cytochrome P450 (which the sequence supports through conserved motifs and architecture), heme is the only defensible cofactor among the four options. Mg²⁺, cob(II)alamin, and Mn²⁺ have no association with P450 enzymes. There is no meaningful ambiguity.


### Important caveats

- The UniProt cofactor annotation uses ECO:0000250 (inferred by similarity from Q96242), not direct experimental determination for this specific protein. However, the P450-heme connection is a universal family property, making this transfer entirely reliable.
- The exact heme-binding motif (FxxGxxxCxG) is somewhat degenerate in plant P450s; the Cys ligand in this sequence appears in the context 'KQCPAKD' rather than the textbook-perfect motif, but the overall P450 architecture is maintained.
- The reviewer-only evidence (UniProt accession, organism, protein name) was not available to the evaluated model; the reasoning must rely solely on sequence features and general P450 biology.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence (~495 aa) exhibits hallmarks of the cytochrome P450 superfamily: appropriate length for a P450, conserved regions consistent with the P450 fold (e.g., the 'FAG' region in 'WTGVNFAGIAHTPLPHF' near the heme-binding pocket, the I-helix 'AG' motif, and the overall domain architecture). The CYP nomenclature and P450 sequence signature are among the most recognizable and universally conserved features in biochemistry. The defining, universal property of ALL cytochrome P450 enzymes is the use of heme (Fe-protoporphyrin IX) as their cofactor/prosthetic group — this is not a probabilistic association but a structural and mechanistic necessity (the heme iron performs substrate oxidation). The other options (Mg²⁺, cob(II)alamin, Mn²⁺) are cofactors for entirely different enzyme classes (kinases/polymerases, methyltransferases/isomerases, and certain oxidoreductases/SODs respectively) and are never associated with P450 enzymes. Thus, recognizing the P450 family from sequence features and applying the universal P450→heme rule meaningfully and decisively distinguishes option A from B, C, and D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The inference relies on well-established, transferable family-level knowledge: (1) recognizing cytochrome P450 sequence features from the provided sequence, and (2) applying the universal, textbook fact that all P450 enzymes require heme. This does not require knowing the specific annotation for this exact Selaginella protein. The P450-heme connection is one of the most fundamental and universally taught facts in enzymology."
  },
  "case_id": "cofactor_0086",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4",
      "C4",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation (C5, H4) explicitly lists heme (ChEBI:CHEBI:30413) as the cofactor for this protein (Divinyl ether synthase CYP74M3, a cytochrome P450). The evidence code ECO:0000250 indicates transfer by similarity from Q96242, but this is entirely consistent with the universal, defining property of the cytochrome P450 superfamily: all P450 enzymes use heme (iron-protoporphyrin IX) as their prosthetic group. The protein is confirmed as a CYP74 family member (EC 4.2.1.183) by experimental characterization (PubMed:26776054, C6/H3)."
  },
  "important_caveats": [
    "The UniProt cofactor annotation uses ECO:0000250 (inferred by similarity from Q96242), not direct experimental determination for this specific protein. However, the P450-heme connection is a universal family property, making this transfer entirely reliable.",
    "The exact heme-binding motif (FxxGxxxCxG) is somewhat degenerate in plant P450s; the Cys ligand in this sequence appears in the context 'KQCPAKD' rather than the textbook-perfect motif, but the overall P450 architecture is maintained.",
    "The reviewer-only evidence (UniProt accession, organism, protein name) was not available to the evaluated model; the reasoning must rely solely on sequence features and general P450 biology."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Once the protein is recognized as a cytochrome P450 (which the sequence supports through conserved motifs and architecture), heme is the only defensible cofactor among the four options. Mg²⁺, cob(II)alamin, and Mn²⁺ have no association with P450 enzymes. There is no meaningful ambiguity."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0086",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation (C5, H4) explicitly lists heme (ChEBI:CHEBI:30413) as the cofactor for this protein (Divinyl ether synthase CYP74M3, a cytochrome P450). The evidence code ECO:0000250 indicates transfer by similarity from Q96242, but this is entirely consistent with the universal, defining property of the cytochrome P450 superfamily: all P450 enzymes use heme (iron-protoporphyrin IX) as their prosthetic group. The protein is confirmed as a CYP74 family member (EC 4.2.1.183) by experimental characterization (PubMed:26776054, C6/H3).",
    "evidence_ids": ["C5", "H4", "C4", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence (~495 aa) exhibits hallmarks of the cytochrome P450 superfamily: appropriate length for a P450, conserved regions consistent with the P450 fold (e.g., the 'FAG' region in 'WTGVNFAGIAHTPLPHF' near the heme-binding pocket, the I-helix 'AG' motif, and the overall domain architecture). The CYP nomenclature and P450 sequence signature are among the most recognizable and universally conserved features in biochemistry. The defining, universal property of ALL cytochrome P450 enzymes is the use of heme (Fe-protoporphyrin IX) as their cofactor/prosthetic group — this is not a probabilistic association but a structural and mechanistic necessity (the heme iron performs substrate oxidation). The other options (Mg²⁺, cob(II)alamin, Mn²⁺) are cofactors for entirely different enzyme classes (kinases/polymerases, methyltransferases/isomerases, and certain oxidoreductases/SODs respectively) and are never associated with P450 enzymes. Thus, recognizing the P450 family from sequence features and applying the universal P450→heme rule meaningfully and decisively distinguishes option A from B, C, and D.",
    "missing_item_specific_fact": "",
    "reason": "The inference relies on well-established, transferable family-level knowledge: (1) recognizing cytochrome P450 sequence features from the provided sequence, and (2) applying the universal, textbook fact that all P450 enzymes require heme. This does not require knowing the specific annotation for this exact Selaginella protein. The P450-heme connection is one of the most fundamental and universally taught facts in enzymology."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Once the protein is recognized as a cytochrome P450 (which the sequence supports through conserved motifs and architecture), heme is the only defensible cofactor among the four options. Mg²⁺, cob(II)alamin, and Mn²⁺ have no association with P450 enzymes. There is no meaningful ambiguity."
  },
  "important_caveats": [
    "The UniProt cofactor annotation uses ECO:0000250 (inferred by similarity from Q96242), not direct experimental determination for this specific protein. However, the P450-heme connection is a universal family property, making this transfer entirely reliable.",
    "The exact heme-binding motif (FxxGxxxCxG) is somewhat degenerate in plant P450s; the Cys ligand in this sequence appears in the context 'KQCPAKD' rather than the textbook-perfect motif, but the overall P450 architecture is maintained.",
    "The reviewer-only evidence (UniProt accession, organism, protein name) was not available to the evaluated model; the reasoning must rely solely on sequence features and general P450 biology."
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
  "benchmark_sequence_length": 495,
  "benchmark_sequence_sha256": "0b22ddba73dd0ac278bf9cedf5b7de50ecaf7f1f1efc3e1bef923293962e731d",
  "current_entry_audit": {
    "entryVersion": 70,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2010-10-05",
    "sequenceVersion": 1
  },
  "current_record_sha256": "bbcc4fc0f0a6a06bea7928590de148b29c4a9f23d154d0013d30b0e3b948d201",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 495,
  "current_source_sequence_sha256": "0b22ddba73dd0ac278bf9cedf5b7de50ecaf7f1f1efc3e1bef923293962e731d",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 68,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "D8QZ31",
  "selected_historical_entry_version": 68,
  "selected_historical_record_sha256": "446460c71bbb00249dbc4f4d90a0a588e3143add26550ba5b1c5802db8e21cdd",
  "selected_historical_source_sequence_length": 495,
  "selected_historical_source_sequence_sha256": "0b22ddba73dd0ac278bf9cedf5b7de50ecaf7f1f1efc3e1bef923293962e731d",
  "selected_historical_version": {
    "accession": "D8QZ31",
    "database": "Swiss-Prot",
    "entryVersion": 68,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "C74M3_SELML",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D8QZ31.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"D8QZ31\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:27:50.224082+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bbcc4fc0f0a6a06bea7928590de148b29c4a9f23d154d0013d30b0e3b948d201",
  "url": "https://rest.uniprot.org/uniprotkb/D8QZ31.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D8QZ31.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":70,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2010-10-05\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:27:50.224082+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bbcc4fc0f0a6a06bea7928590de148b29c4a9f23d154d0013d30b0e3b948d201",
  "url": "https://rest.uniprot.org/uniprotkb/D8QZ31.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D8QZ31.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Gemmiferous spikemoss\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Lycopodiopsida\",\"Selaginellales\",\"Selaginellaceae\",\"Selaginelloideae\",\"Selaginella\"],\"scientificName\":\"Selaginella moellendorffii\",\"synonyms\":[\"Kungiselaginella moellendorffii\"],\"taxonId\":88036}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:27:50.224082+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bbcc4fc0f0a6a06bea7928590de148b29c4a9f23d154d0013d30b0e3b948d201",
  "url": "https://rest.uniprot.org/uniprotkb/D8QZ31.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D8QZ31.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"26776054\",\"source\":\"PubMed\"}],\"value\":\"4.2.1.183\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"26776054\",\"source\":\"PubMed\"}],\"value\":\"Etheroleic acid synthase CYP74M3\"}}],\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"26776054\",\"source\":\"PubMed\"}],\"value\":\"Divinyl ether synthase CYP74M3\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:27:50.224082+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bbcc4fc0f0a6a06bea7928590de148b29c4a9f23d154d0013d30b0e3b948d201",
  "url": "https://rest.uniprot.org/uniprotkb/D8QZ31.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D8QZ31.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:30413\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q96242\",\"source\":\"UniProtKB\"}],\"name\":\"heme\"}],\"commentType\":\"COFACTOR\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-02T04:27:50.224082+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bbcc4fc0f0a6a06bea7928590de148b29c4a9f23d154d0013d30b0e3b948d201",
  "url": "https://rest.uniprot.org/uniprotkb/D8QZ31.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D8QZ31.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Gorina S.S.\",\"Toporkova Y.Y.\",\"Mukhtarova L.S.\",\"Smirnova E.O.\",\"Chechetkin I.R.\",\"Khairutdinov B.I.\",\"Gogolev Y.V.\",\"Grechkin A.N.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"26776054\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.bbalip.2016.01.001\"}],\"citationType\":\"journal article\",\"firstPage\":\"301\",\"id\":\"26776054\",\"journal\":\"Biochim. Biophys. Acta\",\"lastPage\":\"309\",\"publicationDate\":\"2016\",\"title\":\"Oxylipin biosynthesis in spikemoss Selaginella moellendorffii: Molecular cloning and identification of divinyl ether synthases CYP74M1 and CYP74M3.\",\"volume\":\"1861\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:27:50.224082+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bbcc4fc0f0a6a06bea7928590de148b29c4a9f23d154d0013d30b0e3b948d201",
  "url": "https://rest.uniprot.org/uniprotkb/D8QZ31.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D8QZ31?format=txt&versions=68)

```json
{
  "entry_version": 68,
  "evidence_id": "H1",
  "excerpt": "ID   C74M3_SELML             Reviewed;         495 AA.\nAC   D8QZ31;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-OCT-2010, sequence version 1.\nDT   28-JAN-2026, entry version 68.\nDE   RecName: Full=Divinyl ether synthase CYP74M3 {ECO:0000303|PubMed:26776054};\nDE   AltName: Full=Etheroleic acid synthase CYP74M3 {ECO:0000305|PubMed:26776054};\nDE            EC=4.2.1.183 {ECO:0000269|PubMed:26776054};\nGN   Name=CYP74M3 {ECO:0000303|PubMed:26776054};\nGN   Synonyms=DES2 {ECO:0000303|PubMed:26776054};\nGN   ORFNames=SELMODRAFT_81998 {ECO:0000312|EMBL:EFJ34345.1};\nOS   Selaginella moellendorffii (Spikemoss).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Lycopodiopsida; Selaginellales; Selaginellaceae; Selaginella.\nOX   NCBI_TaxID=88036;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:52.203972+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "446460c71bbb00249dbc4f4d90a0a588e3143add26550ba5b1c5802db8e21cdd",
  "url": "https://rest.uniprot.org/unisave/D8QZ31?format=txt&versions=68"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D8QZ31?format=txt&versions=68)

```json
{
  "entry_version": 68,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Divinyl ether synthase CYP74M3 {ECO:0000303|PubMed:26776054};\nDE   AltName: Full=Etheroleic acid synthase CYP74M3 {ECO:0000305|PubMed:26776054};\nDE            EC=4.2.1.183 {ECO:0000269|PubMed:26776054};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:52.203972+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-8",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "446460c71bbb00249dbc4f4d90a0a588e3143add26550ba5b1c5802db8e21cdd",
  "url": "https://rest.uniprot.org/unisave/D8QZ31?format=txt&versions=68"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D8QZ31?format=txt&versions=68)

```json
{
  "entry_version": 68,
  "evidence_id": "H3",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, AND PATHWAY.\nRX   PubMed=26776054; DOI=10.1016/j.bbalip.2016.01.001;\nRA   Gorina S.S., Toporkova Y.Y., Mukhtarova L.S., Smirnova E.O.,\nRA   Chechetkin I.R., Khairutdinov B.I., Gogolev Y.V., Grechkin A.N.;\nRT   \"Oxylipin biosynthesis in spikemoss Selaginella moellendorffii: Molecular\nRT   cloning and identification of divinyl ether synthases CYP74M1 and\nRT   CYP74M3.\";\nRL   Biochim. Biophys. Acta 1861:301-309(2016).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:52.203972+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 40-48",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "446460c71bbb00249dbc4f4d90a0a588e3143add26550ba5b1c5802db8e21cdd",
  "url": "https://rest.uniprot.org/unisave/D8QZ31?format=txt&versions=68"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D8QZ31?format=txt&versions=68)

```json
{
  "entry_version": 68,
  "evidence_id": "H4",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=heme; Xref=ChEBI:CHEBI:30413;\nCC         Evidence={ECO:0000250|UniProtKB:Q96242};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:52.203972+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 70-72",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "446460c71bbb00249dbc4f4d90a0a588e3143add26550ba5b1c5802db8e21cdd",
  "url": "https://rest.uniprot.org/unisave/D8QZ31?format=txt&versions=68"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 86. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
