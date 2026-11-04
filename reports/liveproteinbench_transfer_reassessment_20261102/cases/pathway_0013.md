# pathway_0013

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/pathway_0013.txt)

**Task:** `pathway`  
**Expected answer:** **C** — Amino-acid biosynthesis

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MSTPSKKRCGVLGATGAVGTRFILLLEQSPLLELVAVGASERSAGKKYRDAVRWKQASPMPASVADLTVRRCAPSEFSDCDIIFSGLDPVAAGDIEMAFLKANFAVFSNAKNYRLDPIVPLVVPLVNAGHIDVIPAQRKHYGLDKGLIVCNSNCAVVGLVIPAKALIQKFGPIESVSMVTMQAVSGAGYPGVSSMDIFDNIVPFIPGEEGKIATESRKILGNLNPDLAGFSDQQPLQVSVACNRVPVLDGHTVCASLRFVNRPAPTASQVRDALREYKSEVQLLGCPSAPRQAIHVLDDVDRPQPRLDRDTEAGYACSVGRIREDDSGVFDIQFVALSHNTVLGASGSSILNAESAILKGYI

[Multiple Choices]
A. (S)-3-hydroxy-3-methylglutaryl-CoA from 3-isovaleryl-CoA: step 3/3. .
B. oxylipin biosynthesis. .
C. Amino-acid biosynthesis
D. L-histidine biosynthesis
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Protein Pathway Prediction, which is to predict the primary metabolic or signaling pathway in which a given protein functions. Biological pathways are series of chemical reactions occurring within a cell that are essential for life. Based on the protein's amino acid sequence, you should identify the most relevant pathway from the given options.. The inputs provided by the user for this task include:

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

> The matched sequence is annotated as aspartate-semialdehyde dehydrogenase, with pathway annotations placing it in amino-acid biosynthesis, including methionine and threonine biosynthesis. This supports the broad option C.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with an enzyme in the aspartate-family amino-acid biosynthesis pathway: aspartate-semialdehyde dehydrogenase catalyzes a step producing a precursor used in amino-acid biosynthesis. That family-level function meaningfully favors the broad amino-acid-biosynthesis option over the offered oxylipin, isovaleryl-CoA, and histidine-pathway alternatives.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A transferable inference from the enzyme family and its pathway role distinguishes C among these choices; knowing the exact protein’s database record is not required. The sequence-based family identification is an inference rather than direct experimental evidence from the original input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supported family-level pathway is amino-acid biosynthesis; the specific histidine-biosynthesis alternative does not describe this enzyme’s aspartate-family pathway.


### Important caveats

