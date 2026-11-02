# cofactor_0043

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `cofactor`  
**Author expected answer:** **C** — pantetheine 4&#x27;-phosphate

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MPSHTFNPQAGYDLAVDRNLGLGEIFYNRAQKSHQAIAVCDGGAVLTYGQLHAKAYRLAQELSQWLRLTEKPVGIVVQHGMADVVAQMAVIYAGGSCAPMDPTLPDNQIQGRLKRLDAVCVLTDQANRHRDLGADVLCIDDFDIADLAPEDTLYPVATNLEHCAYLIHTSGTTAEPKAVQIAARSILHVAFYAPLEPVYDTDVVAHANNSSFDVSLFDIWVPLLRGAQIAVINKAVLLDPPMMAREIDRLGITVMATTTAVLNLAAFIYPKAFAKLRLVTIGGEAANVAAIRIILKNGPPAMLFNAYGPTECCVFCLAHQITPADVEHGSIGVSIGKPVGRTITYIAGDEGGESDQGELWIGGPGVSPGYFRQPEKNLAAFSDLGEAMTSLENPVRFYRTGDIVRRRPNGALEYVGRRDHQVKVRGFRIELEAVEAGLLKTGLFSDAVAMRIEMPQNGAGSILAAYVVPTDVSKPPTMDEALESAKSILPHYMVPQLELVPRLPLNRHLKVDRKQLAELFGRRWEDVSPAQPENASQDVRSALVSLWATVLASPLSTYGDDDDFLHLGGTSLQAAMLINQIRHKFDIEVSLLTLYDNTTLGALTSIIKQRLSGQSETLHNEKDSWVADSEIADDLSCPLDRPIDWCRDTEGRVFLTGGTGFVGAFLLADLLHMPQTSQVRCLVRATDAAVGQERLRAALDKYGLWEDGFADKLVAIAGLLEDDYLGMGREQFEEAASWASVVFHLGARVNYAQPYSLHRASNTLGTRNMVRFACAGRTKAIHYVSSIGCFGPTGSILGTTSVREDEPLLPHITALPYDHGYAQSQWVADALLRRLMDRGFPIAIYRPGFIVGHSQTGACNPDDFLSRLIDACREIGCYPQLPNQRKEFVPVDYVNAAILHIAASPASLGHAYHIVPPTRAVSIDMDNSMALVDRAGNSPMRPVSYKEWVERLAATSPKRLLPLQPMLAERVKDGLTRWELYENMPVYETTNTARALQNYPGGLQFPVLDTSLMKRYLDFLEAKG

[Multiple Choices]
A. Mg(2+)
B. NAD(+)
C. pantetheine 4'-phosphate
D. Fe(2+)
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

> The exact sequence matches a UniProt entry annotated with pantetheine 4'-phosphate as a cofactor. The annotation is computational, based on a PROSITE-ProRule, rather than direct experimental evidence in the supplied excerpts.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence alone does not provide clear, readily interpretable evidence that distinguishes pantetheine 4'-phosphate from the other listed cofactors; doing so requires identifying its specific protein function or domain features.


**Missing item-specific fact**

> The sequence's association with FrzA and the annotation of a phosphopantetheine-bearing carrier-protein feature are not stated in the question.


**Reason**

> The correct choice is supported by a sequence-matched protein annotation, but the input supplies no functional or domain context that makes this specific cofactor inferable by general biological reasoning.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The available evidence specifically supports choice C; it does not establish another listed option as an alternative answer.


### Important caveats

