# active_site_0000

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/active_site_0000.txt)

**Task:** `active_site`  
**Expected answer:** **C** — Position 154 (Acyl-thioester intermediate)

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
A. Position 256 (Proton acceptor)
B. Position 206 (For beta-ketoacyl synthase activity)
C. Position 154 (Acyl-thioester intermediate)
D. Position 209 (Proton donor)
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzyme Active Site Prediction, which is to identify the key amino acid residues that form the active site of an enzyme. The active site is the specific region on the enzyme where a substrate binds and the chemical reaction is catalyzed. Based on the full protein sequence provided, you must select the option that correctly lists the amino acid residues (by their type and position) that constitute the enzyme's catalytic center.. The inputs provided by the user for this task include:

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

> The sequence-matched UniProt annotation identifies position 154 as the acyl-thioester intermediate site. This annotation is computationally assigned by PIRSR, rather than direct experimental evidence in the supplied excerpts.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with the aspartate-semialdehyde-dehydrogenase family, whose conserved catalytic cysteine forms a covalent acyl-thioester intermediate. The cysteine-containing region around position 154 supports choice C; this family-level mechanism distinguishes it from the unrelated beta-ketoacyl-synthase activity and the offered proton-role alternatives.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model could use family recognition, conserved catalytic features, and the known reaction mechanism to identify the catalytic-thioester choice without recalling this protein's specific database record. Exact residue mapping may require sequence alignment or family knowledge, but that is legitimate transfer.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the offered alternatives, the acyl-thioester-forming catalytic cysteine is the defensible family-based choice.


### Important caveats

