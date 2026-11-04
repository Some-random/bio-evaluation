# cofactor_0157

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/cofactor_0157.txt)

**Task:** `cofactor`  
**Expected answer:** **C** — Mg(2+)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | Unusable review | Unusable review |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MPAATDLANAWFAKRGWKPFAFQRRVWAAVERGESGLLHASTGAGKTYAVWLAALRAFKPRPQGRHLAPIQVLWVTPMRALAADTARALQAPLDELQLPWSVGVRSGDTNSAERARQARRLPSVLITTPESLTLLLTRAKAREDFATLQLVVVDEWHELLGNKRGVQLQLALARLRHWHPGLPTWGLSATLGNLQHARDVLLPQGGLLVQGRQDKALQVDTLLPKAIERFPWAGHMGLKMLDQVCHEIDASASSLVFTNTRAQAEIWYQALLEARPDWAGLIALHHASLARDTRDWVERSLKQGSLKAVICTSSLDLGVDFLPVERVLQIGSAKGIARLMQRAGRSGHAPGRRSRVTLVPTHSLELVEAAAARQALLAGHIEARFSPRLCMDVLVQHLVSMALGSGFRPEQLLAEVRSTWAFRQLRDSQWQWALDFVCHGGSSLTAYPDYQRVERQADGVYRVTSERLARRHRMGIGTIVSDANLQLKYWSKGGGGKTLGSVEEAFIARLRPGDTLVFAGRVLELVRVENMTAYVRRSTARKAAVARWNGGRMPLSSELADALVEQLDAAAHERFEGPEMRAVRPLLALQAQWSALPTTSTLLAETFKSRQGWHLFLYPFAGRMANLGLANLIAWRVSRAQPLSVSIAVNDYGFELLSPAQVDWASHLPQALGTADLLEDVLASLNAGEMALRRFREIAQIAGLVFGGYPAAQKSTRQIQASSGLFYEVFRKHDAGNLLLGQARDEVLSEELEIERLHRQLLKMSELQLDLQALRRPGPLAFALLVEGMRETLSTEKLADRIARMVAELEQAANAG

[Multiple Choices]
A. FAD
B. Fe(2+)
C. Mg(2+)
D. Mn(2+)
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Predicting Protein Cofactor, which is to identify the specific cofactor required for a given protein's catalytic activity. A cofactor is a non-protein chemical compound or metallic ion that is essential for an enzyme's function. Based on the provided protein sequence, you will need to determine which of the multiple-choice options is the correct cofactor.. The inputs provided by the user for this task include:

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

> The sequence-matched UniProt annotation reports Mg(2+) as the cofactor, citing a publication, and states that the ssDNA-stimulated ATPase is most active with Mg(2+) or Ca(2+); Mn(2+) stimulates only at low concentrations. Thus Mg(2+) is supported among the offered choices.

