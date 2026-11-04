# GO_cellular_component_0149

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_cellular_component_0149.txt)

**Task:** `GO_cellular_component`  
**Expected answer:** **D** — nuclear membrane

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MKYTLEGSNARVIAKAVQSLSKVGKEMFIEIDQQSLQMRAINATQSAVGSISFKRSMFEVYDMPPHSDFYCKISMKGCLAVFRNMNEVEYCELNLLDNQTNLQVNLRCKLETTKEATISIIDDQNINTNINTDQMPNIIRGDHKLLTDISNNFNSSEEELTLEANSGSVVAKNYIEGARVNDKFMRTQLKLKPSEFEQYQVTKETVITFCIKEFRAFLLFAECLNASLTLEFDEAGMPFLLKIKKHGEIECLLIMSTLSPDDISFSEDYCQKDLTVQDEDVRAAAAKRKSSVSKPNVTNKRKGSSSEPAAVQPKRRVEETQLESSLDNPLFQFRDSEAPSVQHPRILAEVDTVVLIEDEAEQEALMLAAADAALEASMAPAPEPPNSTEVCFINTDDSQQPKPAKSSSDEDETIPQSPERPNKVLGVLLGLLQGCVSRLKTMLRLDEHLISGYELL

[Multiple Choices]
A. ribonucleoprotein complex
B. phosphopantothenoylcysteine decarboxylase complex
C. trans-Golgi network membrane
D. nuclear membrane
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Cellular Component Prediction, which is to predict the primary Cellular Component where a protein is located, according to the Gene Ontology (GO) framework. A protein's location within a cell (e.g., Nucleus, Mitochondria, Cytoplasm) is critical for its function and is often determined by specific targeting signals in its amino acid sequence. Based on the provided sequence, you must identify the most likely compartment where the protein resides.. The inputs provided by the user for this task include:

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

> The sequence-matched UniProt record reports experimental localization of isoform A at the nuclear envelope, including colocalization with lamin at the nuclear periphery; it also carries an experimentally supported nuclear-envelope GO annotation. This supports the offered nuclear membrane choice, though the record notes that isoform B localizes to the nucleus.

