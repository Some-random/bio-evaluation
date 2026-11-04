# EC_number_0043

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0043.txt)

**Task:** `EC_number`  
**Expected answer:** **D** — 2.3.1.193

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MTVKVRFDKEVRDYAKGEKVKDSILKLTETALAQALENFHRRMIVIEGDTLRKAELAGILAGASARVLSGILEELMKKRLRDESEDKIEVLYATDALGEETFGRKRYEAFRKHFDVLAGSNVEVKAVTFKHTRDILGRTYDLLILDMSYDYSPNDLGRIIETVRGGGLIFILAHPFEKWKNMWTGFHKSLVTPPYTIDDVKKRFNRRLIRKFTEHDGIYIITEGGKARKKPKRSKSQARIKARKGVPIPEETLFPKELYEMALTEGQVEVLKAFEELVEGGMLVLTADRGRGKSVSVGIGAIGLALALKKRTRIVVTAPELENVQALFRFAKRALERLGFKPYVVEERGLIKELYARKIGLRYYPPADGYKKSADLYILDEAAGIHVPILHKYLNKERVVYSSTIHGYEGAGRGFSVKFLKRAREKREFKELHMDEPIRYAENDPIERWLFDVLLLDAEPVELTEEDFELIEKKEVYLEEPDLDDWFENDREDLRNFVGIYILAHYRNRPSDVALLADAPHHEARVLRLKNGKIVTAIQIAKEGGIPKKVIEKMAKGYKPRGNIIPDMMVKHHYLKEFAKLKGYRIVRIATHPDAMDRGLGSKALELLEKEAREKGLDWIGSGFGASEELVRFWVRNGFAVVHLSPARNPVSGEFTAIVLKPISERAKKLIKKANDEFRIRLTEWLGDTHRELEPEIARWLFETPFGEAVDYPVHLTEIQKKRLDAFTGKVLTYDTVVDAVKPIVKLYFLDGWMKPYLDERQIRLLIYRVLQAHSWEETAKLIDRTETFTMIEVRDIIRGLWYYYKRLLKA

[Multiple Choices]
A. 2.3.1.319
B. 3.2.1.55
C. 5.3.99.13
D. 2.3.1.193
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

> The matched-sequence UniProt records assign EC 2.3.1.193 to this protein and describe acetylation of cytidine in elongator tRNA(Met). The specific EC assignment is attributed to the computational HAMAP rule; related RNA-acetylation annotations also cite a publication. This supports the key, though the supplied evidence does not independently establish direct experimental verification of the exact tRNA(Met) reaction.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 811-residue sequence is consistent with the conserved, multidomain TmcA-family RNA acetyltransferases, which combine nucleotide-dependent chemistry with an acetyltransferase function. Transferable family knowledge connects that architecture to acetylation of cytidine in tRNA and favors D, EC 2.3.1.193, over the other offered substrate-specific acetyltransferase A; the hydrolase and isomerase choices are less compatible.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level inference from the sequence can meaningfully distinguish the TmcA-associated EC choice without relying on the target's database record. The fine-grained substrate assignment is probabilistic from sequence-family recognition, not a direct demonstration of the reaction.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The options do not present another clearly equivalent EC assignment for the inferred TmcA-family activity.


### Important caveats

