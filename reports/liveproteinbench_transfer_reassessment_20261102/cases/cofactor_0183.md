# cofactor_0183

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/cofactor_0183.txt)

**Task:** `cofactor`  
**Expected answer:** **D** — Fe(2+)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MDSEFLELTQLLPRWVDLENVVRGEVEARYILKRAADHLANLRSGGDSGAEETGYLVGALVDRNWERIHTGHFSQVPLVTRKIYAIACCFKIFFLLLESTSPAQKDACSEILDEAQLLGCMEDWSELKVALMDYLDKDGAVALNSAPLPTLEPLTRVTSNCDIPQLDAPSLEEFQTKCFEAGQPTLLLNTIQHWPALHKWLDLNYLLQVAGNRTVPIEIGSNYASDEWSQQLVKIRDFLSRQFGKEPSKAGQNIEYLAQHELFAQIPALKEDISIPDYCTISNEDTPGAVDIKAWLGPAGTVSPMHYDPKHNLLCQVFGSKRIILAAPADTDNLYPHDSEFLANTARIDAAQLDPETYPLVAKVKFYQLLLQPGDCLYMPPKWWHYVRSEAPSFSVSFWWE

[Multiple Choices]
A. FMN
B. Mo-bis(molybdopterin guanine dinucleotide)
C. heme b
D. Fe(2+)
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

> The sequence-matched UniProt record annotates Fe(2+) as the cofactor, one ion per subunit. The annotation is transferred by similarity from a homolog (ECO:0000250), rather than direct experimental evidence for this protein, but it supports the expected answer.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with a JmjC-domain oxygenase: it contains an HxD motif (in the segment MHYDPK), characteristic of the metal-binding site in Fe(II)-dependent 2-oxoglutarate oxygenases. Family-level knowledge therefore makes Fe(2+) a meaningful choice over FMN, molybdenum cofactor, or heme b.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A conserved sequence feature and transferable knowledge of the JmjC oxygenase family provide a credible basis for distinguishing Fe(2+) among these options. This is an inference, not proof of the exact protein's cofactor occupancy or experimental dependence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The offered alternatives are distinct, and the JmjC/Fe(II)-oxygenase inference favors only Fe(2+).


### Important caveats

