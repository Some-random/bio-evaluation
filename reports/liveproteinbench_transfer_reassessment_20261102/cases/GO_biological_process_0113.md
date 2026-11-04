# GO_biological_process_0113

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_biological_process_0113.txt)

**Task:** `GO_biological_process`  
**Expected answer:** **C** — biosynthetic process

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MTLTENVMKPQIQRFTRDHDPKVLWQVVEEDGAVIIEGFLPHEVIQKFDCELDVRSKATKGGEMNQEFYQMPVPTTTKWMNDLTATCPTFRHEILNNDILHSLCNVAFEPHGDYWLLNGMAMEMMPGNPTQQIHNDHGTHPILQYLRPDAPAPVFSIITAVTEFTESNGATRVILGSHRWPQGQKAKDDQAVRAALQPGDALVMHRSTKHGGAAHDADNQDHRRLLLTCMGTCQLAPYETNVTVPRPIVESMTPLAQKMIGWRSTRPVISNVTGLNTVRMKHLENQIELKSNVPLNVGGC

[Multiple Choices]
A. pollen wall assembly
B. negative regulation of RNA export from nucleus
C. biosynthetic process
D. response to cytokine
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Biological Process Prediction, which is to predict the primary biological process a given protein participates in, as defined by the Gene Ontology (GO) 'Biological Process' branch. A biological process is a series of molecular events that accomplishes a larger biological program, such as cell division or signal transduction. Based on the provided protein sequence, you must select the option that best describes the overall biological objective to which the protein contributes.. The inputs provided by the user for this task include:

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

