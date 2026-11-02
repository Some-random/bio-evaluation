# GO_molecular_function_0096

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **B** — UDP-glucose 6-dehydrogenase activity

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | contradicted | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | contradicted | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MKDLKVAVVGLGYVGLPLAVEFGKKRTVVGFDINQGRIAELRQGIDSTLEVDAAELKEASELSFTFNLQDLQKCNVFIVTVPTPIDEHKQPDLTPLVKASESIGKVLKKGDIVIYESTVYPGATEEDCVPVLEKFSGLRFNEDFFAGYSPERINPGDKEHRVSSIKKVTSGSTPEIAELVDSLYREIITAGTHKASSIKVAEAAKVIENTQRDLNIALINELAIIFNRMGIDTEAVLKAAGTKWNFMPFRPGLVGGHCIGVDPYYLTHKAQSIGYHPEIILAGRRLNDGMGAYVVSQLVKAMLKRRIHVDGARVLLMGLTFKENCPDLRNTKVVDIVRELAEYNIQVDVFDPWVSAEDAMHEYGITPVGTPSHGAYDGIILAVAHSEFKNMGAENIRKLGKAEHVLYDLKYLLDEDKSDLRL

[Multiple Choices]
A. 4 iron, 4 sulfur cluster binding
B. UDP-glucose 6-dehydrogenase activity
C. DNA-binding transcription factor binding
D. thioredoxin peroxidase activity
```

<details>
<summary>Original system instructions, verbatim</summary>

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

## GPT-6 Luna

**Saved status:** `valid_review`.

### Expected-answer support: contradicted

> The sequence-matched entry identifies this protein as UDP-N-acetylglucosamine 6-dehydrogenase (EC 1.1.1.136), experimentally annotated for UDP-GlcNAc conversion—not UDP-glucose 6-dehydrogenase (EC 1.1.1.22), which is the reaction specified by choice B.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C9](#evidence-c9), [GO1](#evidence-go1).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is compatible with a nucleotide-sugar dehydrogenase, making B a superficially plausible option, but general reasoning from the sequence does not establish the particular sugar substrate.


**Missing item-specific fact**

> The protein-specific substrate and reaction assignment: UDP-GlcNAc, rather than UDP-glucose, is the experimentally annotated substrate.


**Reason**

> Distinguishing the near-related UDP-sugar dehydrogenase activities requires protein-specific functional annotation or experimental substrate evidence absent from the input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supported specific activity is not listed. B is the closest-looking option but names a different substrate and reaction; the evidence does not establish that another listed choice fits.


### Important caveats

- The reviewer-only UniProt records match the supplied sequence and include experimental evidence for UDP-GlcNAc dehydrogenase activity.
- The cited evidence does not explicitly report a negative assay for UDP-glucose, so it does not rule out every possible side activity; it does not support B as the protein's primary activity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is compatible with a nucleotide-sugar dehydrogenase, making B a superficially plausible option, but general reasoning from the sequence does not establish the particular sugar substrate.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific substrate and reaction assignment: UDP-GlcNAc, rather than UDP-glucose, is the experimentally annotated substrate.",
    "reason": "Distinguishing the near-related UDP-sugar dehydrogenase activities requires protein-specific functional annotation or experimental substrate evidence absent from the input."
  },
  "case_id": "GO_molecular_function_0096",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C9",
      "GO1"
    ],
    "judgment": "contradicted",
    "reason": "The sequence-matched entry identifies this protein as UDP-N-acetylglucosamine 6-dehydrogenase (EC 1.1.1.136), experimentally annotated for UDP-GlcNAc conversion—not UDP-glucose 6-dehydrogenase (EC 1.1.1.22), which is the reaction specified by choice B."
  },
  "important_caveats": [
    "The reviewer-only UniProt records match the supplied sequence and include experimental evidence for UDP-GlcNAc dehydrogenase activity.",
    "The cited evidence does not explicitly report a negative assay for UDP-glucose, so it does not rule out every possible side activity; it does not support B as the protein's primary activity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supported specific activity is not listed. B is the closest-looking option but names a different substrate and reaction; the evidence does not establish that another listed choice fits."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0096",
  "expected_answer_check": {
    "judgment": "contradicted",
    "reason": "The sequence-matched entry identifies this protein as UDP-N-acetylglucosamine 6-dehydrogenase (EC 1.1.1.136), experimentally annotated for UDP-GlcNAc conversion—not UDP-glucose 6-dehydrogenase (EC 1.1.1.22), which is the reaction specified by choice B.",
    "evidence_ids": ["C4", "C5", "C6", "C9", "GO1"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is compatible with a nucleotide-sugar dehydrogenase, making B a superficially plausible option, but general reasoning from the sequence does not establish the particular sugar substrate.",
    "missing_item_specific_fact": "The protein-specific substrate and reaction assignment: UDP-GlcNAc, rather than UDP-glucose, is the experimentally annotated substrate.",
    "reason": "Distinguishing the near-related UDP-sugar dehydrogenase activities requires protein-specific functional annotation or experimental substrate evidence absent from the input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supported specific activity is not listed. B is the closest-looking option but names a different substrate and reaction; the evidence does not establish that another listed choice fits."
  },
  "important_caveats": [
    "The reviewer-only UniProt records match the supplied sequence and include experimental evidence for UDP-GlcNAc dehydrogenase activity.",
    "The cited evidence does not explicitly report a negative assay for UDP-glucose, so it does not rule out every possible side activity; it does not support B as the protein's primary activity."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: contradicted

> The UniProt entry Q9RHD7 (WbpO, Pseudomonas aeruginosa) is experimentally annotated (ECO:0000269, PubMed:18065759) as UDP-N-acetyl-D-glucosamine 6-dehydrogenase (EC 1.1.1.136, GO:0047004), catalyzing UDP-GlcNAc → UDP-GlcNAcA. The expected answer B specifies 'UDP-glucose 6-dehydrogenase activity' (GO:0003979, EC 1.1.1.22), which acts on UDP-glucose → UDP-glucuronate. These are distinct EC numbers, distinct GO terms, and distinct substrates. The protein's annotated catalytic activity (C6, C9) is GO:0047004, not GO:0003979. No evidence in the entry supports activity on UDP-glucose. B is the closest option among the four but is technically incorrect for this protein.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C9](#evidence-c9), [H6](#evidence-h6), [H7](#evidence-h7), [H10](#evidence-h10), [GO1](#evidence-go1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 422-aa sequence contains an N-terminal Rossmann-fold motif (GLGYVGL at positions ~10-16, GxGxxG pattern) characteristic of NAD(P)-dependent dehydrogenases/oxidoreductases. It lacks CxxCxxxxC cysteine motifs diagnostic of 4Fe-4S cluster binding (eliminates A), lacks thioredoxin/peroxiredoxin signatures (small ~200-250 aa, CxxC peroxidatic cysteine; eliminates D), and lacks any DNA-binding or transcription-factor-interaction domains (eliminates C). Among the four options, only B describes an oxidoreductase/dehydrogenase activity, which is the only class consistent with the Rossmann-fold architecture. A model recognizing the NAD-binding fold can eliminate A, C, and D and select B.


**Missing item-specific fact**

> The exact substrate specificity (UDP-GlcNAc vs UDP-glucose) cannot be determined from sequence alone; however, this distinction is irrelevant to selecting B over A/C/D since B is the only dehydrogenase option.


**Reason**

> The sequence's Rossmann-fold NAD-binding motif and overall dehydrogenase architecture provide a concrete biological argument to select the sole oxidoreductase option (B) over Fe-S binding (A), TF binding (C), and peroxidase activity (D). The imprecision in the substrate name within option B does not prevent reasoning-based discrimination among the four choices.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A, C, and D are clearly incompatible with the sequence features (no Fe-S motifs, no DNA-binding domains, no peroxidase/thioredoxin architecture). B is the only dehydrogenase option and is the sole defensible choice, despite its imprecise substrate name (UDP-glucose vs UDP-N-acetylglucosamine).


### Important caveats

- The expected answer text 'UDP-glucose 6-dehydrogenase activity' (GO:0003979, EC 1.1.1.22) does not match the protein's actual annotated activity 'UDP-N-acetylglucosamine 6-dehydrogenase activity' (GO:0047004, EC 1.1.1.136). These are related but distinct enzymes in the UDP-sugar dehydrogenase family.
- The expected answer is the best available option among the four distractors but is technically a misannotation of the specific substrate. A more precise option would read 'UDP-N-acetylglucosamine 6-dehydrogenase activity.'
- The sequence match is confirmed (SHA256 identical, 422 aa) between the benchmark input and UniProt Q9RHD7.
- The GO annotation for the correct term (GO:0047004) carries EXP evidence (PubMed:18065759), making it experimentally established rather than purely computational.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 422-aa sequence contains an N-terminal Rossmann-fold motif (GLGYVGL at positions ~10-16, GxGxxG pattern) characteristic of NAD(P)-dependent dehydrogenases/oxidoreductases. It lacks CxxCxxxxC cysteine motifs diagnostic of 4Fe-4S cluster binding (eliminates A), lacks thioredoxin/peroxiredoxin signatures (small ~200-250 aa, CxxC peroxidatic cysteine; eliminates D), and lacks any DNA-binding or transcription-factor-interaction domains (eliminates C). Among the four options, only B describes an oxidoreductase/dehydrogenase activity, which is the only class consistent with the Rossmann-fold architecture. A model recognizing the NAD-binding fold can eliminate A, C, and D and select B.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The exact substrate specificity (UDP-GlcNAc vs UDP-glucose) cannot be determined from sequence alone; however, this distinction is irrelevant to selecting B over A/C/D since B is the only dehydrogenase option.",
    "reason": "The sequence's Rossmann-fold NAD-binding motif and overall dehydrogenase architecture provide a concrete biological argument to select the sole oxidoreductase option (B) over Fe-S binding (A), TF binding (C), and peroxidase activity (D). The imprecision in the substrate name within option B does not prevent reasoning-based discrimination among the four choices."
  },
  "case_id": "GO_molecular_function_0096",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C9",
      "H6",
      "H7",
      "H10",
      "GO1"
    ],
    "judgment": "contradicted",
    "reason": "The UniProt entry Q9RHD7 (WbpO, Pseudomonas aeruginosa) is experimentally annotated (ECO:0000269, PubMed:18065759) as UDP-N-acetyl-D-glucosamine 6-dehydrogenase (EC 1.1.1.136, GO:0047004), catalyzing UDP-GlcNAc → UDP-GlcNAcA. The expected answer B specifies 'UDP-glucose 6-dehydrogenase activity' (GO:0003979, EC 1.1.1.22), which acts on UDP-glucose → UDP-glucuronate. These are distinct EC numbers, distinct GO terms, and distinct substrates. The protein's annotated catalytic activity (C6, C9) is GO:0047004, not GO:0003979. No evidence in the entry supports activity on UDP-glucose. B is the closest option among the four but is technically incorrect for this protein."
  },
  "important_caveats": [
    "The expected answer text 'UDP-glucose 6-dehydrogenase activity' (GO:0003979, EC 1.1.1.22) does not match the protein's actual annotated activity 'UDP-N-acetylglucosamine 6-dehydrogenase activity' (GO:0047004, EC 1.1.1.136). These are related but distinct enzymes in the UDP-sugar dehydrogenase family.",
    "The expected answer is the best available option among the four distractors but is technically a misannotation of the specific substrate. A more precise option would read 'UDP-N-acetylglucosamine 6-dehydrogenase activity.'",
    "The sequence match is confirmed (SHA256 identical, 422 aa) between the benchmark input and UniProt Q9RHD7.",
    "The GO annotation for the correct term (GO:0047004) carries EXP evidence (PubMed:18065759), making it experimentally established rather than purely computational."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, C, and D are clearly incompatible with the sequence features (no Fe-S motifs, no DNA-binding domains, no peroxidase/thioredoxin architecture). B is the only dehydrogenase option and is the sole defensible choice, despite its imprecise substrate name (UDP-glucose vs UDP-N-acetylglucosamine)."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0096",
  "expected_answer_check": {
    "judgment": "contradicted",
    "reason": "The UniProt entry Q9RHD7 (WbpO, Pseudomonas aeruginosa) is experimentally annotated (ECO:0000269, PubMed:18065759) as UDP-N-acetyl-D-glucosamine 6-dehydrogenase (EC 1.1.1.136, GO:0047004), catalyzing UDP-GlcNAc → UDP-GlcNAcA. The expected answer B specifies 'UDP-glucose 6-dehydrogenase activity' (GO:0003979, EC 1.1.1.22), which acts on UDP-glucose → UDP-glucuronate. These are distinct EC numbers, distinct GO terms, and distinct substrates. The protein's annotated catalytic activity (C6, C9) is GO:0047004, not GO:0003979. No evidence in the entry supports activity on UDP-glucose. B is the closest option among the four but is technically incorrect for this protein.",
    "evidence_ids": ["C4", "C5", "C6", "C9", "H6", "H7", "H10", "GO1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 422-aa sequence contains an N-terminal Rossmann-fold motif (GLGYVGL at positions ~10-16, GxGxxG pattern) characteristic of NAD(P)-dependent dehydrogenases/oxidoreductases. It lacks CxxCxxxxC cysteine motifs diagnostic of 4Fe-4S cluster binding (eliminates A), lacks thioredoxin/peroxiredoxin signatures (small ~200-250 aa, CxxC peroxidatic cysteine; eliminates D), and lacks any DNA-binding or transcription-factor-interaction domains (eliminates C). Among the four options, only B describes an oxidoreductase/dehydrogenase activity, which is the only class consistent with the Rossmann-fold architecture. A model recognizing the NAD-binding fold can eliminate A, C, and D and select B.",
    "missing_item_specific_fact": "The exact substrate specificity (UDP-GlcNAc vs UDP-glucose) cannot be determined from sequence alone; however, this distinction is irrelevant to selecting B over A/C/D since B is the only dehydrogenase option.",
    "reason": "The sequence's Rossmann-fold NAD-binding motif and overall dehydrogenase architecture provide a concrete biological argument to select the sole oxidoreductase option (B) over Fe-S binding (A), TF binding (C), and peroxidase activity (D). The imprecision in the substrate name within option B does not prevent reasoning-based discrimination among the four choices."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, C, and D are clearly incompatible with the sequence features (no Fe-S motifs, no DNA-binding domains, no peroxidase/thioredoxin architecture). B is the only dehydrogenase option and is the sole defensible choice, despite its imprecise substrate name (UDP-glucose vs UDP-N-acetylglucosamine)."
  },
  "important_caveats": [
    "The expected answer text 'UDP-glucose 6-dehydrogenase activity' (GO:0003979, EC 1.1.1.22) does not match the protein's actual annotated activity 'UDP-N-acetylglucosamine 6-dehydrogenase activity' (GO:0047004, EC 1.1.1.136). These are related but distinct enzymes in the UDP-sugar dehydrogenase family.",
    "The expected answer is the best available option among the four distractors but is technically a misannotation of the specific substrate. A more precise option would read 'UDP-N-acetylglucosamine 6-dehydrogenase activity.'",
    "The sequence match is confirmed (SHA256 identical, 422 aa) between the benchmark input and UniProt Q9RHD7.",
    "The GO annotation for the correct term (GO:0047004) carries EXP evidence (PubMed:18065759), making it experimentally established rather than purely computational."
  ]
}
```