- The supporting residue annotation is computationally transferred, not independently demonstrated experimentally by the supplied evidence.
- The sequence and canonical residue numbering match the cited entry; the author's precise source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with the aspartate-semialdehyde-dehydrogenase family, whose conserved catalytic cysteine forms a covalent acyl-thioester intermediate. The cysteine-containing region around position 154 supports choice C; this family-level mechanism distinguishes it from the unrelated beta-ketoacyl-synthase activity and the offered proton-role alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model could use family recognition, conserved catalytic features, and the known reaction mechanism to identify the catalytic-thioester choice without recalling this protein's specific database record. Exact residue mapping may require sequence alignment or family knowledge, but that is legitimate transfer."
  },
  "case_id": "active_site_0000",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies position 154 as the acyl-thioester intermediate site. This annotation is computationally assigned by PIRSR, rather than direct experimental evidence in the supplied excerpts."
  },
  "important_caveats": [
    "The supporting residue annotation is computationally transferred, not independently demonstrated experimentally by the supplied evidence.",
    "The sequence and canonical residue numbering match the cited entry; the author's precise source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered alternatives, the acyl-thioester-forming catalytic cysteine is the defensible family-based choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0000",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies position 154 as the acyl-thioester intermediate site. This annotation is computationally assigned by PIRSR, rather than direct experimental evidence in the supplied excerpts.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with the aspartate-semialdehyde-dehydrogenase family, whose conserved catalytic cysteine forms a covalent acyl-thioester intermediate. The cysteine-containing region around position 154 supports choice C; this family-level mechanism distinguishes it from the unrelated beta-ketoacyl-synthase activity and the offered proton-role alternatives.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model could use family recognition, conserved catalytic features, and the known reaction mechanism to identify the catalytic-thioester choice without recalling this protein's specific database record. Exact residue mapping may require sequence alignment or family knowledge, but that is legitimate transfer."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered alternatives, the acyl-thioester-forming catalytic cysteine is the defensible family-based choice."
  },
  "important_caveats": [
    "The supporting residue annotation is computationally transferred, not independently demonstrated experimentally by the supplied evidence.",
    "The sequence and canonical residue numbering match the cited entry; the author's precise source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (A0A080WMA9) annotates position 154 as 'Acyl-thioester intermediate' active site (evidence C5, H3), with evidence code ECO:0000255 from PIRSR000148. The residue at position 154 in the provided sequence is indeed Cys (C), consistent with the well-established ASADH catalytic mechanism where the catalytic cysteine forms a thioacyl intermediate. The annotation is computational (PIRSR pattern-based) but aligns with the known family mechanism. The other options are contradicted: position 256 is Ser (not the proton acceptor His at 251), position 206 is Ile (irrelevant to ASADH), and position 209 is Glu (not an annotated active site residue).

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C6](#evidence-c6), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains N-terminal Rossmann-fold motifs (e.g., GASDR at ~positions 39-43) and a length (~362 aa) consistent with aspartate-semialdehyde dehydrogenase (ASADH, EC 1.2.1.11). ASADH is a well-characterized enzyme family with a textbook Cys-His catalytic dyad: the cysteine forms a covalent thioacyl (acyl-thioester) intermediate, and the histidine acts as proton acceptor. Option B ('beta-ketoacyl synthase activity') refers to a completely unrelated enzyme class (fatty acid synthesis) and can be eliminated immediately. Option A pairs 'proton acceptor' with position 256, but the proton-accepting His in ASADH is at a different position (251 in this entry); position 256 is Ser. Option D uses 'proton donor,' which is not the standard mechanistic description for ASADH's His. Option C correctly pairs the acyl-thioester intermediate function with a cysteine in the conserved PIRSR000148 motif context (CNSNC around positions 150-155). A model familiar with the ASADH family's conserved catalytic motif and mechanism can identify the catalytic Cys and match it to option C's description.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable knowledge of the ASADH family (catalytic Cys-His dyad, thioacyl intermediate mechanism, conserved motifs, NADP-binding Rossmann fold) combined with elimination of clearly wrong distractors (wrong enzyme class in B, wrong position in A, wrong mechanistic role in D) provides a credible reasoning path to select C without needing to memorize this exact protein's UniProt entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only option C correctly pairs an ASADH active-site residue (Cys) with its proper mechanistic role (acyl-thioester intermediate). The other options contain factual errors: wrong enzyme (B), wrong position for the stated function (A), or wrong mechanistic role (D).


### Important caveats

- The UniProt annotation for position 154 is based on PIRSR pattern matching (ECO:0000255, computational), not direct experimental mutagenesis on this specific protein. However, the ASADH catalytic mechanism is well-established from structural and biochemical studies of homologs (e.g., E. coli ASADH, PDB structures).
- The sequence contains multiple cysteines (positions 9, 72, 73, 81, 150, 154, 243, 254, 287, 318); identifying the catalytic one requires recognizing the conserved PIRSR000148 motif context (CNSNC pattern around 150-155), which is family-level knowledge.
- The reviewer-only evidence confirms the UniProt accession and annotation but was not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains N-terminal Rossmann-fold motifs (e.g., GASDR at ~positions 39-43) and a length (~362 aa) consistent with aspartate-semialdehyde dehydrogenase (ASADH, EC 1.2.1.11). ASADH is a well-characterized enzyme family with a textbook Cys-His catalytic dyad: the cysteine forms a covalent thioacyl (acyl-thioester) intermediate, and the histidine acts as proton acceptor. Option B ('beta-ketoacyl synthase activity') refers to a completely unrelated enzyme class (fatty acid synthesis) and can be eliminated immediately. Option A pairs 'proton acceptor' with position 256, but the proton-accepting His in ASADH is at a different position (251 in this entry); position 256 is Ser. Option D uses 'proton donor,' which is not the standard mechanistic description for ASADH's His. Option C correctly pairs the acyl-thioester intermediate function with a cysteine in the conserved PIRSR000148 motif context (CNSNC around positions 150-155). A model familiar with the ASADH family's conserved catalytic motif and mechanism can identify the catalytic Cys and match it to option C's description.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge of the ASADH family (catalytic Cys-His dyad, thioacyl intermediate mechanism, conserved motifs, NADP-binding Rossmann fold) combined with elimination of clearly wrong distractors (wrong enzyme class in B, wrong position in A, wrong mechanistic role in D) provides a credible reasoning path to select C without needing to memorize this exact protein's UniProt entry."
  },
  "case_id": "active_site_0000",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C6",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (A0A080WMA9) annotates position 154 as 'Acyl-thioester intermediate' active site (evidence C5, H3), with evidence code ECO:0000255 from PIRSR000148. The residue at position 154 in the provided sequence is indeed Cys (C), consistent with the well-established ASADH catalytic mechanism where the catalytic cysteine forms a thioacyl intermediate. The annotation is computational (PIRSR pattern-based) but aligns with the known family mechanism. The other options are contradicted: position 256 is Ser (not the proton acceptor His at 251), position 206 is Ile (irrelevant to ASADH), and position 209 is Glu (not an annotated active site residue)."
  },
  "important_caveats": [
    "The UniProt annotation for position 154 is based on PIRSR pattern matching (ECO:0000255, computational), not direct experimental mutagenesis on this specific protein. However, the ASADH catalytic mechanism is well-established from structural and biochemical studies of homologs (e.g., E. coli ASADH, PDB structures).",
    "The sequence contains multiple cysteines (positions 9, 72, 73, 81, 150, 154, 243, 254, 287, 318); identifying the catalytic one requires recognizing the conserved PIRSR000148 motif context (CNSNC pattern around 150-155), which is family-level knowledge.",
    "The reviewer-only evidence confirms the UniProt accession and annotation but was not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only option C correctly pairs an ASADH active-site residue (Cys) with its proper mechanistic role (acyl-thioester intermediate). The other options contain factual errors: wrong enzyme (B), wrong position for the stated function (A), or wrong mechanistic role (D)."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0000",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (A0A080WMA9) annotates position 154 as 'Acyl-thioester intermediate' active site (evidence C5, H3), with evidence code ECO:0000255 from PIRSR000148. The residue at position 154 in the provided sequence is indeed Cys (C), consistent with the well-established ASADH catalytic mechanism where the catalytic cysteine forms a thioacyl intermediate. The annotation is computational (PIRSR pattern-based) but aligns with the known family mechanism. The other options are contradicted: position 256 is Ser (not the proton acceptor His at 251), position 206 is Ile (irrelevant to ASADH), and position 209 is Glu (not an annotated active site residue).",
    "evidence_ids": ["C5", "H3", "C6", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains N-terminal Rossmann-fold motifs (e.g., GASDR at ~positions 39-43) and a length (~362 aa) consistent with aspartate-semialdehyde dehydrogenase (ASADH, EC 1.2.1.11). ASADH is a well-characterized enzyme family with a textbook Cys-His catalytic dyad: the cysteine forms a covalent thioacyl (acyl-thioester) intermediate, and the histidine acts as proton acceptor. Option B ('beta-ketoacyl synthase activity') refers to a completely unrelated enzyme class (fatty acid synthesis) and can be eliminated immediately. Option A pairs 'proton acceptor' with position 256, but the proton-accepting His in ASADH is at a different position (251 in this entry); position 256 is Ser. Option D uses 'proton donor,' which is not the standard mechanistic description for ASADH's His. Option C correctly pairs the acyl-thioester intermediate function with a cysteine in the conserved PIRSR000148 motif context (CNSNC around positions 150-155). A model familiar with the ASADH family's conserved catalytic motif and mechanism can identify the catalytic Cys and match it to option C's description.",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge of the ASADH family (catalytic Cys-His dyad, thioacyl intermediate mechanism, conserved motifs, NADP-binding Rossmann fold) combined with elimination of clearly wrong distractors (wrong enzyme class in B, wrong position in A, wrong mechanistic role in D) provides a credible reasoning path to select C without needing to memorize this exact protein's UniProt entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only option C correctly pairs an ASADH active-site residue (Cys) with its proper mechanistic role (acyl-thioester intermediate). The other options contain factual errors: wrong enzyme (B), wrong position for the stated function (A), or wrong mechanistic role (D)."
  },
  "important_caveats": [
    "The UniProt annotation for position 154 is based on PIRSR pattern matching (ECO:0000255, computational), not direct experimental mutagenesis on this specific protein. However, the ASADH catalytic mechanism is well-established from structural and biochemical studies of homologs (e.g., E. coli ASADH, PDB structures).",
    "The sequence contains multiple cysteines (positions 9, 72, 73, 81, 150, 154, 243, 254, 287, 318); identifying the catalytic one requires recognizing the conserved PIRSR000148 motif context (CNSNC pattern around 150-155), which is family-level knowledge.",
    "The reviewer-only evidence confirms the UniProt accession and annotation but was not available to the evaluated model."
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
  "excerpt": "{\"description\":\"Acyl-thioester intermediate\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PIRSR000148-1\",\"source\":\"PIRSR\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":154},\"start\":{\"modifier\":\"EXACT\",\"value\":154}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
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
  "excerpt": "{\"description\":\"Proton acceptor\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PIRSR000148-1\",\"source\":\"PIRSR\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":251},\"start\":{\"modifier\":\"EXACT\",\"value\":251}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
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
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"26869335\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"4ZIC\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58349\",\"name\":\"NADP(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":15},\"start\":{\"modifier\":\"EXACT\",\"value\":15}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-02T04:23:53.783847+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bf278bc137aa3857c873dcee85929131e2e626bb23054806edb11415af48ec0e",
  "url": "https://rest.uniprot.org/uniprotkb/A0A080WMA9.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A080WMA9.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q5ALM0\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58349\",\"name\":\"NADP(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":16},\"start\":{\"modifier\":\"EXACT\",\"value\":16}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-02T04:23:53.783847+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bf278bc137aa3857c873dcee85929131e2e626bb23054806edb11415af48ec0e",
  "url": "https://rest.uniprot.org/uniprotkb/A0A080WMA9.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A080WMA9.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"A0A179UL48\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58349\",\"name\":\"NADP(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":17},\"start\":{\"modifier\":\"EXACT\",\"value\":17}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
  "retrieved_utc": "2026-11-02T04:23:53.783847+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bf278bc137aa3857c873dcee85929131e2e626bb23054806edb11415af48ec0e",
  "url": "https://rest.uniprot.org/uniprotkb/A0A080WMA9.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A080WMA9.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"A0A179UL48\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58349\",\"name\":\"NADP(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":18},\"start\":{\"modifier\":\"EXACT\",\"value\":18}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/6",
  "retrieved_utc": "2026-11-02T04:23:53.783847+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bf278bc137aa3857c873dcee85929131e2e626bb23054806edb11415af48ec0e",
  "url": "https://rest.uniprot.org/uniprotkb/A0A080WMA9.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A080WMA9.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"26869335\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"4ZIC\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58349\",\"name\":\"NADP(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":40},\"start\":{\"modifier\":\"EXACT\",\"value\":40}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/7",
  "retrieved_utc": "2026-11-02T04:23:53.783847+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bf278bc137aa3857c873dcee85929131e2e626bb23054806edb11415af48ec0e",
  "url": "https://rest.uniprot.org/uniprotkb/A0A080WMA9.json"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A080WMA9.json)

