# cofactor_0144: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/cofactor_0144.txt)

**Task:** `cofactor`  
**Author key, unchanged:** **A** — Mn(2+)

| Round | Reviewer | Key support | Transfer / lookup | Output usability (canonical status) |
|---|---|---|---|---|
| before | GPT-6 Luna | supported | lookup-dependent | usable output (valid_review) |
| before | Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | usable output (valid_review) |
| after | GPT-6 Luna | supported | reasoning-supported | usable output (valid_review) |
| after | Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | usable output (valid_review) |

**Usable output means format-valid review, not reasoning-supported or biologically correct.** A usable output can classify the question as reasoning-supported, lookup-dependent or uncertain. An output error is a problem with the saved model response; it does not count a defective benchmark question or wrong key. Each saved review is retained in full below. Labels from output errors are displayed as saved and excluded from label statistics. The author key and reviewer evidence were visible to reviewers; this is a review of answerability and key support, not a benchmark-solving score.

## Complete original question

```text
[Protein Sequence]
MQKLLSLPSNLVQSFHELERVNRTDWFCTSDPVGKKLGSGGGTSWLLEECYNEYSDGATFGEWLEKEKRILLHAGGQSRRLPGYAPSGKILTPVPVFRWERGQHLGQNLLSLQLPLYEKIMSLAPDKLHTLIASGDVYIRSEKPLQSIPEADVVCYGLWVDPSLATHHGVFASDRKHPEQLDFMLQKPSLAELESLSKTHLFLMDIGIWLLSDRAVEILMKRSHKESSEELKYYDLYSDFGLALGTHPRIEDEEVNTLSVAILPLPGGEFYHYGTSKELISSTLSVQNKVYDQRRIMHRKVKPNPAMFVQNAVVRIPLCAENADLWIENSHIGPKWKIASRHIITGVPENDWSLAVPAGVCVDVVPMGDKGFVARPYGLDDVFKGDLRDSKTTLTGIPFGEWMSKRGLSYTDLKGRTDDLQAVSVFPMVNSVEELGLVLRWMLSEPELEEGKNIWLRSEHFSADEISAGANLKRLYAQREEFRKGNWKALAVNHEKSVFYQLDLADAAEDFVRLGLDMPELLPEDALQMSRIHNRMLRARILKLDGKDYRPEEQAAFDLLRDGLLDGISNRKSTPKLDVYSDQIVWGRSPVRIDMAGGWTDTPPYSLYSGGNVVNLAIELNGQPPLQVYVKPCKDFHIVLRSIDMGAMEIVSTFDELQDYKKIGSPFSIPKAALSLAGFAPAFSAVSYASLEEQLKDFGAGIEVTLLAAIPAGSGLGTSSILASTVLGAINDFCGLAWDKNEICQRTLVLEQLLTTGGGWQDQYGGVLQGVKLLQTEAGFAQSPLVRWLPDHLFTHPEYKDCHLLYYTGITRTAKGILAEIVSSMFLNSSLHLNLLSEMKAHALDMNEAIQRGSFVEFGRLVGKTWEQNKALDSGTNPPAVEAIIDLIKDYTLGYKLPGAGGGGYLYMVAKDPQAAVRIRKILTENAPNPRARFVEMTLSDKGFQVSRS

[Multiple Choices]
A. Mn(2+)
B. NAD(+)
C. Na(+)
D. Zn(2+)
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Predicting Protein Cofactor, which is to identify the specific cofactor required for a given protein's catalytic activity. A cofactor is a non-protein chemical compound or metallic ion that is essential for an enzyme's function. Based on the provided protein sequence, you will need to determine which of the multiple-choice options is the correct cofactor.. The inputs provided by the user for this task include:

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

## Four saved visible reviews

## Before: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched UniProt entry annotates Mn(2+) as a cofactor and says the L-fucokinase activity requires divalent cations such as Mn(2+) and Mg(2+). This supports A, though the annotation is transferred from another UniProt entry rather than direct experimental evidence for this sequence.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The protein's kinase and pyrophosphorylase activities make a divalent metal cofactor biologically plausible, but that general inference does not establish that this particular protein uses Mn(2+) rather than another metal.


**Missing item-specific fact**

> The protein-specific cofactor annotation that Mn(2+) is among the divalent cations supporting its L-fucokinase activity.


**Reason**

> The sequence alone does not supply functional annotation or experimental cofactor measurements. Selecting Mn(2+) over the other choices depends on an item-specific annotation or equivalent protein-specific knowledge.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed choices, Mn(2+) is supported by the annotation. However, the annotation also identifies Mg(2+) as a required divalent cation, and Mg(2+) is not offered.


### Important caveats

- The Mn(2+) and Mg(2+) annotations are transferred by similarity (ECO:0000250), not shown here to be direct experimental measurements for the supplied protein.
- The source sequence matches the supplied sequence; the cited annotation describes both L-fucokinase and GDP-fucose pyrophosphorylase activities.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The protein's kinase and pyrophosphorylase activities make a divalent metal cofactor biologically plausible, but that general inference does not establish that this particular protein uses Mn(2+) rather than another metal.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific cofactor annotation that Mn(2+) is among the divalent cations supporting its L-fucokinase activity.",
    "reason": "The sequence alone does not supply functional annotation or experimental cofactor measurements. Selecting Mn(2+) over the other choices depends on an item-specific annotation or equivalent protein-specific knowledge."
  },
  "case_id": "cofactor_0144",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry annotates Mn(2+) as a cofactor and says the L-fucokinase activity requires divalent cations such as Mn(2+) and Mg(2+). This supports A, though the annotation is transferred from another UniProt entry rather than direct experimental evidence for this sequence."
  },
  "important_caveats": [
    "The Mn(2+) and Mg(2+) annotations are transferred by similarity (ECO:0000250), not shown here to be direct experimental measurements for the supplied protein.",
    "The source sequence matches the supplied sequence; the cited annotation describes both L-fucokinase and GDP-fucose pyrophosphorylase activities."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, Mn(2+) is supported by the annotation. However, the annotation also identifies Mg(2+) as a required divalent cation, and Mg(2+) is not offered."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0144",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry annotates Mn(2+) as a cofactor and says the L-fucokinase activity requires divalent cations such as Mn(2+) and Mg(2+). This supports A, though the annotation is transferred from another UniProt entry rather than direct experimental evidence for this sequence.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The protein's kinase and pyrophosphorylase activities make a divalent metal cofactor biologically plausible, but that general inference does not establish that this particular protein uses Mn(2+) rather than another metal.",
    "missing_item_specific_fact": "The protein-specific cofactor annotation that Mn(2+) is among the divalent cations supporting its L-fucokinase activity.",
    "reason": "The sequence alone does not supply functional annotation or experimental cofactor measurements. Selecting Mn(2+) over the other choices depends on an item-specific annotation or equivalent protein-specific knowledge."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, Mn(2+) is supported by the annotation. However, the annotation also identifies Mg(2+) as a required divalent cation, and Mg(2+) is not offered."
  },
  "important_caveats": [
    "The Mn(2+) and Mg(2+) annotations are transferred by similarity (ECO:0000250), not shown here to be direct experimental measurements for the supplied protein.",
    "The source sequence matches the supplied sequence; the cited annotation describes both L-fucokinase and GDP-fucose pyrophosphorylase activities."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q58T34 (FKP_BACFG, L-fucokinase/L-fucose-1-P guanylyltransferase from Bacteroides fragilis) annotates Mn(2+) as a required cofactor for the L-fucokinase activity (ECO:0000250, similarity-based inference from Q9LNJ9). The note states: 'The L-fucokinase activity absolutely requires divalent cations such as Mn(2+) and Mg(2+).' Mg(2+) is also listed but is not among the four answer choices. Among the provided options (Mn2+, NAD+, Na+, Zn2+), only Mn(2+) appears in the cofactor annotation. The evidence code is similarity-based rather than direct experimental proof for this specific protein, but the annotation nonetheless supports the key.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4), [C4](#evidence-c4), [C1](#evidence-c1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The four choices span distinct cofactor classes: NAD(+) is a hydride-transfer cofactor for dehydrogenases; Na(+) is a monovalent ion not typically a catalytic cofactor; Zn(2+) is characteristic of metalloproteases, carbonic anhydrases, and certain dehydrogenases; Mn(2+) is a divalent cation used by kinases to coordinate the β- and γ-phosphates of ATP. Recognizing the protein as a sugar kinase (the sequence contains glycine-rich stretches such as 'GSGGGTSWL' suggestive of a nucleotide-binding/P-loop region, and the overall architecture is consistent with a multi-domain transferase) allows elimination of NAD+, Na+, and Zn(2+), leaving Mn(2+) as the only plausible kinase cofactor among the options. Even without full sequence recognition, the elimination logic—kinases need divalent cations for phosphate coordination, and among the four choices only Mn(2+) fits—provides a defensible general-biology argument.


**Missing item-specific fact**

> None that is essential. The specific annotation confirming Mn(2+) for this exact protein is similarity-based (ECO:0000250), but the reasoning from enzyme-class cofactor preferences is sufficient to select Mn(2+) over the three clearly inappropriate distractors.


**Reason**

> General knowledge of kinase cofactor requirements (divalent cations for ATP phosphate coordination) meaningfully distinguishes Mn(2+) from NAD+ (dehydrogenase cofactor), Na+ (non-catalytic monovalent ion), and Zn(2+) (metalloprotease/dehydrogenase cofactor). The glycine-rich motifs in the sequence provide weak but real structural hints toward a nucleotide-binding/kinase fold. This constitutes a concrete biological argument rather than pure lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Mg(2+) is also annotated as a cofactor for this protein but is absent from the answer choices, so it cannot create ambiguity. Among the four provided options, Mn(2+) is the only one matching any annotated cofactor, and the other three are clearly inappropriate for a kinase. No genuine ambiguity exists within the given option set.


### Important caveats

- The cofactor annotation carries evidence code ECO:0000250 (inferred by similarity from Q9LNJ9), not direct experimental measurement on this specific B. fragilis protein. The Cryo-EM structure (PDB 5YYS, 4.2 Å) was determined but the cofactor assignment is transferred.
- The protein has two catalytic activities (L-fucokinase and GDP-fucose pyrophosphorylase). The L-fucokinase activity requires Mn(2+) and Mg(2+); the pyrophosphorylase activity has a high preference for Mg(2+). The question does not specify which activity's cofactor is being asked about, but since only Mn(2+) appears among the choices, this does not affect the answer.
- The sequence-match to Q58T34 is confirmed (SHA-256 match, 949 aa), and the historical entry (v87) is identical to the current entry (v89) for the relevant annotation fields.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The four choices span distinct cofactor classes: NAD(+) is a hydride-transfer cofactor for dehydrogenases; Na(+) is a monovalent ion not typically a catalytic cofactor; Zn(2+) is characteristic of metalloproteases, carbonic anhydrases, and certain dehydrogenases; Mn(2+) is a divalent cation used by kinases to coordinate the β- and γ-phosphates of ATP. Recognizing the protein as a sugar kinase (the sequence contains glycine-rich stretches such as 'GSGGGTSWL' suggestive of a nucleotide-binding/P-loop region, and the overall architecture is consistent with a multi-domain transferase) allows elimination of NAD+, Na+, and Zn(2+), leaving Mn(2+) as the only plausible kinase cofactor among the options. Even without full sequence recognition, the elimination logic—kinases need divalent cations for phosphate coordination, and among the four choices only Mn(2+) fits—provides a defensible general-biology argument.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None that is essential. The specific annotation confirming Mn(2+) for this exact protein is similarity-based (ECO:0000250), but the reasoning from enzyme-class cofactor preferences is sufficient to select Mn(2+) over the three clearly inappropriate distractors.",
    "reason": "General knowledge of kinase cofactor requirements (divalent cations for ATP phosphate coordination) meaningfully distinguishes Mn(2+) from NAD+ (dehydrogenase cofactor), Na+ (non-catalytic monovalent ion), and Zn(2+) (metalloprotease/dehydrogenase cofactor). The glycine-rich motifs in the sequence provide weak but real structural hints toward a nucleotide-binding/kinase fold. This constitutes a concrete biological argument rather than pure lookup."
  },
  "case_id": "cofactor_0144",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4",
      "C4",
      "C1"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q58T34 (FKP_BACFG, L-fucokinase/L-fucose-1-P guanylyltransferase from Bacteroides fragilis) annotates Mn(2+) as a required cofactor for the L-fucokinase activity (ECO:0000250, similarity-based inference from Q9LNJ9). The note states: 'The L-fucokinase activity absolutely requires divalent cations such as Mn(2+) and Mg(2+).' Mg(2+) is also listed but is not among the four answer choices. Among the provided options (Mn2+, NAD+, Na+, Zn2+), only Mn(2+) appears in the cofactor annotation. The evidence code is similarity-based rather than direct experimental proof for this specific protein, but the annotation nonetheless supports the key."
  },
  "important_caveats": [
    "The cofactor annotation carries evidence code ECO:0000250 (inferred by similarity from Q9LNJ9), not direct experimental measurement on this specific B. fragilis protein. The Cryo-EM structure (PDB 5YYS, 4.2 Å) was determined but the cofactor assignment is transferred.",
    "The protein has two catalytic activities (L-fucokinase and GDP-fucose pyrophosphorylase). The L-fucokinase activity requires Mn(2+) and Mg(2+); the pyrophosphorylase activity has a high preference for Mg(2+). The question does not specify which activity's cofactor is being asked about, but since only Mn(2+) appears among the choices, this does not affect the answer.",
    "The sequence-match to Q58T34 is confirmed (SHA-256 match, 949 aa), and the historical entry (v87) is identical to the current entry (v89) for the relevant annotation fields."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Mg(2+) is also annotated as a cofactor for this protein but is absent from the answer choices, so it cannot create ambiguity. Among the four provided options, Mn(2+) is the only one matching any annotated cofactor, and the other three are clearly inappropriate for a kinase. No genuine ambiguity exists within the given option set."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0144",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q58T34 (FKP_BACFG, L-fucokinase/L-fucose-1-P guanylyltransferase from Bacteroides fragilis) annotates Mn(2+) as a required cofactor for the L-fucokinase activity (ECO:0000250, similarity-based inference from Q9LNJ9). The note states: 'The L-fucokinase activity absolutely requires divalent cations such as Mn(2+) and Mg(2+).' Mg(2+) is also listed but is not among the four answer choices. Among the provided options (Mn2+, NAD+, Na+, Zn2+), only Mn(2+) appears in the cofactor annotation. The evidence code is similarity-based rather than direct experimental proof for this specific protein, but the annotation nonetheless supports the key.",
    "evidence_ids": ["C5", "H4", "C4", "C1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The four choices span distinct cofactor classes: NAD(+) is a hydride-transfer cofactor for dehydrogenases; Na(+) is a monovalent ion not typically a catalytic cofactor; Zn(2+) is characteristic of metalloproteases, carbonic anhydrases, and certain dehydrogenases; Mn(2+) is a divalent cation used by kinases to coordinate the β- and γ-phosphates of ATP. Recognizing the protein as a sugar kinase (the sequence contains glycine-rich stretches such as 'GSGGGTSWL' suggestive of a nucleotide-binding/P-loop region, and the overall architecture is consistent with a multi-domain transferase) allows elimination of NAD+, Na+, and Zn(2+), leaving Mn(2+) as the only plausible kinase cofactor among the options. Even without full sequence recognition, the elimination logic—kinases need divalent cations for phosphate coordination, and among the four choices only Mn(2+) fits—provides a defensible general-biology argument.",
    "missing_item_specific_fact": "None that is essential. The specific annotation confirming Mn(2+) for this exact protein is similarity-based (ECO:0000250), but the reasoning from enzyme-class cofactor preferences is sufficient to select Mn(2+) over the three clearly inappropriate distractors.",
    "reason": "General knowledge of kinase cofactor requirements (divalent cations for ATP phosphate coordination) meaningfully distinguishes Mn(2+) from NAD+ (dehydrogenase cofactor), Na+ (non-catalytic monovalent ion), and Zn(2+) (metalloprotease/dehydrogenase cofactor). The glycine-rich motifs in the sequence provide weak but real structural hints toward a nucleotide-binding/kinase fold. This constitutes a concrete biological argument rather than pure lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Mg(2+) is also annotated as a cofactor for this protein but is absent from the answer choices, so it cannot create ambiguity. Among the four provided options, Mn(2+) is the only one matching any annotated cofactor, and the other three are clearly inappropriate for a kinase. No genuine ambiguity exists within the given option set."
  },
  "important_caveats": [
    "The cofactor annotation carries evidence code ECO:0000250 (inferred by similarity from Q9LNJ9), not direct experimental measurement on this specific B. fragilis protein. The Cryo-EM structure (PDB 5YYS, 4.2 Å) was determined but the cofactor assignment is transferred.",
    "The protein has two catalytic activities (L-fucokinase and GDP-fucose pyrophosphorylase). The L-fucokinase activity requires Mn(2+) and Mg(2+); the pyrophosphorylase activity has a high preference for Mg(2+). The question does not specify which activity's cofactor is being asked about, but since only Mn(2+) appears among the choices, this does not affect the answer.",
    "The sequence-match to Q58T34 is confirmed (SHA-256 match, 949 aa), and the historical entry (v87) is identical to the current entry (v89) for the relevant annotation fields."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched UniProt entry lists Mn(2+) as a cofactor for the L-fucokinase activity, alongside Mg(2+). This annotation is transferred from another protein rather than direct evidence for this exact protein, but supports Mn(2+) as a valid answer among the offered options.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with the large, bifunctional fucokinase/GDP-fucose pyrophosphorylase family. Transferable knowledge of nucleotide-phosphoryl-transfer enzymes supports a requirement for divalent cations; among these choices, Mn(2+) is the plausible metal option, whereas NAD(+) and Na(+) do not fit that role and no zinc-binding feature is evident. Related-family knowledge also supports Mn(2+) as one usable ion, though Mg(2+) is another and is not offered.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level inference meaningfully favors Mn(2+) over the listed alternatives without needing the exact protein's database annotation. It does not establish that Mn(2+) is the only effective ion.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The evidence also identifies Mg(2+) as relevant, but Mg(2+) is not among the offered choices. Of the choices shown, Mn(2+) is supported.


### Important caveats

- The cofactor annotation is based on transfer from a related protein (ECO:0000250), not direct experimental evidence for this sequence.
- The enzyme has more than one catalytic activity, and the cited annotation associates Mn(2+) with its L-fucokinase activity while also noting Mg(2+).

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with the large, bifunctional fucokinase/GDP-fucose pyrophosphorylase family. Transferable knowledge of nucleotide-phosphoryl-transfer enzymes supports a requirement for divalent cations; among these choices, Mn(2+) is the plausible metal option, whereas NAD(+) and Na(+) do not fit that role and no zinc-binding feature is evident. Related-family knowledge also supports Mn(2+) as one usable ion, though Mg(2+) is another and is not offered.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference meaningfully favors Mn(2+) over the listed alternatives without needing the exact protein's database annotation. It does not establish that Mn(2+) is the only effective ion."
  },
  "case_id": "cofactor_0144",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry lists Mn(2+) as a cofactor for the L-fucokinase activity, alongside Mg(2+). This annotation is transferred from another protein rather than direct evidence for this exact protein, but supports Mn(2+) as a valid answer among the offered options."
  },
  "important_caveats": [
    "The cofactor annotation is based on transfer from a related protein (ECO:0000250), not direct experimental evidence for this sequence.",
    "The enzyme has more than one catalytic activity, and the cited annotation associates Mn(2+) with its L-fucokinase activity while also noting Mg(2+)."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence also identifies Mg(2+) as relevant, but Mg(2+) is not among the offered choices. Of the choices shown, Mn(2+) is supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0144",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry lists Mn(2+) as a cofactor for the L-fucokinase activity, alongside Mg(2+). This annotation is transferred from another protein rather than direct evidence for this exact protein, but supports Mn(2+) as a valid answer among the offered options.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with the large, bifunctional fucokinase/GDP-fucose pyrophosphorylase family. Transferable knowledge of nucleotide-phosphoryl-transfer enzymes supports a requirement for divalent cations; among these choices, Mn(2+) is the plausible metal option, whereas NAD(+) and Na(+) do not fit that role and no zinc-binding feature is evident. Related-family knowledge also supports Mn(2+) as one usable ion, though Mg(2+) is another and is not offered.",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference meaningfully favors Mn(2+) over the listed alternatives without needing the exact protein's database annotation. It does not establish that Mn(2+) is the only effective ion."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence also identifies Mg(2+) as relevant, but Mg(2+) is not among the offered choices. Of the choices shown, Mn(2+) is supported."
  },
  "important_caveats": [
    "The cofactor annotation is based on transfer from a related protein (ECO:0000250), not direct experimental evidence for this sequence.",
    "The enzyme has more than one catalytic activity, and the cited annotation associates Mn(2+) with its L-fucokinase activity while also noting Mg(2+)."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (Q58T34, L-fucokinase/GDP-fucose pyrophosphorylase from Bacteroides fragilis) explicitly lists Mn(2+) as a cofactor for the L-fucokinase activity, with the note that 'The L-fucokinase activity absolutely requires divalent cations such as Mn(2+) and Mg(2+).' Mg(2+) is also listed but is not among the answer choices. The evidence code is ECO:0000250 (inferred by similarity from Q9LNJ9), so this is a homology-based annotation rather than direct experimental data for this exact protein, but it does list Mn(2+) as a cofactor. Among the four offered options, Mn(2+) is the only one annotated as a cofactor for this protein.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains recognizable kinase-associated motifs: a GSGG nucleotide-binding motif near the N-terminus ('KKLGSGGGTSWLLEECYNEYSDGATFGEW'), GK-containing phosphate-binding patterns ('GKILTP', 'GKGF'), and an overall architecture consistent with a sugar kinase / pyrophosphorylase. From general enzymology, all kinases (EC 2.7.x) require divalent metal cations—typically Mg(2+) or Mn(2+)—to coordinate the triphosphate of the nucleotide donor and stabilize the transition state during phosphoryl transfer. Among the four offered choices: (A) Mn(2+) is a classic divalent cation cofactor for kinases; (B) NAD(+) is the cofactor for oxidoreductases/dehydrogenases, not kinases; (C) Na(+) is a monovalent ion associated with transporters, ion channels, and some GTPases, not a kinase catalytic cofactor; (D) Zn(2+) is characteristic of metalloproteases, alcohol dehydrogenases, carbonic anhydrases, and zinc-finger domains, but not of sugar kinases. Therefore, recognizing the kinase character of the sequence and applying the universal principle that kinases require divalent cations meaningfully selects Mn(2+) over the three distractors without needing to know the specific UniProt annotation of this protein.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The inference relies on well-established, transferable knowledge: (1) sequence motifs (GSGG, GK) indicate a kinase/nucleotidyltransferase; (2) kinases universally require divalent cations (Mg2+ or Mn2+); (3) among the four choices, only Mn(2+) is a divalent cation appropriate for kinase chemistry. NAD+ belongs to a completely different enzyme class (oxidoreductases), Na+ is not a kinase cofactor, and Zn(2+) is associated with proteases and other metalloenzymes. This is standard biochemistry applicable across the kinase superfamily.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the four choices, only Mn(2+) is a plausible kinase cofactor. NAD+ is for oxidoreductases, Na+ is not a kinase cofactor, and Zn(2+) is for metalloproteases/other classes. Mg(2+) is also a valid cofactor per the annotation but is not offered as a choice, so no ambiguity arises among the presented options.


### Important caveats

- The UniProt cofactor annotation uses evidence code ECO:0000250 (inferred by similarity from Q9LNJ9), meaning the Mn(2+) assignment is homology-based rather than directly experimentally validated for this exact Bacteroides fragilis FKP sequence.
- The annotation also lists Mg(2+) as an equally valid cofactor for the L-fucokinase domain and the preferred cofactor for the GDP-fucose pyrophosphorylase domain; Mg(2+) is absent from the choices, so Mn(2+) is the only correct option among those offered.
- The protein is bifunctional (kinase + pyrophosphorylase); the question asks for 'the cofactor' without specifying which catalytic domain, but the kinase domain's requirement for Mn(2+)/Mg(2+) is the dominant and most commonly referenced cofactor annotation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains recognizable kinase-associated motifs: a GSGG nucleotide-binding motif near the N-terminus ('KKLGSGGGTSWLLEECYNEYSDGATFGEW'), GK-containing phosphate-binding patterns ('GKILTP', 'GKGF'), and an overall architecture consistent with a sugar kinase / pyrophosphorylase. From general enzymology, all kinases (EC 2.7.x) require divalent metal cations—typically Mg(2+) or Mn(2+)—to coordinate the triphosphate of the nucleotide donor and stabilize the transition state during phosphoryl transfer. Among the four offered choices: (A) Mn(2+) is a classic divalent cation cofactor for kinases; (B) NAD(+) is the cofactor for oxidoreductases/dehydrogenases, not kinases; (C) Na(+) is a monovalent ion associated with transporters, ion channels, and some GTPases, not a kinase catalytic cofactor; (D) Zn(2+) is characteristic of metalloproteases, alcohol dehydrogenases, carbonic anhydrases, and zinc-finger domains, but not of sugar kinases. Therefore, recognizing the kinase character of the sequence and applying the universal principle that kinases require divalent cations meaningfully selects Mn(2+) over the three distractors without needing to know the specific UniProt annotation of this protein.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The inference relies on well-established, transferable knowledge: (1) sequence motifs (GSGG, GK) indicate a kinase/nucleotidyltransferase; (2) kinases universally require divalent cations (Mg2+ or Mn2+); (3) among the four choices, only Mn(2+) is a divalent cation appropriate for kinase chemistry. NAD+ belongs to a completely different enzyme class (oxidoreductases), Na+ is not a kinase cofactor, and Zn(2+) is associated with proteases and other metalloenzymes. This is standard biochemistry applicable across the kinase superfamily."
  },
  "case_id": "cofactor_0144",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (Q58T34, L-fucokinase/GDP-fucose pyrophosphorylase from Bacteroides fragilis) explicitly lists Mn(2+) as a cofactor for the L-fucokinase activity, with the note that 'The L-fucokinase activity absolutely requires divalent cations such as Mn(2+) and Mg(2+).' Mg(2+) is also listed but is not among the answer choices. The evidence code is ECO:0000250 (inferred by similarity from Q9LNJ9), so this is a homology-based annotation rather than direct experimental data for this exact protein, but it does list Mn(2+) as a cofactor. Among the four offered options, Mn(2+) is the only one annotated as a cofactor for this protein."
  },
  "important_caveats": [
    "The UniProt cofactor annotation uses evidence code ECO:0000250 (inferred by similarity from Q9LNJ9), meaning the Mn(2+) assignment is homology-based rather than directly experimentally validated for this exact Bacteroides fragilis FKP sequence.",
    "The annotation also lists Mg(2+) as an equally valid cofactor for the L-fucokinase domain and the preferred cofactor for the GDP-fucose pyrophosphorylase domain; Mg(2+) is absent from the choices, so Mn(2+) is the only correct option among those offered.",
    "The protein is bifunctional (kinase + pyrophosphorylase); the question asks for 'the cofactor' without specifying which catalytic domain, but the kinase domain's requirement for Mn(2+)/Mg(2+) is the dominant and most commonly referenced cofactor annotation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four choices, only Mn(2+) is a plausible kinase cofactor. NAD+ is for oxidoreductases, Na+ is not a kinase cofactor, and Zn(2+) is for metalloproteases/other classes. Mg(2+) is also a valid cofactor per the annotation but is not offered as a choice, so no ambiguity arises among the presented options."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0144",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (Q58T34, L-fucokinase/GDP-fucose pyrophosphorylase from Bacteroides fragilis) explicitly lists Mn(2+) as a cofactor for the L-fucokinase activity, with the note that 'The L-fucokinase activity absolutely requires divalent cations such as Mn(2+) and Mg(2+).' Mg(2+) is also listed but is not among the answer choices. The evidence code is ECO:0000250 (inferred by similarity from Q9LNJ9), so this is a homology-based annotation rather than direct experimental data for this exact protein, but it does list Mn(2+) as a cofactor. Among the four offered options, Mn(2+) is the only one annotated as a cofactor for this protein.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains recognizable kinase-associated motifs: a GSGG nucleotide-binding motif near the N-terminus ('KKLGSGGGTSWLLEECYNEYSDGATFGEW'), GK-containing phosphate-binding patterns ('GKILTP', 'GKGF'), and an overall architecture consistent with a sugar kinase / pyrophosphorylase. From general enzymology, all kinases (EC 2.7.x) require divalent metal cations—typically Mg(2+) or Mn(2+)—to coordinate the triphosphate of the nucleotide donor and stabilize the transition state during phosphoryl transfer. Among the four offered choices: (A) Mn(2+) is a classic divalent cation cofactor for kinases; (B) NAD(+) is the cofactor for oxidoreductases/dehydrogenases, not kinases; (C) Na(+) is a monovalent ion associated with transporters, ion channels, and some GTPases, not a kinase catalytic cofactor; (D) Zn(2+) is characteristic of metalloproteases, alcohol dehydrogenases, carbonic anhydrases, and zinc-finger domains, but not of sugar kinases. Therefore, recognizing the kinase character of the sequence and applying the universal principle that kinases require divalent cations meaningfully selects Mn(2+) over the three distractors without needing to know the specific UniProt annotation of this protein.",
    "missing_item_specific_fact": "",
    "reason": "The inference relies on well-established, transferable knowledge: (1) sequence motifs (GSGG, GK) indicate a kinase/nucleotidyltransferase; (2) kinases universally require divalent cations (Mg2+ or Mn2+); (3) among the four choices, only Mn(2+) is a divalent cation appropriate for kinase chemistry. NAD+ belongs to a completely different enzyme class (oxidoreductases), Na+ is not a kinase cofactor, and Zn(2+) is associated with proteases and other metalloenzymes. This is standard biochemistry applicable across the kinase superfamily."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four choices, only Mn(2+) is a plausible kinase cofactor. NAD+ is for oxidoreductases, Na+ is not a kinase cofactor, and Zn(2+) is for metalloproteases/other classes. Mg(2+) is also a valid cofactor per the annotation but is not offered as a choice, so no ambiguity arises among the presented options."
  },
  "important_caveats": [
    "The UniProt cofactor annotation uses evidence code ECO:0000250 (inferred by similarity from Q9LNJ9), meaning the Mn(2+) assignment is homology-based rather than directly experimentally validated for this exact Bacteroides fragilis FKP sequence.",
    "The annotation also lists Mg(2+) as an equally valid cofactor for the L-fucokinase domain and the preferred cofactor for the GDP-fucose pyrophosphorylase domain; Mg(2+) is absent from the choices, so Mn(2+) is the only correct option among those offered.",
    "The protein is bifunctional (kinase + pyrophosphorylase); the question asks for 'the cofactor' without specifying which catalytic domain, but the kinase domain's requirement for Mn(2+)/Mg(2+) is the dominant and most commonly referenced cofactor annotation."
  ]
}
```

