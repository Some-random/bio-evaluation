# GO_molecular_function_0003

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_molecular_function_0003.txt)

**Task:** `GO_molecular_function`  
**Expected answer:** **A** — carboxylesterase activity

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | contradicted | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MNKVKVGDAQVSYCIDGKGPGLVLVHGTGGDSETNWGHLMPALTNDWTVVRPDYSGSGITSDEGKQLEVKEIAAQVVAAAEAARVVPFDLVGFSLGSAVVIAIAADYPHLVRRIVLLGAFLSSRDIRQKTQFELWRDLIRTDRAALSRLILLTGFSPDFISKQGHDGVSVIINSFVSEINWEGMARQVELDLSIDVSEAARRIEKPTLVIGCSHDHIVPSSQAKSVVRIIRGAQYTELHTGHLAHIENPEEFILLLRSFLLSEDVP

[Multiple Choices]
A. carboxylesterase activity
B. double-stranded DNA endonuclease activity
C. structural constituent of nuclear pore
D. manganese ion transmembrane transporter activity
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Molecular Function Prediction, which is to predict the fundamental activity of a protein at the molecular level, as defined by the Gene Ontology (GO) 'Molecular Function' branch. This describes the elemental tasks a protein performs, such as catalysis, transport, or binding to specific molecules. Based on the protein's amino acid sequence, you are to select the option that best describes its primary molecular function.. The inputs provided by the user for this task include:

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

### Expected-answer support: contradicted

> The sequence-matched source describes the protein's experimentally supported activity as N-deacetylation of pyrrolizixenacetamide (C5, C6). That is hydrolysis of an amide bond, whereas carboxylesterase activity is defined as hydrolysis of a carboxylic ester (GO3). The computational keyword annotation in H5 does not establish this more specific activity.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [GO3](#evidence-go3), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a GxSxG motif (G-F-S-L-G), a transferable feature associated with the catalytic serine in serine hydrolases. That makes the hydrolase-like option A a more meaningful fit than a DNA endonuclease or nuclear-pore structural protein; the sequence also lacks an obvious multipass membrane-protein architecture expected for option D. The motif is not specific enough to establish ester rather than amide hydrolysis.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level hydrolase inference meaningfully favors A among these disparate choices, so exact-target lookup is not necessary to distinguish the options. However, the sequence-based inference does not validate the precise carboxylesterase annotation, and the recorded activity is an amide deacetylation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence supports a hydrolase-like choice over the other offered categories, but A's specific ester-hydrolysis wording does not match the reported primary reaction. None of the remaining options better describes that reaction.


### Important caveats