</details>

## Existing project source checks of Luna’s review

The notes below were prepared for specific claims in the Luna review. They are not independent validation of Qwen’s claims, expert adjudication, or replacement verdicts.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

### Source check 1

**Check:** `reaction_substrate_difference_traced`.

> C4-C6/C9 identify UDP-N-acetylglucosamine oxidation (EC1.1.1.136); GO1 defines UDP-glucose oxidation (EC1.1.1.22).

**Remaining uncertainty:** The N-acetyl substrate distinction is present in source names and reactions. Lack of UDP-glucose activity is not independently assayed in the provided fields.

Evidence checked: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C9](#evidence-c9), [GO1](#evidence-go1).

## Reviewer-only source evidence

**Both reviewers received this source evidence separately from the original question. It was not available to the original evaluated model.** Source support and reasoning from the original sequence/choices are distinct assessments.

**Accession:** `Q9RHD7` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 111. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9RHD7.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:27.130209+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"18065759","source":"PubMed"}],"value":"1.1.1.136"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"UDP-N-acetyl-D-glucosamine 6-dehydrogenase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"UDP-GlcNAc 6-dehydrogenase"}]}}
```

Source SHA-256: `9908d3a1c42951cf34f5af4acef817be24931c868b8047c883d1accce98092cd`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9RHD7.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:27.130209+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"10627048","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"10931835","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"18065759","source":"PubMed"}],"value":"Dehydrogenase required for the biosynthesis of the B-band O antigen of serotype O6 lipopolysaccharide (PubMed:10627048). Is also required for flagellin glycosylation (PubMed:18065759). Catalyzes the conversion of UDP-N-acetylglucosamine (UDP-GlcNAc) to UDP-N-acetylglucosaminuronic acid (UDP-GlcNAcA) (PubMed:18065759). Can also catalyze the conversion of UDP-N-acetyl-galactosamine (UDP-GalNAc) to UDP-N-acetylgalactosaminuronic acid (UDP-GalNAcA), with low efficiency (PubMed:10931835, PubMed:18065759). Can use NAD(+) or NADP(+), with a preference for NAD(+) (PubMed:18065759)"}]}
```

