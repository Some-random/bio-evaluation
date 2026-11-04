# catalytic_activity_0053

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/catalytic_activity_0053.txt)

**Task:** `catalytic_activity`  
**Expected answer:** **B** — (7,8-dihydropterin-6-yl)methyl diphosphate + 4-aminobenzoate = 7,8-dihydropteroate + diphosphate

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MSKIFGIVNITTDSFSDGGLYLDTDKAIEHALHLVEDGADVIDLGAASSNPDTTEVGVVEEIKRLKPVIKALKEKGISISVDTFKPEVQSFCIEQKVDFINDIQGFPYPEIYSGLAKSDCKLVLMHSVQRIGAATKVETNPEEVFTSMMEFFKERIAALVEAGVKRERIILDPGMGFFLGSNPETSILVLKRFPEIQEAFNLQVMIAVSRKSFLGKITGTDVKSRLAPTLAAEMYAYKKGADYLRTHDVKSLSDALKISKALG

[Multiple Choices]
A. lipid A (E. coli) + a 1,2-diacyl-sn-glycero-3-phosphoethanolamine + H(+) = lipid A 4'-(2-aminoethyl diphosphate) (E. coli) + a 1,2-diacyl-sn-glycerol
B. (7,8-dihydropterin-6-yl)methyl diphosphate + 4-aminobenzoate = 7,8-dihydropteroate + diphosphate
C. (2R)-1,2-dihydrovomilenine + NADP(+) = vomilenine + NADPH + H(+)
D. (S)-norprotosinomenine + S-adenosyl-L-methionine = (S)-6-O-methylnorprotosinomenine + S-adenosyl-L-homocysteine + H(+)
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzymatic Reaction Prediction, which is to identify the specific chemical reaction catalyzed by a given enzyme. This involves understanding the enzyme's function based on its amino acid sequence and then selecting the correct transformation of substrates into products from a list of possible reactions.. The inputs provided by the user for this task include:

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

> The sequence matches the reviewed record whose catalytic-activity annotation gives the reaction in option B. That annotation cites experimental evidence (ECO:0000269); this supports the key, though the cited paper was not independently reviewed here.

