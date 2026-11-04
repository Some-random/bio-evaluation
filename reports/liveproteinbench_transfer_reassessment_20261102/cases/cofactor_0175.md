# cofactor_0175

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/cofactor_0175.txt)

**Task:** `cofactor`  
**Expected answer:** **A** — Mg(2+)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MKPLVIFDLDGTLVDTPSGIVSAFITALRDLSMPFEDRRAIRATIGLPLEKAFGQILALPVEDERVTAAVRQYQAVFREQVLPQAPGLVFPGVVEGLALLKGQGYTLAVATSKVFASAKALLEAAGLWSYFDLVLGADMVAHPKPHPEMGLLAMSRLGADAATTAMVGDTTHDLLMAKQAGMAAIGVTWGIHTTDQLKAAEPQVIVDTFSEVVGAAHALLKLSSSPVSYC

[Multiple Choices]
A. Mg(2+)
B. [4Fe-4S] cluster
C. Mn(2+)
D. FAD
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

> The sequence-matched UniProt record annotates Mg(2+) as the cofactor, with the annotation transferred from another UniProt entry (ECO:0000250), rather than presented as direct experimental evidence for this protein. This is consistent with the protein being annotated as a probable phosphatase, but the evidence is computational and qualified.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence begins with an Asp-x-Asp-x-Thr motif (DLDGT), characteristic of HAD-like phosphatases. Such phosphatases commonly use Mg(2+) in catalysis, making Mg(2+) a meaningful choice over the offered Fe-S cluster or FAD; Mn(2+) is a possible metal alternative in some enzymes but is less typical.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A transferable phosphatase-family motif and its usual metal-dependent catalytic chemistry provide a credible, if probabilistic, basis for selecting Mg(2+) without knowing this exact protein's database annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence motif and phosphatase-family pattern favor Mg(2+) among the listed options. The possibility that some related enzymes can use another divalent metal does not make another offered choice equally defensible here.


### Important caveats

