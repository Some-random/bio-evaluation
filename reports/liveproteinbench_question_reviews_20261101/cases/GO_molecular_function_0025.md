# GO_molecular_function_0025

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **D** — fucokinase activity

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
A. potassium channel regulator activity
B. manganese ion transmembrane transporter activity
C. oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen
D. fucokinase activity
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

### Expected-answer support: supported

> The supplied sequence exactly matches the Bacteroides fragilis FKP entry. That entry reports fucokinase activity and the ATP-dependent fucose phosphorylation reaction with experimental evidence linked to PubMed 30242642, supporting D for this sequence. The enzyme is bifunctional, though: it also catalyzes a second reaction not listed among the choices.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C6](#evidence-c6), [C9](#evidence-c9).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence does not provide a clear general biological cue that establishes fucose as the substrate. Its length and enzyme-like sequence could make channel or transporter choices less plausible, but do not distinguish fucokinase from other soluble enzyme activities such as the listed oxidoreductase activity.


**Missing item-specific fact**

> The protein-specific functional identification or experimental evidence that this sequence encodes an enzyme phosphorylating L-fucose.


**Reason**

> Choosing D requires identifying this particular protein's substrate-specific activity, a fact not supplied in the prompt. Merely recognizing the sequence or invoking a predictor would not make the choice reasoning-supported.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> D is supported as one of the protein's molecular functions. The protein also has fucose-1-phosphate guanylyltransferase activity, but that activity is not an offered choice; it does not make another listed option defensible.


### Important caveats

- The experimental support is reported in UniProt and linked to PubMed 30242642; the primary paper was not independently reviewed here.
- The sequence match supports applicability to the supplied sequence, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence does not provide a clear general biological cue that establishes fucose as the substrate. Its length and enzyme-like sequence could make channel or transporter choices less plausible, but do not distinguish fucokinase from other soluble enzyme activities such as the listed oxidoreductase activity.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific functional identification or experimental evidence that this sequence encodes an enzyme phosphorylating L-fucose.",
    "reason": "Choosing D requires identifying this particular protein's substrate-specific activity, a fact not supplied in the prompt. Merely recognizing the sequence or invoking a predictor would not make the choice reasoning-supported."
  },
  "case_id": "GO_molecular_function_0025",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C6",
      "C9"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the Bacteroides fragilis FKP entry. That entry reports fucokinase activity and the ATP-dependent fucose phosphorylation reaction with experimental evidence linked to PubMed 30242642, supporting D for this sequence. The enzyme is bifunctional, though: it also catalyzes a second reaction not listed among the choices."
  },
  "important_caveats": [
    "The experimental support is reported in UniProt and linked to PubMed 30242642; the primary paper was not independently reviewed here.",
    "The sequence match supports applicability to the supplied sequence, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "D is supported as one of the protein's molecular functions. The protein also has fucose-1-phosphate guanylyltransferase activity, but that activity is not an offered choice; it does not make another listed option defensible."
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
    "reason": "The supplied sequence exactly matches the Bacteroides fragilis FKP entry. That entry reports fucokinase activity and the ATP-dependent fucose phosphorylation reaction with experimental evidence linked to PubMed 30242642, supporting D for this sequence. The enzyme is bifunctional, though: it also catalyzes a second reaction not listed among the choices.",
    "evidence_ids": ["C1", "C5", "C6", "C9"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence does not provide a clear general biological cue that establishes fucose as the substrate. Its length and enzyme-like sequence could make channel or transporter choices less plausible, but do not distinguish fucokinase from other soluble enzyme activities such as the listed oxidoreductase activity.",
    "missing_item_specific_fact": "The protein-specific functional identification or experimental evidence that this sequence encodes an enzyme phosphorylating L-fucose.",
    "reason": "Choosing D requires identifying this particular protein's substrate-specific activity, a fact not supplied in the prompt. Merely recognizing the sequence or invoking a predictor would not make the choice reasoning-supported."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "D is supported as one of the protein's molecular functions. The protein also has fucose-1-phosphate guanylyltransferase activity, but that activity is not an offered choice; it does not make another listed option defensible."
  },
  "important_caveats": [
    "The experimental support is reported in UniProt and linked to PubMed 30242642; the primary paper was not independently reviewed here.",
    "The sequence match supports applicability to the supplied sequence, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt Q58T34 (FKP_BACFG, 949 AA, sequence match confirmed) is annotated with GO:0050201 'fucokinase activity' at EXP:UniProtKB evidence level, backed by direct assay (ECO:0000269, PubMed:30242642). The catalytic reaction L-fucose + ATP → β-L-fucose 1-phosphate + ADP + H⁺ (EC 2.7.1.52) is experimentally confirmed. The protein is bifunctional (also has fucose-1-phosphate guanylyltransferase activity, GO:0047341), but fucokinase activity is a valid primary molecular function annotation. The expected answer D matches the GO term exactly.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C9](#evidence-c9), [C10](#evidence-c10), [C11](#evidence-c11), [H1](#evidence-h1), [H3](#evidence-h3), [H4](#evidence-h4), [H7](#evidence-h7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 949-residue sequence encodes a large, predominantly soluble enzyme. Option A (potassium channel regulator activity) describes small regulatory subunits or accessory proteins that bind ion channels (e.g., KChIPs, Kvβ subunits); a ~950-residue catalytic protein is inconsistent. Option B (manganese ion transmembrane transporter activity) requires a polytopic membrane protein with defined TM helix topology; while a few hydrophobic stretches exist, the overall architecture lacks the repeated TM segments characteristic of metal-ion transporters. Option C (oxidoreductase with O₂ incorporation, EC 1.14) requires cofactor-binding motifs (heme, flavin, iron-sulfur clusters) and a characteristic active-site architecture absent here. Option D (fucokinase activity, a phosphotransferase) is the only option consistent with a large soluble enzyme containing glycine-rich nucleotide-binding regions (e.g., 'GSGGGTSWLLEEC' near the N-terminus) and catalytic residues typical of sugar kinases. By class-level elimination, D is the only defensible choice.


**Missing item-specific fact**

> Precise identification of the substrate as L-fucose (rather than another sugar) from sequence alone would require family-specific knowledge or database lookup; however, D is the sole kinase/phosphotransferase option among the four, so the specific substrate label is determined by default within the constrained option set.


**Reason**

> The distractors belong to entirely different protein classes (channel regulator, membrane transporter, oxidoreductase), making class-level elimination via general biological reasoning sufficient to select D. The question does not require distinguishing fucokinase from other sugar kinases because no other kinase option is offered.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A, B, and C describe fundamentally different protein classes (ion channel regulator, membrane transporter, oxidoreductase) that are incompatible with a large soluble phosphotransferase. The protein is bifunctional (fucokinase + guanylyltransferase), but only the fucokinase activity is offered as an option; the guanylyltransferase activity is not a competing choice. No ambiguity among the four options.


### Important caveats

- The protein is bifunctional; the question asks for the 'primary' molecular function, and fucokinase activity is one of two experimentally confirmed activities. The other (fucose-1-phosphate guanylyltransferase, GO:0047341) is not offered as a distractor.
- The specific substrate identification (L-fucose) from raw sequence alone is not achievable without database or family knowledge; the answer is reachable here only because D is the unique kinase option among four class-mismatched distractors.
- All UniProt evidence cited is from the current and historical (entry version 87) Swiss-Prot record with sequence match confirmed; the GO annotation carries EXP evidence code.
- Reviewer-only sources were used to confirm the key; these were not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 949-residue sequence encodes a large, predominantly soluble enzyme. Option A (potassium channel regulator activity) describes small regulatory subunits or accessory proteins that bind ion channels (e.g., KChIPs, Kvβ subunits); a ~950-residue catalytic protein is inconsistent. Option B (manganese ion transmembrane transporter activity) requires a polytopic membrane protein with defined TM helix topology; while a few hydrophobic stretches exist, the overall architecture lacks the repeated TM segments characteristic of metal-ion transporters. Option C (oxidoreductase with O₂ incorporation, EC 1.14) requires cofactor-binding motifs (heme, flavin, iron-sulfur clusters) and a characteristic active-site architecture absent here. Option D (fucokinase activity, a phosphotransferase) is the only option consistent with a large soluble enzyme containing glycine-rich nucleotide-binding regions (e.g., 'GSGGGTSWLLEEC' near the N-terminus) and catalytic residues typical of sugar kinases. By class-level elimination, D is the only defensible choice.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Precise identification of the substrate as L-fucose (rather than another sugar) from sequence alone would require family-specific knowledge or database lookup; however, D is the sole kinase/phosphotransferase option among the four, so the specific substrate label is determined by default within the constrained option set.",
    "reason": "The distractors belong to entirely different protein classes (channel regulator, membrane transporter, oxidoreductase), making class-level elimination via general biological reasoning sufficient to select D. The question does not require distinguishing fucokinase from other sugar kinases because no other kinase option is offered."
  },
  "case_id": "GO_molecular_function_0025",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C9",
      "C10",
      "C11",
      "H1",
      "H3",
      "H4",
      "H7"
    ],
    "judgment": "supported",
    "reason": "UniProt Q58T34 (FKP_BACFG, 949 AA, sequence match confirmed) is annotated with GO:0050201 'fucokinase activity' at EXP:UniProtKB evidence level, backed by direct assay (ECO:0000269, PubMed:30242642). The catalytic reaction L-fucose + ATP → β-L-fucose 1-phosphate + ADP + H⁺ (EC 2.7.1.52) is experimentally confirmed. The protein is bifunctional (also has fucose-1-phosphate guanylyltransferase activity, GO:0047341), but fucokinase activity is a valid primary molecular function annotation. The expected answer D matches the GO term exactly."
  },
  "important_caveats": [
    "The protein is bifunctional; the question asks for the 'primary' molecular function, and fucokinase activity is one of two experimentally confirmed activities. The other (fucose-1-phosphate guanylyltransferase, GO:0047341) is not offered as a distractor.",
    "The specific substrate identification (L-fucose) from raw sequence alone is not achievable without database or family knowledge; the answer is reachable here only because D is the unique kinase option among four class-mismatched distractors.",
    "All UniProt evidence cited is from the current and historical (entry version 87) Swiss-Prot record with sequence match confirmed; the GO annotation carries EXP evidence code.",
    "Reviewer-only sources were used to confirm the key; these were not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and C describe fundamentally different protein classes (ion channel regulator, membrane transporter, oxidoreductase) that are incompatible with a large soluble phosphotransferase. The protein is bifunctional (fucokinase + guanylyltransferase), but only the fucokinase activity is offered as an option; the guanylyltransferase activity is not a competing choice. No ambiguity among the four options."
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
    "reason": "UniProt Q58T34 (FKP_BACFG, 949 AA, sequence match confirmed) is annotated with GO:0050201 'fucokinase activity' at EXP:UniProtKB evidence level, backed by direct assay (ECO:0000269, PubMed:30242642). The catalytic reaction L-fucose + ATP → β-L-fucose 1-phosphate + ADP + H⁺ (EC 2.7.1.52) is experimentally confirmed. The protein is bifunctional (also has fucose-1-phosphate guanylyltransferase activity, GO:0047341), but fucokinase activity is a valid primary molecular function annotation. The expected answer D matches the GO term exactly.",
    "evidence_ids": ["C4", "C5", "C6", "C9", "C10", "C11", "H1", "H3", "H4", "H7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 949-residue sequence encodes a large, predominantly soluble enzyme. Option A (potassium channel regulator activity) describes small regulatory subunits or accessory proteins that bind ion channels (e.g., KChIPs, Kvβ subunits); a ~950-residue catalytic protein is inconsistent. Option B (manganese ion transmembrane transporter activity) requires a polytopic membrane protein with defined TM helix topology; while a few hydrophobic stretches exist, the overall architecture lacks the repeated TM segments characteristic of metal-ion transporters. Option C (oxidoreductase with O₂ incorporation, EC 1.14) requires cofactor-binding motifs (heme, flavin, iron-sulfur clusters) and a characteristic active-site architecture absent here. Option D (fucokinase activity, a phosphotransferase) is the only option consistent with a large soluble enzyme containing glycine-rich nucleotide-binding regions (e.g., 'GSGGGTSWLLEEC' near the N-terminus) and catalytic residues typical of sugar kinases. By class-level elimination, D is the only defensible choice.",
    "missing_item_specific_fact": "Precise identification of the substrate as L-fucose (rather than another sugar) from sequence alone would require family-specific knowledge or database lookup; however, D is the sole kinase/phosphotransferase option among the four, so the specific substrate label is determined by default within the constrained option set.",
    "reason": "The distractors belong to entirely different protein classes (channel regulator, membrane transporter, oxidoreductase), making class-level elimination via general biological reasoning sufficient to select D. The question does not require distinguishing fucokinase from other sugar kinases because no other kinase option is offered."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and C describe fundamentally different protein classes (ion channel regulator, membrane transporter, oxidoreductase) that are incompatible with a large soluble phosphotransferase. The protein is bifunctional (fucokinase + guanylyltransferase), but only the fucokinase activity is offered as an option; the guanylyltransferase activity is not a competing choice. No ambiguity among the four options."
  },
  "important_caveats": [
    "The protein is bifunctional; the question asks for the 'primary' molecular function, and fucokinase activity is one of two experimentally confirmed activities. The other (fucose-1-phosphate guanylyltransferase, GO:0047341) is not offered as a distractor.",
    "The specific substrate identification (L-fucose) from raw sequence alone is not achievable without database or family knowledge; the answer is reachable here only because D is the unique kinase option among four class-mismatched distractors.",
    "All UniProt evidence cited is from the current and historical (entry version 87) Swiss-Prot record with sequence match confirmed; the GO annotation carries EXP evidence code.",
    "Reviewer-only sources were used to confirm the key; these were not available to the evaluated model."
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
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

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
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:01.700323+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"30242642","source":"PubMed"}],"value":"Bifunctional enzyme involved in the salvage pathway of GDP-fucose synthesis. Catalyzes two successive reactions, the ATP-dependent phosphorylation of L-fucose to L-fucose 1-phosphate, and its guanylylation to GDP-L-fucose. GDP-fucose is an important fucose donor in the process of fucosylated oligosaccharides formation"}]}
```

Source SHA-256: `613cb95f164460b198373fe8b1a0278d6f82b5f36a7ad73441bef68f5e41af74`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q58T34.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:01.700323+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000305","id":"30242642","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:13242"}}],"reaction":{"ecNumber":"2.7.1.52","evidences":[{"evidenceCode":"ECO:0000269","id":"30242642","source":"PubMed"}],"name":"beta-L-fucose + ATP = beta-L-fucose 1-phosphate + ADP + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:13241"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:30616"},{"database":"ChEBI","id":"CHEBI:42589"},{"database":"ChEBI","id":"CHEBI:57268"},{"database":"ChEBI","id":"CHEBI:456216"}]}}
```

