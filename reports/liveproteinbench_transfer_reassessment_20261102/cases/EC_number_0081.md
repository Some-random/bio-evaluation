# EC_number_0081

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0081.txt)

**Task:** `EC_number`  
**Expected answer:** **B** — 2.5.1.160

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MAVSSCARAFPSFECRSDAEFSGGIPRHDIPNSGKASILSHGSSVHGLSSLIYRFPPNFVRQLSIKARRNCSNIGVAQVVAASWSNNNSSPDFTPVAKAVDAAAAAAAAIAPVDTTVVNEDVALVENETCNDQNVQFDSLPSMKYASFLNSDGSVAIHAGERLGRGIVTDAITTPVVNTSAYFFNKTSELIDFKEKRRASFEYGRYGNPTTVVLEEKISALEGAESTLLMASGMCASTVMLLALVPAGGHIVTTTDCYRKTRIFIETILPKMGITATVIDPADVGALELALNQKKVNLFFTESPTNPFLRCVDIELVSKLCHEKGALVCIDGTFATPLNQKALALGADLVLHSATKFLGGHNDVLAGCISGPLKLVSEIRNLHHILGGALNPNAAYLIIRGMKTLHLRVQQQNSTALRMAEILEAHPKVRHVYYPGLQSHPEHHIAKKQMTGFGGVVSFEVDGDLLTTAKFVDALKIPYIAPSFGGCESIVDQPAIMSYWDLSQSDRAKYGIMDNLVRFSFGVEDFDDLKADILQALDSI

[Multiple Choices]
A. 2.5.1.56
B. 2.5.1.160
C. 2.4.1.392
D. 1.14.14.154
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

> The matched sequence's UniProt entry assigns EC 2.5.1.160 and gives the corresponding O-phosphohomoserine reaction, citing experimental evidence (ECO:0000269). The cited reference is a characterization study, although it was not independently reviewed here.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminus is consistent with a plant plastid-targeting peptide, and the long enzyme core is consistent with a PLP-dependent cystathionine synthase family enzyme. Transferable knowledge of plant methionine biosynthesis favors the O-phosphohomoserine route (B) over the succinyl-homoserine-related alternative (A). The other choices describe a glycosyltransferase or an oxidoreductase and are much less consistent with this sequence and context.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family and pathway-level knowledge gives a meaningful probabilistic distinction among the offered choices without needing the exact protein's database annotation. Sequence alone does not prove substrate specificity, so the distinction is not certain.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The alternatives are distinct EC classifications, and the sequence/context favors B. The available evidence mentions an alternative succinyl-homoserine reaction only as a curator-inferred reaction, not as an equally established basis for choosing A.


### Important caveats