- The reviewer-only annotations apply to an exact sequence match, but were not part of the original input.
- The pathway annotations cite experimental evidence, although the cited primary studies were not independently assessed here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with an enzyme in the aspartate-family amino-acid biosynthesis pathway: aspartate-semialdehyde dehydrogenase catalyzes a step producing a precursor used in amino-acid biosynthesis. That family-level function meaningfully favors the broad amino-acid-biosynthesis option over the offered oxylipin, isovaleryl-CoA, and histidine-pathway alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A transferable inference from the enzyme family and its pathway role distinguishes C among these choices; knowing the exact protein’s database record is not required. The sequence-based family identification is an inference rather than direct experimental evidence from the original input."
  },
  "case_id": "pathway_0013",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The matched sequence is annotated as aspartate-semialdehyde dehydrogenase, with pathway annotations placing it in amino-acid biosynthesis, including methionine and threonine biosynthesis. This supports the broad option C."
  },
  "important_caveats": [
    "The reviewer-only annotations apply to an exact sequence match, but were not part of the original input.",
    "The pathway annotations cite experimental evidence, although the cited primary studies were not independently assessed here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supported family-level pathway is amino-acid biosynthesis; the specific histidine-biosynthesis alternative does not describe this enzyme’s aspartate-family pathway."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0013",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched sequence is annotated as aspartate-semialdehyde dehydrogenase, with pathway annotations placing it in amino-acid biosynthesis, including methionine and threonine biosynthesis. This supports the broad option C.",
    "evidence_ids": ["C4", "C5", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with an enzyme in the aspartate-family amino-acid biosynthesis pathway: aspartate-semialdehyde dehydrogenase catalyzes a step producing a precursor used in amino-acid biosynthesis. That family-level function meaningfully favors the broad amino-acid-biosynthesis option over the offered oxylipin, isovaleryl-CoA, and histidine-pathway alternatives.",
    "missing_item_specific_fact": "",
    "reason": "A transferable inference from the enzyme family and its pathway role distinguishes C among these choices; knowing the exact protein’s database record is not required. The sequence-based family identification is an inference rather than direct experimental evidence from the original input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supported family-level pathway is amino-acid biosynthesis; the specific histidine-biosynthesis alternative does not describe this enzyme’s aspartate-family pathway."
  },
  "important_caveats": [
    "The reviewer-only annotations apply to an exact sequence match, but were not part of the original input.",
    "The pathway annotations cite experimental evidence, although the cited primary studies were not independently assessed here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation (evidence C4, C5, C6, H4, H5) identifies the protein as Aspartate-semialdehyde dehydrogenase (EC 1.2.1.11), annotated in 'Amino-acid biosynthesis; L-methionine biosynthesis via de novo pathway; L-homoserine from L-aspartate: step 2/3' and 'Amino-acid biosynthesis; L-threonine biosynthesis; L-threonine from L-aspartate: step 2/5', both with experimental evidence (ECO:0000269, PubMed). The expected answer C ('Amino-acid biosynthesis') is directly supported by these annotations. The other options (A: HMG-CoA pathway, B: oxylipin biosynthesis, D: L-histidine biosynthesis) are not associated with this protein.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal sequence contains the highly conserved Rossmann-fold motif 'GVLGATGAVGTRFILLLEQ' (residues ~10-30), which is a hallmark of the aspartate-semialdehyde dehydrogenase (ASADH) family. In E. coli ASADH, the corresponding region reads 'MAKQTVVGVLGATGAVGTRFILLLEQ', showing near-identical conservation of the 'GVLGATGAVGTRFILLLEQ' segment. This NADPH-binding Rossmann fold is a transferable family-level feature recognized across ASADH orthologs. ASADH catalyzes the NADPH-dependent reduction of aspartyl-phosphate to aspartate semialdehyde, a committed step in the common aspartate-family amino acid biosynthesis pathway leading to methionine, threonine, and isoleucine. This firmly places the protein in 'Amino-acid biosynthesis' (C). It excludes A (HMG-CoA/mevalonate pathway uses CoA-transferases and thiolases, not NADPH Rossmann-fold dehydrogenases of this type), B (oxylipin biosynthesis involves lipoxygenases and P450s, unrelated to this fold), and D (L-histidine biosynthesis uses entirely different enzyme classes such as ATP phosphoribosyltransferase and imidazoleglycerol-phosphate dehydratase, none of which share this N-terminal Rossmann-fold signature or catalytic mechanism).


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The conserved N-terminal 'GVLGATGAVGTRFILLLEQ' motif is a well-known ASADH family signature found across bacterial and fungal orthologs. A model trained on protein families can recognize this as an NADPH-dependent dehydrogenase of the ASADH class, whose established role in aspartate-family amino acid biosynthesis (Met/Thr/Ile) is standard biochemistry. This family-level inference meaningfully distinguishes C from all other offered choices without requiring the exact UniProt entry for this specific fungal protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> C ('Amino-acid biosynthesis') is the correct broad pathway. D ('L-histidine biosynthesis') is a specific amino-acid pathway but ASADH is not part of it. A and B are unrelated metabolic pathways. No ambiguity exists among the offered choices.


### Important caveats

- The UniProt annotation for this protein is from a fungal organism (Blastomyces gilchristii), but the ASADH family and its pathway assignment are well-conserved across all domains of life.
- The pathway annotation carries experimental evidence codes (ECO:0000269 from PubMed:30107909 and PubMed:29608391), not purely computational inference.
- The N-terminal motif match to E. coli ASADH is based on well-known sequence conservation in the ASADH family; the specific fungal ortholog may have minor insertions (e.g., 'MSTPSKKRC' vs 'MAKQTVV') but the core Rossmann-fold motif is preserved.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal sequence contains the highly conserved Rossmann-fold motif 'GVLGATGAVGTRFILLLEQ' (residues ~10-30), which is a hallmark of the aspartate-semialdehyde dehydrogenase (ASADH) family. In E. coli ASADH, the corresponding region reads 'MAKQTVVGVLGATGAVGTRFILLLEQ', showing near-identical conservation of the 'GVLGATGAVGTRFILLLEQ' segment. This NADPH-binding Rossmann fold is a transferable family-level feature recognized across ASADH orthologs. ASADH catalyzes the NADPH-dependent reduction of aspartyl-phosphate to aspartate semialdehyde, a committed step in the common aspartate-family amino acid biosynthesis pathway leading to methionine, threonine, and isoleucine. This firmly places the protein in 'Amino-acid biosynthesis' (C). It excludes A (HMG-CoA/mevalonate pathway uses CoA-transferases and thiolases, not NADPH Rossmann-fold dehydrogenases of this type), B (oxylipin biosynthesis involves lipoxygenases and P450s, unrelated to this fold), and D (L-histidine biosynthesis uses entirely different enzyme classes such as ATP phosphoribosyltransferase and imidazoleglycerol-phosphate dehydratase, none of which share this N-terminal Rossmann-fold signature or catalytic mechanism).",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The conserved N-terminal 'GVLGATGAVGTRFILLLEQ' motif is a well-known ASADH family signature found across bacterial and fungal orthologs. A model trained on protein families can recognize this as an NADPH-dependent dehydrogenase of the ASADH class, whose established role in aspartate-family amino acid biosynthesis (Met/Thr/Ile) is standard biochemistry. This family-level inference meaningfully distinguishes C from all other offered choices without requiring the exact UniProt entry for this specific fungal protein."
  },
  "case_id": "pathway_0013",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation (evidence C4, C5, C6, H4, H5) identifies the protein as Aspartate-semialdehyde dehydrogenase (EC 1.2.1.11), annotated in 'Amino-acid biosynthesis; L-methionine biosynthesis via de novo pathway; L-homoserine from L-aspartate: step 2/3' and 'Amino-acid biosynthesis; L-threonine biosynthesis; L-threonine from L-aspartate: step 2/5', both with experimental evidence (ECO:0000269, PubMed). The expected answer C ('Amino-acid biosynthesis') is directly supported by these annotations. The other options (A: HMG-CoA pathway, B: oxylipin biosynthesis, D: L-histidine biosynthesis) are not associated with this protein."
  },
  "important_caveats": [
    "The UniProt annotation for this protein is from a fungal organism (Blastomyces gilchristii), but the ASADH family and its pathway assignment are well-conserved across all domains of life.",
    "The pathway annotation carries experimental evidence codes (ECO:0000269 from PubMed:30107909 and PubMed:29608391), not purely computational inference.",
    "The N-terminal motif match to E. coli ASADH is based on well-known sequence conservation in the ASADH family; the specific fungal ortholog may have minor insertions (e.g., 'MSTPSKKRC' vs 'MAKQTVV') but the core Rossmann-fold motif is preserved."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "C ('Amino-acid biosynthesis') is the correct broad pathway. D ('L-histidine biosynthesis') is a specific amino-acid pathway but ASADH is not part of it. A and B are unrelated metabolic pathways. No ambiguity exists among the offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0013",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation (evidence C4, C5, C6, H4, H5) identifies the protein as Aspartate-semialdehyde dehydrogenase (EC 1.2.1.11), annotated in 'Amino-acid biosynthesis; L-methionine biosynthesis via de novo pathway; L-homoserine from L-aspartate: step 2/3' and 'Amino-acid biosynthesis; L-threonine biosynthesis; L-threonine from L-aspartate: step 2/5', both with experimental evidence (ECO:0000269, PubMed). The expected answer C ('Amino-acid biosynthesis') is directly supported by these annotations. The other options (A: HMG-CoA pathway, B: oxylipin biosynthesis, D: L-histidine biosynthesis) are not associated with this protein.",
    "evidence_ids": ["C4", "C5", "C6", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal sequence contains the highly conserved Rossmann-fold motif 'GVLGATGAVGTRFILLLEQ' (residues ~10-30), which is a hallmark of the aspartate-semialdehyde dehydrogenase (ASADH) family. In E. coli ASADH, the corresponding region reads 'MAKQTVVGVLGATGAVGTRFILLLEQ', showing near-identical conservation of the 'GVLGATGAVGTRFILLLEQ' segment. This NADPH-binding Rossmann fold is a transferable family-level feature recognized across ASADH orthologs. ASADH catalyzes the NADPH-dependent reduction of aspartyl-phosphate to aspartate semialdehyde, a committed step in the common aspartate-family amino acid biosynthesis pathway leading to methionine, threonine, and isoleucine. This firmly places the protein in 'Amino-acid biosynthesis' (C). It excludes A (HMG-CoA/mevalonate pathway uses CoA-transferases and thiolases, not NADPH Rossmann-fold dehydrogenases of this type), B (oxylipin biosynthesis involves lipoxygenases and P450s, unrelated to this fold), and D (L-histidine biosynthesis uses entirely different enzyme classes such as ATP phosphoribosyltransferase and imidazoleglycerol-phosphate dehydratase, none of which share this N-terminal Rossmann-fold signature or catalytic mechanism).",
    "missing_item_specific_fact": "",
    "reason": "The conserved N-terminal 'GVLGATGAVGTRFILLLEQ' motif is a well-known ASADH family signature found across bacterial and fungal orthologs. A model trained on protein families can recognize this as an NADPH-dependent dehydrogenase of the ASADH class, whose established role in aspartate-family amino acid biosynthesis (Met/Thr/Ile) is standard biochemistry. This family-level inference meaningfully distinguishes C from all other offered choices without requiring the exact UniProt entry for this specific fungal protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "C ('Amino-acid biosynthesis') is the correct broad pathway. D ('L-histidine biosynthesis') is a specific amino-acid pathway but ASADH is not part of it. A and B are unrelated metabolic pathways. No ambiguity exists among the offered choices."
  },
  "important_caveats": [
    "The UniProt annotation for this protein is from a fungal organism (Blastomyces gilchristii), but the ASADH family and its pathway assignment are well-conserved across all domains of life.",
    "The pathway annotation carries experimental evidence codes (ECO:0000269 from PubMed:30107909 and PubMed:29608391), not purely computational inference.",
    "The N-terminal motif match to E. coli ASADH is based on well-known sequence conservation in the ASADH family; the specific fungal ortholog may have minor insertions (e.g., 'MSTPSKKRC' vs 'MAKQTVV') but the core Rossmann-fold motif is preserved."
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
  "benchmark_sequence_length": 362,
  "benchmark_sequence_sha256": "f30799121529a0913069a9614b7c0737990588a5013bf3d73955823ac077cf36",
  "current_entry_audit": {
    "entryVersion": 28,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-02-05",
    "sequenceVersion": 2
  },
  "current_record_sha256": "bfbfb6c511568b902ff86e7618d016f76423131a7103b823ff729117ec12dafa",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 362,
  "current_source_sequence_sha256": "f30799121529a0913069a9614b7c0737990588a5013bf3d73955823ac077cf36",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 26,
      "exact_sequence_comparison": "matched",
      "sequence_version": 2
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A179UL48",
  "selected_historical_entry_version": 26,
  "selected_historical_record_sha256": "4f875f72a66f602258c8fcfbbffa13b408826e3f67e6f950e3069cb2c5b75a5d",
  "selected_historical_source_sequence_length": 362,
  "selected_historical_source_sequence_sha256": "f30799121529a0913069a9614b7c0737990588a5013bf3d73955823ac077cf36",
  "selected_historical_version": {
    "accession": "A0A179UL48",
    "database": "Swiss-Prot",
    "entryVersion": 26,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "DHAS_BLAGS",
    "sequenceVersion": 2
  }
}
```

**Qualifications:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A179UL48.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A179UL48\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:24:30.243142+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bfbfb6c511568b902ff86e7618d016f76423131a7103b823ff729117ec12dafa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A179UL48.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A179UL48.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":28,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-02-05\",\"sequenceVersion\":2}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:24:30.243142+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bfbfb6c511568b902ff86e7618d016f76423131a7103b823ff729117ec12dafa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A179UL48.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A179UL48.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Blastomyces dermatitidis\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000002038\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Eurotiomycetes\",\"Eurotiomycetidae\",\"Onygenales\",\"Ajellomycetaceae\",\"Blastomyces\"],\"scientificName\":\"Blastomyces gilchristii (strain SLH14081)\",\"taxonId\":559298}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:24:30.243142+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bfbfb6c511568b902ff86e7618d016f76423131a7103b823ff729117ec12dafa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A179UL48.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A179UL48.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"29608391\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"30107909\",\"source\":\"PubMed\"}],\"value\":\"1.2.1.11\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Aspartate-semialdehyde dehydrogenase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:24:30.243142+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bfbfb6c511568b902ff86e7618d016f76423131a7103b823ff729117ec12dafa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A179UL48.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A179UL48.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"30107909\",\"source\":\"PubMed\"}],\"value\":\"Amino-acid biosynthesis; L-methionine biosynthesis via de novo pathway; L-homoserine from L-aspartate: step 2/3\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/4",
  "retrieved_utc": "2026-11-02T04:24:30.243142+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bfbfb6c511568b902ff86e7618d016f76423131a7103b823ff729117ec12dafa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A179UL48.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A179UL48.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"30107909\",\"source\":\"PubMed\"}],\"value\":\"Amino-acid biosynthesis; L-threonine biosynthesis; L-threonine from L-aspartate: step 2/5\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/5",
  "retrieved_utc": "2026-11-02T04:24:30.243142+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bfbfb6c511568b902ff86e7618d016f76423131a7103b823ff729117ec12dafa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A179UL48.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A179UL48.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Dahal G.P.\",\"Viola R.E.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"29608391\"},{\"database\":\"DOI\",\"id\":\"10.1177/2472555218767844\"}],\"citationType\":\"journal article\",\"firstPage\":\"520\",\"id\":\"29608391\",\"journal\":\"SLAS Discovery\",\"lastPage\":\"531\",\"publicationDate\":\"2018\",\"title\":\"A Fragment Library Screening Approach to Identify Selective Inhibitors against an Essential Fungal Enzyme.\",\"volume\":\"23\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"ACTIVITY REGULATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:24:30.243142+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bfbfb6c511568b902ff86e7618d016f76423131a7103b823ff729117ec12dafa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A179UL48.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A179UL48.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Dahal G.P.\",\"Viola R.E.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"30107909\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.bbrc.2018.08.053\"}],\"citationType\":\"journal article\",\"firstPage\":\"2848\",\"id\":\"30107909\",\"journal\":\"Biochem. Biophys. Res. Commun.\",\"lastPage\":\"2854\",\"publicationDate\":\"2018\",\"title\":\"Structural insights into inhibitor binding to a fungal ortholog of aspartate semialdehyde dehydrogenase.\",\"volume\":\"503\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6C85\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6C8W\",\"source\":\"PDB\"}],\"referenceNumber\":3,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (2.4 ANGSTROMS) IN COMPLEX WITH INHIBITOR AND NADP(+)\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"ACTIVITY REGULATION\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"PATHWAY\",\"SUBUNIT\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-02T04:24:30.243142+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bfbfb6c511568b902ff86e7618d016f76423131a7103b823ff729117ec12dafa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A179UL48.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26)

```json
{
  "entry_version": 26,
  "evidence_id": "H1",
  "excerpt": "ID   DHAS_BLAGS              Reviewed;         362 AA.\nAC   A0A179UL48;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-FEB-2025, sequence version 2.\nDT   28-JAN-2026, entry version 26.\nDE   RecName: Full=Aspartate-semialdehyde dehydrogenase {ECO:0000305};\nDE            EC=1.2.1.11 {ECO:0000269|PubMed:29608391, ECO:0000269|PubMed:30107909};\nGN   ORFNames=BDBG_16922 {ECO:0000312|EMBL:OAT07949.1};\nOS   Blastomyces gilchristii (strain SLH14081) (Blastomyces dermatitidis).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;\nOC   Eurotiomycetidae; Onygenales; Ajellomycetaceae; Blastomyces.\nOX   NCBI_TaxID=559298 {ECO:0000312|Proteomes:UP000002038};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:32.458235+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-12",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4f875f72a66f602258c8fcfbbffa13b408826e3f67e6f950e3069cb2c5b75a5d",
  "url": "https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26)

```json
{
  "entry_version": 26,
  "evidence_id": "H2",
  "excerpt": "RN   [2] {ECO:0000305}\nRP   FUNCTION, CATALYTIC ACTIVITY, AND ACTIVITY REGULATION.\nRX   PubMed=29608391; DOI=10.1177/2472555218767844;\nRA   Dahal G.P., Viola R.E.;\nRT   \"A Fragment Library Screening Approach to Identify Selective Inhibitors\nRT   against an Essential Fungal Enzyme.\";\nRL   SLAS Discovery 23:520-531(2018).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:32.458235+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 25-31",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4f875f72a66f602258c8fcfbbffa13b408826e3f67e6f950e3069cb2c5b75a5d",
  "url": "https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26)

```json
{
  "entry_version": 26,
  "evidence_id": "H3",
  "excerpt": "RN   [3] {ECO:0007744|PDB:6C85, ECO:0007744|PDB:6C8W}\nRP   X-RAY CRYSTALLOGRAPHY (2.4 ANGSTROMS) IN COMPLEX WITH INHIBITOR AND\nRP   NADP(+), FUNCTION, CATALYTIC ACTIVITY, ACTIVITY REGULATION,\nRP   BIOPHYSICOCHEMICAL PROPERTIES, PATHWAY, AND SUBUNIT.\nRX   PubMed=30107909; DOI=10.1016/j.bbrc.2018.08.053;\nRA   Dahal G.P., Viola R.E.;\nRT   \"Structural insights into inhibitor binding to a fungal ortholog of\nRT   aspartate semialdehyde dehydrogenase.\";\nRL   Biochem. Biophys. Res. Commun. 503:2848-2854(2018).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:32.458235+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 32-40",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4f875f72a66f602258c8fcfbbffa13b408826e3f67e6f950e3069cb2c5b75a5d",
  "url": "https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26)

```json
{
  "entry_version": 26,
  "evidence_id": "H4",
  "excerpt": "CC   -!- PATHWAY: Amino-acid biosynthesis; L-methionine biosynthesis via de novo\nCC       pathway; L-homoserine from L-aspartate: step 2/3.\nCC       {ECO:0000269|PubMed:30107909}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:32.458235+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 64-66",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4f875f72a66f602258c8fcfbbffa13b408826e3f67e6f950e3069cb2c5b75a5d",
  "url": "https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26)

```json
{
  "entry_version": 26,
  "evidence_id": "H5",
  "excerpt": "CC   -!- PATHWAY: Amino-acid biosynthesis; L-threonine biosynthesis; L-threonine\nCC       from L-aspartate: step 2/5. {ECO:0000269|PubMed:30107909}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:32.458235+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 67-68",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4f875f72a66f602258c8fcfbbffa13b408826e3f67e6f950e3069cb2c5b75a5d",
  "url": "https://rest.uniprot.org/unisave/A0A179UL48?format=txt&versions=26"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 13. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
