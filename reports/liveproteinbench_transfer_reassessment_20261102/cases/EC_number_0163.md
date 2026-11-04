# EC_number_0163

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0163.txt)

**Task:** `EC_number`  
**Expected answer:** **C** — 2.7.1.52

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
A. 2.7.2.4
B. 3.2.2.5
C. 2.7.1.52
D. 2.7.8.43
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

> The sequence-matched UniProt record assigns EC 2.7.1.52 to the L-fucokinase activity, and its catalytic-activity annotation reports the corresponding fucose phosphorylation reaction with experimental evidence. The protein is also annotated with a second activity, EC 2.7.7.30.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 949-residue sequence has a long, multidomain architecture consistent with the bacterial bifunctional fucokinase/GDP-fucose pyrophosphorylase family: an N-terminal sugar-kinase region and a C-terminal nucleotide-sugar-forming region. Transferable knowledge of this family links its kinase activity to L-fucokinase, EC 2.7.1.52, making C meaningfully distinguishable from the unrelated reaction classes in the other choices.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The inference relies on family-level architecture and function shared with related proteins, not on recalling this exact protein's database entry. Sequence-based family recognition is probabilistic, but provides a meaningful basis for selecting C.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only C among the choices matches the experimentally annotated kinase activity. The protein is bifunctional and also has EC 2.7.7.30 activity, which is not offered; this caveat does not make another listed option defensible.


### Important caveats

