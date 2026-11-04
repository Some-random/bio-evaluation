# pathway_0184

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/pathway_0184.txt)

**Task:** `pathway`  
**Expected answer:** **D** — Amino-acid biosynthesis

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MATPSKKRCGVLGATGAVGTRFILLLSQHPLLELVAVGASDRSSGKKYRDAVRWKQSAPMPAKVADLTVRCCDPAEFSDCDIIFSGLDPDAAGEIEMAFLKANFAVFSNAKNYRLDPMVPLVVPLVNAGHIDVIPAQRKHFGLDKGMLVCNSNCAVVGLVVPAKALIQKFGPIESVSMVTMQAVSGAGYPGVSSMDIFDNIVPYIPGEEGKISSEARKILGDLNSDLAGFSDQKPLQISVACNRVPVLDGHTVCASLRFVNRPPPTASQVREALREYKPEVQTLGCPSAPKMSIHVMDEVDRPQPRLDRETEGGYACTVGRIREDDSDVFDIQFVALSHNTVLGASGSSILNAESAILKGFV

[Multiple Choices]
A. peptidoglycan biosynthesis. .
B. xylan degradation. .
C. L-isoleucine biosynthesis
D. Amino-acid biosynthesis
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

> The sequence-matched annotation identifies the protein as aspartate-semialdehyde dehydrogenase and places it in amino-acid biosynthesis, including the aspartate-derived methionine and threonine pathways. This supports D. The pathway annotation cites experimental evidence, though the excerpts do not independently establish the details of that experiment.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence's glycine-rich nucleotide-binding region and overall enzyme-family sequence pattern are consistent with aspartate-semialdehyde dehydrogenase. Transferable knowledge of this enzyme family places it in the aspartate-derived amino-acid biosynthesis pathway. That meaningfully favors the broad amino-acid biosynthesis option over peptidoglycan biosynthesis, xylan degradation, and the more specific L-isoleucine biosynthesis option.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level sequence inference can distinguish the offered choices without knowing this protein's database record. The inference is probabilistic, but the alternatives include a broad pathway category that fits the enzyme's known role.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The annotated roles are in amino-acid biosynthesis; the more specific L-isoleucine option does not describe this enzyme's pathway role.


### Important caveats

