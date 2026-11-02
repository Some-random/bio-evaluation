# cofactor_0144

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `cofactor`  
**Author expected answer:** **A** — Mn(2+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

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
<summary>Original system instructions, verbatim</summary>

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

## GPT-6 Luna

**Saved status:** `valid_review`.

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

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

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

## Existing project source checks of Luna’s review

The notes below were prepared for specific claims in the Luna review. They are not independent validation of Qwen’s claims, expert adjudication, or replacement verdicts.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**Both reviewers received this source evidence separately from the original question. It was not available to the original evaluated model.** Source support and reasoning from the original sequence/choices are distinct assessments.

**Accession:** `Q58T34` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 87. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q58T34.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:01.700323+00:00.  

```json
"Q58T34"
```

Source SHA-256: `613cb95f164460b198373fe8b1a0278d6f82b5f36a7ad73441bef68f5e41af74`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q58T34.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:01.700323+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"30242642","source":"PubMed"}],"value":"L-fucokinase/GDP-fucose pyrophosphorylase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"30242642","source":"PubMed"}],"value":"FKP"}]}],"includes":[{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"30242642","source":"PubMed"}],"value":"GDP-fucose pyrophosphorylase"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"30242642","source":"PubMed"}],"value":"2.7.7.30"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305","id":"30242642","source":"PubMed"}],"value":"Fucose-1-phosphate guanylyltransferase"}}},{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"30242642","source":"PubMed"}],"value":"2.7.1.52"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"30242642","source":"PubMed"}],"value":"L-fucokinase"}}}],"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305","id":"30242642","source":"PubMed"}],"value":"L-fucokinase/L-fucose-1-P guanylyltransferase"}}}
```

Source SHA-256: `613cb95f164460b198373fe8b1a0278d6f82b5f36a7ad73441bef68f5e41af74`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q58T34.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:01.700323+00:00.  

```json
{"cofactors":[{"cofactorCrossReference":{"database":"ChEBI","id":"CHEBI:29035"},"evidences":[{"evidenceCode":"ECO:0000250","id":"Q9LNJ9","source":"UniProtKB"}],"name":"Mn(2+)"},{"cofactorCrossReference":{"database":"ChEBI","id":"CHEBI:18420"},"evidences":[{"evidenceCode":"ECO:0000250","id":"Q9LNJ9","source":"UniProtKB"}],"name":"Mg(2+)"}],"commentType":"COFACTOR","note":{"texts":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q9LNJ9","source":"UniProtKB"}],"value":"The L-fucokinase activity absolutely requires divalent cations such as Mn(2+) and Mg(2+)."}]}}
```

Source SHA-256: `613cb95f164460b198373fe8b1a0278d6f82b5f36a7ad73441bef68f5e41af74`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q58T34?format=txt&versions=87)  
**Locator:** `lines 69-75`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 87 / 1.  
**Retrieved:** 2026-11-02T04:31:04.760170+00:00.  

```text
CC   -!- COFACTOR:
CC       Name=Mn(2+); Xref=ChEBI:CHEBI:29035;
CC         Evidence={ECO:0000250|UniProtKB:Q9LNJ9};
CC       Name=Mg(2+); Xref=ChEBI:CHEBI:18420;
CC         Evidence={ECO:0000250|UniProtKB:Q9LNJ9};
CC       Note=The L-fucokinase activity absolutely requires divalent cations
CC       such as Mn(2+) and Mg(2+). {ECO:0000250|UniProtKB:Q9LNJ9};
```

Source SHA-256: `3ecc50c16d349ff2fe2b86dd83a0288577ce5483563a520fae349796ac46e9a8`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 144. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
