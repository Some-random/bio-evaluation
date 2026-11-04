# catalytic_activity_0070

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/catalytic_activity_0070.txt)

**Task:** `catalytic_activity`  
**Expected answer:** **C** — (2R)-2,3-dihydroxy-3-methylbutanoate = 3-methyl-2-oxobutanoate + H2O

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MFASRIRSRALGLHPRARFENTRLPASTTGRRYKSDETLNRVSSKITQPKSQGASQAMLYATGLTEEDMSKPQVGISSVWFEGNPCNMHLHDLSAIVRDSVHRAGLVPMRFNSVGVSDGISMGTKGMRYSLQSRELIADGIETVMNAQWYDANVSLPGCDKNMPGVLMAMGRTNRPSIMVYGGSIKPGCSAKGQKLDLVSAFQSYGQFITGQIDEKERFDIIRNACPGRGACGGMYTANTLATAIETMGMTVPGSSSCPADDPKKLVECENIGEVVKTMLREDIKPRDVLTRQAFENAMIVVNILGGSTNAVLHLIAIADSVGIKLTIDDFQAVSDKTPFLADLKPSGKYLMNDLYNIGGTPALLKYLLKEGLIDGSGITVTGKTMKENVASWPDFPADQDIIRPLSNPIKPSGHLQILRGSLAPGGSVGKITGKEGLRFEGTAKCYDYEDAFIESLERGEIKKGEKTVVIIRYEGPKGGPGMPEMLKPSAAIMGAGLGQDVALLTDGRFSGGSHGFLIGHIVPEAMEGGPIALARDGDRIVIDAEERVVDLDIPTEELEKRRKEWKAPPLRYQKGTLKKYCTLVSDASHGCVTDGPI

[Multiple Choices]
A. 3 malonyl-CoA + acetyl-CoA + 2 S-adenosyl-L-methionine = 3,5-dimethylorsellinate + 2 S-adenosyl-L-homocysteine + 3 CO2 + 4 CoA
B. 2-hydroxyspirilloxanthin + 2 reduced [2Fe-2S]-[ferredoxin] + O2 + 2 H(+) = 2,2-dihydroxyspirilloxanthin + 2 oxidized [2Fe-2S]-[ferredoxin] + H2O
C. (2R)-2,3-dihydroxy-3-methylbutanoate = 3-methyl-2-oxobutanoate + H2O
D. a (3E,5Z)-dienoyl-CoA = a (2E,4E)-(5,6-saturated)-dienoyl-CoA
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

> The sequence-matched UniProt annotation identifies the catalytic reaction as option C and cites experimental evidence (ECO:0000269).

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 598-residue sequence is consistent with the IlvD/dihydroxy-acid dehydratase family, whose members dehydrate branched-chain amino-acid-pathway dihydroxy acids. That family-level activity points to option C, unlike the polyketide synthesis, carotenoid oxidation, or enoyl-CoA transformation in the other choices.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable family knowledge provides a meaningful basis for distinguishing C from the offered alternatives; recalling this exact protein's annotation is not required.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The offered reactions describe distinct enzyme activities, and the dihydroxy-acid dehydratase family supports C.


### Important caveats

