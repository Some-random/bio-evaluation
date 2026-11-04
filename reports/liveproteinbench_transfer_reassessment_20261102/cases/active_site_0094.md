# active_site_0094

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/active_site_0094.txt)

**Task:** `active_site`  
**Expected answer:** **D** — Position 154 (Nucleophile)

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
A. Position 119 (For glutaminase activity)
B. Position 2428 (For thioesterase activity)
C. Position 215 (1)
D. Position 154 (Nucleophile)
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzyme Active Site Prediction, which is to identify the key amino acid residues that form the active site of an enzyme. The active site is the specific region on the enzyme where a substrate binds and the chemical reaction is catalyzed. Based on the full protein sequence provided, you must select the option that correctly lists the amino acid residues (by their type and position) that constitute the enzyme's catalytic center.. The inputs provided by the user for this task include:

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

> The matched-sequence UniProt annotation identifies position 154 as the nucleophile. Its evidence is based on a homolog and a family signature, so it supports the key but is not direct experimental validation of this residue in the supplied protein.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a GGSxG-like segment around position 154, with Ser at 154. A conserved GxSxG-like motif is characteristic of catalytic nucleophilic serines in relevant acyltransferase enzyme families, making D a credible family-level inference and distinguishing it from the other listed choices.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A transferable sequence-motif and enzyme-family inference meaningfully supports D; recalling the exact protein's database entry is not necessary. The inference is not by itself proof of experimentally measured catalytic function.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the offered choices, D is the only one that plausibly identifies a catalytic nucleophile at a sequence position supported by the conserved motif.


### Important caveats

