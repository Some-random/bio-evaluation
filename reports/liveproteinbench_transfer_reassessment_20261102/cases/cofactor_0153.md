# cofactor_0153

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/cofactor_0153.txt)

**Task:** `cofactor`  
**Expected answer:** **D** — NAD(+)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MFMREIELKGHIIDSFILAKVFDRTLELGGDYKVLEFDIGKKKIDTSYAKLLISGDTQQHLDQILEELQNVGANIPEIENANLKPALKDSVLPDGFYSTTNHPTHVKVNDEWIEVANPKMDAVIVVYPEEKRAETKVIRKVKKGDFVLIGHNGIRVMPPEKSREAGQLFEFMNSEVSSEKPKEAIIKRIAKEMHEIREEYKKTGTGGIAIVGGPAIIHTGGGPALAKMVELGYIQAILAGNALATHDIESALYGTSLGVNIKTAKPVTGGHKHHIYAINAINDAGNIKNAVESGVLKEGIMYQCIKNNIPYVLAGSIRDDGPIPDVITDSMVAQDKMRTTVMDKKMVIMLSTLLHSVATGNLMPSYIKTVCVDIQPSTVTKLMDRGTSQAIGVVTDVGVFLVLLLKELERLELQE

[Multiple Choices]
A. Co(2+)
B. [2Fe-2S] cluster
C. heme b
D. NAD(+)
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

> The sequence-matched UniProt record annotates NAD(+) as the cofactor, but the evidence is transferred from another UniProt entry (ECO:0000250), not direct experimental evidence for this exact protein. This supports the key while leaving that qualification.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a glycine-rich region around “TGTGGIAIVGGPA,” consistent with a dinucleotide-binding fold, and the sequence is compatible with the ornithine-cyclodeaminase family, whose transferable cofactor knowledge supports NAD(+). Among these choices, that points to D rather than a metal, iron-sulfur cluster, or heme cofactor.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A nucleotide-binding sequence pattern and family-level knowledge provide a meaningful basis to distinguish NAD(+) from the offered alternatives without knowing this protein’s recorded annotation. The sequence pattern alone is not definitive, and the source annotation itself is similarity-transferred.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No other offered choice has comparable support as the cofactor.


### Important caveats

