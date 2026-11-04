# catalytic_activity_0016

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/catalytic_activity_0016.txt)

**Task:** `catalytic_activity`  
**Expected answer:** **A** — L-fucose + ATP = beta-L-fucose 1-phosphate + ADP + H(+)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MQKLLSLPSNLVQSFHELERVNRTDWFCTSDPVGKKLGSGGGTSWLLEECYNEYSDGATFGEWLEKEKRILLHAGGQSRRLPGYAPSGKILTPVPVFRWERGQHLGQNLLSLQLPLYEKIMSLAPDKLHTLIASGDVYIRSEKPLQSIPEADVVCYGLWVDPSLATHHGVFASDRKHPEQLDFMLQKPSLAELESLSKTHLFLMDIGIWLLSDRAVEILMKRSHKESSEELKYYDLYSDFGLALGTHPRIEDEEVNTLSVAILPLPGGEFYHYGTSKELISSTLSVQNKVYDQRRIMHRKVKPNPAMFVQNAVVRIPLCAENADLWIENSHIGPKWKIASRHIITGVPENDWSLAVPAGVCVDVVPMGDKGFVARPYGLDDVFKGDLRDSKTTLTGIPFGEWMSKRGLSYTDLKGRTDDLQAVSVFPMVNSVEELGLVLRWMLSEPELEEGKNIWLRSEHFSADEISAGANLKRLYAQREEFRKGNWKALAVNHEKSVFYQLDLADAAEDFVRLGLDMPELLPEDALQMSRIHNRMLRARILKLDGKDYRPEEQAAFDLLRDGLLDGISNRKSTPKLDVYSDQIVWGRSPVRIDMAGGWTDTPPYSLYSGGNVVNLAIELNGQPPLQVYVKPCKDFHIVLRSIDMGAMEIVSTFDELQDYKKIGSPFSIPKAALSLAGFAPAFSAVSYASLEEQLKDFGAGIEVTLLAAIPAGSGLGTSSILASTVLGAINDFCGLAWDKNEICQRTLVLEQLLTTGGGWQDQYGGVLQGVKLLQTEAGFAQSPLVRWLPDHLFTHPEYKDCHLLYYTGITRTAKGILAEIVSSMFLNSSLHLNLLSEMKAHALDMNEAIQRGSFVEFGRLVGKTWEQNKALDSGTNPPAVEAIIDLIKDYTLGYKLPGAGGGGYLYMVAKDPQAAVRIRKILTENAPNPRARFVEMTLSDKGFQVSRS

[Multiple Choices]
A. L-fucose + ATP = beta-L-fucose 1-phosphate + ADP + H(+)
B. a cytidine in mRNA + acetyl-CoA + ATP + H2O = an N(4)-acetylcytidine in mRNA + ADP + phosphate + CoA + H(+)
C. Endonucleolytic cleavage to 5'-phosphomonoester.
D. N-[(R)-4-phosphopantothenoyl]-L-cysteine + H(+) = (R)-4'-phosphopantetheine + CO2
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

> The sequence-matched UniProt annotation reports this reaction with experimental evidence (ECO:0000269).

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> A knowledgeable model could recognize sequence patterns consistent with the bifunctional fucokinase/GDP-fucose pyrophosphorylase family. Transferable knowledge of this family connects an ATP-dependent fucose kinase domain to phosphorylation of fucose, matching A; the other choices describe unrelated RNA modification, nuclease, or coenzyme-biosynthesis chemistry.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level sequence recognition gives a meaningful basis for selecting A among these alternatives, although the sequence alone may not establish the exact substrate as decisively as experimental characterization.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only A matches the fucokinase activity indicated by the family-level inference. The protein may have another catalytic activity, but no other option describes it.


### Important caveats

