# pathway_0062

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/pathway_0062.txt)

**Task:** `pathway`  
**Expected answer:** **D** — Capsule biogenesis

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MNQFNKVCVIGLGYIGLPTAAIFASRKIKVIGVDINQNIVDIINKGKIHIVEPGLDILVHMVVNDGYLKATTLPEEADAFIIAVPTPFKGDNHEPNLDYIEMASKAIAKVLKKGNLVILESTSPVGTTEQMAKWLAEERSDLSFPHQCGEVSDIKIAHCPERVLPGQVIRELVENDRIIGGMTQKCAEYAIRLYKIFVQGECIMTNARTAEMTKLTENSFRDLNIAFANELSILCDKLDINVWELIKLANRHPRVNILQPGCGVGGHCIAVDPWFIVYQNPNEAKIIKTAREVNDNKPNFVVQKIKKKIKDILGPKIACLGLAFKPDIDDLRESPALDIVIKLASENASQILVVEPNIKQLPLKLQNKRNIKLVCLSQALDEADVVAVLVRHKEFIEVQSDKVVSFC

[Multiple Choices]
A. Lipid metabolism. .
B. Alkaloid biosynthesis
C. capsule polysaccharide biosynthesis. .
D. Capsule biogenesis
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

> The sequence-matched UniProt pathway annotation explicitly lists “Capsule biogenesis; capsule polysaccharide biosynthesis,” supporting the keyed choice. The annotation cites a 2024 paper and carries experimental evidence, though the excerpt alone does not independently validate the paper’s findings.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with a nucleotide-sugar dehydrogenase, a family whose members make activated sugar derivatives used in polysaccharide synthesis. Transferable knowledge that capsule polysaccharides are assembled from such sugar precursors gives a meaningful basis for choosing the capsule-related options over lipid metabolism or alkaloid biosynthesis.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level inference from the sequence and the functions of related enzymes can distinguish the capsule-related choices without knowing this protein’s exact database annotation. That inference supports the broad pathway assignment, but does not distinguish capsule biogenesis from capsule polysaccharide biosynthesis.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C",
  "D"
]
```

> The sequence-matched source annotation names both capsule biogenesis and capsule polysaccharide biosynthesis as the pathway, and the choices provide no basis to prefer one label over the other.


### Important caveats

- The reviewer-only source identifies a specific enzyme and organism; those details were not supplied in the original input and are not used as original-input facts.
- The pathway annotation applies to the exact matched sequence, but the author’s source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a nucleotide-sugar dehydrogenase, a family whose members make activated sugar derivatives used in polysaccharide synthesis. Transferable knowledge that capsule polysaccharides are assembled from such sugar precursors gives a meaningful basis for choosing the capsule-related options over lipid metabolism or alkaloid biosynthesis.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from the sequence and the functions of related enzymes can distinguish the capsule-related choices without knowing this protein’s exact database annotation. That inference supports the broad pathway assignment, but does not distinguish capsule biogenesis from capsule polysaccharide biosynthesis."
  },
  "case_id": "pathway_0062",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt pathway annotation explicitly lists “Capsule biogenesis; capsule polysaccharide biosynthesis,” supporting the keyed choice. The annotation cites a 2024 paper and carries experimental evidence, though the excerpt alone does not independently validate the paper’s findings."
  },
  "important_caveats": [
    "The reviewer-only source identifies a specific enzyme and organism; those details were not supplied in the original input and are not used as original-input facts.",
    "The pathway annotation applies to the exact matched sequence, but the author’s source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C",
      "D"
    ],
    "reason": "The sequence-matched source annotation names both capsule biogenesis and capsule polysaccharide biosynthesis as the pathway, and the choices provide no basis to prefer one label over the other."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0062",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt pathway annotation explicitly lists “Capsule biogenesis; capsule polysaccharide biosynthesis,” supporting the keyed choice. The annotation cites a 2024 paper and carries experimental evidence, though the excerpt alone does not independently validate the paper’s findings.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with a nucleotide-sugar dehydrogenase, a family whose members make activated sugar derivatives used in polysaccharide synthesis. Transferable knowledge that capsule polysaccharides are assembled from such sugar precursors gives a meaningful basis for choosing the capsule-related options over lipid metabolism or alkaloid biosynthesis.",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from the sequence and the functions of related enzymes can distinguish the capsule-related choices without knowing this protein’s exact database annotation. That inference supports the broad pathway assignment, but does not distinguish capsule biogenesis from capsule polysaccharide biosynthesis."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["C", "D"],
    "reason": "The sequence-matched source annotation names both capsule biogenesis and capsule polysaccharide biosynthesis as the pathway, and the choices provide no basis to prefer one label over the other."
  },
  "important_caveats": [
    "The reviewer-only source identifies a specific enzyme and organism; those details were not supplied in the original input and are not used as original-input facts.",
    "The pathway annotation applies to the exact matched sequence, but the author’s source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation for this sequence (A0A0U3AB61, UDP-N-acetyl-D-mannosamine dehydrogenase, EC 1.1.1.336) explicitly states the pathway as 'Capsule biogenesis; capsule polysaccharide biosynthesis' with experimental evidence (ECO:0000269|PubMed:38382015). Choice D ('Capsule biogenesis') appears verbatim as the first (broader) term in this annotation. However, Choice C ('capsule polysaccharide biosynthesis') is equally present as the sub-pathway term in the same annotation, creating ambiguity about which is 'the primary pathway.'

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C4](#evidence-c4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence (~407 aa) displays hallmark SDR (short-chain dehydrogenase/reductase) family features: a Rossmann-fold-like GxGxxG motif (GLGYIG near N-terminus), a second glycine-rich loop (TSPVGT), and the overall SDR fold architecture. SDRs catalyze NAD(P)-dependent oxidoreductions. Recognizing this as a sugar-nucleotide dehydrogenase (converting UDP-sugar intermediates) immediately excludes lipid metabolism (A) and alkaloid biosynthesis (B), which do not involve UDP-sugar dehydrogenation. Narrowing to capsule-related pathways (C or D) is supported by the general principle that sugar nucleotide dehydrogenases (e.g., UDP-glucose 6-dehydrogenase family members) are key enzymes in polysaccharide precursor biosynthesis. The 'primary pathway' phrasing aligns with UniProt's hierarchical annotation format ('Broader; Sub-pathway'), where the first-listed broader term ('Capsule biogenesis') is conventionally the primary pathway designation. This database-ontology convention is transferable across all UniProt pathway annotations.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The SDR family recognition and the principle that sugar-nucleotide dehydrogenases participate in polysaccharide/capsule biosynthesis provide a credible transferable inference excluding A and B. The C vs D distinction is resolved by the UniProt convention that the first term in 'X; Y' is the broader/primary pathway, which is generalizable across all UniProt annotations. However, biological reasoning could equally favor C as the more specific and mechanistically direct pathway for a dehydrogenase step, making the C/D distinction somewhat arbitrary.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C",
  "D"
]
```

