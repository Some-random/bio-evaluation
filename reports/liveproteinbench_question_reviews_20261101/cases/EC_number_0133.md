# EC_number_0133

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **C** — 1.3.1.36

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MAGETTQLDLSVKAVGWGAADASGTLQPIKFYRRTPGERDVKIRVLYCGVCNFDMEMVRNKWGFTRYPYVFGHETAGEVIEVGSKVQKFKVGDKVGVGCMVGSCGKCFNCQNGMENYCPEPNMADGSVYREQQGEPSFGGCSNVMVVDEKFVLRWPENLPQDTGVPLLCAGIVVYSPMKYMGLDKPGKHIGVIGLGGLGSIAVKFIKAFGGKATVISTSKRKEKEAIEEHGADAFVVNTDTEKLQALAGTMDGVVDTTPGGRTPMSLMLNLLKFDGVVLLVGAPETLFELPVQPLILGRRKIIGSSTGGLKEYQETLDFAAQHNIVCDTEVIGIDYLSTAMERIKNLDVKYRFAIDIGNTLKYED

[Multiple Choices]
A. 1.3.1.73
B. 1.14.14.126
C. 1.3.1.36
D. 3.6.1.5
```

<details>
<summary>Original system instructions, verbatim</summary>

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

## GPT-6 Luna

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The exact supplied sequence matches the UniProt entry annotated as geissoschizine synthase, EC 1.3.1.36, with a corresponding catalytic reaction. The annotation is transferred from a homolog (ECO:0000250), so it supports the key but is not direct experimental evidence for this sequence.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may suggest an enzyme, but no supplied context or general sequence feature uniquely establishes the geissoschizine reaction or distinguishes this precise EC number from the alternatives.


**Missing item-specific fact**

> The protein-specific functional annotation identifying this sequence as geissoschizine synthase and associating it with EC 1.3.1.36.


**Reason**

> Selecting the precise EC classification depends on protein-specific functional knowledge absent from the prompt; recognizing the sequence or consulting an annotation would supply that missing information.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The listed choices specify distinct EC classifications, and the matched sequence annotation supports C.


### Important caveats

- The supporting UniProt EC and catalytic-activity annotations are similarity-transferred from a homolog, not shown here as direct experimental confirmation for the supplied protein.
- The sequence match applies to the cited database record; the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence may suggest an enzyme, but no supplied context or general sequence feature uniquely establishes the geissoschizine reaction or distinguishes this precise EC number from the alternatives.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific functional annotation identifying this sequence as geissoschizine synthase and associating it with EC 1.3.1.36.",
    "reason": "Selecting the precise EC classification depends on protein-specific functional knowledge absent from the prompt; recognizing the sequence or consulting an annotation would supply that missing information."
  },
  "case_id": "EC_number_0133",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact supplied sequence matches the UniProt entry annotated as geissoschizine synthase, EC 1.3.1.36, with a corresponding catalytic reaction. The annotation is transferred from a homolog (ECO:0000250), so it supports the key but is not direct experimental evidence for this sequence."
  },
  "important_caveats": [
    "The supporting UniProt EC and catalytic-activity annotations are similarity-transferred from a homolog, not shown here as direct experimental confirmation for the supplied protein.",
    "The sequence match applies to the cited database record; the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The listed choices specify distinct EC classifications, and the matched sequence annotation supports C."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0133",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact supplied sequence matches the UniProt entry annotated as geissoschizine synthase, EC 1.3.1.36, with a corresponding catalytic reaction. The annotation is transferred from a homolog (ECO:0000250), so it supports the key but is not direct experimental evidence for this sequence.",
    "evidence_ids": ["C1", "C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may suggest an enzyme, but no supplied context or general sequence feature uniquely establishes the geissoschizine reaction or distinguishes this precise EC number from the alternatives.",
    "missing_item_specific_fact": "The protein-specific functional annotation identifying this sequence as geissoschizine synthase and associating it with EC 1.3.1.36.",
    "reason": "Selecting the precise EC classification depends on protein-specific functional knowledge absent from the prompt; recognizing the sequence or consulting an annotation would supply that missing information."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The listed choices specify distinct EC classifications, and the matched sequence annotation supports C."
  },
  "important_caveats": [
    "The supporting UniProt EC and catalytic-activity annotations are similarity-transferred from a homolog, not shown here as direct experimental confirmation for the supplied protein.",
    "The sequence match applies to the cited database record; the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry P0DXJ1 (sequence SHA256 matched) annotates this protein as Geissoschizine synthase with EC 1.3.1.36. The catalytic reaction is (19E)-geissoschizine + NADP(+) = 4,21-dehydrogeissoschizine + NADPH. However, the EC annotation carries evidence code ECO:0000250 (similarity to UniProtKB:W8JWW7), meaning it is a computational inference by homology rather than direct experimental characterization of this specific protein's substrate specificity. The protein name and pathway context derive from PubMed 38212296 (Nat. Commun. 2024), which characterized the ajmaline biosynthesis pathway in Rauvolfia serpentina. The key is supported by current database annotation but rests on transferred similarity evidence.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains recognizable Rossmann-fold NAD(P)-binding motifs (e.g., GCMVGSCGKCFNC, GGLGSIAVKFIK) consistent with an oxidoreductase, which rules out D (3.6.1.5, a hydrolase/GTPase) and B (1.14.14.126, a cytochrome P450 requiring heme-binding motifs like FxxGxxxCxG). However, both remaining options A (1.3.1.73) and C (1.3.1.36) belong to the same EC subclass 1.3.1 (oxidoreductases acting on CH-CH group with NAD+/NADP+ as acceptor). Distinguishing between these two requires knowing the specific substrate (geissoschizine vs. the substrate of 1.3.1.73), which cannot be reliably inferred from general sequence features alone.


**Missing item-specific fact**

> The specific substrate identity of this enzyme (geissoschizine) and the distinction between the substrates of EC 1.3.1.73 and EC 1.3.1.36. Additionally, knowledge that Rauvolfia serpentina alkaloid biosynthesis involves geissoschizine synthase at this pathway step is item-specific pathway knowledge, not general biological reasoning derivable from the sequence.


**Reason**

> While the sequence supports broad classification as an NAD(P)-dependent dehydrogenase (eliminating D and B), the critical distinction between the two 1.3.1.x options requires knowing which specific small-molecule substrate the enzyme acts upon. No general sequence heuristic reliably distinguishes between two dehydrogenases in the same EC subclass by substrate identity. Selection of C over A depends on memorizing this protein's annotation or knowing Rauvolfia serpentina's alkaloid biosynthetic pathway in detail.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "C"
]
```

