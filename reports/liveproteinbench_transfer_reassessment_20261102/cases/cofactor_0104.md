# cofactor_0104

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/cofactor_0104.txt)

**Task:** `cofactor`  
**Expected answer:** **A** — &#91;4Fe-4S&#93; cluster

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MQTYLSTKSIEYYLKELKEIFSQIWLKPSEIEKRCEELFKRSKEFDYKRILVSGETDNTTLYVIEDSSKIHVFSPNRDLRENPLLMRWHPSWYEIESKEIYYKCFLSCEELYEHLELPTVTLVNLCVIENFPIPRLNLSTGTLSSYLRKEQLAKVELIDMQVGTTINQIIKNLLDSQPDIIGLSVNFGQKKLAFEILDLIYSHIENGDLSSIITVGNVIPSFSPEQFFERYPSLLICDKEGEYTLRDLIKMLKKELKLDEVNGISYVDESGEVKHNVAETVNFKEEVPTPSLDILGEISKFRGALTLETSRGCDYSRCTFCPRDHKLRSWRPLSVEQTLKQLDDILRAGKHFNIKPHIYMADEEFIGELPNGTEAQRIIDICEGLLKREEKIKFDFAARADSVYEPKRTKEWNVERLKMWHYCALAGADRIFIGVESGSNQQLKRYGKGTTSEQNIIALRLVSALGINLRIGFIMFDQLMKGLDNLKENLDFLERTDALMKPIDIGDMTYEELYDKLLNDKEFIEKHKTGKPVYTIVSYMLASMEILMNTPYSRMVQLTERKEEVNLIMNDGKPDMNMGRYATSFVDKTNGNLSEACQMWIDSNFGVMYTIKSLHKVANPREKKKLYSYMETHREISHFLLKYLVYNLSPDKESQIILSDFLRMHSMEHILDNSKINVGDGSKENILNVMTNWQLIMEKLLRDVEADLNKGIITDSEDHRLHNTLKRWFSDMGNWSLINAYELN

[Multiple Choices]
A. [4Fe-4S] cluster
B. FAD
C. Mn(2+)
D. heme b
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

> The sequence-matched entry reports a &#91;4Fe-4S&#93; cluster, with experimental evidence and coordination by three cysteines; structural evidence also describes the protein in a complex containing this cluster. Thus choice A is supported.