Citations as saved: [C5](#evidence-c5), [C1](#evidence-c1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 263-residue sequence is consistent with a compact soluble bacterial dihydropteroate synthase (DHPS) family enzyme, whose conserved family-level function is the folate-pathway condensation represented by B. The other choices imply a lipid A-modifying activity, a distinct NADP-dependent alkaloid transformation, or an O-methyltransferase reaction; these are different enzyme families, and A in particular is not a good fit to this compact soluble sequence. This is a family-based inference from the sequence and transferable knowledge, not a claim of experimental proof.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A recognizable enzyme-family inference meaningfully distinguishes B among the offered reactions; recalling the exact protein's database annotation is not necessary.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The options describe distinct enzyme families and transformations; the sequence supports the DHPS reaction rather than leaving multiple choices comparably defensible.


### Important caveats

- The sequence-based family assignment is an inference; the reviewer-only annotation supplies the direct catalytic-activity evidence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 263-residue sequence is consistent with a compact soluble bacterial dihydropteroate synthase (DHPS) family enzyme, whose conserved family-level function is the folate-pathway condensation represented by B. The other choices imply a lipid A-modifying activity, a distinct NADP-dependent alkaloid transformation, or an O-methyltransferase reaction; these are different enzyme families, and A in particular is not a good fit to this compact soluble sequence. This is a family-based inference from the sequence and transferable knowledge, not a claim of experimental proof.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A recognizable enzyme-family inference meaningfully distinguishes B among the offered reactions; recalling the exact protein's database annotation is not necessary."
  },
  "case_id": "catalytic_activity_0053",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C1"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the reviewed record whose catalytic-activity annotation gives the reaction in option B. That annotation cites experimental evidence (ECO:0000269); this supports the key, though the cited paper was not independently reviewed here."
  },
  "important_caveats": [
    "The sequence-based family assignment is an inference; the reviewer-only annotation supplies the direct catalytic-activity evidence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options describe distinct enzyme families and transformations; the sequence supports the DHPS reaction rather than leaving multiple choices comparably defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0053",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the reviewed record whose catalytic-activity annotation gives the reaction in option B. That annotation cites experimental evidence (ECO:0000269); this supports the key, though the cited paper was not independently reviewed here.",
    "evidence_ids": ["C5", "C1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 263-residue sequence is consistent with a compact soluble bacterial dihydropteroate synthase (DHPS) family enzyme, whose conserved family-level function is the folate-pathway condensation represented by B. The other choices imply a lipid A-modifying activity, a distinct NADP-dependent alkaloid transformation, or an O-methyltransferase reaction; these are different enzyme families, and A in particular is not a good fit to this compact soluble sequence. This is a family-based inference from the sequence and transferable knowledge, not a claim of experimental proof.",
    "missing_item_specific_fact": "",
    "reason": "A recognizable enzyme-family inference meaningfully distinguishes B among the offered reactions; recalling the exact protein's database annotation is not necessary."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options describe distinct enzyme families and transformations; the sequence supports the DHPS reaction rather than leaving multiple choices comparably defensible."
  },
  "important_caveats": [
    "The sequence-based family assignment is an inference; the reviewer-only annotation supplies the direct catalytic-activity evidence."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry C0HMD9 annotates this protein as Dihydropteroate synthase type-3 (EC 2.5.1.15) with the exact catalytic reaction stated in choice B. The annotation carries ECO:0000269 (experimental evidence) from PubMed:37419898 (Venkatesan et al., Nat. Commun. 2023), supported by X-ray crystallography in apo form and in complexes with Mg2+ and substrates (PDB: 7S2L, 7S2M, 8SCD). The sequence in the benchmark matches the source entry exactly (263 aa, SHA256 confirmed).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 263-aa sequence contains the conserved 'DPGM' motif (positions ~178-181: 'ERIILDPGMGFFLGSNPETSILVLKRFPEIQEAFNLQVMIAVSRKSFLGKITGTDVKSRLAPTLAAEMYAYKKGADYLRTHDVKSLSDALKISKALG'), a well-known family-level signature of dihydropteroate synthase (DHPS/FolP superfamily) involved in pterin binding. The sequence length (263 aa) is consistent with DHPS (E. coli FolP is also 263 aa) but far too short for a cytochrome P450 (typically 400-600 aa with FxxGxxxCxG heme-binding motif), eliminating choice C. No recognizable SAM-binding motifs (e.g., VLDIGCGT, GxGxG patterns typical of O-methyltransferases) are present, arguing against choice D. No lipid A acyltransferase motifs or membrane-anchoring features typical of LpxM-type enzymes are evident, arguing against choice A. The sul-type sulfonamide resistance proteins (Sul1, Sul2, Sul3) are a well-characterized plasmid-encoded DHPS family in antibiotic resistance literature; all DHPS variants catalyze the same reaction: pterin diphosphate + pABA → dihydropteroate + PPi (choice B). Thus, family-level recognition of the DPGM motif, appropriate chain length, and absence of motifs diagnostic of the other enzyme classes meaningfully distinguishes choice B.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can identify the DHPS family from the conserved DPGM motif, the 263-aa chain length matching the FolP/DHPS superfamily, and the absence of diagnostic motifs for P450s, SAM-methyltransferases, or lipid A acyltransferases. All DHPS variants (chromosomal FolP and plasmid Sul1/2/3) catalyze the same reaction, so family-level inference suffices to select B without needing the exact accession or gene name.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices represent distinct enzyme classes (lipid A acyltransferase, DHPS, cytochrome P450, O-methyltransferase) with clearly different sequence-length and motif requirements. The DPGM motif and 263-aa length uniquely point to DHPS among the offered alternatives.


### Important caveats

- The DPGM motif is a family-level DHPS signature but not absolutely exclusive; however, combined with chain length and absence of competing motifs, it provides a strong and defensible inference.
- The sul3 gene product is a plasmid-encoded DHPS variant; recognizing it as specifically 'Sul3' vs. 'FolP' is not required since all DHPS variants share the same catalytic reaction.
- The experimental evidence (X-ray structures with substrates) confirms the annotation but was not available to the evaluated model; the model must rely on sequence-based family recognition.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 263-aa sequence contains the conserved 'DPGM' motif (positions ~178-181: 'ERIILDPGMGFFLGSNPETSILVLKRFPEIQEAFNLQVMIAVSRKSFLGKITGTDVKSRLAPTLAAEMYAYKKGADYLRTHDVKSLSDALKISKALG'), a well-known family-level signature of dihydropteroate synthase (DHPS/FolP superfamily) involved in pterin binding. The sequence length (263 aa) is consistent with DHPS (E. coli FolP is also 263 aa) but far too short for a cytochrome P450 (typically 400-600 aa with FxxGxxxCxG heme-binding motif), eliminating choice C. No recognizable SAM-binding motifs (e.g., VLDIGCGT, GxGxG patterns typical of O-methyltransferases) are present, arguing against choice D. No lipid A acyltransferase motifs or membrane-anchoring features typical of LpxM-type enzymes are evident, arguing against choice A. The sul-type sulfonamide resistance proteins (Sul1, Sul2, Sul3) are a well-characterized plasmid-encoded DHPS family in antibiotic resistance literature; all DHPS variants catalyze the same reaction: pterin diphosphate + pABA → dihydropteroate + PPi (choice B). Thus, family-level recognition of the DPGM motif, appropriate chain length, and absence of motifs diagnostic of the other enzyme classes meaningfully distinguishes choice B.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can identify the DHPS family from the conserved DPGM motif, the 263-aa chain length matching the FolP/DHPS superfamily, and the absence of diagnostic motifs for P450s, SAM-methyltransferases, or lipid A acyltransferases. All DHPS variants (chromosomal FolP and plasmid Sul1/2/3) catalyze the same reaction, so family-level inference suffices to select B without needing the exact accession or gene name."
  },
  "case_id": "catalytic_activity_0053",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry C0HMD9 annotates this protein as Dihydropteroate synthase type-3 (EC 2.5.1.15) with the exact catalytic reaction stated in choice B. The annotation carries ECO:0000269 (experimental evidence) from PubMed:37419898 (Venkatesan et al., Nat. Commun. 2023), supported by X-ray crystallography in apo form and in complexes with Mg2+ and substrates (PDB: 7S2L, 7S2M, 8SCD). The sequence in the benchmark matches the source entry exactly (263 aa, SHA256 confirmed)."
  },
  "important_caveats": [
    "The DPGM motif is a family-level DHPS signature but not absolutely exclusive; however, combined with chain length and absence of competing motifs, it provides a strong and defensible inference.",
    "The sul3 gene product is a plasmid-encoded DHPS variant; recognizing it as specifically 'Sul3' vs. 'FolP' is not required since all DHPS variants share the same catalytic reaction.",
    "The experimental evidence (X-ray structures with substrates) confirms the annotation but was not available to the evaluated model; the model must rely on sequence-based family recognition."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent distinct enzyme classes (lipid A acyltransferase, DHPS, cytochrome P450, O-methyltransferase) with clearly different sequence-length and motif requirements. The DPGM motif and 263-aa length uniquely point to DHPS among the offered alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0053",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry C0HMD9 annotates this protein as Dihydropteroate synthase type-3 (EC 2.5.1.15) with the exact catalytic reaction stated in choice B. The annotation carries ECO:0000269 (experimental evidence) from PubMed:37419898 (Venkatesan et al., Nat. Commun. 2023), supported by X-ray crystallography in apo form and in complexes with Mg2+ and substrates (PDB: 7S2L, 7S2M, 8SCD). The sequence in the benchmark matches the source entry exactly (263 aa, SHA256 confirmed).",
    "evidence_ids": ["C4", "C5", "C6", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 263-aa sequence contains the conserved 'DPGM' motif (positions ~178-181: 'ERIILDPGMGFFLGSNPETSILVLKRFPEIQEAFNLQVMIAVSRKSFLGKITGTDVKSRLAPTLAAEMYAYKKGADYLRTHDVKSLSDALKISKALG'), a well-known family-level signature of dihydropteroate synthase (DHPS/FolP superfamily) involved in pterin binding. The sequence length (263 aa) is consistent with DHPS (E. coli FolP is also 263 aa) but far too short for a cytochrome P450 (typically 400-600 aa with FxxGxxxCxG heme-binding motif), eliminating choice C. No recognizable SAM-binding motifs (e.g., VLDIGCGT, GxGxG patterns typical of O-methyltransferases) are present, arguing against choice D. No lipid A acyltransferase motifs or membrane-anchoring features typical of LpxM-type enzymes are evident, arguing against choice A. The sul-type sulfonamide resistance proteins (Sul1, Sul2, Sul3) are a well-characterized plasmid-encoded DHPS family in antibiotic resistance literature; all DHPS variants catalyze the same reaction: pterin diphosphate + pABA → dihydropteroate + PPi (choice B). Thus, family-level recognition of the DPGM motif, appropriate chain length, and absence of motifs diagnostic of the other enzyme classes meaningfully distinguishes choice B.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can identify the DHPS family from the conserved DPGM motif, the 263-aa chain length matching the FolP/DHPS superfamily, and the absence of diagnostic motifs for P450s, SAM-methyltransferases, or lipid A acyltransferases. All DHPS variants (chromosomal FolP and plasmid Sul1/2/3) catalyze the same reaction, so family-level inference suffices to select B without needing the exact accession or gene name."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent distinct enzyme classes (lipid A acyltransferase, DHPS, cytochrome P450, O-methyltransferase) with clearly different sequence-length and motif requirements. The DPGM motif and 263-aa length uniquely point to DHPS among the offered alternatives."
  },
  "important_caveats": [
    "The DPGM motif is a family-level DHPS signature but not absolutely exclusive; however, combined with chain length and absence of competing motifs, it provides a strong and defensible inference.",
    "The sul3 gene product is a plasmid-encoded DHPS variant; recognizing it as specifically 'Sul3' vs. 'FolP' is not required since all DHPS variants share the same catalytic reaction.",
    "The experimental evidence (X-ray structures with substrates) confirms the annotation but was not available to the evaluated model; the model must rely on sequence-based family recognition."
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
  "benchmark_sequence_length": 263,
  "benchmark_sequence_sha256": "9c1e668c6f38602c788bb8303e6683a5269f3afe52684cb7a7d4ed2d2985b67a",
  "current_entry_audit": {
    "entryVersion": 4,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-06-18",
    "sequenceVersion": 1
  },
  "current_record_sha256": "ba9202b2e0fdfb687773d6b94fecc4e21695a959dd67b21c7814fcafd1f756dd",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 263,
  "current_source_sequence_sha256": "9c1e668c6f38602c788bb8303e6683a5269f3afe52684cb7a7d4ed2d2985b67a",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 2,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "C0HMD9",
  "selected_historical_entry_version": 2,
  "selected_historical_record_sha256": "471448fab7cd4dd0e76b2ade89d1ed2965f5d7c7a78add137146b1544b0047d8",
  "selected_historical_source_sequence_length": 263,
  "selected_historical_source_sequence_sha256": "9c1e668c6f38602c788bb8303e6683a5269f3afe52684cb7a7d4ed2d2985b67a",
  "selected_historical_version": {
    "accession": "C0HMD9",
    "database": "Swiss-Prot",
    "entryVersion": 2,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "DHP3_ECOLX",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C0HMD9.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"C0HMD9\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:27:26.472274+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ba9202b2e0fdfb687773d6b94fecc4e21695a959dd67b21c7814fcafd1f756dd",
  "url": "https://rest.uniprot.org/uniprotkb/C0HMD9.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C0HMD9.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":4,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-06-18\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:27:26.472274+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ba9202b2e0fdfb687773d6b94fecc4e21695a959dd67b21c7814fcafd1f756dd",
  "url": "https://rest.uniprot.org/uniprotkb/C0HMD9.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C0HMD9.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"CAD30683.1\",\"source\":\"EMBL\"}],\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Pseudomonadota\",\"Gammaproteobacteria\",\"Enterobacterales\",\"Enterobacteriaceae\",\"Escherichia\"],\"scientificName\":\"Escherichia coli\",\"taxonId\":562}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:27:26.472274+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ba9202b2e0fdfb687773d6b94fecc4e21695a959dd67b21c7814fcafd1f756dd",
  "url": "https://rest.uniprot.org/uniprotkb/C0HMD9.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C0HMD9.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P0C002\",\"source\":\"UniProtKB\"}],\"value\":\"Dihydropteroate pyrophosphorylase type III\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P0C002\",\"source\":\"UniProtKB\"}],\"value\":\"Dihydropteroate synthase type III\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"RU361205\",\"source\":\"RuleBase\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"37419898\",\"source\":\"PubMed\"}],\"value\":\"2.5.1.15\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"RU361205\",\"source\":\"RuleBase\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"37419898\",\"source\":\"PubMed\"}],\"value\":\"Dihydropteroate synthase type-3\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"RU361205\",\"source\":\"RuleBase\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"37419898\",\"source\":\"PubMed\"}],\"value\":\"DHPS\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:27:26.472274+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ba9202b2e0fdfb687773d6b94fecc4e21695a959dd67b21c7814fcafd1f756dd",
  "url": "https://rest.uniprot.org/uniprotkb/C0HMD9.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C0HMD9.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"2.5.1.15\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"37419898\",\"source\":\"PubMed\"}],\"name\":\"(7,8-dihydropterin-6-yl)methyl diphosphate + 4-aminobenzoate = 7,8-dihydropteroate + diphosphate\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:19949\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:17836\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:17839\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:33019\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:72950\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:27:26.472274+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ba9202b2e0fdfb687773d6b94fecc4e21695a959dd67b21c7814fcafd1f756dd",
  "url": "https://rest.uniprot.org/uniprotkb/C0HMD9.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C0HMD9.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Venkatesan M.\",\"Fruci M.\",\"Verellen L.A.\",\"Skarina T.\",\"Mesa N.\",\"Flick R.\",\"Pham C.\",\"Mahadevan R.\",\"Stogios P.J.\",\"Savchenko A.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"37419898\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41467-023-39778-7\"}],\"citationType\":\"journal article\",\"firstPage\":\"4031\",\"id\":\"37419898\",\"journal\":\"Nat. Commun.\",\"lastPage\":\"4031\",\"publicationDate\":\"2023\",\"title\":\"Molecular mechanism of plasmid-borne resistance to sulfonamide antibiotics.\",\"volume\":\"14\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7S2L\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7S2M\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8SCD\",\"source\":\"PDB\"}],\"referenceNumber\":2,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (2.06 ANGSTROMS) IN APO FORM AND IN COMPLEXES WITH MG(2+) AND WITH SUBSTRATES\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"MUTAGENESIS OF PHE-177 AND LEU-179\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:27:26.472274+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ba9202b2e0fdfb687773d6b94fecc4e21695a959dd67b21c7814fcafd1f756dd",
  "url": "https://rest.uniprot.org/uniprotkb/C0HMD9.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C0HMD9?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H1",
  "excerpt": "ID   DHP3_ECOLX              Reviewed;         263 AA.\nAC   C0HMD9;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   18-JUN-2025, sequence version 1.\nDT   28-JAN-2026, entry version 2.\nDE   RecName: Full=Dihydropteroate synthase type-3 {ECO:0000255|RuleBase:RU361205, ECO:0000303|PubMed:37419898};\nDE            Short=DHPS {ECO:0000255|RuleBase:RU361205, ECO:0000303|PubMed:37419898};\nDE            EC=2.5.1.15 {ECO:0000255|RuleBase:RU361205, ECO:0000269|PubMed:37419898};\nDE   AltName: Full=Dihydropteroate pyrophosphorylase type III {ECO:0000250|UniProtKB:P0C002};\nDE   AltName: Full=Dihydropteroate synthase type III {ECO:0000250|UniProtKB:P0C002};\nGN   Name=sul3 {ECO:0000303|PubMed:12604565, ECO:0000312|EMBL:CAD30683.1};\nOS   Escherichia coli.\nOG   Plasmid pVP440 {ECO:0000312|EMBL:CAD30683.1}.\nOC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria;\nOC   Enterobacterales; Enterobacteriaceae; Escherichia.\nOX   NCBI_TaxID=562 {ECO:0000312|EMBL:CAD30683.1};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:30.074117+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "471448fab7cd4dd0e76b2ade89d1ed2965f5d7c7a78add137146b1544b0047d8",
  "url": "https://rest.uniprot.org/unisave/C0HMD9?format=txt&versions=2"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C0HMD9?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Dihydropteroate synthase type-3 {ECO:0000255|RuleBase:RU361205, ECO:0000303|PubMed:37419898};\nDE            Short=DHPS {ECO:0000255|RuleBase:RU361205, ECO:0000303|PubMed:37419898};\nDE            EC=2.5.1.15 {ECO:0000255|RuleBase:RU361205, ECO:0000269|PubMed:37419898};\nDE   AltName: Full=Dihydropteroate pyrophosphorylase type III {ECO:0000250|UniProtKB:P0C002};\nDE   AltName: Full=Dihydropteroate synthase type III {ECO:0000250|UniProtKB:P0C002};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:30.074117+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-10",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "471448fab7cd4dd0e76b2ade89d1ed2965f5d7c7a78add137146b1544b0047d8",
  "url": "https://rest.uniprot.org/unisave/C0HMD9?format=txt&versions=2"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C0HMD9?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H3",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:CAD30683.1}\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], AND FUNCTION.\nRC   STRAIN=Rl0044 {ECO:0000312|EMBL:CAD30683.1};\nRC   PLASMID=pVP440 {ECO:0000312|EMBL:CAD30683.1};\nRX   PubMed=12604565; DOI=10.1128/aac.47.3.1169-1172.2003;\nRA   Perreten V., Boerlin P.;\nRT   \"A new sulfonamide resistance gene (sul3) in Escherichia coli is widespread\nRT   in the pig population of Switzerland.\";\nRL   Antimicrob. Agents Chemother. 47:1169-1172(2003).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:30.074117+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 17-25",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "471448fab7cd4dd0e76b2ade89d1ed2965f5d7c7a78add137146b1544b0047d8",
  "url": "https://rest.uniprot.org/unisave/C0HMD9?format=txt&versions=2"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C0HMD9?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H4",
  "excerpt": "RN   [2] {ECO:0007744|PDB:7S2L, ECO:0007744|PDB:7S2M, ECO:0007744|PDB:8SCD}\nRP   X-RAY CRYSTALLOGRAPHY (2.06 ANGSTROMS) IN APO FORM AND IN COMPLEXES WITH\nRP   MG(2+) AND WITH SUBSTRATES, FUNCTION, CATALYTIC ACTIVITY,\nRP   BIOPHYSICOCHEMICAL PROPERTIES, AND MUTAGENESIS OF PHE-177 AND LEU-179.\nRX   PubMed=37419898; DOI=10.1038/s41467-023-39778-7;\nRA   Venkatesan M., Fruci M., Verellen L.A., Skarina T., Mesa N., Flick R.,\nRA   Pham C., Mahadevan R., Stogios P.J., Savchenko A.;\nRT   \"Molecular mechanism of plasmid-borne resistance to sulfonamide\nRT   antibiotics.\";\nRL   Nat. Commun. 14:4031-4031(2023).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:30.074117+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 26-35",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "471448fab7cd4dd0e76b2ade89d1ed2965f5d7c7a78add137146b1544b0047d8",
  "url": "https://rest.uniprot.org/unisave/C0HMD9?format=txt&versions=2"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C0HMD9?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H5",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=(7,8-dihydropterin-6-yl)methyl diphosphate + 4-aminobenzoate =\nCC         7,8-dihydropteroate + diphosphate; Xref=Rhea:RHEA:19949,\nCC         ChEBI:CHEBI:17836, ChEBI:CHEBI:17839, ChEBI:CHEBI:33019,\nCC         ChEBI:CHEBI:72950; EC=2.5.1.15;\nCC         Evidence={ECO:0000269|PubMed:37419898};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:30.074117+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 44-49",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "471448fab7cd4dd0e76b2ade89d1ed2965f5d7c7a78add137146b1544b0047d8",
  "url": "https://rest.uniprot.org/unisave/C0HMD9?format=txt&versions=2"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 53. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
