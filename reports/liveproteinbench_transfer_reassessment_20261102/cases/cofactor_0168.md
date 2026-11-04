# cofactor_0168

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/cofactor_0168.txt)

**Task:** `cofactor`  
**Expected answer:** **A** — FMN

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MALLTDDFDAVVASRRAVRAFLPTPISRKLISEIIDIARLAPSNSNTQPWSIHVLTGEPKQALSALLGIAHNDPSADPLAHLPDDLARKYRERQEKWGELFYGLHQIDKCDDAGRARVSGLNFDFFGAPVGLIFTIDSNLKKYSWLDYGLFLQTLMLTARSRGLSTCPQVSFARFQSLIKDFLHLDDSQEIVCGMSLGYADENATVNSLRMPREMAQGFTHFMGFDR

[Multiple Choices]
A. FMN
B. NAD(+)
C. Fe(2+)
D. tungstopterin
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

> The sequence-matched UniProt annotation identifies FMN as the cofactor and says one FMN binds per subunit. The annotation is transferred from another UniProt entry rather than direct experimental evidence for this protein, so support is by family-level inference, not a demonstrated measurement here.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with a small bacterial nitroreductase-family flavoprotein. Such enzymes commonly use bound FMN for nitro-group reduction, while NAD(H) serves as an electron donor rather than the bound cofactor; iron and tungstopterin are not characteristic of this enzyme family. This family-level pattern meaningfully favors FMN among the offered choices.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model could use sequence-family recognition and transferable knowledge of bacterial nitroreductases to distinguish FMN without retrieving this exact protein's annotation. The family inference is probabilistic, and the original input does not provide a direct functional label.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among these choices, FMN is the defensible bound cofactor; NAD(+) is not interchangeable with the flavin cofactor.


### Important caveats