- The sequence matches the cited current and historical UniProt records, but the author's exact source snapshot is unknown.
- The evidence for the specific EC assignment is computational (HAMAP); the cited publication supports broader RNA acetylation annotation, not necessarily direct validation of every substrate detail shown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 811-residue sequence is consistent with the conserved, multidomain TmcA-family RNA acetyltransferases, which combine nucleotide-dependent chemistry with an acetyltransferase function. Transferable family knowledge connects that architecture to acetylation of cytidine in tRNA and favors D, EC 2.3.1.193, over the other offered substrate-specific acetyltransferase A; the hydrolase and isomerase choices are less compatible.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from the sequence can meaningfully distinguish the TmcA-associated EC choice without relying on the target's database record. The fine-grained substrate assignment is probabilistic from sequence-family recognition, not a direct demonstration of the reaction."
  },
  "case_id": "EC_number_0043",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The matched-sequence UniProt records assign EC 2.3.1.193 to this protein and describe acetylation of cytidine in elongator tRNA(Met). The specific EC assignment is attributed to the computational HAMAP rule; related RNA-acetylation annotations also cite a publication. This supports the key, though the supplied evidence does not independently establish direct experimental verification of the exact tRNA(Met) reaction."
  },
  "important_caveats": [
    "The sequence matches the cited current and historical UniProt records, but the author's exact source snapshot is unknown.",
    "The evidence for the specific EC assignment is computational (HAMAP); the cited publication supports broader RNA acetylation annotation, not necessarily direct validation of every substrate detail shown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options do not present another clearly equivalent EC assignment for the inferred TmcA-family activity."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0043",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched-sequence UniProt records assign EC 2.3.1.193 to this protein and describe acetylation of cytidine in elongator tRNA(Met). The specific EC assignment is attributed to the computational HAMAP rule; related RNA-acetylation annotations also cite a publication. This supports the key, though the supplied evidence does not independently establish direct experimental verification of the exact tRNA(Met) reaction.",
    "evidence_ids": ["C4", "C5", "C6", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 811-residue sequence is consistent with the conserved, multidomain TmcA-family RNA acetyltransferases, which combine nucleotide-dependent chemistry with an acetyltransferase function. Transferable family knowledge connects that architecture to acetylation of cytidine in tRNA and favors D, EC 2.3.1.193, over the other offered substrate-specific acetyltransferase A; the hydrolase and isomerase choices are less compatible.",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from the sequence can meaningfully distinguish the TmcA-associated EC choice without relying on the target's database record. The fine-grained substrate assignment is probabilistic from sequence-family recognition, not a direct demonstration of the reaction."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options do not present another clearly equivalent EC assignment for the inferred TmcA-family activity."
  },
  "important_caveats": [
    "The sequence matches the cited current and historical UniProt records, but the author's exact source snapshot is unknown.",
    "The evidence for the specific EC assignment is computational (HAMAP); the cited publication supports broader RNA acetylation annotation, not necessarily direct validation of every substrate detail shown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry B7R4L8 (TMCA_THES3) is annotated as EC 2.3.1.193 (tRNA(Met) cytidine acetyltransferase TmcA) via HAMAP-Rule MF_01886 (ECO:0000255), with additional experimental support from PubMed:32555463 (Nature 2020, Sas-Chen et al.) confirming RNA acetylation catalytic activity. The benchmark sequence matches the UniProt sequence exactly (811 aa, SHA-256 match). The annotation is primarily computational (HAMAP) but corroborated by experimental evidence.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a GNAT-fold acetyl-CoA-binding motif (visible as 'WIGSGFGASEELVRFWVRNG' near the C-terminal region, with the characteristic GxGxG pattern), identifying it as an acetyltransferase and eliminating B (3.2.1.55, glycosidase) and C (5.3.99.13, isomerase). Distinguishing A (2.3.1.319) from D (2.3.1.193) relies on recognizing the TmoS/TmcA family architecture: the protein displays a two-domain organization with an N-terminal PUA-like RNA-binding domain (the 'EETLFPKELYEMALTEGQVEVLKAFEELVEGGMLVLTADRGRGKSVSVGIGAIGLALALKK' region and downstream PUA-like fold) combined with the C-terminal GNAT acetyltransferase domain. The extremely lysine-rich composition (numerous K-rich stretches throughout) is characteristic of RNA-binding proteins rather than protein acetyltransferases. The TmoS/TmcA family is well-known from bacterial homologs (E. coli TmoS/RimK-like) where this GNAT+PUA two-domain architecture acetylates cytidine 34 of tRNA(Met). This family-level inference—recognizing the acetyltransferase + RNA-binding domain combination as diagnostic of an RNA-modifying acetyltransferase—distinguishes D (tRNA cytidine acetyltransferase) from A (a protein-targeting acetyltransferase).


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The GNAT motif identifies the enzyme class (acetyltransferase), eliminating B and C. The PUA domain and extensive lysine-rich RNA-binding character, recognizable from the TmoS/TmcA family of bacterial homologs and other RNA-modifying enzymes, indicate the substrate is RNA rather than protein, favoring EC 2.3.1.193 over EC 2.3.1.319. This is a legitimate family-level inference from transferable knowledge of related proteins.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> B and C are eliminated by the acetyltransferase fold. Between A and D, the RNA-binding architecture (PUA domain, lysine-rich composition) clearly favors an RNA acetyltransferase (D) over a protein acetyltransferase (A). While recognizing the PUA domain from sequence alone without domain-prediction tools adds some difficulty, the overall composition and two-domain architecture are sufficiently diagnostic for a knowledgeable model.


### Important caveats

- The primary annotation evidence is HAMAP-Rule (ECO:0000255, computational/curated), not direct experimental characterization of this exact archaeal protein, though the 2020 Nature paper provides experimental evidence for the catalytic activity class.
- Recognizing the PUA domain from raw sequence without domain-prediction tools is non-trivial; the argument relies on the overall lysine-rich composition and two-domain architecture as family-level cues.
- The exact identity of EC 2.3.1.319 (option A) is not specified in the question; the reasoning assumes it is a protein-targeting acetyltransferase, which the RNA-binding features would disfavor.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a GNAT-fold acetyl-CoA-binding motif (visible as 'WIGSGFGASEELVRFWVRNG' near the C-terminal region, with the characteristic GxGxG pattern), identifying it as an acetyltransferase and eliminating B (3.2.1.55, glycosidase) and C (5.3.99.13, isomerase). Distinguishing A (2.3.1.319) from D (2.3.1.193) relies on recognizing the TmoS/TmcA family architecture: the protein displays a two-domain organization with an N-terminal PUA-like RNA-binding domain (the 'EETLFPKELYEMALTEGQVEVLKAFEELVEGGMLVLTADRGRGKSVSVGIGAIGLALALKK' region and downstream PUA-like fold) combined with the C-terminal GNAT acetyltransferase domain. The extremely lysine-rich composition (numerous K-rich stretches throughout) is characteristic of RNA-binding proteins rather than protein acetyltransferases. The TmoS/TmcA family is well-known from bacterial homologs (E. coli TmoS/RimK-like) where this GNAT+PUA two-domain architecture acetylates cytidine 34 of tRNA(Met). This family-level inference—recognizing the acetyltransferase + RNA-binding domain combination as diagnostic of an RNA-modifying acetyltransferase—distinguishes D (tRNA cytidine acetyltransferase) from A (a protein-targeting acetyltransferase).",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The GNAT motif identifies the enzyme class (acetyltransferase), eliminating B and C. The PUA domain and extensive lysine-rich RNA-binding character, recognizable from the TmoS/TmcA family of bacterial homologs and other RNA-modifying enzymes, indicate the substrate is RNA rather than protein, favoring EC 2.3.1.193 over EC 2.3.1.319. This is a legitimate family-level inference from transferable knowledge of related proteins."
  },
  "case_id": "EC_number_0043",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "C8",
      "C9",
      "H1",
      "H2",
      "H3",
      "H4",
      "H5",
      "H6",
      "H7"
    ],
    "judgment": "supported",
    "reason": "UniProt entry B7R4L8 (TMCA_THES3) is annotated as EC 2.3.1.193 (tRNA(Met) cytidine acetyltransferase TmcA) via HAMAP-Rule MF_01886 (ECO:0000255), with additional experimental support from PubMed:32555463 (Nature 2020, Sas-Chen et al.) confirming RNA acetylation catalytic activity. The benchmark sequence matches the UniProt sequence exactly (811 aa, SHA-256 match). The annotation is primarily computational (HAMAP) but corroborated by experimental evidence."
  },
  "important_caveats": [
    "The primary annotation evidence is HAMAP-Rule (ECO:0000255, computational/curated), not direct experimental characterization of this exact archaeal protein, though the 2020 Nature paper provides experimental evidence for the catalytic activity class.",
    "Recognizing the PUA domain from raw sequence without domain-prediction tools is non-trivial; the argument relies on the overall lysine-rich composition and two-domain architecture as family-level cues.",
    "The exact identity of EC 2.3.1.319 (option A) is not specified in the question; the reasoning assumes it is a protein-targeting acetyltransferase, which the RNA-binding features would disfavor."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "B and C are eliminated by the acetyltransferase fold. Between A and D, the RNA-binding architecture (PUA domain, lysine-rich composition) clearly favors an RNA acetyltransferase (D) over a protein acetyltransferase (A). While recognizing the PUA domain from sequence alone without domain-prediction tools adds some difficulty, the overall composition and two-domain architecture are sufficiently diagnostic for a knowledgeable model."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0043",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry B7R4L8 (TMCA_THES3) is annotated as EC 2.3.1.193 (tRNA(Met) cytidine acetyltransferase TmcA) via HAMAP-Rule MF_01886 (ECO:0000255), with additional experimental support from PubMed:32555463 (Nature 2020, Sas-Chen et al.) confirming RNA acetylation catalytic activity. The benchmark sequence matches the UniProt sequence exactly (811 aa, SHA-256 match). The annotation is primarily computational (HAMAP) but corroborated by experimental evidence.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "C8", "C9", "H1", "H2", "H3", "H4", "H5", "H6", "H7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a GNAT-fold acetyl-CoA-binding motif (visible as 'WIGSGFGASEELVRFWVRNG' near the C-terminal region, with the characteristic GxGxG pattern), identifying it as an acetyltransferase and eliminating B (3.2.1.55, glycosidase) and C (5.3.99.13, isomerase). Distinguishing A (2.3.1.319) from D (2.3.1.193) relies on recognizing the TmoS/TmcA family architecture: the protein displays a two-domain organization with an N-terminal PUA-like RNA-binding domain (the 'EETLFPKELYEMALTEGQVEVLKAFEELVEGGMLVLTADRGRGKSVSVGIGAIGLALALKK' region and downstream PUA-like fold) combined with the C-terminal GNAT acetyltransferase domain. The extremely lysine-rich composition (numerous K-rich stretches throughout) is characteristic of RNA-binding proteins rather than protein acetyltransferases. The TmoS/TmcA family is well-known from bacterial homologs (E. coli TmoS/RimK-like) where this GNAT+PUA two-domain architecture acetylates cytidine 34 of tRNA(Met). This family-level inference—recognizing the acetyltransferase + RNA-binding domain combination as diagnostic of an RNA-modifying acetyltransferase—distinguishes D (tRNA cytidine acetyltransferase) from A (a protein-targeting acetyltransferase).",
    "missing_item_specific_fact": "",
    "reason": "The GNAT motif identifies the enzyme class (acetyltransferase), eliminating B and C. The PUA domain and extensive lysine-rich RNA-binding character, recognizable from the TmoS/TmcA family of bacterial homologs and other RNA-modifying enzymes, indicate the substrate is RNA rather than protein, favoring EC 2.3.1.193 over EC 2.3.1.319. This is a legitimate family-level inference from transferable knowledge of related proteins."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "B and C are eliminated by the acetyltransferase fold. Between A and D, the RNA-binding architecture (PUA domain, lysine-rich composition) clearly favors an RNA acetyltransferase (D) over a protein acetyltransferase (A). While recognizing the PUA domain from sequence alone without domain-prediction tools adds some difficulty, the overall composition and two-domain architecture are sufficiently diagnostic for a knowledgeable model."
  },
  "important_caveats": [
    "The primary annotation evidence is HAMAP-Rule (ECO:0000255, computational/curated), not direct experimental characterization of this exact archaeal protein, though the 2020 Nature paper provides experimental evidence for the catalytic activity class.",
    "Recognizing the PUA domain from raw sequence without domain-prediction tools is non-trivial; the argument relies on the overall lysine-rich composition and two-domain architecture as family-level cues.",
    "The exact identity of EC 2.3.1.319 (option A) is not specified in the question; the reasoning assumes it is a protein-targeting acetyltransferase, which the RNA-binding features would disfavor."
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
  "benchmark_sequence_length": 811,
  "benchmark_sequence_sha256": "f29b0e1a0dcfc0d2557bc357ee9d967f5b99c737bece29f23ad8fc02dedca365",
  "current_entry_audit": {
    "entryVersion": 78,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2009-02-10",
    "sequenceVersion": 1
  },
  "current_record_sha256": "03548e55c88bf9348a6f65fb414f93b7437267df4d20530afc1cfd7ab5fb87ce",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 811,
  "current_source_sequence_sha256": "f29b0e1a0dcfc0d2557bc357ee9d967f5b99c737bece29f23ad8fc02dedca365",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 76,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "B7R4L8",
  "selected_historical_entry_version": 76,
  "selected_historical_record_sha256": "2b39581803c115006a73d534827c01e6b71ccb3d0024965b8d497beced6710ad",
  "selected_historical_source_sequence_length": 811,
  "selected_historical_source_sequence_sha256": "f29b0e1a0dcfc0d2557bc357ee9d967f5b99c737bece29f23ad8fc02dedca365",
  "selected_historical_version": {
    "accession": "B7R4L8",
    "database": "Swiss-Prot",
    "entryVersion": 76,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "TMCA_THES3",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B7R4L8.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"B7R4L8\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:27:23.286634+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "03548e55c88bf9348a6f65fb414f93b7437267df4d20530afc1cfd7ab5fb87ce",
  "url": "https://rest.uniprot.org/uniprotkb/B7R4L8.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B7R4L8.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":78,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2009-02-10\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:27:23.286634+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "03548e55c88bf9348a6f65fb414f93b7437267df4d20530afc1cfd7ab5fb87ce",
  "url": "https://rest.uniprot.org/uniprotkb/B7R4L8.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B7R4L8.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Archaea\",\"Methanobacteriati\",\"Methanobacteriota\",\"Thermococci\",\"Thermococcales\",\"Thermococcaceae\",\"Thermococcus\"],\"scientificName\":\"Thermococcus sp. (strain AM4)\",\"taxonId\":246969}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:27:23.286634+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "03548e55c88bf9348a6f65fb414f93b7437267df4d20530afc1cfd7ab5fb87ce",
  "url": "https://rest.uniprot.org/uniprotkb/B7R4L8.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B7R4L8.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_01886\",\"source\":\"HAMAP-Rule\"}],\"value\":\"2.3.1.193\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_01886\",\"source\":\"HAMAP-Rule\"}],\"value\":\"tRNA(Met) cytidine acetyltransferase TmcA\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:27:23.286634+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "03548e55c88bf9348a6f65fb414f93b7437267df4d20530afc1cfd7ab5fb87ce",
  "url": "https://rest.uniprot.org/uniprotkb/B7R4L8.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B7R4L8.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"2.3.1.193\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_01886\",\"source\":\"HAMAP-Rule\"}],\"name\":\"cytidine(34) in elongator tRNA(Met) + acetyl-CoA + ATP + H2O = N(4)-acetylcytidine(34) in elongator tRNA(Met) + ADP + phosphate + CoA + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:43788\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:10693\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:10694\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:30616\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:43474\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57287\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57288\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:74900\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:82748\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:456216\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:27:23.286634+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "03548e55c88bf9348a6f65fb414f93b7437267df4d20530afc1cfd7ab5fb87ce",
  "url": "https://rest.uniprot.org/uniprotkb/B7R4L8.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B7R4L8.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_01886\",\"source\":\"HAMAP-Rule\"},{\"evidenceCode\":\"ECO:0000305\",\"id\":\"32555463\",\"source\":\"PubMed\"}],\"name\":\"a cytidine in RNA + acetyl-CoA + ATP + H2O = an N(4)-acetylcytidine in RNA + ADP + phosphate + CoA + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:82211\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:15704\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:19834\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:30616\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:43474\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57287\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57288\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:74900\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:82748\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:456216\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-02T04:27:23.286634+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "03548e55c88bf9348a6f65fb414f93b7437267df4d20530afc1cfd7ab5fb87ce",
  "url": "https://rest.uniprot.org/uniprotkb/B7R4L8.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B7R4L8.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_01886\",\"source\":\"HAMAP-Rule\"},{\"evidenceCode\":\"ECO:0000305\",\"id\":\"32555463\",\"source\":\"PubMed\"}],\"name\":\"a cytidine in tRNA + acetyl-CoA + ATP + H2O = an N(4)-acetylcytidine in tRNA + ADP + phosphate + CoA + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:53876\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:13670\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:13671\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:30616\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:43474\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57287\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57288\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:74900\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:82748\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:456216\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/4",
  "retrieved_utc": "2026-11-02T04:27:23.286634+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "03548e55c88bf9348a6f65fb414f93b7437267df4d20530afc1cfd7ab5fb87ce",
  "url": "https://rest.uniprot.org/uniprotkb/B7R4L8.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B7R4L8.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_01886\",\"source\":\"HAMAP-Rule\"},{\"evidenceCode\":\"ECO:0000305\",\"id\":\"32555463\",\"source\":\"PubMed\"}],\"name\":\"a cytidine in mRNA + acetyl-CoA + ATP + H2O = an N(4)-acetylcytidine in mRNA + ADP + phosphate + CoA + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:58480\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:15145\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:15146\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:30616\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:43474\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57287\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57288\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:74900\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:82748\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:456216\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/5",
  "retrieved_utc": "2026-11-02T04:27:23.286634+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "03548e55c88bf9348a6f65fb414f93b7437267df4d20530afc1cfd7ab5fb87ce",
  "url": "https://rest.uniprot.org/uniprotkb/B7R4L8.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B7R4L8.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"citation\":{\"authors\":[\"Sas-Chen A.\",\"Thomas J.M.\",\"Matzov D.\",\"Taoka M.\",\"Nance K.D.\",\"Nir R.\",\"Bryson K.M.\",\"Shachar R.\",\"Liman G.L.S.\",\"Burkhart B.W.\",\"Gamage S.T.\",\"Nobe Y.\",\"Briney C.A.\",\"Levy M.J.\",\"Fuchs R.T.\",\"Robb G.B.\",\"Hartmann J.\",\"Sharma S.\",\"Lin Q.\",\"Florens L.\",\"Washburn M.P.\",\"Isobe T.\",\"Santangelo T.J.\",\"Shalev-Benami M.\",\"Meier J.L.\",\"Schwartz S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"32555463\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41586-020-2418-2\"}],\"citationType\":\"journal article\",\"firstPage\":\"638\",\"id\":\"32555463\",\"journal\":\"Nature\",\"lastPage\":\"643\",\"publicationDate\":\"2020\",\"title\":\"Dynamic RNA acetylation revealed by quantitative cross-evolutionary mapping.\",\"volume\":\"583\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"AM4\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:27:23.286634+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "03548e55c88bf9348a6f65fb414f93b7437267df4d20530afc1cfd7ab5fb87ce",
  "url": "https://rest.uniprot.org/uniprotkb/B7R4L8.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B7R4L8?format=txt&versions=76)

```json
{
  "entry_version": 76,
  "evidence_id": "H1",
  "excerpt": "ID   TMCA_THES3              Reviewed;         811 AA.\nAC   B7R4L8;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   10-FEB-2009, sequence version 1.\nDT   28-JAN-2026, entry version 76.\nDE   RecName: Full=tRNA(Met) cytidine acetyltransferase TmcA {ECO:0000255|HAMAP-Rule:MF_01886};\nDE            EC=2.3.1.193 {ECO:0000255|HAMAP-Rule:MF_01886};\nGN   Name=tmcA {ECO:0000255|HAMAP-Rule:MF_01886};\nGN   ORFNames=TAM4_2097 {ECO:0000312|EMBL:EEB73240.1};\nOS   Thermococcus sp. (strain AM4).\nOC   Archaea; Methanobacteriati; Methanobacteriota; Thermococci; Thermococcales;\nOC   Thermococcaceae; Thermococcus.\nOX   NCBI_TaxID=246969;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:25.333292+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "2b39581803c115006a73d534827c01e6b71ccb3d0024965b8d497beced6710ad",
  "url": "https://rest.uniprot.org/unisave/B7R4L8?format=txt&versions=76"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B7R4L8?format=txt&versions=76)

```json
{
  "entry_version": 76,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=tRNA(Met) cytidine acetyltransferase TmcA {ECO:0000255|HAMAP-Rule:MF_01886};\nDE            EC=2.3.1.193 {ECO:0000255|HAMAP-Rule:MF_01886};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:25.333292+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-7",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "2b39581803c115006a73d534827c01e6b71ccb3d0024965b8d497beced6710ad",
  "url": "https://rest.uniprot.org/unisave/B7R4L8?format=txt&versions=76"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B7R4L8?format=txt&versions=76)

```json
{
  "entry_version": 76,
  "evidence_id": "H3",
  "excerpt": "RN   [2]\nRP   FUNCTION.\nRC   STRAIN=AM4;\nRX   PubMed=32555463; DOI=10.1038/s41586-020-2418-2;\nRA   Sas-Chen A., Thomas J.M., Matzov D., Taoka M., Nance K.D., Nir R.,\nRA   Bryson K.M., Shachar R., Liman G.L.S., Burkhart B.W., Gamage S.T., Nobe Y.,\nRA   Briney C.A., Levy M.J., Fuchs R.T., Robb G.B., Hartmann J., Sharma S.,\nRA   Lin Q., Florens L., Washburn M.P., Isobe T., Santangelo T.J.,\nRA   Shalev-Benami M., Meier J.L., Schwartz S.;\nRT   \"Dynamic RNA acetylation revealed by quantitative cross-evolutionary\nRT   mapping.\";\nRL   Nature 583:638-643(2020).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:25.333292+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 24-35",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "2b39581803c115006a73d534827c01e6b71ccb3d0024965b8d497beced6710ad",
  "url": "https://rest.uniprot.org/unisave/B7R4L8?format=txt&versions=76"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B7R4L8?format=txt&versions=76)

```json
{
  "entry_version": 76,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=cytidine(34) in elongator tRNA(Met) + acetyl-CoA + ATP + H2O =\nCC         N(4)-acetylcytidine(34) in elongator tRNA(Met) + ADP + phosphate +\nCC         CoA + H(+); Xref=Rhea:RHEA:43788, Rhea:RHEA-COMP:10693, Rhea:RHEA-\nCC         COMP:10694, ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:30616,\nCC         ChEBI:CHEBI:43474, ChEBI:CHEBI:57287, ChEBI:CHEBI:57288,\nCC         ChEBI:CHEBI:74900, ChEBI:CHEBI:82748, ChEBI:CHEBI:456216;\nCC         EC=2.3.1.193; Evidence={ECO:0000255|HAMAP-Rule:MF_01886};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:25.333292+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 44-51",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "2b39581803c115006a73d534827c01e6b71ccb3d0024965b8d497beced6710ad",
  "url": "https://rest.uniprot.org/unisave/B7R4L8?format=txt&versions=76"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B7R4L8?format=txt&versions=76)

```json
{
  "entry_version": 76,
  "evidence_id": "H5",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=a cytidine in RNA + acetyl-CoA + ATP + H2O = an N(4)-\nCC         acetylcytidine in RNA + ADP + phosphate + CoA + H(+);\nCC         Xref=Rhea:RHEA:82211, Rhea:RHEA-COMP:15704, Rhea:RHEA-COMP:19834,\nCC         ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:30616,\nCC         ChEBI:CHEBI:43474, ChEBI:CHEBI:57287, ChEBI:CHEBI:57288,\nCC         ChEBI:CHEBI:74900, ChEBI:CHEBI:82748, ChEBI:CHEBI:456216;\nCC         Evidence={ECO:0000255|HAMAP-Rule:MF_01886,\nCC         ECO:0000305|PubMed:32555463};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:25.333292+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 52-60",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "2b39581803c115006a73d534827c01e6b71ccb3d0024965b8d497beced6710ad",
  "url": "https://rest.uniprot.org/unisave/B7R4L8?format=txt&versions=76"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B7R4L8?format=txt&versions=76)

```json
{
  "entry_version": 76,
  "evidence_id": "H6",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=a cytidine in tRNA + acetyl-CoA + ATP + H2O = an N(4)-\nCC         acetylcytidine in tRNA + ADP + phosphate + CoA + H(+);\nCC         Xref=Rhea:RHEA:53876, Rhea:RHEA-COMP:13670, Rhea:RHEA-COMP:13671,\nCC         ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:30616,\nCC         ChEBI:CHEBI:43474, ChEBI:CHEBI:57287, ChEBI:CHEBI:57288,\nCC         ChEBI:CHEBI:74900, ChEBI:CHEBI:82748, ChEBI:CHEBI:456216;\nCC         Evidence={ECO:0000255|HAMAP-Rule:MF_01886,\nCC         ECO:0000305|PubMed:32555463};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:25.333292+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 61-69",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "2b39581803c115006a73d534827c01e6b71ccb3d0024965b8d497beced6710ad",
  "url": "https://rest.uniprot.org/unisave/B7R4L8?format=txt&versions=76"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B7R4L8?format=txt&versions=76)

```json
{
  "entry_version": 76,
  "evidence_id": "H7",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=a cytidine in mRNA + acetyl-CoA + ATP + H2O = an N(4)-\nCC         acetylcytidine in mRNA + ADP + phosphate + CoA + H(+);\nCC         Xref=Rhea:RHEA:58480, Rhea:RHEA-COMP:15145, Rhea:RHEA-COMP:15146,\nCC         ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:30616,\nCC         ChEBI:CHEBI:43474, ChEBI:CHEBI:57287, ChEBI:CHEBI:57288,\nCC         ChEBI:CHEBI:74900, ChEBI:CHEBI:82748, ChEBI:CHEBI:456216;\nCC         Evidence={ECO:0000255|HAMAP-Rule:MF_01886,\nCC         ECO:0000305|PubMed:32555463};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:25.333292+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 70-78",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "2b39581803c115006a73d534827c01e6b71ccb3d0024965b8d497beced6710ad",
  "url": "https://rest.uniprot.org/unisave/B7R4L8?format=txt&versions=76"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 43. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