- The cofactor annotation is computational (PROSITE-ProRule), not direct experimental confirmation in the supplied evidence.
- The sequence match is exact in both the current and archived UniProt records; the record's cofactor annotation should not be mistaken for information supplied to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence alone does not provide clear, readily interpretable evidence that distinguishes pantetheine 4'-phosphate from the other listed cofactors; doing so requires identifying its specific protein function or domain features.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The sequence's association with FrzA and the annotation of a phosphopantetheine-bearing carrier-protein feature are not stated in the question.",
    "reason": "The correct choice is supported by a sequence-matched protein annotation, but the input supplies no functional or domain context that makes this specific cofactor inferable by general biological reasoning."
  },
  "case_id": "cofactor_0043",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated with pantetheine 4'-phosphate as a cofactor. The annotation is computational, based on a PROSITE-ProRule, rather than direct experimental evidence in the supplied excerpts."
  },
  "important_caveats": [
    "The cofactor annotation is computational (PROSITE-ProRule), not direct experimental confirmation in the supplied evidence.",
    "The sequence match is exact in both the current and archived UniProt records; the record's cofactor annotation should not be mistaken for information supplied to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The available evidence specifically supports choice C; it does not establish another listed option as an alternative answer."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0043",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated with pantetheine 4'-phosphate as a cofactor. The annotation is computational, based on a PROSITE-ProRule, rather than direct experimental evidence in the supplied excerpts.",
    "evidence_ids": ["C1", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence alone does not provide clear, readily interpretable evidence that distinguishes pantetheine 4'-phosphate from the other listed cofactors; doing so requires identifying its specific protein function or domain features.",
    "missing_item_specific_fact": "The sequence's association with FrzA and the annotation of a phosphopantetheine-bearing carrier-protein feature are not stated in the question.",
    "reason": "The correct choice is supported by a sequence-matched protein annotation, but the input supplies no functional or domain context that makes this specific cofactor inferable by general biological reasoning."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The available evidence specifically supports choice C; it does not establish another listed option as an alternative answer."
  },
  "important_caveats": [
    "The cofactor annotation is computational (PROSITE-ProRule), not direct experimental confirmation in the supplied evidence.",
    "The sequence match is exact in both the current and archived UniProt records; the record's cofactor annotation should not be mistaken for information supplied to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A7T8F1L4 (sequence matched, 1024 aa) annotates the cofactor as pantetheine 4'-phosphate (ChEBI:CHEBI:47942) with evidence code ECO:0000255|PROSITE-ProRule:PRU00258. The protein is a non-canonical nonribosomal peptide synthetase (FrzA, EC 1.2.1.101) from Cladobotryum sp. NRPS enzymes universally require pantetheine 4'-phosphate as the phosphopantetheinyl prosthetic group on the peptidyl carrier protein (PCP/T) domain. While the annotation evidence is computational (PROSITE pattern matching), the biological rationale is well-established general biochemistry for NRPS enzymes.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains recognizable NRPS multi-domain architecture signatures: (1) an adenylation (A) domain motif region including 'GDEGGESDQGELWIGGPGVSPGYFRQ' with the characteristic GGPG/A7 motif; (2) a condensation (C) domain motif 'GGTGFVGAFLL' with the classic C-domain glycine-rich flanking; (3) a PCP/thiolation (T) domain motif 'GGSCAPMDPT' containing the conserved serine in a GxxS context that serves as the phosphopantetheinylation site. NRPS enzymes universally require pantetheine 4'-phosphate covalently attached to the T-domain serine to carry activated amino acid intermediates. The distractors (Mg2+, NAD+, Fe2+) are common cofactors for other enzyme classes (kinases, dehydrogenases, oxygenases respectively) and are not associated with NRPS catalytic mechanisms.


**Missing item-specific fact**

> None critical. Recognition of the NRPS domain architecture from sequence motifs and the general biochemical fact that NRPS enzymes require pantetheine 4'-phosphate are both within the scope of general enzymology knowledge.


**Reason**

> A model with knowledge of NRPS domain architecture can identify the A, C, and T domain motifs in the sequence, conclude the protein is a nonribosomal peptide synthetase, and apply the well-known general fact that NRPS enzymes require pantetheine 4'-phosphate as their defining prosthetic group. This does not require recalling a specific database entry for FrzA.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The distractors Mg2+, NAD+, and Fe2+ are not cofactors of NRPS enzymes. Pantetheine 4'-phosphate is the unique and defining cofactor/prosthetic group of the thiolation domain in NRPS systems. No other listed option is defensible for an NRPS.


### Important caveats

- The UniProt cofactor annotation uses ECO:0000255 (PROSITE-ProRule computational inference), not direct experimental measurement of phosphopantetheinylation on this specific protein. However, the NRPS-cofactor relationship is textbook biochemistry.
- The protein is described as 'non-canonical' NRPS (EC 1.2.1.101, an aldehyde reductase-like function), but the presence of T-domain motifs and the PROSITE annotation still support pantetheine 4'-phosphate as the cofactor.
- Identification of NRPS domain motifs from raw sequence requires specialized domain-architecture knowledge; a model without this training would likely default to a generic cofactor guess.
- The sequence is from Cladobotryum sp. (a mycoparasitic fungus), and the protein participates in FR901483 immunosuppressant biosynthesis per the cited 2021 JACS paper.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains recognizable NRPS multi-domain architecture signatures: (1) an adenylation (A) domain motif region including 'GDEGGESDQGELWIGGPGVSPGYFRQ' with the characteristic GGPG/A7 motif; (2) a condensation (C) domain motif 'GGTGFVGAFLL' with the classic C-domain glycine-rich flanking; (3) a PCP/thiolation (T) domain motif 'GGSCAPMDPT' containing the conserved serine in a GxxS context that serves as the phosphopantetheinylation site. NRPS enzymes universally require pantetheine 4'-phosphate covalently attached to the T-domain serine to carry activated amino acid intermediates. The distractors (Mg2+, NAD+, Fe2+) are common cofactors for other enzyme classes (kinases, dehydrogenases, oxygenases respectively) and are not associated with NRPS catalytic mechanisms.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. Recognition of the NRPS domain architecture from sequence motifs and the general biochemical fact that NRPS enzymes require pantetheine 4'-phosphate are both within the scope of general enzymology knowledge.",
    "reason": "A model with knowledge of NRPS domain architecture can identify the A, C, and T domain motifs in the sequence, conclude the protein is a nonribosomal peptide synthetase, and apply the well-known general fact that NRPS enzymes require pantetheine 4'-phosphate as their defining prosthetic group. This does not require recalling a specific database entry for FrzA."
  },
  "case_id": "cofactor_0043",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A7T8F1L4 (sequence matched, 1024 aa) annotates the cofactor as pantetheine 4'-phosphate (ChEBI:CHEBI:47942) with evidence code ECO:0000255|PROSITE-ProRule:PRU00258. The protein is a non-canonical nonribosomal peptide synthetase (FrzA, EC 1.2.1.101) from Cladobotryum sp. NRPS enzymes universally require pantetheine 4'-phosphate as the phosphopantetheinyl prosthetic group on the peptidyl carrier protein (PCP/T) domain. While the annotation evidence is computational (PROSITE pattern matching), the biological rationale is well-established general biochemistry for NRPS enzymes."
  },
  "important_caveats": [
    "The UniProt cofactor annotation uses ECO:0000255 (PROSITE-ProRule computational inference), not direct experimental measurement of phosphopantetheinylation on this specific protein. However, the NRPS-cofactor relationship is textbook biochemistry.",
    "The protein is described as 'non-canonical' NRPS (EC 1.2.1.101, an aldehyde reductase-like function), but the presence of T-domain motifs and the PROSITE annotation still support pantetheine 4'-phosphate as the cofactor.",
    "Identification of NRPS domain motifs from raw sequence requires specialized domain-architecture knowledge; a model without this training would likely default to a generic cofactor guess.",
    "The sequence is from Cladobotryum sp. (a mycoparasitic fungus), and the protein participates in FR901483 immunosuppressant biosynthesis per the cited 2021 JACS paper."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The distractors Mg2+, NAD+, and Fe2+ are not cofactors of NRPS enzymes. Pantetheine 4'-phosphate is the unique and defining cofactor/prosthetic group of the thiolation domain in NRPS systems. No other listed option is defensible for an NRPS."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0043",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A7T8F1L4 (sequence matched, 1024 aa) annotates the cofactor as pantetheine 4'-phosphate (ChEBI:CHEBI:47942) with evidence code ECO:0000255|PROSITE-ProRule:PRU00258. The protein is a non-canonical nonribosomal peptide synthetase (FrzA, EC 1.2.1.101) from Cladobotryum sp. NRPS enzymes universally require pantetheine 4'-phosphate as the phosphopantetheinyl prosthetic group on the peptidyl carrier protein (PCP/T) domain. While the annotation evidence is computational (PROSITE pattern matching), the biological rationale is well-established general biochemistry for NRPS enzymes.",
    "evidence_ids": ["C1", "C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains recognizable NRPS multi-domain architecture signatures: (1) an adenylation (A) domain motif region including 'GDEGGESDQGELWIGGPGVSPGYFRQ' with the characteristic GGPG/A7 motif; (2) a condensation (C) domain motif 'GGTGFVGAFLL' with the classic C-domain glycine-rich flanking; (3) a PCP/thiolation (T) domain motif 'GGSCAPMDPT' containing the conserved serine in a GxxS context that serves as the phosphopantetheinylation site. NRPS enzymes universally require pantetheine 4'-phosphate covalently attached to the T-domain serine to carry activated amino acid intermediates. The distractors (Mg2+, NAD+, Fe2+) are common cofactors for other enzyme classes (kinases, dehydrogenases, oxygenases respectively) and are not associated with NRPS catalytic mechanisms.",
    "missing_item_specific_fact": "None critical. Recognition of the NRPS domain architecture from sequence motifs and the general biochemical fact that NRPS enzymes require pantetheine 4'-phosphate are both within the scope of general enzymology knowledge.",
    "reason": "A model with knowledge of NRPS domain architecture can identify the A, C, and T domain motifs in the sequence, conclude the protein is a nonribosomal peptide synthetase, and apply the well-known general fact that NRPS enzymes require pantetheine 4'-phosphate as their defining prosthetic group. This does not require recalling a specific database entry for FrzA."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The distractors Mg2+, NAD+, and Fe2+ are not cofactors of NRPS enzymes. Pantetheine 4'-phosphate is the unique and defining cofactor/prosthetic group of the thiolation domain in NRPS systems. No other listed option is defensible for an NRPS."
  },
  "important_caveats": [
    "The UniProt cofactor annotation uses ECO:0000255 (PROSITE-ProRule computational inference), not direct experimental measurement of phosphopantetheinylation on this specific protein. However, the NRPS-cofactor relationship is textbook biochemistry.",
    "The protein is described as 'non-canonical' NRPS (EC 1.2.1.101, an aldehyde reductase-like function), but the presence of T-domain motifs and the PROSITE annotation still support pantetheine 4'-phosphate as the cofactor.",
    "Identification of NRPS domain motifs from raw sequence requires specialized domain-architecture knowledge; a model without this training would likely default to a generic cofactor guess.",
    "The sequence is from Cladobotryum sp. (a mycoparasitic fungus), and the protein participates in FR901483 immunosuppressant biosynthesis per the cited 2021 JACS paper."
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

**Accession:** `A0A7T8F1L4` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 18. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1L4.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:48.509506+00:00.  

```json
"A0A7T8F1L4"
```

Source SHA-256: `4cf4e4af61e7d91300bdd1c46dcd31d2e7126d4631315e40df3061127135d0fb`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1L4.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:48.509506+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33372776","source":"PubMed"}],"value":"FR901483 biosynthesis cluster protein A"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"33372776","source":"PubMed"}],"value":"1.2.1.101"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33372776","source":"PubMed"}],"value":"Non-canonical nonribosomal peptide synthetase FrzA"}}}
```

Source SHA-256: `4cf4e4af61e7d91300bdd1c46dcd31d2e7126d4631315e40df3061127135d0fb`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1L4.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:48.509506+00:00.  

```json
{"cofactors":[{"cofactorCrossReference":{"database":"ChEBI","id":"CHEBI:47942"},"evidences":[{"evidenceCode":"ECO:0000255","id":"PRU00258","source":"PROSITE-ProRule"}],"name":"pantetheine 4'-phosphate"}],"commentType":"COFACTOR"}
```

Source SHA-256: `4cf4e4af61e7d91300bdd1c46dcd31d2e7126d4631315e40df3061127135d0fb`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8F1L4?format=txt&versions=18)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 18 / 1.  
**Retrieved:** 2026-11-02T04:25:50.375049+00:00.  

```text
DE   RecName: Full=Non-canonical nonribosomal peptide synthetase FrzA {ECO:0000303|PubMed:33372776};
DE            EC=1.2.1.101 {ECO:0000269|PubMed:33372776};
DE   AltName: Full=FR901483 biosynthesis cluster protein A {ECO:0000303|PubMed:33372776};
```

Source SHA-256: `dc244e3d4206d7a97707ec88200b44521e519f3504ebcf6f0cd7d074b3fd2c4b`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8F1L4?format=txt&versions=18)  
**Locator:** `lines 62-64`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 18 / 1.  
**Retrieved:** 2026-11-02T04:25:50.375049+00:00.  

```text
CC   -!- COFACTOR:
CC       Name=pantetheine 4'-phosphate; Xref=ChEBI:CHEBI:47942;
CC         Evidence={ECO:0000255|PROSITE-ProRule:PRU00258};
```

Source SHA-256: `dc244e3d4206d7a97707ec88200b44521e519f3504ebcf6f0cd7d074b3fd2c4b`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 43. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