- The supplied record's Mg(2+) annotation is based on transfer by similarity, not direct experimental evidence establishing the cofactor for this exact protein.
- The sequence-based family inference supports Mg(2+) but does not by itself demonstrate strict requirement or exclude possible metal substitution.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence begins with an Asp-x-Asp-x-Thr motif (DLDGT), characteristic of HAD-like phosphatases. Such phosphatases commonly use Mg(2+) in catalysis, making Mg(2+) a meaningful choice over the offered Fe-S cluster or FAD; Mn(2+) is a possible metal alternative in some enzymes but is less typical.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A transferable phosphatase-family motif and its usual metal-dependent catalytic chemistry provide a credible, if probabilistic, basis for selecting Mg(2+) without knowing this exact protein's database annotation."
  },
  "case_id": "cofactor_0175",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates Mg(2+) as the cofactor, with the annotation transferred from another UniProt entry (ECO:0000250), rather than presented as direct experimental evidence for this protein. This is consistent with the protein being annotated as a probable phosphatase, but the evidence is computational and qualified."
  },
  "important_caveats": [
    "The supplied record's Mg(2+) annotation is based on transfer by similarity, not direct experimental evidence establishing the cofactor for this exact protein.",
    "The sequence-based family inference supports Mg(2+) but does not by itself demonstrate strict requirement or exclude possible metal substitution."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence motif and phosphatase-family pattern favor Mg(2+) among the listed options. The possibility that some related enzymes can use another divalent metal does not make another offered choice equally defensible here."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0175",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates Mg(2+) as the cofactor, with the annotation transferred from another UniProt entry (ECO:0000250), rather than presented as direct experimental evidence for this protein. This is consistent with the protein being annotated as a probable phosphatase, but the evidence is computational and qualified.",
    "evidence_ids": ["C4", "C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence begins with an Asp-x-Asp-x-Thr motif (DLDGT), characteristic of HAD-like phosphatases. Such phosphatases commonly use Mg(2+) in catalysis, making Mg(2+) a meaningful choice over the offered Fe-S cluster or FAD; Mn(2+) is a possible metal alternative in some enzymes but is less typical.",
    "missing_item_specific_fact": "",
    "reason": "A transferable phosphatase-family motif and its usual metal-dependent catalytic chemistry provide a credible, if probabilistic, basis for selecting Mg(2+) without knowing this exact protein's database annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence motif and phosphatase-family pattern favor Mg(2+) among the listed options. The possibility that some related enzymes can use another divalent metal does not make another offered choice equally defensible here."
  },
  "important_caveats": [
    "The supplied record's Mg(2+) annotation is based on transfer by similarity, not direct experimental evidence establishing the cofactor for this exact protein.",
    "The sequence-based family inference supports Mg(2+) but does not by itself demonstrate strict requirement or exclude possible metal substitution."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q9L392 annotates Mg(2+) as the cofactor (CHEBI:18420) for this 'Probable phosphatase IndB' (EC 3.-.-.-). However, the evidence code is ECO:0000250 (inferred by similarity from Q96GD0), meaning the annotation is a computational transfer rather than direct experimental verification. The protein's function itself is also labeled 'Probable.' The annotation is consistent with general phosphatase biochemistry but is not experimentally confirmed for this exact protein.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> From the 230-aa sequence, a knowledgeable model can apply transferable phosphatase/cofactor knowledge: (1) The sequence contains only a single cysteine (the terminal C), making a 4Fe-4S cluster (requiring 4+ Cys in CxxC/CxxxC spacing) essentially impossible — rules out B. (2) No Rossmann-fold GxGxxG or FAD-binding motifs are present, and the small size and lack of oxidoreductase features argue against FAD — rules out D. (3) The protein is a small hydrolase/phosphatase (EC 3.-.-.-), a class overwhelmingly associated with divalent metal ions. Between Mg(2+) and Mn(2+): Mg(2+) is the most common phosphatase cofactor across the PDB and enzyme databases; Mn(2+) is preferentially associated with superoxide dismutases, certain oxidoreductases, and a minority of phosphatases. The statistical regularity learned from many other phosphatases meaningfully favors Mg(2+) over Mn(2+), though the distinction is probabilistic rather than deterministic.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The elimination of 4Fe-4S (no Cys cluster) and FAD (no binding motif) relies on sequence inspection plus general structural biology. The Mg(2+) vs Mn(2+) preference for a general phosphatase is a well-established statistical pattern across thousands of characterized enzymes, constituting legitimate transferable knowledge. The argument does not require knowing this exact protein's database annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "C"
]
```

> Mg(2+) and Mn(2+) are both common divalent-metal cofactors for phosphatases, and distinguishing them purely from a 230-aa sequence without a clear metal-binding motif signature is genuinely difficult. The preference for Mg(2+) rests on a statistical tendency across the phosphatase superfamily rather than a hard sequence determinant. A model could reasonably argue for Mn(2+) if it identified subtle coordination geometry preferences, though the overall evidence favors Mg(2+).


### Important caveats

- The UniProt cofactor annotation is by similarity (ECO:0000250 from Q96GD0), not experimental. The protein function itself is 'Probable.'
- The Mg(2+) vs Mn(2+) distinction is probabilistic based on population statistics of phosphatase cofactors, not a hard sequence rule.
- The protein's role in indigoidine biosynthesis (from the referenced PubMed paper) provides biological context but was not given to the evaluated model.
- The single terminal cysteine strongly but not absolutely excludes 4Fe-4S; a non-canonical cluster binding site cannot be fully ruled out from primary sequence alone.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "From the 230-aa sequence, a knowledgeable model can apply transferable phosphatase/cofactor knowledge: (1) The sequence contains only a single cysteine (the terminal C), making a 4Fe-4S cluster (requiring 4+ Cys in CxxC/CxxxC spacing) essentially impossible — rules out B. (2) No Rossmann-fold GxGxxG or FAD-binding motifs are present, and the small size and lack of oxidoreductase features argue against FAD — rules out D. (3) The protein is a small hydrolase/phosphatase (EC 3.-.-.-), a class overwhelmingly associated with divalent metal ions. Between Mg(2+) and Mn(2+): Mg(2+) is the most common phosphatase cofactor across the PDB and enzyme databases; Mn(2+) is preferentially associated with superoxide dismutases, certain oxidoreductases, and a minority of phosphatases. The statistical regularity learned from many other phosphatases meaningfully favors Mg(2+) over Mn(2+), though the distinction is probabilistic rather than deterministic.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The elimination of 4Fe-4S (no Cys cluster) and FAD (no binding motif) relies on sequence inspection plus general structural biology. The Mg(2+) vs Mn(2+) preference for a general phosphatase is a well-established statistical pattern across thousands of characterized enzymes, constituting legitimate transferable knowledge. The argument does not require knowing this exact protein's database annotation."
  },
  "case_id": "cofactor_0175",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q9L392 annotates Mg(2+) as the cofactor (CHEBI:18420) for this 'Probable phosphatase IndB' (EC 3.-.-.-). However, the evidence code is ECO:0000250 (inferred by similarity from Q96GD0), meaning the annotation is a computational transfer rather than direct experimental verification. The protein's function itself is also labeled 'Probable.' The annotation is consistent with general phosphatase biochemistry but is not experimentally confirmed for this exact protein."
  },
  "important_caveats": [
    "The UniProt cofactor annotation is by similarity (ECO:0000250 from Q96GD0), not experimental. The protein function itself is 'Probable.'",
    "The Mg(2+) vs Mn(2+) distinction is probabilistic based on population statistics of phosphatase cofactors, not a hard sequence rule.",
    "The protein's role in indigoidine biosynthesis (from the referenced PubMed paper) provides biological context but was not given to the evaluated model.",
    "The single terminal cysteine strongly but not absolutely excludes 4Fe-4S; a non-canonical cluster binding site cannot be fully ruled out from primary sequence alone."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "C"
    ],
    "reason": "Mg(2+) and Mn(2+) are both common divalent-metal cofactors for phosphatases, and distinguishing them purely from a 230-aa sequence without a clear metal-binding motif signature is genuinely difficult. The preference for Mg(2+) rests on a statistical tendency across the phosphatase superfamily rather than a hard sequence determinant. A model could reasonably argue for Mn(2+) if it identified subtle coordination geometry preferences, though the overall evidence favors Mg(2+)."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0175",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q9L392 annotates Mg(2+) as the cofactor (CHEBI:18420) for this 'Probable phosphatase IndB' (EC 3.-.-.-). However, the evidence code is ECO:0000250 (inferred by similarity from Q96GD0), meaning the annotation is a computational transfer rather than direct experimental verification. The protein's function itself is also labeled 'Probable.' The annotation is consistent with general phosphatase biochemistry but is not experimentally confirmed for this exact protein.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "From the 230-aa sequence, a knowledgeable model can apply transferable phosphatase/cofactor knowledge: (1) The sequence contains only a single cysteine (the terminal C), making a 4Fe-4S cluster (requiring 4+ Cys in CxxC/CxxxC spacing) essentially impossible — rules out B. (2) No Rossmann-fold GxGxxG or FAD-binding motifs are present, and the small size and lack of oxidoreductase features argue against FAD — rules out D. (3) The protein is a small hydrolase/phosphatase (EC 3.-.-.-), a class overwhelmingly associated with divalent metal ions. Between Mg(2+) and Mn(2+): Mg(2+) is the most common phosphatase cofactor across the PDB and enzyme databases; Mn(2+) is preferentially associated with superoxide dismutases, certain oxidoreductases, and a minority of phosphatases. The statistical regularity learned from many other phosphatases meaningfully favors Mg(2+) over Mn(2+), though the distinction is probabilistic rather than deterministic.",
    "missing_item_specific_fact": "",
    "reason": "The elimination of 4Fe-4S (no Cys cluster) and FAD (no binding motif) relies on sequence inspection plus general structural biology. The Mg(2+) vs Mn(2+) preference for a general phosphatase is a well-established statistical pattern across thousands of characterized enzymes, constituting legitimate transferable knowledge. The argument does not require knowing this exact protein's database annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "C"],
    "reason": "Mg(2+) and Mn(2+) are both common divalent-metal cofactors for phosphatases, and distinguishing them purely from a 230-aa sequence without a clear metal-binding motif signature is genuinely difficult. The preference for Mg(2+) rests on a statistical tendency across the phosphatase superfamily rather than a hard sequence determinant. A model could reasonably argue for Mn(2+) if it identified subtle coordination geometry preferences, though the overall evidence favors Mg(2+)."
  },
  "important_caveats": [
    "The UniProt cofactor annotation is by similarity (ECO:0000250 from Q96GD0), not experimental. The protein function itself is 'Probable.'",
    "The Mg(2+) vs Mn(2+) distinction is probabilistic based on population statistics of phosphatase cofactors, not a hard sequence rule.",
    "The protein's role in indigoidine biosynthesis (from the referenced PubMed paper) provides biological context but was not given to the evaluated model.",
    "The single terminal cysteine strongly but not absolutely excludes 4Fe-4S; a non-canonical cluster binding site cannot be fully ruled out from primary sequence alone."
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
  "benchmark_sequence_length": 230,
  "benchmark_sequence_sha256": "b7967041b35792185c1644d9b504fb694f8ba3684cfea21d3146e4216c733f75",
  "current_entry_audit": {
    "entryVersion": 72,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2000-10-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "bddaf2ccac530c5a545466788630afc91cfbda30f65717bd8f62c9d8fe9978e0",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 230,
  "current_source_sequence_sha256": "b7967041b35792185c1644d9b504fb694f8ba3684cfea21d3146e4216c733f75",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 71,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q9L392",
  "selected_historical_entry_version": 71,
  "selected_historical_record_sha256": "5062c8957159a8ea1cb613ad377d60f1c0ce04c5d973f743ddaad87c0f43abe1",
  "selected_historical_source_sequence_length": 230,
  "selected_historical_source_sequence_sha256": "b7967041b35792185c1644d9b504fb694f8ba3684cfea21d3146e4216c733f75",
  "selected_historical_version": {
    "accession": "Q9L392",
    "database": "Swiss-Prot",
    "entryVersion": 71,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "INDB_DICD3",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9L392.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q9L392\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:33:04.419071+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bddaf2ccac530c5a545466788630afc91cfbda30f65717bd8f62c9d8fe9978e0",
  "url": "https://rest.uniprot.org/uniprotkb/Q9L392.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9L392.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":72,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2000-10-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:33:04.419071+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bddaf2ccac530c5a545466788630afc91cfbda30f65717bd8f62c9d8fe9978e0",
  "url": "https://rest.uniprot.org/uniprotkb/Q9L392.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9L392.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Erwinia chrysanthemi (strain 3937)\",\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Pseudomonadota\",\"Gammaproteobacteria\",\"Enterobacterales\",\"Pectobacteriaceae\",\"Dickeya\"],\"scientificName\":\"Dickeya dadantii (strain 3937)\",\"taxonId\":198628}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:33:04.419071+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bddaf2ccac530c5a545466788630afc91cfbda30f65717bd8f62c9d8fe9978e0",
  "url": "https://rest.uniprot.org/uniprotkb/Q9L392.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9L392.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"11790734\",\"source\":\"PubMed\"}],\"value\":\"3.-.-.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Probable phosphatase IndB\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:33:04.419071+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bddaf2ccac530c5a545466788630afc91cfbda30f65717bd8f62c9d8fe9978e0",
  "url": "https://rest.uniprot.org/uniprotkb/Q9L392.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9L392.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:18420\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q96GD0\",\"source\":\"UniProtKB\"}],\"name\":\"Mg(2+)\"}],\"commentType\":\"COFACTOR\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:33:04.419071+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bddaf2ccac530c5a545466788630afc91cfbda30f65717bd8f62c9d8fe9978e0",
  "url": "https://rest.uniprot.org/uniprotkb/Q9L392.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9L392.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Reverchon S.\",\"Rouanet C.\",\"Expert D.\",\"Nasser W.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"11790734\"},{\"database\":\"DOI\",\"id\":\"10.1128/jb.184.3.654-665.2002\"}],\"citationType\":\"journal article\",\"firstPage\":\"654\",\"id\":\"11790734\",\"journal\":\"J. Bacteriol.\",\"lastPage\":\"665\",\"publicationDate\":\"2002\",\"title\":\"Characterization of indigoidine biosynthetic genes in Erwinia chrysanthemi and role of this blue pigment in pathogenicity.\",\"volume\":\"184\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"CAB87989.1\",\"source\":\"EMBL\"}],\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"3937\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"FUNCTION\",\"INDUCTION\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:33:04.419071+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bddaf2ccac530c5a545466788630afc91cfbda30f65717bd8f62c9d8fe9978e0",
  "url": "https://rest.uniprot.org/uniprotkb/Q9L392.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9L392?format=txt&versions=71)

```json
{
  "entry_version": 71,
  "evidence_id": "H1",
  "excerpt": "ID   INDB_DICD3              Reviewed;         230 AA.\nAC   Q9L392; E0SMH7;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-OCT-2000, sequence version 1.\nDT   28-JAN-2026, entry version 71.\nDE   RecName: Full=Probable phosphatase IndB {ECO:0000305};\nDE            EC=3.-.-.- {ECO:0000305|PubMed:11790734};\nGN   Name=indB {ECO:0000303|PubMed:11790734};\nGN   OrderedLocusNames=Dda3937_00973 {ECO:0000312|EMBL:ADN00616.1};\nOS   Dickeya dadantii (strain 3937) (Erwinia chrysanthemi (strain 3937)).\nOC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria;\nOC   Enterobacterales; Pectobacteriaceae; Dickeya.\nOX   NCBI_TaxID=198628;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:08.324316+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5062c8957159a8ea1cb613ad377d60f1c0ce04c5d973f743ddaad87c0f43abe1",
  "url": "https://rest.uniprot.org/unisave/Q9L392?format=txt&versions=71"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9L392?format=txt&versions=71)

```json
{
  "entry_version": 71,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Probable phosphatase IndB {ECO:0000305};\nDE            EC=3.-.-.- {ECO:0000305|PubMed:11790734};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:08.324316+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-7",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5062c8957159a8ea1cb613ad377d60f1c0ce04c5d973f743ddaad87c0f43abe1",
  "url": "https://rest.uniprot.org/unisave/Q9L392?format=txt&versions=71"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9L392?format=txt&versions=71)

```json
{
  "entry_version": 71,
  "evidence_id": "H3",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:CAB87989.1}\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, INDUCTION, AND DISRUPTION\nRP   PHENOTYPE.\nRC   STRAIN=3937;\nRX   PubMed=11790734; DOI=10.1128/jb.184.3.654-665.2002;\nRA   Reverchon S., Rouanet C., Expert D., Nasser W.;\nRT   \"Characterization of indigoidine biosynthetic genes in Erwinia chrysanthemi\nRT   and role of this blue pigment in pathogenicity.\";\nRL   J. Bacteriol. 184:654-665(2002).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:08.324316+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 14-22",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5062c8957159a8ea1cb613ad377d60f1c0ce04c5d973f743ddaad87c0f43abe1",
  "url": "https://rest.uniprot.org/unisave/Q9L392?format=txt&versions=71"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9L392?format=txt&versions=71)

```json
{
  "entry_version": 71,
  "evidence_id": "H4",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=Mg(2+); Xref=ChEBI:CHEBI:18420;\nCC         Evidence={ECO:0000250|UniProtKB:Q96GD0};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:08.324316+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 41-43",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5062c8957159a8ea1cb613ad377d60f1c0ce04c5d973f743ddaad87c0f43abe1",
  "url": "https://rest.uniprot.org/unisave/Q9L392?format=txt&versions=71"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 175. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
