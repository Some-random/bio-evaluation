# GO_molecular_function_0091

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_molecular_function_0091.txt)

**Task:** `GO_molecular_function`  
**Expected answer:** **D** — protein serine/threonine kinase activity

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MADKETLLKLREDFKMQNKSVFILGASGETGKVLLKEILGQNLFSKVTLIGRRKLTFEEEAYNNVNQEVVDFEKLDEYAPAFQGHDVGFCCLGTTRRKAGADGFVRVDRDYVLKSAELAKAGGCKHFNLLSSRGADKSSSFLYLQVKGEVEAKVEELKFDRLSVFRPGVLLCDRQESRPGEWLARKFFGSLPDSWASGYAVPVVTVVRAMLNNLVSPGSGQMELLENKAILHLGKDSDGPKL

[Multiple Choices]
A. methionine gamma-lyase activity
B. dolichyl-phosphate-mannose-protein mannosyltransferase activity
C. protein kinase activity
D. protein serine/threonine kinase activity
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Molecular Function Prediction, which is to predict the fundamental activity of a protein at the molecular level, as defined by the Gene Ontology (GO) 'Molecular Function' branch. This describes the elemental tasks a protein performs, such as catalysis, transport, or binding to specific molecules. Based on the protein's amino acid sequence, you are to select the option that best describes its primary molecular function.. The inputs provided by the user for this task include:

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

> The exact-match sequence has a UniProt GO annotation for protein serine/threonine kinase activity (ISO:RGD), supporting the key as a computationally inferred annotation. This is not experimental confirmation: the functional description emphasizes other activities and does not independently establish kinase catalysis.

