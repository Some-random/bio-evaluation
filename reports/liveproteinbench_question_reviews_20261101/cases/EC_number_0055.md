# EC_number_0055

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **D** — 1.1.1.17

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSDMKAIHFGGGNIGRGFVAEFLHKSGYEVVFVDVMDAIINALQQNKSYTVTEVGTSETKSKTIDNYRAINSKTDEDKVVEEIATADIVTCAVGPNILKFIAPVIAKGIENRKKDSPIAVIACENAIGATDTLRKFIEEKLSDSTKSNIQDKARFANSAIDRIVPMQDENAGLNVKIEKFYEWCVESKPFLPSQPPKIEGVHFVEDLTPFIERKLFTVNTGHATAAYYGYNRGKECIHDVLQDKELNEIVRNTLKETAHLIVNKHEISEEDQNQYVEKIIKRISNPVLKDNVERVGRAPLRKLSRNERFIGPAAHLAEMGAKYDALLGGIEMCLRFQNVEGDDESFELAKILKENSSSDATEKITGLERNHTLFPAVEEVVKKVQA

[Multiple Choices]
A. 1.1.1.336
B. 5.6.1.1
C. 2.7.1.39
D. 1.1.1.17
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

> The supplied sequence exactly matches the UniProt entry annotated as EC 1.1.1.17, mannitol-1-phosphate 5-dehydrogenase. The annotation and catalytic reaction are supported by a transferred annotation (ECO:0000250), not shown here as a direct experimental measurement on this protein.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may support broad enzyme-family inference, but no supplied context establishes the specific substrate and reaction needed to distinguish EC 1.1.1.17 from another dehydrogenase option.


**Missing item-specific fact**

> The protein-specific functional annotation or experimental evidence identifying its catalytic reaction as mannitol-1-phosphate oxidation/reduction.


**Reason**

> The exact EC assignment relies on a protein-specific functional fact absent from the question. Identifying the sequence from memory or consulting its database record would be lookup, not reasoning from the provided input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The choices specify distinct EC activities; the evidence supports D, although the sequence and context supplied to the model do not independently establish that exact activity.


### Important caveats