> Both A (1.3.1.73) and C (1.3.1.36) fall within EC subclass 1.3.1 and describe NAD(P)-dependent dehydrogenases acting on CH-CH bonds. From the sequence alone, a model can identify the enzyme as an NAD(P)-binding oxidoreductase but cannot confidently distinguish which specific substrate (and thus which final EC digit) applies. Without memorized pathway knowledge of Rauvolfia serpentina alkaloid biosynthesis, both A and C are plausible choices for a sequence-based predictor.


### Important caveats

- The EC annotation for P0DXJ1 is based on ECO:0000250 (similarity to W8JWW7), not direct experimental assay of this protein's substrate specificity. The annotation is a computational transfer.
- The protein was identified in the context of the ajmaline biosynthesis pathway (PubMed 38212296, 2024), but the specific EC assignment for this enzyme relies on homology rather than in vitro substrate characterization of P0DXJ1 itself.
- The UniProt entry was first public on 2025-06-18; the author's source snapshot date is unknown, so the annotation may not have been available when the benchmark was constructed.
- The sequence match is confirmed (SHA256 identical between benchmark and UniProt P0DXJ1, 365 aa).

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains recognizable Rossmann-fold NAD(P)-binding motifs (e.g., GCMVGSCGKCFNC, GGLGSIAVKFIK) consistent with an oxidoreductase, which rules out D (3.6.1.5, a hydrolase/GTPase) and B (1.14.14.126, a cytochrome P450 requiring heme-binding motifs like FxxGxxxCxG). However, both remaining options A (1.3.1.73) and C (1.3.1.36) belong to the same EC subclass 1.3.1 (oxidoreductases acting on CH-CH group with NAD+/NADP+ as acceptor). Distinguishing between these two requires knowing the specific substrate (geissoschizine vs. the substrate of 1.3.1.73), which cannot be reliably inferred from general sequence features alone.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific substrate identity of this enzyme (geissoschizine) and the distinction between the substrates of EC 1.3.1.73 and EC 1.3.1.36. Additionally, knowledge that Rauvolfia serpentina alkaloid biosynthesis involves geissoschizine synthase at this pathway step is item-specific pathway knowledge, not general biological reasoning derivable from the sequence.",
    "reason": "While the sequence supports broad classification as an NAD(P)-dependent dehydrogenase (eliminating D and B), the critical distinction between the two 1.3.1.x options requires knowing which specific small-molecule substrate the enzyme acts upon. No general sequence heuristic reliably distinguishes between two dehydrogenases in the same EC subclass by substrate identity. Selection of C over A depends on memorizing this protein's annotation or knowing Rauvolfia serpentina's alkaloid biosynthetic pathway in detail."
  },
  "case_id": "EC_number_0133",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry P0DXJ1 (sequence SHA256 matched) annotates this protein as Geissoschizine synthase with EC 1.3.1.36. The catalytic reaction is (19E)-geissoschizine + NADP(+) = 4,21-dehydrogeissoschizine + NADPH. However, the EC annotation carries evidence code ECO:0000250 (similarity to UniProtKB:W8JWW7), meaning it is a computational inference by homology rather than direct experimental characterization of this specific protein's substrate specificity. The protein name and pathway context derive from PubMed 38212296 (Nat. Commun. 2024), which characterized the ajmaline biosynthesis pathway in Rauvolfia serpentina. The key is supported by current database annotation but rests on transferred similarity evidence."
  },
  "important_caveats": [
    "The EC annotation for P0DXJ1 is based on ECO:0000250 (similarity to W8JWW7), not direct experimental assay of this protein's substrate specificity. The annotation is a computational transfer.",
    "The protein was identified in the context of the ajmaline biosynthesis pathway (PubMed 38212296, 2024), but the specific EC assignment for this enzyme relies on homology rather than in vitro substrate characterization of P0DXJ1 itself.",
    "The UniProt entry was first public on 2025-06-18; the author's source snapshot date is unknown, so the annotation may not have been available when the benchmark was constructed.",
    "The sequence match is confirmed (SHA256 identical between benchmark and UniProt P0DXJ1, 365 aa)."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "C"
    ],
    "reason": "Both A (1.3.1.73) and C (1.3.1.36) fall within EC subclass 1.3.1 and describe NAD(P)-dependent dehydrogenases acting on CH-CH bonds. From the sequence alone, a model can identify the enzyme as an NAD(P)-binding oxidoreductase but cannot confidently distinguish which specific substrate (and thus which final EC digit) applies. Without memorized pathway knowledge of Rauvolfia serpentina alkaloid biosynthesis, both A and C are plausible choices for a sequence-based predictor."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0133",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry P0DXJ1 (sequence SHA256 matched) annotates this protein as Geissoschizine synthase with EC 1.3.1.36. The catalytic reaction is (19E)-geissoschizine + NADP(+) = 4,21-dehydrogeissoschizine + NADPH. However, the EC annotation carries evidence code ECO:0000250 (similarity to UniProtKB:W8JWW7), meaning it is a computational inference by homology rather than direct experimental characterization of this specific protein's substrate specificity. The protein name and pathway context derive from PubMed 38212296 (Nat. Commun. 2024), which characterized the ajmaline biosynthesis pathway in Rauvolfia serpentina. The key is supported by current database annotation but rests on transferred similarity evidence.",
    "evidence_ids": ["C1", "C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains recognizable Rossmann-fold NAD(P)-binding motifs (e.g., GCMVGSCGKCFNC, GGLGSIAVKFIK) consistent with an oxidoreductase, which rules out D (3.6.1.5, a hydrolase/GTPase) and B (1.14.14.126, a cytochrome P450 requiring heme-binding motifs like FxxGxxxCxG). However, both remaining options A (1.3.1.73) and C (1.3.1.36) belong to the same EC subclass 1.3.1 (oxidoreductases acting on CH-CH group with NAD+/NADP+ as acceptor). Distinguishing between these two requires knowing the specific substrate (geissoschizine vs. the substrate of 1.3.1.73), which cannot be reliably inferred from general sequence features alone.",
    "missing_item_specific_fact": "The specific substrate identity of this enzyme (geissoschizine) and the distinction between the substrates of EC 1.3.1.73 and EC 1.3.1.36. Additionally, knowledge that Rauvolfia serpentina alkaloid biosynthesis involves geissoschizine synthase at this pathway step is item-specific pathway knowledge, not general biological reasoning derivable from the sequence.",
    "reason": "While the sequence supports broad classification as an NAD(P)-dependent dehydrogenase (eliminating D and B), the critical distinction between the two 1.3.1.x options requires knowing which specific small-molecule substrate the enzyme acts upon. No general sequence heuristic reliably distinguishes between two dehydrogenases in the same EC subclass by substrate identity. Selection of C over A depends on memorizing this protein's annotation or knowing Rauvolfia serpentina's alkaloid biosynthetic pathway in detail."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "C"],
    "reason": "Both A (1.3.1.73) and C (1.3.1.36) fall within EC subclass 1.3.1 and describe NAD(P)-dependent dehydrogenases acting on CH-CH bonds. From the sequence alone, a model can identify the enzyme as an NAD(P)-binding oxidoreductase but cannot confidently distinguish which specific substrate (and thus which final EC digit) applies. Without memorized pathway knowledge of Rauvolfia serpentina alkaloid biosynthesis, both A and C are plausible choices for a sequence-based predictor."
  },
  "important_caveats": [
    "The EC annotation for P0DXJ1 is based on ECO:0000250 (similarity to W8JWW7), not direct experimental assay of this protein's substrate specificity. The annotation is a computational transfer.",
    "The protein was identified in the context of the ajmaline biosynthesis pathway (PubMed 38212296, 2024), but the specific EC assignment for this enzyme relies on homology rather than in vitro substrate characterization of P0DXJ1 itself.",
    "The UniProt entry was first public on 2025-06-18; the author's source snapshot date is unknown, so the annotation may not have been available when the benchmark was constructed.",
    "The sequence match is confirmed (SHA256 identical between benchmark and UniProt P0DXJ1, 365 aa)."
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

**Accession:** `P0DXJ1` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 2. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ1.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:29.884516+00:00.  

```json
"P0DXJ1"
```

Source SHA-256: `6eda11173d33f799125da302047e13f2dbcebc81de87a50235cb3bf62d181ed5`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ1.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:29.884516+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"W8JWW7","source":"UniProtKB"}],"value":"1.3.1.36"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"38212296","source":"PubMed"}],"value":"Geissoschizine synthase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"38212296","source":"PubMed"}],"value":"RsGS"}]}}
```

Source SHA-256: `6eda11173d33f799125da302047e13f2dbcebc81de87a50235cb3bf62d181ed5`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ1.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:29.884516+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"right-to-left","evidences":[{"evidenceCode":"ECO:0000250","id":"W8JWW7","source":"UniProtKB"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:11378"}}],"reaction":{"ecNumber":"1.3.1.36","evidences":[{"evidenceCode":"ECO:0000250","id":"W8JWW7","source":"UniProtKB"}],"name":"(19E)-geissoschizine + NADP(+) = 4,21-dehydrogeissoschizine + NADPH","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:11376"},{"database":"ChEBI","id":"CHEBI:17037"},{"database":"ChEBI","id":"CHEBI:17294"},{"database":"ChEBI","id":"CHEBI:57783"},{"database":"ChEBI","id":"CHEBI:58349"}]}}
```

