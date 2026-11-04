# cofactor_0045

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/cofactor_0045.txt)

**Task:** `cofactor`  
**Expected answer:** **C** — Mg(2+)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MCGVLALILANQSSSAANDLHEALYVLQHRGQDAAGIATSTSSGHIHIRKKNGMAADVFQSGARLANLFGSMGIAHLRYPTAGGSANTEAQPFYVNSPYGICFAHNGNLINTVELRRYLDFEIHRHINSDSDSELMLNIFADELSETKKARVNTEDIFNGLSKMYQRCEGAWACTAMLAGFGVIGFRDAYGIRPLVMGSRPSSDGDGLDYMIASESIALDRLGFTNVRDIQPGEAVIVAKGAEPVFCQVAPRKSYTPDLFEYVYFARPDSVIDGISVYQSRQRMGRYLAARLLEVLGPEGIKEIDVVIPVPETSSPAAASVAHALNKPYCAGYIRNPYVFRTFIMPGQATRQKGVRRKLSAVKEEFKNRTILLVDDSIARGTTSREAISMAREAGVKKIIAACCSPEITYPHIYGIDLPSPHEMVAYERDNNDIAQNLGADRIVYQTLEDLQASCAEIARENDFQEPHTFENGVFSGQYVTPVPEGYFALLEKIRGTGRKEALDKSSKRL

[Multiple Choices]
A. Na(+)
B. heme
C. Mg(2+)
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

> The sequence-matched UniProt record annotates Mg(2+) as a cofactor, with one ion per subunit, but the evidence is transferred by similarity from P00497 rather than a direct measurement on this protein (C5; also H4). The record also annotates a &#91;4Fe-4S&#93; cluster, which is not among the choices (C6; H5). Thus Mg(2+) is supported as the keyed choice, though the choices do not represent every annotated cofactor.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with a phosphoribosylpyrophosphate amidotransferase: its glutamine-utilizing enzyme architecture and PRPP-dependent catalytic domain support a family-level inference. PRPP-processing enzymes commonly use Mg(2+) to coordinate the substrate’s phosphate groups, making Mg(2+) a meaningful choice over Na(+), heme, or tungstopterin. This is a transferable family/mechanism inference, not proof of the exact protein’s measured cofactor complement.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model could distinguish Mg(2+) using the sequence’s enzyme-family features and transferable knowledge of PRPP-dependent catalysis. The target-specific annotation is not necessary to make that choice among the offered alternatives.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although the source also annotates a &#91;4Fe-4S&#93; cluster, that cofactor is not an offered option; none of the other listed choices is comparably supported.


### Important caveats

