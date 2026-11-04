# catalytic_activity_0104

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/catalytic_activity_0104.txt)

**Task:** `catalytic_activity`  
**Expected answer:** **A** — 3-oxocapnine + NADPH + H(+) = capnine + NADP(+)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MRYAVVTGVSSGIGKAICEKFLAKGLYVFGSVRKKEDAKYFEEKYPNTFHTLVFDTTDYPAVDKAVEEIHKVVGKKGLSVLVNNAGVAKYGPIQHVPIEELRQQYEVNVFASVYLTQKLLWLLGASKEAKWQGKVIQISSTAGVMTRPMLGPYSSSKHAVEAIYDALRRELMIYGVEVVLIEPGPIKTEIWGKAKSGGNPYKDTDYGEIFAQLDKAVDEIEKIGLPVEAVAGKAWEAFVAKKPKARYVVAPKKLMFKAAMYLIPDRMLDKIFYKDLKKLTQES

[Multiple Choices]
A. 3-oxocapnine + NADPH + H(+) = capnine + NADP(+)
B. vomilenine = perakine
C. spirilloxanthin + 2 reduced [2Fe-2S]-[ferredoxin] + O2 + 2 H(+) = 2-hydroxyspirilloxanthin + 2 oxidized [2Fe-2S]-[ferredoxin] + H2O
D. 3-methoxytyramine + S-adenosyl-L-methionine = N-methyl-3-methoxytyramine + S-adenosyl-L-homocysteine + H(+)
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

> The sequence-matched UniProt entry annotates this protein as an NADPH-dependent 3-dehydrocapnine reductase and assigns the reaction in A, citing experimental evidence (ECO:0000269). This supports the key, though the cited primary study was not independently reviewed here.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence begins with a glycine-rich dinucleotide-binding-like motif (…TGVSSGIGK…), consistent with an NAD(P)-dependent oxidoreductase. Among the choices, A is an NADPH-driven reduction; B describes a rearrangement, C uses reduced ferredoxin and oxygen, and D is a SAM-dependent methylation. That transferable sequence/cofactor-class inference meaningfully favors A, although it does not by itself establish the specific capnine substrates.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The offered reactions differ in enzyme class and cofactor requirements, so the sequence’s oxidoreductase-like feature provides a meaningful distinction without requiring the exact protein’s recorded annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The options describe distinct reaction and cofactor classes; no second option is comparably supported by the sequence feature.


### Important caveats

