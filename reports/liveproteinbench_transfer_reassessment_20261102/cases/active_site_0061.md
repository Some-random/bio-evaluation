# active_site_0061

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/active_site_0061.txt)

**Task:** `active_site`  
**Expected answer:** **B** — Position 224 (Proton donor)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MTLTFKPLESYREDFSFRNSPAAIARFPFPFPEDQYMYSVNLEPAVSRDPGSVFEHQFDVDEHYVSEMAERARVLELDPGRCLVMPHMAQAAWDTLAMLMEHLARDYPQHFRLTRQGDAWHWQNLALGIDQRFTFGDPASLPCEPLEYITRQMQGDFAVLDQRDGDLFMDAGMVTCPADWSLRFDAGMSFKQWHSPVPMAHQMGVFDRALKYLLNIQVGAPVRRLNWTLTINPRLDTSPETYHEWGNDRGKVTPDNVGRLVHLRVELQLMARLPRSNALLFGIRTYLISLDELVSNPAWAQRLHRVMRDLPDPIADYKGITRYRQTLVDWLRRFDPEA

[Multiple Choices]
A. Position 4681 (Proton acceptor; for dehydratase activity 2)
B. Position 224 (Proton donor)
C. Position 12 (Proton acceptor)
D. Position 230 (For beta-ketoacyl synthase 1 activity)
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

> The sequence-matched UniProt annotation identifies position 224 as an active-site proton donor. This is a literature-linked curator annotation, not, by itself, direct experimental proof; the cited reference also reports mutagenesis of Arg-224.