> The matched-sequence UniProt annotation describes OkaE as catalyzing steps in okaramine alkaloid biosynthesis, with cited experimental evidence. That supports the broad biological-process choice of biosynthetic process. The specific GO annotation for terpenoid biosynthesis is computationally assigned, but the support for choice C does not depend on that narrower annotation.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C8](#evidence-c8).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains motifs consistent with a non-heme Fe(II)/2-oxoglutarate-dependent dioxygenase, an enzyme family that includes oxidative tailoring enzymes in natural-product biosynthesis. That provides a credible basis for choosing the broad biosynthetic-process option over the highly specific pollen-wall, RNA-export-regulation, and cytokine-response choices.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence does not establish the exact substrate, pathway, or organism, and family recognition alone would not prove this enzyme's role. But the family-level enzyme inference meaningfully favors the broad biosynthesis option among the alternatives; exact knowledge of this protein's annotation is not necessary for that distinction.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The other options describe specific processes that are not meaningfully suggested by the sequence, while biosynthetic process is a reasonable broad choice for a likely metabolic enzyme.


### Important caveats

- The original input provides no organism or functional annotation, so the sequence-based inference is probabilistic rather than a determination of the exact pathway.
- The cited experimental annotation supports okaramine biosynthesis; the narrower terpenoid GO annotation is computational and is not needed to justify the keyed broad choice.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains motifs consistent with a non-heme Fe(II)/2-oxoglutarate-dependent dioxygenase, an enzyme family that includes oxidative tailoring enzymes in natural-product biosynthesis. That provides a credible basis for choosing the broad biosynthetic-process option over the highly specific pollen-wall, RNA-export-regulation, and cytokine-response choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence does not establish the exact substrate, pathway, or organism, and family recognition alone would not prove this enzyme's role. But the family-level enzyme inference meaningfully favors the broad biosynthesis option among the alternatives; exact knowledge of this protein's annotation is not necessary for that distinction."
  },
  "case_id": "GO_biological_process_0113",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C8"
    ],
    "judgment": "supported",
    "reason": "The matched-sequence UniProt annotation describes OkaE as catalyzing steps in okaramine alkaloid biosynthesis, with cited experimental evidence. That supports the broad biological-process choice of biosynthetic process. The specific GO annotation for terpenoid biosynthesis is computationally assigned, but the support for choice C does not depend on that narrower annotation."
  },
  "important_caveats": [
    "The original input provides no organism or functional annotation, so the sequence-based inference is probabilistic rather than a determination of the exact pathway.",
    "The cited experimental annotation supports okaramine biosynthesis; the narrower terpenoid GO annotation is computational and is not needed to justify the keyed broad choice."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The other options describe specific processes that are not meaningfully suggested by the sequence, while biosynthetic process is a reasonable broad choice for a likely metabolic enzyme."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0113",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched-sequence UniProt annotation describes OkaE as catalyzing steps in okaramine alkaloid biosynthesis, with cited experimental evidence. That supports the broad biological-process choice of biosynthetic process. The specific GO annotation for terpenoid biosynthesis is computationally assigned, but the support for choice C does not depend on that narrower annotation.",
    "evidence_ids": ["C5", "C6", "C8"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains motifs consistent with a non-heme Fe(II)/2-oxoglutarate-dependent dioxygenase, an enzyme family that includes oxidative tailoring enzymes in natural-product biosynthesis. That provides a credible basis for choosing the broad biosynthetic-process option over the highly specific pollen-wall, RNA-export-regulation, and cytokine-response choices.",
    "missing_item_specific_fact": "",
    "reason": "The sequence does not establish the exact substrate, pathway, or organism, and family recognition alone would not prove this enzyme's role. But the family-level enzyme inference meaningfully favors the broad biosynthesis option among the alternatives; exact knowledge of this protein's annotation is not necessary for that distinction."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The other options describe specific processes that are not meaningfully suggested by the sequence, while biosynthetic process is a reasonable broad choice for a likely metabolic enzyme."
  },
  "important_caveats": [
    "The original input provides no organism or functional annotation, so the sequence-based inference is probabilistic rather than a determination of the exact pathway.",
    "The cited experimental annotation supports okaramine biosynthesis; the narrower terpenoid GO annotation is computational and is not needed to justify the keyed broad choice."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein is OkaE, an iron/alpha-ketoglutarate-dependent dioxygenase in the okaramine biosynthetic gene cluster. UniProt annotates it with GO:0016114 (terpenoid biosynthetic process), which is a descendant of GO:0009058 (biosynthetic process) via the path GO:0016114 → GO:0008299 → GO:0008610 → GO:0009058. The pathway is explicitly labeled 'Alkaloid biosynthesis' and 'Secondary metabolite biosynthesis; terpenoid biosynthesis' with experimental evidence (ECO:0000269, PubMed:28631282, PubMed:29384650). The broad term 'biosynthetic process' (GO:0009058) is a valid ancestor of the specific annotation, so choice C is scientifically supported.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [GO3](#evidence-go3), [GO5](#evidence-go5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains hallmarks of the iron/alpha-ketoglutarate (Fe(II)/2OG) dioxygenase superfamily: the 2-His-1-carboxylate facial triad is visible in motifs such as 'HNDHG' (two histidines) and 'HGDYWLLNGM' (H...D carboxylate spacing), plus 'VILGSHRWPQ' (GSH region). This is a well-known superfamily whose members are overwhelmingly biosynthetic enzymes (e.g., gibberellin 2-oxidases, antibiotic tailoring enzymes, amino acid hydroxylases, secondary metabolite cyclases). A model recognizing this family can infer a biosynthetic role. Furthermore, 'pollen wall assembly' (A) is a plant-specific process absent in fungi, and 'response to cytokine' (D) is an animal immune signaling process; the sequence lacks any nuclear transport or RNA-binding domains needed for (B). The combination of 2OG oxygenase family recognition (transferable from many characterized homologs) and elimination of organism/class-specific distractors meaningfully distinguishes C from A, B, and D.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Recognition of the Fe(II)/2OG oxygenase facial triad from the sequence, combined with the well-established family-level pattern that these enzymes predominantly catalyze biosynthetic transformations, provides a concrete transferable inference. Elimination of pollen (plant-specific), cytokine (animal-specific), and RNA export (no relevant domains) further narrows to C. No target-specific database lookup is required.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options span very different biological contexts (plant pollen, nuclear RNA transport, general biosynthesis, animal immune signaling). Only 'biosynthetic process' is consistent with a 2OG oxygenase in a fungal organism. No ambiguity among the offered choices.


### Important caveats

- GO:0009058 (biosynthetic process) carries the 'gocheck_do_not_annotate' subset, meaning it is rarely used as a direct annotation but is valid as an inherited ancestor term. The question's use of this broad term is acceptable as a parent-level description.
- The UniProt GO annotation (GO:0016114, terpenoid biosynthetic process) is IEA:UniProtKB-UniPathway (computational), while the pathway assignment (Alkaloid biosynthesis) has experimental evidence (ECO:0000269). The broad 'biosynthetic process' is supported regardless of the specific sub-pathway label.
- The reviewer-only evidence identifies the protein as OkaE from Penicillium ochrochloron; this identity was not provided to the evaluated model. The reasoning argument relies on sequence motif recognition and family-level knowledge, not on the specific accession.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains hallmarks of the iron/alpha-ketoglutarate (Fe(II)/2OG) dioxygenase superfamily: the 2-His-1-carboxylate facial triad is visible in motifs such as 'HNDHG' (two histidines) and 'HGDYWLLNGM' (H...D carboxylate spacing), plus 'VILGSHRWPQ' (GSH region). This is a well-known superfamily whose members are overwhelmingly biosynthetic enzymes (e.g., gibberellin 2-oxidases, antibiotic tailoring enzymes, amino acid hydroxylases, secondary metabolite cyclases). A model recognizing this family can infer a biosynthetic role. Furthermore, 'pollen wall assembly' (A) is a plant-specific process absent in fungi, and 'response to cytokine' (D) is an animal immune signaling process; the sequence lacks any nuclear transport or RNA-binding domains needed for (B). The combination of 2OG oxygenase family recognition (transferable from many characterized homologs) and elimination of organism/class-specific distractors meaningfully distinguishes C from A, B, and D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Recognition of the Fe(II)/2OG oxygenase facial triad from the sequence, combined with the well-established family-level pattern that these enzymes predominantly catalyze biosynthetic transformations, provides a concrete transferable inference. Elimination of pollen (plant-specific), cytokine (animal-specific), and RNA export (no relevant domains) further narrows to C. No target-specific database lookup is required."
  },
  "case_id": "GO_biological_process_0113",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "C8",
      "GO3",
      "GO5"
    ],
    "judgment": "supported",
    "reason": "The protein is OkaE, an iron/alpha-ketoglutarate-dependent dioxygenase in the okaramine biosynthetic gene cluster. UniProt annotates it with GO:0016114 (terpenoid biosynthetic process), which is a descendant of GO:0009058 (biosynthetic process) via the path GO:0016114 → GO:0008299 → GO:0008610 → GO:0009058. The pathway is explicitly labeled 'Alkaloid biosynthesis' and 'Secondary metabolite biosynthesis; terpenoid biosynthesis' with experimental evidence (ECO:0000269, PubMed:28631282, PubMed:29384650). The broad term 'biosynthetic process' (GO:0009058) is a valid ancestor of the specific annotation, so choice C is scientifically supported."
  },
  "important_caveats": [
    "GO:0009058 (biosynthetic process) carries the 'gocheck_do_not_annotate' subset, meaning it is rarely used as a direct annotation but is valid as an inherited ancestor term. The question's use of this broad term is acceptable as a parent-level description.",
    "The UniProt GO annotation (GO:0016114, terpenoid biosynthetic process) is IEA:UniProtKB-UniPathway (computational), while the pathway assignment (Alkaloid biosynthesis) has experimental evidence (ECO:0000269). The broad 'biosynthetic process' is supported regardless of the specific sub-pathway label.",
    "The reviewer-only evidence identifies the protein as OkaE from Penicillium ochrochloron; this identity was not provided to the evaluated model. The reasoning argument relies on sequence motif recognition and family-level knowledge, not on the specific accession."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span very different biological contexts (plant pollen, nuclear RNA transport, general biosynthesis, animal immune signaling). Only 'biosynthetic process' is consistent with a 2OG oxygenase in a fungal organism. No ambiguity among the offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0113",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein is OkaE, an iron/alpha-ketoglutarate-dependent dioxygenase in the okaramine biosynthetic gene cluster. UniProt annotates it with GO:0016114 (terpenoid biosynthetic process), which is a descendant of GO:0009058 (biosynthetic process) via the path GO:0016114 → GO:0008299 → GO:0008610 → GO:0009058. The pathway is explicitly labeled 'Alkaloid biosynthesis' and 'Secondary metabolite biosynthesis; terpenoid biosynthesis' with experimental evidence (ECO:0000269, PubMed:28631282, PubMed:29384650). The broad term 'biosynthetic process' (GO:0009058) is a valid ancestor of the specific annotation, so choice C is scientifically supported.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "C8", "GO3", "GO5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains hallmarks of the iron/alpha-ketoglutarate (Fe(II)/2OG) dioxygenase superfamily: the 2-His-1-carboxylate facial triad is visible in motifs such as 'HNDHG' (two histidines) and 'HGDYWLLNGM' (H...D carboxylate spacing), plus 'VILGSHRWPQ' (GSH region). This is a well-known superfamily whose members are overwhelmingly biosynthetic enzymes (e.g., gibberellin 2-oxidases, antibiotic tailoring enzymes, amino acid hydroxylases, secondary metabolite cyclases). A model recognizing this family can infer a biosynthetic role. Furthermore, 'pollen wall assembly' (A) is a plant-specific process absent in fungi, and 'response to cytokine' (D) is an animal immune signaling process; the sequence lacks any nuclear transport or RNA-binding domains needed for (B). The combination of 2OG oxygenase family recognition (transferable from many characterized homologs) and elimination of organism/class-specific distractors meaningfully distinguishes C from A, B, and D.",
    "missing_item_specific_fact": "",
    "reason": "Recognition of the Fe(II)/2OG oxygenase facial triad from the sequence, combined with the well-established family-level pattern that these enzymes predominantly catalyze biosynthetic transformations, provides a concrete transferable inference. Elimination of pollen (plant-specific), cytokine (animal-specific), and RNA export (no relevant domains) further narrows to C. No target-specific database lookup is required."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span very different biological contexts (plant pollen, nuclear RNA transport, general biosynthesis, animal immune signaling). Only 'biosynthetic process' is consistent with a 2OG oxygenase in a fungal organism. No ambiguity among the offered choices."
  },
  "important_caveats": [
    "GO:0009058 (biosynthetic process) carries the 'gocheck_do_not_annotate' subset, meaning it is rarely used as a direct annotation but is valid as an inherited ancestor term. The question's use of this broad term is acceptable as a parent-level description.",
    "The UniProt GO annotation (GO:0016114, terpenoid biosynthetic process) is IEA:UniProtKB-UniPathway (computational), while the pathway assignment (Alkaloid biosynthesis) has experimental evidence (ECO:0000269). The broad 'biosynthetic process' is supported regardless of the specific sub-pathway label.",
    "The reviewer-only evidence identifies the protein as OkaE from Penicillium ochrochloron; this identity was not provided to the evaluated model. The reasoning argument relies on sequence motif recognition and family-level knowledge, not on the specific accession."
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
  "benchmark_sequence_length": 300,
  "benchmark_sequence_sha256": "d3f6009a2039d1f44694d93a97eabb6e8a8f1adccc44678bab4dee0033d44a8e",
  "current_entry_audit": {
    "entryVersion": 22,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2018-10-10",
    "sequenceVersion": 1
  },
  "current_record_sha256": "9990e6a6f579d0a5380e26f04d728094e4f4bad34f420af474667124b07036bb",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 300,
  "current_source_sequence_sha256": "d3f6009a2039d1f44694d93a97eabb6e8a8f1adccc44678bab4dee0033d44a8e",
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
  "requested_accession": "A0A2Z5U507",
  "selected_historical_entry_version": 21,
  "selected_historical_record_sha256": "64ddb23c63ce009b89733028cc2d13c659d4412b3c22f48c98c262654f9060ab",
  "selected_historical_source_sequence_length": 300,
  "selected_historical_source_sequence_sha256": "d3f6009a2039d1f44694d93a97eabb6e8a8f1adccc44678bab4dee0033d44a8e",
  "selected_historical_version": {
    "accession": "A0A2Z5U507",
    "database": "Swiss-Prot",
    "entryVersion": 21,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "OKAE_PENOH",
    "sequenceVersion": 1
  }
}
```

**Qualifications:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2Z5U507.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A2Z5U507\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:24:53.902384+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9990e6a6f579d0a5380e26f04d728094e4f4bad34f420af474667124b07036bb",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2Z5U507.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2Z5U507.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":22,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2018-10-10\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:24:53.902384+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9990e6a6f579d0a5380e26f04d728094e4f4bad34f420af474667124b07036bb",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2Z5U507.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2Z5U507.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Eurotiomycetes\",\"Eurotiomycetidae\",\"Eurotiales\",\"Aspergillaceae\",\"Penicillium\"],\"scientificName\":\"Penicillium ochrochloron\",\"taxonId\":69780}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:24:53.902384+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9990e6a6f579d0a5380e26f04d728094e4f4bad34f420af474667124b07036bb",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2Z5U507.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2Z5U507.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"28631282\",\"source\":\"PubMed\"}],\"value\":\"Okaramines biosynthesis cluster protein E\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"28631282\",\"source\":\"PubMed\"}],\"value\":\"1.14.20.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"28631282\",\"source\":\"PubMed\"}],\"value\":\"Iron/alpha-ketoglutarate-dependent dioxygenase okaE\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:24:53.902384+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9990e6a6f579d0a5380e26f04d728094e4f4bad34f420af474667124b07036bb",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2Z5U507.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2Z5U507.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"28631282\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"29384650\",\"source\":\"PubMed\"}],\"value\":\"Iron/alpha-ketoglutarate-dependent dioxygenase; part of the gene cluster that mediates the biosynthesis of okaramine B, a prenylated indole alkaloid that possesses an unusual octacyclic ring system, including a four-membered azetidine ring and an eight-membered azocine ring, and that exhibits insecticidal activity against silkworm larvae (PubMed:28631282, PubMed:29384650). Within the pathway, okaE forms the unusual 2-dimethyl-3-methyl-azetidine ring to yield 12-deshydroxyl okaramine E from okaramine A (PubMed:28631282). OkaE also catalyzes the hydroxylation of 12-deshydroxyl okaramine E to produce okaramine E (PubMed:28631282). The biosynthesis begins with the NRPS okaA that condenses two tryptophan molecules into cyclo(L-Trp-L-Trp). Prenylation by the prenyltransferase okaC then leads to the formation of cyclo(N8-(alpha,alpha-dimethylallyl)-L-Trp-6a-(alpha,alpha-dime-thylallyl)-L-Trp). This is followed by indole 2,3-epoxidation by the FAD-dependent monooxygenase okaB to facilitate the formation of the hexahydropyrrolo[2,3-b]indole (HPI) moiety of okaramine C. The cytochrome P450 monooxygenase okaD then likely catalyzes formation of the eight-membered ring of okaramine A. The dioxygenase okaE further forms the unusual 2-dimethyl-3-methyl-azetidine ring to yield 12-deshydroxyl okaramine E, as well as the hydroxylation of 12-deshydroxyl okaramine E to produce okaramine E. The cytochrome P450 monooxygenase okaG converts 12-deshydroxyl okaramine E into 3-desmethyl okaramine B which is further methylated by the methyltransferase okaF into okaramine B. In a shunt pathway, okaG and okaF together are also able to convert okaramine E into okaramine D (PubMed:28631282, PubMed:29384650). Okaramine H is produced by nonenzymatic conversion from okaramine A (PubMed:29384650)\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-02T04:24:53.902384+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9990e6a6f579d0a5380e26f04d728094e4f4bad34f420af474667124b07036bb",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2Z5U507.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2Z5U507.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"28631282\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"29384650\",\"source\":\"PubMed\"}],\"value\":\"Alkaloid biosynthesis\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/5",
  "retrieved_utc": "2026-11-02T04:24:53.902384+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9990e6a6f579d0a5380e26f04d728094e4f4bad34f420af474667124b07036bb",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2Z5U507.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2Z5U507.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"value\":\"Secondary metabolite biosynthesis; terpenoid biosynthesis\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/6",
  "retrieved_utc": "2026-11-02T04:24:53.902384+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9990e6a6f579d0a5380e26f04d728094e4f4bad34f420af474667124b07036bb",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2Z5U507.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2Z5U507.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0016114\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"P:terpenoid biosynthetic process\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:UniProtKB-UniPathway\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/4",
  "retrieved_utc": "2026-11-02T04:24:53.902384+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9990e6a6f579d0a5380e26f04d728094e4f4bad34f420af474667124b07036bb",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2Z5U507.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2Z5U507.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"citation\":{\"authors\":[\"Kato N.\",\"Furutani S.\",\"Otaka J.\",\"Noguchi A.\",\"Kinugasa K.\",\"Kai K.\",\"Hayashi H.\",\"Ihara M.\",\"Takahashi S.\",\"Matsuda K.\",\"Osada H.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"29384650\"},{\"database\":\"DOI\",\"id\":\"10.1021/acschembio.7b00878\"}],\"citationType\":\"journal article\",\"firstPage\":\"561\",\"id\":\"29384650\",\"journal\":\"ACS Chem. Biol.\",\"lastPage\":\"566\",\"publicationDate\":\"2018\",\"title\":\"Biosynthesis and Structure-Activity Relationship Studies of Okaramines That Target Insect Glutamate-Gated Chloride Channels.\",\"volume\":\"13\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"ATCC 90288 / AK-40\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"FUNCTION\",\"DISRUPTION PHENOTYPE\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:24:53.902384+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9990e6a6f579d0a5380e26f04d728094e4f4bad34f420af474667124b07036bb",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2Z5U507.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2Z5U507.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"citation\":{\"authors\":[\"Lai C.Y.\",\"Lo I.W.\",\"Hewage R.T.\",\"Chen Y.C.\",\"Chen C.T.\",\"Lee C.F.\",\"Lin S.\",\"Tang M.C.\",\"Lin H.C.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"28631282\"},{\"database\":\"DOI\",\"id\":\"10.1002/anie.201705501\"}],\"citationType\":\"journal article\",\"firstPage\":\"9478\",\"id\":\"28631282\",\"journal\":\"Angew. Chem. Int. Ed.\",\"lastPage\":\"9482\",\"publicationDate\":\"2017\",\"title\":\"Biosynthesis of Complex Indole Alkaloids: Elucidation of the Concise Pathway of Okaramines.\",\"volume\":\"56\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:24:53.902384+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9990e6a6f579d0a5380e26f04d728094e4f4bad34f420af474667124b07036bb",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2Z5U507.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2Z5U507?format=txt&versions=21)

```json
{
  "entry_version": 21,
  "evidence_id": "H1",
  "excerpt": "ID   OKAE_PENOH              Reviewed;         300 AA.\nAC   A0A2Z5U507;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   10-OCT-2018, sequence version 1.\nDT   28-JAN-2026, entry version 21.\nDE   RecName: Full=Iron/alpha-ketoglutarate-dependent dioxygenase okaE {ECO:0000303|PubMed:28631282};\nDE            EC=1.14.20.- {ECO:0000269|PubMed:28631282};\nDE   AltName: Full=Okaramines biosynthesis cluster protein E {ECO:0000303|PubMed:28631282};\nGN   Name=okaE {ECO:0000303|PubMed:28631282};\nOS   Penicillium ochrochloron.\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;\nOC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Penicillium.\nOX   NCBI_TaxID=69780;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:56.491248+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "64ddb23c63ce009b89733028cc2d13c659d4412b3c22f48c98c262654f9060ab",
  "url": "https://rest.uniprot.org/unisave/A0A2Z5U507?format=txt&versions=21"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2Z5U507?format=txt&versions=21)

