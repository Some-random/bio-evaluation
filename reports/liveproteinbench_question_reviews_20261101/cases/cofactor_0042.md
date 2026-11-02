# cofactor_0042

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `cofactor`  
**Author expected answer:** **A** — heme

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MYYRETMLAFVPYLAVFVACYGLVYYRRKRQRLPLPPGPPQLPLVGNLYQIPEMNPWRTYREWHQKYGPIITVKSGLTNTIILGSHKAARDLLDKRNRNYGSRPHFILIGDFIYGGNQTSLLPTGQRWRIHRRILSAFGNVRTSQRYRILYDAESKRLLREILHGGDFFEPFHHYFVRILFALTYGKRVTGSHDPEARDVIEIVDVVLKEASRSSVPEAFPILNSLPGALAPWKRRAQLLFEQHSRLFDNHMNAALANKPWNFCKQALRLKASSEVDRVELNFILGSITEATHSGSMVLGVFIMANILHPDAVRWVQEEIDRVIGPDRLPSFDDMAKLPYLNAYLLEVMRWRPITPGGMPHASFQDDEYMGYHIPKGTTVVANHWSMDFDESVFTDPYEFRPQRWIEDPNLPSIAFGFGTRICPGRHIAESSIFIVAARLLWSFNFDYAYEDGKRQEIDSWNMTQGLDSGPMPFKASFKIRSPKHQEVMDRECGVSDLDIDAILDKIGADFL

[Multiple Choices]
A. heme
B. [2Fe-2S] cluster
C. Fe cation
D. heme b
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

> The exact sequence matches a UniProt entry annotated as a cytochrome P450 monooxygenase with heme as cofactor. The annotation cites evidence transferred from another UniProt entry, so this supports the key as an annotation but is not direct experimental confirmation for this sequence.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is consistent with a cytochrome P450, whose catalytic cofactor is heme; this argues against an iron-sulfur cluster or a free iron cation.


**Missing item-specific fact**

> The input does not provide the protein-specific cofactor annotation or experimental characterization needed to choose the database's generic label “heme” over the overlapping option “heme b.”


**Reason**

