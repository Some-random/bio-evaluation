# catalytic_activity_0014

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/catalytic_activity_0014.txt)

**Task:** `catalytic_activity`  
**Expected answer:** **A** — a phosphate monoester + H2O = an alcohol + phosphate

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MYTLLDILKGLPLLAVAAIASADYPTIPSDLTTPVQQRLAISGMNSVSVGWNTYEKLLKPCVQYGTSSTDLSQETCSLISTTYNTSRTWSNTVILTDLTPATTYYYQIVSTNSTVNSFFSPRTPGDKSPFTTSVVIDLGVYGADGFTVDADGDPTRKVLIPEVEPALNHTTIGRLADTWDDYEWVLHPGDFGYADDWYLTPTNVGDGVNAYEAILENFYDQLAPIAGGKVYMASPGNHEADCEELGTPAIELSCPEGQKNFTDFNVRFGKNMPTSFSSTSSNTKAKVNANKAAALANPPFWYSFEYGMVHVTMIDTETDFPNAPDAPFGTAGLDGGPFGYTGQQLDFFEADLASVDRTVTPWLLVAGHRPWYSTGGQSNICSACKTAFEPLMYQYGVDLGVFGHVHNSQRFAPVNNSVVDPAGMDNPTAPMYIIAGGAGNIEGLSSVGNNISSNRFAYAETFSYATLTFEDENNLSIQFIESATGDILDSSTLYKAHTEQFVNQ

[Multiple Choices]
A. a phosphate monoester + H2O = an alcohol + phosphate
B. roxarsone (III) + AH2 + O2 = 4-hydroxy-3-nitrocyclohexa-2,5-dien-1-one + arsenite + A + H(+)
C. guanosine(in) = guanosine(out)
D. L-aspartate + ATP = 4-phospho-L-aspartate + ADP
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

> The sequence-matched UniProt annotation identifies acid phosphatase A with EC 3.1.3.2 and gives the reaction in choice A. The reaction annotation is supported by similarity transfer, so this supports the key but does not by itself establish a direct assay of this exact protein's catalytic activity.