Citations as saved: [C5](#evidence-c5), [C8](#evidence-c8), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a cysteine-rich segment resembling a radical-SAM cluster-binding motif. As transferable family-level knowledge, radical-SAM enzymes commonly use a &#91;4Fe-4S&#93; cluster coordinated by cysteines. That provides a meaningful basis for choosing A over FAD, Mn(2+), or heme b, although the motif alone is not definitive.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A recognizable cysteine-rich sequence feature and the established cofactor pattern of radical-SAM enzymes support a probabilistic distinction among the offered choices without needing the exact protein's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only A among the offered options is supported as a cofactor by the evidence. The protein is also reported to use cob(II)alamin, but that cofactor is not an offered choice.


### Important caveats

- The sequence does not by itself prove the protein's family or cofactor requirement; the motif-based inference is probabilistic.
- The question's singular phrasing omits another reported cofactor, cob(II)alamin.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a cysteine-rich segment resembling a radical-SAM cluster-binding motif. As transferable family-level knowledge, radical-SAM enzymes commonly use a [4Fe-4S] cluster coordinated by cysteines. That provides a meaningful basis for choosing A over FAD, Mn(2+), or heme b, although the motif alone is not definitive.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A recognizable cysteine-rich sequence feature and the established cofactor pattern of radical-SAM enzymes support a probabilistic distinction among the offered choices without needing the exact protein's annotation."
  },
  "case_id": "cofactor_0104",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C8",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched entry reports a [4Fe-4S] cluster, with experimental evidence and coordination by three cysteines; structural evidence also describes the protein in a complex containing this cluster. Thus choice A is supported."
  },
  "important_caveats": [
    "The sequence does not by itself prove the protein's family or cofactor requirement; the motif-based inference is probabilistic.",
    "The question's singular phrasing omits another reported cofactor, cob(II)alamin."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only A among the offered options is supported as a cofactor by the evidence. The protein is also reported to use cob(II)alamin, but that cofactor is not an offered choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0104",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched entry reports a [4Fe-4S] cluster, with experimental evidence and coordination by three cysteines; structural evidence also describes the protein in a complex containing this cluster. Thus choice A is supported.",
    "evidence_ids": ["C5", "C8", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a cysteine-rich segment resembling a radical-SAM cluster-binding motif. As transferable family-level knowledge, radical-SAM enzymes commonly use a [4Fe-4S] cluster coordinated by cysteines. That provides a meaningful basis for choosing A over FAD, Mn(2+), or heme b, although the motif alone is not definitive.",
    "missing_item_specific_fact": "",
    "reason": "A recognizable cysteine-rich sequence feature and the established cofactor pattern of radical-SAM enzymes support a probabilistic distinction among the offered choices without needing the exact protein's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only A among the offered options is supported as a cofactor by the evidence. The protein is also reported to use cob(II)alamin, but that cofactor is not an offered choice."
  },
  "important_caveats": [
    "The sequence does not by itself prove the protein's family or cofactor requirement; the motif-based inference is probabilistic.",
    "The question's singular phrasing omits another reported cofactor, cob(II)alamin."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation (C5/H6) explicitly states: 'Binds 1 &#91;4Fe-4S&#93; cluster. The cluster is coordinated with 3 cysteines and an exchangeable S-adenosyl-L-methionine.' This is backed by experimental evidence (ECO:0000269|PubMed:28346939) from X-ray crystallography (PDB 5UL2/5UL3/5UL4) showing the protein in complex with &#91;4Fe-4S&#93; cluster. The protein is OxsB, a radical SAM enzyme, for which the &#91;4Fe-4S&#93; cluster is the defining cofactor. The expected answer A is well-supported.

Citations as saved: [C5](#evidence-c5), [C8](#evidence-c8), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the region 'CDYSRCTFCP' (around residues 300-310), which closely matches the canonical radical SAM CX3CX2C motif (here approximately CX3CX1CX2C, a known variant in B12-dependent radical SAM enzymes). The radical SAM motif is one of the most widely recognized sequence signatures in biochemistry and is universally associated with &#91;4Fe-4S&#93; cluster coordination. A knowledgeable model recognizing this motif would immediately associate the protein with &#91;4Fe-4S&#93; cluster chemistry. Additionally, the absence of canonical FAD-binding motifs (Rossmann fold GxGxxG), heme-binding motifs (CxxCH or CxxC), and typical Mn(II)-binding patterns (e.g., DxDxH in superoxide dismutases) further eliminates choices B, C, and D. The large size (~744 AA) and C-terminal 'GDGSK...DSEDH' pattern are consistent with a multi-domain radical SAM enzyme with an additional cofactor-binding domain, but the radical SAM motif alone is sufficient to select &#91;4Fe-4S&#93; among the four offered choices.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The radical SAM CX3CX2C (or close variant) motif is a highly conserved, transferable sequence feature learned from hundreds of characterized radical SAM enzymes. Its presence directly and specifically implicates &#91;4Fe-4S&#93; cluster as the cofactor. The other three choices (FAD, Mn2+, heme b) lack any corresponding sequence signature in this protein. This is a well-established pattern in biochemistry, not a lookup of this specific protein's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The protein binds both &#91;4Fe-4S&#93; and cob(II)alamin, but cob(II)alamin is not among the offered choices. Among the four alternatives (A: &#91;4Fe-4S&#93;, B: FAD, C: Mn2+, D: heme b), only &#91;4Fe-4S&#93; is a confirmed cofactor. No other option is defensible.


### Important caveats

- The protein also binds cob(II)alamin (B12) as a second cofactor (C6/H7), but this is not among the answer choices, so it does not create ambiguity among the offered alternatives.
- The radical SAM motif in this sequence (CDYSRCTFC) deviates slightly from the canonical CX3CX2C pattern (the second spacing is CX1C rather than CX2C), which is a known variation in B12-dependent radical SAM enzymes but could make motif recognition marginally less straightforward.
- The UniProt entry was first publicly released in February 2025; the author's source snapshot date is unknown, so the annotation available to the author may differ from the current record.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the region 'CDYSRCTFCP' (around residues 300-310), which closely matches the canonical radical SAM CX3CX2C motif (here approximately CX3CX1CX2C, a known variant in B12-dependent radical SAM enzymes). The radical SAM motif is one of the most widely recognized sequence signatures in biochemistry and is universally associated with [4Fe-4S] cluster coordination. A knowledgeable model recognizing this motif would immediately associate the protein with [4Fe-4S] cluster chemistry. Additionally, the absence of canonical FAD-binding motifs (Rossmann fold GxGxxG), heme-binding motifs (CxxCH or CxxC), and typical Mn(II)-binding patterns (e.g., DxDxH in superoxide dismutases) further eliminates choices B, C, and D. The large size (~744 AA) and C-terminal 'GDGSK...DSEDH' pattern are consistent with a multi-domain radical SAM enzyme with an additional cofactor-binding domain, but the radical SAM motif alone is sufficient to select [4Fe-4S] among the four offered choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The radical SAM CX3CX2C (or close variant) motif is a highly conserved, transferable sequence feature learned from hundreds of characterized radical SAM enzymes. Its presence directly and specifically implicates [4Fe-4S] cluster as the cofactor. The other three choices (FAD, Mn2+, heme b) lack any corresponding sequence signature in this protein. This is a well-established pattern in biochemistry, not a lookup of this specific protein's annotation."
  },
  "case_id": "cofactor_0104",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C8",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation (C5/H6) explicitly states: 'Binds 1 [4Fe-4S] cluster. The cluster is coordinated with 3 cysteines and an exchangeable S-adenosyl-L-methionine.' This is backed by experimental evidence (ECO:0000269|PubMed:28346939) from X-ray crystallography (PDB 5UL2/5UL3/5UL4) showing the protein in complex with [4Fe-4S] cluster. The protein is OxsB, a radical SAM enzyme, for which the [4Fe-4S] cluster is the defining cofactor. The expected answer A is well-supported."
  },
  "important_caveats": [
    "The protein also binds cob(II)alamin (B12) as a second cofactor (C6/H7), but this is not among the answer choices, so it does not create ambiguity among the offered alternatives.",
    "The radical SAM motif in this sequence (CDYSRCTFC) deviates slightly from the canonical CX3CX2C pattern (the second spacing is CX1C rather than CX2C), which is a known variation in B12-dependent radical SAM enzymes but could make motif recognition marginally less straightforward.",
    "The UniProt entry was first publicly released in February 2025; the author's source snapshot date is unknown, so the annotation available to the author may differ from the current record."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein binds both [4Fe-4S] and cob(II)alamin, but cob(II)alamin is not among the offered choices. Among the four alternatives (A: [4Fe-4S], B: FAD, C: Mn2+, D: heme b), only [4Fe-4S] is a confirmed cofactor. No other option is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0104",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation (C5/H6) explicitly states: 'Binds 1 [4Fe-4S] cluster. The cluster is coordinated with 3 cysteines and an exchangeable S-adenosyl-L-methionine.' This is backed by experimental evidence (ECO:0000269|PubMed:28346939) from X-ray crystallography (PDB 5UL2/5UL3/5UL4) showing the protein in complex with [4Fe-4S] cluster. The protein is OxsB, a radical SAM enzyme, for which the [4Fe-4S] cluster is the defining cofactor. The expected answer A is well-supported.",
    "evidence_ids": ["C5", "C8", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the region 'CDYSRCTFCP' (around residues 300-310), which closely matches the canonical radical SAM CX3CX2C motif (here approximately CX3CX1CX2C, a known variant in B12-dependent radical SAM enzymes). The radical SAM motif is one of the most widely recognized sequence signatures in biochemistry and is universally associated with [4Fe-4S] cluster coordination. A knowledgeable model recognizing this motif would immediately associate the protein with [4Fe-4S] cluster chemistry. Additionally, the absence of canonical FAD-binding motifs (Rossmann fold GxGxxG), heme-binding motifs (CxxCH or CxxC), and typical Mn(II)-binding patterns (e.g., DxDxH in superoxide dismutases) further eliminates choices B, C, and D. The large size (~744 AA) and C-terminal 'GDGSK...DSEDH' pattern are consistent with a multi-domain radical SAM enzyme with an additional cofactor-binding domain, but the radical SAM motif alone is sufficient to select [4Fe-4S] among the four offered choices.",
    "missing_item_specific_fact": "",
    "reason": "The radical SAM CX3CX2C (or close variant) motif is a highly conserved, transferable sequence feature learned from hundreds of characterized radical SAM enzymes. Its presence directly and specifically implicates [4Fe-4S] cluster as the cofactor. The other three choices (FAD, Mn2+, heme b) lack any corresponding sequence signature in this protein. This is a well-established pattern in biochemistry, not a lookup of this specific protein's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein binds both [4Fe-4S] and cob(II)alamin, but cob(II)alamin is not among the offered choices. Among the four alternatives (A: [4Fe-4S], B: FAD, C: Mn2+, D: heme b), only [4Fe-4S] is a confirmed cofactor. No other option is defensible."
  },
  "important_caveats": [
    "The protein also binds cob(II)alamin (B12) as a second cofactor (C6/H7), but this is not among the answer choices, so it does not create ambiguity among the offered alternatives.",
    "The radical SAM motif in this sequence (CDYSRCTFC) deviates slightly from the canonical CX3CX2C pattern (the second spacing is CX1C rather than CX2C), which is a known variation in B12-dependent radical SAM enzymes but could make motif recognition marginally less straightforward.",
    "The UniProt entry was first publicly released in February 2025; the author's source snapshot date is unknown, so the annotation available to the author may differ from the current record."
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
  "benchmark_sequence_length": 744,
  "benchmark_sequence_sha256": "0af3073a7c236a71413178dc89485593fd423e6ef4fe0e3dbe801a5e5e561220",
  "current_entry_audit": {
    "entryVersion": 92,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "1998-01-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "0a5df96f640199749015b4999d23075d213421b74b01cf0009b796669ee43c47",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 744,
  "current_source_sequence_sha256": "0af3073a7c236a71413178dc89485593fd423e6ef4fe0e3dbe801a5e5e561220",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 90,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "O24770",
  "selected_historical_entry_version": 90,
  "selected_historical_record_sha256": "74d13584dd5e362c68994158dea31c83d3658cc87b7425d894b542313b4c08cc",
  "selected_historical_source_sequence_length": 744,
  "selected_historical_source_sequence_sha256": "0af3073a7c236a71413178dc89485593fd423e6ef4fe0e3dbe801a5e5e561220",
  "selected_historical_version": {
    "accession": "O24770",
    "database": "Swiss-Prot",
    "entryVersion": 90,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "OXSB_PRIMG",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O24770.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"O24770\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:29:11.085784+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0a5df96f640199749015b4999d23075d213421b74b01cf0009b796669ee43c47",
  "url": "https://rest.uniprot.org/uniprotkb/O24770.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O24770.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":92,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"1998-01-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:29:11.085784+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0a5df96f640199749015b4999d23075d213421b74b01cf0009b796669ee43c47",
  "url": "https://rest.uniprot.org/uniprotkb/O24770.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O24770.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Bacillus megaterium\",\"lineage\":[\"Bacteria\",\"Bacillati\",\"Bacillota\",\"Bacilli\",\"Caryophanales\",\"Bacillaceae\",\"Priestia\"],\"scientificName\":\"Priestia megaterium\",\"taxonId\":1404}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:29:11.085784+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0a5df96f640199749015b4999d23075d213421b74b01cf0009b796669ee43c47",
  "url": "https://rest.uniprot.org/uniprotkb/O24770.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O24770.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"28346939\",\"source\":\"PubMed\"}],\"value\":\"Cobalamin-dependent S-adenosylmethionine radical enzyme OxsB\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"dAMP isomerase (4'-phospho-dehydrooxetanocin-forming)\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"28346939\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"33560833\",\"source\":\"PubMed\"}],\"value\":\"5.3.99.13\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"4'-phospho-dehydrooxetanocin synthase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:29:11.085784+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0a5df96f640199749015b4999d23075d213421b74b01cf0009b796669ee43c47",
  "url": "https://rest.uniprot.org/uniprotkb/O24770.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O24770.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:49883\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"28346939\",\"source\":\"PubMed\"}],\"name\":\"[4Fe-4S] cluster\"}],\"commentType\":\"COFACTOR\",\"note\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"28346939\",\"source\":\"PubMed\"}],\"value\":\"Binds 1 [4Fe-4S] cluster. The cluster is coordinated with 3 cysteines and an exchangeable S-adenosyl-L-methionine.\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/4",
  "retrieved_utc": "2026-11-02T04:29:11.085784+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0a5df96f640199749015b4999d23075d213421b74b01cf0009b796669ee43c47",
  "url": "https://rest.uniprot.org/uniprotkb/O24770.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O24770.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:16304\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"28346939\",\"source\":\"PubMed\"}],\"name\":\"cob(II)alamin\"}],\"commentType\":\"COFACTOR\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/5",
  "retrieved_utc": "2026-11-02T04:29:11.085784+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0a5df96f640199749015b4999d23075d213421b74b01cf0009b796669ee43c47",
  "url": "https://rest.uniprot.org/uniprotkb/O24770.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O24770.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Zhong A.\",\"Lee Y.H.\",\"Liu Y.N.\",\"Liu H.W.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"33560833\"},{\"database\":\"DOI\",\"id\":\"10.1021/acs.biochem.0c00915\"}],\"citationType\":\"journal article\",\"firstPage\":\"537\",\"id\":\"33560833\",\"journal\":\"Biochemistry\",\"lastPage\":\"546\",\"publicationDate\":\"2021\",\"title\":\"Biosynthesis of Oxetanocin-A Includes a B12-Dependent Radical SAM Enzyme That Can Catalyze both Oxidative Ring Contraction and the Demethylation of SAM.\",\"volume\":\"60\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"ACTIVITY REGULATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:29:11.085784+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0a5df96f640199749015b4999d23075d213421b74b01cf0009b796669ee43c47",
  "url": "https://rest.uniprot.org/uniprotkb/O24770.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O24770.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Bridwell-Rabb J.\",\"Zhong A.\",\"Sun H.G.\",\"Drennan C.L.\",\"Liu H.W.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"28346939\"},{\"database\":\"DOI\",\"id\":\"10.1038/nature21689\"}],\"citationType\":\"journal article\",\"firstPage\":\"322\",\"id\":\"28346939\",\"journal\":\"Nature\",\"lastPage\":\"326\",\"publicationDate\":\"2017\",\"title\":\"A B12-dependent radical SAM enzyme involved in oxetanocin A biosynthesis.\",\"volume\":\"544\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"5UL2\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"5UL3\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"5UL4\",\"source\":\"PDB\"}],\"referenceNumber\":4,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (1.80 ANGSTROMS) IN COMPLEXES WITH [4FE-4S] CLUSTER; COB(II)ALAMIN AND S-ADENOSYL-L-METHIONINE\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"COFACTOR\",\"ACTIVITY REGULATION\",\"DOMAIN\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-02T04:29:11.085784+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0a5df96f640199749015b4999d23075d213421b74b01cf0009b796669ee43c47",
  "url": "https://rest.uniprot.org/uniprotkb/O24770.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O24770?format=txt&versions=90)

```json
{
  "entry_version": 90,
  "evidence_id": "H1",
  "excerpt": "ID   OXSB_PRIMG              Reviewed;         744 AA.\nAC   O24770;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-JAN-1998, sequence version 1.\nDT   28-JAN-2026, entry version 90.\nDE   RecName: Full=4'-phospho-dehydrooxetanocin synthase {ECO:0000305};\nDE            EC=5.3.99.13 {ECO:0000269|PubMed:28346939, ECO:0000269|PubMed:33560833};\nDE   AltName: Full=Cobalamin-dependent S-adenosylmethionine radical enzyme OxsB {ECO:0000303|PubMed:28346939};\nDE   AltName: Full=dAMP isomerase (4'-phospho-dehydrooxetanocin-forming) {ECO:0000305};\nGN   Name=oxsB {ECO:0000312|EMBL:BAA21631.1};\nOS   Priestia megaterium (Bacillus megaterium).\nOG   Plasmid pOXT1 {ECO:0000303|PubMed:10227144}.\nOC   Bacteria; Bacillati; Bacillota; Bacilli; Bacillales; Bacillaceae; Priestia.\nOX   NCBI_TaxID=1404;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:15.786314+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "74d13584dd5e362c68994158dea31c83d3658cc87b7425d894b542313b4c08cc",
  "url": "https://rest.uniprot.org/unisave/O24770?format=txt&versions=90"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O24770?format=txt&versions=90)

```json
{
  "entry_version": 90,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=4'-phospho-dehydrooxetanocin synthase {ECO:0000305};\nDE            EC=5.3.99.13 {ECO:0000269|PubMed:28346939, ECO:0000269|PubMed:33560833};\nDE   AltName: Full=Cobalamin-dependent S-adenosylmethionine radical enzyme OxsB {ECO:0000303|PubMed:28346939};\nDE   AltName: Full=dAMP isomerase (4'-phospho-dehydrooxetanocin-forming) {ECO:0000305};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:15.786314+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-9",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "74d13584dd5e362c68994158dea31c83d3658cc87b7425d894b542313b4c08cc",
  "url": "https://rest.uniprot.org/unisave/O24770?format=txt&versions=90"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O24770?format=txt&versions=90)

```json
{
  "entry_version": 90,
  "evidence_id": "H3",
  "excerpt": "RN   [1]\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA].\nRC   STRAIN=NK84-0128; PLASMID=pOXT1;\nRX   PubMed=10227144; DOI=10.1271/bbb.63.563;\nRA   Morita M., Tomita K., Ishizawa M., Takagi K., Kawamura F., Takahashi H.,\nRA   Morino T.;\nRT   \"Cloning of oxetanocin A biosynthetic and resistance genes that reside on a\nRT   plasmid of Bacillus megaterium strain NK84-0128.\";\nRL   Biosci. Biotechnol. Biochem. 63:563-566(1999).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:15.786314+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 15-23",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "74d13584dd5e362c68994158dea31c83d3658cc87b7425d894b542313b4c08cc",
  "url": "https://rest.uniprot.org/unisave/O24770?format=txt&versions=90"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O24770?format=txt&versions=90)

```json
{
  "entry_version": 90,
  "evidence_id": "H4",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, AND ACTIVITY REGULATION.\nRX   PubMed=33560833; DOI=10.1021/acs.biochem.0c00915;\nRA   Zhong A., Lee Y.H., Liu Y.N., Liu H.W.;\nRT   \"Biosynthesis of Oxetanocin-A Includes a B12-Dependent Radical SAM Enzyme\nRT   That Can Catalyze both Oxidative Ring Contraction and the Demethylation of\nRT   SAM.\";\nRL   Biochemistry 60:537-546(2021).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:15.786314+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 24-31",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "74d13584dd5e362c68994158dea31c83d3658cc87b7425d894b542313b4c08cc",
  "url": "https://rest.uniprot.org/unisave/O24770?format=txt&versions=90"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O24770?format=txt&versions=90)

```json
{
  "entry_version": 90,
  "evidence_id": "H5",
  "excerpt": "RN   [4] {ECO:0007744|PDB:5UL2, ECO:0007744|PDB:5UL3, ECO:0007744|PDB:5UL4}\nRP   X-RAY CRYSTALLOGRAPHY (1.80 ANGSTROMS) IN COMPLEXES WITH [4FE-4S] CLUSTER;\nRP   COB(II)ALAMIN AND S-ADENOSYL-L-METHIONINE, FUNCTION, CATALYTIC ACTIVITY,\nRP   COFACTOR, ACTIVITY REGULATION, AND DOMAIN.\nRX   PubMed=28346939; DOI=10.1038/nature21689;\nRA   Bridwell-Rabb J., Zhong A., Sun H.G., Drennan C.L., Liu H.W.;\nRT   \"A B12-dependent radical SAM enzyme involved in oxetanocin A\nRT   biosynthesis.\";\nRL   Nature 544:322-326(2017).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:15.786314+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 39-47",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "74d13584dd5e362c68994158dea31c83d3658cc87b7425d894b542313b4c08cc",
  "url": "https://rest.uniprot.org/unisave/O24770?format=txt&versions=90"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O24770?format=txt&versions=90)

```json
{
  "entry_version": 90,
  "evidence_id": "H6",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=[4Fe-4S] cluster; Xref=ChEBI:CHEBI:49883;\nCC         Evidence={ECO:0000269|PubMed:28346939};\nCC       Note=Binds 1 [4Fe-4S] cluster. The cluster is coordinated with 3\nCC       cysteines and an exchangeable S-adenosyl-L-methionine.\nCC       {ECO:0000269|PubMed:28346939};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:15.786314+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 84-89",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "74d13584dd5e362c68994158dea31c83d3658cc87b7425d894b542313b4c08cc",
  "url": "https://rest.uniprot.org/unisave/O24770?format=txt&versions=90"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O24770?format=txt&versions=90)

```json
{
  "entry_version": 90,
  "evidence_id": "H7",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=cob(II)alamin; Xref=ChEBI:CHEBI:16304;\nCC         Evidence={ECO:0000269|PubMed:28346939};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:15.786314+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 90-92",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "74d13584dd5e362c68994158dea31c83d3658cc87b7425d894b542313b4c08cc",
  "url": "https://rest.uniprot.org/unisave/O24770?format=txt&versions=90"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 104. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