Citations as saved: [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with an ATP-dependent helicase/ATPase, including a glycine-rich Lys/Thr-containing nucleotide-binding motif. Transferable knowledge of ATPases strongly favors Mg(2+): Mg commonly coordinates ATP phosphates and supports ATP hydrolysis. That distinguishes Mg(2+) from FAD and Fe(2+), and makes it a better choice than Mn(2+), which is not the usual primary ATPase cofactor.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The exact enzyme's relative activity with different ions is protein-specific, but it is not necessary to distinguish these options: the general ATPase–Mg(2+) relationship provides a credible basis for the keyed choice. This is a probabilistic inference, not proof of the assay result.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Ca(2+) is also reported to support high activity, but it is not offered. The evidence describes Mn(2+) as stimulating only at low concentrations, which does not make it equally defensible as the primary cofactor choice.


### Important caveats

- The supplied evidence is a curated annotation citing experimental work; the underlying paper was not independently reviewed here.
- The evidence indicates Mg(2+) or Ca(2+) can give the highest activity, so the choice of Mg(2+) is relative to the options provided.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with an ATP-dependent helicase/ATPase, including a glycine-rich Lys/Thr-containing nucleotide-binding motif. Transferable knowledge of ATPases strongly favors Mg(2+): Mg commonly coordinates ATP phosphates and supports ATP hydrolysis. That distinguishes Mg(2+) from FAD and Fe(2+), and makes it a better choice than Mn(2+), which is not the usual primary ATPase cofactor.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The exact enzyme's relative activity with different ions is protein-specific, but it is not necessary to distinguish these options: the general ATPase–Mg(2+) relationship provides a credible basis for the keyed choice. This is a probabilistic inference, not proof of the assay result."
  },
  "case_id": "cofactor_0157",
  "expected_answer_check": {
    "evidence_ids": [
      "C5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation reports Mg(2+) as the cofactor, citing a publication, and states that the ssDNA-stimulated ATPase is most active with Mg(2+) or Ca(2+); Mn(2+) stimulates only at low concentrations. Thus Mg(2+) is supported among the offered choices."
  },
  "important_caveats": [
    "The supplied evidence is a curated annotation citing experimental work; the underlying paper was not independently reviewed here.",
    "The evidence indicates Mg(2+) or Ca(2+) can give the highest activity, so the choice of Mg(2+) is relative to the options provided."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Ca(2+) is also reported to support high activity, but it is not offered. The evidence describes Mn(2+) as stimulating only at low concentrations, which does not make it equally defensible as the primary cofactor choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0157",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation reports Mg(2+) as the cofactor, citing a publication, and states that the ssDNA-stimulated ATPase is most active with Mg(2+) or Ca(2+); Mn(2+) stimulates only at low concentrations. Thus Mg(2+) is supported among the offered choices.",
    "evidence_ids": ["C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with an ATP-dependent helicase/ATPase, including a glycine-rich Lys/Thr-containing nucleotide-binding motif. Transferable knowledge of ATPases strongly favors Mg(2+): Mg commonly coordinates ATP phosphates and supports ATP hydrolysis. That distinguishes Mg(2+) from FAD and Fe(2+), and makes it a better choice than Mn(2+), which is not the usual primary ATPase cofactor.",
    "missing_item_specific_fact": "",
    "reason": "The exact enzyme's relative activity with different ions is protein-specific, but it is not necessary to distinguish these options: the general ATPase–Mg(2+) relationship provides a credible basis for the keyed choice. This is a probabilistic inference, not proof of the assay result."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Ca(2+) is also reported to support high activity, but it is not offered. The evidence describes Mn(2+) as stimulating only at low concentrations, which does not make it equally defensible as the primary cofactor choice."
  },
  "important_caveats": [
    "The supplied evidence is a curated annotation citing experimental work; the underlying paper was not independently reviewed here.",
    "The evidence indicates Mg(2+) or Ca(2+) can give the highest activity, so the choice of Mg(2+) is relative to the options provided."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `invalid_review`.

**This response is not a usable structured review.** Its saved text is preserved below; any labels in that text are excluded from the summary counts.

**Validation errors:** `answerability_check:required_exact_keys`.

### Expected-answer support: supported

> UniProt entry Q88NV1 (ATP-dependent helicase Lhr-Core) explicitly annotates Mg(2+) as the cofactor with experimental evidence (ECO:0000269, PubMed:30224353). The note states the ssDNA-stimulated ATPase is most active with Mg(2+) or Ca(2+), while Mn(2+), Co(2+), Ni(2+), and Zn(2+) stimulate only at low concentrations. The author's expected answer C (Mg(2+)) matches the primary annotated cofactor.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a recognizable Walker A (P-loop) motif 'GAGKTY' (~residues 30-35), which is the hallmark of ATP-binding proteins including helicases and ATPases. ATP-dependent helicases universally require a divalent metal ion to coordinate ATP phosphates, and Mg(2+) is the canonical and near-universal cofactor for this function. FAD is a flavin cofactor for oxidoreductases (flavoproteins), not helicases, and can be excluded by recognizing the Walker A motif and absence of flavin-binding residues. Fe(2+) is associated with electron-transfer proteins, hemoproteins, and certain oxidases, not ATP-dependent helicases. Between Mg(2+) and Mn(2+): while Mn(2+) can substitute in some enzymes, Mg(2+) is the overwhelmingly preferred cofactor for ATP hydrolysis in helicases; Mn(2+) is more commonly associated with nucleases and polymerases. The protein's helicase/ATPase function (indicated by the Walker A motif and overall architecture) points to Mg(2+) as the primary cofactor. This is a well-established family-level inference applicable to all P-loop NTPases.


**Missing item-specific fact**

Empty string, as saved.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While the UniProt note mentions Mn(2+) can stimulate at low concentrations, the question asks for 'the specific cofactor required for catalytic activity,' and Mg(2+) is the primary, experimentally-validated cofactor for ATP-dependent helicases. Mn(2+) is a marginal substitute, not the required cofactor. The other options (FAD, Fe(2+)) are clearly incompatible with an ATP-dependent helicase. No genuine ambiguity exists among the offered choices.


### Important caveats

- The paper title (PubMed:30224353) mentions 'manganese-dependent DNA nuclease,' which refers to a different protein in the same gene cluster, not Lhr-Core itself. This could potentially mislead a model that recalls the paper title but not the specific protein assignment.
- The Walker A motif 'GAGKTY' is identifiable but not perfectly canonical (canonical is GxxGxGKT/S); it is still clearly recognizable as a P-loop nucleotide-binding motif.
- The UniProt entry was first public in 2025-06-18; the question's construction date relative to this annotation is uncertain.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a recognizable Walker A (P-loop) motif 'GAGKTY' (~residues 30-35), which is the hallmark of ATP-binding proteins including helicases and ATPases. ATP-dependent helicases universally require a divalent metal ion to coordinate ATP phosphates, and Mg(2+) is the canonical and near-universal cofactor for this function. FAD is a flavin cofactor for oxidoreductases (flavoproteins), not helicases, and can be excluded by recognizing the Walker A motif and absence of flavin-binding residues. Fe(2+) is associated with electron-transfer proteins, hemoproteins, and certain oxidases, not ATP-dependent helicases. Between Mg(2+) and Mn(2+): while Mn(2+) can substitute in some enzymes, Mg(2+) is the overwhelmingly preferred cofactor for ATP hydrolysis in helicases; Mn(2+) is more commonly associated with nucleases and polymerases. The protein's helicase/ATPase function (indicated by the Walker A motif and overall architecture) points to Mg(2+) as the primary cofactor. This is a well-established family-level inference applicable to all P-loop NTPases.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": ""
  },
  "case_id": "cofactor_0157",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q88NV1 (ATP-dependent helicase Lhr-Core) explicitly annotates Mg(2+) as the cofactor with experimental evidence (ECO:0000269, PubMed:30224353). The note states the ssDNA-stimulated ATPase is most active with Mg(2+) or Ca(2+), while Mn(2+), Co(2+), Ni(2+), and Zn(2+) stimulate only at low concentrations. The author's expected answer C (Mg(2+)) matches the primary annotated cofactor."
  },
  "important_caveats": [
    "The paper title (PubMed:30224353) mentions 'manganese-dependent DNA nuclease,' which refers to a different protein in the same gene cluster, not Lhr-Core itself. This could potentially mislead a model that recalls the paper title but not the specific protein assignment.",
    "The Walker A motif 'GAGKTY' is identifiable but not perfectly canonical (canonical is GxxGxGKT/S); it is still clearly recognizable as a P-loop nucleotide-binding motif.",
    "The UniProt entry was first public in 2025-06-18; the question's construction date relative to this annotation is uncertain."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While the UniProt note mentions Mn(2+) can stimulate at low concentrations, the question asks for 'the specific cofactor required for catalytic activity,' and Mg(2+) is the primary, experimentally-validated cofactor for ATP-dependent helicases. Mn(2+) is a marginal substitute, not the required cofactor. The other options (FAD, Fe(2+)) are clearly incompatible with an ATP-dependent helicase. No genuine ambiguity exists among the offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0157",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q88NV1 (ATP-dependent helicase Lhr-Core) explicitly annotates Mg(2+) as the cofactor with experimental evidence (ECO:0000269, PubMed:30224353). The note states the ssDNA-stimulated ATPase is most active with Mg(2+) or Ca(2+), while Mn(2+), Co(2+), Ni(2+), and Zn(2+) stimulate only at low concentrations. The author's expected answer C (Mg(2+)) matches the primary annotated cofactor.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a recognizable Walker A (P-loop) motif 'GAGKTY' (~residues 30-35), which is the hallmark of ATP-binding proteins including helicases and ATPases. ATP-dependent helicases universally require a divalent metal ion to coordinate ATP phosphates, and Mg(2+) is the canonical and near-universal cofactor for this function. FAD is a flavin cofactor for oxidoreductases (flavoproteins), not helicases, and can be excluded by recognizing the Walker A motif and absence of flavin-binding residues. Fe(2+) is associated with electron-transfer proteins, hemoproteins, and certain oxidases, not ATP-dependent helicases. Between Mg(2+) and Mn(2+): while Mn(2+) can substitute in some enzymes, Mg(2+) is the overwhelmingly preferred cofactor for ATP hydrolysis in helicases; Mn(2+) is more commonly associated with nucleases and polymerases. The protein's helicase/ATPase function (indicated by the Walker A motif and overall architecture) points to Mg(2+) as the primary cofactor. This is a well-established family-level inference applicable to all P-loop NTPases.",
    "missing_item_specific_fact": ""
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While the UniProt note mentions Mn(2+) can stimulate at low concentrations, the question asks for 'the specific cofactor required for catalytic activity,' and Mg(2+) is the primary, experimentally-validated cofactor for ATP-dependent helicases. Mn(2+) is a marginal substitute, not the required cofactor. The other options (FAD, Fe(2+)) are clearly incompatible with an ATP-dependent helicase. No genuine ambiguity exists among the offered choices."
  },
  "important_caveats": [
    "The paper title (PubMed:30224353) mentions 'manganese-dependent DNA nuclease,' which refers to a different protein in the same gene cluster, not Lhr-Core itself. This could potentially mislead a model that recalls the paper title but not the specific protein assignment.",
    "The Walker A motif 'GAGKTY' is identifiable but not perfectly canonical (canonical is GxxGxGKT/S); it is still clearly recognizable as a P-loop nucleotide-binding motif.",
    "The UniProt entry was first public in 2025-06-18; the question's construction date relative to this annotation is uncertain."
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
  "benchmark_sequence_length": 816,
  "benchmark_sequence_sha256": "04b81b45ba26233790ff428a795f481711ac7e3aac4c98668894f3efbb9df8b6",
  "current_entry_audit": {
    "entryVersion": 136,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2003-06-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "6d8894082892e958a6d474c6369d1253a40ea091c6c725a7684d7987f6ec7875",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 816,
  "current_source_sequence_sha256": "04b81b45ba26233790ff428a795f481711ac7e3aac4c98668894f3efbb9df8b6",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 134,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q88NV1",
  "selected_historical_entry_version": 134,
  "selected_historical_record_sha256": "abb725c0c25289242145250b8c248a3dabbf40cb4984bd0802e1533569e5a66f",
  "selected_historical_source_sequence_length": 816,
  "selected_historical_source_sequence_sha256": "04b81b45ba26233790ff428a795f481711ac7e3aac4c98668894f3efbb9df8b6",
  "selected_historical_version": {
    "accession": "Q88NV1",
    "database": "Swiss-Prot",
    "entryVersion": 134,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "LHRC_PSEPK",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q88NV1.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q88NV1\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:31:56.411071+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6d8894082892e958a6d474c6369d1253a40ea091c6c725a7684d7987f6ec7875",
  "url": "https://rest.uniprot.org/uniprotkb/Q88NV1.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q88NV1.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":136,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2003-06-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:31:56.411071+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6d8894082892e958a6d474c6369d1253a40ea091c6c725a7684d7987f6ec7875",
  "url": "https://rest.uniprot.org/uniprotkb/Q88NV1.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q88NV1.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Pseudomonadota\",\"Gammaproteobacteria\",\"Pseudomonadales\",\"Pseudomonadaceae\",\"Pseudomonas\"],\"scientificName\":\"Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440)\",\"taxonId\":160488}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:31:56.411071+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6d8894082892e958a6d474c6369d1253a40ea091c6c725a7684d7987f6ec7875",
  "url": "https://rest.uniprot.org/uniprotkb/Q88NV1.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q88NV1.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"DNA and RNA:DNA 3'-5' helicase Lhr-Core\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"30224353\",\"source\":\"PubMed\"}],\"value\":\"5.6.2.-\"},{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"30224353\",\"source\":\"PubMed\"}],\"value\":\"5.6.2.4\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30224353\",\"source\":\"PubMed\"}],\"value\":\"ATP-dependent helicase Lhr-Core\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30224353\",\"source\":\"PubMed\"}],\"value\":\"Lhr-Core\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:31:56.411071+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6d8894082892e958a6d474c6369d1253a40ea091c6c725a7684d7987f6ec7875",
  "url": "https://rest.uniprot.org/uniprotkb/Q88NV1.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q88NV1.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:18420\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"30224353\",\"source\":\"PubMed\"}],\"name\":\"Mg(2+)\"}],\"commentType\":\"COFACTOR\",\"note\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"30224353\",\"source\":\"PubMed\"}],\"value\":\"ssDNA-stimulated ATPase is most active with Mg(2+) or Ca(2+); Mn(2+), Co(2+), Ni(2+) and Zn(2+) stimulate at low concentrations only.\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-02T04:31:56.411071+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6d8894082892e958a6d474c6369d1253a40ea091c6c725a7684d7987f6ec7875",
  "url": "https://rest.uniprot.org/uniprotkb/Q88NV1.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q88NV1.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Ejaz A.\",\"Shuman S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"30224353\"},{\"database\":\"DOI\",\"id\":\"10.1074/jbc.ra118.005296\"}],\"citationType\":\"journal article\",\"firstPage\":\"17491\",\"id\":\"30224353\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"17504\",\"publicationDate\":\"2018\",\"title\":\"Characterization of Lhr-Core DNA helicase and manganese- dependent DNA nuclease components of a bacterial gene cluster encoding nucleic acid repair enzymes.\",\"volume\":\"293\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION AS A HELICASE\",\"FUNCTION AS AN ATPASE\",\"COFACTOR\",\"BIOPHYSICOCHEMICAL PROPERTIES\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:31:56.411071+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6d8894082892e958a6d474c6369d1253a40ea091c6c725a7684d7987f6ec7875",
  "url": "https://rest.uniprot.org/uniprotkb/Q88NV1.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q88NV1?format=txt&versions=134)

```json
{
  "entry_version": 134,
  "evidence_id": "H1",
  "excerpt": "ID   LHRC_PSEPK              Reviewed;         816 AA.\nAC   Q88NV1;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-JUN-2003, sequence version 1.\nDT   28-JAN-2026, entry version 134.\nDE   RecName: Full=ATP-dependent helicase Lhr-Core {ECO:0000303|PubMed:30224353};\nDE            Short=Lhr-Core {ECO:0000303|PubMed:30224353};\nDE            EC=5.6.2.- {ECO:0000269|PubMed:30224353};\nDE            EC=5.6.2.4 {ECO:0000269|PubMed:30224353};\nDE   AltName: Full=DNA and RNA:DNA 3'-5' helicase Lhr-Core {ECO:0000305};\nGN   OrderedLocusNames=PP_1103 {ECO:0000312|EMBL:AAN66728.1};\nOS   Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950\nOS   / KT2440).\nOC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria;\nOC   Pseudomonadales; Pseudomonadaceae; Pseudomonas.\nOX   NCBI_TaxID=160488;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:03.031844+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "abb725c0c25289242145250b8c248a3dabbf40cb4984bd0802e1533569e5a66f",
  "url": "https://rest.uniprot.org/unisave/Q88NV1?format=txt&versions=134"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q88NV1?format=txt&versions=134)

```json
{
  "entry_version": 134,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=ATP-dependent helicase Lhr-Core {ECO:0000303|PubMed:30224353};\nDE            Short=Lhr-Core {ECO:0000303|PubMed:30224353};\nDE            EC=5.6.2.- {ECO:0000269|PubMed:30224353};\nDE            EC=5.6.2.4 {ECO:0000269|PubMed:30224353};\nDE   AltName: Full=DNA and RNA:DNA 3'-5' helicase Lhr-Core {ECO:0000305};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:03.031844+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-10",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "abb725c0c25289242145250b8c248a3dabbf40cb4984bd0802e1533569e5a66f",
  "url": "https://rest.uniprot.org/unisave/Q88NV1?format=txt&versions=134"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q88NV1?format=txt&versions=134)

```json
{
  "entry_version": 134,
  "evidence_id": "H3",
  "excerpt": "RN   [2]\nRP   FUNCTION AS A HELICASE, FUNCTION AS AN ATPASE, COFACTOR, AND\nRP   BIOPHYSICOCHEMICAL PROPERTIES.\nRC   STRAIN=ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440;\nRX   PubMed=30224353; DOI=10.1074/jbc.ra118.005296;\nRA   Ejaz A., Shuman S.;\nRT   \"Characterization of Lhr-Core DNA helicase and manganese- dependent DNA\nRT   nuclease components of a bacterial gene cluster encoding nucleic acid\nRT   repair enzymes.\";\nRL   J. Biol. Chem. 293:17491-17504(2018).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:03.031844+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 32-41",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "abb725c0c25289242145250b8c248a3dabbf40cb4984bd0802e1533569e5a66f",
  "url": "https://rest.uniprot.org/unisave/Q88NV1?format=txt&versions=134"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q88NV1?format=txt&versions=134)

```json
{
  "entry_version": 134,
  "evidence_id": "H4",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=Mg(2+); Xref=ChEBI:CHEBI:18420;\nCC         Evidence={ECO:0000269|PubMed:30224353};\nCC       Note=ssDNA-stimulated ATPase is most active with Mg(2+) or Ca(2+);\nCC       Mn(2+), Co(2+), Ni(2+) and Zn(2+) stimulate at low concentrations only.\nCC       {ECO:0000269|PubMed:30224353};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:03.031844+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 58-63",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "abb725c0c25289242145250b8c248a3dabbf40cb4984bd0802e1533569e5a66f",
  "url": "https://rest.uniprot.org/unisave/Q88NV1?format=txt&versions=134"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 157. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