Source SHA-256: `6eda11173d33f799125da302047e13f2dbcebc81de87a50235cb3bf62d181ed5`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ1?format=txt&versions=2)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-02T04:29:32.265438+00:00.  

```text
DE   RecName: Full=Geissoschizine synthase {ECO:0000303|PubMed:38212296};
DE            Short=RsGS {ECO:0000303|PubMed:38212296};
DE            EC=1.3.1.36 {ECO:0000250|UniProtKB:W8JWW7};
```

Source SHA-256: `7ba973e38966d3d8089bcd88dfc1f173357dd4d1bed310495b9a3912403794b7`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ1?format=txt&versions=2)  
**Locator:** `lines 31-37`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-02T04:29:32.265438+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=(19E)-geissoschizine + NADP(+) = 4,21-dehydrogeissoschizine +
CC         NADPH; Xref=Rhea:RHEA:11376, ChEBI:CHEBI:17037, ChEBI:CHEBI:17294,
CC         ChEBI:CHEBI:57783, ChEBI:CHEBI:58349; EC=1.3.1.36;
CC         Evidence={ECO:0000250|UniProtKB:W8JWW7};
CC       PhysiologicalDirection=right-to-left; Xref=Rhea:RHEA:11378;
CC         Evidence={ECO:0000250|UniProtKB:W8JWW7};
```

Source SHA-256: `7ba973e38966d3d8089bcd88dfc1f173357dd4d1bed310495b9a3912403794b7`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 133. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