- A glycine-rich dinucleotide-binding-like motif is suggestive, not sufficient to identify the exact substrate reaction.
- The annotation cites experimental evidence, but that primary evidence was not independently assessed.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence begins with a glycine-rich dinucleotide-binding-like motif (…TGVSSGIGK…), consistent with an NAD(P)-dependent oxidoreductase. Among the choices, A is an NADPH-driven reduction; B describes a rearrangement, C uses reduced ferredoxin and oxygen, and D is a SAM-dependent methylation. That transferable sequence/cofactor-class inference meaningfully favors A, although it does not by itself establish the specific capnine substrates.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The offered reactions differ in enzyme class and cofactor requirements, so the sequence’s oxidoreductase-like feature provides a meaningful distinction without requiring the exact protein’s recorded annotation."
  },
  "case_id": "catalytic_activity_0104",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry annotates this protein as an NADPH-dependent 3-dehydrocapnine reductase and assigns the reaction in A, citing experimental evidence (ECO:0000269). This supports the key, though the cited primary study was not independently reviewed here."
  },
  "important_caveats": [
    "A glycine-rich dinucleotide-binding-like motif is suggestive, not sufficient to identify the exact substrate reaction.",
    "The annotation cites experimental evidence, but that primary evidence was not independently assessed."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options describe distinct reaction and cofactor classes; no second option is comparably supported by the sequence feature."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0104",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry annotates this protein as an NADPH-dependent 3-dehydrocapnine reductase and assigns the reaction in A, citing experimental evidence (ECO:0000269). This supports the key, though the cited primary study was not independently reviewed here.",
    "evidence_ids": ["C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence begins with a glycine-rich dinucleotide-binding-like motif (…TGVSSGIGK…), consistent with an NAD(P)-dependent oxidoreductase. Among the choices, A is an NADPH-driven reduction; B describes a rearrangement, C uses reduced ferredoxin and oxygen, and D is a SAM-dependent methylation. That transferable sequence/cofactor-class inference meaningfully favors A, although it does not by itself establish the specific capnine substrates.",
    "missing_item_specific_fact": "",
    "reason": "The offered reactions differ in enzyme class and cofactor requirements, so the sequence’s oxidoreductase-like feature provides a meaningful distinction without requiring the exact protein’s recorded annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options describe distinct reaction and cofactor classes; no second option is comparably supported by the sequence feature."
  },
  "important_caveats": [
    "A glycine-rich dinucleotide-binding-like motif is suggestive, not sufficient to identify the exact substrate reaction.",
    "The annotation cites experimental evidence, but that primary evidence was not independently assessed."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A3R5XUE6 (CAPC_ORNRH, Ornithobacterium rhinotracheale) is experimentally annotated (ECO:0000269, PubMed:35414181) as NADPH-dependent 3-dehydrocapnine reductase with EC 1.1.1.-, and the catalytic activity is exactly '3-oxocapnine + NADPH + H(+) = capnine + NADP(+)', matching option A verbatim. The benchmark sequence matches the source sequence (283 aa, SHA-256 identical).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains hallmark motifs of the Short-chain Dehydrogenase/Reductase (SDR) superfamily: (1) N-terminal Rossmann-fold NAD(P)H-binding motif 'VVTGVSSGIG' (GxGxxG pattern), (2) the 'NAG' signature in 'LVNNAG', (3) the 'SSSK' motif in 'PYSSSK', and (4) catalytic-region features including a Tyr in 'HAVEAIYDALRREL' and a Lys in 'GKAKSGG'. SDRs are obligately NAD(P)H-dependent oxidoreductases. Among the four choices: A is an NADPH-dependent reductase (matches SDR cofactor and reaction class); B is an isomerase requiring no cofactor; C is a ferredoxin/O2-dependent hydroxylase (typical of P450s or Rieske oxygenases, not SDRs); D is a SAM-dependent methyltransferase. The SDR family identification, a highly conserved and well-characterized protein family learned from thousands of homologs, uniquely selects option A on the basis of cofactor requirement (NADPH) and reaction class (reduction of a keto group to a hydroxyl). The specific substrate 'capnine' need not be known; the cofactor and chemistry are determined by family membership.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Recognizing the SDR superfamily from conserved sequence motifs (Rossmann GxGxxG, NAG, SSSK, catalytic Tyr-Lys) is standard transferable knowledge across biochemistry. This family-level inference directly eliminates B (isomerase, no cofactor), C (ferredoxin/O2 hydroxylase, different enzyme class), and D (SAM methyltransferase), leaving A as the only NAD(P)H-dependent oxidoreductase. The argument does not require knowing this exact enzyme's substrate.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The SDR cofactor requirement (NAD(P)H) and reaction class (oxidoreductase) are incompatible with B (isomerase), C (ferredoxin/O2 hydroxylase), and D (methyltransferase). Only A is consistent with the family assignment.


### Important caveats

- The specific substrate identity (capnine vs. another keto-substrate) cannot be determined from sequence alone; however, among the offered choices only A matches the NADPH-dependent reductase chemistry implied by SDR family membership.
- The SDR catalytic tetrad (YxxxK-DxxxN) spacing in this sequence is not perfectly canonical, which is common in SDR subfamilies and does not undermine the family assignment based on the Rossmann, NAG, and SSSK motifs.
- The experimental annotation (ECO:0000269, PubMed:35414181) confirms the exact reaction, but the family-level inference is sufficient to select A among the given alternatives.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains hallmark motifs of the Short-chain Dehydrogenase/Reductase (SDR) superfamily: (1) N-terminal Rossmann-fold NAD(P)H-binding motif 'VVTGVSSGIG' (GxGxxG pattern), (2) the 'NAG' signature in 'LVNNAG', (3) the 'SSSK' motif in 'PYSSSK', and (4) catalytic-region features including a Tyr in 'HAVEAIYDALRREL' and a Lys in 'GKAKSGG'. SDRs are obligately NAD(P)H-dependent oxidoreductases. Among the four choices: A is an NADPH-dependent reductase (matches SDR cofactor and reaction class); B is an isomerase requiring no cofactor; C is a ferredoxin/O2-dependent hydroxylase (typical of P450s or Rieske oxygenases, not SDRs); D is a SAM-dependent methyltransferase. The SDR family identification, a highly conserved and well-characterized protein family learned from thousands of homologs, uniquely selects option A on the basis of cofactor requirement (NADPH) and reaction class (reduction of a keto group to a hydroxyl). The specific substrate 'capnine' need not be known; the cofactor and chemistry are determined by family membership.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Recognizing the SDR superfamily from conserved sequence motifs (Rossmann GxGxxG, NAG, SSSK, catalytic Tyr-Lys) is standard transferable knowledge across biochemistry. This family-level inference directly eliminates B (isomerase, no cofactor), C (ferredoxin/O2 hydroxylase, different enzyme class), and D (SAM methyltransferase), leaving A as the only NAD(P)H-dependent oxidoreductase. The argument does not require knowing this exact enzyme's substrate."
  },
  "case_id": "catalytic_activity_0104",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H4",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A3R5XUE6 (CAPC_ORNRH, Ornithobacterium rhinotracheale) is experimentally annotated (ECO:0000269, PubMed:35414181) as NADPH-dependent 3-dehydrocapnine reductase with EC 1.1.1.-, and the catalytic activity is exactly '3-oxocapnine + NADPH + H(+) = capnine + NADP(+)', matching option A verbatim. The benchmark sequence matches the source sequence (283 aa, SHA-256 identical)."
  },
  "important_caveats": [
    "The specific substrate identity (capnine vs. another keto-substrate) cannot be determined from sequence alone; however, among the offered choices only A matches the NADPH-dependent reductase chemistry implied by SDR family membership.",
    "The SDR catalytic tetrad (YxxxK-DxxxN) spacing in this sequence is not perfectly canonical, which is common in SDR subfamilies and does not undermine the family assignment based on the Rossmann, NAG, and SSSK motifs.",
    "The experimental annotation (ECO:0000269, PubMed:35414181) confirms the exact reaction, but the family-level inference is sufficient to select A among the given alternatives."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The SDR cofactor requirement (NAD(P)H) and reaction class (oxidoreductase) are incompatible with B (isomerase), C (ferredoxin/O2 hydroxylase), and D (methyltransferase). Only A is consistent with the family assignment."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0104",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A3R5XUE6 (CAPC_ORNRH, Ornithobacterium rhinotracheale) is experimentally annotated (ECO:0000269, PubMed:35414181) as NADPH-dependent 3-dehydrocapnine reductase with EC 1.1.1.-, and the catalytic activity is exactly '3-oxocapnine + NADPH + H(+) = capnine + NADP(+)', matching option A verbatim. The benchmark sequence matches the source sequence (283 aa, SHA-256 identical).",
    "evidence_ids": ["C4", "C5", "H4", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains hallmark motifs of the Short-chain Dehydrogenase/Reductase (SDR) superfamily: (1) N-terminal Rossmann-fold NAD(P)H-binding motif 'VVTGVSSGIG' (GxGxxG pattern), (2) the 'NAG' signature in 'LVNNAG', (3) the 'SSSK' motif in 'PYSSSK', and (4) catalytic-region features including a Tyr in 'HAVEAIYDALRREL' and a Lys in 'GKAKSGG'. SDRs are obligately NAD(P)H-dependent oxidoreductases. Among the four choices: A is an NADPH-dependent reductase (matches SDR cofactor and reaction class); B is an isomerase requiring no cofactor; C is a ferredoxin/O2-dependent hydroxylase (typical of P450s or Rieske oxygenases, not SDRs); D is a SAM-dependent methyltransferase. The SDR family identification, a highly conserved and well-characterized protein family learned from thousands of homologs, uniquely selects option A on the basis of cofactor requirement (NADPH) and reaction class (reduction of a keto group to a hydroxyl). The specific substrate 'capnine' need not be known; the cofactor and chemistry are determined by family membership.",
    "missing_item_specific_fact": "",
    "reason": "Recognizing the SDR superfamily from conserved sequence motifs (Rossmann GxGxxG, NAG, SSSK, catalytic Tyr-Lys) is standard transferable knowledge across biochemistry. This family-level inference directly eliminates B (isomerase, no cofactor), C (ferredoxin/O2 hydroxylase, different enzyme class), and D (SAM methyltransferase), leaving A as the only NAD(P)H-dependent oxidoreductase. The argument does not require knowing this exact enzyme's substrate."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The SDR cofactor requirement (NAD(P)H) and reaction class (oxidoreductase) are incompatible with B (isomerase), C (ferredoxin/O2 hydroxylase), and D (methyltransferase). Only A is consistent with the family assignment."
  },
  "important_caveats": [
    "The specific substrate identity (capnine vs. another keto-substrate) cannot be determined from sequence alone; however, among the offered choices only A matches the NADPH-dependent reductase chemistry implied by SDR family membership.",
    "The SDR catalytic tetrad (YxxxK-DxxxN) spacing in this sequence is not perfectly canonical, which is common in SDR subfamilies and does not undermine the family assignment based on the Rossmann, NAG, and SSSK motifs.",
    "The experimental annotation (ECO:0000269, PubMed:35414181) confirms the exact reaction, but the family-level inference is sufficient to select A among the given alternatives."
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
  "benchmark_sequence_length": 283,
  "benchmark_sequence_sha256": "c34636190c93b708ede11afe25d8f3e950d83ee164fe4651dffd58c7eb032d36",
  "current_entry_audit": {
    "entryVersion": 18,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2019-04-10",
    "sequenceVersion": 1
  },
  "current_record_sha256": "eeb98d69cf0b99fa39b7fc118681807f2518aa1d8a1eb2df8e1e31569d47b1c6",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 283,
  "current_source_sequence_sha256": "c34636190c93b708ede11afe25d8f3e950d83ee164fe4651dffd58c7eb032d36",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 16,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A3R5XUE6",
  "selected_historical_entry_version": 16,
  "selected_historical_record_sha256": "6775a10db7332809ed4375188f70ceb1072cc82dbd87c32150e6341b3a85c434",
  "selected_historical_source_sequence_length": 283,
  "selected_historical_source_sequence_sha256": "c34636190c93b708ede11afe25d8f3e950d83ee164fe4651dffd58c7eb032d36",
  "selected_historical_version": {
    "accession": "A0A3R5XUE6",
    "database": "Swiss-Prot",
    "entryVersion": 16,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "CAPC_ORNRH",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A3R5XUE6.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A3R5XUE6\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:24:46.269818+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "eeb98d69cf0b99fa39b7fc118681807f2518aa1d8a1eb2df8e1e31569d47b1c6",
  "url": "https://rest.uniprot.org/uniprotkb/A0A3R5XUE6.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A3R5XUE6.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":18,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2019-04-10\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:24:46.269818+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "eeb98d69cf0b99fa39b7fc118681807f2518aa1d8a1eb2df8e1e31569d47b1c6",
  "url": "https://rest.uniprot.org/uniprotkb/A0A3R5XUE6.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A3R5XUE6.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Bacteroidota\",\"Flavobacteriia\",\"Flavobacteriales\",\"Weeksellaceae\",\"Ornithobacterium\"],\"scientificName\":\"Ornithobacterium rhinotracheale\",\"taxonId\":28251}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:24:46.269818+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "eeb98d69cf0b99fa39b7fc118681807f2518aa1d8a1eb2df8e1e31569d47b1c6",
  "url": "https://rest.uniprot.org/uniprotkb/A0A3R5XUE6.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A3R5XUE6.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35414181\",\"source\":\"PubMed\"}],\"value\":\"1.1.1.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"35414181\",\"source\":\"PubMed\"}],\"value\":\"NADPH-dependent 3-dehydrocapnine reductase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:24:46.269818+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "eeb98d69cf0b99fa39b7fc118681807f2518aa1d8a1eb2df8e1e31569d47b1c6",
  "url": "https://rest.uniprot.org/uniprotkb/A0A3R5XUE6.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A3R5XUE6.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35414181\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:81576\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35414181\",\"source\":\"PubMed\"}],\"name\":\"3-oxocapnine + NADPH + H(+) = capnine + NADP(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:81575\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57783\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231947\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231953\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-01T06:24:46.269818+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "eeb98d69cf0b99fa39b7fc118681807f2518aa1d8a1eb2df8e1e31569d47b1c6",
  "url": "https://rest.uniprot.org/uniprotkb/A0A3R5XUE6.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A3R5XUE6.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Liu Y.\",\"Wei Y.\",\"Teh T.M.\",\"Liu D.\",\"Zhou Y.\",\"Zhao S.\",\"Ang E.L.\",\"Zhao H.\",\"Zhang Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"35414181\"},{\"database\":\"DOI\",\"id\":\"10.1021/acs.biochem.2c00102\"}],\"citationType\":\"journal article\",\"firstPage\":\"2861\",\"id\":\"35414181\",\"journal\":\"Biochemistry\",\"lastPage\":\"2869\",\"publicationDate\":\"2022\",\"title\":\"Identification and Characterization of the Biosynthetic Pathway of the Sulfonolipid Capnine.\",\"volume\":\"61\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-01T06:24:46.269818+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "eeb98d69cf0b99fa39b7fc118681807f2518aa1d8a1eb2df8e1e31569d47b1c6",
  "url": "https://rest.uniprot.org/uniprotkb/A0A3R5XUE6.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A3R5XUE6?format=txt&versions=16)

```json
{
  "entry_version": 16,
  "evidence_id": "H1",
  "excerpt": "ID   CAPC_ORNRH              Reviewed;         283 AA.\nAC   A0A3R5XUE6;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   10-APR-2019, sequence version 1.\nDT   28-JAN-2026, entry version 16.\nDE   RecName: Full=NADPH-dependent 3-dehydrocapnine reductase {ECO:0000303|PubMed:35414181};\nDE            EC=1.1.1.- {ECO:0000269|PubMed:35414181};\nGN   Name=capC {ECO:0000303|PubMed:35414181};\nGN   ORFNames=EQP59_04780 {ECO:0000312|EMBL:QAR30703.1};\nOS   Ornithobacterium rhinotracheale.\nOC   Bacteria; Pseudomonadati; Bacteroidota; Flavobacteriia; Flavobacteriales;\nOC   Weeksellaceae; Ornithobacterium.\nOX   NCBI_TaxID=28251;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:30.826829+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6775a10db7332809ed4375188f70ceb1072cc82dbd87c32150e6341b3a85c434",
  "url": "https://rest.uniprot.org/unisave/A0A3R5XUE6?format=txt&versions=16"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A3R5XUE6?format=txt&versions=16)

```json
{
  "entry_version": 16,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=NADPH-dependent 3-dehydrocapnine reductase {ECO:0000303|PubMed:35414181};\nDE            EC=1.1.1.- {ECO:0000269|PubMed:35414181};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:30.826829+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-7",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6775a10db7332809ed4375188f70ceb1072cc82dbd87c32150e6341b3a85c434",
  "url": "https://rest.uniprot.org/unisave/A0A3R5XUE6?format=txt&versions=16"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A3R5XUE6?format=txt&versions=16)

```json
{
  "entry_version": 16,
  "evidence_id": "H3",
  "excerpt": "RN   [2]\nRP   FUNCTION, AND CATALYTIC ACTIVITY.\nRX   PubMed=35414181; DOI=10.1021/acs.biochem.2c00102;\nRA   Liu Y., Wei Y., Teh T.M., Liu D., Zhou Y., Zhao S., Ang E.L., Zhao H.,\nRA   Zhang Y.;\nRT   \"Identification and Characterization of the Biosynthetic Pathway of the\nRT   Sulfonolipid Capnine.\";\nRL   Biochemistry 61:2861-2869(2022).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:30.826829+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 21-28",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6775a10db7332809ed4375188f70ceb1072cc82dbd87c32150e6341b3a85c434",
  "url": "https://rest.uniprot.org/unisave/A0A3R5XUE6?format=txt&versions=16"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A3R5XUE6?format=txt&versions=16)

```json
{
  "entry_version": 16,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=3-oxocapnine + NADPH + H(+) = capnine + NADP(+);\nCC         Xref=Rhea:RHEA:81575, ChEBI:CHEBI:15378, ChEBI:CHEBI:57783,\nCC         ChEBI:CHEBI:58349, ChEBI:CHEBI:231947, ChEBI:CHEBI:231953;\nCC         Evidence={ECO:0000269|PubMed:35414181};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:81576;\nCC         Evidence={ECO:0000269|PubMed:35414181};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:30.826829+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 34-40",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6775a10db7332809ed4375188f70ceb1072cc82dbd87c32150e6341b3a85c434",
  "url": "https://rest.uniprot.org/unisave/A0A3R5XUE6?format=txt&versions=16"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 104. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
