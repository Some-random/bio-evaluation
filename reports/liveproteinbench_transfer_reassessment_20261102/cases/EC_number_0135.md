# EC_number_0135

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0135.txt)

**Task:** `EC_number`  
**Expected answer:** **C** — 2.3.1.31

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MSDNTPTPQKNPDTNPYASLISQQIAIIPSFTLESGVTLNNVPVAYKTWGKLNEKADNCLVICHALTGSADVEDWWGPLLGLNKAFDPTRFFIFCGNVIGSPYGTISSVTTNPETGKPFGPEMPGSSVKDDVRLHYIILKSLGVRSVAAVVGGSMGGMTVLEYPLNTPPGFVRAIIPLATSARHSAWCISWGEAQRQSIYSDPDYKDGYYYEIEEEGGKVDLARQPARGLAAARMAALLTYRSRDSFESRFGRRAGGGKSSVPKGGVRIMGGQETTDPSVPSESDLAAKSPSWRAWREHNDGHRSAGARPISRSGSEGPAHREGDAAQAEVVKTQDVKANGNKIGTGGEAPPKIFSAQSYLRYQGDKFTGRFDANCYIHITRKLDTHDLSAPSRDTSLSSLSSGLPSSPDATEEELNARLIHALSLEPPALVIGIESDGLFTTSEQRELAAGIPDAELVVIPSPDGHDGFLLEFEAINGWVEGWLKRKMPEFYERRVINPEEYVQGEEGFGIKKESVFGEAEADVTRW

[Multiple Choices]
A. 2.3.1.322
B. 4.1.1.129
C. 2.3.1.31
D. 3.1.1.4
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

> The supplied reviewer evidence identifies an exact sequence match and annotates it as EC 2.3.1.31. The catalytic-activity annotation specifies homoserine plus acetyl-CoA forming O-acetylhomoserine and CoA, with ECO:0000269 evidence citing a publication. This supports choice C, although the cited experiment was not independently reviewed here.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with the conserved Met2/homoserine O-acetyltransferase family. Family recognition from homologous proteins provides a meaningful basis for EC 2.3.1.31 over the decarboxylase and hydrolase choices; it also distinguishes C from the other acyltransferase choice, A, since the family-level inference is more specific than merely recognizing an acetyltransferase.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level sequence inference can distinguish the offered choices without access to this protein’s recorded database answer. The inference is probabilistic, and the sequence alone does not provide an experimental reaction measurement.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The alternatives represent different EC activities, and the sequence-family inference meaningfully favors C over the listed alternatives.


### Important caveats

