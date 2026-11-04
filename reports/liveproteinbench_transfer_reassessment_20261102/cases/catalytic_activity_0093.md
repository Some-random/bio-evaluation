# catalytic_activity_0093

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/catalytic_activity_0093.txt)

**Task:** `catalytic_activity`  
**Expected answer:** **A** — cytidine(34) in elongator tRNA(Met) + acetyl-CoA + ATP + H2O = N(4)-acetylcytidine(34) in elongator tRNA(Met) + ADP + phosphate + CoA + H(+)

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
A. cytidine(34) in elongator tRNA(Met) + acetyl-CoA + ATP + H2O = N(4)-acetylcytidine(34) in elongator tRNA(Met) + ADP + phosphate + CoA + H(+)
B. L-proline betaine + NADH + O2 + H(+) = N-methyl-L-proline + formaldehyde + NAD(+) + H2O
C. L-homocysteine + glycine betaine = N,N-dimethylglycine + L-methionine
D. L-leucyl-tRNA(Leu) + acetyl-CoA = N-acetyl-L-leucyl-tRNA(Leu) + CoA + H(+)
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

> The sequence-matched UniProt annotation assigns this protein EC 2.3.1.193 and the exact reaction in A, based on a HAMAP rule (C4, C5; also H2, H4). Separate annotation evidence supports acetylation of cytidine in RNA more broadly, including a PubMed-supported entry (C6; H5). The exact tRNA(Met) reaction is computationally annotated in the supplied excerpts, so this supports the key without establishing that the specific reaction was experimentally measured for this protein.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The long soluble sequence is consistent with the multidomain TmcA-family pattern: ATP-utilizing and acetyltransferase functions are combined in an RNA-modifying enzyme. Transferable knowledge of that family supports ATP-dependent acetylation of RNA cytidine, distinguishing A from the betaine reactions in B and C and the ATP-independent leucyl-tRNA acetylation in D. This is a family-level inference from the sequence, not a claim that the exact substrate specificity can be proven from sequence alone.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family recognition and the reaction chemistry provide a meaningful basis to choose A among these alternatives. The exact tRNA(Met) substrate assignment is more specific than the broad family inference, but the choices do not require distinguishing among additional RNA substrates.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only A matches the supported ATP-dependent RNA cytidine acetylation activity; the other choices describe different reaction classes or substrates.


### Important caveats