> Biological knowledge can narrow the choices to heme, but it does not meaningfully distinguish A from D: heme b is a form of heme. Selecting the keyed label therefore depends on item-specific annotation, while the wording leaves the two choices overlapping.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "D"
]
```

> Heme b is a type of heme, and the supplied evidence annotates the cofactor only as “heme”; it does not rule out describing that cofactor more specifically as heme b.


### Important caveats

- The annotation's cofactor evidence is transferred by similarity from UniProtKB:P04798, rather than shown here as a direct measurement for this protein.
- Both the historical and current records match the supplied sequence, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a cytochrome P450, whose catalytic cofactor is heme; this argues against an iron-sulfur cluster or a free iron cation.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The input does not provide the protein-specific cofactor annotation or experimental characterization needed to choose the database's generic label “heme” over the overlapping option “heme b.”",
    "reason": "Biological knowledge can narrow the choices to heme, but it does not meaningfully distinguish A from D: heme b is a form of heme. Selecting the keyed label therefore depends on item-specific annotation, while the wording leaves the two choices overlapping."
  },
  "case_id": "cofactor_0042",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as a cytochrome P450 monooxygenase with heme as cofactor. The annotation cites evidence transferred from another UniProt entry, so this supports the key as an annotation but is not direct experimental confirmation for this sequence."
  },
  "important_caveats": [
    "The annotation's cofactor evidence is transferred by similarity from UniProtKB:P04798, rather than shown here as a direct measurement for this protein.",
    "Both the historical and current records match the supplied sequence, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "D"
    ],
    "reason": "Heme b is a type of heme, and the supplied evidence annotates the cofactor only as “heme”; it does not rule out describing that cofactor more specifically as heme b."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0042",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as a cytochrome P450 monooxygenase with heme as cofactor. The annotation cites evidence transferred from another UniProt entry, so this supports the key as an annotation but is not direct experimental confirmation for this sequence.",
    "evidence_ids": ["C1", "C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is consistent with a cytochrome P450, whose catalytic cofactor is heme; this argues against an iron-sulfur cluster or a free iron cation.",
    "missing_item_specific_fact": "The input does not provide the protein-specific cofactor annotation or experimental characterization needed to choose the database's generic label “heme” over the overlapping option “heme b.”",
    "reason": "Biological knowledge can narrow the choices to heme, but it does not meaningfully distinguish A from D: heme b is a form of heme. Selecting the keyed label therefore depends on item-specific annotation, while the wording leaves the two choices overlapping."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "D"],
    "reason": "Heme b is a type of heme, and the supplied evidence annotates the cofactor only as “heme”; it does not rule out describing that cofactor more specifically as heme b."
  },
  "important_caveats": [
    "The annotation's cofactor evidence is transferred by similarity from UniProtKB:P04798, rather than shown here as a direct measurement for this protein.",
    "Both the historical and current records match the supplied sequence, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation (C5, H4) explicitly lists the cofactor as 'heme' (ChEBI:CHEBI:30413) with evidence code ECO:0000250 (inferred from similarity to P04798, a characterized cytochrome P450). The protein is annotated as 'Cytochrome P450 monooxygenase FrzL' (C4, H2), and the P450 superfamily's dependence on a heme prosthetic group is one of the most well-established facts in enzymology. Although the evidence is transferred (not directly experimental for this specific protein), the P450–heme association is universally accepted. The sequence contains the canonical P450 heme-binding motif 'FGFG' and the conserved heme-ligating cysteine in 'ICPGRH', consistent with a heme-containing P450.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains hallmark cytochrome P450 motifs: the conserved 'FxxGxxxCxG' heme-binding region (visible as 'AFGFGTRICPGRH' with the critical heme-ligating cysteine in 'CPG'), a ~512-aa length typical of fungal P450s, and a membrane-targeting N-terminal region. Recognizing these features identifies the protein as a cytochrome P450, whose catalytic mechanism obligately requires a heme prosthetic group (iron coordinated by the cysteine thiolate). This reasoning eliminates &#91;2Fe-2S&#93; cluster (B, found in ferredoxins/radical SAM enzymes) and free Fe cation (C, a cofactor for non-heme iron enzymes like dioxygenases without a porphyrin).


**Missing item-specific fact**

> Distinguishing between 'heme' (A) and 'heme b' (D) purely from sequence is not feasible; both are chemically correct for P450s (all P450s use protoporphyrin IX, i.e., heme b). The choice between A and D depends on the annotation naming convention (UniProt uses 'heme' as the display name while cross-referencing ChEBI:30413, which is specifically 'heme b'). No sequence feature distinguishes these two labels.


**Reason**

> A model with knowledge of P450 signature motifs can reason its way to 'heme' and eliminate B and C. However, the A-vs-D distinction (heme vs heme b) is a nomenclature-granularity issue with no sequence-based discriminator; both are scientifically valid for P450s. The broad reasoning chain (P450 motifs → heme cofactor) is intact, but the precise A/D selection relies on matching the UniProt annotation convention rather than on a biological argument derivable from the sequence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "D"
]
```

> All cytochrome P450s use heme b (iron(II) protoporphyrin IX with cysteine thiolate ligation). 'Heme' (A) is the general class term used in the UniProt annotation name field; 'heme b' (D) is the specific chemical species (ChEBI:30413, which is what the annotation actually cross-references). Both are scientifically correct descriptions of the P450 cofactor. A model that correctly identifies the protein as a P450 and knows P450s use protoporphyrin IX could defensibly select either A or D. The author's key follows the UniProt display name 'heme' rather than the ChEBI-specific term 'heme b'.


### Important caveats

