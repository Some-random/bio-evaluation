# GO_molecular_function_0171

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_molecular_function_0171.txt)

**Task:** `GO_molecular_function`  
**Expected answer:** **A** — protein dimerization activity

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MAEIPTSSNPSDDPETQKLNGNEEDYDHHHDEDPESDDENYEYALQIAEMLPFPMVMQTAIELDLLGIIATAGPDRQLSAAEIAAALPAAGNPDAPAMLDRMLYLLATYSVVTCTAVDGGASGGVVRKYGLAPVAKYFVSNEDGVSLGALISLNQGQAFLASWSKLKEAVLEGGIPFNKVHGMDVFHYQGTDPRFNKIFNKAMYGQSTYIIKKIVRRYKGFENIQRLVDVGGGLGHTLRVITSNYPSIKGINFDLPHVIQHAPTIPGVEHVGGDMFESIPNGDAIFMKCILHDWSDEHCLKTLKNCYKALPRKGKVIVVQMNMIEEPQTTPLAKAISQLDVCLMTQSPGGKERTRREFQTLAEAAGFAEFNPVCHVAGFWVMEFLK

[Multiple Choices]
A. protein dimerization activity
B. magnesium ion binding
C. metal ion transmembrane transporter activity
D. sphingomyelin transfer activity
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

> The exact sequence is annotated with protein dimerization activity in UniProt, with IEA:InterPro evidence. This is computational annotation, not direct experimental evidence of dimerization; the reported O-methyltransferase activity does not contradict it.