- The supporting UniProt EC annotation is transferred by similarity (ECO:0000250); it does not by itself establish direct experimental verification for this exact protein.
- The sequence match and historical annotation support the expected answer, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence may support broad enzyme-family inference, but no supplied context establishes the specific substrate and reaction needed to distinguish EC 1.1.1.17 from another dehydrogenase option.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific functional annotation or experimental evidence identifying its catalytic reaction as mannitol-1-phosphate oxidation/reduction.",
    "reason": "The exact EC assignment relies on a protein-specific functional fact absent from the question. Identifying the sequence from memory or consulting its database record would be lookup, not reasoning from the provided input."
  },
  "case_id": "EC_number_0055",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry annotated as EC 1.1.1.17, mannitol-1-phosphate 5-dehydrogenase. The annotation and catalytic reaction are supported by a transferred annotation (ECO:0000250), not shown here as a direct experimental measurement on this protein."
  },
  "important_caveats": [
    "The supporting UniProt EC annotation is transferred by similarity (ECO:0000250); it does not by itself establish direct experimental verification for this exact protein.",
    "The sequence match and historical annotation support the expected answer, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices specify distinct EC activities; the evidence supports D, although the sequence and context supplied to the model do not independently establish that exact activity."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0055",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry annotated as EC 1.1.1.17, mannitol-1-phosphate 5-dehydrogenase. The annotation and catalytic reaction are supported by a transferred annotation (ECO:0000250), not shown here as a direct experimental measurement on this protein.",
    "evidence_ids": ["C1", "C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may support broad enzyme-family inference, but no supplied context establishes the specific substrate and reaction needed to distinguish EC 1.1.1.17 from another dehydrogenase option.",
    "missing_item_specific_fact": "The protein-specific functional annotation or experimental evidence identifying its catalytic reaction as mannitol-1-phosphate oxidation/reduction.",
    "reason": "The exact EC assignment relies on a protein-specific functional fact absent from the question. Identifying the sequence from memory or consulting its database record would be lookup, not reasoning from the provided input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices specify distinct EC activities; the evidence supports D, although the sequence and context supplied to the model do not independently establish that exact activity."
  },
  "important_caveats": [
    "The supporting UniProt EC annotation is transferred by similarity (ECO:0000250); it does not by itself establish direct experimental verification for this exact protein.",
    "The sequence match and historical annotation support the expected answer, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProtKB entry A0A223HDH4 (MPDH_AURME) is annotated with EC 1.1.1.17 (Mannitol-1-phosphate 5-dehydrogenase). The benchmark sequence (386 AA) matches the UniProt sequence exactly (SHA256 confirmed). The recommended name 'Mannitol-1-phosphate 5-dehydrogenase' is supported by PubMed:32003433 (ECO:0000303). The catalytic activity (D-mannitol 1-phosphate + NAD+ → beta-D-fructose 6-phosphate + NADH + H+) is recorded. However, the EC number itself carries evidence code ECO:0000250 (similarity-based transfer from Q4X1A4), meaning it is a computational inference rather than a direct experimental measurement for this specific protein. The annotation is nonetheless consistent and well-supported at the family level.

Citations as saved: [C1](#evidence-c1), [C3](#evidence-c3), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal region 'FGGGNIGRGF' contains a Rossmann-fold GxGxxG-type motif, and the 'HD' in 'GYNRGKECIHDVLQ' resembles a catalytic His-Asp dyad, both consistent with an NAD-dependent dehydrogenase. This general reasoning can plausibly eliminate EC 5.6.1.1 (isomerase/chaperone class, no Rossmann fold needed) and EC 2.7.1.39 (kinase/transferase class, different fold architecture). However, distinguishing EC 1.1.1.17 from EC 1.1.1.336—both oxidoreductases acting on CH-OH with NAD+ as acceptor—requires knowing the precise substrate specificity (mannitol-1-phosphate vs. another 2-hydroxy substrate), which depends on active-site pocket geometry not reliably readable from primary sequence alone.


**Missing item-specific fact**

> The specific substrate identity of this enzyme (mannitol-1-phosphate 5-dehydrogenase vs. another 1.1.1.x dehydrogenase such as the one assigned EC 1.1.1.336) cannot be determined from sequence by general biological reasoning. It requires either the UniProt/database annotation for this exact protein, knowledge of the mannitol-1-phosphate 5-dehydrogenase family signature, or experimental substrate-specificity data.


**Reason**

> General sequence features (Rossmann fold, catalytic dyad) support the broad oxidoreductase/dehydrogenase class, narrowing four choices to two (A vs D). But the final step—choosing EC 1.1.1.17 over EC 1.1.1.336—depends on an item-specific fact (this protein's exact substrate is mannitol-1-phosphate) that is not derivable from the sequence by general biological reasoning.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> EC 5.6.1.1 (isomerase) and EC 2.7.1.39 (kinase) are clearly incompatible with the Rossmann-fold dehydrogenase architecture evident in the sequence, so B and C are strong distractors. The real ambiguity is between A (1.1.1.336) and D (1.1.1.17), both dehydrogenases. Without the specific substrate annotation, a knowledgeable model could not definitively exclude A on general grounds, though the 'NAG' region motif weakly hints at the mannitol-dehydrogenase superfamily.


### Important caveats

- The EC 1.1.1.17 annotation in UniProtKB uses evidence code ECO:0000250 (similarity-based transfer from Q4X1A4), not direct experimental characterization of this A. melanogenum protein. The protein name is supported by PubMed:32003433, but the EC assignment itself is computational.
- The UniProt accession (A0A223HDH4) was inferred by the reviewer from dataset metadata; it was not provided to the evaluated model. The model must work from the raw sequence alone.
- EC 1.1.1.336: the reviewer could not confirm whether this is a currently valid, well-characterized EC number or a fabricated/obsolete distractor. If it is not a real EC entry, option A becomes trivially eliminable, which would slightly improve the reasoning-supported portion of the question.
- The sequence length (386 AA) and overall architecture are consistent with the mannitol-dehydrogenase superfamily, but this is a weak family-level signal, not a definitive discriminator at the 4-digit EC level.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal region 'FGGGNIGRGF' contains a Rossmann-fold GxGxxG-type motif, and the 'HD' in 'GYNRGKECIHDVLQ' resembles a catalytic His-Asp dyad, both consistent with an NAD-dependent dehydrogenase. This general reasoning can plausibly eliminate EC 5.6.1.1 (isomerase/chaperone class, no Rossmann fold needed) and EC 2.7.1.39 (kinase/transferase class, different fold architecture). However, distinguishing EC 1.1.1.17 from EC 1.1.1.336—both oxidoreductases acting on CH-OH with NAD+ as acceptor—requires knowing the precise substrate specificity (mannitol-1-phosphate vs. another 2-hydroxy substrate), which depends on active-site pocket geometry not reliably readable from primary sequence alone.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific substrate identity of this enzyme (mannitol-1-phosphate 5-dehydrogenase vs. another 1.1.1.x dehydrogenase such as the one assigned EC 1.1.1.336) cannot be determined from sequence by general biological reasoning. It requires either the UniProt/database annotation for this exact protein, knowledge of the mannitol-1-phosphate 5-dehydrogenase family signature, or experimental substrate-specificity data.",
    "reason": "General sequence features (Rossmann fold, catalytic dyad) support the broad oxidoreductase/dehydrogenase class, narrowing four choices to two (A vs D). But the final step—choosing EC 1.1.1.17 over EC 1.1.1.336—depends on an item-specific fact (this protein's exact substrate is mannitol-1-phosphate) that is not derivable from the sequence by general biological reasoning."
  },
  "case_id": "EC_number_0055",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C3",
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProtKB entry A0A223HDH4 (MPDH_AURME) is annotated with EC 1.1.1.17 (Mannitol-1-phosphate 5-dehydrogenase). The benchmark sequence (386 AA) matches the UniProt sequence exactly (SHA256 confirmed). The recommended name 'Mannitol-1-phosphate 5-dehydrogenase' is supported by PubMed:32003433 (ECO:0000303). The catalytic activity (D-mannitol 1-phosphate + NAD+ → beta-D-fructose 6-phosphate + NADH + H+) is recorded. However, the EC number itself carries evidence code ECO:0000250 (similarity-based transfer from Q4X1A4), meaning it is a computational inference rather than a direct experimental measurement for this specific protein. The annotation is nonetheless consistent and well-supported at the family level."
  },
  "important_caveats": [
    "The EC 1.1.1.17 annotation in UniProtKB uses evidence code ECO:0000250 (similarity-based transfer from Q4X1A4), not direct experimental characterization of this A. melanogenum protein. The protein name is supported by PubMed:32003433, but the EC assignment itself is computational.",
    "The UniProt accession (A0A223HDH4) was inferred by the reviewer from dataset metadata; it was not provided to the evaluated model. The model must work from the raw sequence alone.",
    "EC 1.1.1.336: the reviewer could not confirm whether this is a currently valid, well-characterized EC number or a fabricated/obsolete distractor. If it is not a real EC entry, option A becomes trivially eliminable, which would slightly improve the reasoning-supported portion of the question.",
    "The sequence length (386 AA) and overall architecture are consistent with the mannitol-dehydrogenase superfamily, but this is a weak family-level signal, not a definitive discriminator at the 4-digit EC level."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "EC 5.6.1.1 (isomerase) and EC 2.7.1.39 (kinase) are clearly incompatible with the Rossmann-fold dehydrogenase architecture evident in the sequence, so B and C are strong distractors. The real ambiguity is between A (1.1.1.336) and D (1.1.1.17), both dehydrogenases. Without the specific substrate annotation, a knowledgeable model could not definitively exclude A on general grounds, though the 'NAG' region motif weakly hints at the mannitol-dehydrogenase superfamily."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0055",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProtKB entry A0A223HDH4 (MPDH_AURME) is annotated with EC 1.1.1.17 (Mannitol-1-phosphate 5-dehydrogenase). The benchmark sequence (386 AA) matches the UniProt sequence exactly (SHA256 confirmed). The recommended name 'Mannitol-1-phosphate 5-dehydrogenase' is supported by PubMed:32003433 (ECO:0000303). The catalytic activity (D-mannitol 1-phosphate + NAD+ → beta-D-fructose 6-phosphate + NADH + H+) is recorded. However, the EC number itself carries evidence code ECO:0000250 (similarity-based transfer from Q4X1A4), meaning it is a computational inference rather than a direct experimental measurement for this specific protein. The annotation is nonetheless consistent and well-supported at the family level.",
    "evidence_ids": ["C1", "C3", "C4", "C5", "C6", "H1", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal region 'FGGGNIGRGF' contains a Rossmann-fold GxGxxG-type motif, and the 'HD' in 'GYNRGKECIHDVLQ' resembles a catalytic His-Asp dyad, both consistent with an NAD-dependent dehydrogenase. This general reasoning can plausibly eliminate EC 5.6.1.1 (isomerase/chaperone class, no Rossmann fold needed) and EC 2.7.1.39 (kinase/transferase class, different fold architecture). However, distinguishing EC 1.1.1.17 from EC 1.1.1.336—both oxidoreductases acting on CH-OH with NAD+ as acceptor—requires knowing the precise substrate specificity (mannitol-1-phosphate vs. another 2-hydroxy substrate), which depends on active-site pocket geometry not reliably readable from primary sequence alone.",
    "missing_item_specific_fact": "The specific substrate identity of this enzyme (mannitol-1-phosphate 5-dehydrogenase vs. another 1.1.1.x dehydrogenase such as the one assigned EC 1.1.1.336) cannot be determined from sequence by general biological reasoning. It requires either the UniProt/database annotation for this exact protein, knowledge of the mannitol-1-phosphate 5-dehydrogenase family signature, or experimental substrate-specificity data.",
    "reason": "General sequence features (Rossmann fold, catalytic dyad) support the broad oxidoreductase/dehydrogenase class, narrowing four choices to two (A vs D). But the final step—choosing EC 1.1.1.17 over EC 1.1.1.336—depends on an item-specific fact (this protein's exact substrate is mannitol-1-phosphate) that is not derivable from the sequence by general biological reasoning."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "EC 5.6.1.1 (isomerase) and EC 2.7.1.39 (kinase) are clearly incompatible with the Rossmann-fold dehydrogenase architecture evident in the sequence, so B and C are strong distractors. The real ambiguity is between A (1.1.1.336) and D (1.1.1.17), both dehydrogenases. Without the specific substrate annotation, a knowledgeable model could not definitively exclude A on general grounds, though the 'NAG' region motif weakly hints at the mannitol-dehydrogenase superfamily."
  },
  "important_caveats": [
    "The EC 1.1.1.17 annotation in UniProtKB uses evidence code ECO:0000250 (similarity-based transfer from Q4X1A4), not direct experimental characterization of this A. melanogenum protein. The protein name is supported by PubMed:32003433, but the EC assignment itself is computational.",
    "The UniProt accession (A0A223HDH4) was inferred by the reviewer from dataset metadata; it was not provided to the evaluated model. The model must work from the raw sequence alone.",
    "EC 1.1.1.336: the reviewer could not confirm whether this is a currently valid, well-characterized EC number or a fabricated/obsolete distractor. If it is not a real EC entry, option A becomes trivially eliminable, which would slightly improve the reasoning-supported portion of the question.",
    "The sequence length (386 AA) and overall architecture are consistent with the mannitol-dehydrogenase superfamily, but this is a weak family-level signal, not a definitive discriminator at the 4-digit EC level."
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

**Accession:** `A0A223HDH4` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 15. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223HDH4.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:43.559987+00:00.  

```json
"A0A223HDH4"
```

Source SHA-256: `7c8df05c75e909c885087b874bfd4270859d408d933f4695e68a2b558bd8ea6e`.

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223HDH4.json)  
**Locator:** `/organism`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:43.559987+00:00.  

```json
{"commonName":"Aureobasidium pullulans var. melanogenum","lineage":["Eukaryota","Fungi","Dikarya","Ascomycota","Pezizomycotina","Dothideomycetes","Dothideomycetidae","Dothideales","Saccotheciaceae","Aureobasidium"],"scientificName":"Aureobasidium melanogenum","taxonId":46634}
```

Source SHA-256: `7c8df05c75e909c885087b874bfd4270859d408d933f4695e68a2b558bd8ea6e`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223HDH4.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:43.559987+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q4X1A4","source":"UniProtKB"}],"value":"1.1.1.17"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"32003433","source":"PubMed"}],"value":"Mannitol-1-phosphate 5-dehydrogenase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"32003433","source":"PubMed"}],"value":"MPDH"}]}}
```

Source SHA-256: `7c8df05c75e909c885087b874bfd4270859d408d933f4695e68a2b558bd8ea6e`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223HDH4.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:43.559987+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"1.1.1.17","evidences":[{"evidenceCode":"ECO:0000250","id":"Q4X1A4","source":"UniProtKB"}],"name":"D-mannitol 1-phosphate + NAD(+) = beta-D-fructose 6-phosphate + NADH + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:19661"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:57540"},{"database":"ChEBI","id":"CHEBI:57634"},{"database":"ChEBI","id":"CHEBI:57945"},{"database":"ChEBI","id":"CHEBI:61381"}]}}
```

