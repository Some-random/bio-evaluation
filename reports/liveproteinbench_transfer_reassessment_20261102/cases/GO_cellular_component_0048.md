# GO_cellular_component_0048

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_cellular_component_0048.txt)

**Task:** `GO_cellular_component`  
**Expected answer:** **D** — plasma membrane

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MRVLALSAVFLVASIIGMPAVAKEWQENKSWNAHFTEHKSQGVVVLWNENKQQGFTNNLKRANQAFLPASTFKIPNSLIALDLGVVKDEHQVFKWDGQTRDIATWNRDHNLITAMKYSVVPVYQEFARQIGEARMSKMLHAFDYGNEDISGNVDSFWLDGGIRISATEQISFLRKLYHNKLHVSERSQRIVKQAMLTEANGDYIIRAKTGYSTRIEPKIGWWVGWVELDDNVWFFAMNMDMPTSDGLGLRQAITKEVLKQEKIIP

[Multiple Choices]
A. spindle
B. apicoplast
C. early endosome membrane
D. plasma membrane
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Cellular Component Prediction, which is to predict the primary Cellular Component where a protein is located, according to the Gene Ontology (GO) framework. A protein's location within a cell (e.g., Nucleus, Mitochondria, Cytoplasm) is critical for its function and is often determined by specific targeting signals in its amino acid sequence. Based on the provided sequence, you must identify the most likely compartment where the protein resides.. The inputs provided by the user for this task include:

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

> The sequence-matched UniProt records assign GO:0005886, plasma membrane, to this protein. This is computational evidence (IEA:TreeGrafter), so it supports the expected GO annotation but does not establish experimental localization.