</details>

## Existing project source checks of the old Luna review only

These unchanged notes concern the earlier Luna claims. They do not validate either new review or the old Qwen review. No new scientific adjudication was performed.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Complete reviewer-only evidence and qualifications

All excerpts supplied in the original and revised reviewer user message follow. This material was not available to the original evaluated model. Accession identity came from dataset image-path metadata. Source support and transferable discrimination are separate judgments.

**Applicability metadata, unchanged:**

```json
{
  "requested_accession": "Q58T34",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "0a1aad3ffd7b1cb09dfa4c0be0b330d8ac5ca7321345ec11ac9ab6c74f4a10e2",
  "benchmark_sequence_length": 949,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 89,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2005-04-26",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "613cb95f164460b198373fe8b1a0278d6f82b5f36a7ad73441bef68f5e41af74",
  "current_source_sequence_sha256": "0a1aad3ffd7b1cb09dfa4c0be0b330d8ac5ca7321345ec11ac9ab6c74f4a10e2",
  "current_source_sequence_length": 949,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 87,
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
  },
  "selected_historical_record_sha256": "3ecc50c16d349ff2fe2b86dd83a0288577ce5483563a520fae349796ac46e9a8",
  "selected_historical_source_sequence_sha256": "0a1aad3ffd7b1cb09dfa4c0be0b330d8ac5ca7321345ec11ac9ab6c74f4a10e2",
  "selected_historical_source_sequence_length": 949,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 87,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "actual_author_source_snapshot": "unknown",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed."
}
```