Source SHA-256: `9908d3a1c42951cf34f5af4acef817be24931c868b8047c883d1accce98092cd`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9RHD7.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:27.130209+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"18065759","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:13326"}}],"reaction":{"ecNumber":"1.1.1.136","evidences":[{"evidenceCode":"ECO:0000269","id":"18065759","source":"PubMed"}],"name":"UDP-N-acetyl-alpha-D-glucosamine + 2 NAD(+) + H2O = UDP-2-acetamido-2-deoxy-alpha-D-glucuronate + 2 NADH + 3 H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:13325"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:57540"},{"database":"ChEBI","id":"CHEBI:57705"},{"database":"ChEBI","id":"CHEBI:57945"},{"database":"ChEBI","id":"CHEBI:65040"}]}}
```

Source SHA-256: `9908d3a1c42951cf34f5af4acef817be24931c868b8047c883d1accce98092cd`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9RHD7.json)  
**Locator:** `/uniProtKBCrossReferences/11`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:27.130209+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000269","id":"18065759","source":"PubMed"}],"id":"GO:0047004","properties":[{"key":"GoTerm","value":"F:UDP-N-acetylglucosamine 6-dehydrogenase activity"},{"key":"GoEvidenceType","value":"EXP:UniProtKB"}]}
```

Source SHA-256: `9908d3a1c42951cf34f5af4acef817be24931c868b8047c883d1accce98092cd`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9RHD7?format=txt&versions=111)  
**Locator:** `lines 57-66`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 111 / 1.  
**Retrieved:** 2026-11-01T06:28:50.339116+00:00.  