Citations as saved: [H4](#evidence-h4), [C4](#evidence-c4), [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminus has a clear hydrophobic signal-peptide-like stretch, and the remainder is a long, enzyme-like sequence with many potential glycosylation sites, consistent with a secreted protein. Transferable knowledge makes an extracellular hydrolytic enzyme, including a phosphatase releasing phosphate from a phosphate monoester, a more plausible choice than an intracellular ATP-dependent aspartate kinase (D), a guanosine transport reaction (C), or the highly specific roxarsone redox reaction (B).


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> These sequence features provide a probabilistic distinction among the unusually disparate choices, though they do not independently identify the exact phosphatase or prove its substrate range. The argument relies on general secretion and enzyme-function patterns, not on recalling this protein's record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No alternative is comparably supported by the sequence-level clues and offered reactions.


### Important caveats

- The cited catalytic-reaction annotation is transferred by similarity; the supplied evidence does not establish direct experimental confirmation of this reaction for the exact sequence.
- The signal peptide and glycosylation-like sequence features are suggestive, not diagnostic of phosphatase activity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminus has a clear hydrophobic signal-peptide-like stretch, and the remainder is a long, enzyme-like sequence with many potential glycosylation sites, consistent with a secreted protein. Transferable knowledge makes an extracellular hydrolytic enzyme, including a phosphatase releasing phosphate from a phosphate monoester, a more plausible choice than an intracellular ATP-dependent aspartate kinase (D), a guanosine transport reaction (C), or the highly specific roxarsone redox reaction (B).",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "These sequence features provide a probabilistic distinction among the unusually disparate choices, though they do not independently identify the exact phosphatase or prove its substrate range. The argument relies on general secretion and enzyme-function patterns, not on recalling this protein's record."
  },
  "case_id": "catalytic_activity_0014",
  "expected_answer_check": {
    "evidence_ids": [
      "H4",
      "C4",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies acid phosphatase A with EC 3.1.3.2 and gives the reaction in choice A. The reaction annotation is supported by similarity transfer, so this supports the key but does not by itself establish a direct assay of this exact protein's catalytic activity."
  },
  "important_caveats": [
    "The cited catalytic-reaction annotation is transferred by similarity; the supplied evidence does not establish direct experimental confirmation of this reaction for the exact sequence.",
    "The signal peptide and glycosylation-like sequence features are suggestive, not diagnostic of phosphatase activity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No alternative is comparably supported by the sequence-level clues and offered reactions."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0014",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies acid phosphatase A with EC 3.1.3.2 and gives the reaction in choice A. The reaction annotation is supported by similarity transfer, so this supports the key but does not by itself establish a direct assay of this exact protein's catalytic activity.",
    "evidence_ids": ["H4", "C4", "C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminus has a clear hydrophobic signal-peptide-like stretch, and the remainder is a long, enzyme-like sequence with many potential glycosylation sites, consistent with a secreted protein. Transferable knowledge makes an extracellular hydrolytic enzyme, including a phosphatase releasing phosphate from a phosphate monoester, a more plausible choice than an intracellular ATP-dependent aspartate kinase (D), a guanosine transport reaction (C), or the highly specific roxarsone redox reaction (B).",
    "missing_item_specific_fact": "",
    "reason": "These sequence features provide a probabilistic distinction among the unusually disparate choices, though they do not independently identify the exact phosphatase or prove its substrate range. The argument relies on general secretion and enzyme-function patterns, not on recalling this protein's record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No alternative is comparably supported by the sequence-level clues and offered reactions."
  },
  "important_caveats": [
    "The cited catalytic-reaction annotation is transferred by similarity; the supplied evidence does not establish direct experimental confirmation of this reaction for the exact sequence.",
    "The signal peptide and glycosylation-like sequence features are suggestive, not diagnostic of phosphatase activity."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A9P5CTI1 is annotated as 'Acid phosphatase A' with EC 3.1.3.2, and the catalytic activity is explicitly stated as 'a phosphate monoester + H2O = an alcohol + phosphate' (matching choice A). The EC number assignment carries experimental evidence (ECO:0000269, PubMed 39159278), while the specific reaction annotation is by similarity to P83380 (ECO:0000250). The supplied sequence matches the UniProt entry (504 aa, SHA-256 match). The expected answer is directly supported by the database annotation.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains several transferable acid-phosphatase family signatures. (1) An N-terminal signal peptide (MYTLLDILKGLPLLAVAAIASADY) indicates a secreted protein, consistent with the many secreted fungal acid phosphatases. (2) The 'HPG' tripeptide motif appears in 'VLHPGDFGYADDW' (~position 200); HPG is a well-known active-site motif in the acid phosphatase (AP) superfamily, shared across many characterized acid phosphatases. (3) 'DT' motifs appear in 'TDLTP' and 'MIDTET', another conserved feature of acid phosphatases. These motifs collectively point to a phosphatase. Against the alternatives: (C) a guanosine transporter would require multiple transmembrane helices, which are absent; (D) aspartate kinase (EC 2.7.2.4) would show Walker-A/B ATP-binding motifs and a kinase fold, neither present; (B) roxarsone degradation is an extremely rare arsenic/nitro compound metabolism with no recognizable sequence signature for a general model. The combination of HPG + DT + signal peptide + absence of transporter/kinase features provides a credible, transferable inference favoring choice A.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can recognize the HPG and DT motifs as acid-phosphatase signatures from family-level knowledge of other characterized acid phosphatases, note the secretory signal peptide, and eliminate the transporter (C) and kinase (D) options by the absence of their defining structural motifs. Option B (roxarsone metabolism) is an extremely obscure reaction with no generalizable sequence signature. The inference is probabilistic but meaningfully distinguishes A from the other three choices.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices represent very different enzyme classes (phosphatase, arsenic-metabolizing nitroreductase, nucleoside transporter, aspartate kinase). The sequence features (HPG, DT, signal peptide, no TM helices, no kinase motifs) point clearly to the phosphatase option and against the others. No ambiguity among the offered choices.


### Important caveats

- The EC 3.1.3.2 assignment has experimental evidence (PubMed 39159278), but the specific catalytic-reaction annotation is by similarity (ECO:0000250 to P83380), not a direct kinetic measurement on this protein.
- The HPG and DT motifs are family-level signatures; they indicate membership in the acid phosphatase superfamily but do not by themselves prove the exact EC number or rule out every possible phosphatase sub-class. However, among the four offered choices, only A corresponds to a phosphatase reaction.
- The reviewer-only evidence (accession, organism, annotation) was not available to the evaluated model; the reasoning above relies solely on the supplied sequence and transferable family knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains several transferable acid-phosphatase family signatures. (1) An N-terminal signal peptide (MYTLLDILKGLPLLAVAAIASADY) indicates a secreted protein, consistent with the many secreted fungal acid phosphatases. (2) The 'HPG' tripeptide motif appears in 'VLHPGDFGYADDW' (~position 200); HPG is a well-known active-site motif in the acid phosphatase (AP) superfamily, shared across many characterized acid phosphatases. (3) 'DT' motifs appear in 'TDLTP' and 'MIDTET', another conserved feature of acid phosphatases. These motifs collectively point to a phosphatase. Against the alternatives: (C) a guanosine transporter would require multiple transmembrane helices, which are absent; (D) aspartate kinase (EC 2.7.2.4) would show Walker-A/B ATP-binding motifs and a kinase fold, neither present; (B) roxarsone degradation is an extremely rare arsenic/nitro compound metabolism with no recognizable sequence signature for a general model. The combination of HPG + DT + signal peptide + absence of transporter/kinase features provides a credible, transferable inference favoring choice A.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the HPG and DT motifs as acid-phosphatase signatures from family-level knowledge of other characterized acid phosphatases, note the secretory signal peptide, and eliminate the transporter (C) and kinase (D) options by the absence of their defining structural motifs. Option B (roxarsone metabolism) is an extremely obscure reaction with no generalizable sequence signature. The inference is probabilistic but meaningfully distinguishes A from the other three choices."
  },
  "case_id": "catalytic_activity_0014",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A9P5CTI1 is annotated as 'Acid phosphatase A' with EC 3.1.3.2, and the catalytic activity is explicitly stated as 'a phosphate monoester + H2O = an alcohol + phosphate' (matching choice A). The EC number assignment carries experimental evidence (ECO:0000269, PubMed 39159278), while the specific reaction annotation is by similarity to P83380 (ECO:0000250). The supplied sequence matches the UniProt entry (504 aa, SHA-256 match). The expected answer is directly supported by the database annotation."
  },
  "important_caveats": [
    "The EC 3.1.3.2 assignment has experimental evidence (PubMed 39159278), but the specific catalytic-reaction annotation is by similarity (ECO:0000250 to P83380), not a direct kinetic measurement on this protein.",
    "The HPG and DT motifs are family-level signatures; they indicate membership in the acid phosphatase superfamily but do not by themselves prove the exact EC number or rule out every possible phosphatase sub-class. However, among the four offered choices, only A corresponds to a phosphatase reaction.",
    "The reviewer-only evidence (accession, organism, annotation) was not available to the evaluated model; the reasoning above relies solely on the supplied sequence and transferable family knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent very different enzyme classes (phosphatase, arsenic-metabolizing nitroreductase, nucleoside transporter, aspartate kinase). The sequence features (HPG, DT, signal peptide, no TM helices, no kinase motifs) point clearly to the phosphatase option and against the others. No ambiguity among the offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0014",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A9P5CTI1 is annotated as 'Acid phosphatase A' with EC 3.1.3.2, and the catalytic activity is explicitly stated as 'a phosphate monoester + H2O = an alcohol + phosphate' (matching choice A). The EC number assignment carries experimental evidence (ECO:0000269, PubMed 39159278), while the specific reaction annotation is by similarity to P83380 (ECO:0000250). The supplied sequence matches the UniProt entry (504 aa, SHA-256 match). The expected answer is directly supported by the database annotation.",
    "evidence_ids": ["C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains several transferable acid-phosphatase family signatures. (1) An N-terminal signal peptide (MYTLLDILKGLPLLAVAAIASADY) indicates a secreted protein, consistent with the many secreted fungal acid phosphatases. (2) The 'HPG' tripeptide motif appears in 'VLHPGDFGYADDW' (~position 200); HPG is a well-known active-site motif in the acid phosphatase (AP) superfamily, shared across many characterized acid phosphatases. (3) 'DT' motifs appear in 'TDLTP' and 'MIDTET', another conserved feature of acid phosphatases. These motifs collectively point to a phosphatase. Against the alternatives: (C) a guanosine transporter would require multiple transmembrane helices, which are absent; (D) aspartate kinase (EC 2.7.2.4) would show Walker-A/B ATP-binding motifs and a kinase fold, neither present; (B) roxarsone degradation is an extremely rare arsenic/nitro compound metabolism with no recognizable sequence signature for a general model. The combination of HPG + DT + signal peptide + absence of transporter/kinase features provides a credible, transferable inference favoring choice A.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the HPG and DT motifs as acid-phosphatase signatures from family-level knowledge of other characterized acid phosphatases, note the secretory signal peptide, and eliminate the transporter (C) and kinase (D) options by the absence of their defining structural motifs. Option B (roxarsone metabolism) is an extremely obscure reaction with no generalizable sequence signature. The inference is probabilistic but meaningfully distinguishes A from the other three choices."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent very different enzyme classes (phosphatase, arsenic-metabolizing nitroreductase, nucleoside transporter, aspartate kinase). The sequence features (HPG, DT, signal peptide, no TM helices, no kinase motifs) point clearly to the phosphatase option and against the others. No ambiguity among the offered choices."
  },
  "important_caveats": [
    "The EC 3.1.3.2 assignment has experimental evidence (PubMed 39159278), but the specific catalytic-reaction annotation is by similarity (ECO:0000250 to P83380), not a direct kinetic measurement on this protein.",
    "The HPG and DT motifs are family-level signatures; they indicate membership in the acid phosphatase superfamily but do not by themselves prove the exact EC number or rule out every possible phosphatase sub-class. However, among the four offered choices, only A corresponds to a phosphatase reaction.",
    "The reviewer-only evidence (accession, organism, annotation) was not available to the evaluated model; the reasoning above relies solely on the supplied sequence and transferable family knowledge."
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
  "benchmark_sequence_length": 504,
  "benchmark_sequence_sha256": "dcda6da0c7d50473b9560bf4d1978a67b54735105a6b2467d06a1090413f472b",
  "current_entry_audit": {
    "entryVersion": 10,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2023-09-13",
    "sequenceVersion": 1
  },
  "current_record_sha256": "1be111585efed83255b10cbc6cda847b1b52b83b0994b143d9f8fb2f69bbc018",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 504,
  "current_source_sequence_sha256": "dcda6da0c7d50473b9560bf4d1978a67b54735105a6b2467d06a1090413f472b",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 8,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A9P5CTI1",
  "selected_historical_entry_version": 8,
  "selected_historical_record_sha256": "91c728249343ee0d31ffdd7c84ed5f85a5866e543ea7cf6700c997db73ea6b0e",
  "selected_historical_source_sequence_length": 504,
  "selected_historical_source_sequence_sha256": "dcda6da0c7d50473b9560bf4d1978a67b54735105a6b2467d06a1090413f472b",
  "selected_historical_version": {
    "accession": "A0A9P5CTI1",
    "database": "Swiss-Prot",
    "entryVersion": 8,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "APHA_CRYP1",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9P5CTI1.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A9P5CTI1\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:26:19.276567+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1be111585efed83255b10cbc6cda847b1b52b83b0994b143d9f8fb2f69bbc018",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9P5CTI1.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9P5CTI1.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":10,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2023-09-13\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:26:19.276567+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1be111585efed83255b10cbc6cda847b1b52b83b0994b143d9f8fb2f69bbc018",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9P5CTI1.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9P5CTI1.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Sordariomycetes\",\"Sordariomycetidae\",\"Diaporthales\",\"Cryphonectriaceae\",\"Cryphonectria-Endothia species complex\",\"Cryphonectria\"],\"scientificName\":\"Cryphonectria parasitica (strain ATCC 38755 / EP155)\",\"taxonId\":660469}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:26:19.276567+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1be111585efed83255b10cbc6cda847b1b52b83b0994b143d9f8fb2f69bbc018",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9P5CTI1.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9P5CTI1.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39159278\",\"source\":\"PubMed\"}],\"value\":\"3.1.3.2\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39159278\",\"source\":\"PubMed\"}],\"value\":\"Acid phosphatase A\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:26:19.276567+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1be111585efed83255b10cbc6cda847b1b52b83b0994b143d9f8fb2f69bbc018",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9P5CTI1.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9P5CTI1.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"3.1.3.2\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P83380\",\"source\":\"UniProtKB\"}],\"name\":\"a phosphate monoester + H2O = an alcohol + phosphate\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:15017\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:30879\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:43474\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:67140\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:26:19.276567+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1be111585efed83255b10cbc6cda847b1b52b83b0994b143d9f8fb2f69bbc018",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9P5CTI1.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9P5CTI1.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Zhao L.\",\"Wei X.\",\"Chen F.\",\"Yuan L.\",\"Chen B.\",\"Li R.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39159278\"},{\"database\":\"DOI\",\"id\":\"10.1371/journal.ppat.1012476\"}],\"citationType\":\"journal article\",\"firstPage\":\"e1012476\",\"id\":\"39159278\",\"journal\":\"PLoS Pathog.\",\"lastPage\":\"e1012476\",\"publicationDate\":\"2024\",\"title\":\"N6-methyladenosine RNA methyltransferase CpMTA1 mediates CpAphA mRNA stability through a YTHDF1-dependent m6A modification in the chestnut blight fungus.\",\"volume\":\"20\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"DISRUPTION PHENOTYPE\",\"INDUCTION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:26:19.276567+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1be111585efed83255b10cbc6cda847b1b52b83b0994b143d9f8fb2f69bbc018",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9P5CTI1.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9P5CTI1?format=txt&versions=8)

```json
{
  "entry_version": 8,
  "evidence_id": "H1",
  "excerpt": "ID   APHA_CRYP1              Reviewed;         504 AA.\nAC   A0A9P5CTI1;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   13-SEP-2023, sequence version 1.\nDT   28-JAN-2026, entry version 8.\nDE   RecName: Full=Acid phosphatase A {ECO:0000303|PubMed:39159278};\nDE            EC=3.1.3.2 {ECO:0000269|PubMed:39159278};\nDE   Flags: Precursor;\nGN   Name=APHA {ECO:0000303|PubMed:39159278}; ORFNames=M406DRAFT_348724;\nOS   Cryphonectria parasitica (strain ATCC 38755 / EP155).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;\nOC   Sordariomycetidae; Diaporthales; Cryphonectriaceae;\nOC   Cryphonectria-Endothia species complex; Cryphonectria.\nOX   NCBI_TaxID=660469;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:21.617735+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "91c728249343ee0d31ffdd7c84ed5f85a5866e543ea7cf6700c997db73ea6b0e",
  "url": "https://rest.uniprot.org/unisave/A0A9P5CTI1?format=txt&versions=8"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9P5CTI1?format=txt&versions=8)

```json
{
  "entry_version": 8,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Acid phosphatase A {ECO:0000303|PubMed:39159278};\nDE            EC=3.1.3.2 {ECO:0000269|PubMed:39159278};\nDE   Flags: Precursor;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:21.617735+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-8",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "91c728249343ee0d31ffdd7c84ed5f85a5866e543ea7cf6700c997db73ea6b0e",
  "url": "https://rest.uniprot.org/unisave/A0A9P5CTI1?format=txt&versions=8"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9P5CTI1?format=txt&versions=8)

```json
{
  "entry_version": 8,
  "evidence_id": "H3",
  "excerpt": "RN   [2]\nRP   FUNCTION, DISRUPTION PHENOTYPE, AND INDUCTION.\nRX   PubMed=39159278; DOI=10.1371/journal.ppat.1012476;\nRA   Zhao L., Wei X., Chen F., Yuan L., Chen B., Li R.;\nRT   \"N6-methyladenosine RNA methyltransferase CpMTA1 mediates CpAphA mRNA\nRT   stability through a YTHDF1-dependent m6A modification in the chestnut\nRT   blight fungus.\";\nRL   PLoS Pathog. 20:e1012476-e1012476(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:21.617735+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 26-33",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "91c728249343ee0d31ffdd7c84ed5f85a5866e543ea7cf6700c997db73ea6b0e",
  "url": "https://rest.uniprot.org/unisave/A0A9P5CTI1?format=txt&versions=8"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9P5CTI1?format=txt&versions=8)

```json
{
  "entry_version": 8,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=a phosphate monoester + H2O = an alcohol + phosphate;\nCC         Xref=Rhea:RHEA:15017, ChEBI:CHEBI:15377, ChEBI:CHEBI:30879,\nCC         ChEBI:CHEBI:43474, ChEBI:CHEBI:67140; EC=3.1.3.2;\nCC         Evidence={ECO:0000250|UniProtKB:P83380};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:21.617735+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 37-41",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "91c728249343ee0d31ffdd7c84ed5f85a5866e543ea7cf6700c997db73ea6b0e",
  "url": "https://rest.uniprot.org/unisave/A0A9P5CTI1?format=txt&versions=8"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 14. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
