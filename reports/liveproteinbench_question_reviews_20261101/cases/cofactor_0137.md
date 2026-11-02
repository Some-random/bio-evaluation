# cofactor_0137

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `cofactor`  
**Author expected answer:** **D** — Mg(2+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MAGVEEADKLKQLGNAAFSERKWHLAIDMYTKAIELTKTPTLFCNRALAELRAELPGAALADADAALGIEPTFAKAYYHKASAYLSLGKHKQALTNYKKVVDLAPQNSDAQAKVEFCKKEIRRINFENAIMTPDEAPLSQTIKLGSVRADYDGPRIENETVTVEFVEAMKEHFRLEKLIDRHDVIFILLEVQKILKKCPNFVSINVPVGEEITVCGDTHGQYYDLLNIFKLNGNPLETNRYLFNGDFVDRGSYSFENIMTLFAYKVLYPDHFFLSRGNHEGVSMNRMYGFEGEVTQKYNSEMFRLFTEVFNSLPIGHIINNEVFVVHGGLYSSDKVTLDDLQHPNRFRDIPESGLICESLWSDPQPMPGRAPSKRGVSCLSFGPDVTETFLNNNNLKLLVRSHEVKDEGYEIEHGGKCITVFSAPNYCDQMGNKGAFIRFTGGDMKPRFTTFTHVPHPGKRPMHYATGFGLF

[Multiple Choices]
A. Co(2+)
B. [2Fe-2S] cluster
C. Cu(2+)
D. Mg(2+)
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

> The exact-match UniProt annotation lists Mg(2+) and Mn(2+) and says the protein binds two Mg(2+) or Mn(2+) ions per subunit, so Mg(2+) is supported among the listed choices. This is a transferred annotation, not direct experimental evidence in the supplied excerpts.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a serine/threonine protein phosphatase catalytic region, including conserved metal-dependent phosphatase motifs. Such phosphatases use divalent metal ions, commonly Mg(2+) or Mn(2+); that is a better fit than Co(2+), Cu(2+), or a &#91;2Fe-2S&#93; cluster among the given choices.


**Missing item-specific fact**

> The exact protein-specific metal-binding annotation and direct experimental metal occupancy are not supplied; the sequence-based family inference does not establish whether Mg(2+) or Mn(2+) is preferred.


**Reason**

> The catalytic-family motifs and the answer choices provide a meaningful biological basis for selecting Mg(2+) over the listed alternatives, without requiring recognition of the exact sequence or its database entry. The supplied evidence supports Mg(2+) but also notes Mn(2+), which is not an option.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The annotation also names Mn(2+), but it is not among the choices. Of the listed options, Mg(2+) is the one supported by the protein-family inference and annotation.


### Important caveats

- The cofactor annotation is transferred by similarity (ECO:0000250), not shown here as a direct measurement for this exact protein.
- The evidence identifies the protein as a Trypanosoma brucei serine/threonine protein phosphatase and matches the supplied sequence, but does not independently validate the underlying primary-paper metal measurements.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a serine/threonine protein phosphatase catalytic region, including conserved metal-dependent phosphatase motifs. Such phosphatases use divalent metal ions, commonly Mg(2+) or Mn(2+); that is a better fit than Co(2+), Cu(2+), or a [2Fe-2S] cluster among the given choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The exact protein-specific metal-binding annotation and direct experimental metal occupancy are not supplied; the sequence-based family inference does not establish whether Mg(2+) or Mn(2+) is preferred.",
    "reason": "The catalytic-family motifs and the answer choices provide a meaningful biological basis for selecting Mg(2+) over the listed alternatives, without requiring recognition of the exact sequence or its database entry. The supplied evidence supports Mg(2+) but also notes Mn(2+), which is not an option."
  },
  "case_id": "cofactor_0137",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact-match UniProt annotation lists Mg(2+) and Mn(2+) and says the protein binds two Mg(2+) or Mn(2+) ions per subunit, so Mg(2+) is supported among the listed choices. This is a transferred annotation, not direct experimental evidence in the supplied excerpts."
  },
  "important_caveats": [
    "The cofactor annotation is transferred by similarity (ECO:0000250), not shown here as a direct measurement for this exact protein.",
    "The evidence identifies the protein as a Trypanosoma brucei serine/threonine protein phosphatase and matches the supplied sequence, but does not independently validate the underlying primary-paper metal measurements."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The annotation also names Mn(2+), but it is not among the choices. Of the listed options, Mg(2+) is the one supported by the protein-family inference and annotation."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0137",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact-match UniProt annotation lists Mg(2+) and Mn(2+) and says the protein binds two Mg(2+) or Mn(2+) ions per subunit, so Mg(2+) is supported among the listed choices. This is a transferred annotation, not direct experimental evidence in the supplied excerpts.",
    "evidence_ids": ["C1", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a serine/threonine protein phosphatase catalytic region, including conserved metal-dependent phosphatase motifs. Such phosphatases use divalent metal ions, commonly Mg(2+) or Mn(2+); that is a better fit than Co(2+), Cu(2+), or a [2Fe-2S] cluster among the given choices.",
    "missing_item_specific_fact": "The exact protein-specific metal-binding annotation and direct experimental metal occupancy are not supplied; the sequence-based family inference does not establish whether Mg(2+) or Mn(2+) is preferred.",
    "reason": "The catalytic-family motifs and the answer choices provide a meaningful biological basis for selecting Mg(2+) over the listed alternatives, without requiring recognition of the exact sequence or its database entry. The supplied evidence supports Mg(2+) but also notes Mn(2+), which is not an option."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The annotation also names Mn(2+), but it is not among the choices. Of the listed options, Mg(2+) is the one supported by the protein-family inference and annotation."
  },
  "important_caveats": [
    "The cofactor annotation is transferred by similarity (ECO:0000250), not shown here as a direct measurement for this exact protein.",
    "The evidence identifies the protein as a Trypanosoma brucei serine/threonine protein phosphatase and matches the supplied sequence, but does not independently validate the underlying primary-paper metal measurements."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q388N2 (PPP5_TRYB2, Trypanosoma brucei PP5-type serine/threonine phosphatase, EC 3.1.3.16) annotates Mg(2+) as a cofactor (C5, H4), noting 'Binds 2 Mg(2+) or Mn(2+) cations per subunit.' The evidence code is ECO:0000250 (inferred by similarity to human PP5, P53041), which is a computational/similarity transfer rather than direct experimental measurement on this specific protein. However, Mg(2+) dependence is a well-established biochemical property of the entire PPP superfamily of phosphoprotein phosphatases, and the 2001 Chaudhuri characterization (PubMed:11290414) confirmed catalytic activity of TbPP5. Mn(2+) is listed as an alternative cofactor but is not among the answer choices, so Mg(2+) is unambiguously the best answer among A–D.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4), [C6](#evidence-c6), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the hallmark GDxHG motif of the PPP superfamily of phosphoprotein phosphatases (visible as 'GDTHG' near residue ~200, along with downstream 'GDFVDRG', 'HGGLYSS', and 'GGKCITVFSAPNYCDQMGNKGAFIRFTGGDM' motifs). Recognition of these motifs identifies the protein as a PPP-type phosphatase. All PPP-type phosphatases (PP1, PP2A, PP2B, PP4, PP5, PP6, PP7) catalyze phosphoryl transfer via a binuclear divalent-metal center, almost universally Mg(2+) or Mn(2+). Among the four choices, Co(2+) (associated with B12-dependent enzymes), &#91;2Fe-2S&#93; clusters (electron-transfer proteins), and Cu(2+) (oxidases, SODs) are incompatible with a phosphatase active site. Mg(2+) is the only option consistent with the PPP catalytic mechanism. This reasoning relies on general enzymology of the PPP superfamily, not on memorizing the specific UniProt entry.


**Missing item-specific fact**

> None critical. Exact PP5 vs PP1 vs PP2A sub-classification is not required because all PPP members share the same Mg(2+)/Mn(2+) metal requirement. The GDxHG motif is sufficient to place the protein in the PPP superfamily.


**Reason**

> A knowledgeable model can identify PPP-family sequence motifs (GDxHG, GD, HG, GG) in the raw sequence, infer the enzyme class, and apply the well-known fact that PPP phosphatases require divalent Mg(2+) (or Mn(2+)) for catalysis. The three distractors represent cofactor classes belonging to entirely different enzyme families, making them distinguishable by general biological reasoning without needing to recall this specific protein's database annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Mn(2+) is also annotated as an alternative cofactor in UniProt, but it is not offered as a choice, so it cannot create ambiguity. Among A–D, only Mg(2+) is consistent with PPP-type phosphatase biochemistry. The other three options (Co2+, &#91;2Fe-2S&#93;, Cu2+) belong to unrelated enzyme classes and are clearly incorrect.


### Important caveats

- The UniProt cofactor annotation carries evidence code ECO:0000250 (similarity-based transfer from human PP5 P53041), not a direct experimental measurement on TbPP5 itself. However, the 2001 Chaudhuri paper (PubMed:11290414) did characterize TbPP5 catalytic activity, and Mg(2+) dependence is a universal property of PPP-type phosphatases.
- Mn(2+) is listed as an interchangeable cofactor in the annotation ('Mg(2+) or Mn(2+)'), but since Mn(2+) is absent from the choices, this does not affect the answer.
- The sequence-to-accession match was confirmed (SHA-256 match, 472 aa, sequence version 1) in both current and archived (v114) UniProt records.
- The GDxHG motif identification from raw sequence is a reasonable but non-trivial pattern-recognition step; a model unfamiliar with PPP-family motifs might not extract this information, but the reasoning pathway is valid and does not require memorization of this specific entry.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the hallmark GDxHG motif of the PPP superfamily of phosphoprotein phosphatases (visible as 'GDTHG' near residue ~200, along with downstream 'GDFVDRG', 'HGGLYSS', and 'GGKCITVFSAPNYCDQMGNKGAFIRFTGGDM' motifs). Recognition of these motifs identifies the protein as a PPP-type phosphatase. All PPP-type phosphatases (PP1, PP2A, PP2B, PP4, PP5, PP6, PP7) catalyze phosphoryl transfer via a binuclear divalent-metal center, almost universally Mg(2+) or Mn(2+). Among the four choices, Co(2+) (associated with B12-dependent enzymes), [2Fe-2S] clusters (electron-transfer proteins), and Cu(2+) (oxidases, SODs) are incompatible with a phosphatase active site. Mg(2+) is the only option consistent with the PPP catalytic mechanism. This reasoning relies on general enzymology of the PPP superfamily, not on memorizing the specific UniProt entry.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. Exact PP5 vs PP1 vs PP2A sub-classification is not required because all PPP members share the same Mg(2+)/Mn(2+) metal requirement. The GDxHG motif is sufficient to place the protein in the PPP superfamily.",
    "reason": "A knowledgeable model can identify PPP-family sequence motifs (GDxHG, GD, HG, GG) in the raw sequence, infer the enzyme class, and apply the well-known fact that PPP phosphatases require divalent Mg(2+) (or Mn(2+)) for catalysis. The three distractors represent cofactor classes belonging to entirely different enzyme families, making them distinguishable by general biological reasoning without needing to recall this specific protein's database annotation."
  },
  "case_id": "cofactor_0137",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4",
      "C6",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q388N2 (PPP5_TRYB2, Trypanosoma brucei PP5-type serine/threonine phosphatase, EC 3.1.3.16) annotates Mg(2+) as a cofactor (C5, H4), noting 'Binds 2 Mg(2+) or Mn(2+) cations per subunit.' The evidence code is ECO:0000250 (inferred by similarity to human PP5, P53041), which is a computational/similarity transfer rather than direct experimental measurement on this specific protein. However, Mg(2+) dependence is a well-established biochemical property of the entire PPP superfamily of phosphoprotein phosphatases, and the 2001 Chaudhuri characterization (PubMed:11290414) confirmed catalytic activity of TbPP5. Mn(2+) is listed as an alternative cofactor but is not among the answer choices, so Mg(2+) is unambiguously the best answer among A–D."
  },
  "important_caveats": [
    "The UniProt cofactor annotation carries evidence code ECO:0000250 (similarity-based transfer from human PP5 P53041), not a direct experimental measurement on TbPP5 itself. However, the 2001 Chaudhuri paper (PubMed:11290414) did characterize TbPP5 catalytic activity, and Mg(2+) dependence is a universal property of PPP-type phosphatases.",
    "Mn(2+) is listed as an interchangeable cofactor in the annotation ('Mg(2+) or Mn(2+)'), but since Mn(2+) is absent from the choices, this does not affect the answer.",
    "The sequence-to-accession match was confirmed (SHA-256 match, 472 aa, sequence version 1) in both current and archived (v114) UniProt records.",
    "The GDxHG motif identification from raw sequence is a reasonable but non-trivial pattern-recognition step; a model unfamiliar with PPP-family motifs might not extract this information, but the reasoning pathway is valid and does not require memorization of this specific entry."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Mn(2+) is also annotated as an alternative cofactor in UniProt, but it is not offered as a choice, so it cannot create ambiguity. Among A–D, only Mg(2+) is consistent with PPP-type phosphatase biochemistry. The other three options (Co2+, [2Fe-2S], Cu2+) belong to unrelated enzyme classes and are clearly incorrect."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0137",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q388N2 (PPP5_TRYB2, Trypanosoma brucei PP5-type serine/threonine phosphatase, EC 3.1.3.16) annotates Mg(2+) as a cofactor (C5, H4), noting 'Binds 2 Mg(2+) or Mn(2+) cations per subunit.' The evidence code is ECO:0000250 (inferred by similarity to human PP5, P53041), which is a computational/similarity transfer rather than direct experimental measurement on this specific protein. However, Mg(2+) dependence is a well-established biochemical property of the entire PPP superfamily of phosphoprotein phosphatases, and the 2001 Chaudhuri characterization (PubMed:11290414) confirmed catalytic activity of TbPP5. Mn(2+) is listed as an alternative cofactor but is not among the answer choices, so Mg(2+) is unambiguously the best answer among A–D.",
    "evidence_ids": ["C5", "H4", "C6", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the hallmark GDxHG motif of the PPP superfamily of phosphoprotein phosphatases (visible as 'GDTHG' near residue ~200, along with downstream 'GDFVDRG', 'HGGLYSS', and 'GGKCITVFSAPNYCDQMGNKGAFIRFTGGDM' motifs). Recognition of these motifs identifies the protein as a PPP-type phosphatase. All PPP-type phosphatases (PP1, PP2A, PP2B, PP4, PP5, PP6, PP7) catalyze phosphoryl transfer via a binuclear divalent-metal center, almost universally Mg(2+) or Mn(2+). Among the four choices, Co(2+) (associated with B12-dependent enzymes), [2Fe-2S] clusters (electron-transfer proteins), and Cu(2+) (oxidases, SODs) are incompatible with a phosphatase active site. Mg(2+) is the only option consistent with the PPP catalytic mechanism. This reasoning relies on general enzymology of the PPP superfamily, not on memorizing the specific UniProt entry.",
    "missing_item_specific_fact": "None critical. Exact PP5 vs PP1 vs PP2A sub-classification is not required because all PPP members share the same Mg(2+)/Mn(2+) metal requirement. The GDxHG motif is sufficient to place the protein in the PPP superfamily.",
    "reason": "A knowledgeable model can identify PPP-family sequence motifs (GDxHG, GD, HG, GG) in the raw sequence, infer the enzyme class, and apply the well-known fact that PPP phosphatases require divalent Mg(2+) (or Mn(2+)) for catalysis. The three distractors represent cofactor classes belonging to entirely different enzyme families, making them distinguishable by general biological reasoning without needing to recall this specific protein's database annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Mn(2+) is also annotated as an alternative cofactor in UniProt, but it is not offered as a choice, so it cannot create ambiguity. Among A–D, only Mg(2+) is consistent with PPP-type phosphatase biochemistry. The other three options (Co2+, [2Fe-2S], Cu2+) belong to unrelated enzyme classes and are clearly incorrect."
  },
  "important_caveats": [
    "The UniProt cofactor annotation carries evidence code ECO:0000250 (similarity-based transfer from human PP5 P53041), not a direct experimental measurement on TbPP5 itself. However, the 2001 Chaudhuri paper (PubMed:11290414) did characterize TbPP5 catalytic activity, and Mg(2+) dependence is a universal property of PPP-type phosphatases.",
    "Mn(2+) is listed as an interchangeable cofactor in the annotation ('Mg(2+) or Mn(2+)'), but since Mn(2+) is absent from the choices, this does not affect the answer.",
    "The sequence-to-accession match was confirmed (SHA-256 match, 472 aa, sequence version 1) in both current and archived (v114) UniProt records.",
    "The GDxHG motif identification from raw sequence is a reasonable but non-trivial pattern-recognition step; a model unfamiliar with PPP-family motifs might not extract this information, but the reasoning pathway is valid and does not require memorization of this specific entry."
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

**Accession:** `Q388N2` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 114. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q388N2.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:44.659218+00:00.  

```json
"Q388N2"
```

Source SHA-256: `8d8adced98584260feb2d973bbdc1cfedd05c91c22d7759b69dbc8e335985936`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q388N2.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:44.659218+00:00.  

```json
{"cofactors":[{"cofactorCrossReference":{"database":"ChEBI","id":"CHEBI:18420"},"evidences":[{"evidenceCode":"ECO:0000250","id":"P53041","source":"UniProtKB"}],"name":"Mg(2+)"},{"cofactorCrossReference":{"database":"ChEBI","id":"CHEBI:29035"},"evidences":[{"evidenceCode":"ECO:0000250","id":"P53041","source":"UniProtKB"}],"name":"Mn(2+)"}],"commentType":"COFACTOR","note":{"texts":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"P53041","source":"UniProtKB"}],"value":"Binds 2 Mg(2+) or Mn(2+) cations per subunit."}]}}
```

Source SHA-256: `8d8adced98584260feb2d973bbdc1cfedd05c91c22d7759b69dbc8e335985936`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q388N2.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:44.659218+00:00.  

```json
{"citation":{"authors":["Chaudhuri M."],"citationCrossReferences":[{"database":"PubMed","id":"11290414"},{"database":"DOI","id":"10.1016/s0378-1119(01)00367-5"}],"citationType":"journal article","firstPage":"1","id":"11290414","journal":"Gene","lastPage":"13","publicationDate":"2001","title":"Cloning and characterization of a novel serine/threonine protein phosphatase type 5 from Trypanosoma brucei.","volume":"266"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceComments":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"11290414","source":"PubMed"}],"type":"STRAIN","value":"LUMP 1026"}],"referenceNumber":2,"referencePositions":["CATALYTIC ACTIVITY","ACTIVITY REGULATION","BIOPHYSICOCHEMICAL PROPERTIES","SUBCELLULAR LOCATION"]}
```

Source SHA-256: `8d8adced98584260feb2d973bbdc1cfedd05c91c22d7759b69dbc8e335985936`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q388N2?format=txt&versions=114)  
**Locator:** `lines 40-48`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 114 / 1.  
**Retrieved:** 2026-11-02T04:30:47.011986+00:00.  

```text
RN   [2] {ECO:0000305}
RP   CATALYTIC ACTIVITY, ACTIVITY REGULATION, BIOPHYSICOCHEMICAL PROPERTIES, AND
RP   SUBCELLULAR LOCATION.
RC   STRAIN=LUMP 1026 {ECO:0000303|PubMed:11290414};
RX   PubMed=11290414; DOI=10.1016/s0378-1119(01)00367-5;
RA   Chaudhuri M.;
RT   "Cloning and characterization of a novel serine/threonine protein
RT   phosphatase type 5 from Trypanosoma brucei.";
RL   Gene 266:1-13(2001).
```

Source SHA-256: `ceefd57fac247af4269990ea2789068697ac2e8d9452900d9533c01a71737c9f`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q388N2?format=txt&versions=114)  
**Locator:** `lines 67-73`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 114 / 1.  
**Retrieved:** 2026-11-02T04:30:47.011986+00:00.  

```text
CC   -!- COFACTOR:
CC       Name=Mg(2+); Xref=ChEBI:CHEBI:18420;
CC         Evidence={ECO:0000250|UniProtKB:P53041};
CC       Name=Mn(2+); Xref=ChEBI:CHEBI:29035;
CC         Evidence={ECO:0000250|UniProtKB:P53041};
CC       Note=Binds 2 Mg(2+) or Mn(2+) cations per subunit.
CC       {ECO:0000250|UniProtKB:P53041};
```

Source SHA-256: `ceefd57fac247af4269990ea2789068697ac2e8d9452900d9533c01a71737c9f`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 137. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