- The exact tRNA(Met) reaction annotation in the supplied evidence is computationally assigned by HAMAP; the PubMed-supported evidence shown is for broader RNA cytidine acetylation.
- The reviewer-only source identity and annotations were not original model inputs and are used only to assess answer support.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The long soluble sequence is consistent with the multidomain TmcA-family pattern: ATP-utilizing and acetyltransferase functions are combined in an RNA-modifying enzyme. Transferable knowledge of that family supports ATP-dependent acetylation of RNA cytidine, distinguishing A from the betaine reactions in B and C and the ATP-independent leucyl-tRNA acetylation in D. This is a family-level inference from the sequence, not a claim that the exact substrate specificity can be proven from sequence alone.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family recognition and the reaction chemistry provide a meaningful basis to choose A among these alternatives. The exact tRNA(Met) substrate assignment is more specific than the broad family inference, but the choices do not require distinguishing among additional RNA substrates."
  },
  "case_id": "catalytic_activity_0093",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H2",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation assigns this protein EC 2.3.1.193 and the exact reaction in A, based on a HAMAP rule (C4, C5; also H2, H4). Separate annotation evidence supports acetylation of cytidine in RNA more broadly, including a PubMed-supported entry (C6; H5). The exact tRNA(Met) reaction is computationally annotated in the supplied excerpts, so this supports the key without establishing that the specific reaction was experimentally measured for this protein."
  },
  "important_caveats": [
    "The exact tRNA(Met) reaction annotation in the supplied evidence is computationally assigned by HAMAP; the PubMed-supported evidence shown is for broader RNA cytidine acetylation.",
    "The reviewer-only source identity and annotations were not original model inputs and are used only to assess answer support."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only A matches the supported ATP-dependent RNA cytidine acetylation activity; the other choices describe different reaction classes or substrates."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0093",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation assigns this protein EC 2.3.1.193 and the exact reaction in A, based on a HAMAP rule (C4, C5; also H2, H4). Separate annotation evidence supports acetylation of cytidine in RNA more broadly, including a PubMed-supported entry (C6; H5). The exact tRNA(Met) reaction is computationally annotated in the supplied excerpts, so this supports the key without establishing that the specific reaction was experimentally measured for this protein.",
    "evidence_ids": ["C4", "C5", "C6", "H2", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The long soluble sequence is consistent with the multidomain TmcA-family pattern: ATP-utilizing and acetyltransferase functions are combined in an RNA-modifying enzyme. Transferable knowledge of that family supports ATP-dependent acetylation of RNA cytidine, distinguishing A from the betaine reactions in B and C and the ATP-independent leucyl-tRNA acetylation in D. This is a family-level inference from the sequence, not a claim that the exact substrate specificity can be proven from sequence alone.",
    "missing_item_specific_fact": "",
    "reason": "Family recognition and the reaction chemistry provide a meaningful basis to choose A among these alternatives. The exact tRNA(Met) substrate assignment is more specific than the broad family inference, but the choices do not require distinguishing among additional RNA substrates."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only A matches the supported ATP-dependent RNA cytidine acetylation activity; the other choices describe different reaction classes or substrates."
  },
  "important_caveats": [
    "The exact tRNA(Met) reaction annotation in the supplied evidence is computationally assigned by HAMAP; the PubMed-supported evidence shown is for broader RNA cytidine acetylation.",
    "The reviewer-only source identity and annotations were not original model inputs and are used only to assess answer support."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry B7R4L8 (sequence matched exactly, 811 aa) annotates this protein as 'tRNA(Met) cytidine acetyltransferase TmcA' (EC 2.3.1.193) with the catalytic activity reaction matching Choice A verbatim. The primary evidence code is ECO:0000255 (HAMAP-Rule MF_01886, a computational family-based annotation), supplemented by ECO:0000305 from PubMed 32555463 (Nature 2020). The annotation is database-supported and consistent with the family assignment, though the primary evidence is computational rather than direct experimental characterization of this specific archaeal protein.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a highly diagnostic GNAT (GCN5-related N-acetyltransferase) motif 'GSGFGA' in the C-terminal region, which is a well-known signature of acetyltransferase enzymes. This immediately eliminates Choices B (oxidase/demethylase) and C (methyltransferase), which involve entirely different enzyme classes. The overall 811-residue multi-domain architecture—N-terminal Rossmann fold (GDTLR...GILAGASARVLS), middle TIM barrel (GIGAIGLALALK...IVVTAPEL), and C-terminal GNAT domain (GSGFGA...GFAVVHLSPARNPVSGEFTAIVLKPISERAKKLIKK)—is the hallmark architecture of the Elongator/TmcA/Nat superfamily of tRNA modification enzymes. Family-level knowledge from well-studied eukaryotic Elongator subunit 3 (ELP3) and bacterial/archaeal TmcA homologs establishes that this multi-domain GNAT architecture specifically modifies the cytidine base at position 34 of the anticodon loop of tRNA(Met), not the amino acid attached to tRNA. Choice D (N-acetyl-leucyl-tRNA transferase) would require a much simpler, single-domain GNAT enzyme acting on the aminoacyl moiety at the 3' end of tRNA, inconsistent with the elaborate nucleic-acid-binding multi-domain architecture observed here. The requirement for ATP hydrolysis (present in A, absent in D) is also a known family-level feature of Elongator/TmcA-type enzymes for tRNA positioning.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can identify the GNAT motif from sequence to establish acetyltransferase activity (eliminating B and C), recognize the multi-domain Rossmann+TIM+GNAT architecture as characteristic of tRNA modification enzymes rather than simple amino acid acetyltransferases (distinguishing A from D), and apply family-level knowledge from well-characterized Elongator/TmcA homologs that these enzymes modify nucleotides (cytidine 34) rather than amino acids on tRNA. The inference relies on transferable family and domain-architecture knowledge rather than memorization of this specific protein's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The GNAT motif clearly eliminates B and C. The multi-domain architecture with nucleic-acid-binding folds is inconsistent with the simple aminoacyl-tRNA acetyltransferase described in D. While the distinction between A and D requires family-level knowledge, the architectural evidence strongly favors A over D. No other option is defensible given the sequence features.


### Important caveats

- The primary UniProt evidence for this annotation is computational (HAMAP rule MF_01886), not direct experimental characterization of this specific Thermococcus protein. The 2020 Nature paper (PubMed 32555463) provides experimental support for RNA acetylation by TmcA homologs but may not have directly assayed this exact archaeal enzyme.
- The distinction between A and D, while supported by family-level reasoning, is not trivially obvious from sequence alone without knowledge of the Elongator/TmcA superfamily's substrate specificity. A model unfamiliar with this family might struggle to definitively exclude D.
- The protein is from an archaeal organism (Thermococcus sp. AM4); most detailed mechanistic knowledge of TmcA/Elongator comes from eukaryotic and bacterial homologs.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a highly diagnostic GNAT (GCN5-related N-acetyltransferase) motif 'GSGFGA' in the C-terminal region, which is a well-known signature of acetyltransferase enzymes. This immediately eliminates Choices B (oxidase/demethylase) and C (methyltransferase), which involve entirely different enzyme classes. The overall 811-residue multi-domain architecture—N-terminal Rossmann fold (GDTLR...GILAGASARVLS), middle TIM barrel (GIGAIGLALALK...IVVTAPEL), and C-terminal GNAT domain (GSGFGA...GFAVVHLSPARNPVSGEFTAIVLKPISERAKKLIKK)—is the hallmark architecture of the Elongator/TmcA/Nat superfamily of tRNA modification enzymes. Family-level knowledge from well-studied eukaryotic Elongator subunit 3 (ELP3) and bacterial/archaeal TmcA homologs establishes that this multi-domain GNAT architecture specifically modifies the cytidine base at position 34 of the anticodon loop of tRNA(Met), not the amino acid attached to tRNA. Choice D (N-acetyl-leucyl-tRNA transferase) would require a much simpler, single-domain GNAT enzyme acting on the aminoacyl moiety at the 3' end of tRNA, inconsistent with the elaborate nucleic-acid-binding multi-domain architecture observed here. The requirement for ATP hydrolysis (present in A, absent in D) is also a known family-level feature of Elongator/TmcA-type enzymes for tRNA positioning.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can identify the GNAT motif from sequence to establish acetyltransferase activity (eliminating B and C), recognize the multi-domain Rossmann+TIM+GNAT architecture as characteristic of tRNA modification enzymes rather than simple amino acid acetyltransferases (distinguishing A from D), and apply family-level knowledge from well-characterized Elongator/TmcA homologs that these enzymes modify nucleotides (cytidine 34) rather than amino acids on tRNA. The inference relies on transferable family and domain-architecture knowledge rather than memorization of this specific protein's annotation."
  },
  "case_id": "catalytic_activity_0093",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H4",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry B7R4L8 (sequence matched exactly, 811 aa) annotates this protein as 'tRNA(Met) cytidine acetyltransferase TmcA' (EC 2.3.1.193) with the catalytic activity reaction matching Choice A verbatim. The primary evidence code is ECO:0000255 (HAMAP-Rule MF_01886, a computational family-based annotation), supplemented by ECO:0000305 from PubMed 32555463 (Nature 2020). The annotation is database-supported and consistent with the family assignment, though the primary evidence is computational rather than direct experimental characterization of this specific archaeal protein."
  },
  "important_caveats": [
    "The primary UniProt evidence for this annotation is computational (HAMAP rule MF_01886), not direct experimental characterization of this specific Thermococcus protein. The 2020 Nature paper (PubMed 32555463) provides experimental support for RNA acetylation by TmcA homologs but may not have directly assayed this exact archaeal enzyme.",
    "The distinction between A and D, while supported by family-level reasoning, is not trivially obvious from sequence alone without knowledge of the Elongator/TmcA superfamily's substrate specificity. A model unfamiliar with this family might struggle to definitively exclude D.",
    "The protein is from an archaeal organism (Thermococcus sp. AM4); most detailed mechanistic knowledge of TmcA/Elongator comes from eukaryotic and bacterial homologs."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The GNAT motif clearly eliminates B and C. The multi-domain architecture with nucleic-acid-binding folds is inconsistent with the simple aminoacyl-tRNA acetyltransferase described in D. While the distinction between A and D requires family-level knowledge, the architectural evidence strongly favors A over D. No other option is defensible given the sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0093",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry B7R4L8 (sequence matched exactly, 811 aa) annotates this protein as 'tRNA(Met) cytidine acetyltransferase TmcA' (EC 2.3.1.193) with the catalytic activity reaction matching Choice A verbatim. The primary evidence code is ECO:0000255 (HAMAP-Rule MF_01886, a computational family-based annotation), supplemented by ECO:0000305 from PubMed 32555463 (Nature 2020). The annotation is database-supported and consistent with the family assignment, though the primary evidence is computational rather than direct experimental characterization of this specific archaeal protein.",
    "evidence_ids": ["C4", "C5", "H4", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a highly diagnostic GNAT (GCN5-related N-acetyltransferase) motif 'GSGFGA' in the C-terminal region, which is a well-known signature of acetyltransferase enzymes. This immediately eliminates Choices B (oxidase/demethylase) and C (methyltransferase), which involve entirely different enzyme classes. The overall 811-residue multi-domain architecture—N-terminal Rossmann fold (GDTLR...GILAGASARVLS), middle TIM barrel (GIGAIGLALALK...IVVTAPEL), and C-terminal GNAT domain (GSGFGA...GFAVVHLSPARNPVSGEFTAIVLKPISERAKKLIKK)—is the hallmark architecture of the Elongator/TmcA/Nat superfamily of tRNA modification enzymes. Family-level knowledge from well-studied eukaryotic Elongator subunit 3 (ELP3) and bacterial/archaeal TmcA homologs establishes that this multi-domain GNAT architecture specifically modifies the cytidine base at position 34 of the anticodon loop of tRNA(Met), not the amino acid attached to tRNA. Choice D (N-acetyl-leucyl-tRNA transferase) would require a much simpler, single-domain GNAT enzyme acting on the aminoacyl moiety at the 3' end of tRNA, inconsistent with the elaborate nucleic-acid-binding multi-domain architecture observed here. The requirement for ATP hydrolysis (present in A, absent in D) is also a known family-level feature of Elongator/TmcA-type enzymes for tRNA positioning.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can identify the GNAT motif from sequence to establish acetyltransferase activity (eliminating B and C), recognize the multi-domain Rossmann+TIM+GNAT architecture as characteristic of tRNA modification enzymes rather than simple amino acid acetyltransferases (distinguishing A from D), and apply family-level knowledge from well-characterized Elongator/TmcA homologs that these enzymes modify nucleotides (cytidine 34) rather than amino acids on tRNA. The inference relies on transferable family and domain-architecture knowledge rather than memorization of this specific protein's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The GNAT motif clearly eliminates B and C. The multi-domain architecture with nucleic-acid-binding folds is inconsistent with the simple aminoacyl-tRNA acetyltransferase described in D. While the distinction between A and D requires family-level knowledge, the architectural evidence strongly favors A over D. No other option is defensible given the sequence features."
  },
  "important_caveats": [
    "The primary UniProt evidence for this annotation is computational (HAMAP rule MF_01886), not direct experimental characterization of this specific Thermococcus protein. The 2020 Nature paper (PubMed 32555463) provides experimental support for RNA acetylation by TmcA homologs but may not have directly assayed this exact archaeal enzyme.",
    "The distinction between A and D, while supported by family-level reasoning, is not trivially obvious from sequence alone without knowledge of the Elongator/TmcA superfamily's substrate specificity. A model unfamiliar with this family might struggle to definitively exclude D.",
    "The protein is from an archaeal organism (Thermococcus sp. AM4); most detailed mechanistic knowledge of TmcA/Elongator comes from eukaryotic and bacterial homologs."
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

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 93. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