- The family assignment is an inference from sequence and transferable knowledge; the reviewer-only annotation corroborates the keyed reaction but was not part of the original input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 598-residue sequence is consistent with the IlvD/dihydroxy-acid dehydratase family, whose members dehydrate branched-chain amino-acid-pathway dihydroxy acids. That family-level activity points to option C, unlike the polyketide synthesis, carotenoid oxidation, or enoyl-CoA transformation in the other choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable family knowledge provides a meaningful basis for distinguishing C from the offered alternatives; recalling this exact protein's annotation is not required."
  },
  "case_id": "catalytic_activity_0070",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies the catalytic reaction as option C and cites experimental evidence (ECO:0000269)."
  },
  "important_caveats": [
    "The family assignment is an inference from sequence and transferable knowledge; the reviewer-only annotation corroborates the keyed reaction but was not part of the original input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The offered reactions describe distinct enzyme activities, and the dihydroxy-acid dehydratase family supports C."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0070",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies the catalytic reaction as option C and cites experimental evidence (ECO:0000269).",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 598-residue sequence is consistent with the IlvD/dihydroxy-acid dehydratase family, whose members dehydrate branched-chain amino-acid-pathway dihydroxy acids. That family-level activity points to option C, unlike the polyketide synthesis, carotenoid oxidation, or enoyl-CoA transformation in the other choices.",
    "missing_item_specific_fact": "",
    "reason": "Transferable family knowledge provides a meaningful basis for distinguishing C from the offered alternatives; recalling this exact protein's annotation is not required."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The offered reactions describe distinct enzyme activities, and the dihydroxy-acid dehydratase family supports C."
  },
  "important_caveats": [
    "The family assignment is an inference from sequence and transferable knowledge; the reviewer-only annotation corroborates the keyed reaction but was not part of the original input."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q0CPG9 (ASTD_ASPTN) is explicitly annotated with EC 4.2.1.9 and the catalytic activity '(2R)-2,3-dihydroxy-3-methylbutanoate = 3-methyl-2-oxobutanoate + H2O' (evidence C5, H4), supported by experimental evidence (ECO:0000269|PubMed:29995859, Yan et al. Nature 2018). The sequence in the question matches the source record exactly (598 aa, sha256 match). The expected answer C is directly the annotated primary catalytic reaction.

Citations as saved: [C5](#evidence-c5), [C4](#evidence-c4), [H4](#evidence-h4), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the hallmark &#91;2Fe-2S&#93; cluster-binding motifs of the dihydroxy-acid dehydratase (DHAD/IlvD/DipD/Mai) family, most notably the 'CPGRGACGG' motif and the 'SSSCPADDPKKL' cysteine-rich segment, which are well-characterized family-level signatures shared across bacterial IlvD and fungal DHAD enzymes. The N-terminal basic residue-rich stretch (MFASRIRSRALGLHPRARFENTRLPASTTGRRYKSDETLNRVSSKITQPKSQGASQAMLYATGLTEEDMSKPQ...) is a mitochondrial targeting presequence, consistent with fungal DHAD (~598 aa total). Critically, the other three choices require structural features clearly absent here: (A) a polyketide synthase requires a multi-domain architecture (>1000 aa with KS, AT, ACP, KR, ER, DH domains); (B) a carotenoid hydroxylase requires transmembrane helices and cytochrome P450 heme-binding or Rieske-type motifs; (D) a dienoyl-CoA reductase requires a Rossmann-fold FAD/NAD-binding motif. None of these are present. The combination of Fe-S cysteine motifs, TIM-barrel-like catalytic domain architecture, mitochondrial targeting, and absence of features for the distractors allows a knowledgeable model to select C via family-level inference.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The DHAD/IlvD family has well-documented sequence signatures (CPGRGACGG Fe-S binding motif, characteristic cysteine spacing) that are transferable knowledge from bacterial IlvD and other fungal DHAD enzymes. Combined with elimination of the other choices based on their required but absent structural features (multi-domain PKS, TM helices, FAD-binding Rossmann fold), the answer is reachable without memorizing this specific protein's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices represent fundamentally different enzyme classes with incompatible structural requirements. Only DHAD (C) is consistent with the observed Fe-S cluster motifs, soluble mitochondrial architecture, and absence of PKS domains, TM helices, or FAD-binding motifs.


### Important caveats

- The protein also has a second EC 4.2.1.9 activity (pentanoate substrate) annotated by similarity to P05791 (ECO:0000250), but this does not affect the answer since only the methylbutanoate reaction is offered among choices.
- The 'CPGRGACGG' motif is strongly suggestive but not absolutely unique to DHAD; however, in the context of the four offered choices and the overall domain architecture, it is sufficiently discriminating.
- The annotation is supported by experimental evidence (PubMed 29995859, Nature 2018) for the primary reaction, not merely computational transfer.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the hallmark [2Fe-2S] cluster-binding motifs of the dihydroxy-acid dehydratase (DHAD/IlvD/DipD/Mai) family, most notably the 'CPGRGACGG' motif and the 'SSSCPADDPKKL' cysteine-rich segment, which are well-characterized family-level signatures shared across bacterial IlvD and fungal DHAD enzymes. The N-terminal basic residue-rich stretch (MFASRIRSRALGLHPRARFENTRLPASTTGRRYKSDETLNRVSSKITQPKSQGASQAMLYATGLTEEDMSKPQ...) is a mitochondrial targeting presequence, consistent with fungal DHAD (~598 aa total). Critically, the other three choices require structural features clearly absent here: (A) a polyketide synthase requires a multi-domain architecture (>1000 aa with KS, AT, ACP, KR, ER, DH domains); (B) a carotenoid hydroxylase requires transmembrane helices and cytochrome P450 heme-binding or Rieske-type motifs; (D) a dienoyl-CoA reductase requires a Rossmann-fold FAD/NAD-binding motif. None of these are present. The combination of Fe-S cysteine motifs, TIM-barrel-like catalytic domain architecture, mitochondrial targeting, and absence of features for the distractors allows a knowledgeable model to select C via family-level inference.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The DHAD/IlvD family has well-documented sequence signatures (CPGRGACGG Fe-S binding motif, characteristic cysteine spacing) that are transferable knowledge from bacterial IlvD and other fungal DHAD enzymes. Combined with elimination of the other choices based on their required but absent structural features (multi-domain PKS, TM helices, FAD-binding Rossmann fold), the answer is reachable without memorizing this specific protein's annotation."
  },
  "case_id": "catalytic_activity_0070",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C4",
      "H4",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q0CPG9 (ASTD_ASPTN) is explicitly annotated with EC 4.2.1.9 and the catalytic activity '(2R)-2,3-dihydroxy-3-methylbutanoate = 3-methyl-2-oxobutanoate + H2O' (evidence C5, H4), supported by experimental evidence (ECO:0000269|PubMed:29995859, Yan et al. Nature 2018). The sequence in the question matches the source record exactly (598 aa, sha256 match). The expected answer C is directly the annotated primary catalytic reaction."
  },
  "important_caveats": [
    "The protein also has a second EC 4.2.1.9 activity (pentanoate substrate) annotated by similarity to P05791 (ECO:0000250), but this does not affect the answer since only the methylbutanoate reaction is offered among choices.",
    "The 'CPGRGACGG' motif is strongly suggestive but not absolutely unique to DHAD; however, in the context of the four offered choices and the overall domain architecture, it is sufficiently discriminating.",
    "The annotation is supported by experimental evidence (PubMed 29995859, Nature 2018) for the primary reaction, not merely computational transfer."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent fundamentally different enzyme classes with incompatible structural requirements. Only DHAD (C) is consistent with the observed Fe-S cluster motifs, soluble mitochondrial architecture, and absence of PKS domains, TM helices, or FAD-binding motifs."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0070",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q0CPG9 (ASTD_ASPTN) is explicitly annotated with EC 4.2.1.9 and the catalytic activity '(2R)-2,3-dihydroxy-3-methylbutanoate = 3-methyl-2-oxobutanoate + H2O' (evidence C5, H4), supported by experimental evidence (ECO:0000269|PubMed:29995859, Yan et al. Nature 2018). The sequence in the question matches the source record exactly (598 aa, sha256 match). The expected answer C is directly the annotated primary catalytic reaction.",
    "evidence_ids": ["C5", "C4", "H4", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the hallmark [2Fe-2S] cluster-binding motifs of the dihydroxy-acid dehydratase (DHAD/IlvD/DipD/Mai) family, most notably the 'CPGRGACGG' motif and the 'SSSCPADDPKKL' cysteine-rich segment, which are well-characterized family-level signatures shared across bacterial IlvD and fungal DHAD enzymes. The N-terminal basic residue-rich stretch (MFASRIRSRALGLHPRARFENTRLPASTTGRRYKSDETLNRVSSKITQPKSQGASQAMLYATGLTEEDMSKPQ...) is a mitochondrial targeting presequence, consistent with fungal DHAD (~598 aa total). Critically, the other three choices require structural features clearly absent here: (A) a polyketide synthase requires a multi-domain architecture (>1000 aa with KS, AT, ACP, KR, ER, DH domains); (B) a carotenoid hydroxylase requires transmembrane helices and cytochrome P450 heme-binding or Rieske-type motifs; (D) a dienoyl-CoA reductase requires a Rossmann-fold FAD/NAD-binding motif. None of these are present. The combination of Fe-S cysteine motifs, TIM-barrel-like catalytic domain architecture, mitochondrial targeting, and absence of features for the distractors allows a knowledgeable model to select C via family-level inference.",
    "missing_item_specific_fact": "",
    "reason": "The DHAD/IlvD family has well-documented sequence signatures (CPGRGACGG Fe-S binding motif, characteristic cysteine spacing) that are transferable knowledge from bacterial IlvD and other fungal DHAD enzymes. Combined with elimination of the other choices based on their required but absent structural features (multi-domain PKS, TM helices, FAD-binding Rossmann fold), the answer is reachable without memorizing this specific protein's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent fundamentally different enzyme classes with incompatible structural requirements. Only DHAD (C) is consistent with the observed Fe-S cluster motifs, soluble mitochondrial architecture, and absence of PKS domains, TM helices, or FAD-binding motifs."
  },
  "important_caveats": [
    "The protein also has a second EC 4.2.1.9 activity (pentanoate substrate) annotated by similarity to P05791 (ECO:0000250), but this does not affect the answer since only the methylbutanoate reaction is offered among choices.",
    "The 'CPGRGACGG' motif is strongly suggestive but not absolutely unique to DHAD; however, in the context of the four offered choices and the overall domain architecture, it is sufficiently discriminating.",
    "The annotation is supported by experimental evidence (PubMed 29995859, Nature 2018) for the primary reaction, not merely computational transfer."
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
  "benchmark_sequence_length": 598,
  "benchmark_sequence_sha256": "fa9e543b4d22dcd970aea00f48d66772e78eab78d909318baa5438958e06b376",
  "current_entry_audit": {
    "entryVersion": 92,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2006-10-17",
    "sequenceVersion": 1
  },
  "current_record_sha256": "0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 598,
  "current_source_sequence_sha256": "fa9e543b4d22dcd970aea00f48d66772e78eab78d909318baa5438958e06b376",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 90,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q0CPG9",
  "selected_historical_entry_version": 90,
  "selected_historical_record_sha256": "9bf655407cf1951ee3eade3f48f59afe8492d4b13add34fd5d783ee9fb63fb58",
  "selected_historical_source_sequence_length": 598,
  "selected_historical_source_sequence_sha256": "fa9e543b4d22dcd970aea00f48d66772e78eab78d909318baa5438958e06b376",
  "selected_historical_version": {
    "accession": "Q0CPG9",
    "database": "Swiss-Prot",
    "entryVersion": 90,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "ASTD_ASPTN",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q0CPG9\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:30:26.147110+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG9.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":92,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2006-10-17\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:30:26.147110+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG9.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Eurotiomycetes\",\"Eurotiomycetidae\",\"Eurotiales\",\"Aspergillaceae\",\"Aspergillus\",\"Circumdati\"],\"scientificName\":\"Aspergillus terreus (strain NIH 2624 / FGSC A1156)\",\"taxonId\":341663}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:30:26.147110+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG9.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"29995859\",\"source\":\"PubMed\"}],\"value\":\"Aspterric acid biosynthesis cluster protein D\"}}],\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"29995859\",\"source\":\"PubMed\"}],\"value\":\"4.2.1.9\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"29995859\",\"source\":\"PubMed\"}],\"value\":\"Dihydroxy-acid dehydratase astD, mitochondrial\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"29995859\",\"source\":\"PubMed\"}],\"value\":\"DHAD astD\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:30:26.147110+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG9.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"29995859\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:24810\"}}],\"reaction\":{\"ecNumber\":\"4.2.1.9\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"29995859\",\"source\":\"PubMed\"}],\"name\":\"(2R)-2,3-dihydroxy-3-methylbutanoate = 3-methyl-2-oxobutanoate + H2O\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:24809\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:11851\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:49072\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:30:26.147110+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG9.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P05791\",\"source\":\"UniProtKB\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:27695\"}}],\"reaction\":{\"ecNumber\":\"4.2.1.9\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P05791\",\"source\":\"UniProtKB\"}],\"name\":\"(2R,3R)-2,3-dihydroxy-3-methylpentanoate = (S)-3-methyl-2-oxopentanoate + H2O\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:27694\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:35146\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:49258\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:30:26.147110+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG9.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Yan Y.\",\"Liu Q.\",\"Zang X.\",\"Yuan S.\",\"Bat-Erdene U.\",\"Nguyen C.\",\"Gan J.\",\"Zhou J.\",\"Jacobsen S.E.\",\"Tang Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"29995859\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41586-018-0319-4\"}],\"citationType\":\"journal article\",\"firstPage\":\"415\",\"id\":\"29995859\",\"journal\":\"Nature\",\"lastPage\":\"418\",\"publicationDate\":\"2018\",\"title\":\"Resistance-gene-directed discovery of a natural-product herbicide with a new mode of action.\",\"volume\":\"559\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"DOMAIN\",\"ACTIVITY REGULATION\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:30:26.147110+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG9.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90)

```json
{
  "entry_version": 90,
  "evidence_id": "H1",
  "excerpt": "ID   ASTD_ASPTN              Reviewed;         598 AA.\nAC   Q0CPG9;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   17-OCT-2006, sequence version 1.\nDT   28-JAN-2026, entry version 90.\nDE   RecName: Full=Dihydroxy-acid dehydratase astD, mitochondrial {ECO:0000303|PubMed:29995859};\nDE            Short=DHAD astD {ECO:0000303|PubMed:29995859};\nDE            EC=4.2.1.9 {ECO:0000269|PubMed:29995859};\nDE   AltName: Full=Aspterric acid biosynthesis cluster protein D {ECO:0000303|PubMed:29995859};\nDE   Flags: Precursor;\nGN   Name=astD {ECO:0000303|PubMed:29995859}; ORFNames=ATEG_04415;\nOS   Aspergillus terreus (strain NIH 2624 / FGSC A1156).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;\nOC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Aspergillus;\nOC   Aspergillus subgen. Circumdati.\nOX   NCBI_TaxID=341663;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:28.917378+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9bf655407cf1951ee3eade3f48f59afe8492d4b13add34fd5d783ee9fb63fb58",
  "url": "https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90)

```json
{
  "entry_version": 90,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Dihydroxy-acid dehydratase astD, mitochondrial {ECO:0000303|PubMed:29995859};\nDE            Short=DHAD astD {ECO:0000303|PubMed:29995859};\nDE            EC=4.2.1.9 {ECO:0000269|PubMed:29995859};\nDE   AltName: Full=Aspterric acid biosynthesis cluster protein D {ECO:0000303|PubMed:29995859};\nDE   Flags: Precursor;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:28.917378+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-10",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9bf655407cf1951ee3eade3f48f59afe8492d4b13add34fd5d783ee9fb63fb58",
  "url": "https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90)

```json
{
  "entry_version": 90,
  "evidence_id": "H3",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, DOMAIN,\nRP   ACTIVITY REGULATION, AND PATHWAY.\nRX   PubMed=29995859; DOI=10.1038/s41586-018-0319-4;\nRA   Yan Y., Liu Q., Zang X., Yuan S., Bat-Erdene U., Nguyen C., Gan J.,\nRA   Zhou J., Jacobsen S.E., Tang Y.;\nRT   \"Resistance-gene-directed discovery of a natural-product herbicide with a\nRT   new mode of action.\";\nRL   Nature 559:415-418(2018).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:28.917378+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 29-37",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9bf655407cf1951ee3eade3f48f59afe8492d4b13add34fd5d783ee9fb63fb58",
  "url": "https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90)

```json
{
  "entry_version": 90,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=(2R)-2,3-dihydroxy-3-methylbutanoate = 3-methyl-2-oxobutanoate\nCC         + H2O; Xref=Rhea:RHEA:24809, ChEBI:CHEBI:11851, ChEBI:CHEBI:15377,\nCC         ChEBI:CHEBI:49072; EC=4.2.1.9;\nCC         Evidence={ECO:0000269|PubMed:29995859};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:24810;\nCC         Evidence={ECO:0000269|PubMed:29995859};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:28.917378+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 52-58",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9bf655407cf1951ee3eade3f48f59afe8492d4b13add34fd5d783ee9fb63fb58",
  "url": "https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90)

```json
{
  "entry_version": 90,
  "evidence_id": "H5",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=(2R,3R)-2,3-dihydroxy-3-methylpentanoate = (S)-3-methyl-2-\nCC         oxopentanoate + H2O; Xref=Rhea:RHEA:27694, ChEBI:CHEBI:15377,\nCC         ChEBI:CHEBI:35146, ChEBI:CHEBI:49258; EC=4.2.1.9;\nCC         Evidence={ECO:0000250|UniProtKB:P05791};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:27695;\nCC         Evidence={ECO:0000250|UniProtKB:P05791};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:28.917378+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 59-65",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9bf655407cf1951ee3eade3f48f59afe8492d4b13add34fd5d783ee9fb63fb58",
  "url": "https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 70. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
