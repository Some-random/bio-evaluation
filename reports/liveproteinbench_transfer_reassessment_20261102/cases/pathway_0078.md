# pathway_0078

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/pathway_0078.txt)

**Task:** `pathway`  
**Expected answer:** **B** — Capsule biogenesis

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MVKKILIVFGTRPEAIKMAPLVKIMENRNDVNFRVCVTGQHRQMLDQILNIFDIKPDYDLNIMQENQDLYDITLKILCGMKNVLNDFKPNIVLVHGDTTTASVTALAAFYQKIKIAHVEAGLRTYNICNPWPEEANRQIIGVLANIHFTPTVKSAENLIKEGKNKEGIFITGNTVIDALFYMTEKIKNDKTFKIKVLSSIGNEYKINDNKKFILVTGHRRENFGEGFLQICEALKIIAINNPDIDIVYPVHLNPNVQKPVKMLLLNISNIYLINPLKYEEFIYLMSKSYFIITDSGGIQEEAPSLGKPILVMRETTERPEAVEAGVVKLVGACKQNIIRESQKLIDDQDEYEKMSKAYNPYGDGRACEKIINILIKGKNNESI

[Multiple Choices]
A. protein ubiquitination. .
B. Capsule biogenesis
C. ajmaline biosynthesis. .
D. iron-sulfur cluster biosynthesis. .
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

> The sequence-matched UniProt record identifies the protein as UDP-N-acetylglucosamine 2-epimerase and annotates its pathway as capsule biogenesis/capsule polysaccharide biosynthesis. The enzyme annotation and pathway claim cite experimental evidence (PubMed 38382015), supporting choice B.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> A knowledgeable model can recognize this 383-aa bacterial sequence as consistent with the UDP-GlcNAc 2-epimerase family. Enzymes of this family interconvert nucleotide sugars, producing a precursor used in bacterial capsule-polysaccharide synthesis. That family-level function points to capsule biogenesis (B), rather than ubiquitination, plant ajmaline biosynthesis, or iron-sulfur cluster assembly.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The offered choices are biologically distinct, and transferable sequence-family knowledge gives a meaningful basis to select capsule biogenesis without recalling this exact protein's database entry. The inference is not equivalent to experimental confirmation of this particular protein's role.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The capsule-polysaccharide pathway is the clearly best-fitting offered choice; the other options concern unrelated processes.


### Important caveats