- The reviewer-only annotation is based on similarity transfer, not direct experimental evidence for the supplied protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a JmjC-domain oxygenase: it contains an HxD motif (in the segment MHYDPK), characteristic of the metal-binding site in Fe(II)-dependent 2-oxoglutarate oxygenases. Family-level knowledge therefore makes Fe(2+) a meaningful choice over FMN, molybdenum cofactor, or heme b.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A conserved sequence feature and transferable knowledge of the JmjC oxygenase family provide a credible basis for distinguishing Fe(2+) among these options. This is an inference, not proof of the exact protein's cofactor occupancy or experimental dependence."
  },
  "case_id": "cofactor_0183",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates Fe(2+) as the cofactor, one ion per subunit. The annotation is transferred by similarity from a homolog (ECO:0000250), rather than direct experimental evidence for this protein, but it supports the expected answer."
  },
  "important_caveats": [
    "The reviewer-only annotation is based on similarity transfer, not direct experimental evidence for the supplied protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The offered alternatives are distinct, and the JmjC/Fe(II)-oxygenase inference favors only Fe(2+)."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0183",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates Fe(2+) as the cofactor, one ion per subunit. The annotation is transferred by similarity from a homolog (ECO:0000250), rather than direct experimental evidence for this protein, but it supports the expected answer.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with a JmjC-domain oxygenase: it contains an HxD motif (in the segment MHYDPK), characteristic of the metal-binding site in Fe(II)-dependent 2-oxoglutarate oxygenases. Family-level knowledge therefore makes Fe(2+) a meaningful choice over FMN, molybdenum cofactor, or heme b.",
    "missing_item_specific_fact": "",
    "reason": "A conserved sequence feature and transferable knowledge of the JmjC oxygenase family provide a credible basis for distinguishing Fe(2+) among these options. This is an inference, not proof of the exact protein's cofactor occupancy or experimental dependence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The offered alternatives are distinct, and the JmjC/Fe(II)-oxygenase inference favors only Fe(2+)."
  },
  "important_caveats": [
    "The reviewer-only annotation is based on similarity transfer, not direct experimental evidence for the supplied protein."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation for this sequence (Q9W0M3, JMJD5/KDM8 from Drosophila melanogaster) explicitly states COFACTOR: Fe(2+), Binds 1 Fe(2+) ion per subunit. The evidence code is ECO:0000250 (inferred by similarity from human JMJD5, Q8N371), meaning the annotation is transferred rather than directly experimentally determined for this exact protein. However, the JmjC domain family's universal requirement for Fe(2+) as a catalytic cofactor is extremely well-established across the entire superfamily, making this a highly reliable annotation. The key (D: Fe(2+)) is consistent with the annotation and with family-level biochemistry.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains hallmarks of the Jumonji C (JmjC) domain superfamily: multiple conserved His and Asp/Glu residues arranged in HxD/E-like patterns (e.g., 'SPMHYDPKHNLLCQVFGSKRIILAAPADTDNLYPHDSEF' containing H-Y-D and H-D motifs characteristic of the Fe(2+)-coordinating triad). The JmjC domain is one of the most extensively characterized Fe(2+)/2-oxoglutarate-dependent dioxygenase families in biology; every member requires Fe(2+) for catalysis. Conversely, the sequence lacks: (A) FMN-binding motifs such as GxGxxG at the N-terminus or the flavin-binding beta-alpha-beta fold; (B) molybdenum cofactor-binding motifs (e.g., the conserved Cys and Arg residues of Mo-cofactor enzymes); (C) heme b-binding motifs (e.g., CxxCH or the bis-His ligation pattern of cytochromes). Thus, family-level knowledge of JmjC proteins plus the absence of motifs diagnostic of the three distractor cofactors provides a clear, transferable basis for selecting D over A, B, and C.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Recognizing the JmjC domain from its conserved His/Asp iron-coordinating residues and knowing that the entire JmjC superfamily is Fe(2+)-dependent is standard transferable protein-family knowledge. The absence of motifs for FMN, Mo-cofactor, and heme b further eliminates the distractors. No fact specific to this exact Drosophila JMJD5 protein beyond its family membership is needed to distinguish the four options.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four cofactor choices are mutually exclusive and associated with distinct, well-characterized protein families. The JmjC domain signature in the sequence, combined with the absence of motifs for the other three cofactors, cleanly points to Fe(2+) without ambiguity.


### Important caveats

- The UniProt cofactor annotation carries evidence code ECO:0000250 (similarity transfer from human Q8N371), not direct experimental evidence on the Drosophila protein. However, the Fe(2+) requirement is a universal family-level property of JmjC dioxygenases, so the transfer is highly reliable.
- The sequence was annotated in UniProt in April 2025 (entry Q9W0M3, Swiss-Prot). The benchmark question's author may have used an earlier or different source snapshot; the sequence itself matches across all checked versions.
- JmjC domain sequence conservation can be degenerate; a model unfamiliar with the family might struggle with positive identification, but the elimination of the three distractor cofactor motifs provides an independent route to the answer.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains hallmarks of the Jumonji C (JmjC) domain superfamily: multiple conserved His and Asp/Glu residues arranged in HxD/E-like patterns (e.g., 'SPMHYDPKHNLLCQVFGSKRIILAAPADTDNLYPHDSEF' containing H-Y-D and H-D motifs characteristic of the Fe(2+)-coordinating triad). The JmjC domain is one of the most extensively characterized Fe(2+)/2-oxoglutarate-dependent dioxygenase families in biology; every member requires Fe(2+) for catalysis. Conversely, the sequence lacks: (A) FMN-binding motifs such as GxGxxG at the N-terminus or the flavin-binding beta-alpha-beta fold; (B) molybdenum cofactor-binding motifs (e.g., the conserved Cys and Arg residues of Mo-cofactor enzymes); (C) heme b-binding motifs (e.g., CxxCH or the bis-His ligation pattern of cytochromes). Thus, family-level knowledge of JmjC proteins plus the absence of motifs diagnostic of the three distractor cofactors provides a clear, transferable basis for selecting D over A, B, and C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Recognizing the JmjC domain from its conserved His/Asp iron-coordinating residues and knowing that the entire JmjC superfamily is Fe(2+)-dependent is standard transferable protein-family knowledge. The absence of motifs for FMN, Mo-cofactor, and heme b further eliminates the distractors. No fact specific to this exact Drosophila JMJD5 protein beyond its family membership is needed to distinguish the four options."
  },
  "case_id": "cofactor_0183",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation for this sequence (Q9W0M3, JMJD5/KDM8 from Drosophila melanogaster) explicitly states COFACTOR: Fe(2+), Binds 1 Fe(2+) ion per subunit. The evidence code is ECO:0000250 (inferred by similarity from human JMJD5, Q8N371), meaning the annotation is transferred rather than directly experimentally determined for this exact protein. However, the JmjC domain family's universal requirement for Fe(2+) as a catalytic cofactor is extremely well-established across the entire superfamily, making this a highly reliable annotation. The key (D: Fe(2+)) is consistent with the annotation and with family-level biochemistry."
  },
  "important_caveats": [
    "The UniProt cofactor annotation carries evidence code ECO:0000250 (similarity transfer from human Q8N371), not direct experimental evidence on the Drosophila protein. However, the Fe(2+) requirement is a universal family-level property of JmjC dioxygenases, so the transfer is highly reliable.",
    "The sequence was annotated in UniProt in April 2025 (entry Q9W0M3, Swiss-Prot). The benchmark question's author may have used an earlier or different source snapshot; the sequence itself matches across all checked versions.",
    "JmjC domain sequence conservation can be degenerate; a model unfamiliar with the family might struggle with positive identification, but the elimination of the three distractor cofactor motifs provides an independent route to the answer."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four cofactor choices are mutually exclusive and associated with distinct, well-characterized protein families. The JmjC domain signature in the sequence, combined with the absence of motifs for the other three cofactors, cleanly points to Fe(2+) without ambiguity."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0183",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation for this sequence (Q9W0M3, JMJD5/KDM8 from Drosophila melanogaster) explicitly states COFACTOR: Fe(2+), Binds 1 Fe(2+) ion per subunit. The evidence code is ECO:0000250 (inferred by similarity from human JMJD5, Q8N371), meaning the annotation is transferred rather than directly experimentally determined for this exact protein. However, the JmjC domain family's universal requirement for Fe(2+) as a catalytic cofactor is extremely well-established across the entire superfamily, making this a highly reliable annotation. The key (D: Fe(2+)) is consistent with the annotation and with family-level biochemistry.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains hallmarks of the Jumonji C (JmjC) domain superfamily: multiple conserved His and Asp/Glu residues arranged in HxD/E-like patterns (e.g., 'SPMHYDPKHNLLCQVFGSKRIILAAPADTDNLYPHDSEF' containing H-Y-D and H-D motifs characteristic of the Fe(2+)-coordinating triad). The JmjC domain is one of the most extensively characterized Fe(2+)/2-oxoglutarate-dependent dioxygenase families in biology; every member requires Fe(2+) for catalysis. Conversely, the sequence lacks: (A) FMN-binding motifs such as GxGxxG at the N-terminus or the flavin-binding beta-alpha-beta fold; (B) molybdenum cofactor-binding motifs (e.g., the conserved Cys and Arg residues of Mo-cofactor enzymes); (C) heme b-binding motifs (e.g., CxxCH or the bis-His ligation pattern of cytochromes). Thus, family-level knowledge of JmjC proteins plus the absence of motifs diagnostic of the three distractor cofactors provides a clear, transferable basis for selecting D over A, B, and C.",
    "missing_item_specific_fact": "",
    "reason": "Recognizing the JmjC domain from its conserved His/Asp iron-coordinating residues and knowing that the entire JmjC superfamily is Fe(2+)-dependent is standard transferable protein-family knowledge. The absence of motifs for FMN, Mo-cofactor, and heme b further eliminates the distractors. No fact specific to this exact Drosophila JMJD5 protein beyond its family membership is needed to distinguish the four options."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four cofactor choices are mutually exclusive and associated with distinct, well-characterized protein families. The JmjC domain signature in the sequence, combined with the absence of motifs for the other three cofactors, cleanly points to Fe(2+) without ambiguity."
  },
  "important_caveats": [
    "The UniProt cofactor annotation carries evidence code ECO:0000250 (similarity transfer from human Q8N371), not direct experimental evidence on the Drosophila protein. However, the Fe(2+) requirement is a universal family-level property of JmjC dioxygenases, so the transfer is highly reliable.",
    "The sequence was annotated in UniProt in April 2025 (entry Q9W0M3, Swiss-Prot). The benchmark question's author may have used an earlier or different source snapshot; the sequence itself matches across all checked versions.",
    "JmjC domain sequence conservation can be degenerate; a model unfamiliar with the family might struggle with positive identification, but the elimination of the three distractor cofactor motifs provides an independent route to the answer."
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
  "benchmark_sequence_length": 401,
  "benchmark_sequence_sha256": "8ae812d7a91d29ae771da37685183b9f346a91cb506ca5e697440360355ffbac",
  "current_entry_audit": {
    "entryVersion": 172,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2010-11-30",
    "sequenceVersion": 2
  },
  "current_record_sha256": "1ea6b03bc8ddb55213f5b2d1a92a5f5660c411ba7d6b4ad94233da43076eafe1",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 401,
  "current_source_sequence_sha256": "8ae812d7a91d29ae771da37685183b9f346a91cb506ca5e697440360355ffbac",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 170,
      "exact_sequence_comparison": "matched",
      "sequence_version": 2
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q9W0M3",
  "selected_historical_entry_version": 170,
  "selected_historical_record_sha256": "45e70668e7a96138303d865036cba4c2edb7da0e5634453cb9fbab186acc3750",
  "selected_historical_source_sequence_length": 401,
  "selected_historical_source_sequence_sha256": "8ae812d7a91d29ae771da37685183b9f346a91cb506ca5e697440360355ffbac",
  "selected_historical_version": {
    "accession": "Q9W0M3",
    "database": "Swiss-Prot",
    "entryVersion": 170,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "KDM8_DROME",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9W0M3.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q9W0M3\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:33:43.683489+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1ea6b03bc8ddb55213f5b2d1a92a5f5660c411ba7d6b4ad94233da43076eafe1",
  "url": "https://rest.uniprot.org/uniprotkb/Q9W0M3.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9W0M3.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":172,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2010-11-30\",\"sequenceVersion\":2}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:33:43.683489+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1ea6b03bc8ddb55213f5b2d1a92a5f5660c411ba7d6b4ad94233da43076eafe1",
  "url": "https://rest.uniprot.org/uniprotkb/Q9W0M3.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9W0M3.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Fruit fly\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000000803\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Ecdysozoa\",\"Arthropoda\",\"Altocrustacea\",\"Allotriocarida\",\"Hexapoda\",\"Insecta\",\"Pterygota\",\"Neoptera\",\"Eumetabola\",\"Endopterygota\",\"Aparaglossata\",\"Panorpida\",\"Diptera\",\"Brachycera\",\"Muscomorpha\",\"Ephydroidea\",\"Drosophilidae\",\"Drosophila\",\"Sophophora\"],\"scientificName\":\"Drosophila melanogaster\",\"taxonId\":7227}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:33:43.683489+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1ea6b03bc8ddb55213f5b2d1a92a5f5660c411ba7d6b4ad94233da43076eafe1",
  "url": "https://rest.uniprot.org/uniprotkb/Q9W0M3.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9W0M3.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Lysine-specific demethylase 8\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8N371\",\"source\":\"UniProtKB\"}],\"value\":\"1.14.11.73\"},{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8N371\",\"source\":\"UniProtKB\"}],\"value\":\"3.4.-.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Jumonji C domain-containing protein 5\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:33:43.683489+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1ea6b03bc8ddb55213f5b2d1a92a5f5660c411ba7d6b4ad94233da43076eafe1",
  "url": "https://rest.uniprot.org/uniprotkb/Q9W0M3.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9W0M3.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:29033\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8N371\",\"source\":\"UniProtKB\"}],\"name\":\"Fe(2+)\"}],\"commentType\":\"COFACTOR\",\"note\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8N371\",\"source\":\"UniProtKB\"}],\"value\":\"Binds 1 Fe(2+) ion per subunit.\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:33:43.683489+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1ea6b03bc8ddb55213f5b2d1a92a5f5660c411ba7d6b4ad94233da43076eafe1",
  "url": "https://rest.uniprot.org/uniprotkb/Q9W0M3.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9W0M3?format=txt&versions=170)

```json
{
  "entry_version": 170,
  "evidence_id": "H1",
  "excerpt": "ID   KDM8_DROME              Reviewed;         401 AA.\nAC   Q9W0M3; M9PDS1; Q86NX2;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   30-NOV-2010, sequence version 2.\nDT   28-JAN-2026, entry version 170.\nDE   RecName: Full=Jumonji C domain-containing protein 5 {ECO:0000305};\nDE            EC=1.14.11.73 {ECO:0000250|UniProtKB:Q8N371};\nDE            EC=3.4.-.- {ECO:0000250|UniProtKB:Q8N371};\nDE   AltName: Full=Lysine-specific demethylase 8 {ECO:0000305};\nGN   Name=JMJD5 {ECO:0000312|FlyBase:FBgn0035166};\nGN   Synonyms=Kdm8 {ECO:0000312|FlyBase:FBgn0035166};\nGN   ORFNames=CG13902 {ECO:0000312|FlyBase:FBgn0035166};\nOS   Drosophila melanogaster (Fruit fly).\nOC   Eukaryota; Metazoa; Ecdysozoa; Arthropoda; Hexapoda; Insecta; Pterygota;\nOC   Neoptera; Endopterygota; Diptera; Brachycera; Muscomorpha; Ephydroidea;\nOC   Drosophilidae; Drosophila; Sophophora.\nOX   NCBI_TaxID=7227 {ECO:0000312|Proteomes:UP000000803};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:45.948211+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-17",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "45e70668e7a96138303d865036cba4c2edb7da0e5634453cb9fbab186acc3750",
  "url": "https://rest.uniprot.org/unisave/Q9W0M3?format=txt&versions=170"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9W0M3?format=txt&versions=170)

```json
{
  "entry_version": 170,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Jumonji C domain-containing protein 5 {ECO:0000305};\nDE            EC=1.14.11.73 {ECO:0000250|UniProtKB:Q8N371};\nDE            EC=3.4.-.- {ECO:0000250|UniProtKB:Q8N371};\nDE   AltName: Full=Lysine-specific demethylase 8 {ECO:0000305};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:45.948211+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-9",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "45e70668e7a96138303d865036cba4c2edb7da0e5634453cb9fbab186acc3750",
  "url": "https://rest.uniprot.org/unisave/Q9W0M3?format=txt&versions=170"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9W0M3?format=txt&versions=170)

```json
{
  "entry_version": 170,
  "evidence_id": "H3",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=Fe(2+); Xref=ChEBI:CHEBI:29033;\nCC         Evidence={ECO:0000250|UniProtKB:Q8N371};\nCC       Note=Binds 1 Fe(2+) ion per subunit. {ECO:0000250|UniProtKB:Q8N371};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:45.948211+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 107-110",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "45e70668e7a96138303d865036cba4c2edb7da0e5634453cb9fbab186acc3750",
  "url": "https://rest.uniprot.org/unisave/Q9W0M3?format=txt&versions=170"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 183. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