Citations as saved: [H3](#evidence-h3), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> In the supplied sequence, position 224 is an arginine in the folded protein's central region. Arginine's protonated guanidinium group can donate a proton but is not a plausible proton acceptor, favoring B over C. Position 4681 is outside the sequence, and beta-ketoacyl synthase activity in D does not fit the sequence context. This is a plausible choice-level inference, not independent proof that position 224 catalyzes the reaction.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Residue chemistry and sequence context meaningfully distinguish the offered choices without relying on the exact protein's recorded annotation, although sequence alone cannot establish the catalytic role with certainty.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No other offered option is comparably defensible: C assigns proton acceptance to an arginine, A gives an out-of-range position, and D names an unrelated enzyme activity.


### Important caveats

- The active-site annotation is supported by a literature-linked curator inference; the supplied excerpts do not independently establish the experimental result in detail.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "In the supplied sequence, position 224 is an arginine in the folded protein's central region. Arginine's protonated guanidinium group can donate a proton but is not a plausible proton acceptor, favoring B over C. Position 4681 is outside the sequence, and beta-ketoacyl synthase activity in D does not fit the sequence context. This is a plausible choice-level inference, not independent proof that position 224 catalyzes the reaction.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Residue chemistry and sequence context meaningfully distinguish the offered choices without relying on the exact protein's recorded annotation, although sequence alone cannot establish the catalytic role with certainty."
  },
  "case_id": "active_site_0061",
  "expected_answer_check": {
    "evidence_ids": [
      "H3",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies position 224 as an active-site proton donor. This is a literature-linked curator annotation, not, by itself, direct experimental proof; the cited reference also reports mutagenesis of Arg-224."
  },
  "important_caveats": [
    "The active-site annotation is supported by a literature-linked curator inference; the supplied excerpts do not independently establish the experimental result in detail."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered option is comparably defensible: C assigns proton acceptance to an arginine, A gives an out-of-range position, and D names an unrelated enzyme activity."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0061",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies position 224 as an active-site proton donor. This is a literature-linked curator annotation, not, by itself, direct experimental proof; the cited reference also reports mutagenesis of Arg-224.",
    "evidence_ids": ["H3", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "In the supplied sequence, position 224 is an arginine in the folded protein's central region. Arginine's protonated guanidinium group can donate a proton but is not a plausible proton acceptor, favoring B over C. Position 4681 is outside the sequence, and beta-ketoacyl synthase activity in D does not fit the sequence context. This is a plausible choice-level inference, not independent proof that position 224 catalyzes the reaction.",
    "missing_item_specific_fact": "",
    "reason": "Residue chemistry and sequence context meaningfully distinguish the offered choices without relying on the exact protein's recorded annotation, although sequence alone cannot establish the catalytic role with certainty."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered option is comparably defensible: C assigns proton acceptance to an arginine, A gives an out-of-range position, and D names an unrelated enzyme activity."
  },
  "important_caveats": [
    "The active-site annotation is supported by a literature-linked curator inference; the supplied excerpts do not independently establish the experimental result in detail."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A4XXY9 annotates position 224 as ACT_SITE with description 'Proton donor' (evidence code ECO:0000305, based on PubMed:27851736). The Nature 2016 paper (PMID 27851736) reports mutagenesis of Arg-224 among key functional residues, supporting its catalytic role. The author's expected answer B (Position 224, Proton donor) matches the database annotation exactly.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C12](#evidence-c12), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Option A (position 4681) is immediately eliminated because the provided sequence is only 338 residues long—position 4681 does not exist. Option D (position 230, 'beta-ketoacyl synthase 1 activity') describes a completely unrelated enzyme class (fatty acid biosynthesis), inconsistent with any oxidative/heme-dependent enzyme context. Between B (position 224) and C (position 12): position 12 lies within the first 4% of a 338-residue globular enzyme, an extremely atypical location for a catalytic residue, which is normally buried in the protein interior. General protein-structure knowledge tells us active sites are internal, not at the extreme N-terminus. Additionally, the sequence contains recognizable heme-binding motifs (HP motifs, conserved His/Pro clusters) concentrated in the C-terminal half (positions ~190–320), placing the catalytic center in that region. Position 224 falls within this catalytic/heme-binding cluster, while position 12 is in the N-terminal extension. These transferable structural and functional principles meaningfully distinguish B from C.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can eliminate A (out-of-range position), D (wrong enzyme class), and C (implausible N-terminal active site location in a 338-aa heme enzyme) using general protein biochemistry. The remaining choice B is supported by the internal positioning consistent with the heme-binding region. This does not require recalling the specific UniProt annotation for this exact protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A and D are clearly wrong (out-of-range position and unrelated enzyme function). Option C is strongly disfavored by the general principle that catalytic residues in multi-domain globular enzymes are not at position 12. Only B remains as a defensible answer.


### Important caveats

- The evidence code for position 224 is ECO:0000305 (inferred by curator), not a direct experimental measurement of the proton-donor role, though it is based on mutagenesis data from the Nature 2016 paper.
- The model cannot see the UniProt accession or organism name from the original input; identification relies on sequence-based reasoning and general knowledge.
- Position 12 (Arg) being the N-terminal residue type does not automatically exclude it, but the structural context of a 338-aa multi-domain heme enzyme makes an N-terminal active site extraordinarily unlikely.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Option A (position 4681) is immediately eliminated because the provided sequence is only 338 residues long—position 4681 does not exist. Option D (position 230, 'beta-ketoacyl synthase 1 activity') describes a completely unrelated enzyme class (fatty acid biosynthesis), inconsistent with any oxidative/heme-dependent enzyme context. Between B (position 224) and C (position 12): position 12 lies within the first 4% of a 338-residue globular enzyme, an extremely atypical location for a catalytic residue, which is normally buried in the protein interior. General protein-structure knowledge tells us active sites are internal, not at the extreme N-terminus. Additionally, the sequence contains recognizable heme-binding motifs (HP motifs, conserved His/Pro clusters) concentrated in the C-terminal half (positions ~190–320), placing the catalytic center in that region. Position 224 falls within this catalytic/heme-binding cluster, while position 12 is in the N-terminal extension. These transferable structural and functional principles meaningfully distinguish B from C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can eliminate A (out-of-range position), D (wrong enzyme class), and C (implausible N-terminal active site location in a 338-aa heme enzyme) using general protein biochemistry. The remaining choice B is supported by the internal positioning consistent with the heme-binding region. This does not require recalling the specific UniProt annotation for this exact protein."
  },
  "case_id": "active_site_0061",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C12",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A4XXY9 annotates position 224 as ACT_SITE with description 'Proton donor' (evidence code ECO:0000305, based on PubMed:27851736). The Nature 2016 paper (PMID 27851736) reports mutagenesis of Arg-224 among key functional residues, supporting its catalytic role. The author's expected answer B (Position 224, Proton donor) matches the database annotation exactly."
  },
  "important_caveats": [
    "The evidence code for position 224 is ECO:0000305 (inferred by curator), not a direct experimental measurement of the proton-donor role, though it is based on mutagenesis data from the Nature 2016 paper.",
    "The model cannot see the UniProt accession or organism name from the original input; identification relies on sequence-based reasoning and general knowledge.",
    "Position 12 (Arg) being the N-terminal residue type does not automatically exclude it, but the structural context of a 338-aa multi-domain heme enzyme makes an N-terminal active site extraordinarily unlikely."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and D are clearly wrong (out-of-range position and unrelated enzyme function). Option C is strongly disfavored by the general principle that catalytic residues in multi-domain globular enzymes are not at position 12. Only B remains as a defensible answer."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0061",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A4XXY9 annotates position 224 as ACT_SITE with description 'Proton donor' (evidence code ECO:0000305, based on PubMed:27851736). The Nature 2016 paper (PMID 27851736) reports mutagenesis of Arg-224 among key functional residues, supporting its catalytic role. The author's expected answer B (Position 224, Proton donor) matches the database annotation exactly.",
    "evidence_ids": ["C5", "H3", "C12", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Option A (position 4681) is immediately eliminated because the provided sequence is only 338 residues long—position 4681 does not exist. Option D (position 230, 'beta-ketoacyl synthase 1 activity') describes a completely unrelated enzyme class (fatty acid biosynthesis), inconsistent with any oxidative/heme-dependent enzyme context. Between B (position 224) and C (position 12): position 12 lies within the first 4% of a 338-residue globular enzyme, an extremely atypical location for a catalytic residue, which is normally buried in the protein interior. General protein-structure knowledge tells us active sites are internal, not at the extreme N-terminus. Additionally, the sequence contains recognizable heme-binding motifs (HP motifs, conserved His/Pro clusters) concentrated in the C-terminal half (positions ~190–320), placing the catalytic center in that region. Position 224 falls within this catalytic/heme-binding cluster, while position 12 is in the N-terminal extension. These transferable structural and functional principles meaningfully distinguish B from C.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can eliminate A (out-of-range position), D (wrong enzyme class), and C (implausible N-terminal active site location in a 338-aa heme enzyme) using general protein biochemistry. The remaining choice B is supported by the internal positioning consistent with the heme-binding region. This does not require recalling the specific UniProt annotation for this exact protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and D are clearly wrong (out-of-range position and unrelated enzyme function). Option C is strongly disfavored by the general principle that catalytic residues in multi-domain globular enzymes are not at position 12. Only B remains as a defensible answer."
  },
  "important_caveats": [
    "The evidence code for position 224 is ECO:0000305 (inferred by curator), not a direct experimental measurement of the proton-donor role, though it is based on mutagenesis data from the Nature 2016 paper.",
    "The model cannot see the UniProt accession or organism name from the original input; identification relies on sequence-based reasoning and general knowledge.",
    "Position 12 (Arg) being the N-terminal residue type does not automatically exclude it, but the structural context of a 338-aa multi-domain heme enzyme makes an N-terminal active site extraordinarily unlikely."
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
  "benchmark_sequence_length": 338,
  "benchmark_sequence_sha256": "75ea9108a4ed3d75fa901ba65e99729712f4656bf9b3d0e96a0e505fcbdb5087",
  "current_entry_audit": {
    "entryVersion": 75,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2007-05-29",
    "sequenceVersion": 1
  },
  "current_record_sha256": "65d3c1576347e504fed534849c54776f620bd7f146082e8f553e0f17d025fbba",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 338,
  "current_source_sequence_sha256": "75ea9108a4ed3d75fa901ba65e99729712f4656bf9b3d0e96a0e505fcbdb5087",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 74,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A4XXY9",
  "selected_historical_entry_version": 74,
  "selected_historical_record_sha256": "89b08a06f96b1f3860d8b7d5d12c92348e7bae650952f557ad480f020fea1521",
  "selected_historical_source_sequence_length": 338,
  "selected_historical_source_sequence_sha256": "75ea9108a4ed3d75fa901ba65e99729712f4656bf9b3d0e96a0e505fcbdb5087",
  "selected_historical_version": {
    "accession": "A4XXY9",
    "database": "Swiss-Prot",
    "entryVersion": 74,
    "firstRelease": "2025_03/2025_03",
    "firstReleaseDate": "18-Jun-2025",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "HODMA_ECTM1",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A4XXY9.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A4XXY9\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:24:59.391884+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "65d3c1576347e504fed534849c54776f620bd7f146082e8f553e0f17d025fbba",
  "url": "https://rest.uniprot.org/uniprotkb/A4XXY9.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A4XXY9.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":75,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2007-05-29\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:24:59.391884+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "65d3c1576347e504fed534849c54776f620bd7f146082e8f553e0f17d025fbba",
  "url": "https://rest.uniprot.org/uniprotkb/A4XXY9.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A4XXY9.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Pseudomonas mendocina\",\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Pseudomonadota\",\"Gammaproteobacteria\",\"Pseudomonadales\",\"Pseudomonadaceae\",\"Ectopseudomonas\"],\"scientificName\":\"Ectopseudomonas mendocina (strain ymp)\",\"taxonId\":399739}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:24:59.391884+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "65d3c1576347e504fed534849c54776f620bd7f146082e8f553e0f17d025fbba",
  "url": "https://rest.uniprot.org/uniprotkb/A4XXY9.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A4XXY9.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"27851736\",\"source\":\"PubMed\"}],\"value\":\"1.14.13.238\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"27851736\",\"source\":\"PubMed\"}],\"value\":\"Heme-dependent oxidative N-demethylase alpha subunit\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"27851736\",\"source\":\"PubMed\"}],\"value\":\"HODM alpha subunit\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:24:59.391884+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "65d3c1576347e504fed534849c54776f620bd7f146082e8f553e0f17d025fbba",
  "url": "https://rest.uniprot.org/uniprotkb/A4XXY9.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A4XXY9.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Proton donor\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"27851736\",\"source\":\"PubMed\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":224},\"start\":{\"modifier\":\"EXACT\",\"value\":224}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-01T06:24:59.391884+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "65d3c1576347e504fed534849c54776f620bd7f146082e8f553e0f17d025fbba",
  "url": "https://rest.uniprot.org/uniprotkb/A4XXY9.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A4XXY9.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"27851736\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"5LTE\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"5LTH\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"5LTI\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:60344\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:60344\",\"name\":\"heme b\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":38},\"start\":{\"modifier\":\"EXACT\",\"value\":38}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-01T06:24:59.391884+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "65d3c1576347e504fed534849c54776f620bd7f146082e8f553e0f17d025fbba",
  "url": "https://rest.uniprot.org/uniprotkb/A4XXY9.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A4XXY9.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"proximal binding residue\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"27851736\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"5LTE\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"5LTH\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"5LTI\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:60344\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:18248\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:60344\",\"name\":\"heme b\"},\"ligandPart\":{\"id\":\"ChEBI:CHEBI:18248\",\"name\":\"Fe\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":194},\"start\":{\"modifier\":\"EXACT\",\"value\":194}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-01T06:24:59.391884+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "65d3c1576347e504fed534849c54776f620bd7f146082e8f553e0f17d025fbba",
  "url": "https://rest.uniprot.org/uniprotkb/A4XXY9.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A4XXY9.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"27851736\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"5LTE\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"5LTH\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"5LTI\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:60344\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:60344\",\"name\":\"heme b\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":226},\"start\":{\"modifier\":\"EXACT\",\"value\":226}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-01T06:24:59.391884+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "65d3c1576347e504fed534849c54776f620bd7f146082e8f553e0f17d025fbba",
  "url": "https://rest.uniprot.org/uniprotkb/A4XXY9.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A4XXY9.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"27851736\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"5LTH\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"5LTI\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58040\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58040\",\"name\":\"dimethylamine\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":266},\"start\":{\"modifier\":\"EXACT\",\"value\":266}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
  "retrieved_utc": "2026-11-01T06:24:59.391884+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "65d3c1576347e504fed534849c54776f620bd7f146082e8f553e0f17d025fbba",
  "url": "https://rest.uniprot.org/uniprotkb/A4XXY9.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A4XXY9.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"27851736\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"5LTE\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"5LTH\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"5LTI\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:60344\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:60344\",\"name\":\"heme b\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":317},\"start\":{\"modifier\":\"EXACT\",\"value\":317}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/6",
  "retrieved_utc": "2026-11-01T06:24:59.391884+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "65d3c1576347e504fed534849c54776f620bd7f146082e8f553e0f17d025fbba",
  "url": "https://rest.uniprot.org/uniprotkb/A4XXY9.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A4XXY9.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"27851736\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"5LTE\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"5LTH\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"5LTI\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:60344\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:60344\",\"name\":\"heme b\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":318},\"start\":{\"modifier\":\"EXACT\",\"value\":318}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/7",
  "retrieved_utc": "2026-11-01T06:24:59.391884+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "65d3c1576347e504fed534849c54776f620bd7f146082e8f553e0f17d025fbba",
  "url": "https://rest.uniprot.org/uniprotkb/A4XXY9.json"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A4XXY9.json)

