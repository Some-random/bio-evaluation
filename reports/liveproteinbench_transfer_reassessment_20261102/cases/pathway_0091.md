# pathway_0091

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/pathway_0091.txt)

**Task:** `pathway`  
**Expected answer:** **B** — Cell wall degradation

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MLSLFNRLPWLHRVLITAFSAIIVFAIFFLPNSEDLRKPDAQREVGRHYPVTLDNQLVSTPEEEVIAPPSVMLRWETYQVANGESAALLFQRAGLSSRVLYELTSSNSDINNQLSKLMPKDELKFGFDKDNQLVQLKRTISPYETFVVTRSDSGFTSEFDKKEVTFQLNYAEAKITSNFWNAGVTAGLSANQIIELANMFGWDIDFALDIREGDQFKLLYQEKIVEGSVIGRGNIIAATFINQGSTFTAILDDNTGNYYDQNGRAMKKAFLRSPLDFRRVSSNFNPRRLHPVTGQIKAHRGTDYVAPVGTPIWAAGDGVVEKSSYNQFNGNYVYIRHSNTYITKYLHLQRRLVKTGERVKQGQTIGTLGGTGRVTGPHLHYEFLVNGIHKNPRTVELPQAQSLTGKAKETFIANAKQRMEKLERYSQLLYANQ

[Multiple Choices]
A. Lipid metabolism
B. Cell wall degradation
C. L-threonine from L-aspartate: step 2/5. .
D. Alkaloid biosynthesis. .
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Protein Pathway Prediction, which is to predict the primary metabolic or signaling pathway in which a given protein functions. Biological pathways are series of chemical reactions occurring within a cell that are essential for life. Based on the protein's amino acid sequence, you should identify the most relevant pathway from the given options.. The inputs provided by the user for this task include:

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

> The sequence-matched UniProt record names the protein as a peptidoglycan DD-endopeptidase and annotates its pathway as cell wall/peptidoglycan degradation. The pathway annotation carries an experimental evidence code, although it remains a database annotation rather than independent validation here.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a strongly hydrophobic N-terminal segment consistent with export or membrane targeting, followed by a large soluble enzyme region. Histidine-containing motifs in that region are compatible with a metallopeptidase; bacterial exported peptidoglycan hydrolases are a plausible family-level match. That pattern favors cell wall degradation (B) over the typically cytosolic threonine-biosynthesis enzyme in C or alkaloid biosynthesis in D. It is also a better fit than lipid metabolism (A), though the sequence alone does not prove substrate specificity.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable knowledge about bacterial export signals and peptidoglycan-hydrolase metallopeptidases gives a meaningful, probabilistic basis for choosing B among these alternatives. The exact-target database annotation is not necessary to make that distinction.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The export-targeting segment and enzyme-domain pattern make B the best-supported choice among the offered alternatives; no other option is comparably defensible from the supplied sequence.


### Important caveats