- The source annotation for position 154 is supported by homolog transfer and a computational signature, not direct experimental evidence for this exact protein in the supplied excerpts.
- The sequence contains additional annotated active-site positions, but they are not offered as competing choices.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a GGSxG-like segment around position 154, with Ser at 154. A conserved GxSxG-like motif is characteristic of catalytic nucleophilic serines in relevant acyltransferase enzyme families, making D a credible family-level inference and distinguishing it from the other listed choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A transferable sequence-motif and enzyme-family inference meaningfully supports D; recalling the exact protein's database entry is not necessary. The inference is not by itself proof of experimentally measured catalytic function."
  },
  "case_id": "active_site_0094",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The matched-sequence UniProt annotation identifies position 154 as the nucleophile. Its evidence is based on a homolog and a family signature, so it supports the key but is not direct experimental validation of this residue in the supplied protein."
  },
  "important_caveats": [
    "The source annotation for position 154 is supported by homolog transfer and a computational signature, not direct experimental evidence for this exact protein in the supplied excerpts.",
    "The sequence contains additional annotated active-site positions, but they are not offered as competing choices."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, D is the only one that plausibly identifies a catalytic nucleophile at a sequence position supported by the conserved motif."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0094",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched-sequence UniProt annotation identifies position 154 as the nucleophile. Its evidence is based on a homolog and a family signature, so it supports the key but is not direct experimental validation of this residue in the supplied protein.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a GGSxG-like segment around position 154, with Ser at 154. A conserved GxSxG-like motif is characteristic of catalytic nucleophilic serines in relevant acyltransferase enzyme families, making D a credible family-level inference and distinguishing it from the other listed choices.",
    "missing_item_specific_fact": "",
    "reason": "A transferable sequence-motif and enzyme-family inference meaningfully supports D; recalling the exact protein's database entry is not necessary. The inference is not by itself proof of experimentally measured catalytic function."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, D is the only one that plausibly identifies a catalytic nucleophile at a sequence position supported by the conserved motif."
  },
  "important_caveats": [
    "The source annotation for position 154 is supported by homolog transfer and a computational signature, not direct experimental evidence for this exact protein in the supplied excerpts.",
    "The sequence contains additional annotated active-site positions, but they are not offered as competing choices."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (J9VIY8) annotates position 154 as 'Active site' with description 'Nucleophile' (evidence C5, H3). The evidence codes are ECO:0000250 (transferred by similarity to O60062) and ECO:0000255 (PIRSR000443-1, computational family annotation), so this is a computational/similarity-based annotation rather than direct experimental evidence for this specific protein. Nevertheless, the database record explicitly supports the expected answer D.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Multiple transferable features distinguish D from the alternatives: (1) Option B (position 2428) is impossible since the protein is only 528 residues long. (2) Option C has a nonsensical descriptor '(1)', clearly a distractor. (3) Option A claims 'glutaminase activity' at position 119; the sequence lacks glutaminase catalytic motifs (no Cys-His-Asp triad or glutaminase-specific fold), and position 119 is Phe (F), which cannot serve as a nucleophile. (4) Position 154 is Ser (S) embedded in the context 'VGGSMGGMTV', which contains a GxSxG motif (G-G-S-M-G), the canonical nucleophilic elbow signature learned from hundreds of serine hydrolases, acetyltransferases, and α/β-hydrolase-fold enzymes. Recognizing a serine in a GxSxG context as a catalytic nucleophile is standard transferable enzymology knowledge. Additionally, the overall sequence architecture (GNAT-like or acetyltransferase-like fold features) is inconsistent with glutaminase activity, further eliminating A.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can eliminate B (position exceeds protein length), C (nonsensical label), and A (wrong enzyme class, non-catalytic residue at position 119), then identify the GxSxG nucleophilic elbow at position 154 as the hallmark of a serine nucleophile in transferases. This relies on widely learned sequence-motif knowledge from other proteins, not on memorizing this specific entry's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the four offered choices, only D is biochemically coherent: B is geometrically impossible, C is incoherent, and A attributes the wrong activity to a non-catalytic residue. No two options are defensible simultaneously.


### Important caveats

- The UniProt annotation at position 154 is computational (transferred by similarity and PIRSR family), not direct experimental evidence for this specific protein.
- Additional active-site residues (positions 438 and 467) are annotated in the same entry but are not offered as options, so they do not create ambiguity among the given choices.
- The GxSxG motif identification depends on correct sequence counting; miscounting by even one position would shift the residue identity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Multiple transferable features distinguish D from the alternatives: (1) Option B (position 2428) is impossible since the protein is only 528 residues long. (2) Option C has a nonsensical descriptor '(1)', clearly a distractor. (3) Option A claims 'glutaminase activity' at position 119; the sequence lacks glutaminase catalytic motifs (no Cys-His-Asp triad or glutaminase-specific fold), and position 119 is Phe (F), which cannot serve as a nucleophile. (4) Position 154 is Ser (S) embedded in the context 'VGGSMGGMTV', which contains a GxSxG motif (G-G-S-M-G), the canonical nucleophilic elbow signature learned from hundreds of serine hydrolases, acetyltransferases, and α/β-hydrolase-fold enzymes. Recognizing a serine in a GxSxG context as a catalytic nucleophile is standard transferable enzymology knowledge. Additionally, the overall sequence architecture (GNAT-like or acetyltransferase-like fold features) is inconsistent with glutaminase activity, further eliminating A.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can eliminate B (position exceeds protein length), C (nonsensical label), and A (wrong enzyme class, non-catalytic residue at position 119), then identify the GxSxG nucleophilic elbow at position 154 as the hallmark of a serine nucleophile in transferases. This relies on widely learned sequence-motif knowledge from other proteins, not on memorizing this specific entry's annotation."
  },
  "case_id": "active_site_0094",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (J9VIY8) annotates position 154 as 'Active site' with description 'Nucleophile' (evidence C5, H3). The evidence codes are ECO:0000250 (transferred by similarity to O60062) and ECO:0000255 (PIRSR000443-1, computational family annotation), so this is a computational/similarity-based annotation rather than direct experimental evidence for this specific protein. Nevertheless, the database record explicitly supports the expected answer D."
  },
  "important_caveats": [
    "The UniProt annotation at position 154 is computational (transferred by similarity and PIRSR family), not direct experimental evidence for this specific protein.",
    "Additional active-site residues (positions 438 and 467) are annotated in the same entry but are not offered as options, so they do not create ambiguity among the given choices.",
    "The GxSxG motif identification depends on correct sequence counting; miscounting by even one position would shift the residue identity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four offered choices, only D is biochemically coherent: B is geometrically impossible, C is incoherent, and A attributes the wrong activity to a non-catalytic residue. No two options are defensible simultaneously."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0094",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (J9VIY8) annotates position 154 as 'Active site' with description 'Nucleophile' (evidence C5, H3). The evidence codes are ECO:0000250 (transferred by similarity to O60062) and ECO:0000255 (PIRSR000443-1, computational family annotation), so this is a computational/similarity-based annotation rather than direct experimental evidence for this specific protein. Nevertheless, the database record explicitly supports the expected answer D.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Multiple transferable features distinguish D from the alternatives: (1) Option B (position 2428) is impossible since the protein is only 528 residues long. (2) Option C has a nonsensical descriptor '(1)', clearly a distractor. (3) Option A claims 'glutaminase activity' at position 119; the sequence lacks glutaminase catalytic motifs (no Cys-His-Asp triad or glutaminase-specific fold), and position 119 is Phe (F), which cannot serve as a nucleophile. (4) Position 154 is Ser (S) embedded in the context 'VGGSMGGMTV', which contains a GxSxG motif (G-G-S-M-G), the canonical nucleophilic elbow signature learned from hundreds of serine hydrolases, acetyltransferases, and α/β-hydrolase-fold enzymes. Recognizing a serine in a GxSxG context as a catalytic nucleophile is standard transferable enzymology knowledge. Additionally, the overall sequence architecture (GNAT-like or acetyltransferase-like fold features) is inconsistent with glutaminase activity, further eliminating A.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can eliminate B (position exceeds protein length), C (nonsensical label), and A (wrong enzyme class, non-catalytic residue at position 119), then identify the GxSxG nucleophilic elbow at position 154 as the hallmark of a serine nucleophile in transferases. This relies on widely learned sequence-motif knowledge from other proteins, not on memorizing this specific entry's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four offered choices, only D is biochemically coherent: B is geometrically impossible, C is incoherent, and A attributes the wrong activity to a non-catalytic residue. No two options are defensible simultaneously."
  },
  "important_caveats": [
    "The UniProt annotation at position 154 is computational (transferred by similarity and PIRSR family), not direct experimental evidence for this specific protein.",
    "Additional active-site residues (positions 438 and 467) are annotated in the same entry but are not offered as options, so they do not create ambiguity among the given choices.",
    "The GxSxG motif identification depends on correct sequence counting; miscounting by even one position would shift the residue identity."
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
  "excerpt": "{\"description\":\"Nucleophile\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"O60062\",\"source\":\"UniProtKB\"},{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PIRSR000443-1\",\"source\":\"PIRSR\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":154},\"start\":{\"modifier\":\"EXACT\",\"value\":154}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/7",
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
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"O60062\",\"source\":\"UniProtKB\"},{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PIRSR000443-1\",\"source\":\"PIRSR\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":438},\"start\":{\"modifier\":\"EXACT\",\"value\":438}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/8",
  "retrieved_utc": "2026-11-02T04:28:54.980036+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1dd26bd473689f347eca69268d64365a8d99894cc29c382df0bdcbe9218d5cda",
  "url": "https://rest.uniprot.org/uniprotkb/J9VIY8.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VIY8.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"O60062\",\"source\":\"UniProtKB\"},{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PIRSR000443-1\",\"source\":\"PIRSR\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":467},\"start\":{\"modifier\":\"EXACT\",\"value\":467}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/9",
  "retrieved_utc": "2026-11-02T04:28:54.980036+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1dd26bd473689f347eca69268d64365a8d99894cc29c382df0bdcbe9218d5cda",
  "url": "https://rest.uniprot.org/uniprotkb/J9VIY8.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VIY8.json)

