# pathway_0166

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/pathway_0166.txt)

**Task:** `pathway`  
**Expected answer:** **D** — Steroid biosynthesis

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MSWPLIGAYALLAFVAIIALNVTYQFLFRLLNKTRPPLVFHWIPFIGSTIHYGMDPYGFFFSCREKYGDIFTFILLGRPTTVYLGTQGNEFILNGKLKDVNAEEVYSPLTTPVFGSDVVYDCPNSKLIEQKKFIKFGLSQTALEAHVPLIEKEVEDYLAMSPNFHGTSGEVDITAAMAEITIFTAGSALQGEEVRSKLTTEFAVLYHDLDKGFTPINFMLPWAPLPHNKKRDAAHARMRAIYIDIINKRRNAGDNVPEKLDMIGNLMQCTYKNGQPLPDKEIAHIMITLLMAGQHSSSSISSWIMLRLASQPAVVEELYQEQLANLERTGPNNSLAPLQYKDFDNLPLHQNVIRETLRLNSSIHSLMRKVKNPLPVPGTPYVIPTSHVLLSAPGVTALSDEYFPNAMAWDPHRWETQAPKENDKDDIVDYGYGAISKGTSSPYLPFGAGRHRCIGEKFAYLNLAVIVATMVRHLRFSNLDGQTGVPATDYSSLFSGPMKPARIRWERRAAKSG

[Multiple Choices]
A. L-histidine biosynthesis
B. Amino-acid degradation
C. chorismate biosynthesis
D. Steroid biosynthesis
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

> The sequence-matched entry identifies the protein as a sterol 14-alpha demethylase and annotates it to steroid/sterol biosynthesis. The pathway annotation is transferred by similarity, so it is not direct experimental proof for this exact protein, but it supports choice D.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a hydrophobic N-terminal membrane anchor and a cytochrome-P450-like catalytic domain with a heme-thiolate signature. Transferable knowledge of fungal P450 families makes a sterol-pathway enzyme such as CYP51 a credible inference; CYP51-type sterol demethylases act in sterol biosynthesis. That meaningfully favors steroid biosynthesis over histidine biosynthesis, chorismate biosynthesis, or amino-acid degradation.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The relevant distinction can be made from family-level sequence recognition and knowledge of fungal sterol metabolism; it does not require recalling this exact protein's database annotation. The family assignment is an inference, not a guarantee from the sequence alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the offered choices, steroid biosynthesis is the fitting pathway for a fungal sterol-demethylase-like P450.


### Important caveats