- The GxSxG motif supports a hydrolase-family inference but does not by itself establish substrate specificity.
- The supplied source reports the specific deacetylation reaction; it does not rule out all possible secondary activities.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a GxSxG motif (G-F-S-L-G), a transferable feature associated with the catalytic serine in serine hydrolases. That makes the hydrolase-like option A a more meaningful fit than a DNA endonuclease or nuclear-pore structural protein; the sequence also lacks an obvious multipass membrane-protein architecture expected for option D. The motif is not specific enough to establish ester rather than amide hydrolysis.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level hydrolase inference meaningfully favors A among these disparate choices, so exact-target lookup is not necessary to distinguish the options. However, the sequence-based inference does not validate the precise carboxylesterase annotation, and the recorded activity is an amide deacetylation."
  },
  "case_id": "GO_molecular_function_0003",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "GO3",
      "H5"
    ],
    "judgment": "contradicted",
    "reason": "The sequence-matched source describes the protein's experimentally supported activity as N-deacetylation of pyrrolizixenacetamide (C5, C6). That is hydrolysis of an amide bond, whereas carboxylesterase activity is defined as hydrolysis of a carboxylic ester (GO3). The computational keyword annotation in H5 does not establish this more specific activity."
  },
  "important_caveats": [
    "The GxSxG motif supports a hydrolase-family inference but does not by itself establish substrate specificity.",
    "The supplied source reports the specific deacetylation reaction; it does not rule out all possible secondary activities."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence supports a hydrolase-like choice over the other offered categories, but A's specific ester-hydrolysis wording does not match the reported primary reaction. None of the remaining options better describes that reaction."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0003",
  "expected_answer_check": {
    "judgment": "contradicted",
    "reason": "The sequence-matched source describes the protein's experimentally supported activity as N-deacetylation of pyrrolizixenacetamide (C5, C6). That is hydrolysis of an amide bond, whereas carboxylesterase activity is defined as hydrolysis of a carboxylic ester (GO3). The computational keyword annotation in H5 does not establish this more specific activity.",
    "evidence_ids": ["C5", "C6", "GO3", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a GxSxG motif (G-F-S-L-G), a transferable feature associated with the catalytic serine in serine hydrolases. That makes the hydrolase-like option A a more meaningful fit than a DNA endonuclease or nuclear-pore structural protein; the sequence also lacks an obvious multipass membrane-protein architecture expected for option D. The motif is not specific enough to establish ester rather than amide hydrolysis.",
    "missing_item_specific_fact": "",
    "reason": "A family-level hydrolase inference meaningfully favors A among these disparate choices, so exact-target lookup is not necessary to distinguish the options. However, the sequence-based inference does not validate the precise carboxylesterase annotation, and the recorded activity is an amide deacetylation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence supports a hydrolase-like choice over the other offered categories, but A's specific ester-hydrolysis wording does not match the reported primary reaction. None of the remaining options better describes that reaction."
  },
  "important_caveats": [
    "The GxSxG motif supports a hydrolase-family inference but does not by itself establish substrate specificity.",
    "The supplied source reports the specific deacetylation reaction; it does not rule out all possible secondary activities."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry annotates this protein with GO:0052689 (carboxylic ester hydrolase activity) via IEA:UniProtKB-KW, which is the parent term of GO:0106435 (carboxylesterase activity, the answer choice). The protein's Ntn-hydrolase fold (evidenced by the VHGTGG and CSHDH motifs) is consistent with the carboxylic ester hydrolase superfamily. However, the experimental evidence (ECO:0000269, PubMed:39428351) assigns EC 3.5.1.- (amidase/N-deacetylase), not EC 3.1.1.- (esterase). The GO annotation is inferred-electronic (IEA), not experimental. The answer is supported at the parent-term level by database annotation and fold classification, though the specific catalytic reaction is N-deacetylation rather than ester hydrolysis.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the VHGTGG motif and CSHDH catalytic residues, which are diagnostic of the Ntn-hydrolase (N-terminal nucleophile hydrolase) superfamily. This immediately identifies the protein as a hydrolase. Among the four choices: (B) double-stranded DNA endonuclease activity requires a nuclease fold (e.g., restriction enzyme, RecA-like, or HNH domains) entirely incompatible with Ntn-hydrolase motifs; (C) structural constituent of nuclear pore requires eukaryotic nucleoporin features (FG-repeats, large size, specific NPC subunit folds) absent here; (D) manganese ion transmembrane transporter activity requires multiple transmembrane helices (typically 6-8 TM segments in ZnT/MnT transporters), which this 266-aa soluble protein lacks. Only option A (carboxylesterase activity) is a hydrolase activity compatible with the Ntn-hydrolase fold. Thus, family-level recognition of the Ntn-hydrolase superfamily and elimination of non-hydrolase activities from the choices meaningfully distinguishes A.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The Ntn-hydrolase fold motifs (VHGTGG, CSHDH) are directly visible in the sequence and are well-known family signatures learned from penicillin acylase, glutaminase, cephalosporin acylase, and other Ntn-hydrolases. Recognizing this fold as a hydrolase and eliminating the three non-hydrolase options (nuclease, structural, transporter) is a standard sequence-to-function inference that does not require memorizing this specific protein's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options B, C, and D are clearly incompatible with the Ntn-hydrolase fold and the small soluble bacterial protein context. Only A is a hydrolase activity. No other option is defensible.


### Important caveats

- The actual experimental activity is EC 3.5.1.- (N-deacetylase/amidase), not EC 3.1.1.- (carboxylesterase). The GO annotation GO:0052689 is parent-level and IEA-inferred, not experimentally derived for this specific reaction.
- GO:0106435 (carboxylesterase activity) is a child of GO:0052689 (carboxylic ester hydrolase activity); the UniProt annotation is at the parent level, not the specific carboxylesterase term.
- The Ntn-hydrolase superfamily contains both esterases and amidases; distinguishing them from sequence alone is difficult. However, among the four offered choices, only A is a hydrolase, making the discrimination robust regardless of the esterase-vs-amidase subtlety.
- The UniProt accession and organism identity were not provided to the evaluated model; the reasoning relies solely on sequence motifs and general family knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the VHGTGG motif and CSHDH catalytic residues, which are diagnostic of the Ntn-hydrolase (N-terminal nucleophile hydrolase) superfamily. This immediately identifies the protein as a hydrolase. Among the four choices: (B) double-stranded DNA endonuclease activity requires a nuclease fold (e.g., restriction enzyme, RecA-like, or HNH domains) entirely incompatible with Ntn-hydrolase motifs; (C) structural constituent of nuclear pore requires eukaryotic nucleoporin features (FG-repeats, large size, specific NPC subunit folds) absent here; (D) manganese ion transmembrane transporter activity requires multiple transmembrane helices (typically 6-8 TM segments in ZnT/MnT transporters), which this 266-aa soluble protein lacks. Only option A (carboxylesterase activity) is a hydrolase activity compatible with the Ntn-hydrolase fold. Thus, family-level recognition of the Ntn-hydrolase superfamily and elimination of non-hydrolase activities from the choices meaningfully distinguishes A.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The Ntn-hydrolase fold motifs (VHGTGG, CSHDH) are directly visible in the sequence and are well-known family signatures learned from penicillin acylase, glutaminase, cephalosporin acylase, and other Ntn-hydrolases. Recognizing this fold as a hydrolase and eliminating the three non-hydrolase options (nuclease, structural, transporter) is a standard sequence-to-function inference that does not require memorizing this specific protein's annotation."
  },
  "case_id": "GO_molecular_function_0003",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry annotates this protein with GO:0052689 (carboxylic ester hydrolase activity) via IEA:UniProtKB-KW, which is the parent term of GO:0106435 (carboxylesterase activity, the answer choice). The protein's Ntn-hydrolase fold (evidenced by the VHGTGG and CSHDH motifs) is consistent with the carboxylic ester hydrolase superfamily. However, the experimental evidence (ECO:0000269, PubMed:39428351) assigns EC 3.5.1.- (amidase/N-deacetylase), not EC 3.1.1.- (esterase). The GO annotation is inferred-electronic (IEA), not experimental. The answer is supported at the parent-term level by database annotation and fold classification, though the specific catalytic reaction is N-deacetylation rather than ester hydrolysis."
  },
  "important_caveats": [
    "The actual experimental activity is EC 3.5.1.- (N-deacetylase/amidase), not EC 3.1.1.- (carboxylesterase). The GO annotation GO:0052689 is parent-level and IEA-inferred, not experimentally derived for this specific reaction.",
    "GO:0106435 (carboxylesterase activity) is a child of GO:0052689 (carboxylic ester hydrolase activity); the UniProt annotation is at the parent level, not the specific carboxylesterase term.",
    "The Ntn-hydrolase superfamily contains both esterases and amidases; distinguishing them from sequence alone is difficult. However, among the four offered choices, only A is a hydrolase, making the discrimination robust regardless of the esterase-vs-amidase subtlety.",
    "The UniProt accession and organism identity were not provided to the evaluated model; the reasoning relies solely on sequence motifs and general family knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B, C, and D are clearly incompatible with the Ntn-hydrolase fold and the small soluble bacterial protein context. Only A is a hydrolase activity. No other option is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0003",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry annotates this protein with GO:0052689 (carboxylic ester hydrolase activity) via IEA:UniProtKB-KW, which is the parent term of GO:0106435 (carboxylesterase activity, the answer choice). The protein's Ntn-hydrolase fold (evidenced by the VHGTGG and CSHDH motifs) is consistent with the carboxylic ester hydrolase superfamily. However, the experimental evidence (ECO:0000269, PubMed:39428351) assigns EC 3.5.1.- (amidase/N-deacetylase), not EC 3.1.1.- (esterase). The GO annotation is inferred-electronic (IEA), not experimental. The answer is supported at the parent-term level by database annotation and fold classification, though the specific catalytic reaction is N-deacetylation rather than ester hydrolysis.",
    "evidence_ids": ["C4", "C5", "C6", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the VHGTGG motif and CSHDH catalytic residues, which are diagnostic of the Ntn-hydrolase (N-terminal nucleophile hydrolase) superfamily. This immediately identifies the protein as a hydrolase. Among the four choices: (B) double-stranded DNA endonuclease activity requires a nuclease fold (e.g., restriction enzyme, RecA-like, or HNH domains) entirely incompatible with Ntn-hydrolase motifs; (C) structural constituent of nuclear pore requires eukaryotic nucleoporin features (FG-repeats, large size, specific NPC subunit folds) absent here; (D) manganese ion transmembrane transporter activity requires multiple transmembrane helices (typically 6-8 TM segments in ZnT/MnT transporters), which this 266-aa soluble protein lacks. Only option A (carboxylesterase activity) is a hydrolase activity compatible with the Ntn-hydrolase fold. Thus, family-level recognition of the Ntn-hydrolase superfamily and elimination of non-hydrolase activities from the choices meaningfully distinguishes A.",
    "missing_item_specific_fact": "",
    "reason": "The Ntn-hydrolase fold motifs (VHGTGG, CSHDH) are directly visible in the sequence and are well-known family signatures learned from penicillin acylase, glutaminase, cephalosporin acylase, and other Ntn-hydrolases. Recognizing this fold as a hydrolase and eliminating the three non-hydrolase options (nuclease, structural, transporter) is a standard sequence-to-function inference that does not require memorizing this specific protein's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B, C, and D are clearly incompatible with the Ntn-hydrolase fold and the small soluble bacterial protein context. Only A is a hydrolase activity. No other option is defensible."
  },
  "important_caveats": [
    "The actual experimental activity is EC 3.5.1.- (N-deacetylase/amidase), not EC 3.1.1.- (carboxylesterase). The GO annotation GO:0052689 is parent-level and IEA-inferred, not experimentally derived for this specific reaction.",
    "GO:0106435 (carboxylesterase activity) is a child of GO:0052689 (carboxylic ester hydrolase activity); the UniProt annotation is at the parent level, not the specific carboxylesterase term.",
    "The Ntn-hydrolase superfamily contains both esterases and amidases; distinguishing them from sequence alone is difficult. However, among the four offered choices, only A is a hydrolase, making the discrimination robust regardless of the esterase-vs-amidase subtlety.",
    "The UniProt accession and organism identity were not provided to the evaluated model; the reasoning relies solely on sequence motifs and general family knowledge."
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
  "benchmark_sequence_length": 266,
  "benchmark_sequence_sha256": "db237f760869551b09464ba4867169aafc47d9b85d114228f62281edb6b9c76d",
  "current_entry_audit": {
    "entryVersion": 30,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2018-01-31",
    "sequenceVersion": 1
  },
  "current_record_sha256": "ae3334cfc3b11f2536437c9d5e79945575a56544d5415a430b401730b6c628d9",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 266,
  "current_source_sequence_sha256": "db237f760869551b09464ba4867169aafc47d9b85d114228f62281edb6b9c76d",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 28,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A2G0QDP0",
  "selected_historical_entry_version": 28,
  "selected_historical_record_sha256": "d0bca0810bb663b04edc4dd649d45e97b5536f59d4132847e0dc79e272689d14",
  "selected_historical_source_sequence_length": 266,
  "selected_historical_source_sequence_sha256": "db237f760869551b09464ba4867169aafc47d9b85d114228f62281edb6b9c76d",
  "selected_historical_version": {
    "accession": "A0A2G0QDP0",
    "database": "Swiss-Prot",
    "entryVersion": 28,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "XHPG_XENHO",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2G0QDP0.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A2G0QDP0\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:24:47.833416+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ae3334cfc3b11f2536437c9d5e79945575a56544d5415a430b401730b6c628d9",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2G0QDP0.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2G0QDP0.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":30,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2018-01-31\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:24:47.833416+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ae3334cfc3b11f2536437c9d5e79945575a56544d5415a430b401730b6c628d9",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2G0QDP0.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2G0QDP0.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Pseudomonadota\",\"Gammaproteobacteria\",\"Enterobacterales\",\"Morganellaceae\",\"Xenorhabdus\"],\"scientificName\":\"Xenorhabdus hominickii\",\"taxonId\":351679}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:24:47.833416+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ae3334cfc3b11f2536437c9d5e79945575a56544d5415a430b401730b6c628d9",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2G0QDP0.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2G0QDP0.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39428351\",\"source\":\"PubMed\"}],\"value\":\"Pyrrolizixenamide hydrolase\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39428351\",\"source\":\"PubMed\"}],\"value\":\"3.5.1.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"39428351\",\"source\":\"PubMed\"}],\"value\":\"Pyrrolizixenacetamide deacetylase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:24:47.833416+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ae3334cfc3b11f2536437c9d5e79945575a56544d5415a430b401730b6c628d9",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2G0QDP0.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2G0QDP0.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39428351\",\"source\":\"PubMed\"}],\"value\":\"Involved in the biosynthetic pathway of pyrrolizwilline, a pyrrolizidine alkaloid. Catalyzes the N-deacetylation of pyrrolizixenacetamide\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-02T04:24:47.833416+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ae3334cfc3b11f2536437c9d5e79945575a56544d5415a430b401730b6c628d9",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2G0QDP0.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2G0QDP0.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39428351\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:83308\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39428351\",\"source\":\"PubMed\"}],\"name\":\"pyrrolizixenacetamide + H2O = 3-amino-5,6,7,7a-tetrahydro-1H-pyrrolizin-1-one + acetate + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:83307\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:30089\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:232461\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:232462\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:24:47.833416+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ae3334cfc3b11f2536437c9d5e79945575a56544d5415a430b401730b6c628d9",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2G0QDP0.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2G0QDP0.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Effert J.\",\"Westphalen M.\",\"Calderari A.\",\"Shi Y.M.\",\"Elamri I.\",\"Najah S.\",\"Gruen P.\",\"Li Y.\",\"Gruez A.\",\"Weissman K.J.\",\"Bode H.B.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39428351\"},{\"database\":\"DOI\",\"id\":\"10.1002/anie.202411258\"}],\"citationType\":\"journal article\",\"firstPage\":\"e202411258\",\"id\":\"39428351\",\"journal\":\"Angew. Chem. Int. Ed.\",\"lastPage\":\"e202411258\",\"publicationDate\":\"2024\",\"title\":\"Pyrrolizwilline, a unique bacterial alkaloid assembled by a nonribosomal peptide synthetase and non-enzymatic dimerization.\",\"volume\":\"63\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8QZU\",\"source\":\"PDB\"}],\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"DSM 17903 / CIP 109072 / KE01\"}],\"referenceNumber\":2,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (1.18 ANGSTROMS) OF MUTANT ALA-94 IN COMPLEX WITH ACETATE\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"DISRUPTION PHENOTYPE\",\"SUBUNIT\",\"ACTIVE SITE\",\"MUTAGENESIS OF ASN-35 AND SER-94\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:24:47.833416+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ae3334cfc3b11f2536437c9d5e79945575a56544d5415a430b401730b6c628d9",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2G0QDP0.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2G0QDP0?format=txt&versions=28)

```json
{
  "entry_version": 28,
  "evidence_id": "H1",
  "excerpt": "ID   XHPG_XENHO              Reviewed;         266 AA.\nAC   A0A2G0QDP0;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   31-JAN-2018, sequence version 1.\nDT   28-JAN-2026, entry version 28.\nDE   RecName: Full=Pyrrolizixenacetamide deacetylase {ECO:0000305|PubMed:39428351};\nDE            EC=3.5.1.- {ECO:0000269|PubMed:39428351};\nDE   AltName: Full=Pyrrolizixenamide hydrolase {ECO:0000303|PubMed:39428351};\nGN   Name=xhpG {ECO:0000303|PubMed:39428351};\nGN   ORFNames=Xhom_00310 {ECO:0000312|EMBL:PHM57344.1};\nOS   Xenorhabdus hominickii.\nOC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria;\nOC   Enterobacterales; Morganellaceae; Xenorhabdus.\nOX   NCBI_TaxID=351679;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:49.959052+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d0bca0810bb663b04edc4dd649d45e97b5536f59d4132847e0dc79e272689d14",
  "url": "https://rest.uniprot.org/unisave/A0A2G0QDP0?format=txt&versions=28"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2G0QDP0?format=txt&versions=28)

```json
{
  "entry_version": 28,
  "evidence_id": "H2",
  "excerpt": "RN   [2] {ECO:0007744|PDB:8QZU}\nRP   X-RAY CRYSTALLOGRAPHY (1.18 ANGSTROMS) OF MUTANT ALA-94 IN COMPLEX WITH\nRP   ACETATE, FUNCTION, CATALYTIC ACTIVITY, DISRUPTION PHENOTYPE, SUBUNIT,\nRP   ACTIVE SITE, AND MUTAGENESIS OF ASN-35 AND SER-94.\nRC   STRAIN=DSM 17903 / CIP 109072 / KE01;\nRX   PubMed=39428351; DOI=10.1002/anie.202411258;\nRA   Effert J., Westphalen M., Calderari A., Shi Y.M., Elamri I., Najah S.,\nRA   Gruen P., Li Y., Gruez A., Weissman K.J., Bode H.B.;\nRT   \"Pyrrolizwilline, a unique bacterial alkaloid assembled by a nonribosomal\nRT   peptide synthetase and non-enzymatic dimerization.\";\nRL   Angew. Chem. Int. Ed. 63:e202411258-e202411258(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:49.959052+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 25-35",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d0bca0810bb663b04edc4dd649d45e97b5536f59d4132847e0dc79e272689d14",
  "url": "https://rest.uniprot.org/unisave/A0A2G0QDP0?format=txt&versions=28"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2G0QDP0?format=txt&versions=28)

```json
{
  "entry_version": 28,
  "evidence_id": "H3",
  "excerpt": "CC   -!- FUNCTION: Involved in the biosynthetic pathway of pyrrolizwilline, a\nCC       pyrrolizidine alkaloid. Catalyzes the N-deacetylation of\nCC       pyrrolizixenacetamide. {ECO:0000269|PubMed:39428351}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:49.959052+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 36-38",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d0bca0810bb663b04edc4dd649d45e97b5536f59d4132847e0dc79e272689d14",
  "url": "https://rest.uniprot.org/unisave/A0A2G0QDP0?format=txt&versions=28"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2G0QDP0?format=txt&versions=28)

```json
{
  "entry_version": 28,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=pyrrolizixenacetamide + H2O = 3-amino-5,6,7,7a-tetrahydro-1H-\nCC         pyrrolizin-1-one + acetate + H(+); Xref=Rhea:RHEA:83307,\nCC         ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:30089,\nCC         ChEBI:CHEBI:232461, ChEBI:CHEBI:232462;\nCC         Evidence={ECO:0000269|PubMed:39428351};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:83308;\nCC         Evidence={ECO:0000269|PubMed:39428351};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:49.959052+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 39-46",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d0bca0810bb663b04edc4dd649d45e97b5536f59d4132847e0dc79e272689d14",
  "url": "https://rest.uniprot.org/unisave/A0A2G0QDP0?format=txt&versions=28"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2G0QDP0?format=txt&versions=28)

```json
{
  "entry_version": 28,
  "evidence_id": "H5",
  "excerpt": "DR   GO; GO:0052689; F:carboxylic ester hydrolase activity; IEA:UniProtKB-KW.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:49.959052+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 66-66",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d0bca0810bb663b04edc4dd649d45e97b5536f59d4132847e0dc79e272689d14",
  "url": "https://rest.uniprot.org/unisave/A0A2G0QDP0?format=txt&versions=28"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0005384\nname: manganese ion transmembrane transporter activity\nnamespace: molecular_function\ndef: \"Enables the transfer of manganese (Mn) ions from one side of a membrane to the other.\" [GOC:dgf]\nxref: MetaCyc:RXN0-16\nxref: Reactome:R-HSA-8959798 \"SLC30A10 transports Mn2+ from cytosol to extracellular region\"\nis_a: GO:0046915 ! transition metal ion transmembrane transporter activity\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005384",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 56277-56285",
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
  "excerpt": "[Term]\nid: GO:0017056\nname: structural constituent of nuclear pore\nnamespace: molecular_function\nalt_id: GO:0005487\ndef: \"The action of a molecule that contributes to the structural integrity of the nuclear pore complex, a protein-lined channel in the nuclear envelope that allows the transfer of macromolecules.\" [GOC:mah, PMID:25802992]\ncomment: Note that this term is meant to be used for nuclear pore proteins. For importins and exportins, consider 'nuclear import signal receptor activity' or 'nuclear export signal receptor activity', respectively.\nsynonym: \"nuclear pore activity\" RELATED []\nsynonym: \"nucleocytoplasmic transporter activity\" EXACT []\nxref: Reactome:R-HSA-1176059 \"Translocation of Influenza A virus nonstructural protein 1 (NS1A) into the nucleus\"\nxref: Reactome:R-HSA-170796 \"NPC transports GCK1:GCKR from cytosol to nucleoplasm\"\nxref: Reactome:R-HSA-192627 \"Viral mRNA Export\"\nxref: Reactome:R-HSA-192925 \"Export of Spliced Viral mRNA\"\nxref: Reactome:R-HSA-5252041 \"NPC transports Hikeshi:HSP70s:ATP from cytosol to nucleoplasm\"\nxref: Reactome:R-HSA-5661474 \"Defective NPC does not transport GCK1:GKRP from cytosol to nucleoplasm\"\nxref: Reactome:R-HSA-6783483 \"tRNA:XPOT:RAN:GTP translocates from the nucleus to the cytosol\"\nis_a: GO:0005198 ! structural molecule activity\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0017056",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 132832-132849",
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
  "excerpt": "[Term]\nid: GO:0106435\nname: carboxylesterase activity\nnamespace: molecular_function\ndef: \"Catalysis of the reaction: a carboxylic ester + H2O = a carboxylate + an alcohol + H+.\" [RHEA:21164]\ncomment: Note: This covers a broad range of specificity; also hydrolyzes vitamin A esters.\nsynonym: \"ali-esterase activity\" RELATED [EC:3.1.1.1]\nsynonym: \"alpha-carboxylesterase activity\" NARROW []\nsynonym: \"B-esterase activity\" NARROW [EC:3.1.1.1]\nsynonym: \"cocaine esterase\" NARROW [EC:3.1.1.1]\nsynonym: \"nonspecific carboxylesterase activity\" RELATED []\nsynonym: \"procaine esterase\" NARROW [] {comment=\"EC:3.1.1.1\"}\nsynonym: \"serine esterase activity\" NARROW []\nsynonym: \"triacetin esterase\" NARROW []\nsynonym: \"vitamin A esterase\" NARROW []\nxref: EC:3.1.1.1\nxref: MetaCyc:CARBOXYLESTERASE-RXN\nxref: Reactome:R-HSA-9619024 \"CES1 trimer hydrolyses ACEI pro-drugs to ACEIs\"\nxref: Reactome:R-HSA-9727567 \"CES1 hydrolyses sacubitril to sacubitrilat\"\nxref: Reactome:R-HSA-9749647 \"CES2 hydrolyzes ASA-\"\nxref: RHEA:21164\nxref: RHEA:31779\nxref: RHEA:38555\nxref: RHEA:47348\nxref: RHEA:47352\nxref: RHEA:47356\nxref: RHEA:47360\nxref: RHEA:47364\nxref: RHEA:47388\nxref: RHEA:47392\nxref: RHEA:50136\nxref: RHEA:50144\nxref: RHEA:50148\nxref: RHEA:59388\nxref: RHEA:63052\nis_a: GO:0052689 ! carboxylic ester hydrolase activity\nproperty_value: skos:exactMatch EC:3.1.1.1\nproperty_value: skos:exactMatch RHEA:21164\nproperty_value: skos:narrowMatch RHEA:31779\nproperty_value: skos:narrowMatch RHEA:38555\nproperty_value: skos:narrowMatch RHEA:47348\nproperty_value: skos:narrowMatch RHEA:47352\nproperty_value: skos:narrowMatch RHEA:47356\nproperty_value: skos:narrowMatch RHEA:47360\nproperty_value: skos:narrowMatch RHEA:47364\nproperty_value: skos:narrowMatch RHEA:47388\nproperty_value: skos:narrowMatch RHEA:47392\nproperty_value: skos:narrowMatch RHEA:50136\nproperty_value: skos:narrowMatch RHEA:50144\nproperty_value: skos:narrowMatch RHEA:50148\nproperty_value: skos:narrowMatch RHEA:59388\nproperty_value: skos:narrowMatch RHEA:63052\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0106435",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 430643-430695",
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
  "excerpt": "[Term]\nid: GO:1990238\nname: double-stranded DNA endonuclease activity\nnamespace: molecular_function\ndef: \"Catalysis of the hydrolysis of ester linkages within a double-stranded DNA molecule by creating internal breaks.\" [PMID:22885404]\nsynonym: \"double-stranded DNA endodeoxyribonuclease activity\" EXACT []\nsynonym: \"dsDNA-specific endodeoxyribonuclease activity\" RELATED []\nis_a: GO:0004520 ! DNA endonuclease activity\nis_a: GO:0016788 ! hydrolase activity, acting on ester bonds\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:1990238",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 550453-550462",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 3. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
