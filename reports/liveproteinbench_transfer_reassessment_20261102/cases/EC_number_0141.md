# EC_number_0141

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0141.txt)

**Task:** `EC_number`  
**Expected answer:** **D** — 1.1.1.138

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MPISIPKGEKLMDLLSMKGKVTIVTGASGPRGMGIEAARGIAEMGGNVALTYAGRKEGGEKNAAALEKEYGIKAKAYKLDVANYESCCQLVKDVIADFGQIDAFVANAGKTADSGVLDGEISAFEEVIQTDLLGVAYCAKAVGHHFKERQTGSFVITASMSGHIANFPQEQTSYNVAKAGCIHMARSLANEWRDFARVNSISPGYIDTGLSDFVDKETQKLWHSMIPMGRDGDAKELKAAYVYFCSDASTYTTGSDLVIDGGYCAR

[Multiple Choices]
A. 1.1.1.195
B. 4.2.1.70
C. 1.14.19.80
D. 1.1.1.138
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzyme Commission (EC) Number Prediction, which is to predict the complete 4-digit Enzyme Commission (EC) number for a given protein. The EC number is a numerical classification that categorizes enzymes based on the chemical reactions they catalyze. You should select the most accurate EC number from the provided options based on the protein's sequence.. The inputs provided by the user for this task include:

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

> The sequence-matched UniProt record assigns EC 1.1.1.138 and identifies the enzyme as NADP-dependent mannitol dehydrogenase. Its catalytic-activity annotation gives the mannitol-to-fructose reaction, with PubMed-linked evidence; this supports the key rather than merely reporting a computational prediction.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

Empty string, as saved.


**Missing item-specific fact**

> Whether this protein catalyzes the mannitol/fructose reaction (and its associated cofactor specificity), rather than the reaction classified by EC 1.1.1.195.


**Reason**

> The glycine-rich N-terminal motif is consistent with a soluble nucleotide-binding oxidoreductase, making the hydratase and membrane desaturase choices poor fits. But that broad inference does not distinguish the two oxidoreductase choices: the sequence provides no evident, readily interpretable feature that establishes the substrate specificity needed for the exact EC assignment.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence supports a broad oxidoreductase interpretation, but the evidence available from it does not independently establish that the competing oxidoreductase option is also correct.


### Important caveats