- The Mg(2+) annotation is based on similarity evidence, not direct experimental confirmation for this exact protein.
- The enzyme may have more than one cofactor; the choices omit the annotated &#91;4Fe-4S&#93; cluster.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a phosphoribosylpyrophosphate amidotransferase: its glutamine-utilizing enzyme architecture and PRPP-dependent catalytic domain support a family-level inference. PRPP-processing enzymes commonly use Mg(2+) to coordinate the substrate’s phosphate groups, making Mg(2+) a meaningful choice over Na(+), heme, or tungstopterin. This is a transferable family/mechanism inference, not proof of the exact protein’s measured cofactor complement.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model could distinguish Mg(2+) using the sequence’s enzyme-family features and transferable knowledge of PRPP-dependent catalysis. The target-specific annotation is not necessary to make that choice among the offered alternatives."
  },
  "case_id": "cofactor_0045",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates Mg(2+) as a cofactor, with one ion per subunit, but the evidence is transferred by similarity from P00497 rather than a direct measurement on this protein (C5; also H4). The record also annotates a [4Fe-4S] cluster, which is not among the choices (C6; H5). Thus Mg(2+) is supported as the keyed choice, though the choices do not represent every annotated cofactor."
  },
  "important_caveats": [
    "The Mg(2+) annotation is based on similarity evidence, not direct experimental confirmation for this exact protein.",
    "The enzyme may have more than one cofactor; the choices omit the annotated [4Fe-4S] cluster."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the source also annotates a [4Fe-4S] cluster, that cofactor is not an offered option; none of the other listed choices is comparably supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0045",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates Mg(2+) as a cofactor, with one ion per subunit, but the evidence is transferred by similarity from P00497 rather than a direct measurement on this protein (C5; also H4). The record also annotates a [4Fe-4S] cluster, which is not among the choices (C6; H5). Thus Mg(2+) is supported as the keyed choice, though the choices do not represent every annotated cofactor.",
    "evidence_ids": ["C5", "C6", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with a phosphoribosylpyrophosphate amidotransferase: its glutamine-utilizing enzyme architecture and PRPP-dependent catalytic domain support a family-level inference. PRPP-processing enzymes commonly use Mg(2+) to coordinate the substrate’s phosphate groups, making Mg(2+) a meaningful choice over Na(+), heme, or tungstopterin. This is a transferable family/mechanism inference, not proof of the exact protein’s measured cofactor complement.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model could distinguish Mg(2+) using the sequence’s enzyme-family features and transferable knowledge of PRPP-dependent catalysis. The target-specific annotation is not necessary to make that choice among the offered alternatives."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the source also annotates a [4Fe-4S] cluster, that cofactor is not an offered option; none of the other listed choices is comparably supported."
  },
  "important_caveats": [
    "The Mg(2+) annotation is based on similarity evidence, not direct experimental confirmation for this exact protein.",
    "The enzyme may have more than one cofactor; the choices omit the annotated [4Fe-4S] cluster."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry for this sequence (A0A7T8J1U7, Phosphoribosylpyrophosphate amidotransferase FrzK, EC 2.4.2.14) explicitly lists Mg(2+) as a cofactor ('Binds 1 Mg(2+) ion per subunit'), annotated with evidence code ECO:0000250 (transferred from P00497, the E. coli PurF enzyme). The entry also lists &#91;4Fe-4S&#93; cluster, but that is not among the offered choices. Among the four options, Mg(2+) is the annotated cofactor and is the correct answer.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the CXGX motif (Cys-Glu-Gly-Ala in 'CEGAWACTAM') characteristic of class I glutamine amidotransferases, along with a C-terminal PRPP-binding domain. This identifies the protein as a member of the PRPP amidotransferase (PurF/amidophosphoribosyltransferase) family. From extensive knowledge of this family across E. coli PurF, human amidophosphoribosyltransferase, and other homologs, Mg(2+) is the universal, well-established divalent-metal cofactor that coordinates the PRPP substrate's pyrophosphate and ribose-5-phosphate moieties during catalysis. Among the offered choices: heme is for peroxidases/cytochromes (no heme-binding motifs present); tungstopterin is for tungsten-dependent oxidoreductases (completely unrelated enzyme class); Na(+) is not a recognized cofactor for phosphoribosyltransferases. Mg(2+) is the only biochemically sensible cofactor for a PRPP amidotransferase, making this a family-level inference well-supported by transferable knowledge.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Recognition of the class I amidotransferase family from the CXGX motif and overall domain architecture, combined with the textbook-level knowledge that Mg(2+) is the canonical cofactor for all PRPP amidotransferases (established from E. coli PurF, human ATase, and many other homologs), provides a concrete and highly reliable inference. The distractors are eliminated by basic cofactor-enzyme-class associations learned from many other proteins.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the four offered choices, only Mg(2+) is a recognized cofactor for PRPP amidotransferases. Heme, tungstopterin, and Na(+) are associated with entirely different enzyme classes and have no connection to phosphoribosyltransferase catalysis. The UniProt entry also lists &#91;4Fe-4S&#93; cluster, but that option was not offered, so no ambiguity exists among the given alternatives.


### Important caveats

- The Mg(2+) annotation is transferred by similarity (ECO:0000250) from E. coli PurF (P00497), not directly experimentally verified for FrzK, though the functional characterization in PubMed:33372776 supports the enzyme identity.
- The entry also annotates a &#91;4Fe-4S&#93; cluster as a cofactor (also by similarity transfer); this was not offered as a choice, so it does not create ambiguity among the given options.
- The CXGX motif recognition and family assignment are sequence-based inferences; the exact motif match ('CEGAWA') is consistent with class I amidotransferases but the full domain architecture confirmation would require structural or more detailed sequence analysis.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the CXGX motif (Cys-Glu-Gly-Ala in 'CEGAWACTAM') characteristic of class I glutamine amidotransferases, along with a C-terminal PRPP-binding domain. This identifies the protein as a member of the PRPP amidotransferase (PurF/amidophosphoribosyltransferase) family. From extensive knowledge of this family across E. coli PurF, human amidophosphoribosyltransferase, and other homologs, Mg(2+) is the universal, well-established divalent-metal cofactor that coordinates the PRPP substrate's pyrophosphate and ribose-5-phosphate moieties during catalysis. Among the offered choices: heme is for peroxidases/cytochromes (no heme-binding motifs present); tungstopterin is for tungsten-dependent oxidoreductases (completely unrelated enzyme class); Na(+) is not a recognized cofactor for phosphoribosyltransferases. Mg(2+) is the only biochemically sensible cofactor for a PRPP amidotransferase, making this a family-level inference well-supported by transferable knowledge.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Recognition of the class I amidotransferase family from the CXGX motif and overall domain architecture, combined with the textbook-level knowledge that Mg(2+) is the canonical cofactor for all PRPP amidotransferases (established from E. coli PurF, human ATase, and many other homologs), provides a concrete and highly reliable inference. The distractors are eliminated by basic cofactor-enzyme-class associations learned from many other proteins."
  },
  "case_id": "cofactor_0045",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry for this sequence (A0A7T8J1U7, Phosphoribosylpyrophosphate amidotransferase FrzK, EC 2.4.2.14) explicitly lists Mg(2+) as a cofactor ('Binds 1 Mg(2+) ion per subunit'), annotated with evidence code ECO:0000250 (transferred from P00497, the E. coli PurF enzyme). The entry also lists [4Fe-4S] cluster, but that is not among the offered choices. Among the four options, Mg(2+) is the annotated cofactor and is the correct answer."
  },
  "important_caveats": [
    "The Mg(2+) annotation is transferred by similarity (ECO:0000250) from E. coli PurF (P00497), not directly experimentally verified for FrzK, though the functional characterization in PubMed:33372776 supports the enzyme identity.",
    "The entry also annotates a [4Fe-4S] cluster as a cofactor (also by similarity transfer); this was not offered as a choice, so it does not create ambiguity among the given options.",
    "The CXGX motif recognition and family assignment are sequence-based inferences; the exact motif match ('CEGAWA') is consistent with class I amidotransferases but the full domain architecture confirmation would require structural or more detailed sequence analysis."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four offered choices, only Mg(2+) is a recognized cofactor for PRPP amidotransferases. Heme, tungstopterin, and Na(+) are associated with entirely different enzyme classes and have no connection to phosphoribosyltransferase catalysis. The UniProt entry also lists [4Fe-4S] cluster, but that option was not offered, so no ambiguity exists among the given alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0045",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry for this sequence (A0A7T8J1U7, Phosphoribosylpyrophosphate amidotransferase FrzK, EC 2.4.2.14) explicitly lists Mg(2+) as a cofactor ('Binds 1 Mg(2+) ion per subunit'), annotated with evidence code ECO:0000250 (transferred from P00497, the E. coli PurF enzyme). The entry also lists [4Fe-4S] cluster, but that is not among the offered choices. Among the four options, Mg(2+) is the annotated cofactor and is the correct answer.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the CXGX motif (Cys-Glu-Gly-Ala in 'CEGAWACTAM') characteristic of class I glutamine amidotransferases, along with a C-terminal PRPP-binding domain. This identifies the protein as a member of the PRPP amidotransferase (PurF/amidophosphoribosyltransferase) family. From extensive knowledge of this family across E. coli PurF, human amidophosphoribosyltransferase, and other homologs, Mg(2+) is the universal, well-established divalent-metal cofactor that coordinates the PRPP substrate's pyrophosphate and ribose-5-phosphate moieties during catalysis. Among the offered choices: heme is for peroxidases/cytochromes (no heme-binding motifs present); tungstopterin is for tungsten-dependent oxidoreductases (completely unrelated enzyme class); Na(+) is not a recognized cofactor for phosphoribosyltransferases. Mg(2+) is the only biochemically sensible cofactor for a PRPP amidotransferase, making this a family-level inference well-supported by transferable knowledge.",
    "missing_item_specific_fact": "",
    "reason": "Recognition of the class I amidotransferase family from the CXGX motif and overall domain architecture, combined with the textbook-level knowledge that Mg(2+) is the canonical cofactor for all PRPP amidotransferases (established from E. coli PurF, human ATase, and many other homologs), provides a concrete and highly reliable inference. The distractors are eliminated by basic cofactor-enzyme-class associations learned from many other proteins."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four offered choices, only Mg(2+) is a recognized cofactor for PRPP amidotransferases. Heme, tungstopterin, and Na(+) are associated with entirely different enzyme classes and have no connection to phosphoribosyltransferase catalysis. The UniProt entry also lists [4Fe-4S] cluster, but that option was not offered, so no ambiguity exists among the given alternatives."
  },
  "important_caveats": [
    "The Mg(2+) annotation is transferred by similarity (ECO:0000250) from E. coli PurF (P00497), not directly experimentally verified for FrzK, though the functional characterization in PubMed:33372776 supports the enzyme identity.",
    "The entry also annotates a [4Fe-4S] cluster as a cofactor (also by similarity transfer); this was not offered as a choice, so it does not create ambiguity among the given options.",
    "The CXGX motif recognition and family assignment are sequence-based inferences; the exact motif match ('CEGAWA') is consistent with class I amidotransferases but the full domain architecture confirmation would require structural or more detailed sequence analysis."
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
  "benchmark_sequence_length": 510,
  "benchmark_sequence_sha256": "44dc44e51fdf196ccecccc1dbeec4ed51df88981f809d29be8495d6c59ba2224",
  "current_entry_audit": {
    "entryVersion": 18,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2021-06-02",
    "sequenceVersion": 1
  },
  "current_record_sha256": "56665e1cd9e3380e3faeac05a356479129623641a0ef275c9308eeccf948063d",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 510,
  "current_source_sequence_sha256": "44dc44e51fdf196ccecccc1dbeec4ed51df88981f809d29be8495d6c59ba2224",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 16,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A7T8J1U7",
  "selected_historical_entry_version": 16,
  "selected_historical_record_sha256": "578ee5dbb88bc40f60a644a1dc0fae09acdb5d05f79fe55109621fabea2329a5",
  "selected_historical_source_sequence_length": 510,
  "selected_historical_source_sequence_sha256": "44dc44e51fdf196ccecccc1dbeec4ed51df88981f809d29be8495d6c59ba2224",
  "selected_historical_version": {
    "accession": "A0A7T8J1U7",
    "database": "Swiss-Prot",
    "entryVersion": 16,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "FRZK_CLASX",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8J1U7.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A7T8J1U7\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:25:51.826168+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "56665e1cd9e3380e3faeac05a356479129623641a0ef275c9308eeccf948063d",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8J1U7.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8J1U7.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":18,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2021-06-02\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:25:51.826168+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "56665e1cd9e3380e3faeac05a356479129623641a0ef275c9308eeccf948063d",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8J1U7.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8J1U7.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Sordariomycetes\",\"Hypocreomycetidae\",\"Hypocreales\",\"Hypocreaceae\",\"Cladobotryum\"],\"scientificName\":\"Cladobotryum sp\",\"taxonId\":2040732}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:25:51.826168+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "56665e1cd9e3380e3faeac05a356479129623641a0ef275c9308eeccf948063d",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8J1U7.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8J1U7.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33372776\",\"source\":\"PubMed\"}],\"value\":\"FR901483 biosynthesis clusters protein K\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33372776\",\"source\":\"PubMed\"}],\"value\":\"Glutamine phosphoribosylpyrophosphate amidotransferase\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"33372776\",\"source\":\"PubMed\"}],\"value\":\"2.4.2.14\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33372776\",\"source\":\"PubMed\"}],\"value\":\"Phosphoribosylpyrophosphate amidotransferase FrzK\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33372776\",\"source\":\"PubMed\"}],\"value\":\"ATase FrzK\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:25:51.826168+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "56665e1cd9e3380e3faeac05a356479129623641a0ef275c9308eeccf948063d",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8J1U7.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8J1U7.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:18420\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P00497\",\"source\":\"UniProtKB\"}],\"name\":\"Mg(2+)\"}],\"commentType\":\"COFACTOR\",\"note\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P00497\",\"source\":\"UniProtKB\"}],\"value\":\"Binds 1 Mg(2+) ion per subunit.\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:25:51.826168+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "56665e1cd9e3380e3faeac05a356479129623641a0ef275c9308eeccf948063d",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8J1U7.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8J1U7.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:49883\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P00497\",\"source\":\"UniProtKB\"}],\"name\":\"[4Fe-4S] cluster\"}],\"commentType\":\"COFACTOR\",\"note\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P00497\",\"source\":\"UniProtKB\"}],\"value\":\"Binds 1 [4Fe-4S] cluster per subunit.\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-02T04:25:51.826168+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "56665e1cd9e3380e3faeac05a356479129623641a0ef275c9308eeccf948063d",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8J1U7.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8J1U7.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Zhang Z.\",\"Tamura Y.\",\"Tang M.\",\"Qiao T.\",\"Sato M.\",\"Otsu Y.\",\"Sasamura S.\",\"Taniguchi M.\",\"Watanabe K.\",\"Tang Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"33372776\"},{\"database\":\"DOI\",\"id\":\"10.1021/jacs.0c12352\"}],\"citationType\":\"journal article\",\"firstPage\":\"132\",\"id\":\"33372776\",\"journal\":\"J. Am. Chem. Soc.\",\"lastPage\":\"136\",\"publicationDate\":\"2021\",\"title\":\"Biosynthesis of the Immunosuppressant (-)-FR901483.\",\"volume\":\"143\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"11231\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"FUNCTION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:25:51.826168+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "56665e1cd9e3380e3faeac05a356479129623641a0ef275c9308eeccf948063d",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8J1U7.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8J1U7?format=txt&versions=16)

```json
{
  "entry_version": 16,
  "evidence_id": "H1",
  "excerpt": "ID   FRZK_CLASX              Reviewed;         510 AA.\nAC   A0A7T8J1U7;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   02-JUN-2021, sequence version 1.\nDT   28-JAN-2026, entry version 16.\nDE   RecName: Full=Phosphoribosylpyrophosphate amidotransferase FrzK {ECO:0000303|PubMed:33372776};\nDE            Short=ATase FrzK {ECO:0000303|PubMed:33372776};\nDE            EC=2.4.2.14 {ECO:0000269|PubMed:33372776};\nDE   AltName: Full=FR901483 biosynthesis clusters protein K {ECO:0000303|PubMed:33372776};\nDE   AltName: Full=Glutamine phosphoribosylpyrophosphate amidotransferase {ECO:0000303|PubMed:33372776};\nGN   Name=FrzK {ECO:0000303|PubMed:33372776};\nOS   Cladobotryum sp.\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;\nOC   Hypocreomycetidae; Hypocreales; Hypocreaceae; Cladobotryum.\nOX   NCBI_TaxID=2040732;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:55.036238+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "578ee5dbb88bc40f60a644a1dc0fae09acdb5d05f79fe55109621fabea2329a5",
  "url": "https://rest.uniprot.org/unisave/A0A7T8J1U7?format=txt&versions=16"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8J1U7?format=txt&versions=16)

```json
{
  "entry_version": 16,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Phosphoribosylpyrophosphate amidotransferase FrzK {ECO:0000303|PubMed:33372776};\nDE            Short=ATase FrzK {ECO:0000303|PubMed:33372776};\nDE            EC=2.4.2.14 {ECO:0000269|PubMed:33372776};\nDE   AltName: Full=FR901483 biosynthesis clusters protein K {ECO:0000303|PubMed:33372776};\nDE   AltName: Full=Glutamine phosphoribosylpyrophosphate amidotransferase {ECO:0000303|PubMed:33372776};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:55.036238+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-10",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "578ee5dbb88bc40f60a644a1dc0fae09acdb5d05f79fe55109621fabea2329a5",
  "url": "https://rest.uniprot.org/unisave/A0A7T8J1U7?format=txt&versions=16"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8J1U7?format=txt&versions=16)

```json
{
  "entry_version": 16,
  "evidence_id": "H3",
  "excerpt": "RN   [1]\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], AND FUNCTION.\nRC   STRAIN=11231;\nRX   PubMed=33372776; DOI=10.1021/jacs.0c12352;\nRA   Zhang Z., Tamura Y., Tang M., Qiao T., Sato M., Otsu Y., Sasamura S.,\nRA   Taniguchi M., Watanabe K., Tang Y.;\nRT   \"Biosynthesis of the Immunosuppressant (-)-FR901483.\";\nRL   J. Am. Chem. Soc. 143:132-136(2021).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:55.036238+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 16-23",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "578ee5dbb88bc40f60a644a1dc0fae09acdb5d05f79fe55109621fabea2329a5",
  "url": "https://rest.uniprot.org/unisave/A0A7T8J1U7?format=txt&versions=16"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8J1U7?format=txt&versions=16)

```json
{
  "entry_version": 16,
  "evidence_id": "H4",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=Mg(2+); Xref=ChEBI:CHEBI:18420;\nCC         Evidence={ECO:0000250|UniProtKB:P00497};\nCC       Note=Binds 1 Mg(2+) ion per subunit. {ECO:0000250|UniProtKB:P00497};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:55.036238+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 44-47",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "578ee5dbb88bc40f60a644a1dc0fae09acdb5d05f79fe55109621fabea2329a5",
  "url": "https://rest.uniprot.org/unisave/A0A7T8J1U7?format=txt&versions=16"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8J1U7?format=txt&versions=16)

```json
{
  "entry_version": 16,
  "evidence_id": "H5",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=[4Fe-4S] cluster; Xref=ChEBI:CHEBI:49883;\nCC         Evidence={ECO:0000250|UniProtKB:P00497};\nCC       Note=Binds 1 [4Fe-4S] cluster per subunit.\nCC       {ECO:0000250|UniProtKB:P00497};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:55.036238+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 48-52",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "578ee5dbb88bc40f60a644a1dc0fae09acdb5d05f79fe55109621fabea2329a5",
  "url": "https://rest.uniprot.org/unisave/A0A7T8J1U7?format=txt&versions=16"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 45. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