```json
{
  "evidence_id": "C8",
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

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VIY8?format=txt&versions=54)

```json
{
  "entry_version": 54,
  "evidence_id": "H3",
  "excerpt": "FT   ACT_SITE        154\nFT                   /note=\"Nucleophile\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:O60062,\nFT                   ECO:0000255|PIRSR:PIRSR000443-1\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:57.924962+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 118-121",
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
  "excerpt": "FT   ACT_SITE        438\nFT                   /evidence=\"ECO:0000250|UniProtKB:O60062,\nFT                   ECO:0000255|PIRSR:PIRSR000443-1\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:57.924962+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 122-124",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f199a40bd4613a52dfaa0c84625c1bb8a81d2d65e01501415825a1c3b01fb844",
  "url": "https://rest.uniprot.org/unisave/J9VIY8?format=txt&versions=54"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VIY8?format=txt&versions=54)

```json
{
  "entry_version": 54,
  "evidence_id": "H5",
  "excerpt": "FT   ACT_SITE        467\nFT                   /evidence=\"ECO:0000250|UniProtKB:O60062,\nFT                   ECO:0000255|PIRSR:PIRSR000443-1\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:57.924962+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 125-127",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f199a40bd4613a52dfaa0c84625c1bb8a81d2d65e01501415825a1c3b01fb844",
  "url": "https://rest.uniprot.org/unisave/J9VIY8?format=txt&versions=54"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 94. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