Citations as saved: [C6](#evidence-c6), [H4](#evidence-h4), [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is a compact, soluble protein and contains an N-terminal GXGXXG-like segment (GASGETG), consistent with a kinase-like nucleotide-binding loop. Transferable knowledge of eukaryotic protein kinases makes a serine/threonine kinase a plausible, more specific choice than the broad kinase option; the sequence does not show the usual full set of canonical kinase motifs, so this is a probabilistic family-level inference, not proof.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence and choices provide a meaningful basis for favoring D over the unrelated lyase and membrane mannosyltransferase options, and kinase-family regularities make the serine/threonine subtype plausible relative to the broader kinase term. The inference is limited because the sequence alone does not firmly establish kinase activity or substrate specificity.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Protein serine/threonine kinase activity is a subtype of protein kinase activity, so C is broadly true if D is true. However, the prompt asks for the best description, and D is the more specific choice.


### Important caveats

- The supporting GO annotation is inferred from sequence orthology, not direct experimental evidence of kinase activity.
- The sequence motif is suggestive rather than a complete canonical kinase signature.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is a compact, soluble protein and contains an N-terminal GXGXXG-like segment (GASGETG), consistent with a kinase-like nucleotide-binding loop. Transferable knowledge of eukaryotic protein kinases makes a serine/threonine kinase a plausible, more specific choice than the broad kinase option; the sequence does not show the usual full set of canonical kinase motifs, so this is a probabilistic family-level inference, not proof.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence and choices provide a meaningful basis for favoring D over the unrelated lyase and membrane mannosyltransferase options, and kinase-family regularities make the serine/threonine subtype plausible relative to the broader kinase term. The inference is limited because the sequence alone does not firmly establish kinase activity or substrate specificity."
  },
  "case_id": "GO_molecular_function_0091",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "H4",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The exact-match sequence has a UniProt GO annotation for protein serine/threonine kinase activity (ISO:RGD), supporting the key as a computationally inferred annotation. This is not experimental confirmation: the functional description emphasizes other activities and does not independently establish kinase catalysis."
  },
  "important_caveats": [
    "The supporting GO annotation is inferred from sequence orthology, not direct experimental evidence of kinase activity.",
    "The sequence motif is suggestive rather than a complete canonical kinase signature."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Protein serine/threonine kinase activity is a subtype of protein kinase activity, so C is broadly true if D is true. However, the prompt asks for the best description, and D is the more specific choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0091",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact-match sequence has a UniProt GO annotation for protein serine/threonine kinase activity (ISO:RGD), supporting the key as a computationally inferred annotation. This is not experimental confirmation: the functional description emphasizes other activities and does not independently establish kinase catalysis.",
    "evidence_ids": ["C6", "H4", "C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is a compact, soluble protein and contains an N-terminal GXGXXG-like segment (GASGETG), consistent with a kinase-like nucleotide-binding loop. Transferable knowledge of eukaryotic protein kinases makes a serine/threonine kinase a plausible, more specific choice than the broad kinase option; the sequence does not show the usual full set of canonical kinase motifs, so this is a probabilistic family-level inference, not proof.",
    "missing_item_specific_fact": "",
    "reason": "The sequence and choices provide a meaningful basis for favoring D over the unrelated lyase and membrane mannosyltransferase options, and kinase-family regularities make the serine/threonine subtype plausible relative to the broader kinase term. The inference is limited because the sequence alone does not firmly establish kinase activity or substrate specificity."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Protein serine/threonine kinase activity is a subtype of protein kinase activity, so C is broadly true if D is true. However, the prompt asks for the best description, and D is the more specific choice."
  },
  "important_caveats": [
    "The supporting GO annotation is inferred from sequence orthology, not direct experimental evidence of kinase activity.",
    "The sequence motif is suggestive rather than a complete canonical kinase signature."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry B0BNF8 (HTATIP2/TIP30, rat) carries GO:0004674 (protein serine/threonine kinase activity) as a database annotation. However, this annotation carries evidence code ISO:RGD (Inferred from Sequence Orthology from RGD), meaning it is a transferred annotation, not experimentally verified. The entry's own FUNCTION comment describes translation repression via eEF1A interaction, nuclear import inhibition, redox sensing, and NADPH binding — none of which is kinase activity. The annotation is therefore technically present but of low confidence and contradicted by the protein's described function. The expected answer is supported in the narrow sense that the GO term is recorded, but the underlying evidence is weak and the functional description does not corroborate it.

Citations as saved: [C6](#evidence-c6), [C5](#evidence-c5), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

Empty string, as saved.


**Missing item-specific fact**

> The specific ISO:RGD database annotation assigning GO:0004674 to this exact protein sequence. The protein (TIP30/HTATIP2) lacks canonical kinase catalytic motifs (HRD catalytic loop, DFG activation loop, VAIK lysine). The P-loop/Walker A motif (GASGETGKV) is present but is shared by GTPases, ABC transporters, and many non-kinase nucleotide-binding proteins and does not specifically indicate protein kinase activity. The protein's actual experimentally supported function (translation repression via eEF1A) is unrelated to kinase activity. No transferable family-level or sequence-feature inference from other proteins meaningfully supports assigning kinase activity to this 242-aa protein.


**Reason**

> The sequence contains a Walker A/P-loop motif (GASGETGKV), which indicates nucleotide binding but is not specific to kinases — it is found in GTPases, ABC transporters, helicases, and many other families. Critically, the sequence lacks the hallmark protein-kinase catalytic motifs: the HRD catalytic aspartate loop, the DFG activation-loop motif, and the bilobal kinase fold architecture. The protein is only 242 aa, far smaller than typical protein kinases. A knowledgeable model using transferable kinase-family knowledge would not assign kinase activity based on these features. Options C and D are in an is_a relationship (GO:0004674 is_a GO:0004672), so even if kinase activity were assumed, distinguishing the two requires knowing the substrate specificity (Ser/Thr vs Tyr), which is absent from the sequence. The expected answer D rests entirely on a low-confidence ISO:RGD transferred annotation that contradicts the protein's actual described function. Without that specific database record, biological reasoning from the sequence and general kinase-family knowledge does not produce answer D.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C",
  "D"
]
```

> GO:0004674 (option D) is_a GO:0004672 (option C). If the protein were truly a kinase, both terms would be valid annotations, with D being more specific. The question asks for the 'primary molecular function' but does not specify whether the most specific or the broader term is preferred. Without knowing substrate specificity from the sequence, a model could defensibly select either C or D. Additionally, since the protein's actual function is not kinase activity, neither C nor D is biologically accurate, but within the answer set they remain the closest options.


### Important caveats

- The GO:0004674 annotation carries evidence code ISO:RGD (transferred by orthology), not experimental evidence. The protein's own FUNCTION comment describes translation repression, not kinase activity.
- The P-loop motif (GASGETGKV) in the sequence is a Walker A nucleotide-binding motif found in many unrelated protein families and is not diagnostic of kinase activity.
- The protein (TIP30/HTATIP2) is a well-studied translation regulator and redox sensor; its kinase annotation in databases is of uncertain reliability.
- The reviewer-only evidence reveals the protein identity (HTATIP2, rat) and the ISO:RGD annotation, neither of which was available to the evaluated model.
- Options C and D are in an is_a hierarchy, creating inherent ambiguity when the protein's kinase status is itself questionable.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific ISO:RGD database annotation assigning GO:0004674 to this exact protein sequence. The protein (TIP30/HTATIP2) lacks canonical kinase catalytic motifs (HRD catalytic loop, DFG activation loop, VAIK lysine). The P-loop/Walker A motif (GASGETGKV) is present but is shared by GTPases, ABC transporters, and many non-kinase nucleotide-binding proteins and does not specifically indicate protein kinase activity. The protein's actual experimentally supported function (translation repression via eEF1A) is unrelated to kinase activity. No transferable family-level or sequence-feature inference from other proteins meaningfully supports assigning kinase activity to this 242-aa protein.",
    "reason": "The sequence contains a Walker A/P-loop motif (GASGETGKV), which indicates nucleotide binding but is not specific to kinases — it is found in GTPases, ABC transporters, helicases, and many other families. Critically, the sequence lacks the hallmark protein-kinase catalytic motifs: the HRD catalytic aspartate loop, the DFG activation-loop motif, and the bilobal kinase fold architecture. The protein is only 242 aa, far smaller than typical protein kinases. A knowledgeable model using transferable kinase-family knowledge would not assign kinase activity based on these features. Options C and D are in an is_a relationship (GO:0004674 is_a GO:0004672), so even if kinase activity were assumed, distinguishing the two requires knowing the substrate specificity (Ser/Thr vs Tyr), which is absent from the sequence. The expected answer D rests entirely on a low-confidence ISO:RGD transferred annotation that contradicts the protein's actual described function. Without that specific database record, biological reasoning from the sequence and general kinase-family knowledge does not produce answer D."
  },
  "case_id": "GO_molecular_function_0091",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "C5",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry B0BNF8 (HTATIP2/TIP30, rat) carries GO:0004674 (protein serine/threonine kinase activity) as a database annotation. However, this annotation carries evidence code ISO:RGD (Inferred from Sequence Orthology from RGD), meaning it is a transferred annotation, not experimentally verified. The entry's own FUNCTION comment describes translation repression via eEF1A interaction, nuclear import inhibition, redox sensing, and NADPH binding — none of which is kinase activity. The annotation is therefore technically present but of low confidence and contradicted by the protein's described function. The expected answer is supported in the narrow sense that the GO term is recorded, but the underlying evidence is weak and the functional description does not corroborate it."
  },
  "important_caveats": [
    "The GO:0004674 annotation carries evidence code ISO:RGD (transferred by orthology), not experimental evidence. The protein's own FUNCTION comment describes translation repression, not kinase activity.",
    "The P-loop motif (GASGETGKV) in the sequence is a Walker A nucleotide-binding motif found in many unrelated protein families and is not diagnostic of kinase activity.",
    "The protein (TIP30/HTATIP2) is a well-studied translation regulator and redox sensor; its kinase annotation in databases is of uncertain reliability.",
    "The reviewer-only evidence reveals the protein identity (HTATIP2, rat) and the ISO:RGD annotation, neither of which was available to the evaluated model.",
    "Options C and D are in an is_a hierarchy, creating inherent ambiguity when the protein's kinase status is itself questionable."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C",
      "D"
    ],
    "reason": "GO:0004674 (option D) is_a GO:0004672 (option C). If the protein were truly a kinase, both terms would be valid annotations, with D being more specific. The question asks for the 'primary molecular function' but does not specify whether the most specific or the broader term is preferred. Without knowing substrate specificity from the sequence, a model could defensibly select either C or D. Additionally, since the protein's actual function is not kinase activity, neither C nor D is biologically accurate, but within the answer set they remain the closest options."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0091",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry B0BNF8 (HTATIP2/TIP30, rat) carries GO:0004674 (protein serine/threonine kinase activity) as a database annotation. However, this annotation carries evidence code ISO:RGD (Inferred from Sequence Orthology from RGD), meaning it is a transferred annotation, not experimentally verified. The entry's own FUNCTION comment describes translation repression via eEF1A interaction, nuclear import inhibition, redox sensing, and NADPH binding — none of which is kinase activity. The annotation is therefore technically present but of low confidence and contradicted by the protein's described function. The expected answer is supported in the narrow sense that the GO term is recorded, but the underlying evidence is weak and the functional description does not corroborate it.",
    "evidence_ids": ["C6", "C5", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "",
    "missing_item_specific_fact": "The specific ISO:RGD database annotation assigning GO:0004674 to this exact protein sequence. The protein (TIP30/HTATIP2) lacks canonical kinase catalytic motifs (HRD catalytic loop, DFG activation loop, VAIK lysine). The P-loop/Walker A motif (GASGETGKV) is present but is shared by GTPases, ABC transporters, and many non-kinase nucleotide-binding proteins and does not specifically indicate protein kinase activity. The protein's actual experimentally supported function (translation repression via eEF1A) is unrelated to kinase activity. No transferable family-level or sequence-feature inference from other proteins meaningfully supports assigning kinase activity to this 242-aa protein.",
    "reason": "The sequence contains a Walker A/P-loop motif (GASGETGKV), which indicates nucleotide binding but is not specific to kinases — it is found in GTPases, ABC transporters, helicases, and many other families. Critically, the sequence lacks the hallmark protein-kinase catalytic motifs: the HRD catalytic aspartate loop, the DFG activation-loop motif, and the bilobal kinase fold architecture. The protein is only 242 aa, far smaller than typical protein kinases. A knowledgeable model using transferable kinase-family knowledge would not assign kinase activity based on these features. Options C and D are in an is_a relationship (GO:0004674 is_a GO:0004672), so even if kinase activity were assumed, distinguishing the two requires knowing the substrate specificity (Ser/Thr vs Tyr), which is absent from the sequence. The expected answer D rests entirely on a low-confidence ISO:RGD transferred annotation that contradicts the protein's actual described function. Without that specific database record, biological reasoning from the sequence and general kinase-family knowledge does not produce answer D."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["C", "D"],
    "reason": "GO:0004674 (option D) is_a GO:0004672 (option C). If the protein were truly a kinase, both terms would be valid annotations, with D being more specific. The question asks for the 'primary molecular function' but does not specify whether the most specific or the broader term is preferred. Without knowing substrate specificity from the sequence, a model could defensibly select either C or D. Additionally, since the protein's actual function is not kinase activity, neither C nor D is biologically accurate, but within the answer set they remain the closest options."
  },
  "important_caveats": [
    "The GO:0004674 annotation carries evidence code ISO:RGD (transferred by orthology), not experimental evidence. The protein's own FUNCTION comment describes translation repression, not kinase activity.",
    "The P-loop motif (GASGETGKV) in the sequence is a Walker A nucleotide-binding motif found in many unrelated protein families and is not diagnostic of kinase activity.",
    "The protein (TIP30/HTATIP2) is a well-studied translation regulator and redox sensor; its kinase annotation in databases is of uncertain reliability.",
    "The reviewer-only evidence reveals the protein identity (HTATIP2, rat) and the ISO:RGD annotation, neither of which was available to the evaluated model.",
    "Options C and D are in an is_a hierarchy, creating inherent ambiguity when the protein's kinase status is itself questionable."
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
  "benchmark_sequence_length": 242,
  "benchmark_sequence_sha256": "84a71691c15d738414b9418bb4ec9b787bd7004f741e211117cb2d48da890b5f",
  "current_entry_audit": {
    "entryVersion": 119,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2008-02-26",
    "sequenceVersion": 1
  },
  "current_record_sha256": "5bc2319a85294d9bd0de3c58ce0c0ccfe250318e8fba8d882b03e077196791bb",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 242,
  "current_source_sequence_sha256": "84a71691c15d738414b9418bb4ec9b787bd7004f741e211117cb2d48da890b5f",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 117,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "B0BNF8",
  "selected_historical_entry_version": 117,
  "selected_historical_record_sha256": "c91b6ccd39bbf56d358216a7ae481826bd770d8f3f708b47271a14d3c7924ec0",
  "selected_historical_source_sequence_length": 242,
  "selected_historical_source_sequence_sha256": "84a71691c15d738414b9418bb4ec9b787bd7004f741e211117cb2d48da890b5f",
  "selected_historical_version": {
    "accession": "B0BNF8",
    "database": "Swiss-Prot",
    "entryVersion": 117,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "HTAI2_RAT",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B0BNF8.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"B0BNF8\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:27:12.867856+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5bc2319a85294d9bd0de3c58ce0c0ccfe250318e8fba8d882b03e077196791bb",
  "url": "https://rest.uniprot.org/uniprotkb/B0BNF8.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B0BNF8.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":119,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2008-02-26\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:27:12.867856+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5bc2319a85294d9bd0de3c58ce0c0ccfe250318e8fba8d882b03e077196791bb",
  "url": "https://rest.uniprot.org/uniprotkb/B0BNF8.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B0BNF8.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Rat\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000002494\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Chordata\",\"Craniata\",\"Vertebrata\",\"Euteleostomi\",\"Mammalia\",\"Eutheria\",\"Euarchontoglires\",\"Glires\",\"Rodentia\",\"Myomorpha\",\"Muroidea\",\"Muridae\",\"Murinae\",\"Rattus\"],\"scientificName\":\"Rattus norvegicus\",\"taxonId\":10116}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:27:12.867856+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5bc2319a85294d9bd0de3c58ce0c0ccfe250318e8fba8d882b03e077196791bb",
  "url": "https://rest.uniprot.org/uniprotkb/B0BNF8.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B0BNF8.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Protein HTATIP2\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:27:12.867856+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5bc2319a85294d9bd0de3c58ce0c0ccfe250318e8fba8d882b03e077196791bb",
  "url": "https://rest.uniprot.org/uniprotkb/B0BNF8.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B0BNF8.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9BUP3\",\"source\":\"UniProtKB\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"31468715\",\"source\":\"PubMed\"}],\"value\":\"Represses translation by preventing reactivation of elongation factor eEF1A (PubMed:31468715). May also inhibit nuclear import by competing with nuclear import substrates for binding to a subset of nuclear transport receptors (By similarity). Has additionally been proposed to act as a redox sensor involved in cellular oxidative stress surveillance (By similarity). May bind NADPH (By similarity)\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-02T04:27:12.867856+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5bc2319a85294d9bd0de3c58ce0c0ccfe250318e8fba8d882b03e077196791bb",
  "url": "https://rest.uniprot.org/uniprotkb/B0BNF8.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B0BNF8.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0004674\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:protein serine/threonine kinase activity\"},{\"key\":\"GoEvidenceType\",\"value\":\"ISO:RGD\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/23",
  "retrieved_utc": "2026-11-02T04:27:12.867856+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5bc2319a85294d9bd0de3c58ce0c0ccfe250318e8fba8d882b03e077196791bb",
  "url": "https://rest.uniprot.org/uniprotkb/B0BNF8.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B0BNF8.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Grund A.\",\"Szaroszyk M.\",\"Korf-Klingebiel M.\",\"Malek Mohammadi M.\",\"Trogisch F.A.\",\"Schrameck U.\",\"Gigina A.\",\"Tiedje C.\",\"Gaestel M.\",\"Kraft T.\",\"Hegermann J.\",\"Batkai S.\",\"Thum T.\",\"Perrot A.\",\"Remedios C.D.\",\"Riechert E.\",\"Voelkers M.\",\"Doroudgar S.\",\"Jungmann A.\",\"Bauer R.\",\"Yin X.\",\"Mayr M.\",\"Wollert K.C.\",\"Pich A.\",\"Xiao H.\",\"Katus H.A.\",\"Bauersachs J.\",\"Mueller O.J.\",\"Heineke J.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"31468715\"},{\"database\":\"DOI\",\"id\":\"10.15252/emmm.201810018\"}],\"citationType\":\"journal article\",\"firstPage\":\"e10018\",\"id\":\"31468715\",\"journal\":\"EMBO Mol. Med.\",\"lastPage\":\"e10018\",\"publicationDate\":\"2019\",\"title\":\"TIP30 counteracts cardiac hypertrophy and failure by inhibiting translational elongation.\",\"volume\":\"11\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":4,\"referencePositions\":[\"FUNCTION\",\"INTERACTION WITH EEF1A1\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-02T04:27:12.867856+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5bc2319a85294d9bd0de3c58ce0c0ccfe250318e8fba8d882b03e077196791bb",
  "url": "https://rest.uniprot.org/uniprotkb/B0BNF8.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B0BNF8?format=txt&versions=117)

```json
{
  "entry_version": 117,
  "evidence_id": "H1",
  "excerpt": "ID   HTAI2_RAT               Reviewed;         242 AA.\nAC   B0BNF8; A0A8I6AEZ6; G3V8Y4;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   26-FEB-2008, sequence version 1.\nDT   28-JAN-2026, entry version 117.\nDE   RecName: Full=Protein HTATIP2 {ECO:0000305};\nGN   Name=Htatip2 {ECO:0000312|RGD:1309941};\nOS   Rattus norvegicus (Rat).\nOC   Eukaryota; Metazoa; Chordata; Craniata; Vertebrata; Euteleostomi; Mammalia;\nOC   Eutheria; Euarchontoglires; Glires; Rodentia; Myomorpha; Muroidea; Muridae;\nOC   Murinae; Rattus.\nOX   NCBI_TaxID=10116 {ECO:0000312|Proteomes:UP000002494};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:16.468432+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-12",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c91b6ccd39bbf56d358216a7ae481826bd770d8f3f708b47271a14d3c7924ec0",
  "url": "https://rest.uniprot.org/unisave/B0BNF8?format=txt&versions=117"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B0BNF8?format=txt&versions=117)

```json
{
  "entry_version": 117,
  "evidence_id": "H2",
  "excerpt": "RN   [4] {ECO:0000305}\nRP   FUNCTION, AND INTERACTION WITH EEF1A1.\nRX   PubMed=31468715; DOI=10.15252/emmm.201810018;\nRA   Grund A., Szaroszyk M., Korf-Klingebiel M., Malek Mohammadi M.,\nRA   Trogisch F.A., Schrameck U., Gigina A., Tiedje C., Gaestel M., Kraft T.,\nRA   Hegermann J., Batkai S., Thum T., Perrot A., Remedios C.D., Riechert E.,\nRA   Voelkers M., Doroudgar S., Jungmann A., Bauer R., Yin X., Mayr M.,\nRA   Wollert K.C., Pich A., Xiao H., Katus H.A., Bauersachs J., Mueller O.J.,\nRA   Heineke J.;\nRT   \"TIP30 counteracts cardiac hypertrophy and failure by inhibiting\nRT   translational elongation.\";\nRL   EMBO Mol. Med. 11:e10018-e10018(2019).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:16.468432+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 77-88",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c91b6ccd39bbf56d358216a7ae481826bd770d8f3f708b47271a14d3c7924ec0",
  "url": "https://rest.uniprot.org/unisave/B0BNF8?format=txt&versions=117"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B0BNF8?format=txt&versions=117)

```json
{
  "entry_version": 117,
  "evidence_id": "H3",
  "excerpt": "CC   -!- FUNCTION: Represses translation by preventing reactivation of\nCC       elongation factor eEF1A (PubMed:31468715). May also inhibit nuclear\nCC       import by competing with nuclear import substrates for binding to a\nCC       subset of nuclear transport receptors (By similarity). Has additionally\nCC       been proposed to act as a redox sensor involved in cellular oxidative\nCC       stress surveillance (By similarity). May bind NADPH (By similarity).\nCC       {ECO:0000250|UniProtKB:Q9BUP3, ECO:0000269|PubMed:31468715}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:16.468432+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 89-95",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c91b6ccd39bbf56d358216a7ae481826bd770d8f3f708b47271a14d3c7924ec0",
  "url": "https://rest.uniprot.org/unisave/B0BNF8?format=txt&versions=117"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B0BNF8?format=txt&versions=117)

```json
{
  "entry_version": 117,
  "evidence_id": "H4",
  "excerpt": "DR   GO; GO:0004674; F:protein serine/threonine kinase activity; ISO:RGD.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:16.468432+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 131-131",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c91b6ccd39bbf56d358216a7ae481826bd770d8f3f708b47271a14d3c7924ec0",
  "url": "https://rest.uniprot.org/unisave/B0BNF8?format=txt&versions=117"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0004169\nname: dolichyl-phosphate-mannose-protein mannosyltransferase activity\nnamespace: molecular_function\ndef: \"Catalysis of the reaction: dolichyl phosphate D-mannose + protein = dolichyl phosphate + O-D-mannosylprotein.\" [EC:2.4.1.109, GOC:pr]\ncomment: Note that this activity has never been observed in green plants. However, N- and C-mannosylation may occur in these species; see figure 1 in PMID:21558543.\nsynonym: \"dolichol phosphomannose-protein mannosyltransferase activity\" RELATED [EC:2.4.1.109]\nsynonym: \"dolichyl-phosphate-D-mannose:protein O-D-mannosyltransferase activity\" RELATED [EC:2.4.1.109]\nsynonym: \"dolichyl-phosphate-mannose-protein O-mannosyltransferase activity\" EXACT []\nsynonym: \"O-glycoside mannosyltransferase\" BROAD []\nsynonym: \"protein O-D-mannosyltransferase activity\" RELATED [EC:2.4.1.109]\nsynonym: \"protein O-mannosyltransferase activity\" EXACT []\nxref: EC:2.4.1.109\nxref: MetaCyc:2.4.1.109-RXN\nxref: Reactome:R-HSA-5615556 \"Defective POMT2 does not transfer Man from Dol-P-Man to DAG1\"\nxref: Reactome:R-HSA-5615604 \"Defective POMT1 does not transfer Man from Dol-P-Man to DAG1\"\nxref: Reactome:R-HSA-5615637 \"POMT1:POMT2 transfers Man from Dol-P-Man to DAG1(30-653)\"\nxref: Reactome:R-HSA-9816277 \"CDH1 is O-manosylated\"\nis_a: GO:0000030 ! mannosyltransferase activity\nis_a: GO:0140096 ! catalytic activity, acting on a protein\nproperty_value: skos:exactMatch EC:2.4.1.109\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0004169",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 36869-36890",
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
  "excerpt": "[Term]\nid: GO:0004672\nname: protein kinase activity\nnamespace: molecular_function\nalt_id: GO:0050222\ndef: \"Catalysis of the phosphorylation of an amino acid residue in a protein, usually according to the reaction: a protein + ATP = a phosphoprotein + ADP.\" [PMID:25399640]\ncomment: Note that triphosphate is used as a phosphate donor by at least one kinase.\nsubset: goslim_candida\nsynonym: \"protamine kinase activity\" NARROW []\nxref: Reactome:R-HSA-156832 \"INF-gamma induced phosphorylation of L13a\"\nxref: Reactome:R-HSA-5693148 \"BCKDK phosphorylates BCKDH\"\nxref: Reactome:R-HSA-937034 \"IRAK1 phosphorylates Pellino\"\nxref: Reactome:R-HSA-9604606 \"Unknown kinase phosphorylates NICD4\"\nxref: Reactome:R-HSA-9673284 \"GTP-bound RAC1 contributes to MAPK8 activation\"\nxref: Reactome:R-HSA-9732753 \"JAK1-activated RAF1 phosphorylates MAPKs\"\nxref: Reactome:R-HSA-975139 \"IRAK1 phosphorylates Pellino upon TLR7/8 or 9 activation\"\nxref: Reactome:R-HSA-9833820 \"PKR dimer autophosphorylates\"\nxref: Reactome:R-HSA-9835885 \"p-PKR dimer phosphorylates eIF2-alpha\"\nxref: Reactome:R-HSA-9836159 \"p-PKR dimer phosphorylates DHX9\"\nxref: Reactome:R-HSA-9836184 \"p-PKR dimer phosphorylates CDK1\"\nxref: Reactome:R-HSA-9836322 \"p-PKR dimer phosphorylates MKK6\"\nxref: Reactome:R-HSA-9836362 \"p-PKR dimer phosphorylates TP53 tetramer\"\nxref: Reactome:R-HSA-9836383 \"p-PKR dimer phosphorylates ILF3:ILF2\"\nxref: Reactome:R-HSA-9836404 \"p-PKR dimer phosphorylates MAPT\"\nxref: Reactome:R-HSA-9836435 \"p-PKR dimer phosphorylates SNCA\"\nxref: Reactome:R-HSA-9836449 \"p-PKR dimer phosphorylates HIV tat\"\nxref: Reactome:R-HSA-9836515 \"p-PKR dimer phosphorylates PTPN2\"\nxref: Reactome:R-HSA-9836617 \"p-PKR dimer phosphorylates SPHK1\"\nxref: Reactome:R-HSA-9836664 \"p-PKR dimer phosphorylates PPP2R5A\"\nis_a: GO:0016301 ! kinase activity\nis_a: GO:0016773 ! phosphotransferase activity, alcohol group as acceptor\nis_a: GO:0140096 ! catalytic activity, acting on a protein\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0004672",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 46659-46691",
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
  "excerpt": "[Term]\nid: GO:0004674\nname: protein serine/threonine kinase activity\nnamespace: molecular_function\nalt_id: GO:0004695\nalt_id: GO:0004696\nalt_id: GO:0004700\nalt_id: GO:0106311\ndef: \"Catalysis of the reactions: ATP + protein serine = ADP + protein serine phosphate, and ATP + protein threonine = ADP + protein threonine phosphate.\" [EC:2.7.11.-, GOC:bf, PMID:2956925]\nsynonym: \"protein serine kinase activity\" NARROW [EC:2.7.11.1]\nsynonym: \"protein serine-threonine kinase activity\" RELATED [EC:2.7.11.1]\nsynonym: \"protein threonine kinase activity\" NARROW []\nsynonym: \"protein-serine kinase activity\" NARROW [EC:2.7.11.1]\nsynonym: \"serine kinase activity\" NARROW [EC:2.7.11.1]\nsynonym: \"serine protein kinase activity\" NARROW [EC:2.7.11.1]\nsynonym: \"serine(threonine) protein kinase activity\" RELATED [EC:2.7.11.1]\nsynonym: \"serine-specific protein kinase activity\" NARROW [EC:2.7.11.1]\nsynonym: \"serine/threonine protein kinase activity\" RELATED [EC:2.7.11.1]\nsynonym: \"threonine-specific protein kinase activity\" NARROW [EC:2.7.11.1]\nxref: EC:2.7.11.-\nxref: EC:2.7.11.1\nxref: EC:2.7.11.28\nxref: EC:2.7.11.29\nxref: EC:2.7.11.3\nxref: EC:2.7.11.9\nxref: MetaCyc:PROTEIN-KINASE-RXN\nxref: Reactome:R-HSA-109702 \"PDPK1 phosphorylates AKT2\"\nxref: Reactome:R-HSA-109822 \"MAPK3,(MAPK1) phosphorylates GRB2-1:SOS1:p-Y427-SHC1\"\nxref: Reactome:R-HSA-109823 \"MAPK3,(MAPK1) phosphorylates GRB2-1:SOS1:p-Y-IRS1,p-Y-IRS2\"\nxref: Reactome:R-HSA-109860 \"MAP2K1 phosphorylates MAPK3\"\nxref: Reactome:R-HSA-109862 \"MAP2K2 phosphorylates MAPK1\"\nxref: Reactome:R-HSA-111919 \"PKA phosphorylates CREB1\"\nxref: Reactome:R-HSA-111970 \"PKC phosphorylates GRK2\"\nxref: Reactome:R-HSA-112342 \"Inactivation of MAP2K1 by CDK1\"\nxref: Reactome:R-HSA-112381 \"Hyperphosphorylation (Ser2) of RNA Pol II CTD by P-TEFb complex\"\nxref: Reactome:R-HSA-1168635 \"PRKCB (PKC-beta) phosphorylates CARMA1\"\nxref: Reactome:R-HSA-1168638 \"Activated IKK phosphorylates I-kappaB\"\nxref: Reactome:R-HSA-1168641 \"TAK1 associated with the CBM complex phosphorylates IKKbeta\"\nxref: Reactome:R-HSA-1181149 \"ACVR2A,B (ActRIIA,B) phosphorylates ACVR1B (ActRIB, ALK4) in response to Activin\"\nxref: Reactome:R-HSA-1181156 \"Type II Activin Receptor (ActRII/ACVR2) phosphorylates Type I Activin Receptor (ActRIB/ACVR1B) in response to NODAL\"\nxref: Reactome:R-HSA-1181355 \"Phosphorylation of R-SMAD2/3 by NODAL receptor\"\nxref: Reactome:R-HSA-1225894 \"Type II Activin Receptor (ActRIIB/ACVR2B) phosphorylates Type I Activin Receptor (ActRIC/ACVR1C) in response to NODAL\"\nxref: Reactome:R-HSA-1358791 \"Phosphorylation of USP8 by P-AKT\"\nxref: Reactome:R-HSA-1362270 \"Phosphorylation of LIN52 component of MuvB by DYRK1A\"\nxref: Reactome:R-HSA-139908 \"Phosphorylation of DLC2 by MAPK8\"\nxref: Reactome:R-HSA-139918 \"Phosphorylation of BIM by JNK\"\nxref: Reactome:R-HSA-1445144 \"p-AKT1,p-AKT2 phosphorylates AS160 (TBC1D4)\"\nxref: Reactome:R-HSA-1449597 \"p-AKT2 phosphorylates Myosin 5A\"\nxref: Reactome:R-HSA-1454699 \"AMPK-alpha2 phosphorylates TBC1D1\"\nxref: Reactome:R-HSA-1458463 \"p-AKT2 phosphorylates RGC2\"\nxref: Reactome:R-HSA-1549526 \"Phosphorylation of SMAD2,3 by Activin:Activin Receptor\"\nxref: Reactome:R-HSA-156673 \"Regulation of KIF23 (MKLP1) by phosphorylation\"\nxref: Reactome:R-HSA-156678 \"Activation of Cdc25C\"\nxref: Reactome:R-HSA-156682 \"PLK1 phosphorylates NUDC\"\nxref: Reactome:R-HSA-156699 \"Inactivation of Wee1 kinase\"\nxref: Reactome:R-HSA-156723 \"Regulation of KIF20A (MKL2) by phosphorylation\"\nxref: Reactome:R-HSA-1592233 \"p38 MAPK phosphorylates PPARGC1A\"\nxref: Reactome:R-HSA-162363 \"p-T309,S474-AKT2:PIP3 phosphorylates PDE3B\"\nxref: Reactome:R-HSA-162657 \"Inactivation of Myt1 kinase\"\nxref: Reactome:R-HSA-163010 \"Down Regulation of Emi1 through Phosphorylation of Emi1\"\nxref: Reactome:R-HSA-1632857 \"ULK1 phosphorylates AMBRA1:BECN1 complex\"\nxref: Reactome:R-HSA-163416 \"hormone-sensitive lipase (HSL) + 2 ATP -> phosphorylated HSL + 2 ADP\"\nxref: Reactome:R-HSA-163418 \"perilipin + 2 ATP -> phosphorylated perilipin + 2 ADP\"\nxref: Reactome:R-HSA-1638803 \"Phosphorylation of cohesin by PLK1 at centromeres\"\nxref: Reactome:R-HSA-164151 \"LKB1 phosphorylates the alpha subunit of AMPK heterotrimer\"\nxref: Reactome:R-HSA-165162 \"Phosphorylation of TSC2 by PKB\"\nxref: Reactome:R-HSA-165182 \"Phosphorylation of complexed TSC2 by PKB\"\nxref: Reactome:R-HSA-165692 \"Phosphorylation of 4E-BP1 by activated mTORC1\"\nxref: Reactome:R-HSA-165718 \"mTORC1 phosphorylation of RPS6KB1 (S6K)\"\nxref: Reactome:R-HSA-165726 \"Phosphorylation of Ribosomal protein S6 by activated S6K1\"\nxref: Reactome:R-HSA-165758 \"Phosphorylation and inactivation of eEF2K by activated S6K1\"\nxref: Reactome:R-HSA-165766 \"Phosphorylation and activation of eIF4G by activated S6K1\"\nxref: Reactome:R-HSA-165777 \"Phosphorylation and activation of eIF4B by activated S6K1\"\nxref: Reactome:R-HSA-166119 \"First phosphorylation of IRAK1 by IRAK4 bound to activated TLR:MyD88:Mal\"\nxref: Reactome:R-HSA-166245 \"Phosphorylation of IRF-3/IRF7 and their release from the activated TLR complex\"\nxref: Reactome:R-HSA-166284 \"Second phosphorylation of IRAK1 by IRAK4 bound to activated TLR:MyD88:TIRAP\"\nxref: Reactome:R-HSA-166286 \"Multiple IRAK1 autophosphorylation steps\"\nxref: Reactome:R-HSA-167084 \"Hyperphosphorylation (Ser2) of RNA Pol II CTD by P-TEFb complex\"\nxref: Reactome:R-HSA-167098 \"Phosphorylation (Ser5) of RNA pol II CTD\"\nxref: Reactome:R-HSA-168053 \"Phosphorylated MAPKs phosphorylate ATF-2\"\nxref: Reactome:R-HSA-168140 \"Active IKK Complex phosphorylates NF-kappa-B inhibitor\"\nxref: Reactome:R-HSA-168184 \"Activated TAK1 mediates phosphorylation of the IKK Complex\"\nxref: Reactome:R-HSA-170055 \"Myt-1 mediated phosphorylation of Cyclin B:Cdc2 complexes\"\nxref: Reactome:R-HSA-170076 \"CAK phosphorylates CDK1 bound to CCNB1\"\nxref: Reactome:R-HSA-170087 \"CAK phosphorylates CDK1 bound to CCNA\"\nxref: Reactome:R-HSA-170116 \"PKMYT1 phosphorylates CCNA:CDK1\"\nxref: Reactome:R-HSA-170126 \"Phosphorylation of Cyclin B1 in the CRS domain\"\nxref: Reactome:R-HSA-170977 \"FRS2 is phosphorylated by active TrkA receptor\"\nxref: Reactome:R-HSA-174119 \"Free APC/C phosphorylated by Plk1\"\nxref: Reactome:R-HSA-174174 \"Phosphorylation of the Emi1 DSGxxS degron by Plk1\"\nxref: Reactome:R-HSA-176116 \"Recruitment and activation of Chk1\"\nxref: Reactome:R-HSA-176298 \"Activation of claspin\"\nxref: Reactome:R-HSA-187688 \"p38 MAPK phosphorylates MAPKAPK2, MAPKAPK3\"\nxref: Reactome:R-HSA-187949 \"CAK-mediated phosphorylation of Cyclin A:Cdk2\"\nxref: Reactome:R-HSA-188350 \"CAK-mediated phosphorylation of Cyclin E:Cdk2\"\nxref: Reactome:R-HSA-193647 \"IRAK is activated\"\nxref: Reactome:R-HSA-193703 \"IKKbeta is activated\"\nxref: Reactome:R-HSA-193705 \"IKKbeta phosphorylates IkB causing NF-kB to dissociate\"\nxref: Reactome:R-HSA-195275 \"Phosphorylation of APC component of the destruction complex\"\nxref: Reactome:R-HSA-195283 \"Phosphorylation of phospho- (Ser45, Thr41) beta-catenin  at Ser37 by GSK-3\"\nxref: Reactome:R-HSA-195287 \"Phosphorylation of phospho-(Ser45 ) at Thr 41 by GSK-3\"\nxref: Reactome:R-HSA-195300 \"Phosphorylation of phospho-(Ser45,Thr41,Ser37) at Ser33 by GSK-3\"\nxref: Reactome:R-HSA-195318 \"Phosphorylation of beta-catenin at Ser45 by CK1 alpha\"\nxref: Reactome:R-HSA-198270 \"PDPK1 phosphorylates AKT at T308\"\nxref: Reactome:R-HSA-198347 \"AKT phosphorylates BAD\"\nxref: Reactome:R-HSA-198371 \"AKT phosphorylates GSK3\"\nxref: Reactome:R-HSA-198599 \"AKT phosphorylates MDM2\"\nxref: Reactome:R-HSA-198609 \"AKT phosphorylates TSC2, inhibiting it\"\nxref: Reactome:R-HSA-198611 \"AKT phosphorylates IKKalpha\"\nxref: Reactome:R-HSA-198613 \"AKT phosphorylates p21Cip1 and p27Kip1\"\nxref: Reactome:R-HSA-198621 \"AKT phosphorylates caspase-9\"\nxref: Reactome:R-HSA-198640 \"TORC2 (mTOR) phosphorylates AKT at S473\"\nxref: Reactome:R-HSA-198669 \"p38MAPK phosphorylates MSK1\"\nxref: Reactome:R-HSA-198731 \"ERK1/2 activates ELK1\"\nxref: Reactome:R-HSA-198746 \"ERK1/2/5 activate RSK1/2/3\"\nxref: Reactome:R-HSA-198756 \"ERK1/2 phosphorylates MSK1\"\nxref: Reactome:R-HSA-199298 \"AKT phosphorylates CREB1\"\nxref: Reactome:R-HSA-199299 \"AKT phosphorylates FOXO transcription factors\"\nxref: Reactome:R-HSA-199839 \"AKT can phosphorylate RSK\"\nxref: Reactome:R-HSA-199863 \"AKT can phosphorylate NR4A1 (NUR77)\"\nxref: Reactome:R-HSA-199895 \"RSK1/2/3 phosphorylates CREB at Serine 119\"\nxref: Reactome:R-HSA-199910 \"MSK1 activates ATF1\"\nxref: Reactome:R-HSA-199917 \"MAPKAPK2 phosphorylates CREB at Serine 133\"\nxref: Reactome:R-HSA-199929 \"ERK5 activates the transcription factor MEF2\"\nxref: Reactome:R-HSA-199935 \"MSK1 activates CREB\"\nxref: Reactome:R-HSA-200143 \"AKT phosphorylates AKT1S1 (PRAS40)\"\nxref: Reactome:R-HSA-200421 \"Activation of cytosolic AMPK by phosphorylation\"\nxref: Reactome:R-HSA-201677 \"Phosphorylation of LRP5/6 cytoplasmic domain by membrane-associated GSK3beta\"\nxref: Reactome:R-HSA-201691 \"Phosphorylation of LRP5/6 cytoplasmic domain by CSNKI\"\nxref: Reactome:R-HSA-201717 \"CSNK2-mediated phosphorylation of DVL\"\nxref: Reactome:R-HSA-202111 \"AKT1 phosphorylates eNOS\"\nxref: Reactome:R-HSA-202222 \"Phosphorylation of PKC theta\"\nxref: Reactome:R-HSA-202437 \"Phosphorylation of CARMA1\"\nxref: Reactome:R-HSA-202459 \"Phosphorylation of Bcl10\"\nxref: Reactome:R-HSA-202500 \"Activation of IKK complex\"\nxref: Reactome:R-HSA-202510 \"Activation of TAK1-TAB2 complex\"\nxref: Reactome:R-HSA-202541 \"p-S177,S181-IKKB:IKKA:pUb-NEMO phosphorylates IkB-alpha:NF-kB\"\nxref: Reactome:R-HSA-2028284 \"Phosphorylation of STK4 (MST1) and SAV1 by STK4\"\nxref: Reactome:R-HSA-2028555 \"Phosphorylation of LATS1 and 2 by p-STK4 (p-MST1)\"\nxref: Reactome:R-HSA-2028583 \"Phosphorylation of YAP by LATS2\"\nxref: Reactome:R-HSA-2028589 \"Phosphorylation of LATS1 and 2 by p-STK3 (p-MST2)\"\nxref: Reactome:R-HSA-2028591 \"Phosphorylation of STK3 (MST2) and SAV1 by STK3\"\nxref: Reactome:R-HSA-2028598 \"Phosphorylation of YAP by LATS1\"\nxref: Reactome:R-HSA-2028629 \"Phosphorylation of MOB1A and B by p-STK4 (p-MST1)\"\nxref: Reactome:R-HSA-2028635 \"Phosphorylation of MOB1A and B by p-STK3 (p-MST2)\"\nxref: Reactome:R-HSA-2028661 \"Phosphorylation of WWTR1 (TAZ) by LATS2\"\nxref: Reactome:R-HSA-2028670 \"Phosphorylation of MOB1A and B by p-STK4(MST1)/N\"\nxref: Reactome:R-HSA-2028673 \"Phosphorylation of LATS1 and 2 by p-STK3 (MST2)/N\"\nxref: Reactome:R-HSA-2028675 \"Phosphorylation of MOB1A and B by p-STK3(MST2)/N\"\nxref: Reactome:R-HSA-2028679 \"Phosphorylation of LATS1 and 2 by p-STK4(MST1)/N\"\nxref: Reactome:R-HSA-2029454 \"Autophosphorylation of PAK1\"\nxref: Reactome:R-HSA-2029460 \"PAK1 phosphorylates LIMK1\"\nxref: Reactome:R-HSA-2029469 \"p-ERK phosphorylates WAVEs and ABI\"\nxref: Reactome:R-HSA-2060328 \"Phosphorylation of WWTR1 (TAZ) by LATS1\"\nxref: Reactome:R-HSA-209087 \"IKBA is phosphorylated by Phospho IKKB kinase\"\nxref: Reactome:R-HSA-211164 \"AKT phosphorylates FOXO1A\"\nxref: Reactome:R-HSA-211583 \"Partial autophosphorylation of PAK-2 at  Ser-19, Ser-20, Ser-55, Ser-192, and Ser-197\"\nxref: Reactome:R-HSA-211650 \"Autophosphorylation of PAK-2p34 in the activation loop\"\nxref: Reactome:R-HSA-2168079 \"MASTL (GWL) phosphorylates ARPP19\"\nxref: Reactome:R-HSA-2176475 \"Phosphorylation of SMAD2 and SMAD3 linker regions by CDK8 or CDK9\"\nxref: Reactome:R-HSA-2214351 \"PLK1 phosphorylates GORASP1\"\nxref: Reactome:R-HSA-2243938 \"AKT1 E17K mutant is phosphorylated by TORC2 complex\"\nxref: Reactome:R-HSA-2243942 \"PDPK1 phosphorylates AKT1 E17K mutant\"\nxref: Reactome:R-HSA-2294580 \"PLK1 hyperphosphorylates Condensin II complex\"\nxref: Reactome:R-HSA-2396007 \"IRF3 is phosphorylated by TBK1\"\nxref: Reactome:R-HSA-2399941 \"AKT1 E17K mutant phosphorylates BAD\"\nxref: Reactome:R-HSA-2399966 \"AKT1 E17K mutant phosphorylates GSK3\"\nxref: Reactome:R-HSA-2399969 \"AKT1 E17K mutant phosphorylates p21Cip1 and p27Kip1\"\nxref: Reactome:R-HSA-2399977 \"AKT1 E17K mutant phosphorylates AKT1S1 (PRAS40)\"\nxref: Reactome:R-HSA-2399981 \"AKT1 E17K mutant phosphorylates MDM2\"\nxref: Reactome:R-HSA-2399982 \"AKT1 E17K mutant phosphorylates TSC2, inhibiting it\"\nxref: Reactome:R-HSA-2399985 \"AKT1 E17K mutant phosphorylates caspase-9\"\nxref: Reactome:R-HSA-2399988 \"AKT1 E17K mutant phosphorylates NR4A1 (NUR77)\"\nxref: Reactome:R-HSA-2399992 \"AKT1 E17K mutant phosphorylates forkhead box transcription factors\"\nxref: Reactome:R-HSA-2399996 \"AKT1 E17K mutant phosphorylates CREB1\"\nxref: Reactome:R-HSA-2399999 \"AKT1 E17K mutant phosphorylates RSK\"\nxref: Reactome:R-HSA-2400001 \"AKT1 E17K mutant phosphorylates CHUK (IKKalpha)\"\nxref: Reactome:R-HSA-2422927 \"MAPK3-3 or MAPK1 phosphorylate GORASP2\"\nxref: Reactome:R-HSA-2430535 \"MASTL phosphorylates ENSA\"\nxref: Reactome:R-HSA-2466068 \"Phosphorylation of cohesin by PLK1 at chromosomal arms\"\nxref: Reactome:R-HSA-2470508 \"ACVR2A,B (ActRIIA,B) phosphorylates ACVR1C (ActRIC, ALK7) in response to Activin\"\nxref: Reactome:R-HSA-2529020 \"CK2 phosphorylates condensin I subunits\"\nxref: Reactome:R-HSA-2562526 \"PLK1 phosphorylates OPTN\"\nxref: Reactome:R-HSA-2574840 \"AJUBA facilitates AURKA autophosphorylation\"\nxref: Reactome:R-HSA-2730856 \"Autophosphorylation of PAK\"\nxref: Reactome:R-HSA-2730868 \"Phosphorylation of MEK7 by MEKK1\"\nxref: Reactome:R-HSA-2730876 \"Phosphorylation of IKK-beta by TAK1\"\nxref: Reactome:R-HSA-2730896 \"Phosphorylation of MEK4 by MEKK1\"\nxref: Reactome:R-HSA-2730900 \"Activation of TAK1 complex bound to pUb-TRAF6\"\nxref: Reactome:R-HSA-2984226 \"PLK1 phosphorylates NEK9\"\nxref: Reactome:R-HSA-2984258 \"NEK9 phosphorylates NEK6/NEK7\"\nxref: Reactome:R-HSA-2990880 \"NEK6/NEK7 phosphorylates NUP98\"\nxref: Reactome:R-HSA-2993898 \"VRK1/VRK2 phosphorylate BANF1\"\nxref: Reactome:R-HSA-3000310 \"AURKA phosphorylates PLK1\"\nxref: Reactome:R-HSA-3000327 \"PLK1 phosphorylates BORA\"\nxref: Reactome:R-HSA-3132737 \"MAPKs phosphorylate ETS1 and ETS2\"\nxref: Reactome:R-HSA-3209160 \"Activated ERKs phosphorylate ERF\"\nxref: Reactome:R-HSA-3222006 \"STK11 (LKB1) phosphorylates NUAK1\"\nxref: Reactome:R-HSA-3222020 \"NUAK1 phosphorylates TP53\"\nxref: Reactome:R-HSA-3228469 \"MAP3K5 phosphorylates MKK3 and MKK6\"\nxref: Reactome:R-HSA-3229102 \"p-MAPKAPK3 phosphorylates BMI1\"\nxref: Reactome:R-HSA-3229152 \"MAP3K5 (ASK1) phosphorylates MAP2K4 (SEK1)\"\nxref: Reactome:R-HSA-3239014 \"MAPKAPK5 phosphorylates TP53\"\nxref: Reactome:R-HSA-3239019 \"Active p38 MAPK phosphorylates MAPKAPK5\"\nxref: Reactome:R-HSA-3249371 \"TBK1 phosphorylates STAT6 at Ser407\"\nxref: Reactome:R-HSA-3371435 \"Constitutive phosphorylation by GSK3\"\nxref: Reactome:R-HSA-3371531 \"Constitutive phosphorylation  by pERK1/2\"\nxref: Reactome:R-HSA-3371567 \"DBC1 is phosphorylated by ATM/ART\"\nxref: Reactome:R-HSA-349426 \"Phosphorylation of MDM4 by CHEK2\"\nxref: Reactome:R-HSA-349444 \"Phosphorylation of COP1 at Ser-387  by ATM\"\nxref: Reactome:R-HSA-349455 \"Phosphorylation of MDM4 by ATM\"\nxref: Reactome:R-HSA-374696 \"Phosphorylation of L1 by p90rsk\"\nxref: Reactome:R-HSA-3769394 \"AKT phosphorylates CBY1\"\nxref: Reactome:R-HSA-377186 \"Activated Akt1 phosphorylates AKT1S1 (PRAS40)\"\nxref: Reactome:R-HSA-3772435 \"WNT signaling stimulates CSNK1-dependent phosphorylation of DVL\"\nxref: Reactome:R-HSA-380272 \"Plk1-mediated phosphorylation of Nlp\"\nxref: Reactome:R-HSA-381091 \"IRE1 dimer autophosphorylates\"\nxref: Reactome:R-HSA-381111 \"EIF2AK3 (PERK) phosphorylates EIF2S1 (eIF2-alpha)Phosphorylation of eIF2-alpha by PERK\"\nxref: Reactome:R-HSA-3857328 \"RPS6KA1/2/3 phosphorylates CEBPB on S321\"\nxref: Reactome:R-HSA-3857329 \"MAPK3 (ERK1) and MAPK1 (ERK2) phosphorylate CEBPB\"\nxref: Reactome:R-HSA-3858480 \"WNT-dependent phosphorylation of DVL\"\nxref: Reactome:R-HSA-389756 \"AKT interacts and phosphorylates Cot\"\nxref: Reactome:R-HSA-392752 \"Phosphorylation of L1 by CK-II\"\nxref: Reactome:R-HSA-3928577 \"ROCK phosphorylates LIMK1,2\"\nxref: Reactome:R-HSA-3928608 \"LIMK phosphorylates CFL1, inactivating it\"\nxref: Reactome:R-HSA-3928616 \"Activated ROCK phosphorylates MRLCs\"\nxref: Reactome:R-HSA-3928620 \"PAK1 autophosphorylates\"\nxref: Reactome:R-HSA-3928625 \"PAKs autophosphorylate\"\nxref: Reactome:R-HSA-3928640 \"PAKs phosphorylate MLC\"\nxref: Reactome:R-HSA-399939 \"Autophosphorylation of PAK\"\nxref: Reactome:R-HSA-399944 \"Phosphorylation of CRMPs by Cdk5\"\nxref: Reactome:R-HSA-399950 \"Phosphorylation of cofilin by LIMK-1\"\nxref: Reactome:R-HSA-399951 \"Phosphorylation of CRMPs by GSK3beta\"\nxref: Reactome:R-HSA-399952 \"Phosphorylation of LIMK-1 by PAK\"\nxref: Reactome:R-HSA-399978 \"Protein kinase C, alpha type phosphorylates MARCKS\"\nxref: Reactome:R-HSA-4088134 \"PLK1 phosphorylates FOXM1\"\nxref: Reactome:R-HSA-419083 \"Myosin phosphatase inactivation by ROCK\"\nxref: Reactome:R-HSA-419087 \"LIM kinase phosphorylation by ROCK\"\nxref: Reactome:R-HSA-419197 \"Myosin regulatory light chain phosphorylation by ROCK\"\nxref: Reactome:R-HSA-419644 \"Transphosphorylation of pLIMK1\"\nxref: Reactome:R-HSA-428961 \"Phosphorylation of cPLA2 by MAPK p38 alpha\"\nxref: Reactome:R-HSA-429016 \"ALOX5 is phosphorylated by MAPKAP2\"\nxref: Reactome:R-HSA-429714 \"CSNK1G2 phosphorylates p-CERT1-2\"\nxref: Reactome:R-HSA-432110 \"Integrin alpha IIb beta3 T779 phosphorylation blocks SHC binding\"\nxref: Reactome:R-HSA-4332358 \"Dissociation of CaM and CAMK2 autophosphorylation\"\nxref: Reactome:R-HSA-4332363 \"Autophosphorylation and activation of CAMK2\"\nxref: Reactome:R-HSA-4332388 \"Activation of MAP3K7 in response to WNT\"\nxref: Reactome:R-HSA-4411383 \"NLK phosphorylates TCF/LEF\"\nxref: Reactome:R-HSA-4411402 \"Activation of NLK\"\nxref: Reactome:R-HSA-442724 \"Phosphorylation of CREB1 by ribosomal protein S6 kinases (RSKs)\"\nxref: Reactome:R-HSA-442739 \"PDPK1 phosphorylates RSKs\"\nxref: Reactome:R-HSA-442832 \"PAK phosphorylates cortactin\"\nxref: Reactome:R-HSA-445072 \"Interaction of PAK1 with Rac1-GTP\"\nxref: Reactome:R-HSA-446694 \"IRAK4 phosphorylates IRAK1\"\nxref: Reactome:R-HSA-446701 \"IRAK4-activated IRAK1 autophosphorylates\"\nxref: Reactome:R-HSA-448948 \"Phosphorylation of E proteins by p38 MAPK\"\nxref: Reactome:R-HSA-448955 \"Phosphorylation of MEF2 proteins by p38\"\nxref: Reactome:R-HSA-450222 \"Active p38 MAPK phosphorylates MAPKAPK2 or 3\"\nxref: Reactome:R-HSA-450325 \"c-FOS activation by phospho ERK1/2\"\nxref: Reactome:R-HSA-450337 \"Activated TAK1 phosphorylates MKK4/MKK7\"\nxref: Reactome:R-HSA-450346 \"activated human TAK1 phosphorylates MKK3/MKK6\"\nxref: Reactome:R-HSA-450463 \"MK2 phosphorylates ZFP36 (Tristetraproline, TTP)\"\nxref: Reactome:R-HSA-450474 \"MK2 phosphorylates BRF1\"\nxref: Reactome:R-HSA-450490 \"Protein Kinase B/Akt phosphorylates BRF1\"\nxref: Reactome:R-HSA-450499 \"Protein Kinase B (AKT) phosphorylates KSRP\"\nxref: Reactome:R-HSA-450827 \"hp-IRAK1, hp-IRAK4 4 phosphorylate Pellino-1 and 2\"\nxref: Reactome:R-HSA-451152 \"MAP kinase p38 phosphorylates KSRP\"\nxref: Reactome:R-HSA-4551570 \"VANGL2 is phosphorylated in response to WNT5A\"\nxref: Reactome:R-HSA-4608825 \"DVL2 is phosphorylated after WNT5A binding to FZD\"\nxref: Reactome:R-HSA-4793911 \"MAPKAPK2 phosphorylates HSF1\"\nxref: Reactome:R-HSA-5082387 \"Phosphorylation of HSF1 at Ser230 induces transactivation\"\nxref: Reactome:R-HSA-5082405 \"Phosphorylation of HSF1 at Ser326 induces transactivation\"\nxref: Reactome:R-HSA-5213464 \"RIPK1 is phosphorylated\"\nxref: Reactome:R-HSA-5213466 \"RIPK3 is phosphorylated\"\nxref: Reactome:R-HSA-5218814 \"PAK2 autophorylates\"\nxref: Reactome:R-HSA-5218821 \"PDK1 phosphorylates PKC\"\nxref: Reactome:R-HSA-5218826 \"Active ROCK1,ROCK2 phosphorylates p-5Y-PTK2 on S732\"\nxref: Reactome:R-HSA-5218854 \"p-Y420-FYN is phosphorylated on S21\"\nxref: Reactome:R-HSA-5218906 \"RIPK3 phosphorylates MLKL\"\nxref: Reactome:R-HSA-5218916 \"p-MAPK2/3 phosphorylates HSP27\"\nxref: Reactome:R-HSA-5228811 \"NFKBIA variant is not phosphorylated within IkBA:NF-kappaB\"\nxref: Reactome:R-HSA-5229343 \"AXIN is phosphorylated in the destruction complex\"\nxref: Reactome:R-HSA-5260201 \"p-AKT2 phosphorylates C2CD5\"\nxref: Reactome:R-HSA-5357472 \"PAK1-3 autophosphorylates\"\nxref: Reactome:R-HSA-5357477 \"PAK1-3 phosphorylates VE-cadherin\"\nxref: Reactome:R-HSA-5357831 \"CHUK, IKBKB phosphorylate CYLD at S418\"\nxref: Reactome:R-HSA-5578777 \"DMPK phosphorylates PLN\"\nxref: Reactome:R-HSA-5607722 \"Active NIK phosphorylates IKKA dimer\"\nxref: Reactome:R-HSA-5607726 \"Active NIK:p-S176,180-IKKA dimer phosphorylates p100:RELB\"\nxref: Reactome:R-HSA-5607732 \"K63polyUb-TAK1 autophosphorylates\"\nxref: Reactome:R-HSA-5607742 \"K63polyUb-p-3T,1S-TAK1 phosphorylates IKK-beta\"\nxref: Reactome:R-HSA-5610718 \"CK1 phosphorylates p-GLI2\"\nxref: Reactome:R-HSA-5610722 \"CK1 phosphorylates p-GLI3\"\nxref: Reactome:R-HSA-5610730 \"GSK3 phosphorylates p-GLI2\"\nxref: Reactome:R-HSA-5610732 \"GSK3 phosphorylates p-GLI3\"\nxref: Reactome:R-HSA-5623667 \"PDPK1 phosphorylates PKN1,2,3\"\nxref: Reactome:R-HSA-5624473 \"Protein kinase A (PKA) and RPS6KA5 (MSK1) phosphorylates p65 (RELA) subunit\"\nxref: Reactome:R-HSA-5624492 \"PAK phosphorylates p21 RAF1 on S338\"\nxref: Reactome:R-HSA-5625784 \"PKN1 phosphorylates histone 3 of nucleosomes associate with KLK2 and KLK3 promoters\"\nxref: Reactome:R-HSA-5627775 \"Autophosphorylation of PAK1,2,3\"\nxref: Reactome:R-HSA-5632670 \"CSNK1A1 phosphorylates SMO dimer\"\nxref: Reactome:R-HSA-5632672 \"ADRBK1 phosphorylates SMO dimer\"\nxref: Reactome:R-HSA-5635841 \"GLI proteins are phosphorylated\"\nxref: Reactome:R-HSA-5635842 \"ULK3 phosphorylates GLI\"\nxref: Reactome:R-HSA-5665868 \"AMPK (complex) phosphorylates ULK1 (complex)\"\nxref: Reactome:R-HSA-5666160 \"AURKB phosphorylates DIAPH2-2 at kinetochores\"\nxref: Reactome:R-HSA-5668545 \"NIK autophosphorylates on T559\"\nxref: Reactome:R-HSA-5668932 \"PAK2 phosphorylates myosin regulatory light chain (MRLC)\"\nxref: Reactome:R-HSA-5668947 \"PAK1 phosphorylates myosin phosphatase\"\nxref: Reactome:R-HSA-5668984 \"PAK1 or PAK2 phosphorylates MYLK\"\nxref: Reactome:R-HSA-5669250 \"PAK1 phosphorylates FLNA\"\nxref: Reactome:R-HSA-5671749 \"p-T774-PKN1 phosphorylates CDC25C\"\nxref: Reactome:R-HSA-5671763 \"p-T774-PKN1 phosphorylates PPP1R14A\"\nxref: Reactome:R-HSA-5671919 \"Activated CIT phosphorylates MRLCs\"\nxref: Reactome:R-HSA-5672008 \"Thr-180 of ULK1 is phosphorylated\"\nxref: Reactome:R-HSA-5672010 \"Active MTORC1 phosphorylates ULK1\"\nxref: Reactome:R-HSA-5672828 \"mTORC1 phosphorylates AKT1S1\"\nxref: Reactome:R-HSA-5672948 \"MARK3 phosphorylates KSR1\"\nxref: Reactome:R-HSA-5672973 \"MAP2Ks phosphorylate MAPKs\"\nxref: Reactome:R-HSA-5672978 \"RAF phosphorylates MAP2K dimer\"\nxref: Reactome:R-HSA-5674496 \"Activated MAPKs phosphorylate MAP2K1\"\nxref: Reactome:R-HSA-5675194 \"Activated MAPK phosphorylates RAF1\"\nxref: Reactome:R-HSA-5675198 \"Activated MAPKs phosphorylate BRAF\"\nxref: Reactome:R-HSA-5675868 \"ULK1 phosphorylates ATG13 and RB1CC1\"\nxref: Reactome:R-HSA-5679205 \"ULK1 phosphorylates Beclin-1\"\nxref: Reactome:R-HSA-5682026 \"MRN bound to shortened telomeres activates ATM\"\nxref: Reactome:R-HSA-5682101 \"PKA phosphorylates 4xPALM-C-p-2S-ABCA1 tetramer\"\nxref: Reactome:R-HSA-5682598 \"ATM phosphorylates HERC2\"\nxref: Reactome:R-HSA-5682983 \"ATM phosphorylates WHSC1\"\nxref: Reactome:R-HSA-5683425 \"ATM phosphorylates TP53BP1 at DNA DSBs\"\nxref: Reactome:R-HSA-5683792 \"p-T68-CHEK2 autophosphorylates\"\nxref: Reactome:R-HSA-5683801 \"CHEK2 phosphorylates BRCA1\"\nxref: Reactome:R-HSA-5683964 \"ATM phosphorylates EYA1-4\"\nxref: Reactome:R-HSA-5684096 \"CDK2 phosphorylates RBBP8\"\nxref: Reactome:R-HSA-5684140 \"ATM phosphorylates RBBP8\"\nxref: Reactome:R-HSA-5684887 \"Activation of CHEK1 at resected DNA DSBs\"\nxref: Reactome:R-HSA-5685156 \"ATR phosphorylates RPA2\"\nxref: Reactome:R-HSA-5685230 \"CHEK1 phosphorylates RAD51\"\nxref: Reactome:R-HSA-5685242 \"CHEK1 phosphorylates BRCA2\"\nxref: Reactome:R-HSA-5686578 \"Activated ATM phosphorylates ABL1\"\nxref: Reactome:R-HSA-5686704 \"Activated ATM phosphorylates DCLRE1C\"\nxref: Reactome:R-HSA-5687086 \"PAK1,2,3 phosphorylates MAPK6,4\"\nxref: Reactome:R-HSA-5687090 \"p-S MAPK6 phosphorylates NCOA3\"\nxref: Reactome:R-HSA-5687094 \"p-S MAPK6,4 phosphorylate MAPKAPK5\"\nxref: Reactome:R-HSA-5687101 \"p-T182 MAPKAPK5 phosphorylates FOXO3\"\nxref: Reactome:R-HSA-5687121 \"p-S MAPKAPK5 phosphorylates HSPB1\"\nxref: Reactome:R-HSA-5687183 \"PRKDC phosphorylates DCLRE1C at DNA DSBs\"\nxref: Reactome:R-HSA-5690250 \"p-T182-MAPKAPK5 phoshphorylates DNAJB1\"\nxref: Reactome:R-HSA-5692768 \"MAPKAPK5 phosphorylates KALRN\"\nxref: Reactome:R-HSA-5692775 \"SEPT7:p-S189 MAPK6:p-T182 MAPKAPK5 phosphorylates CDC42EPs\"\nxref: Reactome:R-HSA-5692779 \"p-T182 MAPKAPK5 phosphorylates FOXO1\"\nxref: Reactome:R-HSA-5693536 \"ATM phosphorylates MDC1\"\nxref: Reactome:R-HSA-5693540 \"MRN activates ATM\"\nxref: Reactome:R-HSA-5693549 \"ATM phosphorylates histone H2AFX on S139 at DNA DSBs\"\nxref: Reactome:R-HSA-5693551 \"Phosphorylation of BRCA1-A complex at multiple sites by ATM\"\nxref: Reactome:R-HSA-5693575 \"DNA-PKcs autophosphorylates\"\nxref: Reactome:R-HSA-5693598 \"ATM phosphorylates NBN\"\nxref: Reactome:R-HSA-5693609 \"ATM phosphorylates TP53 at S15\"\nxref: Reactome:R-HSA-5694441 \"CSNK1D phosphorylates SEC23\"\nxref: Reactome:R-HSA-6788392 \"ATR phosphorylates RPA2, FANCI, FANCD2 and FANCM at ICL-DNA\"\nxref: Reactome:R-HSA-6795290 \"TORC2 complex phosphorylates SGK1\"\nxref: Reactome:R-HSA-6795460 \"SGK1 phosphorylates MDM2\"\nxref: Reactome:R-HSA-6795473 \"PDPK1 phosphorylates SGK1\"\nxref: Reactome:R-HSA-6798372 \"ATM phosphorylates DYRK2\"\nxref: Reactome:R-HSA-6798374 \"DYRK2 phosphorylates TP53\"\nxref: Reactome:R-HSA-6799097 \"ATM phosphorylates ZNF420\"\nxref: Reactome:R-HSA-6799246 \"CHEK1 phosphorylates TP53\"\nxref: Reactome:R-HSA-6799332 \"ATR phosphorylates TP53\"\nxref: Reactome:R-HSA-6799409 \"HIPK2 phosphorylates TP53\"\nxref: Reactome:R-HSA-6800490 \"ATM phosphorylates PIDD1\"\nxref: Reactome:R-HSA-6801666 \"PLK2 phosphorylates CENPJ\"\nxref: Reactome:R-HSA-6801675 \"PLK2 phosphorylates NPM1\"\nxref: Reactome:R-HSA-6802911 \"High kinase activity BRAF complexes phosphorylate MAP2Ks\"\nxref: Reactome:R-HSA-6802919 \"RAS:GTP:moderate kinase activity p-RAF complexes phosphorylate MAP2Ks\"\nxref: Reactome:R-HSA-6802926 \"Mutant RAS:p-RAF complexes phosphorylate MAP2Ks\"\nxref: Reactome:R-HSA-6802933 \"p-BRAF and RAF fusion dimers phosphorylate MAP2Ks\"\nxref: Reactome:R-HSA-6802935 \"MAPKs are phosphorylated downstream of BRAF and RAF fusion dimers\"\nxref: Reactome:R-HSA-6802943 \"RAS:GTP:inactive p-RAF complexes phosphorylate MAP2Ks\"\nxref: Reactome:R-HSA-6802973 \"PLK3 phosphorylates CDC25C\"\nxref: Reactome:R-HSA-6804266 \"CHEK2 phosphorylates TTC5\"\nxref: Reactome:R-HSA-6804276 \"ATM phosphorylates TTC5\"\nxref: Reactome:R-HSA-6804955 \"ATM phosphorylates MDM2\"\nxref: Reactome:R-HSA-6805059 \"CK2:FACT phosphorylates TP53\"\nxref: Reactome:R-HSA-6805103 \"AURKA phosphorylates TP53\"\nxref: Reactome:R-HSA-6805126 \"AURKB phosphorylates TP53\"\nxref: Reactome:R-HSA-6805276 \"CDK5 phosphorylates TP53\"\nxref: Reactome:R-HSA-6805285 \"PLK3 phosphorylates TP53\"\nxref: Reactome:R-HSA-6805399 \"TAF1 phosphorylates TP53\"\nxref: Reactome:R-HSA-6805479 \"TP53RK phosphorylates TP53\"\nxref: Reactome:R-HSA-6805640 \"AKT phosphorylates KAT6A\"\nxref: Reactome:R-HSA-6805785 \"AKT phosphorylates PHF20\"\nxref: Reactome:R-HSA-6810233 \"CDK7 phosphorylates serine-5 and serine-7 of heptad repeats in C-terminal domain of RNA polymerase II at snRNA promoter\"\nxref: Reactome:R-HSA-6811454 \"MAPKs phosphorylate PP2A\"\nxref: Reactome:R-HSA-6814409 \"CK2 phosphorylates PDCL\"\nxref: Reactome:R-HSA-69604 \"Phosphorylation of CDC25A by CHEK1\"\nxref: Reactome:R-HSA-69608 \"Phosphorylation of CDC25A by CHEK2\"\nxref: Reactome:R-HSA-69685 \"CHEK2 phosphorylates TP53\"\nxref: Reactome:R-HSA-69891 \"Phosphorylation and activation of CHEK2 by ATM\"\nxref: Reactome:R-HSA-75010 \"Phosphorylation of Cdc25C at Ser 216 by Chk1\"\nxref: Reactome:R-HSA-75028 \"Phosphorylation of Wee1 kinase by Chk1\"\nxref: Reactome:R-HSA-75809 \"Phosphorylation of Cdc25C at Ser216 by CHEK2\"\nxref: Reactome:R-HSA-75820 \"Phosphorylation of Cyclin D1 at T286 by glycogen synthase kinase-3 beta\"\nxref: Reactome:R-HSA-77071 \"Phosphorylation (Ser5) of RNA pol II CTD\"\nxref: Reactome:R-HSA-8850945 \"Casein kinase II phosphorylates PTEN\"\nxref: Reactome:R-HSA-8852306 \"Mitotic phosphorylation-induced dissociation of GTSE1 from microtubule plus ends\"\nxref: Reactome:R-HSA-8852317 \"PLK1 phosphorylates GTSE1\"\nxref: Reactome:R-HSA-8853419 \"TPX2 promotes AURKA autophosphorylation\"\nxref: Reactome:R-HSA-8853444 \"AURKA phosphorylates PHLDA1\"\nxref: Reactome:R-HSA-8854908 \"PKA phosphorylates RET:GDNF:GFRA dimer\"\nxref: Reactome:R-HSA-8856813 \"AAK1 phosphorylates AP-2 mu subunit at T156\"\nxref: Reactome:R-HSA-8863007 \"p25-bound CDK5 phosphorylates CDC25B\"\nxref: Reactome:R-HSA-8863011 \"p25-bound CDK5 phosphorylates CDC25C\"\nxref: Reactome:R-HSA-8863014 \"p25-bound CDK5 phosphorylates CDC25A\"\nxref: Reactome:R-HSA-8863895 \"IKKB phosphorylates SNAP23\"\nxref: Reactome:R-HSA-8868118 \"MAPK12 phosphorylates PTPN3\"\nxref: Reactome:R-HSA-8868260 \"CDK5:p25 phosphorylates GOLGA2\"\nxref: Reactome:R-HSA-8868340 \"CDK5:p25 phosphorylates lamin B1\"\nxref: Reactome:R-HSA-8868344 \"CDK5:p25 phosphorylates lamin A\"\nxref: Reactome:R-HSA-8868567 \"CDK5:p25 phosphorylates PRDX1\"\nxref: Reactome:R-HSA-8868573 \"CDK5:p25 phosphorylates PRDX2\"\nxref: Reactome:R-HSA-8868666 \"CDK5:p25 phosphorylates JUN\"\nxref: Reactome:R-HSA-8870558 \"CDK5:p25 phosphorylates FOXO3\"\nxref: Reactome:R-HSA-8873929 \"Casein kinase II phosphorylates STARD10\"\nxref: Reactome:R-HSA-8876446 \"p-ULK1 phosphorylates DENND3\"\nxref: Reactome:R-HSA-8877691 \"MAP2K6 phosphorylates PIP4K2B\"\nxref: Reactome:R-HSA-8878050 \"HIPK2 phosphorylates RUNX1 and EP300\"\nxref: Reactome:R-HSA-8878054 \"HIPK2 phosphorylates RUNX1\"\nxref: Reactome:R-HSA-8932322 \"CK2 phosphorylates NFE2L2\"\nxref: Reactome:R-HSA-8933446 \"Active AKT phosphorylates DENND1A and DENND1B in response to insulin signaling\"\nxref: Reactome:R-HSA-8939963 \"Activated AKT phosphorylates RUNX2\"\nxref: Reactome:R-HSA-8940100 \"CDK1 phosphorylates VCPIP1\"\nxref: Reactome:R-HSA-8942836 \"CDK4/6:CCND complexes are activated by T-loop phosphorylation of CDK4/6\"\nxref: Reactome:R-HSA-8944454 \"mTORC1 phosphorylates MAF1\"\nxref: Reactome:R-HSA-8948039 \"FUNDC1 is phosphorylated by CK2\"\nxref: Reactome:R-HSA-8948146 \"FUNDC1 is phosphorylated by ULK1 at Ser17\"\nxref: Reactome:R-HSA-8948757 \"AKT phosphorylates MKRN1\"\nxref: Reactome:R-HSA-8952289 \"FAM20C phosphorylates FAM20C substrates\"\nxref: Reactome:R-HSA-9007539 \"CHEK1 phosphorylates E2F6\"\nxref: Reactome:R-HSA-9008480 \"GSK3B phosphorylates RUNX2\"\nxref: Reactome:R-HSA-9008822 \"PPM1D dephosphorylates RUNX2\"\nxref: Reactome:R-HSA-9009208 \"Activated ERKs phosphorylate RUNX2\"\nxref: Reactome:R-HSA-9012319 \"p-TEFb phosphorylates serine 2 in RNA polymerase II CTD\"\nxref: Reactome:R-HSA-9013978 \"Phosphorylation of IRF-3/IRF7 and their release from the activated TLR3 complex\"\nxref: Reactome:R-HSA-9021357 \"PRKCI phosphorylates ELF3\"\nxref: Reactome:R-HSA-9022314 \"HIPK2 phosphorylates MECP2\"\nxref: Reactome:R-HSA-9023132 \"AURKB phosphorylates MECP2 at S423\"\nxref: Reactome:R-HSA-9032751 \"Estrogen-independent phosphorylation of ESR1 S118 by MAPK1 and MAPK3\"\nxref: Reactome:R-HSA-9032863 \"CDK5 phosphorylates NTRK2\"\nxref: Reactome:R-HSA-912470 \"ATR phosphorylates Histone H2A.X at unsynapsed regions\"\nxref: Reactome:R-HSA-913996 \"PKA/PKG phosphorylate Rap1GAP2\"\nxref: Reactome:R-HSA-918229 \"Phosphorylation and release of IRF3/IRF7\"\nxref: Reactome:R-HSA-927889 \"SMG1 phosphorylates UPF1 (enhanced by Exon Junction Complex)\"\nxref: Reactome:R-HSA-933525 \"Phosphorylation and release of IRF7\"\nxref: Reactome:R-HSA-934559 \"SPRY2 is phosphorylated by phosphorylated MNK1\"\nxref: Reactome:R-HSA-936951 \"Activation of TAK1 complex bound to activated TLR4 complex\"\nxref: Reactome:R-HSA-937022 \"IRAK4 autophosphorylation in the complex with activated TLR:MyD88:TIRAP\"\nxref: Reactome:R-HSA-937059 \"Phosphorylation of IRAK2 bound to the activated IRAK4:MyD88 oligomer:TIRAP:activated TLR complex\"\nxref: Reactome:R-HSA-9604328 \"AKT1 phosphorylates NOTCH4\"\nxref: Reactome:R-HSA-9610153 \"Activated BRAF phosphorylates MAP2K dimers downstream of RAP1 and NGF\"\nxref: Reactome:R-HSA-9610156 \"MAP2Ks phosphorylate MAPKs downstream of BRAF and NGF\"\nxref: Reactome:R-HSA-9610163 \"BRAF autophosphorylates downstream of RAP1 and NGF\"\nxref: Reactome:R-HSA-9612501 \"SGK phosphorylates CREB1\"\nxref: Reactome:R-HSA-9612509 \"SGK phosphorylates SRF\"\nxref: Reactome:R-HSA-9612980 \"BRAF in Rap1-GTP complex:BRAF complex autophosphorylates\"\nxref: Reactome:R-HSA-9613530 \"PRKAA2 phosphorylates PLINs\"\nxref: Reactome:R-HSA-9619515 \"AMPK phosphorylates MAPT\"\nxref: Reactome:R-HSA-9619843 \"ERKs phosphorylate RSKs\"\nxref: Reactome:R-HSA-9620004 \"RSKs autophosphorylate\"\nxref: Reactome:R-HSA-9624526 \"AKT phosphorylates FOXO3 downstream of ESR1 and EGFR\"\nxref: Reactome:R-HSA-9626880 \"MAPK11 or MAPK14 phosphorylates NCF1 at Ser345\"\nxref: Reactome:R-HSA-9627089 \"CASP9 is phosphorylated at T412\"\nxref: Reactome:R-HSA-9632858 \"PRKCZ autophosphorylates downstream of estrogen stimulation\"\nxref: Reactome:R-HSA-9632868 \"CDKN1B is phosphorylated in response to estrogen\"\nxref: Reactome:R-HSA-9633008 \"p-T899-EIF2AK4 (GCN2) phosphorylates EIF2AS1\"\nxref: Reactome:R-HSA-9633742 \"EIF2AK4 (GCN2) dimer autophosphorylates\"\nxref: Reactome:R-HSA-9634702 \"LINC01139 promotes phosphorylation of HIF1A by LRRK2\"\nxref: Reactome:R-HSA-9645535 \"ALPK1 phosphorylates TIFA\"\nxref: Reactome:R-HSA-9648089 \"NEK6 and NEK7 phosphorylate EML4\"\nxref: Reactome:R-HSA-9648883 \"p-T-EIF2AK1:ferriheme dimer autophosphorylates\"\nxref: Reactome:R-HSA-9648888 \"p-T,T486,T488-EIF2AK1 phosphorylates EIF2S1 (eIF2-alpha)\"\nxref: Reactome:R-HSA-9652165 \"MAP2K mutants constitutively phosphorylate MAPKs\"\nxref: Reactome:R-HSA-9653503 \"KRAS4B is phosphorylated on serine 181\"\nxref: Reactome:R-HSA-9656214 \"MAP2Ks phosphorylate MAPKs downstream of RAF1 mutants\"\nxref: Reactome:R-HSA-9656215 \"RAF1 mutant complexes phosphorylate MAP2K dimer\"\nxref: Reactome:R-HSA-9662823 \"PLK2, MAPK14 phosphorylate ADAM17\"\nxref: Reactome:R-HSA-9673346 \"Unknown kinase phosphorylates p-DVL\"\nxref: Reactome:R-HSA-9683664 \"GSK3 phosphorylates Nucleoprotein\"\nxref: Reactome:R-HSA-9699579 \"AKT phosphorylates FOXO3 downstream of FLT3\"\nxref: Reactome:R-HSA-9705320 \"TBK1, IKBKE are autophosphorylated at Ser172\"\nxref: Reactome:R-HSA-9705323 \"Phosphorylation of TBK1/IKBKE\"\nxref: Reactome:R-HSA-9725030 \"MAPK1 phsophorylates ZC3HCF1 in a NPM-ALK-dependent manner\"\nxref: Reactome:R-HSA-9729260 \"GSK3 phosphorylates nucleoprotein\"\nxref: Reactome:R-HSA-9729300 \"Unknown kinase phosphorylates nucleoprotein\"\nxref: Reactome:R-HSA-9729318 \"CSNK1A1 phosphorylates nucleoprotein\"\nxref: Reactome:R-HSA-9731111 \"MAPK1 and MAPK3 phosphorylate SMAD2 and SMAD3\"\nxref: Reactome:R-HSA-9734547 \"JAK2-activated MAPKs phosphorylate YBX1\"\nxref: Reactome:R-HSA-975125 \"Multiple IRAK1 autophosphorylation steps within the complex pIRAK4:MyD88:activated TLR7/8 or 9\"\nxref: Reactome:R-HSA-975134 \"Second phosphorylation of IRAK1 by IRAK4 bound to MyD88: activated TLR 7/8 or 9\"\nxref: Reactome:R-HSA-975160 \"Phosphorylation of IRAK2 bound to the activated IRAK4:MyD88 oligomer:activated TLR 7/8 or 9\"\nxref: Reactome:R-HSA-975170 \"IRAK4 autophosphorylation in the complex with MyD88:activated TLR 7/8 or 9\"\nxref: Reactome:R-HSA-975180 \"First phosphorylation of IRAK1 by IRAK4 bound to MyD88:activated TLR 7/8 or 9\"\nxref: Reactome:R-HSA-9758486 \"Unknown kinase phosphorylates 9b\"\nxref: Reactome:R-HSA-975853 \"Multiple IRAK1 autophosphorylation within the complex p-IRAK4:oligo MyD88:activated TLR\"\nxref: Reactome:R-HSA-975861 \"Phosphorylation of IRAK2 bound to the activated IRAK4:MyD88 oligomerl:activated TLR5 or 10 complex\"\nxref: Reactome:R-HSA-975865 \"IRAK4 autophosphorylation within the complex activated TLR:MyD88\"\nxref: Reactome:R-HSA-975874 \"Second phosphorylation of IRAK1 by IRAK4 bound to MyD88:activated TLR complex\"\nxref: Reactome:R-HSA-975878 \"First phosphorylation of IRAK1 by IRAK4 bound to MyD88:activated TLR\"\nxref: Reactome:R-HSA-9762094 \"GSK3B phosphorylates p-NFE2L2\"\nxref: Reactome:R-HSA-9765960 \"ERKs phosphorylate MCRIP1\"\nxref: Reactome:R-HSA-9766532 \"SQSTM1 oligomer is phosphorylated\"\nxref: Reactome:R-HSA-9769115 \"MAPK1,(MAPK3) phosphorylates NPAS4\"\nxref: Reactome:R-HSA-9773803 \"Active IKBKB phosphorylates NF-kappa-B inhibitor\"\nxref: Reactome:R-HSA-9796053 \"PRKCI phosphorylates NFE2L2\"\nxref: Reactome:R-HSA-9796067 \"PRKAA2 phosphorylates nuclear NFE2L2\"\nxref: Reactome:R-HSA-9796081 \"EIF2AK3 phosphorylates NFE2L2\"\nxref: Reactome:R-HSA-9815501 \"MAPKAPK2 phosphorylates RIPK1 at S320\"\nxref: Reactome:R-HSA-9817397 \"TBK1, IKBKE phosphorylate RIPK1 at T189\"\nxref: Reactome:R-HSA-9818789 \"CHUK, IKBKB phosphorylate RIPK1 at S25\"\nxref: Reactome:R-HSA-9819106 \"ULK1 phosphorylates RIPK1 at S357\"\nxref: Reactome:R-HSA-9824582 \"MAPK1 phosphorylates SOX10\"\nxref: Reactome:R-HSA-9824897 \"p-S-TBK1 phosphorylates OPTN\"\nxref: Reactome:R-HSA-9824977 \"MAPK1-dependent phosphorylation of MITF-M\"\nxref: Reactome:R-HSA-9824994 \"RPS6KA1-dependent phosphorylation of MITF-M\"\nxref: Reactome:R-HSA-9824995 \"GSK3B phosphorylates p-S409 MITF-M at S397, S401 and S405\"\nxref: Reactome:R-HSA-9824999 \"GSK3B phosphorylates p-S73 MITF-M at residue S69\"\nxref: Reactome:R-HSA-9825704 \"AKT3 phosphorylates TBX3\"\nxref: Reactome:R-HSA-9831514 \"CK2 phosphorylates nascent P\"\nxref: Reactome:R-HSA-9831712 \"M dimer is phosphorylated\"\nxref: Reactome:R-HSA-9832782 \"p-S232-S237-P is further phosphorylated\"\nxref: Reactome:R-HSA-9834076 \"PINK1 is autophosphorylated\"\nxref: Reactome:R-HSA-9834945 \"PINK1 phosphorylates Ub on MOM proteins\"\nxref: Reactome:R-HSA-9835011 \"PINK1 phosphorylates PRKN at S65\"\nxref: Reactome:R-HSA-9839363 \"TGFBR3 phosphorylation by TGFBR2 complex\"\nxref: Reactome:R-HSA-9851972 \"PLK1 phosphorylates FIRRM at S43\"\nxref: Reactome:R-HSA-9853369 \"PLK1 phosphorylates FIRMM at S744\"\nxref: Reactome:R-HSA-9855910 \"USF1 is phosphorylated by p-MAPK14\"\nxref: Reactome:R-HSA-9857661 \"p-T308,S473-AKT1 (phospho-PKB) phosphorylates GJA1 (Connexin-43)\"\nxref: Reactome:R-HSA-9857673 \"p-T308,S473-AKT1 phosphorylates ITGA5 (Integrin alpha5) in ITGA5:ITGB1 (Integrin alpha5:Integrin beta1)\"\nxref: Reactome:R-HSA-9860292 \"Activated IKBKB phosphorylates IRF5\"\nxref: Reactome:R-HSA-9860785 \"PDPK1 (PDK1) phosphorylates PKN2 on threonine-816\"\nxref: Reactome:R-HSA-9860800 \"mTORC2 phosphorylates AKT1 on serine-473\"\nxref: Reactome:R-HSA-9861642 \"NEK1 phosphorylates ME1\"\nxref: Reactome:R-HSA-9909369 \"CSNK1E,CSNK1D phosphorylate CRY and PER proteins\"\nxref: Reactome:R-HSA-9912396 \"CDK5 phosphorylates CLOCK on serine-451 and serine-461\"\nxref: Reactome:R-HSA-9912401 \"CK2alpha phosphorylates BMAL1 (ARNTL) on serine-90\"\nxref: Reactome:R-HSA-9920673 \"CDK5 phosphorylates PER2 on serine-396\"\nxref: Reactome:R-HSA-9922273 \"CSNK1D,E phosphorylates CLOCK in p-S-CRY:p-S-PER:CSNK1D,E:p-S90,Ac-538-BMAL:p-2T,3S-CLOCK:target gene\"\nxref: Reactome:R-HSA-9926483 \"MARK3 phosphorylates MITF-M on S173\"\nxref: Reactome:R-HSA-9929360 \"GSK3B phosphorylates CD274\"\nxref: Reactome:R-HSA-9931292 \"AMPK phosphorylates CD274\"\nxref: Reactome:R-HSA-9931409 \"NEK2 phosphorylates CD274\"\nxref: Reactome:R-HSA-9931418 \"CK2 phosphorylates CD274\"\nxref: Reactome:R-HSA-9933380 \"Cytosolic tail of CDH1 is phosphorylated\"\nxref: Reactome:R-HSA-9942578 \"Phosphorylation of CDC25A by p38 MAPK\"\nxref: Reactome:R-HSA-9943662 \"CHEK1 phosphorylates NEK11\"\nxref: Reactome:R-HSA-9943675 \"GSK3B phosphorylates CDC25A\"\nxref: Reactome:R-HSA-9943676 \"NEK11 phosphorylates CDC25A\"\nxref: Reactome:R-HSA-9943678 \"CHEK1 phosphorylates CHEK2-phosphorylated CDC25A\"\nxref: Reactome:R-HSA-9943687 \"PLK3 phosphorylates CDC25A\"\nxref: Reactome:R-HSA-9943736 \"Casein kinase I phosphorylates CDC25A\"\nxref: Reactome:R-HSA-9954237 \"PIM1 phosphorylates GBP1\"\nis_a: GO:0004672 ! protein kinase activity\nproperty_value: skos:exactMatch EC:2.7.11.-\nproperty_value: skos:exactMatch MetaCyc:PROTEIN-KINASE-RXN\nproperty_value: skos:narrowMatch EC:2.7.11.1\nproperty_value: skos:narrowMatch EC:2.7.11.28\nproperty_value: skos:narrowMatch EC:2.7.11.29\nproperty_value: skos:narrowMatch EC:2.7.11.3\nproperty_value: skos:narrowMatch EC:2.7.11.9\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0004674",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 46709-47278",
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
  "excerpt": "[Term]\nid: GO:0018826\nname: methionine gamma-lyase activity\nnamespace: molecular_function\ndef: \"Catalysis of the reaction: L-methionine + H2O = methanethiol + 2-oxobutanoate + NH4+.\" [RHEA:23800]\nsynonym: \"L-methioninase activity\" RELATED [EC:4.4.1.11]\nsynonym: \"L-methionine gamma-lyase activity\" RELATED [EC:4.4.1.11]\nsynonym: \"L-methionine methanethiol-lyase (deaminating)\" RELATED [EC:4.4.1.11]\nsynonym: \"L-methionine methanethiol-lyase (deaminating; 2-oxobutanoate-forming)\" RELATED [EC:4.4.1.11]\nsynonym: \"methioninase activity\" RELATED [EC:4.4.1.11]\nsynonym: \"methionine dethiomethylase activity\" RELATED [EC:4.4.1.11]\nsynonym: \"methionine lyase activity\" RELATED [EC:4.4.1.11]\nxref: EC:4.4.1.11\nxref: MetaCyc:METHIONINE-GAMMA-LYASE-RXN\nxref: RHEA:23800\nxref: UM-BBD_reactionID:r0432\nis_a: GO:0016846 ! carbon-sulfur lyase activity\nproperty_value: skos:exactMatch EC:4.4.1.11\nproperty_value: skos:exactMatch RHEA:23800\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0018826",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 142709-142728",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 91. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