```json
{
  "evidence_id": "C12",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q5ALM0\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58349\",\"name\":\"NADP(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":43},\"start\":{\"modifier\":\"EXACT\",\"value\":43}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/8",
  "retrieved_utc": "2026-11-02T04:23:53.783847+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bf278bc137aa3857c873dcee85929131e2e626bb23054806edb11415af48ec0e",
  "url": "https://rest.uniprot.org/uniprotkb/A0A080WMA9.json"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A080WMA9.json)

```json
{
  "evidence_id": "C13",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"26869335\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"4ZIC\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58349\",\"name\":\"NADP(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":87},\"start\":{\"modifier\":\"EXACT\",\"value\":87}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/9",
  "retrieved_utc": "2026-11-02T04:23:53.783847+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bf278bc137aa3857c873dcee85929131e2e626bb23054806edb11415af48ec0e",
  "url": "https://rest.uniprot.org/uniprotkb/A0A080WMA9.json"
}
```

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A080WMA9.json)

```json
{
  "evidence_id": "C14",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"26869335\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"4ZIC\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58349\",\"name\":\"NADP(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":88},\"start\":{\"modifier\":\"EXACT\",\"value\":88}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/10",
  "retrieved_utc": "2026-11-02T04:23:53.783847+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bf278bc137aa3857c873dcee85929131e2e626bb23054806edb11415af48ec0e",
  "url": "https://rest.uniprot.org/uniprotkb/A0A080WMA9.json"
}
```

### Evidence C15

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A080WMA9.json)

```json
{
  "evidence_id": "C15",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"26869335\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"4ZIC\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58349\",\"name\":\"NADP(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":186},\"start\":{\"modifier\":\"EXACT\",\"value\":186}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/11",
  "retrieved_utc": "2026-11-02T04:23:53.783847+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bf278bc137aa3857c873dcee85929131e2e626bb23054806edb11415af48ec0e",
  "url": "https://rest.uniprot.org/uniprotkb/A0A080WMA9.json"
}
```

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A080WMA9.json)

```json
{
  "evidence_id": "C16",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"A0A179UL48\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58349\",\"name\":\"NADP(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":340},\"start\":{\"modifier\":\"EXACT\",\"value\":340}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/12",
  "retrieved_utc": "2026-11-02T04:23:53.783847+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bf278bc137aa3857c873dcee85929131e2e626bb23054806edb11415af48ec0e",
  "url": "https://rest.uniprot.org/uniprotkb/A0A080WMA9.json"
}
```

### Evidence C17

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A080WMA9.json)

```json
{
  "evidence_id": "C17",
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
  "excerpt": "FT   ACT_SITE        154\nFT                   /note=\"Acyl-thioester intermediate\"\nFT                   /evidence=\"ECO:0000255|PIRSR:PIRSR000148-1\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:23:57.418115+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 125-127",
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
  "excerpt": "FT   ACT_SITE        251\nFT                   /note=\"Proton acceptor\"\nFT                   /evidence=\"ECO:0000255|PIRSR:PIRSR000148-1\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:23:57.418115+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 128-130",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "319e2a6ea09f79026f215490dfab47119b95e8f6a8e21b934e31e170e04fc34f",
  "url": "https://rest.uniprot.org/unisave/A0A080WMA9?format=txt&versions=38"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A080WMA9?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H5",
  "excerpt": "FT   BINDING         15\nFT                   /ligand=\"NADP(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58349\"\nFT                   /evidence=\"ECO:0000269|PubMed:26869335,\nFT                   ECO:0007744|PDB:4ZIC\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:23:57.418115+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 131-135",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "319e2a6ea09f79026f215490dfab47119b95e8f6a8e21b934e31e170e04fc34f",
  "url": "https://rest.uniprot.org/unisave/A0A080WMA9?format=txt&versions=38"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A080WMA9?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H6",
  "excerpt": "FT   BINDING         16\nFT                   /ligand=\"NADP(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58349\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q5ALM0\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:23:57.418115+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 136-139",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "319e2a6ea09f79026f215490dfab47119b95e8f6a8e21b934e31e170e04fc34f",
  "url": "https://rest.uniprot.org/unisave/A0A080WMA9?format=txt&versions=38"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A080WMA9?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H7",
  "excerpt": "FT   BINDING         17\nFT                   /ligand=\"NADP(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58349\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:A0A179UL48\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:23:57.418115+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 140-143",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "319e2a6ea09f79026f215490dfab47119b95e8f6a8e21b934e31e170e04fc34f",
  "url": "https://rest.uniprot.org/unisave/A0A080WMA9?format=txt&versions=38"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A080WMA9?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H8",
  "excerpt": "FT   BINDING         18\nFT                   /ligand=\"NADP(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58349\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:A0A179UL48\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:23:57.418115+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 144-147",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "319e2a6ea09f79026f215490dfab47119b95e8f6a8e21b934e31e170e04fc34f",
  "url": "https://rest.uniprot.org/unisave/A0A080WMA9?format=txt&versions=38"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A080WMA9?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H9",
  "excerpt": "FT   BINDING         40\nFT                   /ligand=\"NADP(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58349\"\nFT                   /evidence=\"ECO:0000269|PubMed:26869335,\nFT                   ECO:0007744|PDB:4ZIC\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:23:57.418115+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 148-152",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "319e2a6ea09f79026f215490dfab47119b95e8f6a8e21b934e31e170e04fc34f",
  "url": "https://rest.uniprot.org/unisave/A0A080WMA9?format=txt&versions=38"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A080WMA9?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H10",
  "excerpt": "FT   BINDING         43\nFT                   /ligand=\"NADP(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58349\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q5ALM0\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:23:57.418115+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 153-156",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "319e2a6ea09f79026f215490dfab47119b95e8f6a8e21b934e31e170e04fc34f",
  "url": "https://rest.uniprot.org/unisave/A0A080WMA9?format=txt&versions=38"
}
```

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A080WMA9?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H11",
  "excerpt": "FT   BINDING         87\nFT                   /ligand=\"NADP(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58349\"\nFT                   /evidence=\"ECO:0000269|PubMed:26869335,\nFT                   ECO:0007744|PDB:4ZIC\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:23:57.418115+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 157-161",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "319e2a6ea09f79026f215490dfab47119b95e8f6a8e21b934e31e170e04fc34f",
  "url": "https://rest.uniprot.org/unisave/A0A080WMA9?format=txt&versions=38"
}
```

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A080WMA9?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H12",
  "excerpt": "FT   BINDING         88\nFT                   /ligand=\"NADP(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58349\"\nFT                   /evidence=\"ECO:0000269|PubMed:26869335,\nFT                   ECO:0007744|PDB:4ZIC\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:23:57.418115+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 162-166",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "319e2a6ea09f79026f215490dfab47119b95e8f6a8e21b934e31e170e04fc34f",
  "url": "https://rest.uniprot.org/unisave/A0A080WMA9?format=txt&versions=38"
}
```

### Evidence H13

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A080WMA9?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H13",
  "excerpt": "FT   BINDING         186\nFT                   /ligand=\"NADP(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58349\"\nFT                   /evidence=\"ECO:0000269|PubMed:26869335,\nFT                   ECO:0007744|PDB:4ZIC\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:23:57.418115+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 167-171",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "319e2a6ea09f79026f215490dfab47119b95e8f6a8e21b934e31e170e04fc34f",
  "url": "https://rest.uniprot.org/unisave/A0A080WMA9?format=txt&versions=38"
}
```

### Evidence H14

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A080WMA9?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H14",
  "excerpt": "FT   BINDING         340\nFT                   /ligand=\"NADP(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58349\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:A0A179UL48\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:23:57.418115+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 172-175",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "319e2a6ea09f79026f215490dfab47119b95e8f6a8e21b934e31e170e04fc34f",
  "url": "https://rest.uniprot.org/unisave/A0A080WMA9?format=txt&versions=38"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 0. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