- The reviewer-only record matches the supplied sequence.
- The cited cofactor evidence is transferred by similarity; it does not establish direct experimental verification for this exact protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a glycine-rich region around “TGTGGIAIVGGPA,” consistent with a dinucleotide-binding fold, and the sequence is compatible with the ornithine-cyclodeaminase family, whose transferable cofactor knowledge supports NAD(+). Among these choices, that points to D rather than a metal, iron-sulfur cluster, or heme cofactor.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A nucleotide-binding sequence pattern and family-level knowledge provide a meaningful basis to distinguish NAD(+) from the offered alternatives without knowing this protein’s recorded annotation. The sequence pattern alone is not definitive, and the source annotation itself is similarity-transferred."
  },
  "case_id": "cofactor_0153",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates NAD(+) as the cofactor, but the evidence is transferred from another UniProt entry (ECO:0000250), not direct experimental evidence for this exact protein. This supports the key while leaving that qualification."
  },
  "important_caveats": [
    "The reviewer-only record matches the supplied sequence.",
    "The cited cofactor evidence is transferred by similarity; it does not establish direct experimental verification for this exact protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered choice has comparable support as the cofactor."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0153",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates NAD(+) as the cofactor, but the evidence is transferred from another UniProt entry (ECO:0000250), not direct experimental evidence for this exact protein. This supports the key while leaving that qualification.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a glycine-rich region around “TGTGGIAIVGGPA,” consistent with a dinucleotide-binding fold, and the sequence is compatible with the ornithine-cyclodeaminase family, whose transferable cofactor knowledge supports NAD(+). Among these choices, that points to D rather than a metal, iron-sulfur cluster, or heme cofactor.",
    "missing_item_specific_fact": "",
    "reason": "A nucleotide-binding sequence pattern and family-level knowledge provide a meaningful basis to distinguish NAD(+) from the offered alternatives without knowing this protein’s recorded annotation. The sequence pattern alone is not definitive, and the source annotation itself is similarity-transferred."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered choice has comparable support as the cofactor."
  },
  "important_caveats": [
    "The reviewer-only record matches the supplied sequence.",
    "The cited cofactor evidence is transferred by similarity; it does not establish direct experimental verification for this exact protein."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q6LXX7 (exact sequence match) annotates the cofactor as NAD(+) (CHEBI:57540) with evidence code ECO:0000250 (inferred by similarity from Q8YMD9, the well-characterized bacterial ornithine cyclodeaminase). The protein is annotated as Ornithine cyclodeaminase (EC 4.3.1.12, experimentally supported by ECO:0000269/PubMed:30636068). The OCD family's NAD(+) dependence is well-established from the extensively studied bacterial enzyme. The cofactor assignment for this specific archaeal protein is by similarity rather than direct experiment, but it is consistent with the family-level biochemistry and the EC number assignment.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4), [C4](#evidence-c4), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a recognizable Rossmann-fold-like NAD(P)-binding motif: 'GGPAIIHTGGGPALAK' within a hydrophobic stretch, which is characteristic of the GxGxxG-type dinucleotide-binding domain found in NAD-dependent enzymes. Ornithine cyclodeaminase (EC 4.3.1.12) is a well-studied family (bacterial OCD from Pseudomonas putida is the paradigm) that uses NAD(+) as a catalytic cofactor via a Rossmann-fold domain; the sequence's overall architecture and these GG-motif features are consistent with this family. The alternatives can be meaningfully excluded: (A) Co(2+) (cobalamin) enzymes have distinct RxxHx cobalamin-binding motifs absent here; (B) &#91;2Fe-2S&#93; clusters require Cys-rich motifs (CxxCxxC patterns) not present in this sequence; (C) heme b binding requires specific His/Cys residues in defined structural contexts not evident here. The combination of Rossmann-fold sequence features and OCD-family homology (learned from bacterial homologs) provides a concrete, transferable inference favoring NAD(+).


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can recognize the Rossmann-fold GG motifs in the sequence, associate them with NAD(P)-binding domains, and use family-level knowledge of ornithine cyclodeaminase (well-characterized in bacteria) to identify NAD(+) as the cofactor. The three distractors lack their characteristic sequence signatures in this protein, allowing meaningful elimination.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The Rossmann-fold motifs and OCD-family context point specifically to NAD(+). The other three cofactors (Co2+/cobalamin, &#91;2Fe-2S&#93;, heme b) require distinctive sequence features (cobalamin-binding motifs, Cys-rich cluster motifs, heme-ligating residues in specific geometry) that are absent from this sequence. No genuine ambiguity exists among the offered choices.


### Important caveats

- The cofactor annotation for this specific archaeal protein carries evidence code ECO:0000250 (inferred by similarity from Q8YMD9), not direct experimental measurement on this enzyme. However, the EC assignment (4.3.1.12) is experimentally supported (ECO:0000269), and the OCD family's NAD(+) dependence is well-established.
- The sequence-match to UniProt Q6LXX7 is exact (SHA256 confirmed), confirming the protein identity.
- The Rossmann-fold motif in this sequence ('GGPAIIHTGGGPALAK') is somewhat degenerate compared to the canonical GxGxxG consensus, but it falls within the range of NAD-binding motifs observed in the OCD/glutamate-synthase superfamily.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a recognizable Rossmann-fold-like NAD(P)-binding motif: 'GGPAIIHTGGGPALAK' within a hydrophobic stretch, which is characteristic of the GxGxxG-type dinucleotide-binding domain found in NAD-dependent enzymes. Ornithine cyclodeaminase (EC 4.3.1.12) is a well-studied family (bacterial OCD from Pseudomonas putida is the paradigm) that uses NAD(+) as a catalytic cofactor via a Rossmann-fold domain; the sequence's overall architecture and these GG-motif features are consistent with this family. The alternatives can be meaningfully excluded: (A) Co(2+) (cobalamin) enzymes have distinct RxxHx cobalamin-binding motifs absent here; (B) [2Fe-2S] clusters require Cys-rich motifs (CxxCxxC patterns) not present in this sequence; (C) heme b binding requires specific His/Cys residues in defined structural contexts not evident here. The combination of Rossmann-fold sequence features and OCD-family homology (learned from bacterial homologs) provides a concrete, transferable inference favoring NAD(+).",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the Rossmann-fold GG motifs in the sequence, associate them with NAD(P)-binding domains, and use family-level knowledge of ornithine cyclodeaminase (well-characterized in bacteria) to identify NAD(+) as the cofactor. The three distractors lack their characteristic sequence signatures in this protein, allowing meaningful elimination."
  },
  "case_id": "cofactor_0153",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4",
      "C4",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q6LXX7 (exact sequence match) annotates the cofactor as NAD(+) (CHEBI:57540) with evidence code ECO:0000250 (inferred by similarity from Q8YMD9, the well-characterized bacterial ornithine cyclodeaminase). The protein is annotated as Ornithine cyclodeaminase (EC 4.3.1.12, experimentally supported by ECO:0000269/PubMed:30636068). The OCD family's NAD(+) dependence is well-established from the extensively studied bacterial enzyme. The cofactor assignment for this specific archaeal protein is by similarity rather than direct experiment, but it is consistent with the family-level biochemistry and the EC number assignment."
  },
  "important_caveats": [
    "The cofactor annotation for this specific archaeal protein carries evidence code ECO:0000250 (inferred by similarity from Q8YMD9), not direct experimental measurement on this enzyme. However, the EC assignment (4.3.1.12) is experimentally supported (ECO:0000269), and the OCD family's NAD(+) dependence is well-established.",
    "The sequence-match to UniProt Q6LXX7 is exact (SHA256 confirmed), confirming the protein identity.",
    "The Rossmann-fold motif in this sequence ('GGPAIIHTGGGPALAK') is somewhat degenerate compared to the canonical GxGxxG consensus, but it falls within the range of NAD-binding motifs observed in the OCD/glutamate-synthase superfamily."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The Rossmann-fold motifs and OCD-family context point specifically to NAD(+). The other three cofactors (Co2+/cobalamin, [2Fe-2S], heme b) require distinctive sequence features (cobalamin-binding motifs, Cys-rich cluster motifs, heme-ligating residues in specific geometry) that are absent from this sequence. No genuine ambiguity exists among the offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0153",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q6LXX7 (exact sequence match) annotates the cofactor as NAD(+) (CHEBI:57540) with evidence code ECO:0000250 (inferred by similarity from Q8YMD9, the well-characterized bacterial ornithine cyclodeaminase). The protein is annotated as Ornithine cyclodeaminase (EC 4.3.1.12, experimentally supported by ECO:0000269/PubMed:30636068). The OCD family's NAD(+) dependence is well-established from the extensively studied bacterial enzyme. The cofactor assignment for this specific archaeal protein is by similarity rather than direct experiment, but it is consistent with the family-level biochemistry and the EC number assignment.",
    "evidence_ids": ["C5", "H4", "C4", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a recognizable Rossmann-fold-like NAD(P)-binding motif: 'GGPAIIHTGGGPALAK' within a hydrophobic stretch, which is characteristic of the GxGxxG-type dinucleotide-binding domain found in NAD-dependent enzymes. Ornithine cyclodeaminase (EC 4.3.1.12) is a well-studied family (bacterial OCD from Pseudomonas putida is the paradigm) that uses NAD(+) as a catalytic cofactor via a Rossmann-fold domain; the sequence's overall architecture and these GG-motif features are consistent with this family. The alternatives can be meaningfully excluded: (A) Co(2+) (cobalamin) enzymes have distinct RxxHx cobalamin-binding motifs absent here; (B) [2Fe-2S] clusters require Cys-rich motifs (CxxCxxC patterns) not present in this sequence; (C) heme b binding requires specific His/Cys residues in defined structural contexts not evident here. The combination of Rossmann-fold sequence features and OCD-family homology (learned from bacterial homologs) provides a concrete, transferable inference favoring NAD(+).",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the Rossmann-fold GG motifs in the sequence, associate them with NAD(P)-binding domains, and use family-level knowledge of ornithine cyclodeaminase (well-characterized in bacteria) to identify NAD(+) as the cofactor. The three distractors lack their characteristic sequence signatures in this protein, allowing meaningful elimination."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The Rossmann-fold motifs and OCD-family context point specifically to NAD(+). The other three cofactors (Co2+/cobalamin, [2Fe-2S], heme b) require distinctive sequence features (cobalamin-binding motifs, Cys-rich cluster motifs, heme-ligating residues in specific geometry) that are absent from this sequence. No genuine ambiguity exists among the offered choices."
  },
  "important_caveats": [
    "The cofactor annotation for this specific archaeal protein carries evidence code ECO:0000250 (inferred by similarity from Q8YMD9), not direct experimental measurement on this enzyme. However, the EC assignment (4.3.1.12) is experimentally supported (ECO:0000269), and the OCD family's NAD(+) dependence is well-established.",
    "The sequence-match to UniProt Q6LXX7 is exact (SHA256 confirmed), confirming the protein identity.",
    "The Rossmann-fold motif in this sequence ('GGPAIIHTGGGPALAK') is somewhat degenerate compared to the canonical GxGxxG consensus, but it falls within the range of NAD-binding motifs observed in the OCD/glutamate-synthase superfamily."
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
  "benchmark_sequence_length": 415,
  "benchmark_sequence_sha256": "355b4d824ba114e0b6eb06dbc86bbba020b6e400b3af07fafa23ce7ab0b5684b",
  "current_entry_audit": {
    "entryVersion": 102,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2004-07-05",
    "sequenceVersion": 1
  },
  "current_record_sha256": "3e88c87b8e607d8f9da2f5b9ef0b835869c5da2ca430a53bbee11e2710822d63",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 415,
  "current_source_sequence_sha256": "355b4d824ba114e0b6eb06dbc86bbba020b6e400b3af07fafa23ce7ab0b5684b",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 100,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q6LXX7",
  "selected_historical_entry_version": 100,
  "selected_historical_record_sha256": "fb75c52fd5da78db70bc1f15507ff585eec805f8d1c74be8d2e60b19ae2897fb",
  "selected_historical_source_sequence_length": 415,
  "selected_historical_source_sequence_sha256": "355b4d824ba114e0b6eb06dbc86bbba020b6e400b3af07fafa23ce7ab0b5684b",
  "selected_historical_version": {
    "accession": "Q6LXX7",
    "database": "Swiss-Prot",
    "entryVersion": 100,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "AOCD_METMP",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6LXX7.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q6LXX7\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:31:35.053650+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3e88c87b8e607d8f9da2f5b9ef0b835869c5da2ca430a53bbee11e2710822d63",
  "url": "https://rest.uniprot.org/uniprotkb/Q6LXX7.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6LXX7.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":102,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2004-07-05\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:31:35.053650+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3e88c87b8e607d8f9da2f5b9ef0b835869c5da2ca430a53bbee11e2710822d63",
  "url": "https://rest.uniprot.org/uniprotkb/Q6LXX7.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6LXX7.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Archaea\",\"Methanobacteriati\",\"Methanobacteriota\",\"Methanomada group\",\"Methanococci\",\"Methanococcales\",\"Methanococcaceae\",\"Methanococcus\"],\"scientificName\":\"Methanococcus maripaludis (strain DSM 14266 / JCM 13030 / NBRC 101832 / S2 / LL)\",\"taxonId\":267377}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:31:35.053650+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3e88c87b8e607d8f9da2f5b9ef0b835869c5da2ca430a53bbee11e2710822d63",
  "url": "https://rest.uniprot.org/uniprotkb/Q6LXX7.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6LXX7.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30636068\",\"source\":\"PubMed\"}],\"value\":\"Archaeal ornithine cyclodeaminase\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30636068\",\"source\":\"PubMed\"}],\"value\":\"Mls2\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"30636068\",\"source\":\"PubMed\"}],\"value\":\"4.3.1.12\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30636068\",\"source\":\"PubMed\"}],\"value\":\"Ornithine cyclodeaminase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"OCD\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:31:35.053650+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3e88c87b8e607d8f9da2f5b9ef0b835869c5da2ca430a53bbee11e2710822d63",
  "url": "https://rest.uniprot.org/uniprotkb/Q6LXX7.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6LXX7.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:57540\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8YMD9\",\"source\":\"UniProtKB\"}],\"name\":\"NAD(+)\"}],\"commentType\":\"COFACTOR\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:31:35.053650+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3e88c87b8e607d8f9da2f5b9ef0b835869c5da2ca430a53bbee11e2710822d63",
  "url": "https://rest.uniprot.org/uniprotkb/Q6LXX7.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6LXX7.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Burnat M.\",\"Picossi S.\",\"Valladares A.\",\"Herrero A.\",\"Flores E.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"30636068\"},{\"database\":\"DOI\",\"id\":\"10.1111/mmi.14203\"}],\"citationType\":\"journal article\",\"firstPage\":\"883\",\"id\":\"30636068\",\"journal\":\"Mol. Microbiol.\",\"lastPage\":\"897\",\"publicationDate\":\"2019\",\"title\":\"Catabolic pathway of arginine in Anabaena involves a novel bifunctional enzyme that produces proline from arginine.\",\"volume\":\"111\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"DSM 14266 / JCM 13030 / NBRC 101832 / S2 / LL\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:31:35.053650+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3e88c87b8e607d8f9da2f5b9ef0b835869c5da2ca430a53bbee11e2710822d63",
  "url": "https://rest.uniprot.org/uniprotkb/Q6LXX7.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6LXX7?format=txt&versions=100)

```json
{
  "entry_version": 100,
  "evidence_id": "H1",
  "excerpt": "ID   AOCD_METMP              Reviewed;         415 AA.\nAC   Q6LXX7;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-JUL-2004, sequence version 1.\nDT   28-JAN-2026, entry version 100.\nDE   RecName: Full=Ornithine cyclodeaminase {ECO:0000303|PubMed:30636068};\nDE            Short=OCD {ECO:0000305};\nDE            EC=4.3.1.12 {ECO:0000269|PubMed:30636068};\nDE   AltName: Full=Archaeal ornithine cyclodeaminase {ECO:0000303|PubMed:30636068};\nDE   AltName: Full=Mls2 {ECO:0000303|PubMed:30636068};\nGN   OrderedLocusNames=MMP1218 {ECO:0000312|EMBL:CAF30774.1};\nOS   Methanococcus maripaludis (strain DSM 14266 / JCM 13030 / NBRC 101832 / S2\nOS   / LL).\nOC   Archaea; Methanobacteriati; Methanobacteriota; Methanomada group;\nOC   Methanococci; Methanococcales; Methanococcaceae; Methanococcus.\nOX   NCBI_TaxID=267377;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:37.153182+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "fb75c52fd5da78db70bc1f15507ff585eec805f8d1c74be8d2e60b19ae2897fb",
  "url": "https://rest.uniprot.org/unisave/Q6LXX7?format=txt&versions=100"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6LXX7?format=txt&versions=100)

```json
{
  "entry_version": 100,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Ornithine cyclodeaminase {ECO:0000303|PubMed:30636068};\nDE            Short=OCD {ECO:0000305};\nDE            EC=4.3.1.12 {ECO:0000269|PubMed:30636068};\nDE   AltName: Full=Archaeal ornithine cyclodeaminase {ECO:0000303|PubMed:30636068};\nDE   AltName: Full=Mls2 {ECO:0000303|PubMed:30636068};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:37.153182+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-10",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "fb75c52fd5da78db70bc1f15507ff585eec805f8d1c74be8d2e60b19ae2897fb",
  "url": "https://rest.uniprot.org/unisave/Q6LXX7?format=txt&versions=100"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6LXX7?format=txt&versions=100)

```json
{
  "entry_version": 100,
  "evidence_id": "H3",
  "excerpt": "RN   [2]\nRP   FUNCTION, AND CATALYTIC ACTIVITY.\nRC   STRAIN=DSM 14266 / JCM 13030 / NBRC 101832 / S2 / LL;\nRX   PubMed=30636068; DOI=10.1111/mmi.14203;\nRA   Burnat M., Picossi S., Valladares A., Herrero A., Flores E.;\nRT   \"Catabolic pathway of arginine in Anabaena involves a novel bifunctional\nRT   enzyme that produces proline from arginine.\";\nRL   Mol. Microbiol. 111:883-897(2019).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:37.153182+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 30-37",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "fb75c52fd5da78db70bc1f15507ff585eec805f8d1c74be8d2e60b19ae2897fb",
  "url": "https://rest.uniprot.org/unisave/Q6LXX7?format=txt&versions=100"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6LXX7?format=txt&versions=100)

```json
{
  "entry_version": 100,
  "evidence_id": "H4",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=NAD(+); Xref=ChEBI:CHEBI:57540;\nCC         Evidence={ECO:0000250|UniProtKB:Q8YMD9};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:37.153182+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 50-52",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "fb75c52fd5da78db70bc1f15507ff585eec805f8d1c74be8d2e60b19ae2897fb",
  "url": "https://rest.uniprot.org/unisave/Q6LXX7?format=txt&versions=100"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 153. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
