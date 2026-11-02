# catalytic_activity_0008

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **A** — apo-&#91;ACP&#93; + CoA = holo-&#91;ACP&#93; + adenosine 3&#x27;,5&#x27;-bisphosphate + H(+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MTDSNLLGLTCWLIDTRTLWPGQHIKDAASDILHLLSNDERNAVLRKIFIADARMSLASALLKRLYISRALNIPWRDVKIARKGDPTHGKPCAVLPDGSFAPIDFNVSHQAGLVSLVGWNPPPGQSQSALVGTDIVCVNERDDYRTIDQEGFDAWIDIYEDVFSEAERWDMKYNVDYITLLDGRIIQGNSLGRVDRCVRRNKDLSITLPTGETHSFNSDLLIDAKLRRFYSFFCYKEAYIKLAGEALLAPWLKELEFQNVKSPKPGTVARCSTHGTWGEKVSDVEVVLHGEKVEDVKMTLQAFEENFMLATAVQGLRDLEAPPFTKLNLENDVVAFAS

[Multiple Choices]
A. apo-[ACP] + CoA = holo-[ACP] + adenosine 3',5'-bisphosphate + H(+)
B. 3 malonyl-CoA + acetyl-CoA + 2 S-adenosyl-L-methionine = 3,5-dimethylorsellinate + 2 S-adenosyl-L-homocysteine + 3 CO2 + 4 CoA
C. 2-oxospirilloxanthin + 2 reduced [2Fe-2S]-[ferredoxin] + O2 + 2 H(+) = 2'-hydroxy-2-oxospirilloxanthin + 2 oxidized [2Fe-2S]-[ferredoxin] + H2O
D. (9S)-hydroperoxy-(10E,12Z)-octadecadienoate = colneleate + H2O
```

<details>
<summary>Original system instructions, verbatim</summary>

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

## GPT-6 Luna

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The exact sequence matches a UniProt entry annotated as a 4′-phosphopantetheinyl transferase, with the stated apo-ACP + CoA reaction. The annotation is transferred by similarity (ECO:0000250), so this supports the key as a computational annotation, not as direct experimental confirmation for this protein.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> If the protein is known to be a phosphopantetheinyl transferase, its role of transferring a phosphopantetheine group from CoA to apo-ACP selects A. But the supplied sequence and choices alone do not provide a sufficiently clear, general biological cue establishing that protein identity.


**Missing item-specific fact**

> The protein’s identity or family annotation as a 4′-phosphopantetheinyl transferase, or equivalent homology/domain evidence, is absent from the input.


**Reason**

> Choosing A depends on identifying this particular sequence as a phosphopantetheinyl transferase; the reviewer-only database match supports the key but was not available to the evaluated model.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The annotated activity matches A; the other options describe distinct reactions, and no supplied evidence supports them for this sequence.


### Important caveats

- The sequence match is exact, including in the historical entry checked.
- The cited catalytic-activity annotation is inferred by similarity to UniProtKB:Q4X1W0; no direct experimental validation for this protein is established by the excerpts.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "If the protein is known to be a phosphopantetheinyl transferase, its role of transferring a phosphopantetheine group from CoA to apo-ACP selects A. But the supplied sequence and choices alone do not provide a sufficiently clear, general biological cue establishing that protein identity.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein’s identity or family annotation as a 4′-phosphopantetheinyl transferase, or equivalent homology/domain evidence, is absent from the input.",
    "reason": "Choosing A depends on identifying this particular sequence as a phosphopantetheinyl transferase; the reviewer-only database match supports the key but was not available to the evaluated model."
  },
  "case_id": "catalytic_activity_0008",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as a 4′-phosphopantetheinyl transferase, with the stated apo-ACP + CoA reaction. The annotation is transferred by similarity (ECO:0000250), so this supports the key as a computational annotation, not as direct experimental confirmation for this protein."
  },
  "important_caveats": [
    "The sequence match is exact, including in the historical entry checked.",
    "The cited catalytic-activity annotation is inferred by similarity to UniProtKB:Q4X1W0; no direct experimental validation for this protein is established by the excerpts."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The annotated activity matches A; the other options describe distinct reactions, and no supplied evidence supports them for this sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0008",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as a 4′-phosphopantetheinyl transferase, with the stated apo-ACP + CoA reaction. The annotation is transferred by similarity (ECO:0000250), so this supports the key as a computational annotation, not as direct experimental confirmation for this protein.",
    "evidence_ids": ["C1", "C4", "C5", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "If the protein is known to be a phosphopantetheinyl transferase, its role of transferring a phosphopantetheine group from CoA to apo-ACP selects A. But the supplied sequence and choices alone do not provide a sufficiently clear, general biological cue establishing that protein identity.",
    "missing_item_specific_fact": "The protein’s identity or family annotation as a 4′-phosphopantetheinyl transferase, or equivalent homology/domain evidence, is absent from the input.",
    "reason": "Choosing A depends on identifying this particular sequence as a phosphopantetheinyl transferase; the reviewer-only database match supports the key but was not available to the evaluated model."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The annotated activity matches A; the other options describe distinct reactions, and no supplied evidence supports them for this sequence."
  },
  "important_caveats": [
    "The sequence match is exact, including in the historical entry checked.",
    "The cited catalytic-activity annotation is inferred by similarity to UniProtKB:Q4X1W0; no direct experimental validation for this protein is established by the excerpts."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The supplied sequence (338 aa, SHA256 99855a22…) matches UniProt entry A0A223GB52 (PPTA_AURME) in both current and historical (entry v19) snapshots. The entry is annotated as 4'-phosphopantetheinyl transferase (EC 2.7.8.7) with the exact catalytic activity 'apo-&#91;ACP&#93; + CoA = holo-&#91;ACP&#93; + adenosine 3',5'-bisphosphate + H(+)', matching Choice A verbatim. Note that the evidence code is ECO:0000250 (inferred by similarity from Q4X1W0), so this is a transferred/computational annotation rather than direct experimental validation for this specific protein, but the annotation is clearly present and consistent.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Partial elimination is possible: Choice B describes a multi-step type I PKS reaction requiring a very large multi-domain protein (typically >1000 aa), inconsistent with a 338-aa sequence; Choice C implies a cytochrome P450 or Fe-dependent hydroxylase requiring a conserved heme-binding motif (FxxGxxxCxG) absent from this sequence; Choice D implies a lipoxygenase/hydroperoxide isomerase with specific conserved motifs also absent. However, positively identifying Choice A requires recognizing PPTase-superfamily motifs (e.g., conserved regions around the active-site loop involved in phosphopantetheinyl transfer) that are not part of general undergraduate biochemistry knowledge and are not obvious from the sequence without specialized training or database lookup.


**Missing item-specific fact**

> Recognition of the specific PPTase-superfamily fold and active-site motifs (e.g., the conserved loop region and the characteristic secondary-structure arrangement of fungal PPTases) that would allow positive identification of 4'-phosphopantetheinyl transferase activity from the raw sequence, as opposed to mere elimination of the other three choices.


**Reason**

> While the three distractors can be partially excluded by sequence length and absence of diagnostic motifs (PKS size, P450 heme motif, LOX motifs), positively confirming PPTase activity from sequence alone requires specialized knowledge of PPTase-superfamily motifs or memorization of this entry's annotation. The question therefore depends on item-specific recognition rather than general biological reasoning.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices describe fundamentally different enzyme classes (PPTase, type I PKS, carotenoid hydroxylase, lipoxygenase isomerase) with distinct substrate/product chemistries. Given the 338-aa sequence, Choices B, C, and D are strongly disfavored by size and motif absence, leaving A as the only viable option. No genuine ambiguity among defensible answers.


### Important caveats

- The PPTase annotation carries evidence code ECO:0000250 (inferred by similarity from Q4X1W0), not direct experimental evidence for this Aureobasidium protein.
- The identity of the UniProt accession was inferred by the reviewer from dataset metadata; it was not provided to the evaluated model.
- The historical annotation (entry v19, released Jan 2026) already contained the PPTase annotation, so the answer was available at the approximate benchmark construction time.
- Elimination-based reasoning (ruling out B by size, C by absence of heme motif, D by absence of LOX motifs) provides partial but not fully positive justification for Choice A.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Partial elimination is possible: Choice B describes a multi-step type I PKS reaction requiring a very large multi-domain protein (typically >1000 aa), inconsistent with a 338-aa sequence; Choice C implies a cytochrome P450 or Fe-dependent hydroxylase requiring a conserved heme-binding motif (FxxGxxxCxG) absent from this sequence; Choice D implies a lipoxygenase/hydroperoxide isomerase with specific conserved motifs also absent. However, positively identifying Choice A requires recognizing PPTase-superfamily motifs (e.g., conserved regions around the active-site loop involved in phosphopantetheinyl transfer) that are not part of general undergraduate biochemistry knowledge and are not obvious from the sequence without specialized training or database lookup.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Recognition of the specific PPTase-superfamily fold and active-site motifs (e.g., the conserved loop region and the characteristic secondary-structure arrangement of fungal PPTases) that would allow positive identification of 4'-phosphopantetheinyl transferase activity from the raw sequence, as opposed to mere elimination of the other three choices.",
    "reason": "While the three distractors can be partially excluded by sequence length and absence of diagnostic motifs (PKS size, P450 heme motif, LOX motifs), positively confirming PPTase activity from sequence alone requires specialized knowledge of PPTase-superfamily motifs or memorization of this entry's annotation. The question therefore depends on item-specific recognition rather than general biological reasoning."
  },
  "case_id": "catalytic_activity_0008",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence (338 aa, SHA256 99855a22…) matches UniProt entry A0A223GB52 (PPTA_AURME) in both current and historical (entry v19) snapshots. The entry is annotated as 4'-phosphopantetheinyl transferase (EC 2.7.8.7) with the exact catalytic activity 'apo-[ACP] + CoA = holo-[ACP] + adenosine 3',5'-bisphosphate + H(+)', matching Choice A verbatim. Note that the evidence code is ECO:0000250 (inferred by similarity from Q4X1W0), so this is a transferred/computational annotation rather than direct experimental validation for this specific protein, but the annotation is clearly present and consistent."
  },
  "important_caveats": [
    "The PPTase annotation carries evidence code ECO:0000250 (inferred by similarity from Q4X1W0), not direct experimental evidence for this Aureobasidium protein.",
    "The identity of the UniProt accession was inferred by the reviewer from dataset metadata; it was not provided to the evaluated model.",
    "The historical annotation (entry v19, released Jan 2026) already contained the PPTase annotation, so the answer was available at the approximate benchmark construction time.",
    "Elimination-based reasoning (ruling out B by size, C by absence of heme motif, D by absence of LOX motifs) provides partial but not fully positive justification for Choice A."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices describe fundamentally different enzyme classes (PPTase, type I PKS, carotenoid hydroxylase, lipoxygenase isomerase) with distinct substrate/product chemistries. Given the 338-aa sequence, Choices B, C, and D are strongly disfavored by size and motif absence, leaving A as the only viable option. No genuine ambiguity among defensible answers."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0008",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence (338 aa, SHA256 99855a22…) matches UniProt entry A0A223GB52 (PPTA_AURME) in both current and historical (entry v19) snapshots. The entry is annotated as 4'-phosphopantetheinyl transferase (EC 2.7.8.7) with the exact catalytic activity 'apo-[ACP] + CoA = holo-[ACP] + adenosine 3',5'-bisphosphate + H(+)', matching Choice A verbatim. Note that the evidence code is ECO:0000250 (inferred by similarity from Q4X1W0), so this is a transferred/computational annotation rather than direct experimental validation for this specific protein, but the annotation is clearly present and consistent.",
    "evidence_ids": ["C1", "C4", "C5", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Partial elimination is possible: Choice B describes a multi-step type I PKS reaction requiring a very large multi-domain protein (typically >1000 aa), inconsistent with a 338-aa sequence; Choice C implies a cytochrome P450 or Fe-dependent hydroxylase requiring a conserved heme-binding motif (FxxGxxxCxG) absent from this sequence; Choice D implies a lipoxygenase/hydroperoxide isomerase with specific conserved motifs also absent. However, positively identifying Choice A requires recognizing PPTase-superfamily motifs (e.g., conserved regions around the active-site loop involved in phosphopantetheinyl transfer) that are not part of general undergraduate biochemistry knowledge and are not obvious from the sequence without specialized training or database lookup.",
    "missing_item_specific_fact": "Recognition of the specific PPTase-superfamily fold and active-site motifs (e.g., the conserved loop region and the characteristic secondary-structure arrangement of fungal PPTases) that would allow positive identification of 4'-phosphopantetheinyl transferase activity from the raw sequence, as opposed to mere elimination of the other three choices.",
    "reason": "While the three distractors can be partially excluded by sequence length and absence of diagnostic motifs (PKS size, P450 heme motif, LOX motifs), positively confirming PPTase activity from sequence alone requires specialized knowledge of PPTase-superfamily motifs or memorization of this entry's annotation. The question therefore depends on item-specific recognition rather than general biological reasoning."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices describe fundamentally different enzyme classes (PPTase, type I PKS, carotenoid hydroxylase, lipoxygenase isomerase) with distinct substrate/product chemistries. Given the 338-aa sequence, Choices B, C, and D are strongly disfavored by size and motif absence, leaving A as the only viable option. No genuine ambiguity among defensible answers."
  },
  "important_caveats": [
    "The PPTase annotation carries evidence code ECO:0000250 (inferred by similarity from Q4X1W0), not direct experimental evidence for this Aureobasidium protein.",
    "The identity of the UniProt accession was inferred by the reviewer from dataset metadata; it was not provided to the evaluated model.",
    "The historical annotation (entry v19, released Jan 2026) already contained the PPTase annotation, so the answer was available at the approximate benchmark construction time.",
    "Elimination-based reasoning (ruling out B by size, C by absence of heme motif, D by absence of LOX motifs) provides partial but not fully positive justification for Choice A."
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

**Accession:** `A0A223GB52` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 19. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223GB52.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:40.730186+00:00.  

```json
"A0A223GB52"
```

Source SHA-256: `1f85238d8648a62503daea44a4355d8b9818bf0320c1e3b669761c3f74e77098`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223GB52.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:40.730186+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q4X1W0","source":"UniProtKB"}],"value":"Acyl-carrier-protein synthase"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q4X1W0","source":"UniProtKB"}],"value":"Phosphopantetheine:protein transferase"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q4X1W0","source":"UniProtKB"}],"value":"2.7.8.7"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"Ref.2","source":"Reference"}],"value":"4'-phosphopantetheinyl transferase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"Ref.2","source":"Reference"}],"value":"PPTase"}]}}
```