- The source annotation matches the supplied sequence and cites experimental evidence, but the primary study was not independently assessed.
- The plant/plastid inference comes from the sequence itself and transferable biological knowledge, not from reviewer-only organism or accession information.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminus is consistent with a plant plastid-targeting peptide, and the long enzyme core is consistent with a PLP-dependent cystathionine synthase family enzyme. Transferable knowledge of plant methionine biosynthesis favors the O-phosphohomoserine route (B) over the succinyl-homoserine-related alternative (A). The other choices describe a glycosyltransferase or an oxidoreductase and are much less consistent with this sequence and context.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family and pathway-level knowledge gives a meaningful probabilistic distinction among the offered choices without needing the exact protein's database annotation. Sequence alone does not prove substrate specificity, so the distinction is not certain."
  },
  "case_id": "EC_number_0081",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C7"
    ],
    "judgment": "supported",
    "reason": "The matched sequence's UniProt entry assigns EC 2.5.1.160 and gives the corresponding O-phosphohomoserine reaction, citing experimental evidence (ECO:0000269). The cited reference is a characterization study, although it was not independently reviewed here."
  },
  "important_caveats": [
    "The source annotation matches the supplied sequence and cites experimental evidence, but the primary study was not independently assessed.",
    "The plant/plastid inference comes from the sequence itself and transferable biological knowledge, not from reviewer-only organism or accession information."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives are distinct EC classifications, and the sequence/context favors B. The available evidence mentions an alternative succinyl-homoserine reaction only as a curator-inferred reaction, not as an equally established basis for choosing A."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0081",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched sequence's UniProt entry assigns EC 2.5.1.160 and gives the corresponding O-phosphohomoserine reaction, citing experimental evidence (ECO:0000269). The cited reference is a characterization study, although it was not independently reviewed here.",
    "evidence_ids": ["C4", "C5", "C7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminus is consistent with a plant plastid-targeting peptide, and the long enzyme core is consistent with a PLP-dependent cystathionine synthase family enzyme. Transferable knowledge of plant methionine biosynthesis favors the O-phosphohomoserine route (B) over the succinyl-homoserine-related alternative (A). The other choices describe a glycosyltransferase or an oxidoreductase and are much less consistent with this sequence and context.",
    "missing_item_specific_fact": "",
    "reason": "Family and pathway-level knowledge gives a meaningful probabilistic distinction among the offered choices without needing the exact protein's database annotation. Sequence alone does not prove substrate specificity, so the distinction is not certain."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives are distinct EC classifications, and the sequence/context favors B. The available evidence mentions an alternative succinyl-homoserine reaction only as a curator-inferred reaction, not as an equally established basis for choosing A."
  },
  "important_caveats": [
    "The source annotation matches the supplied sequence and cites experimental evidence, but the primary study was not independently assessed.",
    "The plant/plastid inference comes from the sequence itself and transferable biological knowledge, not from reviewer-only organism or accession information."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q9ZPL5 (CGS1_TOBAC, Cystathionine gamma-synthase 1, chloroplastic) assigns EC 2.5.1.160 with experimental evidence (ECO:0000269|PubMed:10595588). The catalytic activity (O-phospho-L-homoserine + L-cysteine = L,L-cystathionine + phosphate) is directly supported by the cited 1999 Clausen et al. paper. The sequence match is confirmed (sha256 match, 540 AA). The expected answer B (2.5.1.160) is well-supported by experimental data.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the hallmark 'SGMCAST' PLP-binding motif (residues ~265-271) and the 'HHILGG' motif, which are diagnostic of fold-type I PLP-dependent enzymes in the transaminase/synthase superfamily. This immediately eliminates C (2.4.1.392, a glycosyltransferase) and D (1.14.14.154, a heme-containing oxidoreductase), as neither uses PLP. The N-terminal ~130 residues show the composition and length typical of a chloroplast transit peptide (serine/threonine-rich, lacking acidic residues, with multiple arginines), consistent with plant chloroplastic CGS. The 'SGMCAST' motif specifically is a well-known signature of cystathionine gamma-synthase (CGS) among EC 2.5.1.x enzymes; it distinguishes CGS from cystathionine beta-synthase (which uses a different PLP-binding arrangement) and from other alkyl-transferases. The overall domain architecture (the 'GADLVLHSATKFLGGHNDVLAGCISGPLKLVSEIRNLHHILGG' segment) matches published CGS structures. While both A (2.5.1.56) and B (2.5.1.160) fall within EC 2.5.1.x, the specific SGMCAST motif and chloroplast targeting signal are transferable knowledge from CGS homologs in Arabidopsis, E. coli, and other organisms that meaningfully favor B over A.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The PLP-binding motifs (SGMCAST, HHILGG) and chloroplast transit peptide provide transferable family-level knowledge from known CGS homologs that distinguishes B from C and D decisively, and provides a reasonable probabilistic argument favoring B over A within the EC 2.5.1.x subclass. The SGMCAST motif is a recognized CGS-specific signature learned from multiple CGS structures and sequences across organisms.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options C and D are clearly eliminated by the PLP-binding motifs. Between A and B, the SGMCAST motif and chloroplast transit peptide provide a reasonable basis to favor B (CGS) over A (2.5.1.56), though the distinction between these two EC 2.5.1.x entries from sequence alone is less absolute than the elimination of C and D. Still, the specific CGS-associated sequence architecture makes B the most defensible choice.


### Important caveats

- The distinction between EC 2.5.1.56 and EC 2.5.1.160 from sequence alone relies on recognizing the SGMCAST motif as CGS-specific; if 2.5.1.56 were a very closely related enzyme, the margin would narrow.
- The chloroplast transit peptide inference is based on general composition patterns (Ser/Thr/Arg-rich, no acidic residues in the N-terminal ~130 residues) rather than a validated transit-prediction tool output.
- The UniProt annotation for this entry was first released in 2025-06-18 (Swiss-Prot), so the historical availability of this specific annotation to the benchmark author is noted but does not affect the scientific validity of the answer.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the hallmark 'SGMCAST' PLP-binding motif (residues ~265-271) and the 'HHILGG' motif, which are diagnostic of fold-type I PLP-dependent enzymes in the transaminase/synthase superfamily. This immediately eliminates C (2.4.1.392, a glycosyltransferase) and D (1.14.14.154, a heme-containing oxidoreductase), as neither uses PLP. The N-terminal ~130 residues show the composition and length typical of a chloroplast transit peptide (serine/threonine-rich, lacking acidic residues, with multiple arginines), consistent with plant chloroplastic CGS. The 'SGMCAST' motif specifically is a well-known signature of cystathionine gamma-synthase (CGS) among EC 2.5.1.x enzymes; it distinguishes CGS from cystathionine beta-synthase (which uses a different PLP-binding arrangement) and from other alkyl-transferases. The overall domain architecture (the 'GADLVLHSATKFLGGHNDVLAGCISGPLKLVSEIRNLHHILGG' segment) matches published CGS structures. While both A (2.5.1.56) and B (2.5.1.160) fall within EC 2.5.1.x, the specific SGMCAST motif and chloroplast targeting signal are transferable knowledge from CGS homologs in Arabidopsis, E. coli, and other organisms that meaningfully favor B over A.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The PLP-binding motifs (SGMCAST, HHILGG) and chloroplast transit peptide provide transferable family-level knowledge from known CGS homologs that distinguishes B from C and D decisively, and provides a reasonable probabilistic argument favoring B over A within the EC 2.5.1.x subclass. The SGMCAST motif is a recognized CGS-specific signature learned from multiple CGS structures and sequences across organisms."
  },
  "case_id": "EC_number_0081",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C7",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q9ZPL5 (CGS1_TOBAC, Cystathionine gamma-synthase 1, chloroplastic) assigns EC 2.5.1.160 with experimental evidence (ECO:0000269|PubMed:10595588). The catalytic activity (O-phospho-L-homoserine + L-cysteine = L,L-cystathionine + phosphate) is directly supported by the cited 1999 Clausen et al. paper. The sequence match is confirmed (sha256 match, 540 AA). The expected answer B (2.5.1.160) is well-supported by experimental data."
  },
  "important_caveats": [
    "The distinction between EC 2.5.1.56 and EC 2.5.1.160 from sequence alone relies on recognizing the SGMCAST motif as CGS-specific; if 2.5.1.56 were a very closely related enzyme, the margin would narrow.",
    "The chloroplast transit peptide inference is based on general composition patterns (Ser/Thr/Arg-rich, no acidic residues in the N-terminal ~130 residues) rather than a validated transit-prediction tool output.",
    "The UniProt annotation for this entry was first released in 2025-06-18 (Swiss-Prot), so the historical availability of this specific annotation to the benchmark author is noted but does not affect the scientific validity of the answer."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C and D are clearly eliminated by the PLP-binding motifs. Between A and B, the SGMCAST motif and chloroplast transit peptide provide a reasonable basis to favor B (CGS) over A (2.5.1.56), though the distinction between these two EC 2.5.1.x entries from sequence alone is less absolute than the elimination of C and D. Still, the specific CGS-associated sequence architecture makes B the most defensible choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0081",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q9ZPL5 (CGS1_TOBAC, Cystathionine gamma-synthase 1, chloroplastic) assigns EC 2.5.1.160 with experimental evidence (ECO:0000269|PubMed:10595588). The catalytic activity (O-phospho-L-homoserine + L-cysteine = L,L-cystathionine + phosphate) is directly supported by the cited 1999 Clausen et al. paper. The sequence match is confirmed (sha256 match, 540 AA). The expected answer B (2.5.1.160) is well-supported by experimental data.",
    "evidence_ids": ["C4", "C5", "C7", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the hallmark 'SGMCAST' PLP-binding motif (residues ~265-271) and the 'HHILGG' motif, which are diagnostic of fold-type I PLP-dependent enzymes in the transaminase/synthase superfamily. This immediately eliminates C (2.4.1.392, a glycosyltransferase) and D (1.14.14.154, a heme-containing oxidoreductase), as neither uses PLP. The N-terminal ~130 residues show the composition and length typical of a chloroplast transit peptide (serine/threonine-rich, lacking acidic residues, with multiple arginines), consistent with plant chloroplastic CGS. The 'SGMCAST' motif specifically is a well-known signature of cystathionine gamma-synthase (CGS) among EC 2.5.1.x enzymes; it distinguishes CGS from cystathionine beta-synthase (which uses a different PLP-binding arrangement) and from other alkyl-transferases. The overall domain architecture (the 'GADLVLHSATKFLGGHNDVLAGCISGPLKLVSEIRNLHHILGG' segment) matches published CGS structures. While both A (2.5.1.56) and B (2.5.1.160) fall within EC 2.5.1.x, the specific SGMCAST motif and chloroplast targeting signal are transferable knowledge from CGS homologs in Arabidopsis, E. coli, and other organisms that meaningfully favor B over A.",
    "missing_item_specific_fact": "",
    "reason": "The PLP-binding motifs (SGMCAST, HHILGG) and chloroplast transit peptide provide transferable family-level knowledge from known CGS homologs that distinguishes B from C and D decisively, and provides a reasonable probabilistic argument favoring B over A within the EC 2.5.1.x subclass. The SGMCAST motif is a recognized CGS-specific signature learned from multiple CGS structures and sequences across organisms."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C and D are clearly eliminated by the PLP-binding motifs. Between A and B, the SGMCAST motif and chloroplast transit peptide provide a reasonable basis to favor B (CGS) over A (2.5.1.56), though the distinction between these two EC 2.5.1.x entries from sequence alone is less absolute than the elimination of C and D. Still, the specific CGS-associated sequence architecture makes B the most defensible choice."
  },
  "important_caveats": [
    "The distinction between EC 2.5.1.56 and EC 2.5.1.160 from sequence alone relies on recognizing the SGMCAST motif as CGS-specific; if 2.5.1.56 were a very closely related enzyme, the margin would narrow.",
    "The chloroplast transit peptide inference is based on general composition patterns (Ser/Thr/Arg-rich, no acidic residues in the N-terminal ~130 residues) rather than a validated transit-prediction tool output.",
    "The UniProt annotation for this entry was first released in 2025-06-18 (Swiss-Prot), so the historical availability of this specific annotation to the benchmark author is noted but does not affect the scientific validity of the answer."
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
  "benchmark_sequence_length": 540,
  "benchmark_sequence_sha256": "ba16e25199265c199c5f6fa664cd94c6606bb9ff0eb538cf1ec6625421ac5a8a",
  "current_entry_audit": {
    "entryVersion": 112,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-06-18",
    "sequenceVersion": 2
  },
  "current_record_sha256": "eba20b71fa68300db26e07dbef891aceaac0dafd788c516e4e6cd7e6d24a0088",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 540,
  "current_source_sequence_sha256": "ba16e25199265c199c5f6fa664cd94c6606bb9ff0eb538cf1ec6625421ac5a8a",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 110,
      "exact_sequence_comparison": "matched",
      "sequence_version": 2
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q9ZPL5",
  "selected_historical_entry_version": 110,
  "selected_historical_record_sha256": "3437ba65b4e8147dfa9317dbc3f6f4d938558890b29fbadf232e8d98ba79ca89",
  "selected_historical_source_sequence_length": 540,
  "selected_historical_source_sequence_sha256": "ba16e25199265c199c5f6fa664cd94c6606bb9ff0eb538cf1ec6625421ac5a8a",
  "selected_historical_version": {
    "accession": "Q9ZPL5",
    "database": "Swiss-Prot",
    "entryVersion": 110,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "CGS1_TOBAC",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9ZPL5.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q9ZPL5\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:33:56.568005+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "eba20b71fa68300db26e07dbef891aceaac0dafd788c516e4e6cd7e6d24a0088",
  "url": "https://rest.uniprot.org/uniprotkb/Q9ZPL5.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9ZPL5.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":112,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-06-18\",\"sequenceVersion\":2}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:33:56.568005+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "eba20b71fa68300db26e07dbef891aceaac0dafd788c516e4e6cd7e6d24a0088",
  "url": "https://rest.uniprot.org/uniprotkb/Q9ZPL5.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9ZPL5.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Common tobacco\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"asterids\",\"lamiids\",\"Solanales\",\"Solanaceae\",\"Nicotianoideae\",\"Nicotianeae\",\"Nicotiana\"],\"scientificName\":\"Nicotiana tabacum\",\"taxonId\":4097}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:33:56.568005+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "eba20b71fa68300db26e07dbef891aceaac0dafd788c516e4e6cd7e6d24a0088",
  "url": "https://rest.uniprot.org/uniprotkb/Q9ZPL5.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9ZPL5.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"10595588\",\"source\":\"PubMed\"}],\"value\":\"2.5.1.160\"}],\"fullName\":{\"value\":\"Cystathionine gamma-synthase 1, chloroplastic\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:33:56.568005+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "eba20b71fa68300db26e07dbef891aceaac0dafd788c516e4e6cd7e6d24a0088",
  "url": "https://rest.uniprot.org/uniprotkb/Q9ZPL5.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9ZPL5.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"2.5.1.160\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"10595588\",\"source\":\"PubMed\"}],\"name\":\"O-phospho-L-homoserine + L-cysteine = L,L-cystathionine + phosphate\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:80891\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:35235\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:43474\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57590\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58161\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:33:56.568005+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "eba20b71fa68300db26e07dbef891aceaac0dafd788c516e4e6cd7e6d24a0088",
  "url": "https://rest.uniprot.org/uniprotkb/Q9ZPL5.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9ZPL5.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"10595588\",\"source\":\"PubMed\"}],\"name\":\"O-succinyl-L-homoserine + L-cysteine = L,L-cystathionine + succinate + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:20397\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:30031\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:35235\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57661\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58161\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:33:56.568005+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "eba20b71fa68300db26e07dbef891aceaac0dafd788c516e4e6cd7e6d24a0088",
  "url": "https://rest.uniprot.org/uniprotkb/Q9ZPL5.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9ZPL5.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Clausen T.\",\"Wahl M.C.\",\"Messerschmidt A.\",\"Huber R.\",\"Fuhrmann J.C.\",\"Laber B.\",\"Streber W.\",\"Steegborn C.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"10595588\"},{\"database\":\"DOI\",\"id\":\"10.1515/bc.1999.157\"}],\"citationType\":\"journal article\",\"firstPage\":\"1237\",\"id\":\"10595588\",\"journal\":\"Biol. Chem.\",\"lastPage\":\"1242\",\"publicationDate\":\"1999\",\"title\":\"Cloning, purification and characterisation of cystathionine gamma-synthase from Nicotiana tabacum.\",\"volume\":\"380\"},\"referenceNumber\":3,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA] OF 97-540\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"ACTIVITY REGULATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-02T04:33:56.568005+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "eba20b71fa68300db26e07dbef891aceaac0dafd788c516e4e6cd7e6d24a0088",
  "url": "https://rest.uniprot.org/uniprotkb/Q9ZPL5.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9ZPL5?format=txt&versions=110)

```json
{
  "entry_version": 110,
  "evidence_id": "H1",
  "excerpt": "ID   CGS1_TOBAC              Reviewed;         540 AA.\nAC   Q9ZPL5; W8SGH6;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   18-JUN-2025, sequence version 2.\nDT   28-JAN-2026, entry version 110.\nDE   RecName: Full=Cystathionine gamma-synthase 1, chloroplastic;\nDE            EC=2.5.1.160 {ECO:0000269|PubMed:10595588};\nDE   Flags: Precursor;\nGN   Name=CGS1 {ECO:0000305}; ORFNames=LOC107822634;\nOS   Nicotiana tabacum (Common tobacco).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   asterids; lamiids; Solanales; Solanaceae; Nicotianoideae; Nicotianeae;\nOC   Nicotiana.\nOX   NCBI_TaxID=4097;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:34:02.156603+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3437ba65b4e8147dfa9317dbc3f6f4d938558890b29fbadf232e8d98ba79ca89",
  "url": "https://rest.uniprot.org/unisave/Q9ZPL5?format=txt&versions=110"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9ZPL5?format=txt&versions=110)

```json
{
  "entry_version": 110,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Cystathionine gamma-synthase 1, chloroplastic;\nDE            EC=2.5.1.160 {ECO:0000269|PubMed:10595588};\nDE   Flags: Precursor;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:34:02.156603+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-8",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3437ba65b4e8147dfa9317dbc3f6f4d938558890b29fbadf232e8d98ba79ca89",
  "url": "https://rest.uniprot.org/unisave/Q9ZPL5?format=txt&versions=110"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9ZPL5?format=txt&versions=110)

```json
{
  "entry_version": 110,
  "evidence_id": "H3",
  "excerpt": "RN   [3]\nRP   NUCLEOTIDE SEQUENCE [MRNA] OF 97-540, FUNCTION, CATALYTIC ACTIVITY,\nRP   BIOPHYSICOCHEMICAL PROPERTIES, AND ACTIVITY REGULATION.\nRX   PubMed=10595588; DOI=10.1515/bc.1999.157;\nRA   Clausen T., Wahl M.C., Messerschmidt A., Huber R., Fuhrmann J.C., Laber B.,\nRA   Streber W., Steegborn C.;\nRT   \"Cloning, purification and characterisation of cystathionine gamma-synthase\nRT   from Nicotiana tabacum.\";\nRL   Biol. Chem. 380:1237-1242(1999).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:34:02.156603+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 29-37",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3437ba65b4e8147dfa9317dbc3f6f4d938558890b29fbadf232e8d98ba79ca89",
  "url": "https://rest.uniprot.org/unisave/Q9ZPL5?format=txt&versions=110"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9ZPL5?format=txt&versions=110)

```json
{
  "entry_version": 110,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=O-phospho-L-homoserine + L-cysteine = L,L-cystathionine +\nCC         phosphate; Xref=Rhea:RHEA:80891, ChEBI:CHEBI:35235,\nCC         ChEBI:CHEBI:43474, ChEBI:CHEBI:57590, ChEBI:CHEBI:58161;\nCC         EC=2.5.1.160; Evidence={ECO:0000269|PubMed:10595588};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:34:02.156603+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 58-62",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3437ba65b4e8147dfa9317dbc3f6f4d938558890b29fbadf232e8d98ba79ca89",
  "url": "https://rest.uniprot.org/unisave/Q9ZPL5?format=txt&versions=110"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9ZPL5?format=txt&versions=110)

```json
{
  "entry_version": 110,
  "evidence_id": "H5",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=O-succinyl-L-homoserine + L-cysteine = L,L-cystathionine +\nCC         succinate + H(+); Xref=Rhea:RHEA:20397, ChEBI:CHEBI:15378,\nCC         ChEBI:CHEBI:30031, ChEBI:CHEBI:35235, ChEBI:CHEBI:57661,\nCC         ChEBI:CHEBI:58161; Evidence={ECO:0000305|PubMed:10595588};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:34:02.156603+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 63-67",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3437ba65b4e8147dfa9317dbc3f6f4d938558890b29fbadf232e8d98ba79ca89",
  "url": "https://rest.uniprot.org/unisave/Q9ZPL5?format=txt&versions=110"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 81. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