```json
{
  "evidence_id": "C12",
  "excerpt": "{\"citation\":{\"authors\":[\"Ortmayer M.\",\"Lafite P.\",\"Menon B.R.\",\"Tralau T.\",\"Fisher K.\",\"Denkhaus L.\",\"Scrutton N.S.\",\"Rigby S.E.\",\"Munro A.W.\",\"Hay S.\",\"Leys D.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"27851736\"},{\"database\":\"DOI\",\"id\":\"10.1038/nature20159\"}],\"citationType\":\"journal article\",\"firstPage\":\"593\",\"id\":\"27851736\",\"journal\":\"Nature\",\"lastPage\":\"597\",\"publicationDate\":\"2016\",\"title\":\"An oxidative N-demethylase reveals PAS transition from ubiquitous sensor to enzyme.\",\"volume\":\"539\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"5LTE\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"5LTH\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"5LTI\",\"source\":\"PDB\"}],\"referenceNumber\":2,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (1.65 ANGSTROMS) IN COMPLEXES WITH HEME B AND DIMETHYLAMINE\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"SUBUNIT\",\"DOMAIN\",\"MUTAGENESIS OF TRP-180; ARG-224 AND GLU-266\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-01T06:24:59.391884+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "65d3c1576347e504fed534849c54776f620bd7f146082e8f553e0f17d025fbba",
  "url": "https://rest.uniprot.org/uniprotkb/A4XXY9.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A4XXY9?format=txt&versions=74)

```json
{
  "entry_version": 74,
  "evidence_id": "H1",
  "excerpt": "ID   HODMA_ECTM1             Reviewed;         338 AA.\nAC   A4XXY9;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   29-MAY-2007, sequence version 1.\nDT   18-JUN-2025, entry version 74.\nDE   RecName: Full=Heme-dependent oxidative N-demethylase alpha subunit {ECO:0000303|PubMed:27851736};\nDE            Short=HODM alpha subunit {ECO:0000303|PubMed:27851736};\nDE            EC=1.14.13.238 {ECO:0000269|PubMed:27851736};\nGN   OrderedLocusNames=Pmen_3455 {ECO:0000312|EMBL:ABP86205.1};\nOS   Ectopseudomonas mendocina (strain ymp) (Pseudomonas mendocina).\nOC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria;\nOC   Pseudomonadales; Pseudomonadaceae; Ectopseudomonas.\nOX   NCBI_TaxID=399739;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:45.629873+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "89b08a06f96b1f3860d8b7d5d12c92348e7bae650952f557ad480f020fea1521",
  "url": "https://rest.uniprot.org/unisave/A4XXY9?format=txt&versions=74"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A4XXY9?format=txt&versions=74)