- The evidence supports A for the sequence-matched protein; the provided annotation also reports a second catalytic activity not listed among the choices.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A knowledgeable model could recognize sequence patterns consistent with the bifunctional fucokinase/GDP-fucose pyrophosphorylase family. Transferable knowledge of this family connects an ATP-dependent fucose kinase domain to phosphorylation of fucose, matching A; the other choices describe unrelated RNA modification, nuclease, or coenzyme-biosynthesis chemistry.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level sequence recognition gives a meaningful basis for selecting A among these alternatives, although the sequence alone may not establish the exact substrate as decisively as experimental characterization."
  },
  "case_id": "catalytic_activity_0016",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation reports this reaction with experimental evidence (ECO:0000269)."
  },
  "important_caveats": [
    "The evidence supports A for the sequence-matched protein; the provided annotation also reports a second catalytic activity not listed among the choices."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only A matches the fucokinase activity indicated by the family-level inference. The protein may have another catalytic activity, but no other option describes it."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0016",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation reports this reaction with experimental evidence (ECO:0000269).",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "A knowledgeable model could recognize sequence patterns consistent with the bifunctional fucokinase/GDP-fucose pyrophosphorylase family. Transferable knowledge of this family connects an ATP-dependent fucose kinase domain to phosphorylation of fucose, matching A; the other choices describe unrelated RNA modification, nuclease, or coenzyme-biosynthesis chemistry.",
    "missing_item_specific_fact": "",
    "reason": "Family-level sequence recognition gives a meaningful basis for selecting A among these alternatives, although the sequence alone may not establish the exact substrate as decisively as experimental characterization."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only A matches the fucokinase activity indicated by the family-level inference. The protein may have another catalytic activity, but no other option describes it."
  },
  "important_caveats": [
    "The evidence supports A for the sequence-matched protein; the provided annotation also reports a second catalytic activity not listed among the choices."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q58T34 (sequence SHA256 matched exactly to the benchmark sequence) explicitly annotates the catalytic activity as 'L-fucose + ATP = beta-L-fucose 1-phosphate + ADP + H(+)' (EC 2.7.1.52, L-fucokinase) with evidence code ECO:0000269 (direct experimental evidence from PubMed:30242642, a cryo-EM and functional study). The reaction text in the annotation matches option A verbatim. The protein is a bifunctional L-fucokinase/GDP-fucose pyrophosphorylase (FKP), and the fucokinase half-reaction is the one listed among the choices.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4), [C4](#evidence-c4), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Several transferable features distinguish option A from the alternatives: (1) Protein size: at 949 aa, the protein is far too large for a typical endonuclease (option C, usually 100-300 aa) or phosphopantothenoylcysteine decarboxylase (option D, ~250 aa in known homologs). (2) Kinase motifs: the N-terminal region contains a glycine-rich stretch 'GSGGGTSW' consistent with a P-loop/ATP-binding glycine-rich motif found in many sugar kinases, pointing toward a phosphotransferase (kinase) rather than a nuclease, decarboxylase, or RNA acetyltransferase. (3) Among the four options, only A describes a kinase reaction; B is an RNA acetyltransferase (would require RNA-binding motifs and acetyl-CoA-binding domain, absent here), C is a hydrolase, and D is a lyase. (4) Family-level knowledge: bifunctional FKP enzymes (~900 aa, kinase + pyrophosphorylase domains) are a well-characterized family in Bacteroidetes, and the overall domain architecture (two large lobes with distinct motifs) is consistent with this family. Recognizing a ~900 aa bifunctional kinase/transferase with a glycine-rich ATP-binding loop is transferable family knowledge, not a lookup of this specific protein's record.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The combination of protein size (949 aa), presence of glycine-rich kinase-like motifs, absence of nuclease/decarboxylase/RNA-binding features, and knowledge of the FKP family (bifunctional ~900 aa enzymes in Bacteroidetes) provides a concrete, transferable argument that meaningfully distinguishes option A from B, C, and D without requiring recall of this exact protein's database annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent four fundamentally different enzyme classes (kinase, RNA acetyltransferase, nuclease, decarboxylase). The protein's size, sequence motifs, and domain architecture clearly favor a kinase/transferase, making A the only defensible choice. Although the UniProt entry lists a second activity (guanylyltransferase, EC 2.7.7.30), that reaction is not among the offered options, so it does not create ambiguity.


### Important caveats

- The UniProt entry annotates two catalytic activities (fucokinase EC 2.7.1.52 and guanylyltransferase EC 2.7.7.30). Only the fucokinase reaction appears among the choices, so no ambiguity arises from the bifunctional nature.
- The evidence code ECO:0000269 indicates direct experimental evidence (from the 2019 cryo-EM/functional study), strengthening the annotation's reliability.
- The glycine-rich motif 'GSGGG' is suggestive but not uniquely diagnostic of fucose kinase; the size and family-level context are the stronger discriminators.
- Organism identity (Bacteroides fragilis) was not provided in the original input; the FKP family argument relies on recognizing the ~900 aa bifunctional architecture as a known family pattern rather than on knowing the specific organism.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Several transferable features distinguish option A from the alternatives: (1) Protein size: at 949 aa, the protein is far too large for a typical endonuclease (option C, usually 100-300 aa) or phosphopantothenoylcysteine decarboxylase (option D, ~250 aa in known homologs). (2) Kinase motifs: the N-terminal region contains a glycine-rich stretch 'GSGGGTSW' consistent with a P-loop/ATP-binding glycine-rich motif found in many sugar kinases, pointing toward a phosphotransferase (kinase) rather than a nuclease, decarboxylase, or RNA acetyltransferase. (3) Among the four options, only A describes a kinase reaction; B is an RNA acetyltransferase (would require RNA-binding motifs and acetyl-CoA-binding domain, absent here), C is a hydrolase, and D is a lyase. (4) Family-level knowledge: bifunctional FKP enzymes (~900 aa, kinase + pyrophosphorylase domains) are a well-characterized family in Bacteroidetes, and the overall domain architecture (two large lobes with distinct motifs) is consistent with this family. Recognizing a ~900 aa bifunctional kinase/transferase with a glycine-rich ATP-binding loop is transferable family knowledge, not a lookup of this specific protein's record.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The combination of protein size (949 aa), presence of glycine-rich kinase-like motifs, absence of nuclease/decarboxylase/RNA-binding features, and knowledge of the FKP family (bifunctional ~900 aa enzymes in Bacteroidetes) provides a concrete, transferable argument that meaningfully distinguishes option A from B, C, and D without requiring recall of this exact protein's database annotation."
  },
  "case_id": "catalytic_activity_0016",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4",
      "C4",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q58T34 (sequence SHA256 matched exactly to the benchmark sequence) explicitly annotates the catalytic activity as 'L-fucose + ATP = beta-L-fucose 1-phosphate + ADP + H(+)' (EC 2.7.1.52, L-fucokinase) with evidence code ECO:0000269 (direct experimental evidence from PubMed:30242642, a cryo-EM and functional study). The reaction text in the annotation matches option A verbatim. The protein is a bifunctional L-fucokinase/GDP-fucose pyrophosphorylase (FKP), and the fucokinase half-reaction is the one listed among the choices."
  },
  "important_caveats": [
    "The UniProt entry annotates two catalytic activities (fucokinase EC 2.7.1.52 and guanylyltransferase EC 2.7.7.30). Only the fucokinase reaction appears among the choices, so no ambiguity arises from the bifunctional nature.",
    "The evidence code ECO:0000269 indicates direct experimental evidence (from the 2019 cryo-EM/functional study), strengthening the annotation's reliability.",
    "The glycine-rich motif 'GSGGG' is suggestive but not uniquely diagnostic of fucose kinase; the size and family-level context are the stronger discriminators.",
    "Organism identity (Bacteroides fragilis) was not provided in the original input; the FKP family argument relies on recognizing the ~900 aa bifunctional architecture as a known family pattern rather than on knowing the specific organism."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent four fundamentally different enzyme classes (kinase, RNA acetyltransferase, nuclease, decarboxylase). The protein's size, sequence motifs, and domain architecture clearly favor a kinase/transferase, making A the only defensible choice. Although the UniProt entry lists a second activity (guanylyltransferase, EC 2.7.7.30), that reaction is not among the offered options, so it does not create ambiguity."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0016",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q58T34 (sequence SHA256 matched exactly to the benchmark sequence) explicitly annotates the catalytic activity as 'L-fucose + ATP = beta-L-fucose 1-phosphate + ADP + H(+)' (EC 2.7.1.52, L-fucokinase) with evidence code ECO:0000269 (direct experimental evidence from PubMed:30242642, a cryo-EM and functional study). The reaction text in the annotation matches option A verbatim. The protein is a bifunctional L-fucokinase/GDP-fucose pyrophosphorylase (FKP), and the fucokinase half-reaction is the one listed among the choices.",
    "evidence_ids": ["C5", "H4", "C4", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Several transferable features distinguish option A from the alternatives: (1) Protein size: at 949 aa, the protein is far too large for a typical endonuclease (option C, usually 100-300 aa) or phosphopantothenoylcysteine decarboxylase (option D, ~250 aa in known homologs). (2) Kinase motifs: the N-terminal region contains a glycine-rich stretch 'GSGGGTSW' consistent with a P-loop/ATP-binding glycine-rich motif found in many sugar kinases, pointing toward a phosphotransferase (kinase) rather than a nuclease, decarboxylase, or RNA acetyltransferase. (3) Among the four options, only A describes a kinase reaction; B is an RNA acetyltransferase (would require RNA-binding motifs and acetyl-CoA-binding domain, absent here), C is a hydrolase, and D is a lyase. (4) Family-level knowledge: bifunctional FKP enzymes (~900 aa, kinase + pyrophosphorylase domains) are a well-characterized family in Bacteroidetes, and the overall domain architecture (two large lobes with distinct motifs) is consistent with this family. Recognizing a ~900 aa bifunctional kinase/transferase with a glycine-rich ATP-binding loop is transferable family knowledge, not a lookup of this specific protein's record.",
    "missing_item_specific_fact": "",
    "reason": "The combination of protein size (949 aa), presence of glycine-rich kinase-like motifs, absence of nuclease/decarboxylase/RNA-binding features, and knowledge of the FKP family (bifunctional ~900 aa enzymes in Bacteroidetes) provides a concrete, transferable argument that meaningfully distinguishes option A from B, C, and D without requiring recall of this exact protein's database annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent four fundamentally different enzyme classes (kinase, RNA acetyltransferase, nuclease, decarboxylase). The protein's size, sequence motifs, and domain architecture clearly favor a kinase/transferase, making A the only defensible choice. Although the UniProt entry lists a second activity (guanylyltransferase, EC 2.7.7.30), that reaction is not among the offered options, so it does not create ambiguity."
  },
  "important_caveats": [
    "The UniProt entry annotates two catalytic activities (fucokinase EC 2.7.1.52 and guanylyltransferase EC 2.7.7.30). Only the fucokinase reaction appears among the choices, so no ambiguity arises from the bifunctional nature.",
    "The evidence code ECO:0000269 indicates direct experimental evidence (from the 2019 cryo-EM/functional study), strengthening the annotation's reliability.",
    "The glycine-rich motif 'GSGGG' is suggestive but not uniquely diagnostic of fucose kinase; the size and family-level context are the stronger discriminators.",
    "Organism identity (Bacteroides fragilis) was not provided in the original input; the FKP family argument relies on recognizing the ~900 aa bifunctional architecture as a known family pattern rather than on knowing the specific organism."
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
  "benchmark_sequence_length": 949,
  "benchmark_sequence_sha256": "0a1aad3ffd7b1cb09dfa4c0be0b330d8ac5ca7321345ec11ac9ab6c74f4a10e2",
  "current_entry_audit": {
    "entryVersion": 89,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2005-04-26",
    "sequenceVersion": 1
  },
  "current_record_sha256": "613cb95f164460b198373fe8b1a0278d6f82b5f36a7ad73441bef68f5e41af74",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 949,
  "current_source_sequence_sha256": "0a1aad3ffd7b1cb09dfa4c0be0b330d8ac5ca7321345ec11ac9ab6c74f4a10e2",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 87,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q58T34",
  "selected_historical_entry_version": 87,
  "selected_historical_record_sha256": "3ecc50c16d349ff2fe2b86dd83a0288577ce5483563a520fae349796ac46e9a8",
  "selected_historical_source_sequence_length": 949,
  "selected_historical_source_sequence_sha256": "0a1aad3ffd7b1cb09dfa4c0be0b330d8ac5ca7321345ec11ac9ab6c74f4a10e2",
  "selected_historical_version": {
    "accession": "Q58T34",
    "database": "Swiss-Prot",
    "entryVersion": 87,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "FKP_BACFG",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q58T34.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q58T34\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:31:01.700323+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "613cb95f164460b198373fe8b1a0278d6f82b5f36a7ad73441bef68f5e41af74",
  "url": "https://rest.uniprot.org/uniprotkb/Q58T34.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q58T34.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":89,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2005-04-26\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:31:01.700323+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "613cb95f164460b198373fe8b1a0278d6f82b5f36a7ad73441bef68f5e41af74",
  "url": "https://rest.uniprot.org/uniprotkb/Q58T34.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q58T34.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Bacteroidota\",\"Bacteroidia\",\"Bacteroidales\",\"Bacteroidaceae\",\"Bacteroides\"],\"scientificName\":\"Bacteroides fragilis\",\"taxonId\":817}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:31:01.700323+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "613cb95f164460b198373fe8b1a0278d6f82b5f36a7ad73441bef68f5e41af74",
  "url": "https://rest.uniprot.org/uniprotkb/Q58T34.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q58T34.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30242642\",\"source\":\"PubMed\"}],\"value\":\"L-fucokinase/GDP-fucose pyrophosphorylase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30242642\",\"source\":\"PubMed\"}],\"value\":\"FKP\"}]}],\"includes\":[{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30242642\",\"source\":\"PubMed\"}],\"value\":\"GDP-fucose pyrophosphorylase\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"30242642\",\"source\":\"PubMed\"}],\"value\":\"2.7.7.30\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"30242642\",\"source\":\"PubMed\"}],\"value\":\"Fucose-1-phosphate guanylyltransferase\"}}},{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"30242642\",\"source\":\"PubMed\"}],\"value\":\"2.7.1.52\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30242642\",\"source\":\"PubMed\"}],\"value\":\"L-fucokinase\"}}}],\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"30242642\",\"source\":\"PubMed\"}],\"value\":\"L-fucokinase/L-fucose-1-P guanylyltransferase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:31:01.700323+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "613cb95f164460b198373fe8b1a0278d6f82b5f36a7ad73441bef68f5e41af74",
  "url": "https://rest.uniprot.org/uniprotkb/Q58T34.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q58T34.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"30242642\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:13242\"}}],\"reaction\":{\"ecNumber\":\"2.7.1.52\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"30242642\",\"source\":\"PubMed\"}],\"name\":\"beta-L-fucose + ATP = beta-L-fucose 1-phosphate + ADP + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:13241\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:30616\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:42589\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57268\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:456216\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:31:01.700323+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "613cb95f164460b198373fe8b1a0278d6f82b5f36a7ad73441bef68f5e41af74",
  "url": "https://rest.uniprot.org/uniprotkb/Q58T34.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q58T34.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"30242642\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:13550\"}}],\"reaction\":{\"ecNumber\":\"2.7.7.30\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"30242642\",\"source\":\"PubMed\"}],\"name\":\"beta-L-fucose 1-phosphate + GTP + H(+) = GDP-beta-L-fucose + diphosphate\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:13549\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:33019\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:37565\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57268\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57273\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:31:01.700323+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "613cb95f164460b198373fe8b1a0278d6f82b5f36a7ad73441bef68f5e41af74",
  "url": "https://rest.uniprot.org/uniprotkb/Q58T34.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q58T34.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Liu Y.\",\"Hu H.\",\"Wang J.\",\"Zhou Q.\",\"Wu P.\",\"Yan N.\",\"Wang H.W.\",\"Wu J.W.\",\"Sun L.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"30242642\"},{\"database\":\"DOI\",\"id\":\"10.1007/s13238-018-0576-x\"}],\"citationType\":\"journal article\",\"firstPage\":\"365\",\"id\":\"30242642\",\"journal\":\"Protein Cell\",\"lastPage\":\"369\",\"publicationDate\":\"2019\",\"title\":\"Cryo-EM structure of L-fucokinase/GDP-fucose pyrophosphorylase (FKP) in Bacteroides fragilis.\",\"volume\":\"10\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"5YYS\",\"source\":\"PDB\"}],\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"9343\"}],\"referenceNumber\":3,\"referencePositions\":[\"STRUCTURE BY ELECTRON MICROSCOPY (4.20 ANGSTROMS)\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"SUBUNIT\",\"DOMAIN\",\"MUTAGENESIS OF GLY-76; ARG-80; GLY-88; LYS-89; ARG-592; ASP-594; GLY-597; GLY-598; ASP-601; GLY-713; SER-714; GLY-715; GLY-717; SER-719; SER-720; ALA-723; GLY-758; GLY-759; GLN-761; ASP-762; GLY-899 AND GLY-901\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-02T04:31:01.700323+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "613cb95f164460b198373fe8b1a0278d6f82b5f36a7ad73441bef68f5e41af74",
  "url": "https://rest.uniprot.org/uniprotkb/Q58T34.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q58T34?format=txt&versions=87)

```json
{
  "entry_version": 87,
  "evidence_id": "H1",
  "excerpt": "ID   FKP_BACFG               Reviewed;         949 AA.\nAC   Q58T34;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   26-APR-2005, sequence version 1.\nDT   28-JAN-2026, entry version 87.\nDE   RecName: Full=L-fucokinase/L-fucose-1-P guanylyltransferase {ECO:0000305|PubMed:30242642};\nDE   AltName: Full=L-fucokinase/GDP-fucose pyrophosphorylase {ECO:0000303|PubMed:30242642};\nDE            Short=FKP {ECO:0000303|PubMed:30242642};\nDE   Includes:\nDE     RecName: Full=Fucose-1-phosphate guanylyltransferase {ECO:0000305|PubMed:30242642};\nDE              EC=2.7.7.30 {ECO:0000269|PubMed:30242642};\nDE     AltName: Full=GDP-fucose pyrophosphorylase {ECO:0000303|PubMed:30242642};\nDE   Includes:\nDE     RecName: Full=L-fucokinase {ECO:0000303|PubMed:30242642};\nDE              EC=2.7.1.52 {ECO:0000269|PubMed:30242642};\nGN   Name=fkp {ECO:0000312|EMBL:AAX45030.1};\nGN   ORFNames=HMPREF2533_03026 {ECO:0000312|EMBL:KXU43832.1};\nOS   Bacteroides fragilis.\nOC   Bacteria; Pseudomonadati; Bacteroidota; Bacteroidia; Bacteroidales;\nOC   Bacteroidaceae; Bacteroides.\nOX   NCBI_TaxID=817;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:04.760170+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-21",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3ecc50c16d349ff2fe2b86dd83a0288577ce5483563a520fae349796ac46e9a8",
  "url": "https://rest.uniprot.org/unisave/Q58T34?format=txt&versions=87"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q58T34?format=txt&versions=87)

```json
{
  "entry_version": 87,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=L-fucokinase/L-fucose-1-P guanylyltransferase {ECO:0000305|PubMed:30242642};\nDE   AltName: Full=L-fucokinase/GDP-fucose pyrophosphorylase {ECO:0000303|PubMed:30242642};\nDE            Short=FKP {ECO:0000303|PubMed:30242642};\nDE   Includes:\nDE     RecName: Full=Fucose-1-phosphate guanylyltransferase {ECO:0000305|PubMed:30242642};\nDE              EC=2.7.7.30 {ECO:0000269|PubMed:30242642};\nDE     AltName: Full=GDP-fucose pyrophosphorylase {ECO:0000303|PubMed:30242642};\nDE   Includes:\nDE     RecName: Full=L-fucokinase {ECO:0000303|PubMed:30242642};\nDE              EC=2.7.1.52 {ECO:0000269|PubMed:30242642};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:04.760170+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3ecc50c16d349ff2fe2b86dd83a0288577ce5483563a520fae349796ac46e9a8",
  "url": "https://rest.uniprot.org/unisave/Q58T34?format=txt&versions=87"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q58T34?format=txt&versions=87)

```json
{
  "entry_version": 87,
  "evidence_id": "H3",
  "excerpt": "RN   [3] {ECO:0007744|PDB:5YYS}\nRP   STRUCTURE BY ELECTRON MICROSCOPY (4.20 ANGSTROMS), FUNCTION, CATALYTIC\nRP   ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, SUBUNIT, DOMAIN, AND MUTAGENESIS\nRP   OF GLY-76; ARG-80; GLY-88; LYS-89; ARG-592; ASP-594; GLY-597; GLY-598;\nRP   ASP-601; GLY-713; SER-714; GLY-715; GLY-717; SER-719; SER-720; ALA-723;\nRP   GLY-758; GLY-759; GLN-761; ASP-762; GLY-899 AND GLY-901.\nRC   STRAIN=9343;\nRX   PubMed=30242642; DOI=10.1007/s13238-018-0576-x;\nRA   Liu Y., Hu H., Wang J., Zhou Q., Wu P., Yan N., Wang H.W., Wu J.W., Sun L.;\nRT   \"Cryo-EM structure of L-fucokinase/GDP-fucose pyrophosphorylase (FKP) in\nRT   Bacteroides fragilis.\";\nRL   Protein Cell 10:365-369(2019).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:04.760170+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 36-47",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3ecc50c16d349ff2fe2b86dd83a0288577ce5483563a520fae349796ac46e9a8",
  "url": "https://rest.uniprot.org/unisave/Q58T34?format=txt&versions=87"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q58T34?format=txt&versions=87)

```json
{
  "entry_version": 87,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=L-fucose + ATP = beta-L-fucose 1-phosphate + ADP + H(+);\nCC         Xref=Rhea:RHEA:13241, ChEBI:CHEBI:2181, ChEBI:CHEBI:15378,\nCC         ChEBI:CHEBI:30616, ChEBI:CHEBI:57268, ChEBI:CHEBI:456216;\nCC         EC=2.7.1.52; Evidence={ECO:0000269|PubMed:30242642};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:13242;\nCC         Evidence={ECO:0000305|PubMed:30242642};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:04.760170+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 54-60",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3ecc50c16d349ff2fe2b86dd83a0288577ce5483563a520fae349796ac46e9a8",
  "url": "https://rest.uniprot.org/unisave/Q58T34?format=txt&versions=87"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q58T34?format=txt&versions=87)

```json
{
  "entry_version": 87,
  "evidence_id": "H5",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=beta-L-fucose 1-phosphate + GTP + H(+) = GDP-beta-L-fucose +\nCC         diphosphate; Xref=Rhea:RHEA:13549, ChEBI:CHEBI:15378,\nCC         ChEBI:CHEBI:33019, ChEBI:CHEBI:37565, ChEBI:CHEBI:57268,\nCC         ChEBI:CHEBI:57273; EC=2.7.7.30;\nCC         Evidence={ECO:0000269|PubMed:30242642};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:13550;\nCC         Evidence={ECO:0000305|PubMed:30242642};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:04.760170+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 61-68",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3ecc50c16d349ff2fe2b86dd83a0288577ce5483563a520fae349796ac46e9a8",
  "url": "https://rest.uniprot.org/unisave/Q58T34?format=txt&versions=87"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 16. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