Source SHA-256: `613cb95f164460b198373fe8b1a0278d6f82b5f36a7ad73441bef68f5e41af74`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q58T34.json)  
**Locator:** `/uniProtKBCrossReferences/19`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:01.700323+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000269","id":"30242642","source":"PubMed"}],"id":"GO:0050201","properties":[{"key":"GoTerm","value":"F:fucokinase activity"},{"key":"GoEvidenceType","value":"EXP:UniProtKB"}]}
```

Source SHA-256: `613cb95f164460b198373fe8b1a0278d6f82b5f36a7ad73441bef68f5e41af74`.

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q58T34.json)  
**Locator:** `/uniProtKBCrossReferences/20`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:01.700323+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000269","id":"30242642","source":"PubMed"}],"id":"GO:0047341","properties":[{"key":"GoTerm","value":"F:fucose-1-phosphate guanylyltransferase activity"},{"key":"GoEvidenceType","value":"EXP:UniProtKB"}]}
```

Source SHA-256: `613cb95f164460b198373fe8b1a0278d6f82b5f36a7ad73441bef68f5e41af74`.

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q58T34.json)  
**Locator:** `/references/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:01.700323+00:00.  

```json
{"citation":{"authors":["Liu Y.","Hu H.","Wang J.","Zhou Q.","Wu P.","Yan N.","Wang H.W.","Wu J.W.","Sun L."],"citationCrossReferences":[{"database":"PubMed","id":"30242642"},{"database":"DOI","id":"10.1007/s13238-018-0576-x"}],"citationType":"journal article","firstPage":"365","id":"30242642","journal":"Protein Cell","lastPage":"369","publicationDate":"2019","title":"Cryo-EM structure of L-fucokinase/GDP-fucose pyrophosphorylase (FKP) in Bacteroides fragilis.","volume":"10"},"evidences":[{"evidenceCode":"ECO:0007744","id":"5YYS","source":"PDB"}],"referenceComments":[{"type":"STRAIN","value":"9343"}],"referenceNumber":3,"referencePositions":["STRUCTURE BY ELECTRON MICROSCOPY (4.20 ANGSTROMS)","FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","SUBUNIT","DOMAIN","MUTAGENESIS OF GLY-76; ARG-80; GLY-88; LYS-89; ARG-592; ASP-594; GLY-597; GLY-598; ASP-601; GLY-713; SER-714; GLY-715; GLY-717; SER-719; SER-720; ALA-723; GLY-758; GLY-759; GLN-761; ASP-762; GLY-899 AND GLY-901"]}
```

Source SHA-256: `613cb95f164460b198373fe8b1a0278d6f82b5f36a7ad73441bef68f5e41af74`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q58T34?format=txt&versions=87)  
**Locator:** `lines 1-21`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 87 / 1.  
**Retrieved:** 2026-11-02T04:31:04.760170+00:00.  

```text
ID   FKP_BACFG               Reviewed;         949 AA.
AC   Q58T34;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   26-APR-2005, sequence version 1.
DT   28-JAN-2026, entry version 87.
DE   RecName: Full=L-fucokinase/L-fucose-1-P guanylyltransferase {ECO:0000305|PubMed:30242642};
DE   AltName: Full=L-fucokinase/GDP-fucose pyrophosphorylase {ECO:0000303|PubMed:30242642};
DE            Short=FKP {ECO:0000303|PubMed:30242642};
DE   Includes:
DE     RecName: Full=Fucose-1-phosphate guanylyltransferase {ECO:0000305|PubMed:30242642};
DE              EC=2.7.7.30 {ECO:0000269|PubMed:30242642};
DE     AltName: Full=GDP-fucose pyrophosphorylase {ECO:0000303|PubMed:30242642};
DE   Includes:
DE     RecName: Full=L-fucokinase {ECO:0000303|PubMed:30242642};
DE              EC=2.7.1.52 {ECO:0000269|PubMed:30242642};
GN   Name=fkp {ECO:0000312|EMBL:AAX45030.1};
GN   ORFNames=HMPREF2533_03026 {ECO:0000312|EMBL:KXU43832.1};
OS   Bacteroides fragilis.
OC   Bacteria; Pseudomonadati; Bacteroidota; Bacteroidia; Bacteroidales;
OC   Bacteroidaceae; Bacteroides.
OX   NCBI_TaxID=817;
```

Source SHA-256: `3ecc50c16d349ff2fe2b86dd83a0288577ce5483563a520fae349796ac46e9a8`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q58T34?format=txt&versions=87)  
**Locator:** `lines 48-53`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 87 / 1.  
**Retrieved:** 2026-11-02T04:31:04.760170+00:00.  

```text
CC   -!- FUNCTION: Bifunctional enzyme involved in the salvage pathway of GDP-
CC       fucose synthesis. Catalyzes two successive reactions, the ATP-dependent
CC       phosphorylation of L-fucose to L-fucose 1-phosphate, and its
CC       guanylylation to GDP-L-fucose. GDP-fucose is an important fucose donor
CC       in the process of fucosylated oligosaccharides formation.
CC       {ECO:0000269|PubMed:30242642}.
```

Source SHA-256: `3ecc50c16d349ff2fe2b86dd83a0288577ce5483563a520fae349796ac46e9a8`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q58T34?format=txt&versions=87)  
**Locator:** `lines 54-60`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 87 / 1.  
**Retrieved:** 2026-11-02T04:31:04.760170+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=L-fucose + ATP = beta-L-fucose 1-phosphate + ADP + H(+);
CC         Xref=Rhea:RHEA:13241, ChEBI:CHEBI:2181, ChEBI:CHEBI:15378,
CC         ChEBI:CHEBI:30616, ChEBI:CHEBI:57268, ChEBI:CHEBI:456216;
CC         EC=2.7.1.52; Evidence={ECO:0000269|PubMed:30242642};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:13242;
CC         Evidence={ECO:0000305|PubMed:30242642};
```

Source SHA-256: `3ecc50c16d349ff2fe2b86dd83a0288577ce5483563a520fae349796ac46e9a8`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q58T34?format=txt&versions=87)  
**Locator:** `lines 118-118`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 87 / 1.  
**Retrieved:** 2026-11-02T04:31:04.760170+00:00.  

```text
DR   GO; GO:0050201; F:fucokinase activity; IEA:UniProtKB-EC.
```

Source SHA-256: `3ecc50c16d349ff2fe2b86dd83a0288577ce5483563a520fae349796ac46e9a8`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 25. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