```json
{
  "entry_version": 74,
  "evidence_id": "H2",
  "excerpt": "RN   [2] {ECO:0007744|PDB:5LTE, ECO:0007744|PDB:5LTH, ECO:0007744|PDB:5LTI}\nRP   X-RAY CRYSTALLOGRAPHY (1.65 ANGSTROMS) IN COMPLEXES WITH HEME B AND\nRP   DIMETHYLAMINE, FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES,\nRP   SUBUNIT, DOMAIN, AND MUTAGENESIS OF TRP-180; ARG-224 AND GLU-266.\nRX   PubMed=27851736; DOI=10.1038/nature20159;\nRA   Ortmayer M., Lafite P., Menon B.R., Tralau T., Fisher K., Denkhaus L.,\nRA   Scrutton N.S., Rigby S.E., Munro A.W., Hay S., Leys D.;\nRT   \"An oxidative N-demethylase reveals PAS transition from ubiquitous sensor\nRT   to enzyme.\";\nRL   Nature 539:593-597(2016).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:45.629873+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 24-33",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "89b08a06f96b1f3860d8b7d5d12c92348e7bae650952f557ad480f020fea1521",
  "url": "https://rest.uniprot.org/unisave/A4XXY9?format=txt&versions=74"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A4XXY9?format=txt&versions=74)

```json
{
  "entry_version": 74,
  "evidence_id": "H3",
  "excerpt": "FT   ACT_SITE        224\nFT                   /note=\"Proton donor\"\nFT                   /evidence=\"ECO:0000305|PubMed:27851736\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:45.629873+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 92-94",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "89b08a06f96b1f3860d8b7d5d12c92348e7bae650952f557ad480f020fea1521",
  "url": "https://rest.uniprot.org/unisave/A4XXY9?format=txt&versions=74"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A4XXY9?format=txt&versions=74)

