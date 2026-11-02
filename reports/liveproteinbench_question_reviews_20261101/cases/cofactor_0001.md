# cofactor_0001

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `cofactor`  
**Author expected answer:** **D** — &#91;4Fe-4S&#93; cluster

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MENQHQKFISRRNFIKTSALLGGTAFLGTGLPNIKKTYSKELDYVGNFEYPLAKPENILYSACLQCTVACSIKVKINNGVCMKIDGNPYSAMNLGENLPYDLSPKEAVSIDGKLCPKGQAGIQHAYDPYRLRKVIKRDGPRGSGKWKTIPYDQAIDEIVNGGNIFKDIGENQNVEGLKDIFVLKDPKVAKAMADDVTKIRKKEMTVDEFKAKHKDNLDVLIDPNHPDLGPKNNQFLFQVGRIHNGRIEFTKRFVNDSFGSVNWIEKTTLCGQTSNKAWVHSTREYLEGKWTGGIKSPRPDHRNTEFLLVFGSIVFEANYGPVQETEPITEGLESGRLKIAVVDPRLTKVASKAWKWVPIKPGNDAAFALGMIRWIIENERYDTKFLQNATRLAATNSDEPSYSNATYLVKVEKDGRAAKHLRANEIGIGTEKEFVVISNGKPAAVDPENSNLAIQGELFVDTNLEGIKVKSPLQLIKEEAYSKELAEWAELSGAKQKDIEDISKEFTSHGKKAAVEFYRGAIKHTNGWYNGQALIVLNHLIGNMNWQGGISNTGGGWSYIGDKEGQPYPMANLHPNKLSKFGVPITKEGWKYEESTLFEGYPAKRPWYPFSGNVAQETWPSISDGYPYKIKAALISSHSPMYSLPGGHVQLKTLLDTEKVPLLIASDIVIGDSSQYVDYIFPDLTYLERWATPGQSHHIRVKVNQVRQPVIAPLTENATVFGEEVPISLEALMMSISEKVGLSGFGKDAFGPGKDLNRMEDFYLKLVANIASGNKQGELVKAADSEEMELFKSSHRHLPKTVYDIEKWQQTLTSDEWKRVVYVLNRGGRFASSDDAYEGSFIKKKIPGLARLYLEEIADSRNSISGNYFTGYPKYLPIMDMAENLINDEGEFHLITNKEVFGTQSRTITNYWAQLALQPENFVVLNSVDAKKLKVDNGDKVLVTSTSNPKGEHLIAADESRPTIGKVKIVEGIRPGVVAISTHYGHWGYGARDIQIDGEVVKGEEVRGLGIHPNPLFRLDDNLRGTTLSDPIGGSASYYDTRVNIQRV

[Multiple Choices]
A. heme
B. NAD(+)
C. tungstopterin
D. [4Fe-4S] cluster
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

> The exact sequence matches a UniProt entry annotated as binding a &#91;4Fe-4S&#93; cluster. However, that annotation is transferred from a related protein (ECO:0000250), not direct experimental evidence for this sequence. The same entry also annotates a Mo-bis-MGD cofactor, so the cluster is not the protein’s only annotated cofactor.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may permit broad enzyme-family inference, but cysteine residues or generic family features alone do not establish that this particular protein binds a &#91;4Fe-4S&#93; cluster rather than another listed cofactor.


**Missing item-specific fact**

> The protein-specific cofactor annotation linking this sequence to a &#91;4Fe-4S&#93; cluster; the supplied input gives no protein identity, experimental binding result, or sufficiently diagnostic cofactor-site evidence.


**Reason**

> Selecting D depends on an item-specific cofactor fact absent from the question. Reviewer-only annotation supports the key, but does not make the original sequence-and-choices input reasoning-supported.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed choices, only D is annotated for this sequence. The protein is also annotated to bind Mo-bis-MGD, but that exact cofactor is not offered; tungstopterin is not the same annotation.


### Important caveats

