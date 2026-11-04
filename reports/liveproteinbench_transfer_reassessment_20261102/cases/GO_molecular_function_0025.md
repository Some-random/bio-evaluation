# GO_molecular_function_0025

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_molecular_function_0025.txt)

**Task:** `GO_molecular_function`  
**Expected answer:** **D** — fucokinase activity

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
A. potassium channel regulator activity
B. manganese ion transmembrane transporter activity
C. oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen
D. fucokinase activity
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

### Expected-answer support: supported

> The supplied sequence matches a 949-aa protein whose annotation identifies fucokinase activity with experimental evidence; the cited catalytic reaction is ATP-dependent phosphorylation of L-fucose. The enzyme is also annotated as bifunctional, but fucokinase activity is explicitly supported and matches option D.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C9](#evidence-c9).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The long sequence is consistent with a soluble, multidomain enzyme rather than a potassium-channel regulator or a membrane manganese transporter, which would require channel-associated or membrane-spanning features. Its enzyme-like architecture and nucleotide-binding/kinase-related features provide a transferable basis for favoring a sugar kinase such as fucokinase over the oxygen-dependent oxidoreductase in C. Recognition of the FKP-like two-activity enzyme family would further support D among these choices.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence and alternatives permit a meaningful family- and architecture-level inference without needing the exact protein’s database record. This is a probabilistic distinction, not proof of L-fucose substrate specificity from sequence alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although the protein has another annotated catalytic activity, guanylyltransferase activity is not an offered choice; D is the offered option supported by its fucokinase function.


### Important caveats

- The source evidence supports a bifunctional enzyme, so fucokinase is not necessarily its sole molecular function.
- The exact author source snapshot is unknown, but the supplied matched-sequence evidence includes experimental support for the fucokinase reaction.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The long sequence is consistent with a soluble, multidomain enzyme rather than a potassium-channel regulator or a membrane manganese transporter, which would require channel-associated or membrane-spanning features. Its enzyme-like architecture and nucleotide-binding/kinase-related features provide a transferable basis for favoring a sugar kinase such as fucokinase over the oxygen-dependent oxidoreductase in C. Recognition of the FKP-like two-activity enzyme family would further support D among these choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence and alternatives permit a meaningful family- and architecture-level inference without needing the exact protein’s database record. This is a probabilistic distinction, not proof of L-fucose substrate specificity from sequence alone."
  },
  "case_id": "GO_molecular_function_0025",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C9"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence matches a 949-aa protein whose annotation identifies fucokinase activity with experimental evidence; the cited catalytic reaction is ATP-dependent phosphorylation of L-fucose. The enzyme is also annotated as bifunctional, but fucokinase activity is explicitly supported and matches option D."
  },
  "important_caveats": [
    "The source evidence supports a bifunctional enzyme, so fucokinase is not necessarily its sole molecular function.",
    "The exact author source snapshot is unknown, but the supplied matched-sequence evidence includes experimental support for the fucokinase reaction."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the protein has another annotated catalytic activity, guanylyltransferase activity is not an offered choice; D is the offered option supported by its fucokinase function."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0025",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence matches a 949-aa protein whose annotation identifies fucokinase activity with experimental evidence; the cited catalytic reaction is ATP-dependent phosphorylation of L-fucose. The enzyme is also annotated as bifunctional, but fucokinase activity is explicitly supported and matches option D.",
    "evidence_ids": ["C5", "C6", "C9"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The long sequence is consistent with a soluble, multidomain enzyme rather than a potassium-channel regulator or a membrane manganese transporter, which would require channel-associated or membrane-spanning features. Its enzyme-like architecture and nucleotide-binding/kinase-related features provide a transferable basis for favoring a sugar kinase such as fucokinase over the oxygen-dependent oxidoreductase in C. Recognition of the FKP-like two-activity enzyme family would further support D among these choices.",
    "missing_item_specific_fact": "",
    "reason": "The sequence and alternatives permit a meaningful family- and architecture-level inference without needing the exact protein’s database record. This is a probabilistic distinction, not proof of L-fucose substrate specificity from sequence alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the protein has another annotated catalytic activity, guanylyltransferase activity is not an offered choice; D is the offered option supported by its fucokinase function."
  },
  "important_caveats": [
    "The source evidence supports a bifunctional enzyme, so fucokinase is not necessarily its sole molecular function.",
    "The exact author source snapshot is unknown, but the supplied matched-sequence evidence includes experimental support for the fucokinase reaction."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q58T34 (sequence matched, 949 aa, Bacteroides fragilis) is annotated with GO:0050201 (fucokinase activity) with EXP:UniProtKB evidence from PubMed:30242642, which reports experimental characterization including Cryo-EM structure (PDB 5YYS), catalytic activity assays, and mutagenesis. EC 2.7.1.52 (L-fucokinase) is confirmed experimentally. The protein is bifunctional (also has fucose-1-phosphate guanylyltransferase activity, EC 2.7.7.30), but fucokinase activity is one of its two catalytic functions and is the only matching option among the four choices.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C9](#evidence-c9), [C11](#evidence-c11), [H1](#evidence-h1), [H3](#evidence-h3), [H4](#evidence-h4), [H7](#evidence-h7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 949-aa protein lacks transmembrane segments, eliminating A (potassium channel regulator, typically a small membrane-associated protein) and B (manganese transporter, requires multiple TM helices). No heme-binding CxxCH or other redox-cofactor motifs are present, making C (EC 1.14 oxidoreductase) implausible. The sequence contains P-loop-like motifs (e.g., 'GKSGGG' near the N-terminus, multiple glycine-rich 'GGS'/'GK' stretches) characteristic of nucleotide-binding kinase domains in the GHMP/ribokinase superfamily. Among the four options, D (fucokinase activity, GO:0050201, a kinase) is the only one consistent with a soluble, large, glycine-rich nucleotide-binding enzyme. A model recognizing kinase-family P-loop architecture and the absence of membrane/redox features can meaningfully distinguish D from A, B, and C without knowing this specific protein's database entry.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable knowledge of protein family features (P-loop motifs indicating kinase, absence of TM segments, absence of heme motifs) combined with the structure of the four choices (only one kinase option) allows a knowledgeable model to select D by elimination and positive feature recognition.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The protein is a transferase (kinase + guanylyltransferase), not a channel regulator, transporter, or oxidoreductase. Among the four options, only D corresponds to an actual catalytic activity of this protein. The bifunctionality (guanylyltransferase activity also present) does not create ambiguity because that activity is not offered as an alternative choice.


### Important caveats

- The protein is bifunctional (fucokinase + fucose-1-phosphate guanylyltransferase); the question asks for 'primary molecular function' but the guanylyltransferase activity is not among the options, so this does not affect answerability.
- The P-loop motif recognition from sequence alone is suggestive but not definitive for the exact sub-family; however, since D is the only kinase option among the four, the level of specificity required is 'is this a kinase?' rather than 'which specific kinase?'
- The reviewer-only evidence confirms the identity as Q58T34 (FKP_BACFG), but this accession was not available to the evaluated model; the reasoning argument relies only on sequence features and general protein-family knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 949-aa protein lacks transmembrane segments, eliminating A (potassium channel regulator, typically a small membrane-associated protein) and B (manganese transporter, requires multiple TM helices). No heme-binding CxxCH or other redox-cofactor motifs are present, making C (EC 1.14 oxidoreductase) implausible. The sequence contains P-loop-like motifs (e.g., 'GKSGGG' near the N-terminus, multiple glycine-rich 'GGS'/'GK' stretches) characteristic of nucleotide-binding kinase domains in the GHMP/ribokinase superfamily. Among the four options, D (fucokinase activity, GO:0050201, a kinase) is the only one consistent with a soluble, large, glycine-rich nucleotide-binding enzyme. A model recognizing kinase-family P-loop architecture and the absence of membrane/redox features can meaningfully distinguish D from A, B, and C without knowing this specific protein's database entry.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge of protein family features (P-loop motifs indicating kinase, absence of TM segments, absence of heme motifs) combined with the structure of the four choices (only one kinase option) allows a knowledgeable model to select D by elimination and positive feature recognition."
  },
  "case_id": "GO_molecular_function_0025",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C9",
      "C11",
      "H1",
      "H3",
      "H4",
      "H7"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q58T34 (sequence matched, 949 aa, Bacteroides fragilis) is annotated with GO:0050201 (fucokinase activity) with EXP:UniProtKB evidence from PubMed:30242642, which reports experimental characterization including Cryo-EM structure (PDB 5YYS), catalytic activity assays, and mutagenesis. EC 2.7.1.52 (L-fucokinase) is confirmed experimentally. The protein is bifunctional (also has fucose-1-phosphate guanylyltransferase activity, EC 2.7.7.30), but fucokinase activity is one of its two catalytic functions and is the only matching option among the four choices."
  },
  "important_caveats": [
    "The protein is bifunctional (fucokinase + fucose-1-phosphate guanylyltransferase); the question asks for 'primary molecular function' but the guanylyltransferase activity is not among the options, so this does not affect answerability.",
    "The P-loop motif recognition from sequence alone is suggestive but not definitive for the exact sub-family; however, since D is the only kinase option among the four, the level of specificity required is 'is this a kinase?' rather than 'which specific kinase?'",
    "The reviewer-only evidence confirms the identity as Q58T34 (FKP_BACFG), but this accession was not available to the evaluated model; the reasoning argument relies only on sequence features and general protein-family knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein is a transferase (kinase + guanylyltransferase), not a channel regulator, transporter, or oxidoreductase. Among the four options, only D corresponds to an actual catalytic activity of this protein. The bifunctionality (guanylyltransferase activity also present) does not create ambiguity because that activity is not offered as an alternative choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0025",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q58T34 (sequence matched, 949 aa, Bacteroides fragilis) is annotated with GO:0050201 (fucokinase activity) with EXP:UniProtKB evidence from PubMed:30242642, which reports experimental characterization including Cryo-EM structure (PDB 5YYS), catalytic activity assays, and mutagenesis. EC 2.7.1.52 (L-fucokinase) is confirmed experimentally. The protein is bifunctional (also has fucose-1-phosphate guanylyltransferase activity, EC 2.7.7.30), but fucokinase activity is one of its two catalytic functions and is the only matching option among the four choices.",
    "evidence_ids": ["C4", "C5", "C6", "C9", "C11", "H1", "H3", "H4", "H7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 949-aa protein lacks transmembrane segments, eliminating A (potassium channel regulator, typically a small membrane-associated protein) and B (manganese transporter, requires multiple TM helices). No heme-binding CxxCH or other redox-cofactor motifs are present, making C (EC 1.14 oxidoreductase) implausible. The sequence contains P-loop-like motifs (e.g., 'GKSGGG' near the N-terminus, multiple glycine-rich 'GGS'/'GK' stretches) characteristic of nucleotide-binding kinase domains in the GHMP/ribokinase superfamily. Among the four options, D (fucokinase activity, GO:0050201, a kinase) is the only one consistent with a soluble, large, glycine-rich nucleotide-binding enzyme. A model recognizing kinase-family P-loop architecture and the absence of membrane/redox features can meaningfully distinguish D from A, B, and C without knowing this specific protein's database entry.",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge of protein family features (P-loop motifs indicating kinase, absence of TM segments, absence of heme motifs) combined with the structure of the four choices (only one kinase option) allows a knowledgeable model to select D by elimination and positive feature recognition."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein is a transferase (kinase + guanylyltransferase), not a channel regulator, transporter, or oxidoreductase. Among the four options, only D corresponds to an actual catalytic activity of this protein. The bifunctionality (guanylyltransferase activity also present) does not create ambiguity because that activity is not offered as an alternative choice."
  },
  "important_caveats": [
    "The protein is bifunctional (fucokinase + fucose-1-phosphate guanylyltransferase); the question asks for 'primary molecular function' but the guanylyltransferase activity is not among the options, so this does not affect answerability.",
    "The P-loop motif recognition from sequence alone is suggestive but not definitive for the exact sub-family; however, since D is the only kinase option among the four, the level of specificity required is 'is this a kinase?' rather than 'which specific kinase?'",
    "The reviewer-only evidence confirms the identity as Q58T34 (FKP_BACFG), but this accession was not available to the evaluated model; the reasoning argument relies only on sequence features and general protein-family knowledge."
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
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

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
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"30242642\",\"source\":\"PubMed\"}],\"value\":\"Bifunctional enzyme involved in the salvage pathway of GDP-fucose synthesis. Catalyzes two successive reactions, the ATP-dependent phosphorylation of L-fucose to L-fucose 1-phosphate, and its guanylylation to GDP-L-fucose. GDP-fucose is an important fucose donor in the process of fucosylated oligosaccharides formation\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
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

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q58T34.json)

```json
{
  "evidence_id": "C7",
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

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q58T34.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0005524\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:ATP binding\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:InterPro\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/18",
  "retrieved_utc": "2026-11-02T04:31:01.700323+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "613cb95f164460b198373fe8b1a0278d6f82b5f36a7ad73441bef68f5e41af74",
  "url": "https://rest.uniprot.org/uniprotkb/Q58T34.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q58T34.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"30242642\",\"source\":\"PubMed\"}],\"id\":\"GO:0050201\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:fucokinase activity\"},{\"key\":\"GoEvidenceType\",\"value\":\"EXP:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/19",
  "retrieved_utc": "2026-11-02T04:31:01.700323+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "613cb95f164460b198373fe8b1a0278d6f82b5f36a7ad73441bef68f5e41af74",
  "url": "https://rest.uniprot.org/uniprotkb/Q58T34.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q58T34.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"30242642\",\"source\":\"PubMed\"}],\"id\":\"GO:0047341\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:fucose-1-phosphate guanylyltransferase activity\"},{\"key\":\"GoEvidenceType\",\"value\":\"EXP:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/20",
  "retrieved_utc": "2026-11-02T04:31:01.700323+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "613cb95f164460b198373fe8b1a0278d6f82b5f36a7ad73441bef68f5e41af74",
  "url": "https://rest.uniprot.org/uniprotkb/Q58T34.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q58T34.json)

```json
{
  "evidence_id": "C11",
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

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q58T34?format=txt&versions=87)

```json
{
  "entry_version": 87,
  "evidence_id": "H3",
  "excerpt": "CC   -!- FUNCTION: Bifunctional enzyme involved in the salvage pathway of GDP-\nCC       fucose synthesis. Catalyzes two successive reactions, the ATP-dependent\nCC       phosphorylation of L-fucose to L-fucose 1-phosphate, and its\nCC       guanylylation to GDP-L-fucose. GDP-fucose is an important fucose donor\nCC       in the process of fucosylated oligosaccharides formation.\nCC       {ECO:0000269|PubMed:30242642}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:04.760170+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 48-53",
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

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q58T34?format=txt&versions=87)

```json
{
  "entry_version": 87,
  "evidence_id": "H6",
  "excerpt": "DR   GO; GO:0005524; F:ATP binding; IEA:UniProtKB-KW.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:04.760170+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 117-117",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3ecc50c16d349ff2fe2b86dd83a0288577ce5483563a520fae349796ac46e9a8",
  "url": "https://rest.uniprot.org/unisave/Q58T34?format=txt&versions=87"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q58T34?format=txt&versions=87)

```json
{
  "entry_version": 87,
  "evidence_id": "H7",
  "excerpt": "DR   GO; GO:0050201; F:fucokinase activity; IEA:UniProtKB-EC.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:04.760170+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 118-118",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3ecc50c16d349ff2fe2b86dd83a0288577ce5483563a520fae349796ac46e9a8",
  "url": "https://rest.uniprot.org/unisave/Q58T34?format=txt&versions=87"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q58T34?format=txt&versions=87)

```json
{
  "entry_version": 87,
  "evidence_id": "H8",
  "excerpt": "DR   GO; GO:0047341; F:fucose-1-phosphate guanylyltransferase activity; IEA:UniProtKB-EC.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:04.760170+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 119-119",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3ecc50c16d349ff2fe2b86dd83a0288577ce5483563a520fae349796ac46e9a8",
  "url": "https://rest.uniprot.org/unisave/Q58T34?format=txt&versions=87"
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
  "excerpt": "[Term]\nid: GO:0015459\nname: potassium channel regulator activity\nnamespace: molecular_function\ndef: \"Binds to and modulates the activity of a potassium channel.\" [GOC:dos, GOC:mah]\nsynonym: \"potassium channel gating activity\" EXACT []\nis_a: GO:0099106 ! ion channel regulator activity\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0015459",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 117999-118006",
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
  "excerpt": "[Term]\nid: GO:0016705\nname: oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen\nnamespace: molecular_function\ndef: \"Catalysis of an oxidation-reduction (redox) reaction in which hydrogen or electrons are transferred from each of two donors, and molecular oxygen is reduced or incorporated into a donor.\" [EC:1.14.-.-]\nsynonym: \"oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, miscellaneous\" NARROW []\nxref: EC:1.14.-.-\nxref: Reactome:R-HSA-5333612 \"MeSebGalNac is oxidatively cleaved to MeSeO2H and 2-acetamidoglucal\"\nis_a: GO:0016491 ! oxidoreductase activity\nproperty_value: skos:exactMatch EC:1.14.-.-\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0016705",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 129217-129227",
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
  "excerpt": "[Term]\nid: GO:0050201\nname: fucokinase activity\nnamespace: molecular_function\ndef: \"Catalysis of the reaction: L-fucose + ATP = beta-L-fucose 1-phosphate + ADP + 2 H+.\" [EC:2.7.1.52, RHEA:13241]\nsynonym: \"ATP:6-deoxy-L-galactose 1-phosphotransferase activity\" RELATED [EC:2.7.1.52]\nsynonym: \"ATP:beta-L-fucose 1-phosphotransferase activity\" RELATED [EC:2.7.1.52]\nsynonym: \"fucokinase (phosphorylating) activity\" RELATED [EC:2.7.1.52]\nsynonym: \"fucose kinase activity\" RELATED [EC:2.7.1.52]\nsynonym: \"L-fucokinase activity\" RELATED [EC:2.7.1.52]\nsynonym: \"L-fucose kinase activity\" RELATED [EC:2.7.1.52]\nxref: EC:2.7.1.52\nxref: KEGG_REACTION:R03161\nxref: MetaCyc:FUCOKINASE-RXN\nxref: Reactome:R-HSA-6787540 \"FCSK phosphorylates beta-Fuc to Fuc1P\"\nxref: RHEA:13241\nis_a: GO:0016301 ! kinase activity\nis_a: GO:0016773 ! phosphotransferase activity, alcohol group as acceptor\nproperty_value: skos:exactMatch EC:2.7.1.52\nproperty_value: skos:exactMatch RHEA:13241\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0050201",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 311181-311201",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 25. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