Citations as saved: [C5](#evidence-c5), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal hydrophobic stretch is consistent with a secretion signal, and the sequence is consistent with a soluble beta-lactamase rather than a eukaryotic organelle or spindle protein. Transferable knowledge of bacterial beta-lactamases and their export makes the bacterial cell boundary the only plausible offered choice, distinguishing D from A–C. This does not independently establish plasma-membrane residence.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level and sequence-feature inference meaningfully favors D among these alternatives. The exact TreeGrafter annotation is not needed to distinguish D from the eukaryotic compartments, though it is the direct support for the recorded GO term.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No alternative offered is comparably plausible. However, the inferred bacterial beta-lactamase localization is consistent with export to the periplasm, which is not an offered option and is not the same as demonstrating membrane association.


### Important caveats

- The direct evidence for the expected term is computational GO annotation, not experimental localization evidence.
- A secretion signal supports export but does not by itself show that the mature enzyme is membrane-bound.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic stretch is consistent with a secretion signal, and the sequence is consistent with a soluble beta-lactamase rather than a eukaryotic organelle or spindle protein. Transferable knowledge of bacterial beta-lactamases and their export makes the bacterial cell boundary the only plausible offered choice, distinguishing D from A–C. This does not independently establish plasma-membrane residence.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level and sequence-feature inference meaningfully favors D among these alternatives. The exact TreeGrafter annotation is not needed to distinguish D from the eukaryotic compartments, though it is the direct support for the recorded GO term."
  },
  "case_id": "GO_cellular_component_0048",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt records assign GO:0005886, plasma membrane, to this protein. This is computational evidence (IEA:TreeGrafter), so it supports the expected GO annotation but does not establish experimental localization."
  },
  "important_caveats": [
    "The direct evidence for the expected term is computational GO annotation, not experimental localization evidence.",
    "A secretion signal supports export but does not by itself show that the mature enzyme is membrane-bound."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No alternative offered is comparably plausible. However, the inferred bacterial beta-lactamase localization is consistent with export to the periplasm, which is not an offered option and is not the same as demonstrating membrane association."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0048",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt records assign GO:0005886, plasma membrane, to this protein. This is computational evidence (IEA:TreeGrafter), so it supports the expected GO annotation but does not establish experimental localization.",
    "evidence_ids": ["C5", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal hydrophobic stretch is consistent with a secretion signal, and the sequence is consistent with a soluble beta-lactamase rather than a eukaryotic organelle or spindle protein. Transferable knowledge of bacterial beta-lactamases and their export makes the bacterial cell boundary the only plausible offered choice, distinguishing D from A–C. This does not independently establish plasma-membrane residence.",
    "missing_item_specific_fact": "",
    "reason": "Family-level and sequence-feature inference meaningfully favors D among these alternatives. The exact TreeGrafter annotation is not needed to distinguish D from the eukaryotic compartments, though it is the direct support for the recorded GO term."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No alternative offered is comparably plausible. However, the inferred bacterial beta-lactamase localization is consistent with export to the periplasm, which is not an offered option and is not the same as demonstrating membrane association."
  },
  "important_caveats": [
    "The direct evidence for the expected term is computational GO annotation, not experimental localization evidence.",
    "A secretion signal supports export but does not by itself show that the mature enzyme is membrane-bound."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry for this sequence (Q6XEC0, Beta-lactamase OXA-48 from Klebsiella pneumoniae) carries the GO annotation GO:0005886 (plasma membrane), matching option D. The evidence code is IEA:TreeGrafter (computational inference by phylogenetic tree grafting), not direct experimental localization. However, the annotation is consistent with the protein's biology: it is a Sec-exported bacterial enzyme (precursor with N-terminal signal peptide) in a Gram-negative organism, and GO:0005886 includes 'cytoplasmic membrane' as an EXACT synonym for the bacterial inner membrane. The annotation is the recorded database fact and is biologically plausible for a membrane-adjacent beta-lactamase, though the evidence level is computational rather than experimental.

Citations as saved: [C5](#evidence-c5), [H6](#evidence-h6), [C4](#evidence-c4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal sequence MRVLALSAVFLVASIIGMPAV is a classic Sec-type signal peptide (positively charged N-region, ~18-residue hydrophobic H-region, polar C-region with cleavage site). This is a highly transferable feature: Sec signal peptides direct proteins across the inner (plasma) membrane in bacteria. The protein is small (265 aa), lacks any eukaryotic targeting motifs (no nuclear localization signal, no apicoplast transit peptide with its characteristic arginine-rich/serine-rich pattern, no endosomal sorting signals), and its overall composition and motif architecture (SXXK, SDN, KTG-like motifs visible in the mature region) are consistent with a bacterial serine beta-lactamase. Among the four options: (A) spindle is a eukaryotic microtubule structure incompatible with a Sec-exported bacterial enzyme; (B) apicoplast exists only in apicomplexans and requires a distinct transit peptide; (C) early endosome membrane is a eukaryotic vesicular compartment requiring eukaryotic sorting signals. The Sec signal peptide and bacterial protein character point directly to (D) plasma membrane as the only compartment consistent with the sequence features.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can identify the Sec signal peptide from the hydrophobic N-terminal stretch, recognize the absence of eukaryotic targeting features, and infer bacterial plasma membrane association. This is a standard sequence-feature-to-localization inference taught in biochemistry and does not require recalling the specific UniProt annotation for OXA-48.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The three distractors (spindle, apicoplast, early endosome membrane) are all eukaryotic compartments with no plausible connection to a small Sec-exported bacterial enzyme. Only plasma membrane is compatible with the identified sequence features. No alternative option is defensible given the signal peptide and bacterial protein character.


### Important caveats

- The GO annotation is IEA:TreeGrafter (computational phylogenetic inference), not experimental localization. The actual subcellular distribution of OXA-48 in Gram-negative bacteria may be periplasmic rather than tightly membrane-associated, but periplasm is not among the options.
- The protein is flagged as 'Precursor' in UniProt, confirming the signal peptide; the mature protein after signal peptide cleavage would reside on the periplasmic face of the inner membrane or in the periplasm.
- GO:0005886 in bacterial context is equivalent to the inner/cytoplasmic membrane, making 'plasma membrane' the correct GO term for the membrane the Sec machinery crosses.
- The reviewer-only evidence identifies the organism (K. pneumoniae) and protein name (OXA-48); the evaluated model only sees the raw sequence and must infer bacterial origin from sequence features alone.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal sequence MRVLALSAVFLVASIIGMPAV is a classic Sec-type signal peptide (positively charged N-region, ~18-residue hydrophobic H-region, polar C-region with cleavage site). This is a highly transferable feature: Sec signal peptides direct proteins across the inner (plasma) membrane in bacteria. The protein is small (265 aa), lacks any eukaryotic targeting motifs (no nuclear localization signal, no apicoplast transit peptide with its characteristic arginine-rich/serine-rich pattern, no endosomal sorting signals), and its overall composition and motif architecture (SXXK, SDN, KTG-like motifs visible in the mature region) are consistent with a bacterial serine beta-lactamase. Among the four options: (A) spindle is a eukaryotic microtubule structure incompatible with a Sec-exported bacterial enzyme; (B) apicoplast exists only in apicomplexans and requires a distinct transit peptide; (C) early endosome membrane is a eukaryotic vesicular compartment requiring eukaryotic sorting signals. The Sec signal peptide and bacterial protein character point directly to (D) plasma membrane as the only compartment consistent with the sequence features.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can identify the Sec signal peptide from the hydrophobic N-terminal stretch, recognize the absence of eukaryotic targeting features, and infer bacterial plasma membrane association. This is a standard sequence-feature-to-localization inference taught in biochemistry and does not require recalling the specific UniProt annotation for OXA-48."
  },
  "case_id": "GO_cellular_component_0048",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H6",
      "C4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry for this sequence (Q6XEC0, Beta-lactamase OXA-48 from Klebsiella pneumoniae) carries the GO annotation GO:0005886 (plasma membrane), matching option D. The evidence code is IEA:TreeGrafter (computational inference by phylogenetic tree grafting), not direct experimental localization. However, the annotation is consistent with the protein's biology: it is a Sec-exported bacterial enzyme (precursor with N-terminal signal peptide) in a Gram-negative organism, and GO:0005886 includes 'cytoplasmic membrane' as an EXACT synonym for the bacterial inner membrane. The annotation is the recorded database fact and is biologically plausible for a membrane-adjacent beta-lactamase, though the evidence level is computational rather than experimental."
  },
  "important_caveats": [
    "The GO annotation is IEA:TreeGrafter (computational phylogenetic inference), not experimental localization. The actual subcellular distribution of OXA-48 in Gram-negative bacteria may be periplasmic rather than tightly membrane-associated, but periplasm is not among the options.",
    "The protein is flagged as 'Precursor' in UniProt, confirming the signal peptide; the mature protein after signal peptide cleavage would reside on the periplasmic face of the inner membrane or in the periplasm.",
    "GO:0005886 in bacterial context is equivalent to the inner/cytoplasmic membrane, making 'plasma membrane' the correct GO term for the membrane the Sec machinery crosses.",
    "The reviewer-only evidence identifies the organism (K. pneumoniae) and protein name (OXA-48); the evaluated model only sees the raw sequence and must infer bacterial origin from sequence features alone."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors (spindle, apicoplast, early endosome membrane) are all eukaryotic compartments with no plausible connection to a small Sec-exported bacterial enzyme. Only plasma membrane is compatible with the identified sequence features. No alternative option is defensible given the signal peptide and bacterial protein character."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0048",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry for this sequence (Q6XEC0, Beta-lactamase OXA-48 from Klebsiella pneumoniae) carries the GO annotation GO:0005886 (plasma membrane), matching option D. The evidence code is IEA:TreeGrafter (computational inference by phylogenetic tree grafting), not direct experimental localization. However, the annotation is consistent with the protein's biology: it is a Sec-exported bacterial enzyme (precursor with N-terminal signal peptide) in a Gram-negative organism, and GO:0005886 includes 'cytoplasmic membrane' as an EXACT synonym for the bacterial inner membrane. The annotation is the recorded database fact and is biologically plausible for a membrane-adjacent beta-lactamase, though the evidence level is computational rather than experimental.",
    "evidence_ids": ["C5", "H6", "C4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal sequence MRVLALSAVFLVASIIGMPAV is a classic Sec-type signal peptide (positively charged N-region, ~18-residue hydrophobic H-region, polar C-region with cleavage site). This is a highly transferable feature: Sec signal peptides direct proteins across the inner (plasma) membrane in bacteria. The protein is small (265 aa), lacks any eukaryotic targeting motifs (no nuclear localization signal, no apicoplast transit peptide with its characteristic arginine-rich/serine-rich pattern, no endosomal sorting signals), and its overall composition and motif architecture (SXXK, SDN, KTG-like motifs visible in the mature region) are consistent with a bacterial serine beta-lactamase. Among the four options: (A) spindle is a eukaryotic microtubule structure incompatible with a Sec-exported bacterial enzyme; (B) apicoplast exists only in apicomplexans and requires a distinct transit peptide; (C) early endosome membrane is a eukaryotic vesicular compartment requiring eukaryotic sorting signals. The Sec signal peptide and bacterial protein character point directly to (D) plasma membrane as the only compartment consistent with the sequence features.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can identify the Sec signal peptide from the hydrophobic N-terminal stretch, recognize the absence of eukaryotic targeting features, and infer bacterial plasma membrane association. This is a standard sequence-feature-to-localization inference taught in biochemistry and does not require recalling the specific UniProt annotation for OXA-48."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors (spindle, apicoplast, early endosome membrane) are all eukaryotic compartments with no plausible connection to a small Sec-exported bacterial enzyme. Only plasma membrane is compatible with the identified sequence features. No alternative option is defensible given the signal peptide and bacterial protein character."
  },
  "important_caveats": [
    "The GO annotation is IEA:TreeGrafter (computational phylogenetic inference), not experimental localization. The actual subcellular distribution of OXA-48 in Gram-negative bacteria may be periplasmic rather than tightly membrane-associated, but periplasm is not among the options.",
    "The protein is flagged as 'Precursor' in UniProt, confirming the signal peptide; the mature protein after signal peptide cleavage would reside on the periplasmic face of the inner membrane or in the periplasm.",
    "GO:0005886 in bacterial context is equivalent to the inner/cytoplasmic membrane, making 'plasma membrane' the correct GO term for the membrane the Sec machinery crosses.",
    "The reviewer-only evidence identifies the organism (K. pneumoniae) and protein name (OXA-48); the evaluated model only sees the raw sequence and must infer bacterial origin from sequence features alone."
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
  "benchmark_sequence_length": 265,
  "benchmark_sequence_sha256": "a6ed28bc8365296b7c98865c19ee2bc0a71c741056ededd224a4d8600d3057ba",
  "current_entry_audit": {
    "entryVersion": 138,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2004-07-05",
    "sequenceVersion": 1
  },
  "current_record_sha256": "7a7b0d77f1f923e008e8fc5048255b02d3f9e2d1a0d4b680f7c01328fb477d33",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 265,
  "current_source_sequence_sha256": "a6ed28bc8365296b7c98865c19ee2bc0a71c741056ededd224a4d8600d3057ba",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 136,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q6XEC0",
  "selected_historical_entry_version": 136,
  "selected_historical_record_sha256": "748d62da6dbda55945d3952c2004e283e2a5bc809be9fd394e2b1d0eff688b3a",
  "selected_historical_source_sequence_length": 265,
  "selected_historical_source_sequence_sha256": "a6ed28bc8365296b7c98865c19ee2bc0a71c741056ededd224a4d8600d3057ba",
  "selected_historical_version": {
    "accession": "Q6XEC0",
    "database": "Swiss-Prot",
    "entryVersion": 136,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "BLO48_KLEPN",
    "sequenceVersion": 1
  }
}
```

**Qualifications:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6XEC0.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q6XEC0\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:31:45.821901+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7a7b0d77f1f923e008e8fc5048255b02d3f9e2d1a0d4b680f7c01328fb477d33",
  "url": "https://rest.uniprot.org/uniprotkb/Q6XEC0.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6XEC0.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":138,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2004-07-05\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:31:45.821901+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7a7b0d77f1f923e008e8fc5048255b02d3f9e2d1a0d4b680f7c01328fb477d33",
  "url": "https://rest.uniprot.org/uniprotkb/Q6XEC0.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6XEC0.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"AAP70012.1\",\"source\":\"EMBL\"}],\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Pseudomonadota\",\"Gammaproteobacteria\",\"Enterobacterales\",\"Enterobacteriaceae\",\"Klebsiella\",\"Klebsiella pneumoniae complex\"],\"scientificName\":\"Klebsiella pneumoniae\",\"taxonId\":573}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:31:45.821901+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7a7b0d77f1f923e008e8fc5048255b02d3f9e2d1a0d4b680f7c01328fb477d33",
  "url": "https://rest.uniprot.org/uniprotkb/Q6XEC0.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6XEC0.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"RU361140\",\"source\":\"RuleBase\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"14693513\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"19477418\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"27073009\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38161376\",\"source\":\"PubMed\"}],\"value\":\"3.5.2.6\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"RU361140\",\"source\":\"RuleBase\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"14693513\",\"source\":\"PubMed\"}],\"value\":\"Beta-lactamase OXA-48\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:31:45.821901+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7a7b0d77f1f923e008e8fc5048255b02d3f9e2d1a0d4b680f7c01328fb477d33",
  "url": "https://rest.uniprot.org/uniprotkb/Q6XEC0.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6XEC0.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0005886\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:plasma membrane\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:TreeGrafter\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/257",
  "retrieved_utc": "2026-11-02T04:31:45.821901+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7a7b0d77f1f923e008e8fc5048255b02d3f9e2d1a0d4b680f7c01328fb477d33",
  "url": "https://rest.uniprot.org/uniprotkb/Q6XEC0.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6XEC0.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Poirel L.\",\"Heritier C.\",\"Tolun V.\",\"Nordmann P.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"14693513\"},{\"database\":\"DOI\",\"id\":\"10.1128/aac.48.1.15-22.2004\"}],\"citationType\":\"journal article\",\"firstPage\":\"15\",\"id\":\"14693513\",\"journal\":\"Antimicrob. Agents Chemother.\",\"lastPage\":\"22\",\"publicationDate\":\"2004\",\"title\":\"Emergence of oxacillinase-mediated resistance to imipenem in Klebsiella pneumoniae.\",\"volume\":\"48\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"AAP70012.1\",\"source\":\"EMBL\"}],\"referenceComments\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"AAP70012.1\",\"source\":\"EMBL\"}],\"type\":\"STRAIN\",\"value\":\"11978\"}],\"referenceNumber\":4,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"ACTIVITY REGULATION\",\"INDUCTION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-02T04:31:45.821901+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7a7b0d77f1f923e008e8fc5048255b02d3f9e2d1a0d4b680f7c01328fb477d33",
  "url": "https://rest.uniprot.org/uniprotkb/Q6XEC0.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6XEC0.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Docquier J.D.\",\"Calderone V.\",\"De Luca F.\",\"Benvenuti M.\",\"Giuliani F.\",\"Bellucci L.\",\"Tafi A.\",\"Nordmann P.\",\"Botta M.\",\"Rossolini G.M.\",\"Mangani S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"19477418\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.chembiol.2009.04.010\"}],\"citationType\":\"journal article\",\"firstPage\":\"540\",\"id\":\"19477418\",\"journal\":\"Chem. Biol.\",\"lastPage\":\"547\",\"publicationDate\":\"2009\",\"title\":\"Crystal structure of the OXA-48 beta-lactamase reveals mechanistic diversity among class D carbapenemases.\",\"volume\":\"16\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"3HBR\",\"source\":\"PDB\"}],\"referenceNumber\":12,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (1.90 ANGSTROMS)\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"CARBOXYLATION AT LYS-73\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/11",
  "retrieved_utc": "2026-11-02T04:31:45.821901+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7a7b0d77f1f923e008e8fc5048255b02d3f9e2d1a0d4b680f7c01328fb477d33",
  "url": "https://rest.uniprot.org/uniprotkb/Q6XEC0.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6XEC0.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Stojanoski V.\",\"Adamski C.J.\",\"Hu L.\",\"Mehta S.C.\",\"Sankaran B.\",\"Zwart P.\",\"Prasad B.V.\",\"Palzkill T.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"27073009\"},{\"database\":\"DOI\",\"id\":\"10.1021/acs.biochem.6b00056\"}],\"citationType\":\"journal article\",\"firstPage\":\"2479\",\"id\":\"27073009\",\"journal\":\"Biochemistry\",\"lastPage\":\"2490\",\"publicationDate\":\"2016\",\"title\":\"Removal of the Side Chain at the Active-Site Serine by a Glycine Substitution Increases the Stability of a Wide Range of Serine beta-Lactamases by Relieving Steric Strain.\",\"volume\":\"55\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"5HAP\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"5HAQ\",\"source\":\"PDB\"}],\"referenceNumber\":15,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (1.89 ANGSTROMS) OF 25-265 OF MUTANTS ALA-70 AND GLY-70\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"MUTAGENESIS OF SER-70\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/14",
  "retrieved_utc": "2026-11-02T04:31:45.821901+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7a7b0d77f1f923e008e8fc5048255b02d3f9e2d1a0d4b680f7c01328fb477d33",
  "url": "https://rest.uniprot.org/uniprotkb/Q6XEC0.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6XEC0.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"citation\":{\"authors\":[\"Zhou Q.\",\"Catalan P.\",\"Bell H.\",\"Baumann P.\",\"Cooke R.\",\"Evans R.\",\"Yang J.\",\"Zhang Z.\",\"Zappala D.\",\"Zhang Y.\",\"Blackburn G.M.\",\"He Y.\",\"Jin Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38161376\"},{\"database\":\"DOI\",\"id\":\"10.1021/acscentsci.3c00609\"}],\"citationType\":\"journal article\",\"firstPage\":\"2339\",\"id\":\"38161376\",\"journal\":\"ACS Cent. Sci.\",\"lastPage\":\"2349\",\"publicationDate\":\"2023\",\"title\":\"An Ion-Pair Induced Intermediate Complex Captured in Class D Carbapenemase Reveals Chloride Ion as a Janus Effector Modulating Activity.\",\"volume\":\"9\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7O5N\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7O9N\",\"source\":\"PDB\"}],\"referenceNumber\":20,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (1.53 ANGSTROMS) OF 23-265 IN APO FORM AND IN COMPLEXES WITH IMIPENEM INHIBITOR AND CHLORIDE; BROMIDE; IODIDE; BICARBONATE AND OF MUTANTS ALA-185/ALA-186/ALA-206 AND ALA-250 IN COMPLEXES WITH CHLORIDE AND BROMIDE\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"ACTIVITY REGULATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/19",
  "retrieved_utc": "2026-11-02T04:31:45.821901+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7a7b0d77f1f923e008e8fc5048255b02d3f9e2d1a0d4b680f7c01328fb477d33",
  "url": "https://rest.uniprot.org/uniprotkb/Q6XEC0.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6XEC0?format=txt&versions=136)

```json
{
  "entry_version": 136,
  "evidence_id": "H1",
  "excerpt": "ID   BLO48_KLEPN             Reviewed;         265 AA.\nAC   Q6XEC0;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-JUL-2004, sequence version 1.\nDT   28-JAN-2026, entry version 136.\nDE   RecName: Full=Beta-lactamase OXA-48 {ECO:0000255|RuleBase:RU361140, ECO:0000303|PubMed:14693513};\nDE            EC=3.5.2.6 {ECO:0000255|RuleBase:RU361140, ECO:0000269|PubMed:14693513, ECO:0000269|PubMed:19477418, ECO:0000269|PubMed:27073009, ECO:0000269|PubMed:38161376};\nDE   Flags: Precursor;\nGN   Name=OXA-48 {ECO:0000303|PubMed:14693513};\nGN   Synonyms=bla OXA-48 {ECO:0000312|EMBL:AAP70012.1},\nGN   bla_4 {ECO:0000312|EMBL:SWV87943.1},\nGN   blaOXA-48 {ECO:0000303|PubMed:14693513, ECO:0000312|EMBL:AEV46197.1};\nGN   ORFNames=KPE71T_00045 {ECO:0000312|EMBL:AGW25497.1},\nGN   SAMEA3727706_05517 {ECO:0000312|EMBL:SWV87943.1};\nOS   Klebsiella pneumoniae.\nOG   Plasmid pJEG011 {ECO:0000312|EMBL:AGJ73905.1},\nOG   Plasmid pKP112 {ECO:0000312|EMBL:CRN12897.1},\nOG   Plasmid pKPoxa-48N1 {ECO:0000312|EMBL:AGL12970.1},\nOG   Plasmid pKPoxa-48N2 {ECO:0000312|EMBL:AGL13044.1},\nOG   Plasmid pKpn-E1.Nr7 {ECO:0000312|EMBL:AKA86737.1},\nOG   Plasmid pOXA-48 {ECO:0000312|EMBL:AEV46197.1},\nOG   Plasmid pOXA-48E1 {ECO:0000312|EMBL:AKJ18670.1},\nOG   Plasmid unnamed {ECO:0000312|EMBL:AGW25497.1}, and\nOG   Plasmid P1 {ECO:0000312|EMBL:CAH5611484.1}.\nOC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria;\nOC   Enterobacterales; Enterobacteriaceae; Klebsiella/Raoultella group;\nOC   Klebsiella; Klebsiella pneumoniae complex.\nOX   NCBI_TaxID=573 {ECO:0000312|EMBL:AAP70012.1};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:51.921802+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-28",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "748d62da6dbda55945d3952c2004e283e2a5bc809be9fd394e2b1d0eff688b3a",
  "url": "https://rest.uniprot.org/unisave/Q6XEC0?format=txt&versions=136"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6XEC0?format=txt&versions=136)

```json
{
  "entry_version": 136,
  "evidence_id": "H2",
  "excerpt": "RN   [4] {ECO:0000312|EMBL:AAP70012.1}\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, CATALYTIC ACTIVITY,\nRP   BIOPHYSICOCHEMICAL PROPERTIES, ACTIVITY REGULATION, AND INDUCTION.\nRC   STRAIN=11978 {ECO:0000312|EMBL:AAP70012.1};\nRX   PubMed=14693513; DOI=10.1128/aac.48.1.15-22.2004;\nRA   Poirel L., Heritier C., Tolun V., Nordmann P.;\nRT   \"Emergence of oxacillinase-mediated resistance to imipenem in Klebsiella\nRT   pneumoniae.\";\nRL   Antimicrob. Agents Chemother. 48:15-22(2004).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:51.921802+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 51-59",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "748d62da6dbda55945d3952c2004e283e2a5bc809be9fd394e2b1d0eff688b3a",
  "url": "https://rest.uniprot.org/unisave/Q6XEC0?format=txt&versions=136"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6XEC0?format=txt&versions=136)

```json
{
  "entry_version": 136,
  "evidence_id": "H3",
  "excerpt": "RN   [12] {ECO:0007744|PDB:3HBR}\nRP   X-RAY CRYSTALLOGRAPHY (1.90 ANGSTROMS), FUNCTION, CATALYTIC ACTIVITY,\nRP   BIOPHYSICOCHEMICAL PROPERTIES, AND CARBOXYLATION AT LYS-73.\nRX   PubMed=19477418; DOI=10.1016/j.chembiol.2009.04.010;\nRA   Docquier J.D., Calderone V., De Luca F., Benvenuti M., Giuliani F.,\nRA   Bellucci L., Tafi A., Nordmann P., Botta M., Rossolini G.M., Mangani S.;\nRT   \"Crystal structure of the OXA-48 beta-lactamase reveals mechanistic\nRT   diversity among class D carbapenemases.\";\nRL   Chem. Biol. 16:540-547(2009).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:51.921802+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 123-131",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "748d62da6dbda55945d3952c2004e283e2a5bc809be9fd394e2b1d0eff688b3a",
  "url": "https://rest.uniprot.org/unisave/Q6XEC0?format=txt&versions=136"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6XEC0?format=txt&versions=136)

```json
{
  "entry_version": 136,
  "evidence_id": "H4",
  "excerpt": "RN   [15] {ECO:0007744|PDB:5HAP, ECO:0007744|PDB:5HAQ}\nRP   X-RAY CRYSTALLOGRAPHY (1.89 ANGSTROMS) OF 25-265 OF MUTANTS ALA-70 AND\nRP   GLY-70, FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, AND\nRP   MUTAGENESIS OF SER-70.\nRX   PubMed=27073009; DOI=10.1021/acs.biochem.6b00056;\nRA   Stojanoski V., Adamski C.J., Hu L., Mehta S.C., Sankaran B., Zwart P.,\nRA   Prasad B.V., Palzkill T.;\nRT   \"Removal of the Side Chain at the Active-Site Serine by a Glycine\nRT   Substitution Increases the Stability of a Wide Range of Serine beta-\nRT   Lactamases by Relieving Steric Strain.\";\nRL   Biochemistry 55:2479-2490(2016).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:51.921802+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 153-163",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "748d62da6dbda55945d3952c2004e283e2a5bc809be9fd394e2b1d0eff688b3a",
  "url": "https://rest.uniprot.org/unisave/Q6XEC0?format=txt&versions=136"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6XEC0?format=txt&versions=136)

```json
{
  "entry_version": 136,
  "evidence_id": "H5",
  "excerpt": "RN   [20] {ECO:0007744|PDB:7O5N, ECO:0007744|PDB:7O9N}\nRP   X-RAY CRYSTALLOGRAPHY (1.53 ANGSTROMS) OF 23-265 IN APO FORM AND IN\nRP   COMPLEXES WITH IMIPENEM INHIBITOR AND CHLORIDE; BROMIDE; IODIDE;\nRP   BICARBONATE AND OF MUTANTS ALA-185/ALA-186/ALA-206 AND ALA-250 IN COMPLEXES\nRP   WITH CHLORIDE AND BROMIDE, FUNCTION, CATALYTIC ACTIVITY, AND ACTIVITY\nRP   REGULATION.\nRX   PubMed=38161376; DOI=10.1021/acscentsci.3c00609;\nRA   Zhou Q., Catalan P., Bell H., Baumann P., Cooke R., Evans R., Yang J.,\nRA   Zhang Z., Zappala D., Zhang Y., Blackburn G.M., He Y., Jin Y.;\nRT   \"An Ion-Pair Induced Intermediate Complex Captured in Class D Carbapenemase\nRT   Reveals Chloride Ion as a Janus Effector Modulating Activity.\";\nRL   ACS Cent. Sci. 9:2339-2349(2023).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:51.921802+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 199-210",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "748d62da6dbda55945d3952c2004e283e2a5bc809be9fd394e2b1d0eff688b3a",
  "url": "https://rest.uniprot.org/unisave/Q6XEC0?format=txt&versions=136"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6XEC0?format=txt&versions=136)

```json
{
  "entry_version": 136,
  "evidence_id": "H6",
  "excerpt": "DR   GO; GO:0005886; C:plasma membrane; IEA:TreeGrafter.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:51.921802+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 588-588",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "748d62da6dbda55945d3952c2004e283e2a5bc809be9fd394e2b1d0eff688b3a",
  "url": "https://rest.uniprot.org/unisave/Q6XEC0?format=txt&versions=136"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0005819\nname: spindle\nnamespace: cellular_component\ndef: \"The array of microtubules and associated molecules that forms between opposite poles of a eukaryotic cell during mitosis or meiosis and serves to move the duplicated chromosomes apart.\" [ISBN:0198547684]\nxref: Wikipedia:Spindle_apparatus\nis_a: GO:0043232 ! intracellular membraneless organelle\nrelationship: part_of GO:0015630 ! microtubule cytoskeleton\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005819",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 59855-59863",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO2",
  "excerpt": "[Term]\nid: GO:0005886\nname: plasma membrane\nnamespace: cellular_component\nalt_id: GO:0005887\nalt_id: GO:0005904\ndef: \"The membrane surrounding a cell that separates the cell from its external environment. It consists of a phospholipid bilayer and associated proteins.\" [ISBN:0716731363]\nsubset: goslim_agr\nsubset: goslim_candida\nsubset: goslim_chembl\nsubset: goslim_drosophila\nsubset: goslim_euk_cellular_processes_ribbon\nsubset: goslim_generic\nsubset: goslim_metagenomics\nsubset: goslim_mouse\nsubset: goslim_plant\nsubset: goslim_plant_ribbon\nsubset: goslim_prokaryote\nsubset: goslim_prokaryote_ribbon\nsubset: goslim_yeast\nsynonym: \"bacterial inner membrane\" NARROW []\nsynonym: \"cell membrane\" EXACT []\nsynonym: \"cellular membrane\" EXACT [NIF_Subcellular:sao6433132645]\nsynonym: \"cytoplasmic membrane\" EXACT []\nsynonym: \"inner endospore membrane\" NARROW []\nsynonym: \"integral component of plasma membrane\" NARROW []\nsynonym: \"integral to plasma membrane\" NARROW []\nsynonym: \"juxtamembrane\" BROAD []\nsynonym: \"plasma membrane lipid bilayer\" NARROW [GOC:mah]\nsynonym: \"plasmalemma\" EXACT []\nxref: NIF_Subcellular:sao1663586795\nxref: Wikipedia:Cell_membrane\nis_a: GO:0016020 ! membrane\nrelationship: part_of GO:0071944 ! cell periphery\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005886",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 60420-60454",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO3",
  "excerpt": "[Term]\nid: GO:0020011\nname: apicoplast\nnamespace: cellular_component\ndef: \"The plastid organelle found in apicomplexans.\" [ISBN:0521664470]\nxref: Wikipedia:Apicoplast\nis_a: GO:0009536 ! plastid\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0020011",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 155210-155217",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO4

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO4",
  "excerpt": "[Term]\nid: GO:0031901\nname: early endosome membrane\nnamespace: cellular_component\ndef: \"The lipid bilayer surrounding an early endosome.\" [GOC:pz]\nis_a: GO:0010008 ! endosome membrane\nrelationship: part_of GO:0005769 ! early endosome\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0031901",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 180777-180784",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 48. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