```json
{
  "entry_version": 21,
  "evidence_id": "H2",
  "excerpt": "RN   [1]\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, DISRUPTION PHENOTYPE, AND\nRP   PATHWAY.\nRC   STRAIN=ATCC 90288 / AK-40;\nRX   PubMed=29384650; DOI=10.1021/acschembio.7b00878;\nRA   Kato N., Furutani S., Otaka J., Noguchi A., Kinugasa K., Kai K.,\nRA   Hayashi H., Ihara M., Takahashi S., Matsuda K., Osada H.;\nRT   \"Biosynthesis and Structure-Activity Relationship Studies of Okaramines\nRT   That Target Insect Glutamate-Gated Chloride Channels.\";\nRL   ACS Chem. Biol. 13:561-566(2018).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:56.491248+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 14-23",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "64ddb23c63ce009b89733028cc2d13c659d4412b3c22f48c98c262654f9060ab",
  "url": "https://rest.uniprot.org/unisave/A0A2Z5U507?format=txt&versions=21"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2Z5U507?format=txt&versions=21)

```json
{
  "entry_version": 21,
  "evidence_id": "H3",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, AND PATHWAY.\nRX   PubMed=28631282; DOI=10.1002/anie.201705501;\nRA   Lai C.Y., Lo I.W., Hewage R.T., Chen Y.C., Chen C.T., Lee C.F., Lin S.,\nRA   Tang M.C., Lin H.C.;\nRT   \"Biosynthesis of Complex Indole Alkaloids: Elucidation of the Concise\nRT   Pathway of Okaramines.\";\nRL   Angew. Chem. Int. Ed. 56:9478-9482(2017).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:56.491248+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 24-31",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "64ddb23c63ce009b89733028cc2d13c659d4412b3c22f48c98c262654f9060ab",
  "url": "https://rest.uniprot.org/unisave/A0A2Z5U507?format=txt&versions=21"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2Z5U507?format=txt&versions=21)