```text
CC   -!- FUNCTION: Dehydrogenase required for the biosynthesis of the B-band O
CC       antigen of serotype O6 lipopolysaccharide (PubMed:10627048). Is also
CC       required for flagellin glycosylation (PubMed:18065759). Catalyzes the
CC       conversion of UDP-N-acetylglucosamine (UDP-GlcNAc) to UDP-N-
CC       acetylglucosaminuronic acid (UDP-GlcNAcA) (PubMed:18065759). Can also
CC       catalyze the conversion of UDP-N-acetyl-galactosamine (UDP-GalNAc) to
CC       UDP-N-acetylgalactosaminuronic acid (UDP-GalNAcA), with low efficiency
CC       (PubMed:10931835, PubMed:18065759). Can use NAD(+) or NADP(+), with a
CC       preference for NAD(+) (PubMed:18065759). {ECO:0000269|PubMed:10627048,
CC       ECO:0000269|PubMed:10931835, ECO:0000269|PubMed:18065759}.
```

Source SHA-256: `f7af1f7da3cb8c76a5dd5a6f0015938a765ca8f2ee11a77d973637afedcc3462`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9RHD7?format=txt&versions=111)  
**Locator:** `lines 67-75`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 111 / 1.  
**Retrieved:** 2026-11-01T06:28:50.339116+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=UDP-N-acetyl-alpha-D-glucosamine + 2 NAD(+) + H2O = UDP-2-
CC         acetamido-2-deoxy-alpha-D-glucuronate + 2 NADH + 3 H(+);
CC         Xref=Rhea:RHEA:13325, ChEBI:CHEBI:15377, ChEBI:CHEBI:15378,
CC         ChEBI:CHEBI:57540, ChEBI:CHEBI:57705, ChEBI:CHEBI:57945,
CC         ChEBI:CHEBI:65040; EC=1.1.1.136;
CC         Evidence={ECO:0000269|PubMed:18065759};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:13326;
CC         Evidence={ECO:0000269|PubMed:18065759};
```

Source SHA-256: `f7af1f7da3cb8c76a5dd5a6f0015938a765ca8f2ee11a77d973637afedcc3462`.

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9RHD7?format=txt&versions=111)  
**Locator:** `lines 146-146`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 111 / 1.  
**Retrieved:** 2026-11-01T06:28:50.339116+00:00.  

```text
DR   GO; GO:0047004; F:UDP-N-acetylglucosamine 6-dehydrogenase activity; IEA:UniProtKB-EC.
```

Source SHA-256: `f7af1f7da3cb8c76a5dd5a6f0015938a765ca8f2ee11a77d973637afedcc3462`.

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 32563-32576`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0003979
name: UDP-glucose 6-dehydrogenase activity
namespace: molecular_function
def: "Catalysis of the reaction: H2O + 2 NAD+ + UDP-alpha-D-glucose = 3 H+ + 2 NADH + UDP-alpha-D-glucuronate." [EC:1.1.1.22, RHEA:23596]
xref: EC:1.1.1.22
xref: KEGG_REACTION:R00286
xref: MetaCyc:UGD-RXN
xref: Reactome:R-HSA-173597 "UDP-glucose is oxidised to UDP-glucuronate"
xref: RHEA:23596
is_a: GO:0016616 ! oxidoreductase activity, acting on the CH-OH group of donors, NAD or NADP as acceptor
property_value: skos:exactMatch EC:1.1.1.22
property_value: skos:exactMatch RHEA:23596

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 96. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