- Reviewer-only evidence matches the supplied sequence; the author's exact source snapshot is unknown.
- The source provides PubMed-linked evidence for the EC annotation, but the primary publication was not independently reviewed here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Whether this protein catalyzes the mannitol/fructose reaction (and its associated cofactor specificity), rather than the reaction classified by EC 1.1.1.195.",
    "reason": "The glycine-rich N-terminal motif is consistent with a soluble nucleotide-binding oxidoreductase, making the hydratase and membrane desaturase choices poor fits. But that broad inference does not distinguish the two oxidoreductase choices: the sequence provides no evident, readily interpretable feature that establishes the substrate specificity needed for the exact EC assignment."
  },
  "case_id": "EC_number_0141",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns EC 1.1.1.138 and identifies the enzyme as NADP-dependent mannitol dehydrogenase. Its catalytic-activity annotation gives the mannitol-to-fructose reaction, with PubMed-linked evidence; this supports the key rather than merely reporting a computational prediction."
  },
  "important_caveats": [
    "Reviewer-only evidence matches the supplied sequence; the author's exact source snapshot is unknown.",
    "The source provides PubMed-linked evidence for the EC annotation, but the primary publication was not independently reviewed here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence supports a broad oxidoreductase interpretation, but the evidence available from it does not independently establish that the competing oxidoreductase option is also correct."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0141",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns EC 1.1.1.138 and identifies the enzyme as NADP-dependent mannitol dehydrogenase. Its catalytic-activity annotation gives the mannitol-to-fructose reaction, with PubMed-linked evidence; this supports the key rather than merely reporting a computational prediction.",
    "evidence_ids": ["C4", "C5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "",
    "missing_item_specific_fact": "Whether this protein catalyzes the mannitol/fructose reaction (and its associated cofactor specificity), rather than the reaction classified by EC 1.1.1.195.",
    "reason": "The glycine-rich N-terminal motif is consistent with a soluble nucleotide-binding oxidoreductase, making the hydratase and membrane desaturase choices poor fits. But that broad inference does not distinguish the two oxidoreductase choices: the sequence provides no evident, readily interpretable feature that establishes the substrate specificity needed for the exact EC assignment."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence supports a broad oxidoreductase interpretation, but the evidence available from it does not independently establish that the competing oxidoreductase option is also correct."
  },
  "important_caveats": [
    "Reviewer-only evidence matches the supplied sequence; the author's exact source snapshot is unknown.",
    "The source provides PubMed-linked evidence for the EC annotation, but the primary publication was not independently reviewed here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A223HDI5 (Swiss-Prot, reviewed) annotates this exact 266-aa sequence as NADP-dependent mannitol dehydrogenase (MtDH), EC 1.1.1.138, with experimental evidence (ECO:0000269, PubMed:32003433). The catalytic activity D-mannitol + NADP(+) = D-fructose + NADPH + H(+) is confirmed. Sequence SHA-256 matches the benchmark input.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal motif 'TGASGPRGMGIEAARG' contains the canonical Rossmann-fold GxGxxG pattern (GASGPRGM), diagnostic of NAD(P)-dependent oxidoreductases (EC 1.1.1.x). This immediately eliminates B (EC 4.2.1.70, a lyase/hydratase) and C (EC 1.14.19.80, an oxygen-incorporating oxidoreductase requiring heme or Fe(II)/2-oxoglutarate motifs absent here). Between the remaining EC 1.1.1.x options A (1.1.1.195) and D (1.1.1.138), the sequence shows hallmark Short-chain Dehydrogenase/Reductase (SDR) family features: ~266 aa length, the TGxxxGxG Rossmann fold, a putative catalytic tetrad region (NAGKT…HHFK…SDASTY), and absence of any CoA-binding or multi-domain architecture. Mannitol dehydrogenases (EC 1.1.1.138) are among the best-characterized small SDR enzymes acting on sugar alcohols, and this motif architecture matches fungal MtDH homologs. In contrast, EC 1.1.1.195 (a 2-hydroxyacyl-CoA dehydrogenase variant) typically acts on CoA-linked substrates and often possesses additional substrate-binding domains or belongs to a different structural subfamily. The compact SDR architecture with sugar-alcohol–oriented catalytic geometry is more consistent with mannitol dehydrogenase.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The Rossmann fold identifies EC class 1.1.1.x, and the SDR-family sequence architecture (length, TGxxxGxG, catalytic tetrad spacing, absence of CoA-binding domains) provides a family-level inference that meaningfully distinguishes mannitol dehydrogenase from a CoA-dependent dehydrogenase among the offered choices. This relies on well-established SDR family biology learned across many homologous proteins.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options B and C are clearly eliminated by the Rossmann fold. Between A and D, the compact SDR architecture without CoA-binding features favors D (mannitol dehydrogenase) over A (a CoA-linked dehydrogenase). While both share EC class 1.1.1.x, the family-level structural inference provides a defensible distinction.


### Important caveats

- Distinguishing between two EC 1.1.1.x numbers from sequence alone carries residual uncertainty; the SDR-family argument is probabilistic rather than definitive.
- The reviewer-only UniProt evidence confirms the key experimentally, but the evaluated model does not have access to this annotation.
- EC 1.1.1.195 is a less commonly encountered EC number; its exact substrate scope and structural class should be verified, though it is conventionally associated with CoA-linked substrates.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal motif 'TGASGPRGMGIEAARG' contains the canonical Rossmann-fold GxGxxG pattern (GASGPRGM), diagnostic of NAD(P)-dependent oxidoreductases (EC 1.1.1.x). This immediately eliminates B (EC 4.2.1.70, a lyase/hydratase) and C (EC 1.14.19.80, an oxygen-incorporating oxidoreductase requiring heme or Fe(II)/2-oxoglutarate motifs absent here). Between the remaining EC 1.1.1.x options A (1.1.1.195) and D (1.1.1.138), the sequence shows hallmark Short-chain Dehydrogenase/Reductase (SDR) family features: ~266 aa length, the TGxxxGxG Rossmann fold, a putative catalytic tetrad region (NAGKT…HHFK…SDASTY), and absence of any CoA-binding or multi-domain architecture. Mannitol dehydrogenases (EC 1.1.1.138) are among the best-characterized small SDR enzymes acting on sugar alcohols, and this motif architecture matches fungal MtDH homologs. In contrast, EC 1.1.1.195 (a 2-hydroxyacyl-CoA dehydrogenase variant) typically acts on CoA-linked substrates and often possesses additional substrate-binding domains or belongs to a different structural subfamily. The compact SDR architecture with sugar-alcohol–oriented catalytic geometry is more consistent with mannitol dehydrogenase.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The Rossmann fold identifies EC class 1.1.1.x, and the SDR-family sequence architecture (length, TGxxxGxG, catalytic tetrad spacing, absence of CoA-binding domains) provides a family-level inference that meaningfully distinguishes mannitol dehydrogenase from a CoA-dependent dehydrogenase among the offered choices. This relies on well-established SDR family biology learned across many homologous proteins."
  },
  "case_id": "EC_number_0141",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A223HDI5 (Swiss-Prot, reviewed) annotates this exact 266-aa sequence as NADP-dependent mannitol dehydrogenase (MtDH), EC 1.1.1.138, with experimental evidence (ECO:0000269, PubMed:32003433). The catalytic activity D-mannitol + NADP(+) = D-fructose + NADPH + H(+) is confirmed. Sequence SHA-256 matches the benchmark input."
  },
  "important_caveats": [
    "Distinguishing between two EC 1.1.1.x numbers from sequence alone carries residual uncertainty; the SDR-family argument is probabilistic rather than definitive.",
    "The reviewer-only UniProt evidence confirms the key experimentally, but the evaluated model does not have access to this annotation.",
    "EC 1.1.1.195 is a less commonly encountered EC number; its exact substrate scope and structural class should be verified, though it is conventionally associated with CoA-linked substrates."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B and C are clearly eliminated by the Rossmann fold. Between A and D, the compact SDR architecture without CoA-binding features favors D (mannitol dehydrogenase) over A (a CoA-linked dehydrogenase). While both share EC class 1.1.1.x, the family-level structural inference provides a defensible distinction."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0141",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A223HDI5 (Swiss-Prot, reviewed) annotates this exact 266-aa sequence as NADP-dependent mannitol dehydrogenase (MtDH), EC 1.1.1.138, with experimental evidence (ECO:0000269, PubMed:32003433). The catalytic activity D-mannitol + NADP(+) = D-fructose + NADPH + H(+) is confirmed. Sequence SHA-256 matches the benchmark input.",
    "evidence_ids": ["C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal motif 'TGASGPRGMGIEAARG' contains the canonical Rossmann-fold GxGxxG pattern (GASGPRGM), diagnostic of NAD(P)-dependent oxidoreductases (EC 1.1.1.x). This immediately eliminates B (EC 4.2.1.70, a lyase/hydratase) and C (EC 1.14.19.80, an oxygen-incorporating oxidoreductase requiring heme or Fe(II)/2-oxoglutarate motifs absent here). Between the remaining EC 1.1.1.x options A (1.1.1.195) and D (1.1.1.138), the sequence shows hallmark Short-chain Dehydrogenase/Reductase (SDR) family features: ~266 aa length, the TGxxxGxG Rossmann fold, a putative catalytic tetrad region (NAGKT…HHFK…SDASTY), and absence of any CoA-binding or multi-domain architecture. Mannitol dehydrogenases (EC 1.1.1.138) are among the best-characterized small SDR enzymes acting on sugar alcohols, and this motif architecture matches fungal MtDH homologs. In contrast, EC 1.1.1.195 (a 2-hydroxyacyl-CoA dehydrogenase variant) typically acts on CoA-linked substrates and often possesses additional substrate-binding domains or belongs to a different structural subfamily. The compact SDR architecture with sugar-alcohol–oriented catalytic geometry is more consistent with mannitol dehydrogenase.",
    "missing_item_specific_fact": "",
    "reason": "The Rossmann fold identifies EC class 1.1.1.x, and the SDR-family sequence architecture (length, TGxxxGxG, catalytic tetrad spacing, absence of CoA-binding domains) provides a family-level inference that meaningfully distinguishes mannitol dehydrogenase from a CoA-dependent dehydrogenase among the offered choices. This relies on well-established SDR family biology learned across many homologous proteins."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B and C are clearly eliminated by the Rossmann fold. Between A and D, the compact SDR architecture without CoA-binding features favors D (mannitol dehydrogenase) over A (a CoA-linked dehydrogenase). While both share EC class 1.1.1.x, the family-level structural inference provides a defensible distinction."
  },
  "important_caveats": [
    "Distinguishing between two EC 1.1.1.x numbers from sequence alone carries residual uncertainty; the SDR-family argument is probabilistic rather than definitive.",
    "The reviewer-only UniProt evidence confirms the key experimentally, but the evaluated model does not have access to this annotation.",
    "EC 1.1.1.195 is a less commonly encountered EC number; its exact substrate scope and structural class should be verified, though it is conventionally associated with CoA-linked substrates."
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
  "benchmark_sequence_length": 266,
  "benchmark_sequence_sha256": "9ba750d830f9b17efbb379114b2586beae27b485e183fc99fdd2ab0bad2a96aa",
  "current_entry_audit": {
    "entryVersion": 15,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-01-28",
    "lastSequenceUpdateDate": "2017-10-25",
    "sequenceVersion": 1
  },
  "current_record_sha256": "c6aa71c90f5754236176b13ca1a049caba09e755d0ca2e57921409a1d945c654",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 266,
  "current_source_sequence_sha256": "9ba750d830f9b17efbb379114b2586beae27b485e183fc99fdd2ab0bad2a96aa",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 15,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A223HDI5",
  "selected_historical_entry_version": 15,
  "selected_historical_record_sha256": "cd858973dafcf9f7eafcc69467bc9fac51732b2bdf6281c7e18de2db9ff34dd6",
  "selected_historical_source_sequence_length": 266,
  "selected_historical_source_sequence_sha256": "9ba750d830f9b17efbb379114b2586beae27b485e183fc99fdd2ab0bad2a96aa",
  "selected_historical_version": {
    "accession": "A0A223HDI5",
    "database": "Swiss-Prot",
    "entryVersion": 15,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "NMTDH_AURME",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223HDI5.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A223HDI5\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:24:44.241345+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c6aa71c90f5754236176b13ca1a049caba09e755d0ca2e57921409a1d945c654",
  "url": "https://rest.uniprot.org/uniprotkb/A0A223HDI5.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223HDI5.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":15,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-01-28\",\"lastSequenceUpdateDate\":\"2017-10-25\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:24:44.241345+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c6aa71c90f5754236176b13ca1a049caba09e755d0ca2e57921409a1d945c654",
  "url": "https://rest.uniprot.org/uniprotkb/A0A223HDI5.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223HDI5.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Aureobasidium pullulans var. melanogenum\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Dothideomycetes\",\"Dothideomycetidae\",\"Dothideales\",\"Saccotheciaceae\",\"Aureobasidium\"],\"scientificName\":\"Aureobasidium melanogenum\",\"taxonId\":46634}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:24:44.241345+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c6aa71c90f5754236176b13ca1a049caba09e755d0ca2e57921409a1d945c654",
  "url": "https://rest.uniprot.org/uniprotkb/A0A223HDI5.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223HDI5.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"32003433\",\"source\":\"PubMed\"}],\"value\":\"1.1.1.138\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"32003433\",\"source\":\"PubMed\"}],\"value\":\"NADP-dependent mannitol dehydrogenase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"32003433\",\"source\":\"PubMed\"}],\"value\":\"MtDH\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:24:44.241345+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c6aa71c90f5754236176b13ca1a049caba09e755d0ca2e57921409a1d945c654",
  "url": "https://rest.uniprot.org/uniprotkb/A0A223HDI5.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223HDI5.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"32003433\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:16766\"}},{\"directionType\":\"right-to-left\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"32003433\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:16767\"}}],\"reaction\":{\"ecNumber\":\"1.1.1.138\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"32003433\",\"source\":\"PubMed\"}],\"name\":\"D-mannitol + NADP(+) = D-fructose + NADPH + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:16765\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:16899\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:37721\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57783\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:24:44.241345+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c6aa71c90f5754236176b13ca1a049caba09e755d0ca2e57921409a1d945c654",
  "url": "https://rest.uniprot.org/uniprotkb/A0A223HDI5.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223HDI5.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Xue S.J.\",\"Liu G.L.\",\"Chi Z.\",\"Gao Z.C.\",\"Hu Z.\",\"Chi Z.M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"32003433\"},{\"database\":\"DOI\",\"id\":\"10.1042/bcj20190922\"}],\"citationType\":\"journal article\",\"firstPage\":\"887\",\"id\":\"32003433\",\"journal\":\"Biochem. J.\",\"lastPage\":\"903\",\"publicationDate\":\"2020\",\"title\":\"Genetic evidences for the core biosynthesis pathway, regulation, transport and secretion of liamocins in yeast-like fungal cells.\",\"volume\":\"477\"},\"referenceNumber\":4,\"referencePositions\":[\"FUNCTION\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-02T04:24:44.241345+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c6aa71c90f5754236176b13ca1a049caba09e755d0ca2e57921409a1d945c654",
  "url": "https://rest.uniprot.org/uniprotkb/A0A223HDI5.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A223HDI5?format=txt&versions=15)

```json
{
  "entry_version": 15,
  "evidence_id": "H1",
  "excerpt": "ID   NMTDH_AURME             Reviewed;         266 AA.\nAC   A0A223HDI5;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   25-OCT-2017, sequence version 1.\nDT   28-JAN-2026, entry version 15.\nDE   RecName: Full=NADP-dependent mannitol dehydrogenase {ECO:0000303|PubMed:32003433};\nDE            Short=MtDH {ECO:0000303|PubMed:32003433};\nDE            EC=1.1.1.138 {ECO:0000269|PubMed:32003433};\nOS   Aureobasidium melanogenum (Aureobasidium pullulans var. melanogenum).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Dothideomycetes;\nOC   Dothideomycetidae; Dothideales; Saccotheciaceae; Aureobasidium.\nOX   NCBI_TaxID=46634;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:46.627063+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-12",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "cd858973dafcf9f7eafcc69467bc9fac51732b2bdf6281c7e18de2db9ff34dd6",
  "url": "https://rest.uniprot.org/unisave/A0A223HDI5?format=txt&versions=15"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A223HDI5?format=txt&versions=15)

```json
{
  "entry_version": 15,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=NADP-dependent mannitol dehydrogenase {ECO:0000303|PubMed:32003433};\nDE            Short=MtDH {ECO:0000303|PubMed:32003433};\nDE            EC=1.1.1.138 {ECO:0000269|PubMed:32003433};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:46.627063+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-8",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "cd858973dafcf9f7eafcc69467bc9fac51732b2bdf6281c7e18de2db9ff34dd6",
  "url": "https://rest.uniprot.org/unisave/A0A223HDI5?format=txt&versions=15"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A223HDI5?format=txt&versions=15)

```json
{
  "entry_version": 15,
  "evidence_id": "H3",
  "excerpt": "RN   [4]\nRP   FUNCTION, AND DISRUPTION PHENOTYPE.\nRX   PubMed=32003433; DOI=10.1042/bcj20190922;\nRA   Xue S.J., Liu G.L., Chi Z., Gao Z.C., Hu Z., Chi Z.M.;\nRT   \"Genetic evidences for the core biosynthesis pathway, regulation, transport\nRT   and secretion of liamocins in yeast-like fungal cells.\";\nRL   Biochem. J. 477:887-903(2020).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:46.627063+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 31-37",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "cd858973dafcf9f7eafcc69467bc9fac51732b2bdf6281c7e18de2db9ff34dd6",
  "url": "https://rest.uniprot.org/unisave/A0A223HDI5?format=txt&versions=15"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A223HDI5?format=txt&versions=15)

```json
{
  "entry_version": 15,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=D-mannitol + NADP(+) = D-fructose + NADPH + H(+);\nCC         Xref=Rhea:RHEA:16765, ChEBI:CHEBI:15378, ChEBI:CHEBI:16899,\nCC         ChEBI:CHEBI:37721, ChEBI:CHEBI:57783, ChEBI:CHEBI:58349;\nCC         EC=1.1.1.138; Evidence={ECO:0000305|PubMed:32003433};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:16766;\nCC         Evidence={ECO:0000305|PubMed:32003433};\nCC       PhysiologicalDirection=right-to-left; Xref=Rhea:RHEA:16767;\nCC         Evidence={ECO:0000305|PubMed:32003433};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:46.627063+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 52-60",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "cd858973dafcf9f7eafcc69467bc9fac51732b2bdf6281c7e18de2db9ff34dd6",
  "url": "https://rest.uniprot.org/unisave/A0A223HDI5?format=txt&versions=15"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 141. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
