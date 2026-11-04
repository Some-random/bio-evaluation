# EC_number_0156

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0156.txt)

**Task:** `EC_number`  
**Expected answer:** **B** — 7.6.2.2

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MNTQPTRAIETSGLVKVYNGTRAVDGLDLDVPAGLVYGILGPNGAGKSTTIRMLATLLRPDGGTARVFGHDVTSEPDTVRRRISVTGQYASVDEGLTGTENLVMMGRLQGYSWARARERAAELIDGFGLGDARDRLLKTYSGGMRRRLDIAASIVVTPDLLFLDEPTTGLDPRSRNQVWDIVRALVDAGTTVLLTTQYLDEADQLADRIAVIDHGRVIAEGTTGELKSSLGSNVLRLRLHDAQSRAEAERLLSAELGVTIHRDSDPTALSARIDDPRQGMRALAELSRTQLEVRSFSLGQSSLDEVFLALTGHPADDRSTEEAAEEEKVA

[Multiple Choices]
A. 6.3.5.1
B. 7.6.2.2
C. 2.3.1.319
D. 4.3.1.12
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzyme Commission (EC) Number Prediction, which is to predict the complete 4-digit Enzyme Commission (EC) number for a given protein. The EC number is a numerical classification that categorizes enzymes based on the chemical reactions they catalyze. You should select the most accurate EC number from the provided options based on the protein's sequence.. The inputs provided by the user for this task include:

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

> The sequence-matched UniProt record assigns EC 7.6.2.2 and specifies daunorubicin efflux, with a cited reaction annotation. This supports the key as a curated functional assignment; the excerpts do not independently establish the underlying experimental evidence.