Source SHA-256: `1f85238d8648a62503daea44a4355d8b9818bf0320c1e3b669761c3f74e77098`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223GB52.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:40.730186+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"2.7.8.7","evidences":[{"evidenceCode":"ECO:0000250","id":"Q4X1W0","source":"UniProtKB"}],"name":"apo-[ACP] + CoA = holo-[ACP] + adenosine 3',5'-bisphosphate + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:12068"},{"database":"Rhea","id":"RHEA-COMP:9685"},{"database":"Rhea","id":"RHEA-COMP:9690"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:29999"},{"database":"ChEBI","id":"CHEBI:57287"},{"database":"ChEBI","id":"CHEBI:58343"},{"database":"ChEBI","id":"CHEBI:64479"}]}}
```

Source SHA-256: `1f85238d8648a62503daea44a4355d8b9818bf0320c1e3b669761c3f74e77098`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A223GB52?format=txt&versions=19)  
**Locator:** `lines 6-10`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 19 / 1.  
**Retrieved:** 2026-11-02T04:24:42.924113+00:00.  

```text
DE   RecName: Full=4'-phosphopantetheinyl transferase {ECO:0000303|Ref.2};
DE            Short=PPTase {ECO:0000303|Ref.2};
DE            EC=2.7.8.7 {ECO:0000250|UniProtKB:Q4X1W0};
DE   AltName: Full=Acyl-carrier-protein synthase {ECO:0000250|UniProtKB:Q4X1W0};
DE   AltName: Full=Phosphopantetheine:protein transferase {ECO:0000250|UniProtKB:Q4X1W0};
```

Source SHA-256: `b160e3bc52b04e40113462a98f748a49deb270020947dd63f379ab16fdcd21d0`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A223GB52?format=txt&versions=19)  
**Locator:** `lines 65-70`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 19 / 1.  
**Retrieved:** 2026-11-02T04:24:42.924113+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=apo-[ACP] + CoA = holo-[ACP] + adenosine 3',5'-bisphosphate +
CC         H(+); Xref=Rhea:RHEA:12068, Rhea:RHEA-COMP:9685, Rhea:RHEA-COMP:9690,
CC         ChEBI:CHEBI:15378, ChEBI:CHEBI:29999, ChEBI:CHEBI:57287,
CC         ChEBI:CHEBI:58343, ChEBI:CHEBI:64479; EC=2.7.8.7;
CC         Evidence={ECO:0000250|UniProtKB:Q4X1W0};
```

Source SHA-256: `b160e3bc52b04e40113462a98f748a49deb270020947dd63f379ab16fdcd21d0`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 8. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