Citations as saved: [C11](#evidence-c11), [H10](#evidence-h10).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with a soluble plant O-methyltransferase rather than a membrane transporter or lipid-transfer protein. Transferable knowledge of plant O-methyltransferases, including their tendency to form dimers, gives a credible basis for option A over C or D and favors A among the choices. However, some related O-methyltransferases also bind magnesium, so that family inference does not cleanly exclude B.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level sequence recognition provides a meaningful, probabilistic basis for A without requiring recall of this exact protein's record. It does not establish that dimerization is the protein's primary function, and the choices are not mutually exclusive: magnesium binding may also be plausible for related enzymes.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> Dimerization is a plausible family-level property, while magnesium binding is also plausible for some plant O-methyltransferases. The prompt asks for a primary function but does not make these potentially coexisting molecular functions exclusive.


### Important caveats

- The evidence for the keyed dimerization term is an InterPro-based computational annotation, not an experimental dimerization result.
- The protein's O-methyltransferase catalytic activity is not among the answer choices.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a soluble plant O-methyltransferase rather than a membrane transporter or lipid-transfer protein. Transferable knowledge of plant O-methyltransferases, including their tendency to form dimers, gives a credible basis for option A over C or D and favors A among the choices. However, some related O-methyltransferases also bind magnesium, so that family inference does not cleanly exclude B.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level sequence recognition provides a meaningful, probabilistic basis for A without requiring recall of this exact protein's record. It does not establish that dimerization is the protein's primary function, and the choices are not mutually exclusive: magnesium binding may also be plausible for related enzymes."
  },
  "case_id": "GO_molecular_function_0171",
  "expected_answer_check": {
    "evidence_ids": [
      "C11",
      "H10"
    ],
    "judgment": "supported",
    "reason": "The exact sequence is annotated with protein dimerization activity in UniProt, with IEA:InterPro evidence. This is computational annotation, not direct experimental evidence of dimerization; the reported O-methyltransferase activity does not contradict it."
  },
  "important_caveats": [
    "The evidence for the keyed dimerization term is an InterPro-based computational annotation, not an experimental dimerization result.",
    "The protein's O-methyltransferase catalytic activity is not among the answer choices."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "Dimerization is a plausible family-level property, while magnesium binding is also plausible for some plant O-methyltransferases. The prompt asks for a primary function but does not make these potentially coexisting molecular functions exclusive."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0171",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence is annotated with protein dimerization activity in UniProt, with IEA:InterPro evidence. This is computational annotation, not direct experimental evidence of dimerization; the reported O-methyltransferase activity does not contradict it.",
    "evidence_ids": ["C11", "H10"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with a soluble plant O-methyltransferase rather than a membrane transporter or lipid-transfer protein. Transferable knowledge of plant O-methyltransferases, including their tendency to form dimers, gives a credible basis for option A over C or D and favors A among the choices. However, some related O-methyltransferases also bind magnesium, so that family inference does not cleanly exclude B.",
    "missing_item_specific_fact": "",
    "reason": "Family-level sequence recognition provides a meaningful, probabilistic basis for A without requiring recall of this exact protein's record. It does not establish that dimerization is the protein's primary function, and the choices are not mutually exclusive: magnesium binding may also be plausible for related enzymes."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "Dimerization is a plausible family-level property, while magnesium binding is also plausible for some plant O-methyltransferases. The prompt asks for a primary function but does not make these potentially coexisting molecular functions exclusive."
  },
  "important_caveats": [
    "The evidence for the keyed dimerization term is an InterPro-based computational annotation, not an experimental dimerization result.",
    "The protein's O-methyltransferase catalytic activity is not among the answer choices."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> GO:0046983 (protein dimerization activity) is annotated to this protein (A0AA51Z0J6) with evidence code IEA:InterPro (evidence C11/H10). However, this is a secondary automated annotation. The protein's experimentally verified primary molecular function is O-methyltransferase activity (GO:0008171, ECO:0000269|PubMed:37675639), which is NOT among the offered choices. The author selected A because it is the only option with any annotation linkage to this protein, even though it does not represent the primary molecular function. The annotation technically exists, so the key is supported in a narrow sense, but the question is misleading by labeling this as the 'primary molecular function.'

Citations as saved: [C11](#evidence-c11), [C10](#evidence-c10), [C5](#evidence-c5), [H10](#evidence-h10), [H9](#evidence-h9).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains hallmark features of a class I SAM-dependent O-methyltransferase (plant-type): the GxGxG nucleotide-binding motif region, the VQMNM segment characteristic of plant OMTs, and the overall ~386-aa length typical of this family. A knowledgeable model would recognize this as a plant O-methyltransferase. Since methyltransferase activity is not among the options, the model can apply family-level knowledge that plant O-methyltransferases (COMT, CCoAOMT, isoflavone OMTs, etc.) characteristically function as homodimers, making 'protein dimerization activity' a plausible family-associated property. Options B (magnesium ion binding), C (metal ion transmembrane transporter), and D (sphingomyelin transfer) can be eliminated: the sequence lacks transmembrane helices (ruling out C), lacks canonical Mg-binding motifs (ruling out B), and bears no structural resemblance to lipid-transfer proteins (ruling out D). Thus, among the four offered choices, A is the only biologically plausible option for a plant OMT family member.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A model can identify the protein family from conserved sequence motifs, recall that plant OMTs commonly homodimerize (transferable family knowledge), and eliminate the three clearly incompatible alternatives through sequence-based reasoning. No target-specific annotation lookup is strictly necessary to arrive at A among the four choices.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although the question asks for 'primary molecular function' and the true primary function (O-methyltransferase activity) is absent from the options, only option A has any biological plausibility for this protein. Options B, C, and D are clearly incompatible with the sequence and family identity. No ambiguity exists among the offered choices.


### Important caveats

- The author's key (A, protein dimerization activity) is a secondary IEA:InterPro annotation, NOT the experimentally verified primary molecular function (O-methyltransferase activity, GO:0008171). The question is poorly constructed because the actual primary function is not offered as a choice.
- The dimerization annotation is automated (IEA:InterPro) and not experimentally validated for this specific protein; it is inferred from the InterPro family signature shared with other plant OMTs.
- The protein was first publicly annotated in June 2025; the benchmark's exact source snapshot is unknown but the sequence matches across available versions.
- The question's framing ('primary molecular function') is misleading given the offered options; a well-informed model might be confused by the absence of methyltransferase activity among choices.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains hallmark features of a class I SAM-dependent O-methyltransferase (plant-type): the GxGxG nucleotide-binding motif region, the VQMNM segment characteristic of plant OMTs, and the overall ~386-aa length typical of this family. A knowledgeable model would recognize this as a plant O-methyltransferase. Since methyltransferase activity is not among the options, the model can apply family-level knowledge that plant O-methyltransferases (COMT, CCoAOMT, isoflavone OMTs, etc.) characteristically function as homodimers, making 'protein dimerization activity' a plausible family-associated property. Options B (magnesium ion binding), C (metal ion transmembrane transporter), and D (sphingomyelin transfer) can be eliminated: the sequence lacks transmembrane helices (ruling out C), lacks canonical Mg-binding motifs (ruling out B), and bears no structural resemblance to lipid-transfer proteins (ruling out D). Thus, among the four offered choices, A is the only biologically plausible option for a plant OMT family member.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A model can identify the protein family from conserved sequence motifs, recall that plant OMTs commonly homodimerize (transferable family knowledge), and eliminate the three clearly incompatible alternatives through sequence-based reasoning. No target-specific annotation lookup is strictly necessary to arrive at A among the four choices."
  },
  "case_id": "GO_molecular_function_0171",
  "expected_answer_check": {
    "evidence_ids": [
      "C11",
      "C10",
      "C5",
      "H10",
      "H9"
    ],
    "judgment": "supported",
    "reason": "GO:0046983 (protein dimerization activity) is annotated to this protein (A0AA51Z0J6) with evidence code IEA:InterPro (evidence C11/H10). However, this is a secondary automated annotation. The protein's experimentally verified primary molecular function is O-methyltransferase activity (GO:0008171, ECO:0000269|PubMed:37675639), which is NOT among the offered choices. The author selected A because it is the only option with any annotation linkage to this protein, even though it does not represent the primary molecular function. The annotation technically exists, so the key is supported in a narrow sense, but the question is misleading by labeling this as the 'primary molecular function.'"
  },
  "important_caveats": [
    "The author's key (A, protein dimerization activity) is a secondary IEA:InterPro annotation, NOT the experimentally verified primary molecular function (O-methyltransferase activity, GO:0008171). The question is poorly constructed because the actual primary function is not offered as a choice.",
    "The dimerization annotation is automated (IEA:InterPro) and not experimentally validated for this specific protein; it is inferred from the InterPro family signature shared with other plant OMTs.",
    "The protein was first publicly annotated in June 2025; the benchmark's exact source snapshot is unknown but the sequence matches across available versions.",
    "The question's framing ('primary molecular function') is misleading given the offered options; a well-informed model might be confused by the absence of methyltransferase activity among choices."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the question asks for 'primary molecular function' and the true primary function (O-methyltransferase activity) is absent from the options, only option A has any biological plausibility for this protein. Options B, C, and D are clearly incompatible with the sequence and family identity. No ambiguity exists among the offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0171",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "GO:0046983 (protein dimerization activity) is annotated to this protein (A0AA51Z0J6) with evidence code IEA:InterPro (evidence C11/H10). However, this is a secondary automated annotation. The protein's experimentally verified primary molecular function is O-methyltransferase activity (GO:0008171, ECO:0000269|PubMed:37675639), which is NOT among the offered choices. The author selected A because it is the only option with any annotation linkage to this protein, even though it does not represent the primary molecular function. The annotation technically exists, so the key is supported in a narrow sense, but the question is misleading by labeling this as the 'primary molecular function.'",
    "evidence_ids": ["C11", "C10", "C5", "H10", "H9"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains hallmark features of a class I SAM-dependent O-methyltransferase (plant-type): the GxGxG nucleotide-binding motif region, the VQMNM segment characteristic of plant OMTs, and the overall ~386-aa length typical of this family. A knowledgeable model would recognize this as a plant O-methyltransferase. Since methyltransferase activity is not among the options, the model can apply family-level knowledge that plant O-methyltransferases (COMT, CCoAOMT, isoflavone OMTs, etc.) characteristically function as homodimers, making 'protein dimerization activity' a plausible family-associated property. Options B (magnesium ion binding), C (metal ion transmembrane transporter), and D (sphingomyelin transfer) can be eliminated: the sequence lacks transmembrane helices (ruling out C), lacks canonical Mg-binding motifs (ruling out B), and bears no structural resemblance to lipid-transfer proteins (ruling out D). Thus, among the four offered choices, A is the only biologically plausible option for a plant OMT family member.",
    "missing_item_specific_fact": "",
    "reason": "A model can identify the protein family from conserved sequence motifs, recall that plant OMTs commonly homodimerize (transferable family knowledge), and eliminate the three clearly incompatible alternatives through sequence-based reasoning. No target-specific annotation lookup is strictly necessary to arrive at A among the four choices."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the question asks for 'primary molecular function' and the true primary function (O-methyltransferase activity) is absent from the options, only option A has any biological plausibility for this protein. Options B, C, and D are clearly incompatible with the sequence and family identity. No ambiguity exists among the offered choices."
  },
  "important_caveats": [
    "The author's key (A, protein dimerization activity) is a secondary IEA:InterPro annotation, NOT the experimentally verified primary molecular function (O-methyltransferase activity, GO:0008171). The question is poorly constructed because the actual primary function is not offered as a choice.",
    "The dimerization annotation is automated (IEA:InterPro) and not experimentally validated for this specific protein; it is inferred from the InterPro family signature shared with other plant OMTs.",
    "The protein was first publicly annotated in June 2025; the benchmark's exact source snapshot is unknown but the sequence matches across available versions.",
    "The question's framing ('primary molecular function') is misleading given the offered options; a well-informed model might be confused by the absence of methyltransferase activity among choices."
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
  "benchmark_sequence_length": 386,
  "benchmark_sequence_sha256": "e9eeb8d6c8b562b1805ea6984ca9c62b2d5451bab29078b5f792845db158170c",
  "current_entry_audit": {
    "entryVersion": 12,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2024-01-24",
    "sequenceVersion": 1
  },
  "current_record_sha256": "0a496afceff4c5f0045b71e5aabc8881817c410e0d2ca1f7adf3641e409bfa49",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 386,
  "current_source_sequence_sha256": "e9eeb8d6c8b562b1805ea6984ca9c62b2d5451bab29078b5f792845db158170c",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 10,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0AA51Z0J6",
  "selected_historical_entry_version": 10,
  "selected_historical_record_sha256": "88903183e4675ef7b87342d80b4056576bfff1355cba383be12860aebc9c0f57",
  "selected_historical_source_sequence_length": 386,
  "selected_historical_source_sequence_sha256": "e9eeb8d6c8b562b1805ea6984ca9c62b2d5451bab29078b5f792845db158170c",
  "selected_historical_version": {
    "accession": "A0AA51Z0J6",
    "database": "Swiss-Prot",
    "entryVersion": 10,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "OMT12_LOPWI",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51Z0J6.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0AA51Z0J6\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:26:23.632196+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0a496afceff4c5f0045b71e5aabc8881817c410e0d2ca1f7adf3641e409bfa49",
  "url": "https://rest.uniprot.org/uniprotkb/A0AA51Z0J6.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51Z0J6.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":12,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2024-01-24\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:26:23.632196+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0a496afceff4c5f0045b71e5aabc8881817c410e0d2ca1f7adf3641e409bfa49",
  "url": "https://rest.uniprot.org/uniprotkb/A0AA51Z0J6.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51Z0J6.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Peyote\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"Caryophyllales\",\"Cactineae\",\"Cactaceae\",\"Cactoideae\",\"Cacteae\",\"Lophophora\"],\"scientificName\":\"Lophophora williamsii\",\"synonyms\":[\"Echinocactus williamsii\"],\"taxonId\":130138}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:26:23.632196+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0a496afceff4c5f0045b71e5aabc8881817c410e0d2ca1f7adf3641e409bfa49",
  "url": "https://rest.uniprot.org/uniprotkb/A0AA51Z0J6.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51Z0J6.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"37675639\",\"source\":\"PubMed\"}],\"value\":\"O-methyltransferase 10\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"37675639\",\"source\":\"PubMed\"}],\"value\":\"LwOMT10\"}]}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01020\",\"source\":\"PROSITE-ProRule\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"37675639\",\"source\":\"PubMed\"}],\"value\":\"2.1.1.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38835170\",\"source\":\"PubMed\"}],\"value\":\"O-methyltransferase 12\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38835170\",\"source\":\"PubMed\"}],\"value\":\"LwOMT12\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:26:23.632196+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0a496afceff4c5f0045b71e5aabc8881817c410e0d2ca1f7adf3641e409bfa49",
  "url": "https://rest.uniprot.org/uniprotkb/A0AA51Z0J6.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51Z0J6.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"37675639\",\"source\":\"PubMed\"}],\"value\":\"O-methyltransferase participating in the biosynthesis of natural products derived from phenylethylamine, including mescaline, a natural hallucinogen potentially used in psychotherapeutic treatments (PubMed:37675639). Catalyzes the O-methylation of dopamine, 4-hydroxy-3,5-dimethoxyphenethylamine, 4,5-dihydroxy-3-methoxyphenethylamine and N-methyl-4,5-dihydroxy-3-methoxyphenethylamine (PubMed:37675639). Also involved in the conversion of N-methyl-4-hydroxy-3,5-dimethoxyphenethylamine to N-methylmescaline (PubMed:37675639)\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-02T04:26:23.632196+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0a496afceff4c5f0045b71e5aabc8881817c410e0d2ca1f7adf3641e409bfa49",
  "url": "https://rest.uniprot.org/uniprotkb/A0AA51Z0J6.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51Z0J6.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"37675639\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:81060\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"37675639\",\"source\":\"PubMed\"}],\"name\":\"4-hydroxy-3,5-dimethoxyphenethylamine + S-adenosyl-L-methionine = mescaline + S-adenosyl-L-homocysteine + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:81059\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57856\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:59789\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231762\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231768\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:26:23.632196+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0a496afceff4c5f0045b71e5aabc8881817c410e0d2ca1f7adf3641e409bfa49",
  "url": "https://rest.uniprot.org/uniprotkb/A0AA51Z0J6.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51Z0J6.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"37675639\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:81048\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"37675639\",\"source\":\"PubMed\"}],\"name\":\"dopamine + S-adenosyl-L-methionine = 4-methoxytyramine + S-adenosyl-L-homocysteine + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:81047\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57856\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:59789\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:59905\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:192993\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:26:23.632196+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0a496afceff4c5f0045b71e5aabc8881817c410e0d2ca1f7adf3641e409bfa49",
  "url": "https://rest.uniprot.org/uniprotkb/A0AA51Z0J6.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51Z0J6.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"37675639\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:81052\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"37675639\",\"source\":\"PubMed\"}],\"name\":\"3,4-dihydroxy-5-methoxyphenethylamine + S-adenosyl-L-methionine = 3-hydroxy-4,5-dimethoxyphenethylamine + S-adenosyl-L-homocysteine + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:81051\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57856\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:59789\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231763\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231769\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-02T04:26:23.632196+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0a496afceff4c5f0045b71e5aabc8881817c410e0d2ca1f7adf3641e409bfa49",
  "url": "https://rest.uniprot.org/uniprotkb/A0AA51Z0J6.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51Z0J6.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"37675639\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:84996\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"37675639\",\"source\":\"PubMed\"}],\"name\":\"N-methyl-4-hydroxy-3,5-dimethoxyphenethylamine + S-adenosyl-L-methionine = N-methylmescaline + S-adenosyl-L-homocysteine + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:84995\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57856\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:59789\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231777\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231781\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/4",
  "retrieved_utc": "2026-11-02T04:26:23.632196+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0a496afceff4c5f0045b71e5aabc8881817c410e0d2ca1f7adf3641e409bfa49",
  "url": "https://rest.uniprot.org/uniprotkb/A0AA51Z0J6.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51Z0J6.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0008171\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:O-methyltransferase activity\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:InterPro\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/4",
  "retrieved_utc": "2026-11-02T04:26:23.632196+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0a496afceff4c5f0045b71e5aabc8881817c410e0d2ca1f7adf3641e409bfa49",
  "url": "https://rest.uniprot.org/uniprotkb/A0AA51Z0J6.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51Z0J6.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0046983\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:protein dimerization activity\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:InterPro\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/5",
  "retrieved_utc": "2026-11-02T04:26:23.632196+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0a496afceff4c5f0045b71e5aabc8881817c410e0d2ca1f7adf3641e409bfa49",
  "url": "https://rest.uniprot.org/uniprotkb/A0AA51Z0J6.json"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51Z0J6.json)

```json
{
  "evidence_id": "C12",
  "excerpt": "{\"citation\":{\"authors\":[\"Watkins J.L.\",\"Li Q.\",\"Yeaman S.\",\"Facchini P.J.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"37675639\"},{\"database\":\"DOI\",\"id\":\"10.1111/tpj.16447\"}],\"citationType\":\"journal article\",\"firstPage\":\"635\",\"id\":\"37675639\",\"journal\":\"Plant J.\",\"lastPage\":\"649\",\"publicationDate\":\"2023\",\"title\":\"Elucidation of the mescaline biosynthetic pathway in peyote (Lophophora williamsii).\",\"volume\":\"116\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"WMX25285.1\",\"source\":\"EMBL\"}],\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"cv. Jourdaniana\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\",\"TISSUE SPECIFICITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:26:23.632196+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0a496afceff4c5f0045b71e5aabc8881817c410e0d2ca1f7adf3641e409bfa49",
  "url": "https://rest.uniprot.org/uniprotkb/A0AA51Z0J6.json"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51Z0J6.json)

```json
{
  "evidence_id": "C13",
  "excerpt": "{\"citation\":{\"authors\":[\"Berman P.\",\"de Haro L.A.\",\"Cavaco A.-R.\",\"Panda S.\",\"Dong Y.\",\"Kuzmich N.\",\"Lichtenstein G.\",\"Peleg Y.\",\"Harat H.\",\"Jozwiak A.\",\"Cai J.\",\"Heinig U.\",\"Meir S.\",\"Rogachev I.\",\"Aharoni A.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38835170\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.molp.2024.05.012\"}],\"citationType\":\"journal article\",\"firstPage\":\"1129\",\"id\":\"38835170\",\"journal\":\"Mol. Plant\",\"lastPage\":\"1150\",\"publicationDate\":\"2024\",\"title\":\"The biosynthetic pathway of the hallucinogen mescaline and its heterologous reconstruction.\",\"volume\":\"17\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"XBD97126.1\",\"source\":\"EMBL\"}],\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"cv. Rehovot 7\"}],\"referenceNumber\":2,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:26:23.632196+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0a496afceff4c5f0045b71e5aabc8881817c410e0d2ca1f7adf3641e409bfa49",
  "url": "https://rest.uniprot.org/uniprotkb/A0AA51Z0J6.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AA51Z0J6?format=txt&versions=10)

```json
{
  "entry_version": 10,
  "evidence_id": "H1",
  "excerpt": "ID   OMT12_LOPWI             Reviewed;         386 AA.\nAC   A0AA51Z0J6;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   24-JAN-2024, sequence version 1.\nDT   28-JAN-2026, entry version 10.\nDE   RecName: Full=O-methyltransferase 12 {ECO:0000303|PubMed:38835170};\nDE            Short=LwOMT12 {ECO:0000303|PubMed:38835170};\nDE            EC=2.1.1.- {ECO:0000255|PROSITE-ProRule:PRU01020, ECO:0000269|PubMed:37675639};\nDE   AltName: Full=O-methyltransferase 10 {ECO:0000303|PubMed:37675639};\nDE            Short=LwOMT10 {ECO:0000303|PubMed:37675639};\nGN   Name=OMT12 {ECO:0000303|PubMed:38835170};\nGN   Synonyms=OMT10 {ECO:0000303|PubMed:37675639};\nOS   Lophophora williamsii (Peyote) (Echinocactus williamsii).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   Caryophyllales; Cactineae; Cactaceae; Cactoideae; Cacteae; Lophophora.\nOX   NCBI_TaxID=130138;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:25.490622+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-17",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "88903183e4675ef7b87342d80b4056576bfff1355cba383be12860aebc9c0f57",
  "url": "https://rest.uniprot.org/unisave/A0AA51Z0J6?format=txt&versions=10"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AA51Z0J6?format=txt&versions=10)

```json
{
  "entry_version": 10,
  "evidence_id": "H2",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:WMX25285.1}\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY, PATHWAY, TISSUE\nRP   SPECIFICITY, AND BIOPHYSICOCHEMICAL PROPERTIES.\nRC   STRAIN=cv. Jourdaniana;\nRX   PubMed=37675639; DOI=10.1111/tpj.16447;\nRA   Watkins J.L., Li Q., Yeaman S., Facchini P.J.;\nRT   \"Elucidation of the mescaline biosynthetic pathway in peyote (Lophophora\nRT   williamsii).\";\nRL   Plant J. 116:635-649(2023).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:25.490622+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 18-26",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "88903183e4675ef7b87342d80b4056576bfff1355cba383be12860aebc9c0f57",
  "url": "https://rest.uniprot.org/unisave/A0AA51Z0J6?format=txt&versions=10"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AA51Z0J6?format=txt&versions=10)

```json
{
  "entry_version": 10,
  "evidence_id": "H3",
  "excerpt": "RN   [2] {ECO:0000312|EMBL:XBD97126.1}\nRP   NUCLEOTIDE SEQUENCE [MRNA].\nRC   STRAIN=cv. Rehovot 7;\nRX   PubMed=38835170; DOI=10.1016/j.molp.2024.05.012;\nRA   Berman P., de Haro L.A., Cavaco A.-R., Panda S., Dong Y., Kuzmich N.,\nRA   Lichtenstein G., Peleg Y., Harat H., Jozwiak A., Cai J., Heinig U.,\nRA   Meir S., Rogachev I., Aharoni A.;\nRT   \"The biosynthetic pathway of the hallucinogen mescaline and its\nRT   heterologous reconstruction.\";\nRL   Mol. Plant 17:1129-1150(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:25.490622+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 27-36",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "88903183e4675ef7b87342d80b4056576bfff1355cba383be12860aebc9c0f57",
  "url": "https://rest.uniprot.org/unisave/A0AA51Z0J6?format=txt&versions=10"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AA51Z0J6?format=txt&versions=10)

```json
{
  "entry_version": 10,
  "evidence_id": "H4",
  "excerpt": "CC   -!- FUNCTION: O-methyltransferase participating in the biosynthesis of\nCC       natural products derived from phenylethylamine, including mescaline, a\nCC       natural hallucinogen potentially used in psychotherapeutic treatments\nCC       (PubMed:37675639). Catalyzes the O-methylation of dopamine, 4-hydroxy-\nCC       3,5-dimethoxyphenethylamine, 4,5-dihydroxy-3-methoxyphenethylamine and\nCC       N-methyl-4,5-dihydroxy-3-methoxyphenethylamine (PubMed:37675639). Also\nCC       involved in the conversion of N-methyl-4-hydroxy-3,5-\nCC       dimethoxyphenethylamine to N-methylmescaline (PubMed:37675639).\nCC       {ECO:0000269|PubMed:37675639}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:25.490622+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 37-45",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "88903183e4675ef7b87342d80b4056576bfff1355cba383be12860aebc9c0f57",
  "url": "https://rest.uniprot.org/unisave/A0AA51Z0J6?format=txt&versions=10"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AA51Z0J6?format=txt&versions=10)

```json
{
  "entry_version": 10,
  "evidence_id": "H5",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=4-hydroxy-3,5-dimethoxyphenethylamine + S-adenosyl-L-\nCC         methionine = mescaline + S-adenosyl-L-homocysteine + H(+);\nCC         Xref=Rhea:RHEA:81059, ChEBI:CHEBI:15378, ChEBI:CHEBI:57856,\nCC         ChEBI:CHEBI:59789, ChEBI:CHEBI:231762, ChEBI:CHEBI:231768;\nCC         Evidence={ECO:0000269|PubMed:37675639};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:81060;\nCC         Evidence={ECO:0000269|PubMed:37675639};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:25.490622+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 46-53",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "88903183e4675ef7b87342d80b4056576bfff1355cba383be12860aebc9c0f57",
  "url": "https://rest.uniprot.org/unisave/A0AA51Z0J6?format=txt&versions=10"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AA51Z0J6?format=txt&versions=10)

```json
{
  "entry_version": 10,
  "evidence_id": "H6",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=dopamine + S-adenosyl-L-methionine = 4-methoxytyramine + S-\nCC         adenosyl-L-homocysteine + H(+); Xref=Rhea:RHEA:81047,\nCC         ChEBI:CHEBI:15378, ChEBI:CHEBI:57856, ChEBI:CHEBI:59789,\nCC         ChEBI:CHEBI:59905, ChEBI:CHEBI:192993;\nCC         Evidence={ECO:0000269|PubMed:37675639};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:81048;\nCC         Evidence={ECO:0000269|PubMed:37675639};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:25.490622+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 54-61",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "88903183e4675ef7b87342d80b4056576bfff1355cba383be12860aebc9c0f57",
  "url": "https://rest.uniprot.org/unisave/A0AA51Z0J6?format=txt&versions=10"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AA51Z0J6?format=txt&versions=10)

```json
{
  "entry_version": 10,
  "evidence_id": "H7",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=3,4-dihydroxy-5-methoxyphenethylamine + S-adenosyl-L-\nCC         methionine = 3-hydroxy-4,5-dimethoxyphenethylamine + S-adenosyl-L-\nCC         homocysteine + H(+); Xref=Rhea:RHEA:81051, ChEBI:CHEBI:15378,\nCC         ChEBI:CHEBI:57856, ChEBI:CHEBI:59789, ChEBI:CHEBI:231763,\nCC         ChEBI:CHEBI:231769; Evidence={ECO:0000269|PubMed:37675639};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:81052;\nCC         Evidence={ECO:0000269|PubMed:37675639};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:25.490622+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 62-69",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "88903183e4675ef7b87342d80b4056576bfff1355cba383be12860aebc9c0f57",
  "url": "https://rest.uniprot.org/unisave/A0AA51Z0J6?format=txt&versions=10"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AA51Z0J6?format=txt&versions=10)

```json
{
  "entry_version": 10,
  "evidence_id": "H8",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=N-methyl-4-hydroxy-3,5-dimethoxyphenethylamine + S-adenosyl-L-\nCC         methionine = N-methylmescaline + S-adenosyl-L-homocysteine + H(+);\nCC         Xref=Rhea:RHEA:84995, ChEBI:CHEBI:15378, ChEBI:CHEBI:57856,\nCC         ChEBI:CHEBI:59789, ChEBI:CHEBI:231777, ChEBI:CHEBI:231781;\nCC         Evidence={ECO:0000269|PubMed:37675639};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:84996;\nCC         Evidence={ECO:0000269|PubMed:37675639};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:25.490622+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 70-77",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "88903183e4675ef7b87342d80b4056576bfff1355cba383be12860aebc9c0f57",
  "url": "https://rest.uniprot.org/unisave/A0AA51Z0J6?format=txt&versions=10"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AA51Z0J6?format=txt&versions=10)

```json
{
  "entry_version": 10,
  "evidence_id": "H9",
  "excerpt": "DR   GO; GO:0008171; F:O-methyltransferase activity; IEA:InterPro.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:25.490622+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 110-110",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "88903183e4675ef7b87342d80b4056576bfff1355cba383be12860aebc9c0f57",
  "url": "https://rest.uniprot.org/unisave/A0AA51Z0J6?format=txt&versions=10"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AA51Z0J6?format=txt&versions=10)

```json
{
  "entry_version": 10,
  "evidence_id": "H10",
  "excerpt": "DR   GO; GO:0046983; F:protein dimerization activity; IEA:InterPro.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:25.490622+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 111-111",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "88903183e4675ef7b87342d80b4056576bfff1355cba383be12860aebc9c0f57",
  "url": "https://rest.uniprot.org/unisave/A0AA51Z0J6?format=txt&versions=10"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0000287\nname: magnesium ion binding\nnamespace: molecular_function\ndef: \"Binding to a magnesium (Mg) ion.\" [GOC:ai]\nsynonym: \"magnesium binding\" EXACT []\nsynonym: \"Mg binding\" EXACT []\nis_a: GO:0046872 ! metal ion binding\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0000287",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 3126-3134",
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
  "excerpt": "[Term]\nid: GO:0046873\nname: metal ion transmembrane transporter activity\nnamespace: molecular_function\ndef: \"Enables the transfer of metal ions from one side of a membrane to the other.\" [GOC:ai]\nsynonym: \"heavy metal ion porter activity\" NARROW []\nsynonym: \"heavy metal ion transporter activity\" NARROW []\nsynonym: \"heavy metal ion:hydrogen symporter activity\" NARROW []\nsynonym: \"heavy metal-exporting ATPase activity\" NARROW []\nsynonym: \"high affinity metal ion uptake transporter activity\" NARROW []\nsynonym: \"low affinity metal ion uptake transporter activity\" NARROW []\nis_a: GO:0008324 ! monoatomic cation transmembrane transporter activity\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0046873",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 281293-281305",
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
  "excerpt": "[Term]\nid: GO:0046983\nname: protein dimerization activity\nnamespace: molecular_function\ndef: \"The formation of a protein dimer, a macromolecular structure consists of two noncovalently associated identical or nonidentical subunits.\" [ISBN:0198506732]\nis_a: GO:0005515 ! protein binding\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0046983",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 282554-282560",
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
  "excerpt": "[Term]\nid: GO:0140338\nname: sphingomyelin transfer activity\nnamespace: molecular_function\nalt_id: GO:0010175\ndef: \"Removes a sphingomyelin from the outer leaflet of a donor membrane, transports it through the aqueous phase while protected in a hydrophobic pocket, and brings it to the outer leaflet of an acceptor membrane.\" [PMID:9132017]\nsynonym: \"sphingomyelin carrier activity\" EXACT []\nsynonym: \"sphingosine transmembrane transporter activity\" BROAD []\nis_a: GO:0120014 ! phospholipid transfer activity\nis_a: GO:0120016 ! sphingolipid transfer activity\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0140338",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 439529-439539",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 171. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