```json
{
  "entry_version": 21,
  "evidence_id": "H4",
  "excerpt": "CC   -!- FUNCTION: Iron/alpha-ketoglutarate-dependent dioxygenase; part of the\nCC       gene cluster that mediates the biosynthesis of okaramine B, a\nCC       prenylated indole alkaloid that possesses an unusual octacyclic ring\nCC       system, including a four-membered azetidine ring and an eight-membered\nCC       azocine ring, and that exhibits insecticidal activity against silkworm\nCC       larvae (PubMed:28631282, PubMed:29384650). Within the pathway, okaE\nCC       forms the unusual 2-dimethyl-3-methyl-azetidine ring to yield 12-\nCC       deshydroxyl okaramine E from okaramine A (PubMed:28631282). OkaE also\nCC       catalyzes the hydroxylation of 12-deshydroxyl okaramine E to produce\nCC       okaramine E (PubMed:28631282). The biosynthesis begins with the NRPS\nCC       okaA that condenses two tryptophan molecules into cyclo(L-Trp-L-Trp).\nCC       Prenylation by the prenyltransferase okaC then leads to the formation\nCC       of cyclo(N8-(alpha,alpha-dimethylallyl)-L-Trp-6a-(alpha,alpha-dime-\nCC       thylallyl)-L-Trp). This is followed by indole 2,3-epoxidation by the\nCC       FAD-dependent monooxygenase okaB to facilitate the formation of the\nCC       hexahydropyrrolo[2,3-b]indole (HPI) moiety of okaramine C. The\nCC       cytochrome P450 monooxygenase okaD then likely catalyzes formation of\nCC       the eight-membered ring of okaramine A. The dioxygenase okaE further\nCC       forms the unusual 2-dimethyl-3-methyl-azetidine ring to yield 12-\nCC       deshydroxyl okaramine E, as well as the hydroxylation of 12-deshydroxyl\nCC       okaramine E to produce okaramine E. The cytochrome P450 monoxygenase\nCC       okaG converts 12-deshydroxyl okaramine E into 3-desmethyl okaramine B\nCC       which is further methylated by the methyltransferase okaF into\nCC       okaramine B. In a shunt pathway, okaG and okaF together are also able\nCC       to convert okaramine E into okaramine D (PubMed:28631282,\nCC       PubMed:29384650). Okaramine H is produced by nonenzymatic conversion\nCC       from okaramine A (PubMed:29384650). {ECO:0000269|PubMed:28631282,\nCC       ECO:0000269|PubMed:29384650}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:56.491248+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 32-59",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "64ddb23c63ce009b89733028cc2d13c659d4412b3c22f48c98c262654f9060ab",
  "url": "https://rest.uniprot.org/unisave/A0A2Z5U507?format=txt&versions=21"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2Z5U507?format=txt&versions=21)

```json
{
  "entry_version": 21,
  "evidence_id": "H5",
  "excerpt": "CC   -!- PATHWAY: Alkaloid biosynthesis. {ECO:0000269|PubMed:28631282,\nCC       ECO:0000269|PubMed:29384650}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:56.491248+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 87-88",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "64ddb23c63ce009b89733028cc2d13c659d4412b3c22f48c98c262654f9060ab",
  "url": "https://rest.uniprot.org/unisave/A0A2Z5U507?format=txt&versions=21"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2Z5U507?format=txt&versions=21)