- The evidence supports C as one activity of the protein, not as its only EC number.
- Reviewer-only source identity and annotations were not part of the original inputs.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 949-residue sequence has a long, multidomain architecture consistent with the bacterial bifunctional fucokinase/GDP-fucose pyrophosphorylase family: an N-terminal sugar-kinase region and a C-terminal nucleotide-sugar-forming region. Transferable knowledge of this family links its kinase activity to L-fucokinase, EC 2.7.1.52, making C meaningfully distinguishable from the unrelated reaction classes in the other choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The inference relies on family-level architecture and function shared with related proteins, not on recalling this exact protein's database entry. Sequence-based family recognition is probabilistic, but provides a meaningful basis for selecting C."
  },
  "case_id": "EC_number_0163",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns EC 2.7.1.52 to the L-fucokinase activity, and its catalytic-activity annotation reports the corresponding fucose phosphorylation reaction with experimental evidence. The protein is also annotated with a second activity, EC 2.7.7.30."
  },
  "important_caveats": [
    "The evidence supports C as one activity of the protein, not as its only EC number.",
    "Reviewer-only source identity and annotations were not part of the original inputs."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only C among the choices matches the experimentally annotated kinase activity. The protein is bifunctional and also has EC 2.7.7.30 activity, which is not offered; this caveat does not make another listed option defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0163",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns EC 2.7.1.52 to the L-fucokinase activity, and its catalytic-activity annotation reports the corresponding fucose phosphorylation reaction with experimental evidence. The protein is also annotated with a second activity, EC 2.7.7.30.",
    "evidence_ids": ["C5", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 949-residue sequence has a long, multidomain architecture consistent with the bacterial bifunctional fucokinase/GDP-fucose pyrophosphorylase family: an N-terminal sugar-kinase region and a C-terminal nucleotide-sugar-forming region. Transferable knowledge of this family links its kinase activity to L-fucokinase, EC 2.7.1.52, making C meaningfully distinguishable from the unrelated reaction classes in the other choices.",
    "missing_item_specific_fact": "",
    "reason": "The inference relies on family-level architecture and function shared with related proteins, not on recalling this exact protein's database entry. Sequence-based family recognition is probabilistic, but provides a meaningful basis for selecting C."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only C among the choices matches the experimentally annotated kinase activity. The protein is bifunctional and also has EC 2.7.7.30 activity, which is not offered; this caveat does not make another listed option defensible."
  },
  "important_caveats": [
    "The evidence supports C as one activity of the protein, not as its only EC number.",
    "Reviewer-only source identity and annotations were not part of the original inputs."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q58T34 (FKP_BACFG) for this exact sequence (949 aa, SHA256 matched) annotates EC 2.7.1.52 (L-fucokinase) with evidence code ECO:0000269 (direct experimental evidence from PubMed:30242642, a cryo-EM functional study). The catalytic reaction L-fucose + ATP → beta-L-fucose 1-phosphate + ADP + H+ is confirmed. The protein is bifunctional (also EC 2.7.7.30), but since 2.7.7.30 is not among the offered choices, EC 2.7.1.52 is the correct and supported answer.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains recognizable P-loop/Walker A motifs (e.g., 'GGGTSWL' near position 30, 'GAGGGGYLY' near position 870) indicating a nucleotide-binding kinase fold, which rules out EC 3.2.2.5 (a hydrolase, EC class 3). The ~949-aa length and two-domain architecture (kinase domain fused to a pyrophosphorylase domain, with motifs like 'GSGGGTSWL' and 'GGGWQDQYGG') is characteristic of bifunctional sugar-activating enzymes in nucleotide-sugar salvage pathways. Amino acid kinases (EC 2.7.2.x, e.g., glutamate 5-kinase) typically have distinct folds (e.g., NAGK-like or amino-acid-kinase fold) and do not fuse to pyrophosphorylase domains. Phosphotransferases to nitrogenous compounds (EC 2.7.8.x) also have structurally distinct architectures. The bifunctional kinase+pyrophosphorylase architecture is a hallmark of sugar-activation pathways (e.g., L-fucose salvage: kinase then guanylyltransferase), pointing to a sugar kinase (EC 2.7.1.x). Among the offered choices, only EC 2.7.1.52 is a sugar kinase (2.7.1 subclass, alcohol acceptor), making it the only option consistent with this architecture. While the argument does not specifically prove the substrate is L-fucose rather than another sugar, the question only offers one 2.7.1.x option, so the general 'sugar kinase' inference suffices to select C over A (amino acid kinase), B (hydrolase), and D (nitrogenous-acceptor kinase).


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable knowledge of kinase structural motifs (P-loop), domain architecture (bifunctional sugar-kinase/pyrophosphorylase), and the general principle that sugar-activating pathways use alcohol-group phosphotransferases (2.7.1.x) rather than carboxyl-group (2.7.2.x) or nitrogenous-compound (2.7.8.x) phosphotransferases provides a meaningful basis to distinguish C from the other three options. The argument is probabilistic and family-level but credibly eliminates the alternatives.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although the protein is bifunctional (EC 2.7.1.52 and EC 2.7.7.30), only EC 2.7.1.52 appears among the four offered choices. EC 2.7.7.30 is not listed, so there is no ambiguity among the provided alternatives. The other three options (2.7.2.4, 3.2.2.5, 2.7.8.43) are in different EC sub-subclasses or classes and are not defensible for this protein.


### Important caveats

- The protein is bifunctional with two EC numbers (2.7.1.52 and 2.7.7.30). The question asks for 'the complete 4-digit EC number' (singular), which is slightly imprecise for a bifunctional enzyme, but since only one of the two EC numbers is offered, this does not create ambiguity among the choices.
- The transferable argument distinguishes sugar kinase (2.7.1.x) from amino acid kinase (2.7.2.x), hydrolase (3.x.x.x), and nitrogenous-acceptor kinase (2.7.8.x) based on architecture and motifs, but does not specifically prove the substrate is L-fucose rather than another sugar. However, since only one 2.7.1.x option is offered, this level of discrimination is sufficient.
- The evidence code ECO:0000269 indicates direct experimental evidence (cryo-EM functional characterization, PubMed:30242642), lending strong support to the annotation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains recognizable P-loop/Walker A motifs (e.g., 'GGGTSWL' near position 30, 'GAGGGGYLY' near position 870) indicating a nucleotide-binding kinase fold, which rules out EC 3.2.2.5 (a hydrolase, EC class 3). The ~949-aa length and two-domain architecture (kinase domain fused to a pyrophosphorylase domain, with motifs like 'GSGGGTSWL' and 'GGGWQDQYGG') is characteristic of bifunctional sugar-activating enzymes in nucleotide-sugar salvage pathways. Amino acid kinases (EC 2.7.2.x, e.g., glutamate 5-kinase) typically have distinct folds (e.g., NAGK-like or amino-acid-kinase fold) and do not fuse to pyrophosphorylase domains. Phosphotransferases to nitrogenous compounds (EC 2.7.8.x) also have structurally distinct architectures. The bifunctional kinase+pyrophosphorylase architecture is a hallmark of sugar-activation pathways (e.g., L-fucose salvage: kinase then guanylyltransferase), pointing to a sugar kinase (EC 2.7.1.x). Among the offered choices, only EC 2.7.1.52 is a sugar kinase (2.7.1 subclass, alcohol acceptor), making it the only option consistent with this architecture. While the argument does not specifically prove the substrate is L-fucose rather than another sugar, the question only offers one 2.7.1.x option, so the general 'sugar kinase' inference suffices to select C over A (amino acid kinase), B (hydrolase), and D (nitrogenous-acceptor kinase).",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge of kinase structural motifs (P-loop), domain architecture (bifunctional sugar-kinase/pyrophosphorylase), and the general principle that sugar-activating pathways use alcohol-group phosphotransferases (2.7.1.x) rather than carboxyl-group (2.7.2.x) or nitrogenous-compound (2.7.8.x) phosphotransferases provides a meaningful basis to distinguish C from the other three options. The argument is probabilistic and family-level but credibly eliminates the alternatives."
  },
  "case_id": "EC_number_0163",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q58T34 (FKP_BACFG) for this exact sequence (949 aa, SHA256 matched) annotates EC 2.7.1.52 (L-fucokinase) with evidence code ECO:0000269 (direct experimental evidence from PubMed:30242642, a cryo-EM functional study). The catalytic reaction L-fucose + ATP → beta-L-fucose 1-phosphate + ADP + H+ is confirmed. The protein is bifunctional (also EC 2.7.7.30), but since 2.7.7.30 is not among the offered choices, EC 2.7.1.52 is the correct and supported answer."
  },
  "important_caveats": [
    "The protein is bifunctional with two EC numbers (2.7.1.52 and 2.7.7.30). The question asks for 'the complete 4-digit EC number' (singular), which is slightly imprecise for a bifunctional enzyme, but since only one of the two EC numbers is offered, this does not create ambiguity among the choices.",
    "The transferable argument distinguishes sugar kinase (2.7.1.x) from amino acid kinase (2.7.2.x), hydrolase (3.x.x.x), and nitrogenous-acceptor kinase (2.7.8.x) based on architecture and motifs, but does not specifically prove the substrate is L-fucose rather than another sugar. However, since only one 2.7.1.x option is offered, this level of discrimination is sufficient.",
    "The evidence code ECO:0000269 indicates direct experimental evidence (cryo-EM functional characterization, PubMed:30242642), lending strong support to the annotation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the protein is bifunctional (EC 2.7.1.52 and EC 2.7.7.30), only EC 2.7.1.52 appears among the four offered choices. EC 2.7.7.30 is not listed, so there is no ambiguity among the provided alternatives. The other three options (2.7.2.4, 3.2.2.5, 2.7.8.43) are in different EC sub-subclasses or classes and are not defensible for this protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0163",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q58T34 (FKP_BACFG) for this exact sequence (949 aa, SHA256 matched) annotates EC 2.7.1.52 (L-fucokinase) with evidence code ECO:0000269 (direct experimental evidence from PubMed:30242642, a cryo-EM functional study). The catalytic reaction L-fucose + ATP → beta-L-fucose 1-phosphate + ADP + H+ is confirmed. The protein is bifunctional (also EC 2.7.7.30), but since 2.7.7.30 is not among the offered choices, EC 2.7.1.52 is the correct and supported answer.",
    "evidence_ids": ["C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains recognizable P-loop/Walker A motifs (e.g., 'GGGTSWL' near position 30, 'GAGGGGYLY' near position 870) indicating a nucleotide-binding kinase fold, which rules out EC 3.2.2.5 (a hydrolase, EC class 3). The ~949-aa length and two-domain architecture (kinase domain fused to a pyrophosphorylase domain, with motifs like 'GSGGGTSWL' and 'GGGWQDQYGG') is characteristic of bifunctional sugar-activating enzymes in nucleotide-sugar salvage pathways. Amino acid kinases (EC 2.7.2.x, e.g., glutamate 5-kinase) typically have distinct folds (e.g., NAGK-like or amino-acid-kinase fold) and do not fuse to pyrophosphorylase domains. Phosphotransferases to nitrogenous compounds (EC 2.7.8.x) also have structurally distinct architectures. The bifunctional kinase+pyrophosphorylase architecture is a hallmark of sugar-activation pathways (e.g., L-fucose salvage: kinase then guanylyltransferase), pointing to a sugar kinase (EC 2.7.1.x). Among the offered choices, only EC 2.7.1.52 is a sugar kinase (2.7.1 subclass, alcohol acceptor), making it the only option consistent with this architecture. While the argument does not specifically prove the substrate is L-fucose rather than another sugar, the question only offers one 2.7.1.x option, so the general 'sugar kinase' inference suffices to select C over A (amino acid kinase), B (hydrolase), and D (nitrogenous-acceptor kinase).",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge of kinase structural motifs (P-loop), domain architecture (bifunctional sugar-kinase/pyrophosphorylase), and the general principle that sugar-activating pathways use alcohol-group phosphotransferases (2.7.1.x) rather than carboxyl-group (2.7.2.x) or nitrogenous-compound (2.7.8.x) phosphotransferases provides a meaningful basis to distinguish C from the other three options. The argument is probabilistic and family-level but credibly eliminates the alternatives."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the protein is bifunctional (EC 2.7.1.52 and EC 2.7.7.30), only EC 2.7.1.52 appears among the four offered choices. EC 2.7.7.30 is not listed, so there is no ambiguity among the provided alternatives. The other three options (2.7.2.4, 3.2.2.5, 2.7.8.43) are in different EC sub-subclasses or classes and are not defensible for this protein."
  },
  "important_caveats": [
    "The protein is bifunctional with two EC numbers (2.7.1.52 and 2.7.7.30). The question asks for 'the complete 4-digit EC number' (singular), which is slightly imprecise for a bifunctional enzyme, but since only one of the two EC numbers is offered, this does not create ambiguity among the choices.",
    "The transferable argument distinguishes sugar kinase (2.7.1.x) from amino acid kinase (2.7.2.x), hydrolase (3.x.x.x), and nitrogenous-acceptor kinase (2.7.8.x) based on architecture and motifs, but does not specifically prove the substrate is L-fucose rather than another sugar. However, since only one 2.7.1.x option is offered, this level of discrimination is sufficient.",
    "The evidence code ECO:0000269 indicates direct experimental evidence (cryo-EM functional characterization, PubMed:30242642), lending strong support to the annotation."
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

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 163. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