- The cited cofactor annotation is similarity-transferred, not direct experimental evidence for this exact protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a small bacterial nitroreductase-family flavoprotein. Such enzymes commonly use bound FMN for nitro-group reduction, while NAD(H) serves as an electron donor rather than the bound cofactor; iron and tungstopterin are not characteristic of this enzyme family. This family-level pattern meaningfully favors FMN among the offered choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model could use sequence-family recognition and transferable knowledge of bacterial nitroreductases to distinguish FMN without retrieving this exact protein's annotation. The family inference is probabilistic, and the original input does not provide a direct functional label."
  },
  "case_id": "cofactor_0168",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies FMN as the cofactor and says one FMN binds per subunit. The annotation is transferred from another UniProt entry rather than direct experimental evidence for this protein, so support is by family-level inference, not a demonstrated measurement here."
  },
  "important_caveats": [
    "The cited cofactor annotation is similarity-transferred, not direct experimental evidence for this exact protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among these choices, FMN is the defensible bound cofactor; NAD(+) is not interchangeable with the flavin cofactor."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0168",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies FMN as the cofactor and says one FMN binds per subunit. The annotation is transferred from another UniProt entry rather than direct experimental evidence for this protein, so support is by family-level inference, not a demonstrated measurement here.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with a small bacterial nitroreductase-family flavoprotein. Such enzymes commonly use bound FMN for nitro-group reduction, while NAD(H) serves as an electron donor rather than the bound cofactor; iron and tungstopterin are not characteristic of this enzyme family. This family-level pattern meaningfully favors FMN among the offered choices.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model could use sequence-family recognition and transferable knowledge of bacterial nitroreductases to distinguish FMN without retrieving this exact protein's annotation. The family inference is probabilistic, and the original input does not provide a direct functional label."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among these choices, FMN is the defensible bound cofactor; NAD(+) is not interchangeable with the flavin cofactor."
  },
  "important_caveats": [
    "The cited cofactor annotation is similarity-transferred, not direct experimental evidence for this exact protein."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt annotates this protein (Q9FD36, 4-nitrobenzoate reductase, EC 1.7.1.-) with FMN as cofactor, noting 'Binds 1 FMN per subunit.' However, the evidence code is ECO:0000250 (inferred by similarity to A0R6D0), meaning the FMN assignment was transferred from a homologous protein rather than directly experimentally determined for this exact sequence. The annotation is consistent with the nitroreductase superfamily assignment but is a similarity-based inference, not direct experimental proof.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The protein is 227 amino acids and contains sequence features characteristic of the nitroreductase superfamily (NfsB/NfsA-type): the 'GAPVGLIFTIDSNL' region contains a GxPVG-like flavin-binding motif, and 'CGMSLGYADENATV' contains a GxGxxG-type pattern. The nitroreductase superfamily, extensively characterized across many organisms (E. coli NfsB, NfsA, and homologs), characteristically uses FMN as its catalytic cofactor. This is a well-established family-level pattern. Tungstopterin is restricted to a handful of specialized enzymes (formate dehydrogenases, aldehyde oxidoreductases) with entirely different folds and no sequence resemblance here. Fe(2+) cofactors are typical of oxygenases, peroxidases, and dioxygenases, not small (~220 aa) nitroreductases. NAD+ binding requires a canonical Rossmann fold with the GxGxxG motif in a specific structural context; while some nitroreductases bind NAD(P)H as an electron donor, the catalytic cofactor is FMN, and the question asks for the cofactor required for catalytic activity. Thus, family membership in the nitroreductase superfamily, inferable from sequence features and length, meaningfully distinguishes FMN from the other three options.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can recognize the nitroreductase superfamily from sequence motifs (GxPVG, GxGxxG patterns, overall length ~220-230 aa, oxidoreductase context) and apply the well-established family-level rule that nitroreductases use FMN. The other cofactors (tungstopterin, Fe2+, NAD+) belong to structurally and functionally distinct enzyme classes with no resemblance to this sequence. This is legitimate transferable knowledge from other proteins in the family, not a lookup of this specific protein's record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent cofactors from very different enzyme classes. Tungstopterin is essentially unique to formate/aldehyde oxidoreductases. Fe(2+) is associated with oxygenases and peroxidases. NAD+ is associated with dehydrogenases with Rossmann folds. FMN is the hallmark cofactor of the nitroreductase superfamily, which this protein clearly belongs to based on sequence features and length. Only FMN is defensible.


### Important caveats

- The UniProt FMN annotation for Q9FD36 carries evidence code ECO:0000250 (similarity), meaning it was inferred by homology to protein A0R6D0 rather than directly measured for this protein. The annotation is reasonable but not experimentally confirmed for this exact sequence.
- Some nitroreductases (NfsA-type) also bind NADPH as an electron shuttle, but FMN remains the catalytic cofactor; the question asks for the cofactor required for catalytic activity, which points to FMN.
- The reviewer-only evidence (accession, organism, annotation) was not available to the evaluated model; the reasoning above relies solely on the provided sequence and generalizable family knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The protein is 227 amino acids and contains sequence features characteristic of the nitroreductase superfamily (NfsB/NfsA-type): the 'GAPVGLIFTIDSNL' region contains a GxPVG-like flavin-binding motif, and 'CGMSLGYADENATV' contains a GxGxxG-type pattern. The nitroreductase superfamily, extensively characterized across many organisms (E. coli NfsB, NfsA, and homologs), characteristically uses FMN as its catalytic cofactor. This is a well-established family-level pattern. Tungstopterin is restricted to a handful of specialized enzymes (formate dehydrogenases, aldehyde oxidoreductases) with entirely different folds and no sequence resemblance here. Fe(2+) cofactors are typical of oxygenases, peroxidases, and dioxygenases, not small (~220 aa) nitroreductases. NAD+ binding requires a canonical Rossmann fold with the GxGxxG motif in a specific structural context; while some nitroreductases bind NAD(P)H as an electron donor, the catalytic cofactor is FMN, and the question asks for the cofactor required for catalytic activity. Thus, family membership in the nitroreductase superfamily, inferable from sequence features and length, meaningfully distinguishes FMN from the other three options.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the nitroreductase superfamily from sequence motifs (GxPVG, GxGxxG patterns, overall length ~220-230 aa, oxidoreductase context) and apply the well-established family-level rule that nitroreductases use FMN. The other cofactors (tungstopterin, Fe2+, NAD+) belong to structurally and functionally distinct enzyme classes with no resemblance to this sequence. This is legitimate transferable knowledge from other proteins in the family, not a lookup of this specific protein's record."
  },
  "case_id": "cofactor_0168",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt annotates this protein (Q9FD36, 4-nitrobenzoate reductase, EC 1.7.1.-) with FMN as cofactor, noting 'Binds 1 FMN per subunit.' However, the evidence code is ECO:0000250 (inferred by similarity to A0R6D0), meaning the FMN assignment was transferred from a homologous protein rather than directly experimentally determined for this exact sequence. The annotation is consistent with the nitroreductase superfamily assignment but is a similarity-based inference, not direct experimental proof."
  },
  "important_caveats": [
    "The UniProt FMN annotation for Q9FD36 carries evidence code ECO:0000250 (similarity), meaning it was inferred by homology to protein A0R6D0 rather than directly measured for this protein. The annotation is reasonable but not experimentally confirmed for this exact sequence.",
    "Some nitroreductases (NfsA-type) also bind NADPH as an electron shuttle, but FMN remains the catalytic cofactor; the question asks for the cofactor required for catalytic activity, which points to FMN.",
    "The reviewer-only evidence (accession, organism, annotation) was not available to the evaluated model; the reasoning above relies solely on the provided sequence and generalizable family knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent cofactors from very different enzyme classes. Tungstopterin is essentially unique to formate/aldehyde oxidoreductases. Fe(2+) is associated with oxygenases and peroxidases. NAD+ is associated with dehydrogenases with Rossmann folds. FMN is the hallmark cofactor of the nitroreductase superfamily, which this protein clearly belongs to based on sequence features and length. Only FMN is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0168",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt annotates this protein (Q9FD36, 4-nitrobenzoate reductase, EC 1.7.1.-) with FMN as cofactor, noting 'Binds 1 FMN per subunit.' However, the evidence code is ECO:0000250 (inferred by similarity to A0R6D0), meaning the FMN assignment was transferred from a homologous protein rather than directly experimentally determined for this exact sequence. The annotation is consistent with the nitroreductase superfamily assignment but is a similarity-based inference, not direct experimental proof.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The protein is 227 amino acids and contains sequence features characteristic of the nitroreductase superfamily (NfsB/NfsA-type): the 'GAPVGLIFTIDSNL' region contains a GxPVG-like flavin-binding motif, and 'CGMSLGYADENATV' contains a GxGxxG-type pattern. The nitroreductase superfamily, extensively characterized across many organisms (E. coli NfsB, NfsA, and homologs), characteristically uses FMN as its catalytic cofactor. This is a well-established family-level pattern. Tungstopterin is restricted to a handful of specialized enzymes (formate dehydrogenases, aldehyde oxidoreductases) with entirely different folds and no sequence resemblance here. Fe(2+) cofactors are typical of oxygenases, peroxidases, and dioxygenases, not small (~220 aa) nitroreductases. NAD+ binding requires a canonical Rossmann fold with the GxGxxG motif in a specific structural context; while some nitroreductases bind NAD(P)H as an electron donor, the catalytic cofactor is FMN, and the question asks for the cofactor required for catalytic activity. Thus, family membership in the nitroreductase superfamily, inferable from sequence features and length, meaningfully distinguishes FMN from the other three options.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the nitroreductase superfamily from sequence motifs (GxPVG, GxGxxG patterns, overall length ~220-230 aa, oxidoreductase context) and apply the well-established family-level rule that nitroreductases use FMN. The other cofactors (tungstopterin, Fe2+, NAD+) belong to structurally and functionally distinct enzyme classes with no resemblance to this sequence. This is legitimate transferable knowledge from other proteins in the family, not a lookup of this specific protein's record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent cofactors from very different enzyme classes. Tungstopterin is essentially unique to formate/aldehyde oxidoreductases. Fe(2+) is associated with oxygenases and peroxidases. NAD+ is associated with dehydrogenases with Rossmann folds. FMN is the hallmark cofactor of the nitroreductase superfamily, which this protein clearly belongs to based on sequence features and length. Only FMN is defensible."
  },
  "important_caveats": [
    "The UniProt FMN annotation for Q9FD36 carries evidence code ECO:0000250 (similarity), meaning it was inferred by homology to protein A0R6D0 rather than directly measured for this protein. The annotation is reasonable but not experimentally confirmed for this exact sequence.",
    "Some nitroreductases (NfsA-type) also bind NADPH as an electron shuttle, but FMN remains the catalytic cofactor; the question asks for the cofactor required for catalytic activity, which points to FMN.",
    "The reviewer-only evidence (accession, organism, annotation) was not available to the evaluated model; the reasoning above relies solely on the provided sequence and generalizable family knowledge."
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
  "benchmark_sequence_length": 227,
  "benchmark_sequence_sha256": "3b51488ac857ad147730e4507dad5133e7f22b0c61382381fe8906536f65a0c4",
  "current_entry_audit": {
    "entryVersion": 60,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2001-03-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "79da8ba5f66886d6f25666f32850cc113bc28c677b3bb972cafdd4832f092ca5",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 227,
  "current_source_sequence_sha256": "3b51488ac857ad147730e4507dad5133e7f22b0c61382381fe8906536f65a0c4",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 59,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q9FD36",
  "selected_historical_entry_version": 59,
  "selected_historical_record_sha256": "b8e05036a664f774b75486960f2bb65b17e0fc9481338a912a9e57c2a38f1637",
  "selected_historical_source_sequence_length": 227,
  "selected_historical_source_sequence_sha256": "3b51488ac857ad147730e4507dad5133e7f22b0c61382381fe8906536f65a0c4",
  "selected_historical_version": {
    "accession": "Q9FD36",
    "database": "Swiss-Prot",
    "entryVersion": 59,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "PNBA_PSEPU",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9FD36.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q9FD36\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:32:47.892738+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "79da8ba5f66886d6f25666f32850cc113bc28c677b3bb972cafdd4832f092ca5",
  "url": "https://rest.uniprot.org/uniprotkb/Q9FD36.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9FD36.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":60,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2001-03-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:32:47.892738+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "79da8ba5f66886d6f25666f32850cc113bc28c677b3bb972cafdd4832f092ca5",
  "url": "https://rest.uniprot.org/uniprotkb/Q9FD36.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9FD36.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Arthrobacter siderocapsulatus\",\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Pseudomonadota\",\"Gammaproteobacteria\",\"Pseudomonadales\",\"Pseudomonadaceae\",\"Pseudomonas\"],\"scientificName\":\"Pseudomonas putida\",\"taxonId\":303}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:32:47.892738+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "79da8ba5f66886d6f25666f32850cc113bc28c677b3bb972cafdd4832f092ca5",
  "url": "https://rest.uniprot.org/uniprotkb/Q9FD36.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9FD36.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"11157934\",\"source\":\"PubMed\"}],\"value\":\"1.7.1.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"11157934\",\"source\":\"PubMed\"}],\"value\":\"4-nitrobenzoate reductase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"11157934\",\"source\":\"PubMed\"}],\"value\":\"4NBen reductase\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:32:47.892738+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "79da8ba5f66886d6f25666f32850cc113bc28c677b3bb972cafdd4832f092ca5",
  "url": "https://rest.uniprot.org/uniprotkb/Q9FD36.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9FD36.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:58210\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"A0R6D0\",\"source\":\"UniProtKB\"}],\"name\":\"FMN\"}],\"commentType\":\"COFACTOR\",\"note\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"A0R6D0\",\"source\":\"UniProtKB\"}],\"value\":\"Binds 1 FMN per subunit.\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:32:47.892738+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "79da8ba5f66886d6f25666f32850cc113bc28c677b3bb972cafdd4832f092ca5",
  "url": "https://rest.uniprot.org/uniprotkb/Q9FD36.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9FD36.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Hughes M.A.\",\"Williams P.A.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"11157934\"},{\"database\":\"DOI\",\"id\":\"10.1128/jb.183.4.1225-1232.2001\"}],\"citationType\":\"journal article\",\"firstPage\":\"1225\",\"id\":\"11157934\",\"journal\":\"J. Bacteriol.\",\"lastPage\":\"1232\",\"publicationDate\":\"2001\",\"title\":\"Cloning and characterisation of the pnb genes, encoding enzymes for 4-nitrobenzoate catabolism in Pseudomonas putida TW3.\",\"volume\":\"183\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"TW3\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:32:47.892738+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "79da8ba5f66886d6f25666f32850cc113bc28c677b3bb972cafdd4832f092ca5",
  "url": "https://rest.uniprot.org/uniprotkb/Q9FD36.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9FD36?format=txt&versions=59)

```json
{
  "entry_version": 59,
  "evidence_id": "H1",
  "excerpt": "ID   PNBA_PSEPU              Reviewed;         227 AA.\nAC   Q9FD36;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-MAR-2001, sequence version 1.\nDT   28-JAN-2026, entry version 59.\nDE   RecName: Full=4-nitrobenzoate reductase {ECO:0000303|PubMed:11157934};\nDE            Short=4NBen reductase {ECO:0000303|PubMed:11157934};\nDE            EC=1.7.1.- {ECO:0000269|PubMed:11157934};\nGN   Name=pnbA {ECO:0000303|PubMed:11157934};\nOS   Pseudomonas putida (Arthrobacter siderocapsulatus).\nOC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria;\nOC   Pseudomonadales; Pseudomonadaceae; Pseudomonas.\nOX   NCBI_TaxID=303;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:49.936444+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b8e05036a664f774b75486960f2bb65b17e0fc9481338a912a9e57c2a38f1637",
  "url": "https://rest.uniprot.org/unisave/Q9FD36?format=txt&versions=59"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9FD36?format=txt&versions=59)

```json
{
  "entry_version": 59,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=4-nitrobenzoate reductase {ECO:0000303|PubMed:11157934};\nDE            Short=4NBen reductase {ECO:0000303|PubMed:11157934};\nDE            EC=1.7.1.- {ECO:0000269|PubMed:11157934};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:49.936444+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-8",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b8e05036a664f774b75486960f2bb65b17e0fc9481338a912a9e57c2a38f1637",
  "url": "https://rest.uniprot.org/unisave/Q9FD36?format=txt&versions=59"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9FD36?format=txt&versions=59)

```json
{
  "entry_version": 59,
  "evidence_id": "H3",
  "excerpt": "RN   [1]\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, AND CATALYTIC ACTIVITY.\nRC   STRAIN=TW3;\nRX   PubMed=11157934; DOI=10.1128/jb.183.4.1225-1232.2001;\nRA   Hughes M.A., Williams P.A.;\nRT   \"Cloning and characterisation of the pnb genes, encoding enzymes for 4-\nRT   nitrobenzoate catabolism in Pseudomonas putida TW3.\";\nRL   J. Bacteriol. 183:1225-1232(2001).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:49.936444+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 14-21",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b8e05036a664f774b75486960f2bb65b17e0fc9481338a912a9e57c2a38f1637",
  "url": "https://rest.uniprot.org/unisave/Q9FD36?format=txt&versions=59"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9FD36?format=txt&versions=59)

```json
{
  "entry_version": 59,
  "evidence_id": "H4",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=FMN; Xref=ChEBI:CHEBI:58210;\nCC         Evidence={ECO:0000250|UniProtKB:A0R6D0};\nCC       Note=Binds 1 FMN per subunit. {ECO:0000250|UniProtKB:A0R6D0};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:49.936444+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 35-38",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b8e05036a664f774b75486960f2bb65b17e0fc9481338a912a9e57c2a38f1637",
  "url": "https://rest.uniprot.org/unisave/Q9FD36?format=txt&versions=59"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 168. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