```json
{
  "entry_version": 21,
  "evidence_id": "H6",
  "excerpt": "CC   -!- PATHWAY: Secondary metabolite biosynthesis; terpenoid biosynthesis.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:56.491248+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 89-89",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "64ddb23c63ce009b89733028cc2d13c659d4412b3c22f48c98c262654f9060ab",
  "url": "https://rest.uniprot.org/unisave/A0A2Z5U507?format=txt&versions=21"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0008299\nname: isoprenoid biosynthetic process\nnamespace: biological_process\nalt_id: GO:0009241\ndef: \"The chemical reactions and pathways resulting in the formation of an isoprenoid compound, isoprene (2-methylbuta-1,3-diene) or compounds containing or derived from linked isoprene (3-methyl-2-butenylene) residues.\" [ISBN:0198506732]\nsynonym: \"isoprenoid anabolism\" EXACT []\nsynonym: \"isoprenoid biosynthesis\" EXACT []\nsynonym: \"isoprenoid formation\" EXACT []\nsynonym: \"isoprenoid synthesis\" EXACT []\nsynonym: \"polyisoprenoid anabolism\" NARROW []\nsynonym: \"polyisoprenoid biosynthesis\" NARROW []\nsynonym: \"polyisoprenoid biosynthetic process\" NARROW []\nsynonym: \"polyisoprenoid formation\" NARROW []\nsynonym: \"polyisoprenoid synthesis\" NARROW []\nsynonym: \"polyterpene biosynthesis\" NARROW []\nsynonym: \"polyterpene biosynthetic process\" NARROW []\nxref: MetaCyc:POLYISOPRENSYN-PWY\nis_a: GO:0006720 ! isoprenoid metabolic process\nis_a: GO:0008610 ! lipid biosynthetic process\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0008299",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 81762-81782",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO2",
  "excerpt": "[Term]\nid: GO:0008610\nname: lipid biosynthetic process\nnamespace: biological_process\ndef: \"The chemical reactions and pathways resulting in the formation of lipids, compounds soluble in an organic solvent but not, or sparingly, in an aqueous solvent.\" [GOC:curators]\nsynonym: \"lipid anabolism\" EXACT []\nsynonym: \"lipid biosynthesis\" EXACT []\nsynonym: \"lipid formation\" EXACT []\nsynonym: \"lipid synthesis\" EXACT []\nsynonym: \"lipogenesis\" EXACT [GOC:sl]\nis_a: GO:0006629 ! lipid metabolic process\nis_a: GO:0009058 ! biosynthetic process\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0008610",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 85448-85460",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO3",
  "excerpt": "[Term]\nid: GO:0009058\nname: biosynthetic process\nnamespace: biological_process\nalt_id: GO:0044274\nalt_id: GO:0044711\ndef: \"A cellular process consisting of the biochemical pathways by which a living organism synthesizes chemical substances. This typically represents the energy-requiring part of metabolism in which simpler substances are transformed into more complex ones.\" [GOC:curators, ISBN:0198547684]\nsubset: gocheck_do_not_annotate\nsubset: goslim_chembl\nsubset: goslim_metagenomics\nsubset: goslim_plant\nsubset: goslim_plant_ribbon\nsynonym: \"anabolism\" EXACT []\nsynonym: \"biosynthesis\" EXACT []\nsynonym: \"formation\" BROAD []\nsynonym: \"multicellular organismal biosynthetic process\" NARROW []\nsynonym: \"single-organism biosynthetic process\" RELATED []\nsynonym: \"synthesis\" EXACT []\nxref: Wikipedia:Anabolism\nis_a: GO:0008152 ! metabolic process\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0009058",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 92248-92268",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO4

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO4",
  "excerpt": "[Term]\nid: GO:0010208\nname: pollen wall assembly\nnamespace: biological_process\ndef: \"The formation of reticulate pollen wall pattern consisting of two layers, exine and intine.\" [PMID:11743117]\nsynonym: \"pollen wall formation\" RELATED [GOC:dph, GOC:tb]\nis_a: GO:0010927 ! cellular component assembly involved in morphogenesis\nis_a: GO:0045229 ! external encapsulating structure organization\nrelationship: part_of GO:0009555 ! pollen development\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0010208",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 103869-103878",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO5

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO5",
  "excerpt": "[Term]\nid: GO:0016114\nname: terpenoid biosynthetic process\nnamespace: biological_process\ndef: \"The chemical reactions and pathways resulting in the formation of terpenoids, any member of a class of compounds characterized by an isoprenoid chemical structure.\" [GOC:ai]\nsynonym: \"terpenoid anabolism\" EXACT []\nsynonym: \"terpenoid biosynthesis\" EXACT []\nsynonym: \"terpenoid formation\" EXACT []\nsynonym: \"terpenoid synthesis\" EXACT []\nxref: Wikipedia:Terpenoid\nis_a: GO:0006721 ! terpenoid metabolic process\nis_a: GO:0008299 ! isoprenoid biosynthetic process\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0016114",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 123609-123621",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO6

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO6",
  "excerpt": "[Term]\nid: GO:0034097\nname: response to cytokine\nnamespace: biological_process\ndef: \"Any process that results in a change in state or activity of a cell or an organism (in terms of movement, secretion, enzyme production, gene expression, etc.) as a result of a cytokine stimulus.\" [GOC:sl]\nsynonym: \"response to cytokine stimulus\" EXACT [GOC:dos]\nxref: Reactome:R-HSA-9645135 \"STAT5 Activation\"\nis_a: GO:1901652 ! response to peptide\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0034097",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 205545-205553",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO7

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO7",
  "excerpt": "[Term]\nid: GO:0046832\nname: negative regulation of RNA export from nucleus\nnamespace: biological_process\ndef: \"Any process that stops, prevents, or reduces the frequency, rate or extent of the directed movement of RNA from the nucleus into the cytoplasm.\" [GOC:bf]\nsynonym: \"down regulation of RNA export from nucleus\" EXACT []\nsynonym: \"down-regulation of RNA export from nucleus\" EXACT []\nsynonym: \"downregulation of RNA export from nucleus\" EXACT []\nsynonym: \"inhibition of RNA export from nucleus\" NARROW []\nsynonym: \"negative regulation of RNA export from cell nucleus\" EXACT []\nsynonym: \"negative regulation of RNA export out of nucleus\" EXACT []\nsynonym: \"negative regulation of RNA transport from nucleus to cytoplasm\" EXACT []\nsynonym: \"negative regulation of RNA-nucleus export\" EXACT []\nis_a: GO:0032240 ! negative regulation of nucleobase-containing compound transport\nis_a: GO:0046823 ! negative regulation of nucleocytoplasmic transport\nis_a: GO:0046831 ! regulation of RNA export from nucleus\nrelationship: negatively_regulates GO:0006405 ! RNA export from nucleus\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0046832",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 280910-280927",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 113. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