- The pathway evidence is an annotation citing a publication; these excerpts do not independently validate the experiments.
- The reviewer-only organism and accession information was not part of the original input and is not needed for the family-level inference.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence's glycine-rich nucleotide-binding region and overall enzyme-family sequence pattern are consistent with aspartate-semialdehyde dehydrogenase. Transferable knowledge of this enzyme family places it in the aspartate-derived amino-acid biosynthesis pathway. That meaningfully favors the broad amino-acid biosynthesis option over peptidoglycan biosynthesis, xylan degradation, and the more specific L-isoleucine biosynthesis option.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level sequence inference can distinguish the offered choices without knowing this protein's database record. The inference is probabilistic, but the alternatives include a broad pathway category that fits the enzyme's known role."
  },
  "case_id": "pathway_0184",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched annotation identifies the protein as aspartate-semialdehyde dehydrogenase and places it in amino-acid biosynthesis, including the aspartate-derived methionine and threonine pathways. This supports D. The pathway annotation cites experimental evidence, though the excerpts do not independently establish the details of that experiment."
  },
  "important_caveats": [
    "The pathway evidence is an annotation citing a publication; these excerpts do not independently validate the experiments.",
    "The reviewer-only organism and accession information was not part of the original input and is not needed for the family-level inference."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The annotated roles are in amino-acid biosynthesis; the more specific L-isoleucine option does not describe this enzyme's pathway role."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0184",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched annotation identifies the protein as aspartate-semialdehyde dehydrogenase and places it in amino-acid biosynthesis, including the aspartate-derived methionine and threonine pathways. This supports D. The pathway annotation cites experimental evidence, though the excerpts do not independently establish the details of that experiment.",
    "evidence_ids": ["C4", "C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence's glycine-rich nucleotide-binding region and overall enzyme-family sequence pattern are consistent with aspartate-semialdehyde dehydrogenase. Transferable knowledge of this enzyme family places it in the aspartate-derived amino-acid biosynthesis pathway. That meaningfully favors the broad amino-acid biosynthesis option over peptidoglycan biosynthesis, xylan degradation, and the more specific L-isoleucine biosynthesis option.",
    "missing_item_specific_fact": "",
    "reason": "A family-level sequence inference can distinguish the offered choices without knowing this protein's database record. The inference is probabilistic, but the alternatives include a broad pathway category that fits the enzyme's known role."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The annotated roles are in amino-acid biosynthesis; the more specific L-isoleucine option does not describe this enzyme's pathway role."
  },
  "important_caveats": [
    "The pathway evidence is an annotation citing a publication; these excerpts do not independently validate the experiments.",
    "The reviewer-only organism and accession information was not part of the original input and is not needed for the family-level inference."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation for this sequence (A0A080WMA9) identifies it as Aspartate-semialdehyde dehydrogenase (EC 1.2.1.11) with pathway annotations 'Amino-acid biosynthesis; L-methionine biosynthesis via de novo pathway' and 'Amino-acid biosynthesis; L-threonine biosynthesis.' The expected answer D ('Amino-acid biosynthesis') directly matches the UniProt pathway annotation. The evidence codes (ECO:0000269|PubMed:26869335) indicate experimental support from X-ray crystallography and functional studies.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C4](#evidence-c4), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a recognizable NAD(P)-binding Rossmann fold motif (GAGYPG...GEEGK region) and a catalytic Cys-His dyad (CNSNCAVVGLVVPAK...HTVCASLRFV), which are hallmarks of aspartate-semialdehyde dehydrogenase (ASADH), a well-characterized enzyme family in the aspartate pathway of amino acid biosynthesis (leading to methionine, threonine, and lysine). A model with knowledge of dehydrogenase families can: (1) rule out A (peptidoglycan biosynthesis) because the protein has a eukaryotic signal peptide region and peptidoglycan synthesis is bacterial; (2) rule out B (xylan degradation) because xylan-active enzymes are glycosyl hydrolases, not NAD-dependent dehydrogenases; (3) rule out C (L-isoleucine biosynthesis) because the aspartate pathway (ASADH) is mechanistically distinct from isoleucine biosynthesis, which proceeds via threonine deaminase and branched-chain amino acid transaminases, not NAD-dependent dehydrogenases with Cys-His catalytic dyads; (4) select D (Amino-acid biosynthesis) as the correct general pathway category for ASADH.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence contains identifiable family-level features (Rossmann NAD-binding fold, catalytic Cys-His dyad, overall domain architecture) that are shared with other ASADH homologs across bacteria and fungi. A knowledgeable model can use these conserved features to place the protein in the ASADH family and thereby in the aspartate amino acid biosynthesis pathway, distinguishing it from isoleucine biosynthesis (which uses entirely different enzyme classes), peptidoglycan synthesis (bacterial), and xylan degradation (hydrolases). This is transferable family knowledge, not a lookup of this specific protein's record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> ASADH is definitively in the aspartate pathway (methionine/threonine/lysine biosynthesis), not isoleucine biosynthesis. The distinction between C and D is clear: isoleucine biosynthesis uses threonine deaminase and branched-chain enzymes, not NAD-dependent dehydrogenases with Cys-His catalytic pairs. Options A and B are clearly wrong for a eukaryotic NAD-dependent dehydrogenase. Only D is defensible.


### Important caveats

- The distinction between C and D relies on recognizing the protein as ASADH specifically (not just any NAD-dependent dehydrogenase). A model that only identifies 'some NAD-dependent dehydrogenase' might struggle between C and D, but the catalytic Cys-His dyad and overall fold are sufficiently characteristic of ASADH for family-level identification.
- Option D is a broad category while C is specific. If the protein were in isoleucine biosynthesis, both C and D could arguably be correct (since isoleucine biosynthesis is a subset of amino acid biosynthesis). However, since ASADH is not in isoleucine biosynthesis, this ambiguity does not arise.
- The sequence includes what appears to be a fungal signal peptide region at the N-terminus, consistent with a eukaryotic (fungal) origin, further supporting exclusion of peptidoglycan biosynthesis.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a recognizable NAD(P)-binding Rossmann fold motif (GAGYPG...GEEGK region) and a catalytic Cys-His dyad (CNSNCAVVGLVVPAK...HTVCASLRFV), which are hallmarks of aspartate-semialdehyde dehydrogenase (ASADH), a well-characterized enzyme family in the aspartate pathway of amino acid biosynthesis (leading to methionine, threonine, and lysine). A model with knowledge of dehydrogenase families can: (1) rule out A (peptidoglycan biosynthesis) because the protein has a eukaryotic signal peptide region and peptidoglycan synthesis is bacterial; (2) rule out B (xylan degradation) because xylan-active enzymes are glycosyl hydrolases, not NAD-dependent dehydrogenases; (3) rule out C (L-isoleucine biosynthesis) because the aspartate pathway (ASADH) is mechanistically distinct from isoleucine biosynthesis, which proceeds via threonine deaminase and branched-chain amino acid transaminases, not NAD-dependent dehydrogenases with Cys-His catalytic dyads; (4) select D (Amino-acid biosynthesis) as the correct general pathway category for ASADH.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence contains identifiable family-level features (Rossmann NAD-binding fold, catalytic Cys-His dyad, overall domain architecture) that are shared with other ASADH homologs across bacteria and fungi. A knowledgeable model can use these conserved features to place the protein in the ASADH family and thereby in the aspartate amino acid biosynthesis pathway, distinguishing it from isoleucine biosynthesis (which uses entirely different enzyme classes), peptidoglycan synthesis (bacterial), and xylan degradation (hydrolases). This is transferable family knowledge, not a lookup of this specific protein's record."
  },
  "case_id": "pathway_0184",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C4",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation for this sequence (A0A080WMA9) identifies it as Aspartate-semialdehyde dehydrogenase (EC 1.2.1.11) with pathway annotations 'Amino-acid biosynthesis; L-methionine biosynthesis via de novo pathway' and 'Amino-acid biosynthesis; L-threonine biosynthesis.' The expected answer D ('Amino-acid biosynthesis') directly matches the UniProt pathway annotation. The evidence codes (ECO:0000269|PubMed:26869335) indicate experimental support from X-ray crystallography and functional studies."
  },
  "important_caveats": [
    "The distinction between C and D relies on recognizing the protein as ASADH specifically (not just any NAD-dependent dehydrogenase). A model that only identifies 'some NAD-dependent dehydrogenase' might struggle between C and D, but the catalytic Cys-His dyad and overall fold are sufficiently characteristic of ASADH for family-level identification.",
    "Option D is a broad category while C is specific. If the protein were in isoleucine biosynthesis, both C and D could arguably be correct (since isoleucine biosynthesis is a subset of amino acid biosynthesis). However, since ASADH is not in isoleucine biosynthesis, this ambiguity does not arise.",
    "The sequence includes what appears to be a fungal signal peptide region at the N-terminus, consistent with a eukaryotic (fungal) origin, further supporting exclusion of peptidoglycan biosynthesis."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "ASADH is definitively in the aspartate pathway (methionine/threonine/lysine biosynthesis), not isoleucine biosynthesis. The distinction between C and D is clear: isoleucine biosynthesis uses threonine deaminase and branched-chain enzymes, not NAD-dependent dehydrogenases with Cys-His catalytic pairs. Options A and B are clearly wrong for a eukaryotic NAD-dependent dehydrogenase. Only D is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0184",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation for this sequence (A0A080WMA9) identifies it as Aspartate-semialdehyde dehydrogenase (EC 1.2.1.11) with pathway annotations 'Amino-acid biosynthesis; L-methionine biosynthesis via de novo pathway' and 'Amino-acid biosynthesis; L-threonine biosynthesis.' The expected answer D ('Amino-acid biosynthesis') directly matches the UniProt pathway annotation. The evidence codes (ECO:0000269|PubMed:26869335) indicate experimental support from X-ray crystallography and functional studies.",
    "evidence_ids": ["C5", "C6", "C4", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a recognizable NAD(P)-binding Rossmann fold motif (GAGYPG...GEEGK region) and a catalytic Cys-His dyad (CNSNCAVVGLVVPAK...HTVCASLRFV), which are hallmarks of aspartate-semialdehyde dehydrogenase (ASADH), a well-characterized enzyme family in the aspartate pathway of amino acid biosynthesis (leading to methionine, threonine, and lysine). A model with knowledge of dehydrogenase families can: (1) rule out A (peptidoglycan biosynthesis) because the protein has a eukaryotic signal peptide region and peptidoglycan synthesis is bacterial; (2) rule out B (xylan degradation) because xylan-active enzymes are glycosyl hydrolases, not NAD-dependent dehydrogenases; (3) rule out C (L-isoleucine biosynthesis) because the aspartate pathway (ASADH) is mechanistically distinct from isoleucine biosynthesis, which proceeds via threonine deaminase and branched-chain amino acid transaminases, not NAD-dependent dehydrogenases with Cys-His catalytic dyads; (4) select D (Amino-acid biosynthesis) as the correct general pathway category for ASADH.",
    "missing_item_specific_fact": "",
    "reason": "The sequence contains identifiable family-level features (Rossmann NAD-binding fold, catalytic Cys-His dyad, overall domain architecture) that are shared with other ASADH homologs across bacteria and fungi. A knowledgeable model can use these conserved features to place the protein in the ASADH family and thereby in the aspartate amino acid biosynthesis pathway, distinguishing it from isoleucine biosynthesis (which uses entirely different enzyme classes), peptidoglycan synthesis (bacterial), and xylan degradation (hydrolases). This is transferable family knowledge, not a lookup of this specific protein's record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "ASADH is definitively in the aspartate pathway (methionine/threonine/lysine biosynthesis), not isoleucine biosynthesis. The distinction between C and D is clear: isoleucine biosynthesis uses threonine deaminase and branched-chain enzymes, not NAD-dependent dehydrogenases with Cys-His catalytic pairs. Options A and B are clearly wrong for a eukaryotic NAD-dependent dehydrogenase. Only D is defensible."
  },
  "important_caveats": [
    "The distinction between C and D relies on recognizing the protein as ASADH specifically (not just any NAD-dependent dehydrogenase). A model that only identifies 'some NAD-dependent dehydrogenase' might struggle between C and D, but the catalytic Cys-His dyad and overall fold are sufficiently characteristic of ASADH for family-level identification.",
    "Option D is a broad category while C is specific. If the protein were in isoleucine biosynthesis, both C and D could arguably be correct (since isoleucine biosynthesis is a subset of amino acid biosynthesis). However, since ASADH is not in isoleucine biosynthesis, this ambiguity does not arise.",
    "The sequence includes what appears to be a fungal signal peptide region at the N-terminus, consistent with a eukaryotic (fungal) origin, further supporting exclusion of peptidoglycan biosynthesis."
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
  "benchmark_sequence_sha256": "ecc9f93bab233675495553ca0dc99c02862199248d190fa6418b0eaf45c3d7b5",
  "current_entry_audit": {
    "entryVersion": 40,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2014-10-29",
    "sequenceVersion": 1
  },
  "current_record_sha256": "bf278bc137aa3857c873dcee85929131e2e626bb23054806edb11415af48ec0e",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 362,
  "current_source_sequence_sha256": "ecc9f93bab233675495553ca0dc99c02862199248d190fa6418b0eaf45c3d7b5",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 38,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A080WMA9",
  "selected_historical_entry_version": 38,
  "selected_historical_record_sha256": "319e2a6ea09f79026f215490dfab47119b95e8f6a8e21b934e31e170e04fc34f",
  "selected_historical_source_sequence_length": 362,
  "selected_historical_source_sequence_sha256": "ecc9f93bab233675495553ca0dc99c02862199248d190fa6418b0eaf45c3d7b5",
  "selected_historical_version": {
    "accession": "A0A080WMA9",
    "database": "Swiss-Prot",
    "entryVersion": 38,
    "firstRelease": "2025_03/2025_03",
    "firstReleaseDate": "18-Jun-2025",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "DHAS_TRIRC",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A080WMA9.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A080WMA9\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:23:53.783847+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bf278bc137aa3857c873dcee85929131e2e626bb23054806edb11415af48ec0e",
  "url": "https://rest.uniprot.org/uniprotkb/A0A080WMA9.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A080WMA9.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":40,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2014-10-29\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:23:53.783847+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bf278bc137aa3857c873dcee85929131e2e626bb23054806edb11415af48ec0e",
  "url": "https://rest.uniprot.org/uniprotkb/A0A080WMA9.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A080WMA9.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Athlete's foot fungus\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000008864\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Eurotiomycetes\",\"Eurotiomycetidae\",\"Onygenales\",\"Arthrodermataceae\",\"Trichophyton\"],\"scientificName\":\"Trichophyton rubrum (strain ATCC MYA-4607 / CBS 118892)\",\"taxonId\":559305}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:23:53.783847+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bf278bc137aa3857c873dcee85929131e2e626bb23054806edb11415af48ec0e",
  "url": "https://rest.uniprot.org/uniprotkb/A0A080WMA9.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A080WMA9.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"26869335\",\"source\":\"PubMed\"}],\"value\":\"TrASADH\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"26869335\",\"source\":\"PubMed\"}],\"value\":\"1.2.1.11\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Aspartate-semialdehyde dehydrogenase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:23:53.783847+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bf278bc137aa3857c873dcee85929131e2e626bb23054806edb11415af48ec0e",
  "url": "https://rest.uniprot.org/uniprotkb/A0A080WMA9.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A080WMA9.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"26869335\",\"source\":\"PubMed\"}],\"value\":\"Amino-acid biosynthesis; L-methionine biosynthesis via de novo pathway; L-homoserine from L-aspartate: step 2/3\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-02T04:23:53.783847+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bf278bc137aa3857c873dcee85929131e2e626bb23054806edb11415af48ec0e",
  "url": "https://rest.uniprot.org/uniprotkb/A0A080WMA9.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A080WMA9.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"26869335\",\"source\":\"PubMed\"}],\"value\":\"Amino-acid biosynthesis; L-threonine biosynthesis; L-threonine from L-aspartate: step 2/5\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/4",
  "retrieved_utc": "2026-11-02T04:23:53.783847+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bf278bc137aa3857c873dcee85929131e2e626bb23054806edb11415af48ec0e",
  "url": "https://rest.uniprot.org/uniprotkb/A0A080WMA9.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A080WMA9.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Li Q.\",\"Mu Z.\",\"Zhao R.\",\"Dahal G.\",\"Viola R.E.\",\"Liu T.\",\"Jin Q.\",\"Cui S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"26869335\"},{\"database\":\"DOI\",\"id\":\"10.1038/srep21067\"}],\"citationType\":\"journal article\",\"firstPage\":\"21067\",\"id\":\"26869335\",\"journal\":\"Sci. Rep.\",\"lastPage\":\"21067\",\"publicationDate\":\"2016\",\"title\":\"Structural Insights into the Tetrameric State of Aspartate-beta-semialdehyde Dehydrogenases from Fungal Species.\",\"volume\":\"6\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"4ZHS\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"4ZIC\",\"source\":\"PDB\"}],\"referenceComments\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"26869335\",\"source\":\"PubMed\"}],\"type\":\"STRAIN\",\"value\":\"BMU01672\"}],\"referenceNumber\":2,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (2.55 ANGSTROMS) IN COMPLEX WITH NADP(+)\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"PATHWAY\",\"SUBUNIT\",\"MUTAGENESIS OF 196-ASP--PHE-198 AND ARG-309\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:23:53.783847+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bf278bc137aa3857c873dcee85929131e2e626bb23054806edb11415af48ec0e",
  "url": "https://rest.uniprot.org/uniprotkb/A0A080WMA9.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A080WMA9?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H1",
  "excerpt": "ID   DHAS_TRIRC              Reviewed;         362 AA.\nAC   A0A080WMA9; A0A140UHG6;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   29-OCT-2014, sequence version 1.\nDT   18-JUN-2025, entry version 38.\nDE   RecName: Full=Aspartate-semialdehyde dehydrogenase {ECO:0000305};\nDE            EC=1.2.1.11 {ECO:0000269|PubMed:26869335};\nDE   AltName: Full=TrASADH {ECO:0000303|PubMed:26869335};\nGN   ORFNames=TERG_03598 {ECO:0000312|EMBL:KFL61260.1};\nOS   Trichophyton rubrum (strain ATCC MYA-4607 / CBS 118892) (Athlete's foot\nOS   fungus).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;\nOC   Eurotiomycetidae; Onygenales; Arthrodermataceae; Trichophyton.\nOX   NCBI_TaxID=559305 {ECO:0000312|Proteomes:UP000008864};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:23:57.418115+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "319e2a6ea09f79026f215490dfab47119b95e8f6a8e21b934e31e170e04fc34f",
  "url": "https://rest.uniprot.org/unisave/A0A080WMA9?format=txt&versions=38"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A080WMA9?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H2",
  "excerpt": "RN   [2] {ECO:0007744|PDB:4ZHS, ECO:0007744|PDB:4ZIC}\nRP   X-RAY CRYSTALLOGRAPHY (2.55 ANGSTROMS) IN COMPLEX WITH NADP(+), FUNCTION,\nRP   CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, PATHWAY, SUBUNIT, AND\nRP   MUTAGENESIS OF 196-ASP--PHE-198 AND ARG-309.\nRC   STRAIN=BMU01672 {ECO:0000303|PubMed:26869335};\nRX   PubMed=26869335; DOI=10.1038/srep21067;\nRA   Li Q., Mu Z., Zhao R., Dahal G., Viola R.E., Liu T., Jin Q., Cui S.;\nRT   \"Structural Insights into the Tetrameric State of Aspartate-beta-\nRT   semialdehyde Dehydrogenases from Fungal Species.\";\nRL   Sci. Rep. 6:21067-21067(2016).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:23:57.418115+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 27-36",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "319e2a6ea09f79026f215490dfab47119b95e8f6a8e21b934e31e170e04fc34f",
  "url": "https://rest.uniprot.org/unisave/A0A080WMA9?format=txt&versions=38"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A080WMA9?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H3",
  "excerpt": "CC   -!- PATHWAY: Amino-acid biosynthesis; L-methionine biosynthesis via de novo\nCC       pathway; L-homoserine from L-aspartate: step 2/3.\nCC       {ECO:0000269|PubMed:26869335}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:23:57.418115+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 57-59",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "319e2a6ea09f79026f215490dfab47119b95e8f6a8e21b934e31e170e04fc34f",
  "url": "https://rest.uniprot.org/unisave/A0A080WMA9?format=txt&versions=38"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A080WMA9?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H4",
  "excerpt": "CC   -!- PATHWAY: Amino-acid biosynthesis; L-threonine biosynthesis; L-threonine\nCC       from L-aspartate: step 2/5. {ECO:0000269|PubMed:26869335}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:23:57.418115+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 60-61",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "319e2a6ea09f79026f215490dfab47119b95e8f6a8e21b934e31e170e04fc34f",
  "url": "https://rest.uniprot.org/unisave/A0A080WMA9?format=txt&versions=38"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 184. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