- The cofactor annotation evidence code is ECO:0000250 (inferred from similarity to P04798), not direct experimental measurement on FrzL. However, the P450–heme association is universally established across the superfamily.
- The A (heme) vs D (heme b) distinction is a naming-granularity issue inherent to the question design; both refer to the same prosthetic group in the P450 context. The UniProt annotation uses 'heme' as the display name but cross-references ChEBI:30413, which is specifically 'heme b.'
- The reviewer-only evidence was absent from the evaluated model input; the model must rely on sequence motifs and general P450 biology.
- The historical entry (version 17, released 2026-01-28) and current entry (version 19) both carry the same cofactor annotation with identical evidence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains hallmark cytochrome P450 motifs: the conserved 'FxxGxxxCxG' heme-binding region (visible as 'AFGFGTRICPGRH' with the critical heme-ligating cysteine in 'CPG'), a ~512-aa length typical of fungal P450s, and a membrane-targeting N-terminal region. Recognizing these features identifies the protein as a cytochrome P450, whose catalytic mechanism obligately requires a heme prosthetic group (iron coordinated by the cysteine thiolate). This reasoning eliminates [2Fe-2S] cluster (B, found in ferredoxins/radical SAM enzymes) and free Fe cation (C, a cofactor for non-heme iron enzymes like dioxygenases without a porphyrin).",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Distinguishing between 'heme' (A) and 'heme b' (D) purely from sequence is not feasible; both are chemically correct for P450s (all P450s use protoporphyrin IX, i.e., heme b). The choice between A and D depends on the annotation naming convention (UniProt uses 'heme' as the display name while cross-referencing ChEBI:30413, which is specifically 'heme b'). No sequence feature distinguishes these two labels.",
    "reason": "A model with knowledge of P450 signature motifs can reason its way to 'heme' and eliminate B and C. However, the A-vs-D distinction (heme vs heme b) is a nomenclature-granularity issue with no sequence-based discriminator; both are scientifically valid for P450s. The broad reasoning chain (P450 motifs → heme cofactor) is intact, but the precise A/D selection relies on matching the UniProt annotation convention rather than on a biological argument derivable from the sequence."
  },
  "case_id": "cofactor_0042",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation (C5, H4) explicitly lists the cofactor as 'heme' (ChEBI:CHEBI:30413) with evidence code ECO:0000250 (inferred from similarity to P04798, a characterized cytochrome P450). The protein is annotated as 'Cytochrome P450 monooxygenase FrzL' (C4, H2), and the P450 superfamily's dependence on a heme prosthetic group is one of the most well-established facts in enzymology. Although the evidence is transferred (not directly experimental for this specific protein), the P450–heme association is universally accepted. The sequence contains the canonical P450 heme-binding motif 'FGFG' and the conserved heme-ligating cysteine in 'ICPGRH', consistent with a heme-containing P450."
  },
  "important_caveats": [
    "The cofactor annotation evidence code is ECO:0000250 (inferred from similarity to P04798), not direct experimental measurement on FrzL. However, the P450–heme association is universally established across the superfamily.",
    "The A (heme) vs D (heme b) distinction is a naming-granularity issue inherent to the question design; both refer to the same prosthetic group in the P450 context. The UniProt annotation uses 'heme' as the display name but cross-references ChEBI:30413, which is specifically 'heme b.'",
    "The reviewer-only evidence was absent from the evaluated model input; the model must rely on sequence motifs and general P450 biology.",
    "The historical entry (version 17, released 2026-01-28) and current entry (version 19) both carry the same cofactor annotation with identical evidence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "D"
    ],
    "reason": "All cytochrome P450s use heme b (iron(II) protoporphyrin IX with cysteine thiolate ligation). 'Heme' (A) is the general class term used in the UniProt annotation name field; 'heme b' (D) is the specific chemical species (ChEBI:30413, which is what the annotation actually cross-references). Both are scientifically correct descriptions of the P450 cofactor. A model that correctly identifies the protein as a P450 and knows P450s use protoporphyrin IX could defensibly select either A or D. The author's key follows the UniProt display name 'heme' rather than the ChEBI-specific term 'heme b'."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0042",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation (C5, H4) explicitly lists the cofactor as 'heme' (ChEBI:CHEBI:30413) with evidence code ECO:0000250 (inferred from similarity to P04798, a characterized cytochrome P450). The protein is annotated as 'Cytochrome P450 monooxygenase FrzL' (C4, H2), and the P450 superfamily's dependence on a heme prosthetic group is one of the most well-established facts in enzymology. Although the evidence is transferred (not directly experimental for this specific protein), the P450–heme association is universally accepted. The sequence contains the canonical P450 heme-binding motif 'FGFG' and the conserved heme-ligating cysteine in 'ICPGRH', consistent with a heme-containing P450.",
    "evidence_ids": ["C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains hallmark cytochrome P450 motifs: the conserved 'FxxGxxxCxG' heme-binding region (visible as 'AFGFGTRICPGRH' with the critical heme-ligating cysteine in 'CPG'), a ~512-aa length typical of fungal P450s, and a membrane-targeting N-terminal region. Recognizing these features identifies the protein as a cytochrome P450, whose catalytic mechanism obligately requires a heme prosthetic group (iron coordinated by the cysteine thiolate). This reasoning eliminates [2Fe-2S] cluster (B, found in ferredoxins/radical SAM enzymes) and free Fe cation (C, a cofactor for non-heme iron enzymes like dioxygenases without a porphyrin).",
    "missing_item_specific_fact": "Distinguishing between 'heme' (A) and 'heme b' (D) purely from sequence is not feasible; both are chemically correct for P450s (all P450s use protoporphyrin IX, i.e., heme b). The choice between A and D depends on the annotation naming convention (UniProt uses 'heme' as the display name while cross-referencing ChEBI:30413, which is specifically 'heme b'). No sequence feature distinguishes these two labels.",
    "reason": "A model with knowledge of P450 signature motifs can reason its way to 'heme' and eliminate B and C. However, the A-vs-D distinction (heme vs heme b) is a nomenclature-granularity issue with no sequence-based discriminator; both are scientifically valid for P450s. The broad reasoning chain (P450 motifs → heme cofactor) is intact, but the precise A/D selection relies on matching the UniProt annotation convention rather than on a biological argument derivable from the sequence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "D"],
    "reason": "All cytochrome P450s use heme b (iron(II) protoporphyrin IX with cysteine thiolate ligation). 'Heme' (A) is the general class term used in the UniProt annotation name field; 'heme b' (D) is the specific chemical species (ChEBI:30413, which is what the annotation actually cross-references). Both are scientifically correct descriptions of the P450 cofactor. A model that correctly identifies the protein as a P450 and knows P450s use protoporphyrin IX could defensibly select either A or D. The author's key follows the UniProt display name 'heme' rather than the ChEBI-specific term 'heme b'."
  },
  "important_caveats": [
    "The cofactor annotation evidence code is ECO:0000250 (inferred from similarity to P04798), not direct experimental measurement on FrzL. However, the P450–heme association is universally established across the superfamily.",
    "The A (heme) vs D (heme b) distinction is a naming-granularity issue inherent to the question design; both refer to the same prosthetic group in the P450 context. The UniProt annotation uses 'heme' as the display name but cross-references ChEBI:30413, which is specifically 'heme b.'",
    "The reviewer-only evidence was absent from the evaluated model input; the model must rely on sequence motifs and general P450 biology.",
    "The historical entry (version 17, released 2026-01-28) and current entry (version 19) both carry the same cofactor annotation with identical evidence."
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

**Accession:** `A0A7T8F1L2` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 17. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1L2.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:50.474399+00:00.  

```json
"A0A7T8F1L2"
```

Source SHA-256: `f00aff6a17b374aa36f10df5183bfa2190858ab4d3bbd58363dfccc724cff906`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1L2.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:50.474399+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33372776","source":"PubMed"}],"value":"FR901483 biosynthesis cluster protein L"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"33372776","source":"PubMed"}],"value":"1.-.-.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33372776","source":"PubMed"}],"value":"Cytochrome P450 monooxygenase FrzL"}}}
```

Source SHA-256: `f00aff6a17b374aa36f10df5183bfa2190858ab4d3bbd58363dfccc724cff906`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1L2.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:50.474399+00:00.  

```json
{"cofactors":[{"cofactorCrossReference":{"database":"ChEBI","id":"CHEBI:30413"},"evidences":[{"evidenceCode":"ECO:0000250","id":"P04798","source":"UniProtKB"}],"name":"heme"}],"commentType":"COFACTOR"}
```

Source SHA-256: `f00aff6a17b374aa36f10df5183bfa2190858ab4d3bbd58363dfccc724cff906`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8F1L2?format=txt&versions=17)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 17 / 1.  
**Retrieved:** 2026-11-01T06:27:34.520828+00:00.  

```text
DE   RecName: Full=Cytochrome P450 monooxygenase FrzL {ECO:0000303|PubMed:33372776};
DE            EC=1.-.-.- {ECO:0000269|PubMed:33372776};
DE   AltName: Full=FR901483 biosynthesis cluster protein L {ECO:0000303|PubMed:33372776};
```

Source SHA-256: `f0424c9067ab83539c73301f9b9c22ba80b885df6566cdc9a868e3422019628c`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8F1L2?format=txt&versions=17)  
**Locator:** `lines 51-53`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 17 / 1.  
**Retrieved:** 2026-11-01T06:27:34.520828+00:00.  

```text
CC   -!- COFACTOR:
CC       Name=heme; Xref=ChEBI:CHEBI:30413;
CC         Evidence={ECO:0000250|UniProtKB:P04798};
```

Source SHA-256: `f0424c9067ab83539c73301f9b9c22ba80b885df6566cdc9a868e3422019628c`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 42. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