Citations as saved: [C5](#evidence-c5), [C8](#evidence-c8).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a basic, lysine-rich C-terminal region and resembles a checkpoint-clamp protein such as Rad9; transferable knowledge of DNA-damage checkpoint proteins supports a nuclear destination. It lacks an evident transmembrane segment or secretory signal, making the trans-Golgi network membrane option unlikely, while the specific CoA-enzyme complex and an RNA-containing complex are poor fits. Among these choices, nuclear membrane is the credible nuclear option.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family/function-level and sequence-based reasoning meaningfully favors D among the offered alternatives. However, the more specific association with the nuclear periphery is not guaranteed by nuclear localization signals or checkpoint-clamp identity alone; the reviewer-only experimental annotation supports that finer localization but is not needed to distinguish D from these alternatives.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No other offered choice is comparably supported by the sequence and transferable biological context.


### Important caveats

- The source reports isoform-specific localization: isoform A is at the nuclear envelope, whereas isoform B is reported in the nucleus.
- Nuclear-envelope localization is not the same as proving that the protein is an integral membrane protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a basic, lysine-rich C-terminal region and resembles a checkpoint-clamp protein such as Rad9; transferable knowledge of DNA-damage checkpoint proteins supports a nuclear destination. It lacks an evident transmembrane segment or secretory signal, making the trans-Golgi network membrane option unlikely, while the specific CoA-enzyme complex and an RNA-containing complex are poor fits. Among these choices, nuclear membrane is the credible nuclear option.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family/function-level and sequence-based reasoning meaningfully favors D among the offered alternatives. However, the more specific association with the nuclear periphery is not guaranteed by nuclear localization signals or checkpoint-clamp identity alone; the reviewer-only experimental annotation supports that finer localization but is not needed to distinguish D from these alternatives."
  },
  "case_id": "GO_cellular_component_0149",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C8"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record reports experimental localization of isoform A at the nuclear envelope, including colocalization with lamin at the nuclear periphery; it also carries an experimentally supported nuclear-envelope GO annotation. This supports the offered nuclear membrane choice, though the record notes that isoform B localizes to the nucleus."
  },
  "important_caveats": [
    "The source reports isoform-specific localization: isoform A is at the nuclear envelope, whereas isoform B is reported in the nucleus.",
    "Nuclear-envelope localization is not the same as proving that the protein is an integral membrane protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered choice is comparably supported by the sequence and transferable biological context."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0149",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record reports experimental localization of isoform A at the nuclear envelope, including colocalization with lamin at the nuclear periphery; it also carries an experimentally supported nuclear-envelope GO annotation. This supports the offered nuclear membrane choice, though the record notes that isoform B localizes to the nucleus.",
    "evidence_ids": ["C5", "C8"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a basic, lysine-rich C-terminal region and resembles a checkpoint-clamp protein such as Rad9; transferable knowledge of DNA-damage checkpoint proteins supports a nuclear destination. It lacks an evident transmembrane segment or secretory signal, making the trans-Golgi network membrane option unlikely, while the specific CoA-enzyme complex and an RNA-containing complex are poor fits. Among these choices, nuclear membrane is the credible nuclear option.",
    "missing_item_specific_fact": "",
    "reason": "Family/function-level and sequence-based reasoning meaningfully favors D among the offered alternatives. However, the more specific association with the nuclear periphery is not guaranteed by nuclear localization signals or checkpoint-clamp identity alone; the reviewer-only experimental annotation supports that finer localization but is not needed to distinguish D from these alternatives."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered choice is comparably supported by the sequence and transferable biological context."
  },
  "important_caveats": [
    "The source reports isoform-specific localization: isoform A is at the nuclear envelope, whereas isoform B is reported in the nucleus.",
    "Nuclear-envelope localization is not the same as proving that the protein is an integral membrane protein."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein is Drosophila melanogaster Rad9 (UniProt O96533), a component of the 9-1-1 checkpoint clamp complex. Experimental evidence (PubMed:22666434, ECO:0000269) shows Isoform A colocalizes with lamin at the nuclear periphery, annotated as 'Nucleus envelope' (GO:0005635). The GO term 'nuclear membrane' (GO:0031965) is part_of nuclear envelope, and the primary paper title explicitly states 'Localization of the Drosophila Rad9 protein to the nuclear membrane.' The expected answer D is well-supported by direct experimental colocalization data.

Citations as saved: [C5](#evidence-c5), [C8](#evidence-c8), [C10](#evidence-c10), [H3](#evidence-h3), [GO1](#evidence-go1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a Rad9/Hus1-like fold (the 9-1-1 checkpoint clamp family, structurally related to PCNA/RFC subunits), identifiable by the conserved domain architecture (e.g., 'FIEIDQQSLQMRAINATQSAVGSISFKRSMFEVYDMPPHSDFYCKISMKGCLAVFRNMNEVEYCELNLLDNQTNLQVNLRCKLETTKEATISIIDDQNINTNINTDQMPNIIRGDHKLLTDISNNFNSSEEELTLEANSGSVVAKNYIEGARVNDKFMRTQLKLKPSEFEQYQVTKETVITFCIKEFRAFLLFAECLNASLTLEFDEAGMPFLLKIKKHGEIECLLIMSTLSPDDISFSEDYCQKDLTVQDEDVRAAAAKRK'). The 9-1-1 complex (Rad9/Rad1/Hus1) is a well-characterized nuclear DNA damage sensor across eukaryotes (yeast, human, Drosophila). The C-terminal region contains clusters of basic residues ('KRKSSVSKPNVTNKRKGSSSEPAAVQPKRRVEETQ') consistent with a bipartite nuclear localization signal. Among the four choices: (A) ribonucleoprotein complex requires RNA-binding domains (RRM, KH, etc.) absent here; (B) phosphopantothenoylcysteine decarboxylase complex is a CoA biosynthesis enzyme with no structural or sequence resemblance; (C) trans-Golgi network membrane requires transmembrane segments or Golgi-retention signals, neither present. Only (D) nuclear membrane is consistent with a nuclear checkpoint clamp protein bearing NLS motifs. Since 'nucleus' alone is not an offered option, D is the sole nuclear compartment among the choices.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level recognition of the 9-1-1 checkpoint clamp fold, combined with the presence of NLS-like basic clusters and absence of TM domains or RNA-binding motifs, allows a knowledgeable model to eliminate A, B, and C and select D. The specific nuclear membrane (vs. nucleoplasm) distinction is not required because 'nucleus' is not among the offered alternatives.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The three distractors are clearly incompatible with a DNA damage checkpoint clamp protein: no RNA-binding domains (eliminates A), no CoA-biosynthesis enzymatic features (eliminates B), and no transmembrane/Golgi-targeting motifs (eliminates C). D is the only nuclear option and the only one consistent with the protein family.


### Important caveats

- The UniProt annotation records 'Nucleus envelope' (GO:0005635) rather than 'nuclear membrane' (GO:0031965) directly; however, nuclear membrane is part_of nuclear envelope, and the primary literature uses 'nuclear membrane' language.
- Isoform B is annotated simply as 'Nucleus' without membrane specification; the question does not specify which isoform the 456-aa canonical sequence corresponds to.
- The specific nuclear membrane targeting in Drosophila Rad9 (lamin colocalization) is a relatively specific finding not shared by all Rad9 orthologs (e.g., human Rad9 is primarily nucleoplasmic), so family knowledge alone gives 'nuclear' but the membrane specificity relies on the offered option set excluding plain 'nucleus.'

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a Rad9/Hus1-like fold (the 9-1-1 checkpoint clamp family, structurally related to PCNA/RFC subunits), identifiable by the conserved domain architecture (e.g., 'FIEIDQQSLQMRAINATQSAVGSISFKRSMFEVYDMPPHSDFYCKISMKGCLAVFRNMNEVEYCELNLLDNQTNLQVNLRCKLETTKEATISIIDDQNINTNINTDQMPNIIRGDHKLLTDISNNFNSSEEELTLEANSGSVVAKNYIEGARVNDKFMRTQLKLKPSEFEQYQVTKETVITFCIKEFRAFLLFAECLNASLTLEFDEAGMPFLLKIKKHGEIECLLIMSTLSPDDISFSEDYCQKDLTVQDEDVRAAAAKRK'). The 9-1-1 complex (Rad9/Rad1/Hus1) is a well-characterized nuclear DNA damage sensor across eukaryotes (yeast, human, Drosophila). The C-terminal region contains clusters of basic residues ('KRKSSVSKPNVTNKRKGSSSEPAAVQPKRRVEETQ') consistent with a bipartite nuclear localization signal. Among the four choices: (A) ribonucleoprotein complex requires RNA-binding domains (RRM, KH, etc.) absent here; (B) phosphopantothenoylcysteine decarboxylase complex is a CoA biosynthesis enzyme with no structural or sequence resemblance; (C) trans-Golgi network membrane requires transmembrane segments or Golgi-retention signals, neither present. Only (D) nuclear membrane is consistent with a nuclear checkpoint clamp protein bearing NLS motifs. Since 'nucleus' alone is not an offered option, D is the sole nuclear compartment among the choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level recognition of the 9-1-1 checkpoint clamp fold, combined with the presence of NLS-like basic clusters and absence of TM domains or RNA-binding motifs, allows a knowledgeable model to eliminate A, B, and C and select D. The specific nuclear membrane (vs. nucleoplasm) distinction is not required because 'nucleus' is not among the offered alternatives."
  },
  "case_id": "GO_cellular_component_0149",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C8",
      "C10",
      "H3",
      "GO1"
    ],
    "judgment": "supported",
    "reason": "The protein is Drosophila melanogaster Rad9 (UniProt O96533), a component of the 9-1-1 checkpoint clamp complex. Experimental evidence (PubMed:22666434, ECO:0000269) shows Isoform A colocalizes with lamin at the nuclear periphery, annotated as 'Nucleus envelope' (GO:0005635). The GO term 'nuclear membrane' (GO:0031965) is part_of nuclear envelope, and the primary paper title explicitly states 'Localization of the Drosophila Rad9 protein to the nuclear membrane.' The expected answer D is well-supported by direct experimental colocalization data."
  },
  "important_caveats": [
    "The UniProt annotation records 'Nucleus envelope' (GO:0005635) rather than 'nuclear membrane' (GO:0031965) directly; however, nuclear membrane is part_of nuclear envelope, and the primary literature uses 'nuclear membrane' language.",
    "Isoform B is annotated simply as 'Nucleus' without membrane specification; the question does not specify which isoform the 456-aa canonical sequence corresponds to.",
    "The specific nuclear membrane targeting in Drosophila Rad9 (lamin colocalization) is a relatively specific finding not shared by all Rad9 orthologs (e.g., human Rad9 is primarily nucleoplasmic), so family knowledge alone gives 'nuclear' but the membrane specificity relies on the offered option set excluding plain 'nucleus.'"
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors are clearly incompatible with a DNA damage checkpoint clamp protein: no RNA-binding domains (eliminates A), no CoA-biosynthesis enzymatic features (eliminates B), and no transmembrane/Golgi-targeting motifs (eliminates C). D is the only nuclear option and the only one consistent with the protein family."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0149",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein is Drosophila melanogaster Rad9 (UniProt O96533), a component of the 9-1-1 checkpoint clamp complex. Experimental evidence (PubMed:22666434, ECO:0000269) shows Isoform A colocalizes with lamin at the nuclear periphery, annotated as 'Nucleus envelope' (GO:0005635). The GO term 'nuclear membrane' (GO:0031965) is part_of nuclear envelope, and the primary paper title explicitly states 'Localization of the Drosophila Rad9 protein to the nuclear membrane.' The expected answer D is well-supported by direct experimental colocalization data.",
    "evidence_ids": ["C5", "C8", "C10", "H3", "GO1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a Rad9/Hus1-like fold (the 9-1-1 checkpoint clamp family, structurally related to PCNA/RFC subunits), identifiable by the conserved domain architecture (e.g., 'FIEIDQQSLQMRAINATQSAVGSISFKRSMFEVYDMPPHSDFYCKISMKGCLAVFRNMNEVEYCELNLLDNQTNLQVNLRCKLETTKEATISIIDDQNINTNINTDQMPNIIRGDHKLLTDISNNFNSSEEELTLEANSGSVVAKNYIEGARVNDKFMRTQLKLKPSEFEQYQVTKETVITFCIKEFRAFLLFAECLNASLTLEFDEAGMPFLLKIKKHGEIECLLIMSTLSPDDISFSEDYCQKDLTVQDEDVRAAAAKRK'). The 9-1-1 complex (Rad9/Rad1/Hus1) is a well-characterized nuclear DNA damage sensor across eukaryotes (yeast, human, Drosophila). The C-terminal region contains clusters of basic residues ('KRKSSVSKPNVTNKRKGSSSEPAAVQPKRRVEETQ') consistent with a bipartite nuclear localization signal. Among the four choices: (A) ribonucleoprotein complex requires RNA-binding domains (RRM, KH, etc.) absent here; (B) phosphopantothenoylcysteine decarboxylase complex is a CoA biosynthesis enzyme with no structural or sequence resemblance; (C) trans-Golgi network membrane requires transmembrane segments or Golgi-retention signals, neither present. Only (D) nuclear membrane is consistent with a nuclear checkpoint clamp protein bearing NLS motifs. Since 'nucleus' alone is not an offered option, D is the sole nuclear compartment among the choices.",
    "missing_item_specific_fact": "",
    "reason": "Family-level recognition of the 9-1-1 checkpoint clamp fold, combined with the presence of NLS-like basic clusters and absence of TM domains or RNA-binding motifs, allows a knowledgeable model to eliminate A, B, and C and select D. The specific nuclear membrane (vs. nucleoplasm) distinction is not required because 'nucleus' is not among the offered alternatives."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors are clearly incompatible with a DNA damage checkpoint clamp protein: no RNA-binding domains (eliminates A), no CoA-biosynthesis enzymatic features (eliminates B), and no transmembrane/Golgi-targeting motifs (eliminates C). D is the only nuclear option and the only one consistent with the protein family."
  },
  "important_caveats": [
    "The UniProt annotation records 'Nucleus envelope' (GO:0005635) rather than 'nuclear membrane' (GO:0031965) directly; however, nuclear membrane is part_of nuclear envelope, and the primary literature uses 'nuclear membrane' language.",
    "Isoform B is annotated simply as 'Nucleus' without membrane specification; the question does not specify which isoform the 456-aa canonical sequence corresponds to.",
    "The specific nuclear membrane targeting in Drosophila Rad9 (lamin colocalization) is a relatively specific finding not shared by all Rad9 orthologs (e.g., human Rad9 is primarily nucleoplasmic), so family knowledge alone gives 'nuclear' but the membrane specificity relies on the offered option set excluding plain 'nucleus.'"
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
  "benchmark_sequence_length": 456,
  "benchmark_sequence_sha256": "049fbc2622dccdc87ef624b34249d33170a7b8c2b478ce2e3efeaa20707cd08e",
  "current_entry_audit": {
    "entryVersion": 173,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "1999-05-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "bb99e71f5e8a793ade93b27d828f52cb97398645ffefb83e64700635ebcbf030",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 456,
  "current_source_sequence_sha256": "049fbc2622dccdc87ef624b34249d33170a7b8c2b478ce2e3efeaa20707cd08e",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 171,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "O96533",
  "selected_historical_entry_version": 171,
  "selected_historical_record_sha256": "382fa0ff4b386f2a325cd0f8b4b5cfa06539582a3119d8a8b62f942b38c935a2",
  "selected_historical_source_sequence_length": 456,
  "selected_historical_source_sequence_sha256": "049fbc2622dccdc87ef624b34249d33170a7b8c2b478ce2e3efeaa20707cd08e",
  "selected_historical_version": {
    "accession": "O96533",
    "database": "Swiss-Prot",
    "entryVersion": 171,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "RAD9_DROME",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O96533.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"O96533\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:29:20.443840+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bb99e71f5e8a793ade93b27d828f52cb97398645ffefb83e64700635ebcbf030",
  "url": "https://rest.uniprot.org/uniprotkb/O96533.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O96533.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":173,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"1999-05-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:29:20.443840+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bb99e71f5e8a793ade93b27d828f52cb97398645ffefb83e64700635ebcbf030",
  "url": "https://rest.uniprot.org/uniprotkb/O96533.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O96533.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Fruit fly\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000000803\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Ecdysozoa\",\"Arthropoda\",\"Altocrustacea\",\"Allotriocarida\",\"Hexapoda\",\"Insecta\",\"Pterygota\",\"Neoptera\",\"Eumetabola\",\"Endopterygota\",\"Aparaglossata\",\"Panorpida\",\"Diptera\",\"Brachycera\",\"Muscomorpha\",\"Ephydroidea\",\"Drosophilidae\",\"Drosophila\",\"Sophophora\"],\"scientificName\":\"Drosophila melanogaster\",\"taxonId\":7227}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:29:20.443840+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bb99e71f5e8a793ade93b27d828f52cb97398645ffefb83e64700635ebcbf030",
  "url": "https://rest.uniprot.org/uniprotkb/O96533.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O96533.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Cell cycle checkpoint control protein Rad9\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:29:20.443840+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bb99e71f5e8a793ade93b27d828f52cb97398645ffefb83e64700635ebcbf030",
  "url": "https://rest.uniprot.org/uniprotkb/O96533.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O96533.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"SUBCELLULAR LOCATION\",\"molecule\":\"Isoform A\",\"note\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"22666434\",\"source\":\"PubMed\"}],\"value\":\"Colocalizes with lamin at the nuclear periphery (PubMed:22666434). Targets the other components of the 9-1-1 complex, Rad1 and Hus1-like to the nuclear periphery (PubMed:22666434). Targeting to the nuclear periphery is disrupted in the presence of persistent double stranded break DNA damage (PubMed:22666434)\"}]},\"subcellularLocations\":[{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"22666434\",\"source\":\"PubMed\"}],\"id\":\"SL-0178\",\"value\":\"Nucleus envelope\"}}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-02T04:29:20.443840+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bb99e71f5e8a793ade93b27d828f52cb97398645ffefb83e64700635ebcbf030",
  "url": "https://rest.uniprot.org/uniprotkb/O96533.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O96533.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"SUBCELLULAR LOCATION\",\"molecule\":\"Isoform B\",\"subcellularLocations\":[{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"22666434\",\"source\":\"PubMed\"}],\"id\":\"SL-0191\",\"value\":\"Nucleus\"}}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/4",
  "retrieved_utc": "2026-11-02T04:29:20.443840+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bb99e71f5e8a793ade93b27d828f52cb97398645ffefb83e64700635ebcbf030",
  "url": "https://rest.uniprot.org/uniprotkb/O96533.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O96533.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000314\",\"id\":\"22666434\",\"source\":\"PubMed\"}],\"id\":\"GO:0030896\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:checkpoint clamp complex\"},{\"key\":\"GoEvidenceType\",\"value\":\"IDA:FlyBase\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/36",
  "retrieved_utc": "2026-11-02T04:29:20.443840+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bb99e71f5e8a793ade93b27d828f52cb97398645ffefb83e64700635ebcbf030",
  "url": "https://rest.uniprot.org/uniprotkb/O96533.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O96533.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"22666434\",\"source\":\"PubMed\"}],\"id\":\"GO:0005635\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:nuclear envelope\"},{\"key\":\"GoEvidenceType\",\"value\":\"EXP:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/37",
  "retrieved_utc": "2026-11-02T04:29:20.443840+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bb99e71f5e8a793ade93b27d828f52cb97398645ffefb83e64700635ebcbf030",
  "url": "https://rest.uniprot.org/uniprotkb/O96533.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O96533.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000314\",\"id\":\"22666434\",\"source\":\"PubMed\"}],\"id\":\"GO:0005634\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:nucleus\"},{\"key\":\"GoEvidenceType\",\"value\":\"IDA:FlyBase\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/38",
  "retrieved_utc": "2026-11-02T04:29:20.443840+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bb99e71f5e8a793ade93b27d828f52cb97398645ffefb83e64700635ebcbf030",
  "url": "https://rest.uniprot.org/uniprotkb/O96533.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O96533.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"citation\":{\"authors\":[\"Kadir R.\",\"Bakhrat A.\",\"Tokarsky R.\",\"Abdu U.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"22666434\"},{\"database\":\"DOI\",\"id\":\"10.1371/journal.pone.0038010\"}],\"citationType\":\"journal article\",\"firstPage\":\"e38010\",\"id\":\"22666434\",\"journal\":\"PLoS ONE\",\"lastPage\":\"e38010\",\"publicationDate\":\"2012\",\"title\":\"Localization of the Drosophila Rad9 protein to the nuclear membrane is regulated by the C-terminal region and is affected in the meiotic checkpoint.\",\"volume\":\"7\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":8,\"referencePositions\":[\"FUNCTION\",\"INTERACTION WITH RAD1 AND HUS1\",\"SUBCELLULAR LOCATION\",\"ALTERNATIVE SPLICING\",\"DEVELOPMENTAL STAGE\",\"NUCLEAR LOCALIZATION SIGNAL\",\"MUTAGENESIS OF 287-LYS--LYS-289; 300-LYS--LYS-302 AND 314-LYS--ARG-316\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/7",
  "retrieved_utc": "2026-11-02T04:29:20.443840+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bb99e71f5e8a793ade93b27d828f52cb97398645ffefb83e64700635ebcbf030",
  "url": "https://rest.uniprot.org/uniprotkb/O96533.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O96533?format=txt&versions=171)

```json
{
  "entry_version": 171,
  "evidence_id": "H1",
  "excerpt": "ID   RAD9_DROME              Reviewed;         456 AA.\nAC   O96533; A8JNV5;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-MAY-1999, sequence version 1.\nDT   28-JAN-2026, entry version 171.\nDE   RecName: Full=Cell cycle checkpoint control protein Rad9 {ECO:0000305};\nGN   Name=Rad9 {ECO:0000312|FlyBase:FBgn0025807};\nGN   ORFNames=CG3945 {ECO:0000312|FlyBase:FBgn0025807};\nOS   Drosophila melanogaster (Fruit fly).\nOC   Eukaryota; Metazoa; Ecdysozoa; Arthropoda; Hexapoda; Insecta; Pterygota;\nOC   Neoptera; Endopterygota; Diptera; Brachycera; Muscomorpha; Ephydroidea;\nOC   Drosophilidae; Drosophila; Sophophora.\nOX   NCBI_TaxID=7227 {ECO:0000312|Proteomes:UP000000803};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:22.754069+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "382fa0ff4b386f2a325cd0f8b4b5cfa06539582a3119d8a8b62f942b38c935a2",
  "url": "https://rest.uniprot.org/unisave/O96533?format=txt&versions=171"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O96533?format=txt&versions=171)

```json
{
  "entry_version": 171,
  "evidence_id": "H2",
  "excerpt": "RN   [8] {ECO:0000305}\nRP   FUNCTION, INTERACTION WITH RAD1 AND HUS1, SUBCELLULAR LOCATION, ALTERNATIVE\nRP   SPLICING, DEVELOPMENTAL STAGE, NUCLEAR LOCALIZATION SIGNAL, AND MUTAGENESIS\nRP   OF 287-LYS--LYS-289; 300-LYS--LYS-302 AND 314-LYS--ARG-316.\nRX   PubMed=22666434; DOI=10.1371/journal.pone.0038010;\nRA   Kadir R., Bakhrat A., Tokarsky R., Abdu U.;\nRT   \"Localization of the Drosophila Rad9 protein to the nuclear membrane is\nRT   regulated by the C-terminal region and is affected in the meiotic\nRT   checkpoint.\";\nRL   PLoS ONE 7:e38010-e38010(2012).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:22.754069+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 104-113",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "382fa0ff4b386f2a325cd0f8b4b5cfa06539582a3119d8a8b62f942b38c935a2",
  "url": "https://rest.uniprot.org/unisave/O96533?format=txt&versions=171"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O96533?format=txt&versions=171)

```json
{
  "entry_version": 171,
  "evidence_id": "H3",
  "excerpt": "CC   -!- SUBCELLULAR LOCATION: [Isoform A]: Nucleus envelope\nCC       {ECO:0000269|PubMed:22666434}. Note=Colocalizes with lamin at the\nCC       nuclear periphery (PubMed:22666434). Targets the other components of\nCC       the 9-1-1 complex, Rad1 and Hus1-like to the nuclear periphery\nCC       (PubMed:22666434). Targeting to the nuclear periphery is disrupted in\nCC       the presence of persistent double stranded break DNA damage\nCC       (PubMed:22666434). {ECO:0000269|PubMed:22666434}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:22.754069+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 130-136",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "382fa0ff4b386f2a325cd0f8b4b5cfa06539582a3119d8a8b62f942b38c935a2",
  "url": "https://rest.uniprot.org/unisave/O96533?format=txt&versions=171"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O96533?format=txt&versions=171)

```json
{
  "entry_version": 171,
  "evidence_id": "H4",
  "excerpt": "CC   -!- SUBCELLULAR LOCATION: [Isoform B]: Nucleus\nCC       {ECO:0000269|PubMed:22666434}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:22.754069+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 137-138",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "382fa0ff4b386f2a325cd0f8b4b5cfa06539582a3119d8a8b62f942b38c935a2",
  "url": "https://rest.uniprot.org/unisave/O96533?format=txt&versions=171"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O96533?format=txt&versions=171)

```json
{
  "entry_version": 171,
  "evidence_id": "H5",
  "excerpt": "DR   GO; GO:0030896; C:checkpoint clamp complex; IDA:FlyBase.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:22.754069+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 193-193",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "382fa0ff4b386f2a325cd0f8b4b5cfa06539582a3119d8a8b62f942b38c935a2",
  "url": "https://rest.uniprot.org/unisave/O96533?format=txt&versions=171"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O96533?format=txt&versions=171)

```json
{
  "entry_version": 171,
  "evidence_id": "H6",
  "excerpt": "DR   GO; GO:0005635; C:nuclear envelope; IEA:UniProtKB-SubCell.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:22.754069+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 194-194",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "382fa0ff4b386f2a325cd0f8b4b5cfa06539582a3119d8a8b62f942b38c935a2",
  "url": "https://rest.uniprot.org/unisave/O96533?format=txt&versions=171"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O96533?format=txt&versions=171)

```json
{
  "entry_version": 171,
  "evidence_id": "H7",
  "excerpt": "DR   GO; GO:0005634; C:nucleus; IDA:FlyBase.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:22.754069+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 195-195",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "382fa0ff4b386f2a325cd0f8b4b5cfa06539582a3119d8a8b62f942b38c935a2",
  "url": "https://rest.uniprot.org/unisave/O96533?format=txt&versions=171"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0031965\nname: nuclear membrane\nnamespace: cellular_component\ndef: \"Either of the lipid bilayers that surround the nucleus and form the nuclear envelope; excludes the intermembrane space.\" [GOC:mah, GOC:pz]\nxref: NIF_Subcellular:sao1687101204\nis_a: GO:0031090 ! organelle membrane\nrelationship: part_of GO:0005635 ! nuclear envelope\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0031965",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 181475-181483",
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
  "excerpt": "[Term]\nid: GO:0032588\nname: trans-Golgi network membrane\nnamespace: cellular_component\ndef: \"The lipid bilayer surrounding any of the compartments that make up the trans-Golgi network.\" [GOC:mah]\nsynonym: \"Golgi trans face membrane\" RELATED []\nsynonym: \"trans Golgi network membrane\" EXACT []\nis_a: GO:0031090 ! organelle membrane\nrelationship: part_of GO:0005802 ! trans-Golgi network\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0032588",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 187565-187574",
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
  "excerpt": "[Term]\nid: GO:0071513\nname: phosphopantothenoylcysteine decarboxylase complex\nnamespace: cellular_component\ndef: \"A protein complex that catalyzes decarboxylation of 4'-phosphopantothenoylcysteine to yield 4'-phosphopantetheine; this is the third step in the biosynthesis of Coenzyme A. The complex is homotrimeric in many eukaryotes, but is a heterotrimer in Saccharomyces.\" [GOC:jh, PMID:19915539]\ncomment: See also the molecular function term 'acetolactate synthase activity ; GO:0003984'.\nis_a: GO:1902494 ! catalytic complex\nrelationship: part_of GO:0005737 ! cytoplasm\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0071513",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 377848-377856",
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
  "excerpt": "[Term]\nid: GO:1990904\nname: ribonucleoprotein complex\nnamespace: cellular_component\nalt_id: GO:0030529\nalt_id: GO:1990903\ndef: \"A macromolecular complex that contains both RNA and protein molecules.\" [GOC:krc, GOC:vesicles]\nsubset: goslim_pir\nsynonym: \"extracellular ribonucleoprotein complex\" NARROW []\nsynonym: \"intracellular ribonucleoprotein complex\" NARROW []\nsynonym: \"protein-RNA complex\" EXACT []\nsynonym: \"RNA-protein complex\" EXACT []\nsynonym: \"RNP\" EXACT []\nxref: Wikipedia:Ribonucleoprotein\nis_a: GO:0032991 ! protein-containing complex\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:1990904",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 556099-556114",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 149. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