```json
{
  "entry_version": 74,
  "evidence_id": "H4",
  "excerpt": "FT   BINDING         38\nFT                   /ligand=\"heme b\"\nFT                   /ligand_id=\"ChEBI:CHEBI:60344\"\nFT                   /evidence=\"ECO:0000269|PubMed:27851736,\nFT                   ECO:0007744|PDB:5LTE, ECO:0007744|PDB:5LTH,\nFT                   ECO:0007744|PDB:5LTI\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:45.629873+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 95-100",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "89b08a06f96b1f3860d8b7d5d12c92348e7bae650952f557ad480f020fea1521",
  "url": "https://rest.uniprot.org/unisave/A4XXY9?format=txt&versions=74"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A4XXY9?format=txt&versions=74)

```json
{
  "entry_version": 74,
  "evidence_id": "H5",
  "excerpt": "FT   BINDING         194\nFT                   /ligand=\"heme b\"\nFT                   /ligand_id=\"ChEBI:CHEBI:60344\"\nFT                   /ligand_part=\"Fe\"\nFT                   /ligand_part_id=\"ChEBI:CHEBI:18248\"\nFT                   /note=\"proximal binding residue\"\nFT                   /evidence=\"ECO:0000269|PubMed:27851736,\nFT                   ECO:0007744|PDB:5LTE, ECO:0007744|PDB:5LTH,\nFT                   ECO:0007744|PDB:5LTI\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:45.629873+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 101-109",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "89b08a06f96b1f3860d8b7d5d12c92348e7bae650952f557ad480f020fea1521",
  "url": "https://rest.uniprot.org/unisave/A4XXY9?format=txt&versions=74"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A4XXY9?format=txt&versions=74)