**Qualifications, unchanged:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q58T34.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q58T34.json",
  "source_sha256": "613cb95f164460b198373fe8b1a0278d6f82b5f36a7ad73441bef68f5e41af74",
  "retrieved_utc": "2026-11-02T04:31:01.700323+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"Q58T34\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q58T34.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q58T34.json",
  "source_sha256": "613cb95f164460b198373fe8b1a0278d6f82b5f36a7ad73441bef68f5e41af74",
  "retrieved_utc": "2026-11-02T04:31:01.700323+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":89,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2005-04-26\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q58T34.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q58T34.json",
  "source_sha256": "613cb95f164460b198373fe8b1a0278d6f82b5f36a7ad73441bef68f5e41af74",
  "retrieved_utc": "2026-11-02T04:31:01.700323+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Bacteroidota\",\"Bacteroidia\",\"Bacteroidales\",\"Bacteroidaceae\",\"Bacteroides\"],\"scientificName\":\"Bacteroides fragilis\",\"taxonId\":817}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q58T34.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q58T34.json",
  "source_sha256": "613cb95f164460b198373fe8b1a0278d6f82b5f36a7ad73441bef68f5e41af74",
  "retrieved_utc": "2026-11-02T04:31:01.700323+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30242642\",\"source\":\"PubMed\"}],\"value\":\"L-fucokinase/GDP-fucose pyrophosphorylase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30242642\",\"source\":\"PubMed\"}],\"value\":\"FKP\"}]}],\"includes\":[{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30242642\",\"source\":\"PubMed\"}],\"value\":\"GDP-fucose pyrophosphorylase\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"30242642\",\"source\":\"PubMed\"}],\"value\":\"2.7.7.30\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"30242642\",\"source\":\"PubMed\"}],\"value\":\"Fucose-1-phosphate guanylyltransferase\"}}},{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"30242642\",\"source\":\"PubMed\"}],\"value\":\"2.7.1.52\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30242642\",\"source\":\"PubMed\"}],\"value\":\"L-fucokinase\"}}}],\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"30242642\",\"source\":\"PubMed\"}],\"value\":\"L-fucokinase/L-fucose-1-P guanylyltransferase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q58T34.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q58T34.json",
  "source_sha256": "613cb95f164460b198373fe8b1a0278d6f82b5f36a7ad73441bef68f5e41af74",
  "retrieved_utc": "2026-11-02T04:31:01.700323+00:00",
  "json_pointer": "/comments/3",
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:29035\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9LNJ9\",\"source\":\"UniProtKB\"}],\"name\":\"Mn(2+)\"},{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:18420\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9LNJ9\",\"source\":\"UniProtKB\"}],\"name\":\"Mg(2+)\"}],\"commentType\":\"COFACTOR\",\"note\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9LNJ9\",\"source\":\"UniProtKB\"}],\"value\":\"The L-fucokinase activity absolutely requires divalent cations such as Mn(2+) and Mg(2+).\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q58T34.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q58T34.json",
  "source_sha256": "613cb95f164460b198373fe8b1a0278d6f82b5f36a7ad73441bef68f5e41af74",
  "retrieved_utc": "2026-11-02T04:31:01.700323+00:00",
  "json_pointer": "/comments/4",
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:18420\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9LNJ9\",\"source\":\"UniProtKB\"}],\"name\":\"Mg(2+)\"}],\"commentType\":\"COFACTOR\",\"note\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9LNJ9\",\"source\":\"UniProtKB\"}],\"value\":\"The GDP-fucose pyrophosphorylase activity also requires divalent cations, with a high preference for Mg(2+).\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q58T34.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q58T34.json",
  "source_sha256": "613cb95f164460b198373fe8b1a0278d6f82b5f36a7ad73441bef68f5e41af74",
  "retrieved_utc": "2026-11-02T04:31:01.700323+00:00",
  "json_pointer": "/references/2",
  "excerpt": "{\"citation\":{\"authors\":[\"Liu Y.\",\"Hu H.\",\"Wang J.\",\"Zhou Q.\",\"Wu P.\",\"Yan N.\",\"Wang H.W.\",\"Wu J.W.\",\"Sun L.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"30242642\"},{\"database\":\"DOI\",\"id\":\"10.1007/s13238-018-0576-x\"}],\"citationType\":\"journal article\",\"firstPage\":\"365\",\"id\":\"30242642\",\"journal\":\"Protein Cell\",\"lastPage\":\"369\",\"publicationDate\":\"2019\",\"title\":\"Cryo-EM structure of L-fucokinase/GDP-fucose pyrophosphorylase (FKP) in Bacteroides fragilis.\",\"volume\":\"10\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"5YYS\",\"source\":\"PDB\"}],\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"9343\"}],\"referenceNumber\":3,\"referencePositions\":[\"STRUCTURE BY ELECTRON MICROSCOPY (4.20 ANGSTROMS)\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"SUBUNIT\",\"DOMAIN\",\"MUTAGENESIS OF GLY-76; ARG-80; GLY-88; LYS-89; ARG-592; ASP-594; GLY-597; GLY-598; ASP-601; GLY-713; SER-714; GLY-715; GLY-717; SER-719; SER-720; ALA-723; GLY-758; GLY-759; GLN-761; ASP-762; GLY-899 AND GLY-901\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q58T34?format=txt&versions=87)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q58T34?format=txt&versions=87",
  "source_sha256": "3ecc50c16d349ff2fe2b86dd83a0288577ce5483563a520fae349796ac46e9a8",
  "retrieved_utc": "2026-11-02T04:31:04.760170+00:00",
  "source_locator": "lines 1-21",
  "excerpt": "ID   FKP_BACFG               Reviewed;         949 AA.\nAC   Q58T34;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   26-APR-2005, sequence version 1.\nDT   28-JAN-2026, entry version 87.\nDE   RecName: Full=L-fucokinase/L-fucose-1-P guanylyltransferase {ECO:0000305|PubMed:30242642};\nDE   AltName: Full=L-fucokinase/GDP-fucose pyrophosphorylase {ECO:0000303|PubMed:30242642};\nDE            Short=FKP {ECO:0000303|PubMed:30242642};\nDE   Includes:\nDE     RecName: Full=Fucose-1-phosphate guanylyltransferase {ECO:0000305|PubMed:30242642};\nDE              EC=2.7.7.30 {ECO:0000269|PubMed:30242642};\nDE     AltName: Full=GDP-fucose pyrophosphorylase {ECO:0000303|PubMed:30242642};\nDE   Includes:\nDE     RecName: Full=L-fucokinase {ECO:0000303|PubMed:30242642};\nDE              EC=2.7.1.52 {ECO:0000269|PubMed:30242642};\nGN   Name=fkp {ECO:0000312|EMBL:AAX45030.1};\nGN   ORFNames=HMPREF2533_03026 {ECO:0000312|EMBL:KXU43832.1};\nOS   Bacteroides fragilis.\nOC   Bacteria; Pseudomonadati; Bacteroidota; Bacteroidia; Bacteroidales;\nOC   Bacteroidaceae; Bacteroides.\nOX   NCBI_TaxID=817;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 87,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q58T34?format=txt&versions=87)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q58T34?format=txt&versions=87",
  "source_sha256": "3ecc50c16d349ff2fe2b86dd83a0288577ce5483563a520fae349796ac46e9a8",
  "retrieved_utc": "2026-11-02T04:31:04.760170+00:00",
  "source_locator": "lines 6-15",
  "excerpt": "DE   RecName: Full=L-fucokinase/L-fucose-1-P guanylyltransferase {ECO:0000305|PubMed:30242642};\nDE   AltName: Full=L-fucokinase/GDP-fucose pyrophosphorylase {ECO:0000303|PubMed:30242642};\nDE            Short=FKP {ECO:0000303|PubMed:30242642};\nDE   Includes:\nDE     RecName: Full=Fucose-1-phosphate guanylyltransferase {ECO:0000305|PubMed:30242642};\nDE              EC=2.7.7.30 {ECO:0000269|PubMed:30242642};\nDE     AltName: Full=GDP-fucose pyrophosphorylase {ECO:0000303|PubMed:30242642};\nDE   Includes:\nDE     RecName: Full=L-fucokinase {ECO:0000303|PubMed:30242642};\nDE              EC=2.7.1.52 {ECO:0000269|PubMed:30242642};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 87,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q58T34?format=txt&versions=87)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q58T34?format=txt&versions=87",
  "source_sha256": "3ecc50c16d349ff2fe2b86dd83a0288577ce5483563a520fae349796ac46e9a8",
  "retrieved_utc": "2026-11-02T04:31:04.760170+00:00",
  "source_locator": "lines 36-47",
  "excerpt": "RN   [3] {ECO:0007744|PDB:5YYS}\nRP   STRUCTURE BY ELECTRON MICROSCOPY (4.20 ANGSTROMS), FUNCTION, CATALYTIC\nRP   ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, SUBUNIT, DOMAIN, AND MUTAGENESIS\nRP   OF GLY-76; ARG-80; GLY-88; LYS-89; ARG-592; ASP-594; GLY-597; GLY-598;\nRP   ASP-601; GLY-713; SER-714; GLY-715; GLY-717; SER-719; SER-720; ALA-723;\nRP   GLY-758; GLY-759; GLN-761; ASP-762; GLY-899 AND GLY-901.\nRC   STRAIN=9343;\nRX   PubMed=30242642; DOI=10.1007/s13238-018-0576-x;\nRA   Liu Y., Hu H., Wang J., Zhou Q., Wu P., Yan N., Wang H.W., Wu J.W., Sun L.;\nRT   \"Cryo-EM structure of L-fucokinase/GDP-fucose pyrophosphorylase (FKP) in\nRT   Bacteroides fragilis.\";\nRL   Protein Cell 10:365-369(2019).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 87,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q58T34?format=txt&versions=87)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q58T34?format=txt&versions=87",
  "source_sha256": "3ecc50c16d349ff2fe2b86dd83a0288577ce5483563a520fae349796ac46e9a8",
  "retrieved_utc": "2026-11-02T04:31:04.760170+00:00",
  "source_locator": "lines 69-75",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=Mn(2+); Xref=ChEBI:CHEBI:29035;\nCC         Evidence={ECO:0000250|UniProtKB:Q9LNJ9};\nCC       Name=Mg(2+); Xref=ChEBI:CHEBI:18420;\nCC         Evidence={ECO:0000250|UniProtKB:Q9LNJ9};\nCC       Note=The L-fucokinase activity absolutely requires divalent cations\nCC       such as Mn(2+) and Mg(2+). {ECO:0000250|UniProtKB:Q9LNJ9};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 87,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q58T34?format=txt&versions=87)

```json
{
  "evidence_id": "H5",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q58T34?format=txt&versions=87",
  "source_sha256": "3ecc50c16d349ff2fe2b86dd83a0288577ce5483563a520fae349796ac46e9a8",
  "retrieved_utc": "2026-11-02T04:31:04.760170+00:00",
  "source_locator": "lines 76-81",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=Mg(2+); Xref=ChEBI:CHEBI:18420;\nCC         Evidence={ECO:0000250|UniProtKB:Q9LNJ9};\nCC       Note=The GDP-fucose pyrophosphorylase activity also requires divalent\nCC       cations, with a high preference for Mg(2+).\nCC       {ECO:0000250|UniProtKB:Q9LNJ9};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 87,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 144. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