- The cofactor evidence is similarity-transferred rather than direct experimental evidence for the supplied sequence.
- The wording may suggest a single required cofactor, while the sequence-matched entry annotates more than one.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence may permit broad enzyme-family inference, but cysteine residues or generic family features alone do not establish that this particular protein binds a [4Fe-4S] cluster rather than another listed cofactor.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific cofactor annotation linking this sequence to a [4Fe-4S] cluster; the supplied input gives no protein identity, experimental binding result, or sufficiently diagnostic cofactor-site evidence.",
    "reason": "Selecting D depends on an item-specific cofactor fact absent from the question. Reviewer-only annotation supports the key, but does not make the original sequence-and-choices input reasoning-supported."
  },
  "case_id": "cofactor_0001",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C6",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as binding a [4Fe-4S] cluster. However, that annotation is transferred from a related protein (ECO:0000250), not direct experimental evidence for this sequence. The same entry also annotates a Mo-bis-MGD cofactor, so the cluster is not the protein’s only annotated cofactor."
  },
  "important_caveats": [
    "The cofactor evidence is similarity-transferred rather than direct experimental evidence for the supplied sequence.",
    "The wording may suggest a single required cofactor, while the sequence-matched entry annotates more than one."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, only D is annotated for this sequence. The protein is also annotated to bind Mo-bis-MGD, but that exact cofactor is not offered; tungstopterin is not the same annotation."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0001",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as binding a [4Fe-4S] cluster. However, that annotation is transferred from a related protein (ECO:0000250), not direct experimental evidence for this sequence. The same entry also annotates a Mo-bis-MGD cofactor, so the cluster is not the protein’s only annotated cofactor.",
    "evidence_ids": ["C1", "C5", "C6", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may permit broad enzyme-family inference, but cysteine residues or generic family features alone do not establish that this particular protein binds a [4Fe-4S] cluster rather than another listed cofactor.",
    "missing_item_specific_fact": "The protein-specific cofactor annotation linking this sequence to a [4Fe-4S] cluster; the supplied input gives no protein identity, experimental binding result, or sufficiently diagnostic cofactor-site evidence.",
    "reason": "Selecting D depends on an item-specific cofactor fact absent from the question. Reviewer-only annotation supports the key, but does not make the original sequence-and-choices input reasoning-supported."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, only D is annotated for this sequence. The protein is also annotated to bind Mo-bis-MGD, but that exact cofactor is not offered; tungstopterin is not the same annotation."
  },
  "important_caveats": [
    "The cofactor evidence is similarity-transferred rather than direct experimental evidence for the supplied sequence.",
    "The wording may suggest a single required cofactor, while the sequence-matched entry annotates more than one."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt annotation for A0A0A8X0K1 (Selenate reductase subunit A, EC 1.97.1.14) lists &#91;4Fe-4S&#93; cluster as a cofactor (C5, H4). However, the annotation evidence code is ECO:0000250 (inferred by similarity from Q7WTU0), not direct experimental measurement. The entry also annotates a second cofactor, Mo-bis(molybdopterin guanine dinucleotide) (C6, H5), meaning the protein actually requires two cofactors. Since only &#91;4Fe-4S&#93; appears among the four choices, the expected answer is the only annotated cofactor present in the option set, making it supported by the database annotation.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4), [C6](#evidence-c6), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> By elimination using general biological knowledge: (1) Tungstopterin (C) is found almost exclusively in hyperthermophilic archaea (e.g., Pyrococcus, Thermococcus); a bacterial protein with a clear N-terminal signal peptide (MENQHQKFISRRNFIKTSALLGGTAFLGTGLPNIKKTYSKELDYVGNFEYPLAKPEN...) is extremely unlikely to use tungstopterin. (2) NAD(+) (B) requires a Rossmann-fold motif (GxGxxG); no such motif is apparent in the 1048-aa sequence. (3) Heme (A) requires characteristic CXXCH or bis-His coordination motifs; none are clearly identifiable. (4) The sequence contains multiple Cys residues in clustered arrangements (e.g., C in 'GVCMK', C in 'KLCPKG', C in 'TTLCGQ') consistent with Fe-S cluster coordination in a large respiratory enzyme. This elimination logic, combined with the Cys pattern, meaningfully distinguishes D from the other three options.


**Missing item-specific fact**

> Positive confirmation that this specific protein binds a &#91;4Fe-4S&#93; (rather than &#91;2Fe-2S&#93; or &#91;3Fe-4S&#93;) cluster requires recognition of the DMSO-reductase family architecture or the specific UniProt annotation. The Cys residues alone are suggestive but not definitive for the exact cluster type.


**Reason**

> Elimination of tungstopterin (archaeal-specific), NAD+ (no Rossmann fold), and heme (no heme-binding motif) is achievable from general biological knowledge and sequence inspection. The residual Cys pattern supports Fe-S. However, the precise identification of &#91;4Fe-4S&#93; over other Fe-S types, and the confirmation that this protein is a member of the DMSO-reductase family, still leans on protein-family knowledge. The question is answerable by reasoning but the margin is not large.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the four choices, only &#91;4Fe-4S&#93; is an annotated cofactor for this protein. The other actual cofactor (Mo-bis-MGD) is not offered. Tungstopterin, NAD+, and heme are not annotated and are eliminated by general biological reasoning. No ambiguity among the presented options.


### Important caveats

- Both cofactor annotations (&#91;4Fe-4S&#93; and Mo-bis-MGD) carry evidence code ECO:0000250 (inferred by similarity from Q7WTU0), not direct experimental validation for this specific protein.
- The protein actually requires TWO cofactors; the question asks for 'the specific cofactor' (singular), which is a minor wording imprecision but does not affect answerability since only one of the two is among the choices.
- The UniProt entry was first released in 2025-02; the author data-construction date is unknown. If the benchmark was constructed before this entry existed, the annotation source may differ.
- Tungstopterin elimination relies on the general rule that tungsten-containing enzymes are predominantly archaeal; rare bacterial exceptions exist but are not relevant here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "By elimination using general biological knowledge: (1) Tungstopterin (C) is found almost exclusively in hyperthermophilic archaea (e.g., Pyrococcus, Thermococcus); a bacterial protein with a clear N-terminal signal peptide (MENQHQKFISRRNFIKTSALLGGTAFLGTGLPNIKKTYSKELDYVGNFEYPLAKPEN...) is extremely unlikely to use tungstopterin. (2) NAD(+) (B) requires a Rossmann-fold motif (GxGxxG); no such motif is apparent in the 1048-aa sequence. (3) Heme (A) requires characteristic CXXCH or bis-His coordination motifs; none are clearly identifiable. (4) The sequence contains multiple Cys residues in clustered arrangements (e.g., C in 'GVCMK', C in 'KLCPKG', C in 'TTLCGQ') consistent with Fe-S cluster coordination in a large respiratory enzyme. This elimination logic, combined with the Cys pattern, meaningfully distinguishes D from the other three options.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Positive confirmation that this specific protein binds a [4Fe-4S] (rather than [2Fe-2S] or [3Fe-4S]) cluster requires recognition of the DMSO-reductase family architecture or the specific UniProt annotation. The Cys residues alone are suggestive but not definitive for the exact cluster type.",
    "reason": "Elimination of tungstopterin (archaeal-specific), NAD+ (no Rossmann fold), and heme (no heme-binding motif) is achievable from general biological knowledge and sequence inspection. The residual Cys pattern supports Fe-S. However, the precise identification of [4Fe-4S] over other Fe-S types, and the confirmation that this protein is a member of the DMSO-reductase family, still leans on protein-family knowledge. The question is answerable by reasoning but the margin is not large."
  },
  "case_id": "cofactor_0001",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4",
      "C6",
      "H5"
    ],
    "judgment": "supported",
    "reason": "UniProt annotation for A0A0A8X0K1 (Selenate reductase subunit A, EC 1.97.1.14) lists [4Fe-4S] cluster as a cofactor (C5, H4). However, the annotation evidence code is ECO:0000250 (inferred by similarity from Q7WTU0), not direct experimental measurement. The entry also annotates a second cofactor, Mo-bis(molybdopterin guanine dinucleotide) (C6, H5), meaning the protein actually requires two cofactors. Since only [4Fe-4S] appears among the four choices, the expected answer is the only annotated cofactor present in the option set, making it supported by the database annotation."
  },
  "important_caveats": [
    "Both cofactor annotations ([4Fe-4S] and Mo-bis-MGD) carry evidence code ECO:0000250 (inferred by similarity from Q7WTU0), not direct experimental validation for this specific protein.",
    "The protein actually requires TWO cofactors; the question asks for 'the specific cofactor' (singular), which is a minor wording imprecision but does not affect answerability since only one of the two is among the choices.",
    "The UniProt entry was first released in 2025-02; the author data-construction date is unknown. If the benchmark was constructed before this entry existed, the annotation source may differ.",
    "Tungstopterin elimination relies on the general rule that tungsten-containing enzymes are predominantly archaeal; rare bacterial exceptions exist but are not relevant here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four choices, only [4Fe-4S] is an annotated cofactor for this protein. The other actual cofactor (Mo-bis-MGD) is not offered. Tungstopterin, NAD+, and heme are not annotated and are eliminated by general biological reasoning. No ambiguity among the presented options."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0001",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt annotation for A0A0A8X0K1 (Selenate reductase subunit A, EC 1.97.1.14) lists [4Fe-4S] cluster as a cofactor (C5, H4). However, the annotation evidence code is ECO:0000250 (inferred by similarity from Q7WTU0), not direct experimental measurement. The entry also annotates a second cofactor, Mo-bis(molybdopterin guanine dinucleotide) (C6, H5), meaning the protein actually requires two cofactors. Since only [4Fe-4S] appears among the four choices, the expected answer is the only annotated cofactor present in the option set, making it supported by the database annotation.",
    "evidence_ids": ["C5", "H4", "C6", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "By elimination using general biological knowledge: (1) Tungstopterin (C) is found almost exclusively in hyperthermophilic archaea (e.g., Pyrococcus, Thermococcus); a bacterial protein with a clear N-terminal signal peptide (MENQHQKFISRRNFIKTSALLGGTAFLGTGLPNIKKTYSKELDYVGNFEYPLAKPEN...) is extremely unlikely to use tungstopterin. (2) NAD(+) (B) requires a Rossmann-fold motif (GxGxxG); no such motif is apparent in the 1048-aa sequence. (3) Heme (A) requires characteristic CXXCH or bis-His coordination motifs; none are clearly identifiable. (4) The sequence contains multiple Cys residues in clustered arrangements (e.g., C in 'GVCMK', C in 'KLCPKG', C in 'TTLCGQ') consistent with Fe-S cluster coordination in a large respiratory enzyme. This elimination logic, combined with the Cys pattern, meaningfully distinguishes D from the other three options.",
    "missing_item_specific_fact": "Positive confirmation that this specific protein binds a [4Fe-4S] (rather than [2Fe-2S] or [3Fe-4S]) cluster requires recognition of the DMSO-reductase family architecture or the specific UniProt annotation. The Cys residues alone are suggestive but not definitive for the exact cluster type.",
    "reason": "Elimination of tungstopterin (archaeal-specific), NAD+ (no Rossmann fold), and heme (no heme-binding motif) is achievable from general biological knowledge and sequence inspection. The residual Cys pattern supports Fe-S. However, the precise identification of [4Fe-4S] over other Fe-S types, and the confirmation that this protein is a member of the DMSO-reductase family, still leans on protein-family knowledge. The question is answerable by reasoning but the margin is not large."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four choices, only [4Fe-4S] is an annotated cofactor for this protein. The other actual cofactor (Mo-bis-MGD) is not offered. Tungstopterin, NAD+, and heme are not annotated and are eliminated by general biological reasoning. No ambiguity among the presented options."
  },
  "important_caveats": [
    "Both cofactor annotations ([4Fe-4S] and Mo-bis-MGD) carry evidence code ECO:0000250 (inferred by similarity from Q7WTU0), not direct experimental validation for this specific protein.",
    "The protein actually requires TWO cofactors; the question asks for 'the specific cofactor' (singular), which is a minor wording imprecision but does not affect answerability since only one of the two is among the choices.",
    "The UniProt entry was first released in 2025-02; the author data-construction date is unknown. If the benchmark was constructed before this entry existed, the annotation source may differ.",
    "Tungstopterin elimination relies on the general rule that tungsten-containing enzymes are predominantly archaeal; rare bacterial exceptions exist but are not relevant here."
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

**Accession:** `A0A0A8X0K1` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 39. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0A8X0K1.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:23:55.467166+00:00.  

```json
"A0A0A8X0K1"
```

Source SHA-256: `d9ac69d7201b1c8bcae325d0c3c51746a094db840f9070cb1335ab6fce005680`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0A8X0K1.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:23:55.467166+00:00.  

```json
{"cofactors":[{"cofactorCrossReference":{"database":"ChEBI","id":"CHEBI:49883"},"evidences":[{"evidenceCode":"ECO:0000250","id":"Q7WTU0","source":"UniProtKB"}],"name":"[4Fe-4S] cluster"}],"commentType":"COFACTOR","note":{"texts":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q7WTU0","source":"UniProtKB"}],"value":"Binds 1 [4Fe-4S] cluster."}]}}
```

Source SHA-256: `d9ac69d7201b1c8bcae325d0c3c51746a094db840f9070cb1335ab6fce005680`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0A8X0K1.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:23:55.467166+00:00.  

```json
{"cofactors":[{"cofactorCrossReference":{"database":"ChEBI","id":"CHEBI:60539"},"evidences":[{"evidenceCode":"ECO:0000250","id":"Q7WTU0","source":"UniProtKB"}],"name":"Mo-bis(molybdopterin guanine dinucleotide)"}],"commentType":"COFACTOR","note":{"texts":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q7WTU0","source":"UniProtKB"}],"value":"Binds 1 molybdenum-bis(molybdopterin guanine dinucleotide) (Mo-bis-MGD) cofactor per subunit."}]}}
```

Source SHA-256: `d9ac69d7201b1c8bcae325d0c3c51746a094db840f9070cb1335ab6fce005680`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0A8X0K1?format=txt&versions=39)  
**Locator:** `lines 46-49`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 39 / 1.  
**Retrieved:** 2026-11-02T04:23:57.438981+00:00.  

```text
CC   -!- COFACTOR:
CC       Name=[4Fe-4S] cluster; Xref=ChEBI:CHEBI:49883;
CC         Evidence={ECO:0000250|UniProtKB:Q7WTU0};
CC       Note=Binds 1 [4Fe-4S] cluster. {ECO:0000250|UniProtKB:Q7WTU0};
```

Source SHA-256: `70a7343ad00a497450d77471ce95793d07ed552a4380e15f246581d88bf602aa`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0A8X0K1?format=txt&versions=39)  
**Locator:** `lines 50-54`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 39 / 1.  
**Retrieved:** 2026-11-02T04:23:57.438981+00:00.  

```text
CC   -!- COFACTOR:
CC       Name=Mo-bis(molybdopterin guanine dinucleotide);
CC         Xref=ChEBI:CHEBI:60539; Evidence={ECO:0000250|UniProtKB:Q7WTU0};
CC       Note=Binds 1 molybdenum-bis(molybdopterin guanine dinucleotide) (Mo-
CC       bis-MGD) cofactor per subunit. {ECO:0000250|UniProtKB:Q7WTU0};
```

Source SHA-256: `70a7343ad00a497450d77471ce95793d07ed552a4380e15f246581d88bf602aa`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 1. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