```json
{
  "entry_version": 74,
  "evidence_id": "H6",
  "excerpt": "FT   BINDING         226\nFT                   /ligand=\"heme b\"\nFT                   /ligand_id=\"ChEBI:CHEBI:60344\"\nFT                   /evidence=\"ECO:0000269|PubMed:27851736,\nFT                   ECO:0007744|PDB:5LTE, ECO:0007744|PDB:5LTH,\nFT                   ECO:0007744|PDB:5LTI\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:45.629873+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 110-115",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "89b08a06f96b1f3860d8b7d5d12c92348e7bae650952f557ad480f020fea1521",
  "url": "https://rest.uniprot.org/unisave/A4XXY9?format=txt&versions=74"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A4XXY9?format=txt&versions=74)

```json
{
  "entry_version": 74,
  "evidence_id": "H7",
  "excerpt": "FT   BINDING         266\nFT                   /ligand=\"dimethylamine\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58040\"\nFT                   /evidence=\"ECO:0000269|PubMed:27851736,\nFT                   ECO:0007744|PDB:5LTH, ECO:0007744|PDB:5LTI\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:45.629873+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 116-120",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "89b08a06f96b1f3860d8b7d5d12c92348e7bae650952f557ad480f020fea1521",
  "url": "https://rest.uniprot.org/unisave/A4XXY9?format=txt&versions=74"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A4XXY9?format=txt&versions=74)

```json
{
  "entry_version": 74,
  "evidence_id": "H8",
  "excerpt": "FT   BINDING         317\nFT                   /ligand=\"heme b\"\nFT                   /ligand_id=\"ChEBI:CHEBI:60344\"\nFT                   /evidence=\"ECO:0000269|PubMed:27851736,\nFT                   ECO:0007744|PDB:5LTE, ECO:0007744|PDB:5LTH,\nFT                   ECO:0007744|PDB:5LTI\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:45.629873+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 121-126",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "89b08a06f96b1f3860d8b7d5d12c92348e7bae650952f557ad480f020fea1521",
  "url": "https://rest.uniprot.org/unisave/A4XXY9?format=txt&versions=74"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A4XXY9?format=txt&versions=74)

```json
{
  "entry_version": 74,
  "evidence_id": "H9",
  "excerpt": "FT   BINDING         318\nFT                   /ligand=\"heme b\"\nFT                   /ligand_id=\"ChEBI:CHEBI:60344\"\nFT                   /evidence=\"ECO:0000269|PubMed:27851736,\nFT                   ECO:0007744|PDB:5LTE, ECO:0007744|PDB:5LTH,\nFT                   ECO:0007744|PDB:5LTI\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:45.629873+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 127-132",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "89b08a06f96b1f3860d8b7d5d12c92348e7bae650952f557ad480f020fea1521",
  "url": "https://rest.uniprot.org/unisave/A4XXY9?format=txt&versions=74"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 61. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