- The reviewer-only record supports the key but was not part of the original input.
- The sequence-based family and pathway inference is probabilistic; the direct support for this protein's pathway association comes from the cited experimental annotation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A knowledgeable model can recognize this 383-aa bacterial sequence as consistent with the UDP-GlcNAc 2-epimerase family. Enzymes of this family interconvert nucleotide sugars, producing a precursor used in bacterial capsule-polysaccharide synthesis. That family-level function points to capsule biogenesis (B), rather than ubiquitination, plant ajmaline biosynthesis, or iron-sulfur cluster assembly.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The offered choices are biologically distinct, and transferable sequence-family knowledge gives a meaningful basis to select capsule biogenesis without recalling this exact protein's database entry. The inference is not equivalent to experimental confirmation of this particular protein's role."
  },
  "case_id": "pathway_0078",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record identifies the protein as UDP-N-acetylglucosamine 2-epimerase and annotates its pathway as capsule biogenesis/capsule polysaccharide biosynthesis. The enzyme annotation and pathway claim cite experimental evidence (PubMed 38382015), supporting choice B."
  },
  "important_caveats": [
    "The reviewer-only record supports the key but was not part of the original input.",
    "The sequence-based family and pathway inference is probabilistic; the direct support for this protein's pathway association comes from the cited experimental annotation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The capsule-polysaccharide pathway is the clearly best-fitting offered choice; the other options concern unrelated processes."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0078",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record identifies the protein as UDP-N-acetylglucosamine 2-epimerase and annotates its pathway as capsule biogenesis/capsule polysaccharide biosynthesis. The enzyme annotation and pathway claim cite experimental evidence (PubMed 38382015), supporting choice B.",
    "evidence_ids": ["C4", "C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "A knowledgeable model can recognize this 383-aa bacterial sequence as consistent with the UDP-GlcNAc 2-epimerase family. Enzymes of this family interconvert nucleotide sugars, producing a precursor used in bacterial capsule-polysaccharide synthesis. That family-level function points to capsule biogenesis (B), rather than ubiquitination, plant ajmaline biosynthesis, or iron-sulfur cluster assembly.",
    "missing_item_specific_fact": "",
    "reason": "The offered choices are biologically distinct, and transferable sequence-family knowledge gives a meaningful basis to select capsule biogenesis without recalling this exact protein's database entry. The inference is not equivalent to experimental confirmation of this particular protein's role."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The capsule-polysaccharide pathway is the clearly best-fitting offered choice; the other options concern unrelated processes."
  },
  "important_caveats": [
    "The reviewer-only record supports the key but was not part of the original input.",
    "The sequence-based family and pathway inference is probabilistic; the direct support for this protein's pathway association comes from the cited experimental annotation."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (A0A0U3CEN8) explicitly annotates the pathway as 'Capsule biogenesis; capsule polysaccharide biosynthesis' with experimental evidence (ECO:0000269, PubMed:38382015). The protein is UDP-N-acetylglucosamine 2-epimerase (EC 5.1.3.14), and the cited 2024 Biochemistry paper by Ghosh & Raushel directly demonstrates its role in producing UDP-ManNAc and CMP-Neu5Ac precursors for Campylobacter jejuni capsular polysaccharides. The sequence in the question matches the annotated entry exactly (SHA-256 confirmed).

Citations as saved: [C5](#evidence-c5), [C4](#evidence-c4), [C6](#evidence-c6), [H3](#evidence-h3), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence (~383 aa) displays characteristic Rossmann-fold NAD(P)-binding motifs (e.g., 'VTGQHRQ' and 'VTGHRRE' patterns) that are hallmarks of the UDP-sugar 2-epimerase / GalE-like family. This family is well-known from E. coli GalE, Neisseria, and other bacterial systems to function in sugar-nucleotide metabolism feeding into surface polysaccharide (capsule, LPS, exopolysaccharide) biosynthesis. Among the four options: (A) Protein ubiquitination involves E1/E2/E3 enzymes with UBC (~150 aa), RING, or HECT domains—none present here. (C) Ajmaline biosynthesis is a plant (Rauwolfia) alkaloid pathway relying on tryptophan decarboxylase, strictosidine synthase, and P450s—structurally and taxonomically incompatible with this prokaryotic NAD-dependent epimerase. (D) Iron-sulfur cluster biosynthesis involves cysteine desulfurases (PLP-dependent IscS), scaffold proteins (IscU), and Fe-S transfer proteins with entirely different folds. The Rossmann-fold epimerase architecture specifically points to sugar-nucleotide interconversion, which among the offered choices maps uniquely to capsule biogenesis (B).


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A model recognizing the NAD-binding Rossmann-fold motifs and the UDP-sugar 2-epimerase family from training on E. coli GalE, Neisseria CneA, and other homologs can connect this enzyme class to bacterial surface polysaccharide/capsule biosynthesis. The three distractors (ubiquitination, plant alkaloid biosynthesis, Fe-S cluster assembly) involve structurally and mechanistically unrelated protein families, making them distinguishable by family-level inference without needing the specific Campylobacter annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices span fundamentally different pathway types (ubiquitin-proteasome, bacterial capsule, plant alkaloid, Fe-S cluster assembly). The Rossmann-fold NAD-dependent epimerase motifs are incompatible with the domain architectures of all three distractors, leaving only capsule biogenesis as a consistent assignment.


### Important caveats

- The UniProt pathway annotation is backed by experimental evidence (ECO:0000269), not merely computational transfer, strengthening the key.
- The specific assignment to 'Capsule biogenesis' rather than a broader 'sugar nucleotide metabolism' label depends on knowing that in Campylobacter this epimerase feeds capsule polysaccharide precursors; however, among the four offered choices, capsule biogenesis is the only sugar-nucleotide-related pathway, so the family-level inference suffices.
- The reviewer-only evidence confirms sequence identity (SHA-256 match) and that the pathway annotation predates the benchmark cutoff (entry version 19, released Jan 2026).

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence (~383 aa) displays characteristic Rossmann-fold NAD(P)-binding motifs (e.g., 'VTGQHRQ' and 'VTGHRRE' patterns) that are hallmarks of the UDP-sugar 2-epimerase / GalE-like family. This family is well-known from E. coli GalE, Neisseria, and other bacterial systems to function in sugar-nucleotide metabolism feeding into surface polysaccharide (capsule, LPS, exopolysaccharide) biosynthesis. Among the four options: (A) Protein ubiquitination involves E1/E2/E3 enzymes with UBC (~150 aa), RING, or HECT domains—none present here. (C) Ajmaline biosynthesis is a plant (Rauwolfia) alkaloid pathway relying on tryptophan decarboxylase, strictosidine synthase, and P450s—structurally and taxonomically incompatible with this prokaryotic NAD-dependent epimerase. (D) Iron-sulfur cluster biosynthesis involves cysteine desulfurases (PLP-dependent IscS), scaffold proteins (IscU), and Fe-S transfer proteins with entirely different folds. The Rossmann-fold epimerase architecture specifically points to sugar-nucleotide interconversion, which among the offered choices maps uniquely to capsule biogenesis (B).",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A model recognizing the NAD-binding Rossmann-fold motifs and the UDP-sugar 2-epimerase family from training on E. coli GalE, Neisseria CneA, and other homologs can connect this enzyme class to bacterial surface polysaccharide/capsule biosynthesis. The three distractors (ubiquitination, plant alkaloid biosynthesis, Fe-S cluster assembly) involve structurally and mechanistically unrelated protein families, making them distinguishable by family-level inference without needing the specific Campylobacter annotation."
  },
  "case_id": "pathway_0078",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C4",
      "C6",
      "H3",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (A0A0U3CEN8) explicitly annotates the pathway as 'Capsule biogenesis; capsule polysaccharide biosynthesis' with experimental evidence (ECO:0000269, PubMed:38382015). The protein is UDP-N-acetylglucosamine 2-epimerase (EC 5.1.3.14), and the cited 2024 Biochemistry paper by Ghosh & Raushel directly demonstrates its role in producing UDP-ManNAc and CMP-Neu5Ac precursors for Campylobacter jejuni capsular polysaccharides. The sequence in the question matches the annotated entry exactly (SHA-256 confirmed)."
  },
  "important_caveats": [
    "The UniProt pathway annotation is backed by experimental evidence (ECO:0000269), not merely computational transfer, strengthening the key.",
    "The specific assignment to 'Capsule biogenesis' rather than a broader 'sugar nucleotide metabolism' label depends on knowing that in Campylobacter this epimerase feeds capsule polysaccharide precursors; however, among the four offered choices, capsule biogenesis is the only sugar-nucleotide-related pathway, so the family-level inference suffices.",
    "The reviewer-only evidence confirms sequence identity (SHA-256 match) and that the pathway annotation predates the benchmark cutoff (entry version 19, released Jan 2026)."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices span fundamentally different pathway types (ubiquitin-proteasome, bacterial capsule, plant alkaloid, Fe-S cluster assembly). The Rossmann-fold NAD-dependent epimerase motifs are incompatible with the domain architectures of all three distractors, leaving only capsule biogenesis as a consistent assignment."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0078",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (A0A0U3CEN8) explicitly annotates the pathway as 'Capsule biogenesis; capsule polysaccharide biosynthesis' with experimental evidence (ECO:0000269, PubMed:38382015). The protein is UDP-N-acetylglucosamine 2-epimerase (EC 5.1.3.14), and the cited 2024 Biochemistry paper by Ghosh & Raushel directly demonstrates its role in producing UDP-ManNAc and CMP-Neu5Ac precursors for Campylobacter jejuni capsular polysaccharides. The sequence in the question matches the annotated entry exactly (SHA-256 confirmed).",
    "evidence_ids": ["C5", "C4", "C6", "H3", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence (~383 aa) displays characteristic Rossmann-fold NAD(P)-binding motifs (e.g., 'VTGQHRQ' and 'VTGHRRE' patterns) that are hallmarks of the UDP-sugar 2-epimerase / GalE-like family. This family is well-known from E. coli GalE, Neisseria, and other bacterial systems to function in sugar-nucleotide metabolism feeding into surface polysaccharide (capsule, LPS, exopolysaccharide) biosynthesis. Among the four options: (A) Protein ubiquitination involves E1/E2/E3 enzymes with UBC (~150 aa), RING, or HECT domains—none present here. (C) Ajmaline biosynthesis is a plant (Rauwolfia) alkaloid pathway relying on tryptophan decarboxylase, strictosidine synthase, and P450s—structurally and taxonomically incompatible with this prokaryotic NAD-dependent epimerase. (D) Iron-sulfur cluster biosynthesis involves cysteine desulfurases (PLP-dependent IscS), scaffold proteins (IscU), and Fe-S transfer proteins with entirely different folds. The Rossmann-fold epimerase architecture specifically points to sugar-nucleotide interconversion, which among the offered choices maps uniquely to capsule biogenesis (B).",
    "missing_item_specific_fact": "",
    "reason": "A model recognizing the NAD-binding Rossmann-fold motifs and the UDP-sugar 2-epimerase family from training on E. coli GalE, Neisseria CneA, and other homologs can connect this enzyme class to bacterial surface polysaccharide/capsule biosynthesis. The three distractors (ubiquitination, plant alkaloid biosynthesis, Fe-S cluster assembly) involve structurally and mechanistically unrelated protein families, making them distinguishable by family-level inference without needing the specific Campylobacter annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices span fundamentally different pathway types (ubiquitin-proteasome, bacterial capsule, plant alkaloid, Fe-S cluster assembly). The Rossmann-fold NAD-dependent epimerase motifs are incompatible with the domain architectures of all three distractors, leaving only capsule biogenesis as a consistent assignment."
  },
  "important_caveats": [
    "The UniProt pathway annotation is backed by experimental evidence (ECO:0000269), not merely computational transfer, strengthening the key.",
    "The specific assignment to 'Capsule biogenesis' rather than a broader 'sugar nucleotide metabolism' label depends on knowing that in Campylobacter this epimerase feeds capsule polysaccharide precursors; however, among the four offered choices, capsule biogenesis is the only sugar-nucleotide-related pathway, so the family-level inference suffices.",
    "The reviewer-only evidence confirms sequence identity (SHA-256 match) and that the pathway annotation predates the benchmark cutoff (entry version 19, released Jan 2026)."
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
  "benchmark_sequence_length": 383,
  "benchmark_sequence_sha256": "ddbc20d90a4cb51741fc357432ae609ce704ff3086e52fc8f54e4db1b9cd9037",
  "current_entry_audit": {
    "entryVersion": 21,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2016-03-16",
    "sequenceVersion": 1
  },
  "current_record_sha256": "79cec39f8af13d58c2f3eacbeec9904c65a82d2ceedf2c1bacc9916abbc9faf0",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 383,
  "current_source_sequence_sha256": "ddbc20d90a4cb51741fc357432ae609ce704ff3086e52fc8f54e4db1b9cd9037",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 19,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A0U3CEN8",
  "selected_historical_entry_version": 19,
  "selected_historical_record_sha256": "ab154b9f6d4f7d6da6b610c345b588d7236e7842a8415b0bb9cb9fac2fce5141",
  "selected_historical_source_sequence_length": 383,
  "selected_historical_source_sequence_sha256": "ddbc20d90a4cb51741fc357432ae609ce704ff3086e52fc8f54e4db1b9cd9037",
  "selected_historical_version": {
    "accession": "A0A0U3CEN8",
    "database": "Swiss-Prot",
    "entryVersion": 19,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "UAGEP_CAMJU",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3CEN8.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A0U3CEN8\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:24:21.799773+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "79cec39f8af13d58c2f3eacbeec9904c65a82d2ceedf2c1bacc9916abbc9faf0",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0U3CEN8.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3CEN8.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":21,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2016-03-16\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:24:21.799773+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "79cec39f8af13d58c2f3eacbeec9904c65a82d2ceedf2c1bacc9916abbc9faf0",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0U3CEN8.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3CEN8.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Campylobacterota\",\"Epsilonproteobacteria\",\"Campylobacterales\",\"Campylobacteraceae\",\"Campylobacter\"],\"scientificName\":\"Campylobacter jejuni\",\"taxonId\":197}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:24:21.799773+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "79cec39f8af13d58c2f3eacbeec9904c65a82d2ceedf2c1bacc9916abbc9faf0",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0U3CEN8.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3CEN8.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38382015\",\"source\":\"PubMed\"}],\"value\":\"Non-hydrolyzing UDP-GlcNAc 2-epimerase\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38382015\",\"source\":\"PubMed\"}],\"value\":\"5.1.3.14\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"UDP-N-acetylglucosamine 2-epimerase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:24:21.799773+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "79cec39f8af13d58c2f3eacbeec9904c65a82d2ceedf2c1bacc9916abbc9faf0",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0U3CEN8.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3CEN8.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38382015\",\"source\":\"PubMed\"}],\"value\":\"Capsule biogenesis; capsule polysaccharide biosynthesis\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-02T04:24:21.799773+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "79cec39f8af13d58c2f3eacbeec9904c65a82d2ceedf2c1bacc9916abbc9faf0",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0U3CEN8.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3CEN8.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Ghosh M.K.\",\"Raushel F.M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38382015\"},{\"database\":\"DOI\",\"id\":\"10.1021/acs.biochem.3c00664\"}],\"citationType\":\"journal article\",\"firstPage\":\"688\",\"id\":\"38382015\",\"journal\":\"Biochemistry\",\"lastPage\":\"698\",\"publicationDate\":\"2024\",\"title\":\"Biosynthesis of UDP-alpha-N-Acetyl-d-mannosaminuronic Acid and CMP-beta-N-Acetyl-d-neuraminic Acid for the Capsular Polysaccharides of Campylobacter jejuni.\",\"volume\":\"63\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"HS:11\"}],\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-02T04:24:21.799773+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "79cec39f8af13d58c2f3eacbeec9904c65a82d2ceedf2c1bacc9916abbc9faf0",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0U3CEN8.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0U3CEN8?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H1",
  "excerpt": "ID   UAGEP_CAMJU             Reviewed;         383 AA.\nAC   A0A0U3CEN8;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   16-MAR-2016, sequence version 1.\nDT   28-JAN-2026, entry version 19.\nDE   RecName: Full=UDP-N-acetylglucosamine 2-epimerase {ECO:0000305};\nDE            EC=5.1.3.14 {ECO:0000269|PubMed:38382015};\nDE   AltName: Full=Non-hydrolyzing UDP-GlcNAc 2-epimerase {ECO:0000303|PubMed:38382015};\nGN   Name=HS11.17 {ECO:0000303|PubMed:38382015};\nOS   Campylobacter jejuni.\nOC   Bacteria; Pseudomonadati; Campylobacterota; Epsilonproteobacteria;\nOC   Campylobacterales; Campylobacteraceae; Campylobacter.\nOX   NCBI_TaxID=197;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:23.855684+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ab154b9f6d4f7d6da6b610c345b588d7236e7842a8415b0bb9cb9fac2fce5141",
  "url": "https://rest.uniprot.org/unisave/A0A0U3CEN8?format=txt&versions=19"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0U3CEN8?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H2",
  "excerpt": "RN   [3]\nRP   FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, AND PATHWAY.\nRC   STRAIN=HS:11;\nRX   PubMed=38382015; DOI=10.1021/acs.biochem.3c00664;\nRA   Ghosh M.K., Raushel F.M.;\nRT   \"Biosynthesis of UDP-alpha-N-Acetyl-d-mannosaminuronic Acid and CMP-beta-N-\nRT   Acetyl-d-neuraminic Acid for the Capsular Polysaccharides of Campylobacter\nRT   jejuni.\";\nRL   Biochemistry 63:688-698(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:23.855684+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 29-37",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ab154b9f6d4f7d6da6b610c345b588d7236e7842a8415b0bb9cb9fac2fce5141",
  "url": "https://rest.uniprot.org/unisave/A0A0U3CEN8?format=txt&versions=19"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0U3CEN8?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H3",
  "excerpt": "CC   -!- PATHWAY: Capsule biogenesis; capsule polysaccharide biosynthesis.\nCC       {ECO:0000269|PubMed:38382015}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:23.855684+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 54-55",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ab154b9f6d4f7d6da6b610c345b588d7236e7842a8415b0bb9cb9fac2fce5141",
  "url": "https://rest.uniprot.org/unisave/A0A0U3CEN8?format=txt&versions=19"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 78. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