> The UniProt pathway annotation explicitly lists both 'Capsule biogenesis' and 'capsule polysaccharide biosynthesis' in a single entry. Choice C is the specific sub-pathway where the enzymatic step directly occurs; Choice D is the broader umbrella pathway. The question asks for 'the primary metabolic or signaling pathway,' which could mean either the broader category (D) or the most directly relevant pathway (C). Both are defensible readings of the annotation.


### Important caveats

- The C vs D distinction is essentially a question of pathway-hierarchy granularity rather than a biological mechanism question. Both terms appear in the same UniProt annotation line.
- Biological reasoning (a dehydrogenase acting on a sugar nucleotide is most directly in polysaccharide biosynthesis) would arguably favor C, while the UniProt convention of listing the broader term first supports D as 'primary.'
- The protein's SDR family assignment is inferable from sequence, but the specific substrate (UDP-ManNAc) and organism (Campylobacter jejuni) are not provided in the original input; placing it in capsule biosynthesis specifically requires either family-level knowledge of sugar-nucleotide dehydrogenases or recognition of this specific enzyme.
- The 2024 experimental characterization (PubMed:38382015) post-dates many training cutoffs, so the specific pathway assignment may not be widely represented in model training data.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence (~407 aa) displays hallmark SDR (short-chain dehydrogenase/reductase) family features: a Rossmann-fold-like GxGxxG motif (GLGYIG near N-terminus), a second glycine-rich loop (TSPVGT), and the overall SDR fold architecture. SDRs catalyze NAD(P)-dependent oxidoreductions. Recognizing this as a sugar-nucleotide dehydrogenase (converting UDP-sugar intermediates) immediately excludes lipid metabolism (A) and alkaloid biosynthesis (B), which do not involve UDP-sugar dehydrogenation. Narrowing to capsule-related pathways (C or D) is supported by the general principle that sugar nucleotide dehydrogenases (e.g., UDP-glucose 6-dehydrogenase family members) are key enzymes in polysaccharide precursor biosynthesis. The 'primary pathway' phrasing aligns with UniProt's hierarchical annotation format ('Broader; Sub-pathway'), where the first-listed broader term ('Capsule biogenesis') is conventionally the primary pathway designation. This database-ontology convention is transferable across all UniProt pathway annotations.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The SDR family recognition and the principle that sugar-nucleotide dehydrogenases participate in polysaccharide/capsule biosynthesis provide a credible transferable inference excluding A and B. The C vs D distinction is resolved by the UniProt convention that the first term in 'X; Y' is the broader/primary pathway, which is generalizable across all UniProt annotations. However, biological reasoning could equally favor C as the more specific and mechanistically direct pathway for a dehydrogenase step, making the C/D distinction somewhat arbitrary."
  },
  "case_id": "pathway_0062",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C4"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation for this sequence (A0A0U3AB61, UDP-N-acetyl-D-mannosamine dehydrogenase, EC 1.1.1.336) explicitly states the pathway as 'Capsule biogenesis; capsule polysaccharide biosynthesis' with experimental evidence (ECO:0000269|PubMed:38382015). Choice D ('Capsule biogenesis') appears verbatim as the first (broader) term in this annotation. However, Choice C ('capsule polysaccharide biosynthesis') is equally present as the sub-pathway term in the same annotation, creating ambiguity about which is 'the primary pathway.'"
  },
  "important_caveats": [
    "The C vs D distinction is essentially a question of pathway-hierarchy granularity rather than a biological mechanism question. Both terms appear in the same UniProt annotation line.",
    "Biological reasoning (a dehydrogenase acting on a sugar nucleotide is most directly in polysaccharide biosynthesis) would arguably favor C, while the UniProt convention of listing the broader term first supports D as 'primary.'",
    "The protein's SDR family assignment is inferable from sequence, but the specific substrate (UDP-ManNAc) and organism (Campylobacter jejuni) are not provided in the original input; placing it in capsule biosynthesis specifically requires either family-level knowledge of sugar-nucleotide dehydrogenases or recognition of this specific enzyme.",
    "The 2024 experimental characterization (PubMed:38382015) post-dates many training cutoffs, so the specific pathway assignment may not be widely represented in model training data."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C",
      "D"
    ],
    "reason": "The UniProt pathway annotation explicitly lists both 'Capsule biogenesis' and 'capsule polysaccharide biosynthesis' in a single entry. Choice C is the specific sub-pathway where the enzymatic step directly occurs; Choice D is the broader umbrella pathway. The question asks for 'the primary metabolic or signaling pathway,' which could mean either the broader category (D) or the most directly relevant pathway (C). Both are defensible readings of the annotation."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0062",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation for this sequence (A0A0U3AB61, UDP-N-acetyl-D-mannosamine dehydrogenase, EC 1.1.1.336) explicitly states the pathway as 'Capsule biogenesis; capsule polysaccharide biosynthesis' with experimental evidence (ECO:0000269|PubMed:38382015). Choice D ('Capsule biogenesis') appears verbatim as the first (broader) term in this annotation. However, Choice C ('capsule polysaccharide biosynthesis') is equally present as the sub-pathway term in the same annotation, creating ambiguity about which is 'the primary pathway.'",
    "evidence_ids": ["C5", "H3", "C4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence (~407 aa) displays hallmark SDR (short-chain dehydrogenase/reductase) family features: a Rossmann-fold-like GxGxxG motif (GLGYIG near N-terminus), a second glycine-rich loop (TSPVGT), and the overall SDR fold architecture. SDRs catalyze NAD(P)-dependent oxidoreductions. Recognizing this as a sugar-nucleotide dehydrogenase (converting UDP-sugar intermediates) immediately excludes lipid metabolism (A) and alkaloid biosynthesis (B), which do not involve UDP-sugar dehydrogenation. Narrowing to capsule-related pathways (C or D) is supported by the general principle that sugar nucleotide dehydrogenases (e.g., UDP-glucose 6-dehydrogenase family members) are key enzymes in polysaccharide precursor biosynthesis. The 'primary pathway' phrasing aligns with UniProt's hierarchical annotation format ('Broader; Sub-pathway'), where the first-listed broader term ('Capsule biogenesis') is conventionally the primary pathway designation. This database-ontology convention is transferable across all UniProt pathway annotations.",
    "missing_item_specific_fact": "",
    "reason": "The SDR family recognition and the principle that sugar-nucleotide dehydrogenases participate in polysaccharide/capsule biosynthesis provide a credible transferable inference excluding A and B. The C vs D distinction is resolved by the UniProt convention that the first term in 'X; Y' is the broader/primary pathway, which is generalizable across all UniProt annotations. However, biological reasoning could equally favor C as the more specific and mechanistically direct pathway for a dehydrogenase step, making the C/D distinction somewhat arbitrary."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["C", "D"],
    "reason": "The UniProt pathway annotation explicitly lists both 'Capsule biogenesis' and 'capsule polysaccharide biosynthesis' in a single entry. Choice C is the specific sub-pathway where the enzymatic step directly occurs; Choice D is the broader umbrella pathway. The question asks for 'the primary metabolic or signaling pathway,' which could mean either the broader category (D) or the most directly relevant pathway (C). Both are defensible readings of the annotation."
  },
  "important_caveats": [
    "The C vs D distinction is essentially a question of pathway-hierarchy granularity rather than a biological mechanism question. Both terms appear in the same UniProt annotation line.",
    "Biological reasoning (a dehydrogenase acting on a sugar nucleotide is most directly in polysaccharide biosynthesis) would arguably favor C, while the UniProt convention of listing the broader term first supports D as 'primary.'",
    "The protein's SDR family assignment is inferable from sequence, but the specific substrate (UDP-ManNAc) and organism (Campylobacter jejuni) are not provided in the original input; placing it in capsule biosynthesis specifically requires either family-level knowledge of sugar-nucleotide dehydrogenases or recognition of this specific enzyme.",
    "The 2024 experimental characterization (PubMed:38382015) post-dates many training cutoffs, so the specific pathway assignment may not be widely represented in model training data."
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
  "benchmark_sequence_length": 407,
  "benchmark_sequence_sha256": "973aa0d220221e72d65582aa5a4553875ac176a4c5c02b0b6f18a17eed4370f3",
  "current_entry_audit": {
    "entryVersion": 22,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2016-03-16",
    "sequenceVersion": 1
  },
  "current_record_sha256": "1ba44594297295985c473e4d8cdbee4c2c9ce9c395356065e2919dc560c56211",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 407,
  "current_source_sequence_sha256": "973aa0d220221e72d65582aa5a4553875ac176a4c5c02b0b6f18a17eed4370f3",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 20,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A0U3AB61",
  "selected_historical_entry_version": 20,
  "selected_historical_record_sha256": "d19839216cf02dcf1b522686093bf66cffa8fdfff2eda11221074180623cea5a",
  "selected_historical_source_sequence_length": 407,
  "selected_historical_source_sequence_sha256": "973aa0d220221e72d65582aa5a4553875ac176a4c5c02b0b6f18a17eed4370f3",
  "selected_historical_version": {
    "accession": "A0A0U3AB61",
    "database": "Swiss-Prot",
    "entryVersion": 20,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "UAMDH_CAMJU",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3AB61.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A0U3AB61\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:24:40.671066+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1ba44594297295985c473e4d8cdbee4c2c9ce9c395356065e2919dc560c56211",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0U3AB61.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3AB61.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":22,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2016-03-16\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:24:40.671066+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1ba44594297295985c473e4d8cdbee4c2c9ce9c395356065e2919dc560c56211",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0U3AB61.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3AB61.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Campylobacterota\",\"Epsilonproteobacteria\",\"Campylobacterales\",\"Campylobacteraceae\",\"Campylobacter\"],\"scientificName\":\"Campylobacter jejuni\",\"taxonId\":197}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:24:40.671066+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1ba44594297295985c473e4d8cdbee4c2c9ce9c395356065e2919dc560c56211",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0U3AB61.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3AB61.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38382015\",\"source\":\"PubMed\"}],\"value\":\"UDP-ManNAc 6-dehydrogenase\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38382015\",\"source\":\"PubMed\"}],\"value\":\"1.1.1.336\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"UDP-N-acetyl-D-mannosamine dehydrogenase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:24:40.671066+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1ba44594297295985c473e4d8cdbee4c2c9ce9c395356065e2919dc560c56211",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0U3AB61.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3AB61.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38382015\",\"source\":\"PubMed\"}],\"value\":\"Capsule biogenesis; capsule polysaccharide biosynthesis\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-01T06:24:40.671066+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1ba44594297295985c473e4d8cdbee4c2c9ce9c395356065e2919dc560c56211",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0U3AB61.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3AB61.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Ghosh M.K.\",\"Raushel F.M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38382015\"},{\"database\":\"DOI\",\"id\":\"10.1021/acs.biochem.3c00664\"}],\"citationType\":\"journal article\",\"firstPage\":\"688\",\"id\":\"38382015\",\"journal\":\"Biochemistry\",\"lastPage\":\"698\",\"publicationDate\":\"2024\",\"title\":\"Biosynthesis of UDP-alpha-N-Acetyl-d-mannosaminuronic Acid and CMP-beta-N-Acetyl-d-neuraminic Acid for the Capsular Polysaccharides of Campylobacter jejuni.\",\"volume\":\"63\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"HS:11\"}],\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-01T06:24:40.671066+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1ba44594297295985c473e4d8cdbee4c2c9ce9c395356065e2919dc560c56211",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0U3AB61.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0U3AB61?format=txt&versions=20)

```json
{
  "entry_version": 20,
  "evidence_id": "H1",
  "excerpt": "ID   UAMDH_CAMJU             Reviewed;         407 AA.\nAC   A0A0U3AB61;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   16-MAR-2016, sequence version 1.\nDT   28-JAN-2026, entry version 20.\nDE   RecName: Full=UDP-N-acetyl-D-mannosamine dehydrogenase {ECO:0000305};\nDE            EC=1.1.1.336 {ECO:0000269|PubMed:38382015};\nDE   AltName: Full=UDP-ManNAc 6-dehydrogenase {ECO:0000303|PubMed:38382015};\nGN   Name=HS11.16 {ECO:0000303|PubMed:38382015};\nOS   Campylobacter jejuni.\nOC   Bacteria; Pseudomonadati; Campylobacterota; Epsilonproteobacteria;\nOC   Campylobacterales; Campylobacteraceae; Campylobacter.\nOX   NCBI_TaxID=197;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:21.162556+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d19839216cf02dcf1b522686093bf66cffa8fdfff2eda11221074180623cea5a",
  "url": "https://rest.uniprot.org/unisave/A0A0U3AB61?format=txt&versions=20"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0U3AB61?format=txt&versions=20)

```json
{
  "entry_version": 20,
  "evidence_id": "H2",
  "excerpt": "RN   [3]\nRP   FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, AND PATHWAY.\nRC   STRAIN=HS:11;\nRX   PubMed=38382015; DOI=10.1021/acs.biochem.3c00664;\nRA   Ghosh M.K., Raushel F.M.;\nRT   \"Biosynthesis of UDP-alpha-N-Acetyl-d-mannosaminuronic Acid and CMP-beta-N-\nRT   Acetyl-d-neuraminic Acid for the Capsular Polysaccharides of Campylobacter\nRT   jejuni.\";\nRL   Biochemistry 63:688-698(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:21.162556+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 29-37",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d19839216cf02dcf1b522686093bf66cffa8fdfff2eda11221074180623cea5a",
  "url": "https://rest.uniprot.org/unisave/A0A0U3AB61?format=txt&versions=20"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0U3AB61?format=txt&versions=20)

```json
{
  "entry_version": 20,
  "evidence_id": "H3",
  "excerpt": "CC   -!- PATHWAY: Capsule biogenesis; capsule polysaccharide biosynthesis.\nCC       {ECO:0000269|PubMed:38382015}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:21.162556+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 56-57",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d19839216cf02dcf1b522686093bf66cffa8fdfff2eda11221074180623cea5a",
  "url": "https://rest.uniprot.org/unisave/A0A0U3AB61?format=txt&versions=20"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 62. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