Citations as saved: [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a clear ABC-type nucleotide-binding signature, including the P-loop motif GPNGAGKST, and is characteristic of an ABC transporter ATP-binding component. Among the choices, B is the transport-associated ATPase EC option; the other choices classify different reaction types.


**Missing item-specific fact**

> The sequence alone does not establish the transported substrate, which would be needed to independently verify the substrate-specific EC assignment; that detail is not necessary to distinguish B from these alternatives.


**Reason**

> Transferable ABC-transporter family knowledge meaningfully favors B over the offered ligase, transferase, and lyase alternatives. The sequence supports the transporter ATPase class, though it does not by itself identify daunorubicin as the substrate.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only B matches the recognizable ABC transporter ATPase function among the offered options.


### Important caveats

- The reviewer-only sequence-matched record supports the EC annotation, but the excerpts provide a curated assignment citing a paper rather than independent evaluation of the underlying experiments.
- The specific transported substrate is not established by the sequence motifs alone.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a clear ABC-type nucleotide-binding signature, including the P-loop motif GPNGAGKST, and is characteristic of an ABC transporter ATP-binding component. Among the choices, B is the transport-associated ATPase EC option; the other choices classify different reaction types.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The sequence alone does not establish the transported substrate, which would be needed to independently verify the substrate-specific EC assignment; that detail is not necessary to distinguish B from these alternatives.",
    "reason": "Transferable ABC-transporter family knowledge meaningfully favors B over the offered ligase, transferase, and lyase alternatives. The sequence supports the transporter ATPase class, though it does not by itself identify daunorubicin as the substrate."
  },
  "case_id": "EC_number_0156",
  "expected_answer_check": {
    "evidence_ids": [
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns EC 7.6.2.2 and specifies daunorubicin efflux, with a cited reaction annotation. This supports the key as a curated functional assignment; the excerpts do not independently establish the underlying experimental evidence."
  },
  "important_caveats": [
    "The reviewer-only sequence-matched record supports the EC annotation, but the excerpts provide a curated assignment citing a paper rather than independent evaluation of the underlying experiments.",
    "The specific transported substrate is not established by the sequence motifs alone."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only B matches the recognizable ABC transporter ATPase function among the offered options."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0156",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns EC 7.6.2.2 and specifies daunorubicin efflux, with a cited reaction annotation. This supports the key as a curated functional assignment; the excerpts do not independently establish the underlying experimental evidence.",
    "evidence_ids": ["H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a clear ABC-type nucleotide-binding signature, including the P-loop motif GPNGAGKST, and is characteristic of an ABC transporter ATP-binding component. Among the choices, B is the transport-associated ATPase EC option; the other choices classify different reaction types.",
    "missing_item_specific_fact": "The sequence alone does not establish the transported substrate, which would be needed to independently verify the substrate-specific EC assignment; that detail is not necessary to distinguish B from these alternatives.",
    "reason": "Transferable ABC-transporter family knowledge meaningfully favors B over the offered ligase, transferase, and lyase alternatives. The sequence supports the transporter ATPase class, though it does not by itself identify daunorubicin as the substrate."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only B matches the recognizable ABC transporter ATPase function among the offered options."
  },
  "important_caveats": [
    "The reviewer-only sequence-matched record supports the EC annotation, but the excerpts provide a curated assignment citing a paper rather than independent evaluation of the underlying experiments.",
    "The specific transported substrate is not established by the sequence motifs alone."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry P0DXG8 (DrrA1, Streptomyces coeruleorubidus) is annotated as EC 7.6.2.2 with evidence code ECO:0000305 (inferred by similarity) citing PubMed:39375957 (2024). The catalytic activity is described as daunorubicin(in) + ATP + H2O = daunorubicin(out) + ADP + phosphate + H(+), consistent with an ATP-driven translocase. The annotation is a similarity-based inference supported by functional context (ABC transporter in daunorubicin efflux), not direct experimental EC determination, but the database record clearly supports the key.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a clear Walker A motif (GPNGAGKST, residues ~30-38) and partial ABC signature motif elements (LDEPT, SDPT) characteristic of the nucleotide-binding domain (NBD) of an ABC transporter. These motifs are diagnostic of ATP-driven translocases (EC class 7). Glutamine synthetase (6.3.5.1, ligase), acyltransferase (2.3.1.319, transferase), and lyase (4.3.1.12) do not possess Walker A or ABC signature motifs and catalyze fundamentally different reaction types (ligation, group transfer, elimination). A model recognizing the Walker A + ABC signature combination can confidently assign EC class 7 (translocase) and exclude classes 6, 2, and 4. Since only one EC 7 option is offered, the family-level ABC transporter signature is sufficient to select B.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The Walker A motif (GxxGxGKS/T pattern: GPNGAGKST) and ABC signature (LDEPT/SDPT elements) are well-known, transferable sequence features of ABC transporter NBDs learned from many homologous proteins. Their presence eliminates all non-translocase options. The overall ~220-residue NBD domain architecture further supports ABC transporter assignment. No target-specific annotation is needed beyond recognizing these conserved motifs.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options span four different EC top-level classes (6, 7, 2, 4). The Walker A and ABC signature motifs unambiguously indicate an ATP-driven translocase, making only option B (EC 7) compatible. No other option is defensible given the sequence features.


### Important caveats

- The UniProt EC annotation uses evidence code ECO:0000305 (inferred by similarity) rather than direct experimental EC characterization, though the 2024 functional study (PubMed:39375957) provides supporting context.
- The protein is the NBD (ATP-binding domain) of an ABC transporter half; the full functional pump requires a transmembrane partner, but the EC assignment applies to the NBD as the catalytic ATPase component.
- The sequence is 330 residues, consistent with a single NBD domain (~220-250 aa) plus flanking regions, typical of standalone ABC NBDs in prokaryotes.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a clear Walker A motif (GPNGAGKST, residues ~30-38) and partial ABC signature motif elements (LDEPT, SDPT) characteristic of the nucleotide-binding domain (NBD) of an ABC transporter. These motifs are diagnostic of ATP-driven translocases (EC class 7). Glutamine synthetase (6.3.5.1, ligase), acyltransferase (2.3.1.319, transferase), and lyase (4.3.1.12) do not possess Walker A or ABC signature motifs and catalyze fundamentally different reaction types (ligation, group transfer, elimination). A model recognizing the Walker A + ABC signature combination can confidently assign EC class 7 (translocase) and exclude classes 6, 2, and 4. Since only one EC 7 option is offered, the family-level ABC transporter signature is sufficient to select B.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The Walker A motif (GxxGxGKS/T pattern: GPNGAGKST) and ABC signature (LDEPT/SDPT elements) are well-known, transferable sequence features of ABC transporter NBDs learned from many homologous proteins. Their presence eliminates all non-translocase options. The overall ~220-residue NBD domain architecture further supports ABC transporter assignment. No target-specific annotation is needed beyond recognizing these conserved motifs."
  },
  "case_id": "EC_number_0156",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry P0DXG8 (DrrA1, Streptomyces coeruleorubidus) is annotated as EC 7.6.2.2 with evidence code ECO:0000305 (inferred by similarity) citing PubMed:39375957 (2024). The catalytic activity is described as daunorubicin(in) + ATP + H2O = daunorubicin(out) + ADP + phosphate + H(+), consistent with an ATP-driven translocase. The annotation is a similarity-based inference supported by functional context (ABC transporter in daunorubicin efflux), not direct experimental EC determination, but the database record clearly supports the key."
  },
  "important_caveats": [
    "The UniProt EC annotation uses evidence code ECO:0000305 (inferred by similarity) rather than direct experimental EC characterization, though the 2024 functional study (PubMed:39375957) provides supporting context.",
    "The protein is the NBD (ATP-binding domain) of an ABC transporter half; the full functional pump requires a transmembrane partner, but the EC assignment applies to the NBD as the catalytic ATPase component.",
    "The sequence is 330 residues, consistent with a single NBD domain (~220-250 aa) plus flanking regions, typical of standalone ABC NBDs in prokaryotes."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span four different EC top-level classes (6, 7, 2, 4). The Walker A and ABC signature motifs unambiguously indicate an ATP-driven translocase, making only option B (EC 7) compatible. No other option is defensible given the sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0156",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry P0DXG8 (DrrA1, Streptomyces coeruleorubidus) is annotated as EC 7.6.2.2 with evidence code ECO:0000305 (inferred by similarity) citing PubMed:39375957 (2024). The catalytic activity is described as daunorubicin(in) + ATP + H2O = daunorubicin(out) + ADP + phosphate + H(+), consistent with an ATP-driven translocase. The annotation is a similarity-based inference supported by functional context (ABC transporter in daunorubicin efflux), not direct experimental EC determination, but the database record clearly supports the key.",
    "evidence_ids": ["C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a clear Walker A motif (GPNGAGKST, residues ~30-38) and partial ABC signature motif elements (LDEPT, SDPT) characteristic of the nucleotide-binding domain (NBD) of an ABC transporter. These motifs are diagnostic of ATP-driven translocases (EC class 7). Glutamine synthetase (6.3.5.1, ligase), acyltransferase (2.3.1.319, transferase), and lyase (4.3.1.12) do not possess Walker A or ABC signature motifs and catalyze fundamentally different reaction types (ligation, group transfer, elimination). A model recognizing the Walker A + ABC signature combination can confidently assign EC class 7 (translocase) and exclude classes 6, 2, and 4. Since only one EC 7 option is offered, the family-level ABC transporter signature is sufficient to select B.",
    "missing_item_specific_fact": "",
    "reason": "The Walker A motif (GxxGxGKS/T pattern: GPNGAGKST) and ABC signature (LDEPT/SDPT elements) are well-known, transferable sequence features of ABC transporter NBDs learned from many homologous proteins. Their presence eliminates all non-translocase options. The overall ~220-residue NBD domain architecture further supports ABC transporter assignment. No target-specific annotation is needed beyond recognizing these conserved motifs."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span four different EC top-level classes (6, 7, 2, 4). The Walker A and ABC signature motifs unambiguously indicate an ATP-driven translocase, making only option B (EC 7) compatible. No other option is defensible given the sequence features."
  },
  "important_caveats": [
    "The UniProt EC annotation uses evidence code ECO:0000305 (inferred by similarity) rather than direct experimental EC characterization, though the 2024 functional study (PubMed:39375957) provides supporting context.",
    "The protein is the NBD (ATP-binding domain) of an ABC transporter half; the full functional pump requires a transmembrane partner, but the EC assignment applies to the NBD as the catalytic ATPase component.",
    "The sequence is 330 residues, consistent with a single NBD domain (~220-250 aa) plus flanking regions, typical of standalone ABC NBDs in prokaryotes."
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
  "benchmark_sequence_length": 330,
  "benchmark_sequence_sha256": "ad2ea907ea45035c9658ce71d6525af775e5e2cb247a1245bff85cb9dce29966",
  "current_entry_audit": {
    "entryVersion": 6,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-02-05",
    "sequenceVersion": 1
  },
  "current_record_sha256": "0e5348463258976e6d6f9f2134ee55b830704023f416fa44d5c29fba2af0d8f5",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 330,
  "current_source_sequence_sha256": "ad2ea907ea45035c9658ce71d6525af775e5e2cb247a1245bff85cb9dce29966",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 4,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "P0DXG8",
  "selected_historical_entry_version": 4,
  "selected_historical_record_sha256": "f95705e32d82541861abe2d430aded67e4107ac1e85c235ef22767620ec1e111",
  "selected_historical_source_sequence_length": 330,
  "selected_historical_source_sequence_sha256": "ad2ea907ea45035c9658ce71d6525af775e5e2cb247a1245bff85cb9dce29966",
  "selected_historical_version": {
    "accession": "P0DXG8",
    "database": "Swiss-Prot",
    "entryVersion": 4,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "DRRA1_STRC4",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXG8.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"P0DXG8\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:29:26.942110+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0e5348463258976e6d6f9f2134ee55b830704023f416fa44d5c29fba2af0d8f5",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXG8.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXG8.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":6,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-02-05\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:29:26.942110+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0e5348463258976e6d6f9f2134ee55b830704023f416fa44d5c29fba2af0d8f5",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXG8.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXG8.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Bacillati\",\"Actinomycetota\",\"Actinomycetes\",\"Kitasatosporales\",\"Streptomycetaceae\",\"Streptomyces\"],\"scientificName\":\"Streptomyces coeruleorubidus\",\"taxonId\":116188}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:29:26.942110+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0e5348463258976e6d6f9f2134ee55b830704023f416fa44d5c29fba2af0d8f5",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXG8.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXG8.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"39375957\",\"source\":\"PubMed\"}],\"value\":\"7.6.2.2\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Daunorubicin resistance ATP-binding protein DrrA1\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:29:26.942110+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0e5348463258976e6d6f9f2134ee55b830704023f416fa44d5c29fba2af0d8f5",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXG8.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXG8.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"39375957\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:33148\"}}],\"reaction\":{\"ecNumber\":\"7.6.2.2\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"39375957\",\"source\":\"PubMed\"}],\"name\":\"daunorubicin(in) + ATP + H2O = daunorubicin(out) + ADP + phosphate + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:33147\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:30616\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:43474\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:64677\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:456216\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:29:26.942110+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0e5348463258976e6d6f9f2134ee55b830704023f416fa44d5c29fba2af0d8f5",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXG8.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXG8.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Dong J.\",\"Ning J.\",\"Tian Y.\",\"Li H.\",\"Chen H.\",\"Guan W.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39375957\"},{\"database\":\"DOI\",\"id\":\"10.1111/1751-7915.70023\"}],\"citationType\":\"journal article\",\"firstPage\":\"e70023\",\"id\":\"39375957\",\"journal\":\"Microb. Biotechnol.\",\"lastPage\":\"e70023\",\"publicationDate\":\"2024\",\"title\":\"The involvement of multiple ABC transporters in daunorubicin efflux in Streptomyces coeruleorubidus.\",\"volume\":\"17\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION IN DAUNORUBICIN EFFLUX\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:29:26.942110+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0e5348463258976e6d6f9f2134ee55b830704023f416fa44d5c29fba2af0d8f5",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXG8.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXG8?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H1",
  "excerpt": "ID   DRRA1_STRC4             Reviewed;         330 AA.\nAC   P0DXG8;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-FEB-2025, sequence version 1.\nDT   28-JAN-2026, entry version 4.\nDE   RecName: Full=Daunorubicin resistance ATP-binding protein DrrA1 {ECO:0000305};\nDE            EC=7.6.2.2 {ECO:0000305|PubMed:39375957};\nGN   Name=drrA1 {ECO:0000303|PubMed:39375957};\nGN   Synonyms=drrA {ECO:0000312|EMBL:WOT33550.1};\nGN   ORFNames=R5U08_05025 {ECO:0000312|EMBL:WOT33550.1};\nOS   Streptomyces coeruleorubidus.\nOC   Bacteria; Bacillati; Actinomycetota; Actinomycetes; Kitasatosporales;\nOC   Streptomycetaceae; Streptomyces.\nOX   NCBI_TaxID=116188;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:29.046585+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f95705e32d82541861abe2d430aded67e4107ac1e85c235ef22767620ec1e111",
  "url": "https://rest.uniprot.org/unisave/P0DXG8?format=txt&versions=4"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXG8?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Daunorubicin resistance ATP-binding protein DrrA1 {ECO:0000305};\nDE            EC=7.6.2.2 {ECO:0000305|PubMed:39375957};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:29.046585+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-7",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f95705e32d82541861abe2d430aded67e4107ac1e85c235ef22767620ec1e111",
  "url": "https://rest.uniprot.org/unisave/P0DXG8?format=txt&versions=4"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXG8?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H3",
  "excerpt": "RN   [2]\nRP   FUNCTION IN DAUNORUBICIN EFFLUX, AND DISRUPTION PHENOTYPE.\nRX   PubMed=39375957; DOI=10.1111/1751-7915.70023;\nRA   Dong J., Ning J., Tian Y., Li H., Chen H., Guan W.;\nRT   \"The involvement of multiple ABC transporters in daunorubicin efflux in\nRT   Streptomyces coeruleorubidus.\";\nRL   Microb. Biotechnol. 17:e70023-e70023(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:29.046585+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 20-26",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f95705e32d82541861abe2d430aded67e4107ac1e85c235ef22767620ec1e111",
  "url": "https://rest.uniprot.org/unisave/P0DXG8?format=txt&versions=4"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXG8?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=daunorubicin(in) + ATP + H2O = daunorubicin(out) + ADP +\nCC         phosphate + H(+); Xref=Rhea:RHEA:33147, ChEBI:CHEBI:15377,\nCC         ChEBI:CHEBI:15378, ChEBI:CHEBI:30616, ChEBI:CHEBI:43474,\nCC         ChEBI:CHEBI:64677, ChEBI:CHEBI:456216; EC=7.6.2.2;\nCC         Evidence={ECO:0000305|PubMed:39375957};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:33148;\nCC         Evidence={ECO:0000305|PubMed:39375957};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:29.046585+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 32-39",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f95705e32d82541861abe2d430aded67e4107ac1e85c235ef22767620ec1e111",
  "url": "https://rest.uniprot.org/unisave/P0DXG8?format=txt&versions=4"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 156. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