- The supplied pathway annotation is similarity-transferred; the evidence does not by itself establish direct pathway experiments on this exact protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a hydrophobic N-terminal membrane anchor and a cytochrome-P450-like catalytic domain with a heme-thiolate signature. Transferable knowledge of fungal P450 families makes a sterol-pathway enzyme such as CYP51 a credible inference; CYP51-type sterol demethylases act in sterol biosynthesis. That meaningfully favors steroid biosynthesis over histidine biosynthesis, chorismate biosynthesis, or amino-acid degradation.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The relevant distinction can be made from family-level sequence recognition and knowledge of fungal sterol metabolism; it does not require recalling this exact protein's database annotation. The family assignment is an inference, not a guarantee from the sequence alone."
  },
  "case_id": "pathway_0166",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched entry identifies the protein as a sterol 14-alpha demethylase and annotates it to steroid/sterol biosynthesis. The pathway annotation is transferred by similarity, so it is not direct experimental proof for this exact protein, but it supports choice D."
  },
  "important_caveats": [
    "The supplied pathway annotation is similarity-transferred; the evidence does not by itself establish direct pathway experiments on this exact protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, steroid biosynthesis is the fitting pathway for a fungal sterol-demethylase-like P450."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0166",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched entry identifies the protein as a sterol 14-alpha demethylase and annotates it to steroid/sterol biosynthesis. The pathway annotation is transferred by similarity, so it is not direct experimental proof for this exact protein, but it supports choice D.",
    "evidence_ids": ["C4", "C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a hydrophobic N-terminal membrane anchor and a cytochrome-P450-like catalytic domain with a heme-thiolate signature. Transferable knowledge of fungal P450 families makes a sterol-pathway enzyme such as CYP51 a credible inference; CYP51-type sterol demethylases act in sterol biosynthesis. That meaningfully favors steroid biosynthesis over histidine biosynthesis, chorismate biosynthesis, or amino-acid degradation.",
    "missing_item_specific_fact": "",
    "reason": "The relevant distinction can be made from family-level sequence recognition and knowledge of fungal sterol metabolism; it does not require recalling this exact protein's database annotation. The family assignment is an inference, not a guarantee from the sequence alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, steroid biosynthesis is the fitting pathway for a fungal sterol-demethylase-like P450."
  },
  "important_caveats": [
    "The supplied pathway annotation is similarity-transferred; the evidence does not by itself establish direct pathway experiments on this exact protein."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (A0A0L1JEW4) annotates this protein as 'Sterol 14-alpha demethylase rstn2' (EC 1.14.14.154), a cytochrome P450 monooxygenase, with the pathway 'Steroid biosynthesis; sterol biosynthesis.' The pathway annotation carries ECO:0000250 (similarity to Q4WNT5, a known CYP51 homolog), and the primary literature (PubMed 33857369) provides experimental evidence for function, catalytic activity, and pathway. The answer D (Steroid biosynthesis) is directly supported by the database annotation and corroborated by experimental characterization.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the unmistakable cytochrome P450 heme-binding signature 'FAGRHRCIGEKF' (the FxxGxxxCxG motif), identifying this as a P450 monooxygenase. The N-terminal hydrophobic stretch is consistent with a membrane-anchored (microsomal) P450, and the overall length (~513 aa) fits fungal CYP51-type enzymes. Among the four offered pathways, steroid/sterol biosynthesis is the ONLY one in which P450 enzymes are central, defining players: CYP51 (sterol 14α-demethylase) is one of the most universally conserved and well-characterized P450s in biology, present in fungi, plants, and animals. In contrast, L-histidine biosynthesis (ATP phosphoribosyltransferase, histidine ammonia-lyase, etc.), chorismate/shikimate biosynthesis (DAHP synthase, shikimate kinase, chorismate synthase), and general amino-acid degradation (transaminases, dehydrogenases, ammonia-lyases) do not classically involve P450 enzymes. Thus, recognizing the P450 family from the heme-binding motif and applying the well-established association of P450s with sterol biosynthesis meaningfully selects D over A, B, and C.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can identify the P450 heme-binding motif directly from the sequence, recall that P450 enzymes are the hallmark oxidoreductases of steroid/ergosterol biosynthesis (CYP51), and eliminate the other three options because those pathways are not P450-dependent. This is a standard family-level inference (P450 → sterol biosynthesis) learned from many homologous proteins, not a lookup of this specific entry's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options are clearly distinguishable by pathway type. Histidine biosynthesis, amino-acid degradation, and chorismate biosynthesis are not P450 pathways. Steroid biosynthesis is the canonical P450 pathway among the choices. No ambiguity exists among the offered alternatives given the identifiable P450 motif.


### Important caveats

- The UniProt pathway annotation for this entry is by similarity (ECO:0000250) to Q4WNT5, a known CYP51 homolog, rather than being derived entirely de novo for this protein. However, the primary literature (PubMed 33857369) independently confirms function and pathway.
- The protein is specifically a CYP51 homolog involved in ergosterol (fungal sterol) biosynthesis, which UniProt categorizes under 'Steroid biosynthesis; sterol biosynthesis.' The option text 'Steroid biosynthesis' is a reasonable match to this annotation.
- The P450 heme-binding motif 'FAGRHRCIGEKF' is unambiguously present in the sequence, making P450 identification straightforward without needing the UniProt record.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the unmistakable cytochrome P450 heme-binding signature 'FAGRHRCIGEKF' (the FxxGxxxCxG motif), identifying this as a P450 monooxygenase. The N-terminal hydrophobic stretch is consistent with a membrane-anchored (microsomal) P450, and the overall length (~513 aa) fits fungal CYP51-type enzymes. Among the four offered pathways, steroid/sterol biosynthesis is the ONLY one in which P450 enzymes are central, defining players: CYP51 (sterol 14α-demethylase) is one of the most universally conserved and well-characterized P450s in biology, present in fungi, plants, and animals. In contrast, L-histidine biosynthesis (ATP phosphoribosyltransferase, histidine ammonia-lyase, etc.), chorismate/shikimate biosynthesis (DAHP synthase, shikimate kinase, chorismate synthase), and general amino-acid degradation (transaminases, dehydrogenases, ammonia-lyases) do not classically involve P450 enzymes. Thus, recognizing the P450 family from the heme-binding motif and applying the well-established association of P450s with sterol biosynthesis meaningfully selects D over A, B, and C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can identify the P450 heme-binding motif directly from the sequence, recall that P450 enzymes are the hallmark oxidoreductases of steroid/ergosterol biosynthesis (CYP51), and eliminate the other three options because those pathways are not P450-dependent. This is a standard family-level inference (P450 → sterol biosynthesis) learned from many homologous proteins, not a lookup of this specific entry's annotation."
  },
  "case_id": "pathway_0166",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (A0A0L1JEW4) annotates this protein as 'Sterol 14-alpha demethylase rstn2' (EC 1.14.14.154), a cytochrome P450 monooxygenase, with the pathway 'Steroid biosynthesis; sterol biosynthesis.' The pathway annotation carries ECO:0000250 (similarity to Q4WNT5, a known CYP51 homolog), and the primary literature (PubMed 33857369) provides experimental evidence for function, catalytic activity, and pathway. The answer D (Steroid biosynthesis) is directly supported by the database annotation and corroborated by experimental characterization."
  },
  "important_caveats": [
    "The UniProt pathway annotation for this entry is by similarity (ECO:0000250) to Q4WNT5, a known CYP51 homolog, rather than being derived entirely de novo for this protein. However, the primary literature (PubMed 33857369) independently confirms function and pathway.",
    "The protein is specifically a CYP51 homolog involved in ergosterol (fungal sterol) biosynthesis, which UniProt categorizes under 'Steroid biosynthesis; sterol biosynthesis.' The option text 'Steroid biosynthesis' is a reasonable match to this annotation.",
    "The P450 heme-binding motif 'FAGRHRCIGEKF' is unambiguously present in the sequence, making P450 identification straightforward without needing the UniProt record."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are clearly distinguishable by pathway type. Histidine biosynthesis, amino-acid degradation, and chorismate biosynthesis are not P450 pathways. Steroid biosynthesis is the canonical P450 pathway among the choices. No ambiguity exists among the offered alternatives given the identifiable P450 motif."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0166",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (A0A0L1JEW4) annotates this protein as 'Sterol 14-alpha demethylase rstn2' (EC 1.14.14.154), a cytochrome P450 monooxygenase, with the pathway 'Steroid biosynthesis; sterol biosynthesis.' The pathway annotation carries ECO:0000250 (similarity to Q4WNT5, a known CYP51 homolog), and the primary literature (PubMed 33857369) provides experimental evidence for function, catalytic activity, and pathway. The answer D (Steroid biosynthesis) is directly supported by the database annotation and corroborated by experimental characterization.",
    "evidence_ids": ["C4", "C5", "C6", "H1", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the unmistakable cytochrome P450 heme-binding signature 'FAGRHRCIGEKF' (the FxxGxxxCxG motif), identifying this as a P450 monooxygenase. The N-terminal hydrophobic stretch is consistent with a membrane-anchored (microsomal) P450, and the overall length (~513 aa) fits fungal CYP51-type enzymes. Among the four offered pathways, steroid/sterol biosynthesis is the ONLY one in which P450 enzymes are central, defining players: CYP51 (sterol 14α-demethylase) is one of the most universally conserved and well-characterized P450s in biology, present in fungi, plants, and animals. In contrast, L-histidine biosynthesis (ATP phosphoribosyltransferase, histidine ammonia-lyase, etc.), chorismate/shikimate biosynthesis (DAHP synthase, shikimate kinase, chorismate synthase), and general amino-acid degradation (transaminases, dehydrogenases, ammonia-lyases) do not classically involve P450 enzymes. Thus, recognizing the P450 family from the heme-binding motif and applying the well-established association of P450s with sterol biosynthesis meaningfully selects D over A, B, and C.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can identify the P450 heme-binding motif directly from the sequence, recall that P450 enzymes are the hallmark oxidoreductases of steroid/ergosterol biosynthesis (CYP51), and eliminate the other three options because those pathways are not P450-dependent. This is a standard family-level inference (P450 → sterol biosynthesis) learned from many homologous proteins, not a lookup of this specific entry's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are clearly distinguishable by pathway type. Histidine biosynthesis, amino-acid degradation, and chorismate biosynthesis are not P450 pathways. Steroid biosynthesis is the canonical P450 pathway among the choices. No ambiguity exists among the offered alternatives given the identifiable P450 motif."
  },
  "important_caveats": [
    "The UniProt pathway annotation for this entry is by similarity (ECO:0000250) to Q4WNT5, a known CYP51 homolog, rather than being derived entirely de novo for this protein. However, the primary literature (PubMed 33857369) independently confirms function and pathway.",
    "The protein is specifically a CYP51 homolog involved in ergosterol (fungal sterol) biosynthesis, which UniProt categorizes under 'Steroid biosynthesis; sterol biosynthesis.' The option text 'Steroid biosynthesis' is a reasonable match to this annotation.",
    "The P450 heme-binding motif 'FAGRHRCIGEKF' is unambiguously present in the sequence, making P450 identification straightforward without needing the UniProt record."
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
  "benchmark_sequence_length": 513,
  "benchmark_sequence_sha256": "19c16af699d50913a7bf4f55defbf96b0893917eaeb57b66b0dc53dd081e1b3c",
  "current_entry_audit": {
    "entryVersion": 40,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2015-11-11",
    "sequenceVersion": 1
  },
  "current_record_sha256": "d02dbb89f818b7eb87df130d530379b150615f58a7786d959f158367f6e7dbef",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 513,
  "current_source_sequence_sha256": "19c16af699d50913a7bf4f55defbf96b0893917eaeb57b66b0dc53dd081e1b3c",
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
  "requested_accession": "A0A0L1JEW4",
  "selected_historical_entry_version": 38,
  "selected_historical_record_sha256": "6c3d64c65d2f83b7569168450886015fb66b6ae6595088f32ba80d12e66f79e5",
  "selected_historical_source_sequence_length": 513,
  "selected_historical_source_sequence_sha256": "19c16af699d50913a7bf4f55defbf96b0893917eaeb57b66b0dc53dd081e1b3c",
  "selected_historical_version": {
    "accession": "A0A0L1JEW4",
    "database": "Swiss-Prot",
    "entryVersion": 38,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "RSTN2_ASPN3",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0L1JEW4.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A0L1JEW4\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:24:12.364317+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d02dbb89f818b7eb87df130d530379b150615f58a7786d959f158367f6e7dbef",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0L1JEW4.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0L1JEW4.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":40,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2015-11-11\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:24:12.364317+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d02dbb89f818b7eb87df130d530379b150615f58a7786d959f158367f6e7dbef",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0L1JEW4.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0L1JEW4.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Eurotiomycetes\",\"Eurotiomycetidae\",\"Eurotiales\",\"Aspergillaceae\",\"Aspergillus\",\"Circumdati\"],\"scientificName\":\"Aspergillus nomiae NRRL (strain ATCC 15546 / NRRL 13137 / CBS 260.88 / M93)\",\"taxonId\":1509407}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:24:12.364317+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d02dbb89f818b7eb87df130d530379b150615f58a7786d959f158367f6e7dbef",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0L1JEW4.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0L1JEW4.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33857369\",\"source\":\"PubMed\"}],\"value\":\"Cytochrome P450 monooxygenase rstn2\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33857369\",\"source\":\"PubMed\"}],\"value\":\"Ergosterol biosynthesis protein rstn2\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33857369\",\"source\":\"PubMed\"}],\"value\":\"Restricticin biosynthesis cluster protein 2\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"33857369\",\"source\":\"PubMed\"}],\"value\":\"1.14.14.154\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33857369\",\"source\":\"PubMed\"}],\"value\":\"Sterol 14-alpha demethylase rstn2\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:24:12.364317+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d02dbb89f818b7eb87df130d530379b150615f58a7786d959f158367f6e7dbef",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0L1JEW4.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0L1JEW4.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q4WNT5\",\"source\":\"UniProtKB\"}],\"value\":\"Steroid biosynthesis; sterol biosynthesis\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/14",
  "retrieved_utc": "2026-11-02T04:24:12.364317+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d02dbb89f818b7eb87df130d530379b150615f58a7786d959f158367f6e7dbef",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0L1JEW4.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0L1JEW4.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Liu N.\",\"Abramyan E.D.\",\"Cheng W.\",\"Perlatti B.\",\"Harvey C.J.B.\",\"Bills G.F.\",\"Tang Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"33857369\"},{\"database\":\"DOI\",\"id\":\"10.1021/jacs.1c01516\"}],\"citationType\":\"journal article\",\"firstPage\":\"6043\",\"id\":\"33857369\",\"journal\":\"J. Am. Chem. Soc.\",\"lastPage\":\"6047\",\"publicationDate\":\"2021\",\"title\":\"Targeted genome mining reveals the biosynthetic gene clusters of natural product CYP51 inhibitors.\",\"volume\":\"143\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:24:12.364317+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d02dbb89f818b7eb87df130d530379b150615f58a7786d959f158367f6e7dbef",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0L1JEW4.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0L1JEW4?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H1",
  "excerpt": "ID   RSTN2_ASPN3             Reviewed;         513 AA.\nAC   A0A0L1JEW4;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   11-NOV-2015, sequence version 1.\nDT   28-JAN-2026, entry version 38.\nDE   RecName: Full=Sterol 14-alpha demethylase rstn2 {ECO:0000303|PubMed:33857369};\nDE            EC=1.14.14.154 {ECO:0000269|PubMed:33857369};\nDE   AltName: Full=Cytochrome P450 monooxygenase rstn2 {ECO:0000303|PubMed:33857369};\nDE   AltName: Full=Ergosterol biosynthesis protein rstn2 {ECO:0000303|PubMed:33857369};\nDE   AltName: Full=Restricticin biosynthesis cluster protein 2 {ECO:0000303|PubMed:33857369};\nGN   Name=rstn2 {ECO:0000303|PubMed:33857369}; ORFNames=ANOM_001443;\nOS   Aspergillus nomiae NRRL (strain ATCC 15546 / NRRL 13137 / CBS 260.88 /\nOS   M93).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;\nOC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Aspergillus;\nOC   Aspergillus subgen. Circumdati.\nOX   NCBI_TaxID=1509407;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:14.653166+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-17",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6c3d64c65d2f83b7569168450886015fb66b6ae6595088f32ba80d12e66f79e5",
  "url": "https://rest.uniprot.org/unisave/A0A0L1JEW4?format=txt&versions=38"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0L1JEW4?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, AND PATHWAY.\nRX   PubMed=33857369; DOI=10.1021/jacs.1c01516;\nRA   Liu N., Abramyan E.D., Cheng W., Perlatti B., Harvey C.J.B., Bills G.F.,\nRA   Tang Y.;\nRT   \"Targeted genome mining reveals the biosynthetic gene clusters of natural\nRT   product CYP51 inhibitors.\";\nRL   J. Am. Chem. Soc. 143:6043-6047(2021).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:14.653166+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 26-33",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6c3d64c65d2f83b7569168450886015fb66b6ae6595088f32ba80d12e66f79e5",
  "url": "https://rest.uniprot.org/unisave/A0A0L1JEW4?format=txt&versions=38"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0L1JEW4?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H3",
  "excerpt": "CC   -!- PATHWAY: Steroid biosynthesis; sterol biosynthesis.\nCC       {ECO:0000250|UniProtKB:Q4WNT5}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:14.653166+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 166-167",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6c3d64c65d2f83b7569168450886015fb66b6ae6595088f32ba80d12e66f79e5",
  "url": "https://rest.uniprot.org/unisave/A0A0L1JEW4?format=txt&versions=38"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 166. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