- The sequence-based family and substrate inference is probabilistic, not a direct demonstration of activity.
- The source annotation supports the expected answer, but the author’s exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a strongly hydrophobic N-terminal segment consistent with export or membrane targeting, followed by a large soluble enzyme region. Histidine-containing motifs in that region are compatible with a metallopeptidase; bacterial exported peptidoglycan hydrolases are a plausible family-level match. That pattern favors cell wall degradation (B) over the typically cytosolic threonine-biosynthesis enzyme in C or alkaloid biosynthesis in D. It is also a better fit than lipid metabolism (A), though the sequence alone does not prove substrate specificity.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge about bacterial export signals and peptidoglycan-hydrolase metallopeptidases gives a meaningful, probabilistic basis for choosing B among these alternatives. The exact-target database annotation is not necessary to make that distinction."
  },
  "case_id": "pathway_0091",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record names the protein as a peptidoglycan DD-endopeptidase and annotates its pathway as cell wall/peptidoglycan degradation. The pathway annotation carries an experimental evidence code, although it remains a database annotation rather than independent validation here."
  },
  "important_caveats": [
    "The sequence-based family and substrate inference is probabilistic, not a direct demonstration of activity.",
    "The source annotation supports the expected answer, but the author’s exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The export-targeting segment and enzyme-domain pattern make B the best-supported choice among the offered alternatives; no other option is comparably defensible from the supplied sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0091",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record names the protein as a peptidoglycan DD-endopeptidase and annotates its pathway as cell wall/peptidoglycan degradation. The pathway annotation carries an experimental evidence code, although it remains a database annotation rather than independent validation here.",
    "evidence_ids": ["C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a strongly hydrophobic N-terminal segment consistent with export or membrane targeting, followed by a large soluble enzyme region. Histidine-containing motifs in that region are compatible with a metallopeptidase; bacterial exported peptidoglycan hydrolases are a plausible family-level match. That pattern favors cell wall degradation (B) over the typically cytosolic threonine-biosynthesis enzyme in C or alkaloid biosynthesis in D. It is also a better fit than lipid metabolism (A), though the sequence alone does not prove substrate specificity.",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge about bacterial export signals and peptidoglycan-hydrolase metallopeptidases gives a meaningful, probabilistic basis for choosing B among these alternatives. The exact-target database annotation is not necessary to make that distinction."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The export-targeting segment and enzyme-domain pattern make B the best-supported choice among the offered alternatives; no other option is comparably defensible from the supplied sequence."
  },
  "important_caveats": [
    "The sequence-based family and substrate inference is probabilistic, not a direct demonstration of activity.",
    "The source annotation supports the expected answer, but the author’s exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q9KU93 (SHYC_VIBCH) annotates this protein as 'Peptidoglycan DD-endopeptidase ShyC' with the pathway comment 'Cell wall degradation; peptidoglycan degradation' (evidence code ECO:0000269, experimental, PubMed:30782657). The author's expected answer B ('Cell wall degradation') directly matches this annotation. The sequence matches the benchmark input (433 aa, SHA-256 confirmed). The EC number 3.4.24.- (metalloendopeptidase) and the experimental characterization of peptidoglycan cleavage activity further support the cell wall degradation pathway.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a clear N-terminal signal peptide (MLSLFNRLPWLHRVLITAFSAIIVFAIFFLPNSE~), indicating a secreted/extracellular protein. More critically, the motif 'GRGNIIAATFINQ' contains the GRGN signature that is a well-known hallmark of the M23 peptidoglycan DD-endopeptidase family, recognized across numerous bacterial autolysins (e.g., lysostaphin from Staphylococcus, various E. coli and Bacillus endopeptidases). The overall domain architecture—signal peptide + M23 peptidase core + potential peptidoglycan-binding region (the GVTAGLSANQ and downstream segments)—is the classic layout of bacterial peptidoglycan hydrolases. This family-level knowledge, learned from many other peptidoglycan-degrading enzymes, directly points to cell wall degradation (option B). The distractors are readily excluded: lipid metabolism enzymes lack GRGN-type peptidase motifs and have lipase/thioesterase folds; L-threonine biosynthesis enzymes (aspartokinase, homoserine dehydrogenase, threonine synthase) have entirely different domains; alkaloid biosynthesis is a plant/fungal secondary metabolism pathway with no relevance to a bacterial secreted peptidase.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The GRGN motif within the M23 peptidase family is a transferable, well-characterized sequence signature shared across many peptidoglycan endopeptidases in diverse bacteria. Combined with the signal peptide and peptidoglycan-binding-like regions, a knowledgeable model can confidently assign cell wall degradation without needing to look up this specific protein's record. The other three options lack any supporting sequence features.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options are biologically distinct and mutually exclusive. Only B (cell wall degradation) is consistent with the M23 peptidase signature and secreted peptidoglycan hydrolase architecture. A, C, and D have no supporting features in the sequence and belong to entirely different functional classes.


### Important caveats

- The GRGN motif is strongly associated with M23 peptidoglycan endopeptidases but could theoretically appear in other metalloproteases; however, the full domain context (signal peptide, binding region, overall size ~433 aa) narrows the assignment to peptidoglycan hydrolases.
- The UniProt pathway annotation is experimentally supported (ECO:0000269, PubMed:30782657), not merely computational, strengthening the key.
- The author's source snapshot is unknown; the historical Swiss-Prot entry (version 105, released Jan 2026) already carries the same pathway annotation, so the key was likely available at benchmark construction time.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a clear N-terminal signal peptide (MLSLFNRLPWLHRVLITAFSAIIVFAIFFLPNSE~), indicating a secreted/extracellular protein. More critically, the motif 'GRGNIIAATFINQ' contains the GRGN signature that is a well-known hallmark of the M23 peptidoglycan DD-endopeptidase family, recognized across numerous bacterial autolysins (e.g., lysostaphin from Staphylococcus, various E. coli and Bacillus endopeptidases). The overall domain architecture—signal peptide + M23 peptidase core + potential peptidoglycan-binding region (the GVTAGLSANQ and downstream segments)—is the classic layout of bacterial peptidoglycan hydrolases. This family-level knowledge, learned from many other peptidoglycan-degrading enzymes, directly points to cell wall degradation (option B). The distractors are readily excluded: lipid metabolism enzymes lack GRGN-type peptidase motifs and have lipase/thioesterase folds; L-threonine biosynthesis enzymes (aspartokinase, homoserine dehydrogenase, threonine synthase) have entirely different domains; alkaloid biosynthesis is a plant/fungal secondary metabolism pathway with no relevance to a bacterial secreted peptidase.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The GRGN motif within the M23 peptidase family is a transferable, well-characterized sequence signature shared across many peptidoglycan endopeptidases in diverse bacteria. Combined with the signal peptide and peptidoglycan-binding-like regions, a knowledgeable model can confidently assign cell wall degradation without needing to look up this specific protein's record. The other three options lack any supporting sequence features."
  },
  "case_id": "pathway_0091",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C7",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q9KU93 (SHYC_VIBCH) annotates this protein as 'Peptidoglycan DD-endopeptidase ShyC' with the pathway comment 'Cell wall degradation; peptidoglycan degradation' (evidence code ECO:0000269, experimental, PubMed:30782657). The author's expected answer B ('Cell wall degradation') directly matches this annotation. The sequence matches the benchmark input (433 aa, SHA-256 confirmed). The EC number 3.4.24.- (metalloendopeptidase) and the experimental characterization of peptidoglycan cleavage activity further support the cell wall degradation pathway."
  },
  "important_caveats": [
    "The GRGN motif is strongly associated with M23 peptidoglycan endopeptidases but could theoretically appear in other metalloproteases; however, the full domain context (signal peptide, binding region, overall size ~433 aa) narrows the assignment to peptidoglycan hydrolases.",
    "The UniProt pathway annotation is experimentally supported (ECO:0000269, PubMed:30782657), not merely computational, strengthening the key.",
    "The author's source snapshot is unknown; the historical Swiss-Prot entry (version 105, released Jan 2026) already carries the same pathway annotation, so the key was likely available at benchmark construction time."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are biologically distinct and mutually exclusive. Only B (cell wall degradation) is consistent with the M23 peptidase signature and secreted peptidoglycan hydrolase architecture. A, C, and D have no supporting features in the sequence and belong to entirely different functional classes."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0091",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q9KU93 (SHYC_VIBCH) annotates this protein as 'Peptidoglycan DD-endopeptidase ShyC' with the pathway comment 'Cell wall degradation; peptidoglycan degradation' (evidence code ECO:0000269, experimental, PubMed:30782657). The author's expected answer B ('Cell wall degradation') directly matches this annotation. The sequence matches the benchmark input (433 aa, SHA-256 confirmed). The EC number 3.4.24.- (metalloendopeptidase) and the experimental characterization of peptidoglycan cleavage activity further support the cell wall degradation pathway.",
    "evidence_ids": ["C4", "C5", "C7", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a clear N-terminal signal peptide (MLSLFNRLPWLHRVLITAFSAIIVFAIFFLPNSE~), indicating a secreted/extracellular protein. More critically, the motif 'GRGNIIAATFINQ' contains the GRGN signature that is a well-known hallmark of the M23 peptidoglycan DD-endopeptidase family, recognized across numerous bacterial autolysins (e.g., lysostaphin from Staphylococcus, various E. coli and Bacillus endopeptidases). The overall domain architecture—signal peptide + M23 peptidase core + potential peptidoglycan-binding region (the GVTAGLSANQ and downstream segments)—is the classic layout of bacterial peptidoglycan hydrolases. This family-level knowledge, learned from many other peptidoglycan-degrading enzymes, directly points to cell wall degradation (option B). The distractors are readily excluded: lipid metabolism enzymes lack GRGN-type peptidase motifs and have lipase/thioesterase folds; L-threonine biosynthesis enzymes (aspartokinase, homoserine dehydrogenase, threonine synthase) have entirely different domains; alkaloid biosynthesis is a plant/fungal secondary metabolism pathway with no relevance to a bacterial secreted peptidase.",
    "missing_item_specific_fact": "",
    "reason": "The GRGN motif within the M23 peptidase family is a transferable, well-characterized sequence signature shared across many peptidoglycan endopeptidases in diverse bacteria. Combined with the signal peptide and peptidoglycan-binding-like regions, a knowledgeable model can confidently assign cell wall degradation without needing to look up this specific protein's record. The other three options lack any supporting sequence features."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are biologically distinct and mutually exclusive. Only B (cell wall degradation) is consistent with the M23 peptidase signature and secreted peptidoglycan hydrolase architecture. A, C, and D have no supporting features in the sequence and belong to entirely different functional classes."
  },
  "important_caveats": [
    "The GRGN motif is strongly associated with M23 peptidoglycan endopeptidases but could theoretically appear in other metalloproteases; however, the full domain context (signal peptide, binding region, overall size ~433 aa) narrows the assignment to peptidoglycan hydrolases.",
    "The UniProt pathway annotation is experimentally supported (ECO:0000269, PubMed:30782657), not merely computational, strengthening the key.",
    "The author's source snapshot is unknown; the historical Swiss-Prot entry (version 105, released Jan 2026) already carries the same pathway annotation, so the key was likely available at benchmark construction time."
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
  "benchmark_sequence_length": 433,
  "benchmark_sequence_sha256": "888de842c37482558167fa97e9321ab347a672a53eb8aa7d6ae9b2562c828db3",
  "current_entry_audit": {
    "entryVersion": 107,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2000-10-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "4c68a5a19b097a0a13e179bb05c32e6e535e30c5a35f230053fa015d7637a8eb",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 433,
  "current_source_sequence_sha256": "888de842c37482558167fa97e9321ab347a672a53eb8aa7d6ae9b2562c828db3",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 105,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q9KU93",
  "selected_historical_entry_version": 105,
  "selected_historical_record_sha256": "69827fcfb90c56fef1edc54124463fb027192860af52edf1a74b01902c49973c",
  "selected_historical_source_sequence_length": 433,
  "selected_historical_source_sequence_sha256": "888de842c37482558167fa97e9321ab347a672a53eb8aa7d6ae9b2562c828db3",
  "selected_historical_version": {
    "accession": "Q9KU93",
    "database": "Swiss-Prot",
    "entryVersion": 105,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "SHYC_VIBCH",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KU93.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q9KU93\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:26.755646+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4c68a5a19b097a0a13e179bb05c32e6e535e30c5a35f230053fa015d7637a8eb",
  "url": "https://rest.uniprot.org/uniprotkb/Q9KU93.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KU93.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":107,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2000-10-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:26.755646+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4c68a5a19b097a0a13e179bb05c32e6e535e30c5a35f230053fa015d7637a8eb",
  "url": "https://rest.uniprot.org/uniprotkb/Q9KU93.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KU93.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"AAF93796.1\",\"source\":\"EMBL\"},{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000000584\",\"source\":\"Proteomes\"}],\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Pseudomonadota\",\"Gammaproteobacteria\",\"Vibrionales\",\"Vibrionaceae\",\"Vibrio\"],\"scientificName\":\"Vibrio cholerae serotype O1 (strain ATCC 39315 / El Tor Inaba N16961)\",\"taxonId\":243277}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:26.755646+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4c68a5a19b097a0a13e179bb05c32e6e535e30c5a35f230053fa015d7637a8eb",
  "url": "https://rest.uniprot.org/uniprotkb/Q9KU93.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KU93.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30782657\",\"source\":\"PubMed\"}],\"value\":\"Autolysin ShyC\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"23834664\",\"source\":\"PubMed\"}],\"value\":\"Sidewall hydrolase C\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"30782657\",\"source\":\"PubMed\"}],\"value\":\"3.4.24.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30782657\",\"source\":\"PubMed\"}],\"value\":\"Peptidoglycan DD-endopeptidase ShyC\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:26.755646+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4c68a5a19b097a0a13e179bb05c32e6e535e30c5a35f230053fa015d7637a8eb",
  "url": "https://rest.uniprot.org/uniprotkb/Q9KU93.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KU93.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"30782657\",\"source\":\"PubMed\"}],\"value\":\"Cell wall degradation; peptidoglycan degradation\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-01T06:25:26.755646+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4c68a5a19b097a0a13e179bb05c32e6e535e30c5a35f230053fa015d7637a8eb",
  "url": "https://rest.uniprot.org/uniprotkb/Q9KU93.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KU93.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Doerr T.\",\"Cava F.\",\"Lam H.\",\"Davis B.M.\",\"Waldor M.K.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"23834664\"},{\"database\":\"DOI\",\"id\":\"10.1111/mmi.12323\"}],\"citationType\":\"journal article\",\"firstPage\":\"949\",\"id\":\"23834664\",\"journal\":\"Mol. Microbiol.\",\"lastPage\":\"962\",\"publicationDate\":\"2013\",\"title\":\"Substrate specificity of an elongation-specific peptidoglycan endopeptidase and its implications for cell wall architecture and growth of Vibrio cholerae.\",\"volume\":\"89\"},\"referenceComments\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"23834664\",\"source\":\"PubMed\"}],\"type\":\"STRAIN\",\"value\":\"ATCC 39315 / El Tor Inaba N16961\"}],\"referenceNumber\":2,\"referencePositions\":[\"SUBCELLULAR LOCATION\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-01T06:25:26.755646+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4c68a5a19b097a0a13e179bb05c32e6e535e30c5a35f230053fa015d7637a8eb",
  "url": "https://rest.uniprot.org/uniprotkb/Q9KU93.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KU93.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Murphy S.G.\",\"Alvarez L.\",\"Adams M.C.\",\"Liu S.\",\"Chappie J.S.\",\"Cava F.\",\"Doerr T.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"30782657\"},{\"database\":\"DOI\",\"id\":\"10.1128/mbio.02620-18\"}],\"citationType\":\"journal article\",\"firstPage\":\"0\",\"id\":\"30782657\",\"journal\":\"MBio\",\"lastPage\":\"0\",\"publicationDate\":\"2019\",\"title\":\"Endopeptidase Regulation as a Novel Function of the Zur-Dependent Zinc Starvation Response.\",\"volume\":\"10\"},\"referenceComments\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30782657\",\"source\":\"PubMed\"}],\"type\":\"STRAIN\",\"value\":\"ATCC 39315 / El Tor Inaba N16961\"}],\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"ACTIVITY REGULATION\",\"PATHWAY\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-01T06:25:26.755646+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4c68a5a19b097a0a13e179bb05c32e6e535e30c5a35f230053fa015d7637a8eb",
  "url": "https://rest.uniprot.org/uniprotkb/Q9KU93.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9KU93?format=txt&versions=105)

```json
{
  "entry_version": 105,
  "evidence_id": "H1",
  "excerpt": "ID   SHYC_VIBCH              Reviewed;         433 AA.\nAC   Q9KU93;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-OCT-2000, sequence version 1.\nDT   28-JAN-2026, entry version 105.\nDE   RecName: Full=Peptidoglycan DD-endopeptidase ShyC {ECO:0000303|PubMed:30782657};\nDE            EC=3.4.24.- {ECO:0000269|PubMed:30782657};\nDE   AltName: Full=Autolysin ShyC {ECO:0000303|PubMed:30782657};\nDE   AltName: Full=Sidewall hydrolase C {ECO:0000303|PubMed:23834664};\nGN   Name=shyC {ECO:0000303|PubMed:23834664, ECO:0000303|PubMed:30782657};\nGN   OrderedLocusNames=VC_0630 {ECO:0000303|PubMed:23834664,\nGN   ECO:0000312|EMBL:AAF93796.1};\nOS   Vibrio cholerae serotype O1 (strain ATCC 39315 / El Tor Inaba N16961).\nOC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria; Vibrionales;\nOC   Vibrionaceae; Vibrio.\nOX   NCBI_TaxID=243277 {ECO:0000312|EMBL:AAF93796.1, ECO:0000312|Proteomes:UP000000584};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:46.934559+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "69827fcfb90c56fef1edc54124463fb027192860af52edf1a74b01902c49973c",
  "url": "https://rest.uniprot.org/unisave/Q9KU93?format=txt&versions=105"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9KU93?format=txt&versions=105)

```json
{
  "entry_version": 105,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   SUBCELLULAR LOCATION, AND DISRUPTION PHENOTYPE.\nRC   STRAIN=ATCC 39315 / El Tor Inaba N16961 {ECO:0000303|PubMed:23834664};\nRX   PubMed=23834664; DOI=10.1111/mmi.12323;\nRA   Doerr T., Cava F., Lam H., Davis B.M., Waldor M.K.;\nRT   \"Substrate specificity of an elongation-specific peptidoglycan\nRT   endopeptidase and its implications for cell wall architecture and growth of\nRT   Vibrio cholerae.\";\nRL   Mol. Microbiol. 89:949-962(2013).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:46.934559+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 31-39",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "69827fcfb90c56fef1edc54124463fb027192860af52edf1a74b01902c49973c",
  "url": "https://rest.uniprot.org/unisave/Q9KU93?format=txt&versions=105"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9KU93?format=txt&versions=105)

```json
{
  "entry_version": 105,
  "evidence_id": "H3",
  "excerpt": "RN   [3]\nRP   FUNCTION, CATALYTIC ACTIVITY, ACTIVITY REGULATION, PATHWAY, AND DISRUPTION\nRP   PHENOTYPE.\nRC   STRAIN=ATCC 39315 / El Tor Inaba N16961 {ECO:0000303|PubMed:30782657};\nRX   PubMed=30782657; DOI=10.1128/mbio.02620-18;\nRA   Murphy S.G., Alvarez L., Adams M.C., Liu S., Chappie J.S., Cava F.,\nRA   Doerr T.;\nRT   \"Endopeptidase Regulation as a Novel Function of the Zur-Dependent Zinc\nRT   Starvation Response.\";\nRL   MBio 10:0-0(2019).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:46.934559+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 40-49",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "69827fcfb90c56fef1edc54124463fb027192860af52edf1a74b01902c49973c",
  "url": "https://rest.uniprot.org/unisave/Q9KU93?format=txt&versions=105"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9KU93?format=txt&versions=105)

```json
{
  "entry_version": 105,
  "evidence_id": "H4",
  "excerpt": "CC   -!- PATHWAY: Cell wall degradation; peptidoglycan degradation.\nCC       {ECO:0000269|PubMed:30782657}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:46.934559+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 62-63",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "69827fcfb90c56fef1edc54124463fb027192860af52edf1a74b01902c49973c",
  "url": "https://rest.uniprot.org/unisave/Q9KU93?format=txt&versions=105"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 91. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