Source SHA-256: `7c8df05c75e909c885087b874bfd4270859d408d933f4695e68a2b558bd8ea6e`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223HDH4.json)  
**Locator:** `/references/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:43.559987+00:00.  

```json
{"citation":{"authors":["Xue S.J.","Liu G.L.","Chi Z.","Gao Z.C.","Hu Z.","Chi Z.M."],"citationCrossReferences":[{"database":"PubMed","id":"32003433"},{"database":"DOI","id":"10.1042/bcj20190922"}],"citationType":"journal article","firstPage":"887","id":"32003433","journal":"Biochem. J.","lastPage":"903","publicationDate":"2020","title":"Genetic evidences for the core biosynthesis pathway, regulation, transport and secretion of liamocins in yeast-like fungal cells.","volume":"477"},"referenceNumber":4,"referencePositions":["FUNCTION","DISRUPTION PHENOTYPE"]}
```

Source SHA-256: `7c8df05c75e909c885087b874bfd4270859d408d933f4695e68a2b558bd8ea6e`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A223HDH4?format=txt&versions=15)  
**Locator:** `lines 1-12`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 15 / 1.  
**Retrieved:** 2026-11-02T04:24:46.025296+00:00.  

```text
ID   MPDH_AURME              Reviewed;         386 AA.
AC   A0A223HDH4;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   25-OCT-2017, sequence version 1.
DT   28-JAN-2026, entry version 15.
DE   RecName: Full=Mannitol-1-phosphate 5-dehydrogenase {ECO:0000303|PubMed:32003433};
DE            Short=MPDH {ECO:0000303|PubMed:32003433};
DE            EC=1.1.1.17 {ECO:0000250|UniProtKB:Q4X1A4};
OS   Aureobasidium melanogenum (Aureobasidium pullulans var. melanogenum).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Dothideomycetes;
OC   Dothideomycetidae; Dothideales; Saccotheciaceae; Aureobasidium.
OX   NCBI_TaxID=46634;
```

Source SHA-256: `cdb64e60ab7ff06bc6c58dba44ce5f9a0a74986e515a667043ef14c65f549ac0`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A223HDH4?format=txt&versions=15)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 15 / 1.  
**Retrieved:** 2026-11-02T04:24:46.025296+00:00.  

```text
DE   RecName: Full=Mannitol-1-phosphate 5-dehydrogenase {ECO:0000303|PubMed:32003433};
DE            Short=MPDH {ECO:0000303|PubMed:32003433};
DE            EC=1.1.1.17 {ECO:0000250|UniProtKB:Q4X1A4};
```

Source SHA-256: `cdb64e60ab7ff06bc6c58dba44ce5f9a0a74986e515a667043ef14c65f549ac0`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A223HDH4?format=txt&versions=15)  
**Locator:** `lines 31-37`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 15 / 1.  
**Retrieved:** 2026-11-02T04:24:46.025296+00:00.  

```text
RN   [4]
RP   FUNCTION, AND DISRUPTION PHENOTYPE.
RX   PubMed=32003433; DOI=10.1042/bcj20190922;
RA   Xue S.J., Liu G.L., Chi Z., Gao Z.C., Hu Z., Chi Z.M.;
RT   "Genetic evidences for the core biosynthesis pathway, regulation, transport
RT   and secretion of liamocins in yeast-like fungal cells.";
RL   Biochem. J. 477:887-903(2020).
```

Source SHA-256: `cdb64e60ab7ff06bc6c58dba44ce5f9a0a74986e515a667043ef14c65f549ac0`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A223HDH4?format=txt&versions=15)  
**Locator:** `lines 53-58`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 15 / 1.  
**Retrieved:** 2026-11-02T04:24:46.025296+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=D-mannitol 1-phosphate + NAD(+) = beta-D-fructose 6-phosphate
CC         + NADH + H(+); Xref=Rhea:RHEA:19661, ChEBI:CHEBI:15378,
CC         ChEBI:CHEBI:57540, ChEBI:CHEBI:57634, ChEBI:CHEBI:57945,
CC         ChEBI:CHEBI:61381; EC=1.1.1.17;
CC         Evidence={ECO:0000250|UniProtKB:Q4X1A4};
```

Source SHA-256: `cdb64e60ab7ff06bc6c58dba44ce5f9a0a74986e515a667043ef14c65f549ac0`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 55. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