- The reviewer-only annotation and evidence were not available as original inputs and are used only to assess whether the expected answer is supported.
- The transferability judgment rests on recognizing a family pattern from the sequence, not on knowing the exact target's database record.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with the conserved Met2/homoserine O-acetyltransferase family. Family recognition from homologous proteins provides a meaningful basis for EC 2.3.1.31 over the decarboxylase and hydrolase choices; it also distinguishes C from the other acyltransferase choice, A, since the family-level inference is more specific than merely recognizing an acetyltransferase.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level sequence inference can distinguish the offered choices without access to this protein’s recorded database answer. The inference is probabilistic, and the sequence alone does not provide an experimental reaction measurement."
  },
  "case_id": "EC_number_0135",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The supplied reviewer evidence identifies an exact sequence match and annotates it as EC 2.3.1.31. The catalytic-activity annotation specifies homoserine plus acetyl-CoA forming O-acetylhomoserine and CoA, with ECO:0000269 evidence citing a publication. This supports choice C, although the cited experiment was not independently reviewed here."
  },
  "important_caveats": [
    "The reviewer-only annotation and evidence were not available as original inputs and are used only to assess whether the expected answer is supported.",
    "The transferability judgment rests on recognizing a family pattern from the sequence, not on knowing the exact target's database record."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives represent different EC activities, and the sequence-family inference meaningfully favors C over the listed alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0135",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied reviewer evidence identifies an exact sequence match and annotates it as EC 2.3.1.31. The catalytic-activity annotation specifies homoserine plus acetyl-CoA forming O-acetylhomoserine and CoA, with ECO:0000269 evidence citing a publication. This supports choice C, although the cited experiment was not independently reviewed here.",
    "evidence_ids": ["C4", "C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with the conserved Met2/homoserine O-acetyltransferase family. Family recognition from homologous proteins provides a meaningful basis for EC 2.3.1.31 over the decarboxylase and hydrolase choices; it also distinguishes C from the other acyltransferase choice, A, since the family-level inference is more specific than merely recognizing an acetyltransferase.",
    "missing_item_specific_fact": "",
    "reason": "A family-level sequence inference can distinguish the offered choices without access to this protein’s recorded database answer. The inference is probabilistic, and the sequence alone does not provide an experimental reaction measurement."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives represent different EC activities, and the sequence-family inference meaningfully favors C over the listed alternatives."
  },
  "important_caveats": [
    "The reviewer-only annotation and evidence were not available as original inputs and are used only to assess whether the expected answer is supported.",
    "The transferability judgment rests on recognizing a family pattern from the sequence, not on knowing the exact target's database record."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry J9VIY8 (MET2_CRYN9) is annotated as Homoserine O-acetyltransferase, EC 2.3.1.31, with experimental evidence (ECO:0000269, PubMed:17353245). The catalytic reaction L-homoserine + acetyl-CoA = O-acetyl-L-homoserine + CoA is confirmed by experimental study (Nazi et al., 2007). The sequence matches the benchmark sequence exactly.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a clear GNAT (GCN5-related N-acetyltransferase) fold signature: the Rossmann-like acetyl-CoA binding motif 'GGSMGGMTV' (GxGxxG pattern) is diagnostic of EC 2.3.x.x acyltransferases, immediately eliminating B (EC 4.1.1.129, a carboxy-lyase requiring a completely different fold) and D (EC 3.1.1.4, phospholipase A2, a hydrolase with a distinct calcium-dependent fold). Between the remaining two acyltransferases A (2.3.1.322) and C (2.3.1.31), the domain architecture—N-terminal extension, central GNAT domain, and a C-terminal extension with a separate structural module (~528 aa, fungal-type composition)—matches the well-characterized MET2/homoserine O-acetyltransferase family found across fungi. This three-domain architecture is a family-level signature of MET2 enzymes involved in the methionine biosynthesis pathway, distinguishing them from other GNAT-family acetyltransferases that typically have a simpler single-domain or two-domain architecture. A model familiar with the MET2 family across fungal species would recognize this architecture and assign EC 2.3.1.31.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The GNAT fold motif eliminates B and D unambiguously. The multi-domain architecture (N-terminal extension + GNAT + C-terminal module) and overall sequence length are consistent with the MET2/homoserine O-acetyltransferase family, a well-characterized enzyme class in fungal amino acid biosynthesis. This is family-level transferable knowledge, not lookup of this specific protein's database record. The distinction between A and C is probabilistic but grounded in recognizable domain architecture shared across MET2 homologs.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> B (lyase) and D (hydrolase) are clearly eliminated by the GNAT fold. Between A and C, the MET2 domain architecture supports C. While A (2.3.1.322) is a plausible distractor for someone recognizing the acyltransferase class but not the specific family, the domain architecture argument meaningfully favors C. No two options are equally defensible given the sequence evidence.


### Important caveats

- The GNAT fold is shared by hundreds of acetyltransferases with diverse substrates; distinguishing EC 2.3.1.31 from EC 2.3.1.322 relies on family-level domain architecture recognition rather than a single unambiguous sequence motif.
- EC 2.3.1.322 is a relatively obscure EC number; its exact identity and whether it also belongs to the GNAT superfamily were not independently verified from the provided evidence.
- The reviewer-only evidence confirms the annotation with experimental evidence (ECO:0000269), but this evidence was not available to the evaluated model.
- The sequence was identified as J9VIY8 (MET2_CRYN9) only through reviewer-only metadata; the evaluated model had no accession or organism information.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a clear GNAT (GCN5-related N-acetyltransferase) fold signature: the Rossmann-like acetyl-CoA binding motif 'GGSMGGMTV' (GxGxxG pattern) is diagnostic of EC 2.3.x.x acyltransferases, immediately eliminating B (EC 4.1.1.129, a carboxy-lyase requiring a completely different fold) and D (EC 3.1.1.4, phospholipase A2, a hydrolase with a distinct calcium-dependent fold). Between the remaining two acyltransferases A (2.3.1.322) and C (2.3.1.31), the domain architecture—N-terminal extension, central GNAT domain, and a C-terminal extension with a separate structural module (~528 aa, fungal-type composition)—matches the well-characterized MET2/homoserine O-acetyltransferase family found across fungi. This three-domain architecture is a family-level signature of MET2 enzymes involved in the methionine biosynthesis pathway, distinguishing them from other GNAT-family acetyltransferases that typically have a simpler single-domain or two-domain architecture. A model familiar with the MET2 family across fungal species would recognize this architecture and assign EC 2.3.1.31.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The GNAT fold motif eliminates B and D unambiguously. The multi-domain architecture (N-terminal extension + GNAT + C-terminal module) and overall sequence length are consistent with the MET2/homoserine O-acetyltransferase family, a well-characterized enzyme class in fungal amino acid biosynthesis. This is family-level transferable knowledge, not lookup of this specific protein's database record. The distinction between A and C is probabilistic but grounded in recognizable domain architecture shared across MET2 homologs."
  },
  "case_id": "EC_number_0135",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry J9VIY8 (MET2_CRYN9) is annotated as Homoserine O-acetyltransferase, EC 2.3.1.31, with experimental evidence (ECO:0000269, PubMed:17353245). The catalytic reaction L-homoserine + acetyl-CoA = O-acetyl-L-homoserine + CoA is confirmed by experimental study (Nazi et al., 2007). The sequence matches the benchmark sequence exactly."
  },
  "important_caveats": [
    "The GNAT fold is shared by hundreds of acetyltransferases with diverse substrates; distinguishing EC 2.3.1.31 from EC 2.3.1.322 relies on family-level domain architecture recognition rather than a single unambiguous sequence motif.",
    "EC 2.3.1.322 is a relatively obscure EC number; its exact identity and whether it also belongs to the GNAT superfamily were not independently verified from the provided evidence.",
    "The reviewer-only evidence confirms the annotation with experimental evidence (ECO:0000269), but this evidence was not available to the evaluated model.",
    "The sequence was identified as J9VIY8 (MET2_CRYN9) only through reviewer-only metadata; the evaluated model had no accession or organism information."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "B (lyase) and D (hydrolase) are clearly eliminated by the GNAT fold. Between A and C, the MET2 domain architecture supports C. While A (2.3.1.322) is a plausible distractor for someone recognizing the acyltransferase class but not the specific family, the domain architecture argument meaningfully favors C. No two options are equally defensible given the sequence evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0135",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry J9VIY8 (MET2_CRYN9) is annotated as Homoserine O-acetyltransferase, EC 2.3.1.31, with experimental evidence (ECO:0000269, PubMed:17353245). The catalytic reaction L-homoserine + acetyl-CoA = O-acetyl-L-homoserine + CoA is confirmed by experimental study (Nazi et al., 2007). The sequence matches the benchmark sequence exactly.",
    "evidence_ids": ["C4", "C5", "C6", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a clear GNAT (GCN5-related N-acetyltransferase) fold signature: the Rossmann-like acetyl-CoA binding motif 'GGSMGGMTV' (GxGxxG pattern) is diagnostic of EC 2.3.x.x acyltransferases, immediately eliminating B (EC 4.1.1.129, a carboxy-lyase requiring a completely different fold) and D (EC 3.1.1.4, phospholipase A2, a hydrolase with a distinct calcium-dependent fold). Between the remaining two acyltransferases A (2.3.1.322) and C (2.3.1.31), the domain architecture—N-terminal extension, central GNAT domain, and a C-terminal extension with a separate structural module (~528 aa, fungal-type composition)—matches the well-characterized MET2/homoserine O-acetyltransferase family found across fungi. This three-domain architecture is a family-level signature of MET2 enzymes involved in the methionine biosynthesis pathway, distinguishing them from other GNAT-family acetyltransferases that typically have a simpler single-domain or two-domain architecture. A model familiar with the MET2 family across fungal species would recognize this architecture and assign EC 2.3.1.31.",
    "missing_item_specific_fact": "",
    "reason": "The GNAT fold motif eliminates B and D unambiguously. The multi-domain architecture (N-terminal extension + GNAT + C-terminal module) and overall sequence length are consistent with the MET2/homoserine O-acetyltransferase family, a well-characterized enzyme class in fungal amino acid biosynthesis. This is family-level transferable knowledge, not lookup of this specific protein's database record. The distinction between A and C is probabilistic but grounded in recognizable domain architecture shared across MET2 homologs."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "B (lyase) and D (hydrolase) are clearly eliminated by the GNAT fold. Between A and C, the MET2 domain architecture supports C. While A (2.3.1.322) is a plausible distractor for someone recognizing the acyltransferase class but not the specific family, the domain architecture argument meaningfully favors C. No two options are equally defensible given the sequence evidence."
  },
  "important_caveats": [
    "The GNAT fold is shared by hundreds of acetyltransferases with diverse substrates; distinguishing EC 2.3.1.31 from EC 2.3.1.322 relies on family-level domain architecture recognition rather than a single unambiguous sequence motif.",
    "EC 2.3.1.322 is a relatively obscure EC number; its exact identity and whether it also belongs to the GNAT superfamily were not independently verified from the provided evidence.",
    "The reviewer-only evidence confirms the annotation with experimental evidence (ECO:0000269), but this evidence was not available to the evaluated model.",
    "The sequence was identified as J9VIY8 (MET2_CRYN9) only through reviewer-only metadata; the evaluated model had no accession or organism information."
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
  "benchmark_sequence_length": 528,
  "benchmark_sequence_sha256": "57825f4d67b7b8a868fb283bc084d32ce6202d902a078ce010f45f7dba5b26c0",
  "current_entry_audit": {
    "entryVersion": 56,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2012-11-28",
    "sequenceVersion": 1
  },
  "current_record_sha256": "1dd26bd473689f347eca69268d64365a8d99894cc29c382df0bdcbe9218d5cda",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 528,
  "current_source_sequence_sha256": "57825f4d67b7b8a868fb283bc084d32ce6202d902a078ce010f45f7dba5b26c0",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 54,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "J9VIY8",
  "selected_historical_entry_version": 54,
  "selected_historical_record_sha256": "f199a40bd4613a52dfaa0c84625c1bb8a81d2d65e01501415825a1c3b01fb844",
  "selected_historical_source_sequence_length": 528,
  "selected_historical_source_sequence_sha256": "57825f4d67b7b8a868fb283bc084d32ce6202d902a078ce010f45f7dba5b26c0",
  "selected_historical_version": {
    "accession": "J9VIY8",
    "database": "Swiss-Prot",
    "entryVersion": 54,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "MET2_CRYN9",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VIY8.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"J9VIY8\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:28:54.980036+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1dd26bd473689f347eca69268d64365a8d99894cc29c382df0bdcbe9218d5cda",
  "url": "https://rest.uniprot.org/uniprotkb/J9VIY8.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VIY8.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":56,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2012-11-28\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:28:54.980036+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1dd26bd473689f347eca69268d64365a8d99894cc29c382df0bdcbe9218d5cda",
  "url": "https://rest.uniprot.org/uniprotkb/J9VIY8.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VIY8.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Cryptococcus neoformans var. grubii serotype A\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000010091\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Basidiomycota\",\"Agaricomycotina\",\"Tremellomycetes\",\"Tremellales\",\"Cryptococcaceae\",\"Cryptococcus\",\"Cryptococcus neoformans species complex\"],\"scientificName\":\"Cryptococcus neoformans (strain H99 / ATCC 208821 / CBS 10515 / FGSC 9487)\",\"taxonId\":235443}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:28:54.980036+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1dd26bd473689f347eca69268d64365a8d99894cc29c382df0bdcbe9218d5cda",
  "url": "https://rest.uniprot.org/uniprotkb/J9VIY8.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VIY8.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"17353245\",\"source\":\"PubMed\"}],\"value\":\"2.3.1.31\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Homoserine O-acetyltransferase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:28:54.980036+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1dd26bd473689f347eca69268d64365a8d99894cc29c382df0bdcbe9218d5cda",
  "url": "https://rest.uniprot.org/uniprotkb/J9VIY8.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VIY8.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"17353245\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:13702\"}}],\"reaction\":{\"ecNumber\":\"2.3.1.31\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"17353245\",\"source\":\"PubMed\"}],\"name\":\"L-homoserine + acetyl-CoA = O-acetyl-L-homoserine + CoA\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:13701\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57287\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57288\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57476\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57716\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:28:54.980036+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1dd26bd473689f347eca69268d64365a8d99894cc29c382df0bdcbe9218d5cda",
  "url": "https://rest.uniprot.org/uniprotkb/J9VIY8.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VIY8.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Nazi I.\",\"Scott A.\",\"Sham A.\",\"Rossi L.\",\"Williamson P.R.\",\"Kronstad J.W.\",\"Wright G.D.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"17353245\"},{\"database\":\"DOI\",\"id\":\"10.1128/aac.01400-06\"}],\"citationType\":\"journal article\",\"firstPage\":\"1731\",\"id\":\"17353245\",\"journal\":\"Antimicrob. Agents Chemother.\",\"lastPage\":\"1736\",\"publicationDate\":\"2007\",\"title\":\"Role of homoserine transacetylase as a new target for antifungal agents.\",\"volume\":\"51\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"ACTIVITY REGULATION\",\"PATHWAY\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:28:54.980036+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1dd26bd473689f347eca69268d64365a8d99894cc29c382df0bdcbe9218d5cda",
  "url": "https://rest.uniprot.org/uniprotkb/J9VIY8.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VIY8?format=txt&versions=54)

```json
{
  "entry_version": 54,
  "evidence_id": "H1",
  "excerpt": "ID   MET2_CRYN9              Reviewed;         528 AA.\nAC   J9VIY8;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   28-NOV-2012, sequence version 1.\nDT   28-JAN-2026, entry version 54.\nDE   RecName: Full=Homoserine O-acetyltransferase {ECO:0000305};\nDE            EC=2.3.1.31 {ECO:0000269|PubMed:17353245};\nGN   Name=MET2 {ECO:0000303|PubMed:17353245};\nGN   ORFNames=CNAG_05122 {ECO:0000312|EMBL:AFR94387.1};\nOS   Cryptococcus neoformans (strain H99 / ATCC 208821 / CBS 10515 / FGSC 9487)\nOS   (Cryptococcus neoformans var. grubii serotype A).\nOC   Eukaryota; Fungi; Dikarya; Basidiomycota; Agaricomycotina; Tremellomycetes;\nOC   Tremellales; Cryptococcaceae; Cryptococcus;\nOC   Cryptococcus neoformans species complex.\nOX   NCBI_TaxID=235443 {ECO:0000312|Proteomes:UP000010091};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:57.924962+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f199a40bd4613a52dfaa0c84625c1bb8a81d2d65e01501415825a1c3b01fb844",
  "url": "https://rest.uniprot.org/unisave/J9VIY8?format=txt&versions=54"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VIY8?format=txt&versions=54)

```json
{
  "entry_version": 54,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Homoserine O-acetyltransferase {ECO:0000305};\nDE            EC=2.3.1.31 {ECO:0000269|PubMed:17353245};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:57.924962+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-7",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f199a40bd4613a52dfaa0c84625c1bb8a81d2d65e01501415825a1c3b01fb844",
  "url": "https://rest.uniprot.org/unisave/J9VIY8?format=txt&versions=54"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VIY8?format=txt&versions=54)

```json
{
  "entry_version": 54,
  "evidence_id": "H3",
  "excerpt": "RN   [2] {ECO:0000305}\nRP   FUNCTION, CATALYTIC ACTIVITY, ACTIVITY REGULATION, PATHWAY, AND DISRUPTION\nRP   PHENOTYPE.\nRX   PubMed=17353245; DOI=10.1128/aac.01400-06;\nRA   Nazi I., Scott A., Sham A., Rossi L., Williamson P.R., Kronstad J.W.,\nRA   Wright G.D.;\nRT   \"Role of homoserine transacetylase as a new target for antifungal agents.\";\nRL   Antimicrob. Agents Chemother. 51:1731-1736(2007).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:57.924962+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 35-42",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f199a40bd4613a52dfaa0c84625c1bb8a81d2d65e01501415825a1c3b01fb844",
  "url": "https://rest.uniprot.org/unisave/J9VIY8?format=txt&versions=54"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VIY8?format=txt&versions=54)

```json
{
  "entry_version": 54,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=L-homoserine + acetyl-CoA = O-acetyl-L-homoserine + CoA;\nCC         Xref=Rhea:RHEA:13701, ChEBI:CHEBI:57287, ChEBI:CHEBI:57288,\nCC         ChEBI:CHEBI:57476, ChEBI:CHEBI:57716; EC=2.3.1.31;\nCC         Evidence={ECO:0000269|PubMed:17353245};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:13702;\nCC         Evidence={ECO:0000269|PubMed:17353245};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:57.924962+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 45-51",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f199a40bd4613a52dfaa0c84625c1bb8a81d2d65e01501415825a1c3b01fb844",
  "url": "https://rest.uniprot.org/unisave/J9VIY8?format=txt&versions=54"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 135. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
