# cofactor_0135

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `cofactor`  
**Author expected answer:** **D** — Mg(2+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MASSDLEAATALKVQGNKAFGQHEWPTAVDFYTQAIAKYDREPSFFSNRAQAHIKLEAYGFAIADATKALELDPAYTKAYWRRALANTAILNYKDALRDFKVVAKREPNNRDAKVKLADCEKLVRRMEFEKAIEVGDPPSAFEDLDIDAIAVDDSYDGVRLEKEMTQEFIDDMIERFKNGKKIHRKYAFQIVKAVKDIVYAEPTMVEIGVDQGTKLTVCGDTHGQFFDLLEIFRLNGYPSEKHAYLFNGDFVDRGSWSTEIALLLYAYKWLRPNGIFLNRGNHETDDMNKVYGFEGECKAKYNERMFKVFSESFSALPLATLIGNKYLVLHGGLFSDDNTSLDDIRKLDRHNQRQPGQQGLMMEMLWTDPQTEPGRGPSKRGVGLQFGPDVTKRFCEKNGLEAIIRSHEVRMEGYEVEHDGRCITVFSAPKYCDTTENKGAFINVGPELKLDFQVFEAVPHPDIKPMAYAQNSIMSMM

[Multiple Choices]
A. heme
B. Zn(2+)
C. Mn(2+)
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

> The matched UniProt annotation lists Mg(2+) as a cofactor, so choice D is supported. However, it also lists Mn(2+) and says the protein binds two Mg(2+) or Mn(2+) ions; the annotation is transferred by similarity rather than direct evidence for this sequence.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may suggest a metal-dependent phosphatase, but it provides no meaningful basis for choosing Mg(2+) over Mn(2+).


**Missing item-specific fact**

> The protein-specific cofactor annotation, which itself permits Mg(2+) or Mn(2+).


**Reason**

> Distinguishing the keyed option requires protein-specific information not supplied in the question, and the available annotation does not establish Mg(2+) as uniquely required.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C",
  "D"
]
```

> The matched annotation names both Mn(2+) and Mg(2+) and describes binding either metal.


### Important caveats

- The sequence matches the annotated protein exactly, but the cofactor annotation is transferred from a homolog and is not independent experimental confirmation for this sequence.
- The evidence supports Mg(2+) as an option, not as the uniquely correct answer.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence may suggest a metal-dependent phosphatase, but it provides no meaningful basis for choosing Mg(2+) over Mn(2+).",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific cofactor annotation, which itself permits Mg(2+) or Mn(2+).",
    "reason": "Distinguishing the keyed option requires protein-specific information not supplied in the question, and the available annotation does not establish Mg(2+) as uniquely required."
  },
  "case_id": "cofactor_0135",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The matched UniProt annotation lists Mg(2+) as a cofactor, so choice D is supported. However, it also lists Mn(2+) and says the protein binds two Mg(2+) or Mn(2+) ions; the annotation is transferred by similarity rather than direct evidence for this sequence."
  },
  "important_caveats": [
    "The sequence matches the annotated protein exactly, but the cofactor annotation is transferred from a homolog and is not independent experimental confirmation for this sequence.",
    "The evidence supports Mg(2+) as an option, not as the uniquely correct answer."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C",
      "D"
    ],
    "reason": "The matched annotation names both Mn(2+) and Mg(2+) and describes binding either metal."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0135",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched UniProt annotation lists Mg(2+) as a cofactor, so choice D is supported. However, it also lists Mn(2+) and says the protein binds two Mg(2+) or Mn(2+) ions; the annotation is transferred by similarity rather than direct evidence for this sequence.",
    "evidence_ids": ["C1", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may suggest a metal-dependent phosphatase, but it provides no meaningful basis for choosing Mg(2+) over Mn(2+).",
    "missing_item_specific_fact": "The protein-specific cofactor annotation, which itself permits Mg(2+) or Mn(2+).",
    "reason": "Distinguishing the keyed option requires protein-specific information not supplied in the question, and the available annotation does not establish Mg(2+) as uniquely required."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["C", "D"],
    "reason": "The matched annotation names both Mn(2+) and Mg(2+) and describes binding either metal."
  },
  "important_caveats": [
    "The sequence matches the annotated protein exactly, but the cofactor annotation is transferred from a homolog and is not independent experimental confirmation for this sequence.",
    "The evidence supports Mg(2+) as an option, not as the uniquely correct answer."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation (C5/H4) explicitly lists Mg(2+) as a cofactor for this serine/threonine-protein phosphatase T (Q2U919, EC 3.1.3.16), stating 'Binds 2 Mg(2+) or Mn(2+) cations per subunit.' The evidence code is ECO:0000250 (similarity-based transfer from P53041, human PPP5), not direct experimental determination for this specific protein. However, a PubMed reference (17475320) reports catalytic activity and biophysical properties for this enzyme, lending indirect experimental support. Mg(2+) is indeed a valid cofactor, so D is supported. However, Mn(2+) (choice C) is equally listed in the same annotation, creating a parallel defensible answer.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the canonical PPP-family metal-binding motif 'GDxHG' (visible in 'TVCGDTHGQFFDL'), which is the hallmark of the PPP superfamily of metal-dependent phosphatases (PP1, PP2A, PP2B, PP4, PP5, PP6, PP7). This motif coordinates two divalent cations (Mg(2+)/Mn(2+)) at the active site and is structurally incompatible with heme (which requires a porphyrin-binding pocket with proximal His in a globin fold) or Zn(2+) (which is used by metalloproteases and other Zn-dependent enzymes with distinct Cys/His coordination geometry). This allows a knowledgeable model to eliminate A (heme) and B (Zn(2+)). For the C vs D distinction, general knowledge of the PPP family indicates Mg(2+) is the primary physiological metal, with Mn(2+) as a less-preferred substitute that can support activity in vitro. This family-level preference is a defensible biological argument favoring D over C.


**Missing item-specific fact**

> The annotation itself states 'Mg(2+) or Mn(2+),' implying both metals can serve as cofactors. No item-specific experimental data in the supplied evidence definitively establishes that Mg(2+) is uniquely required versus Mn(2+) for this particular Aspergillus oryzae PPT. The distinction between the two is based on the conventional listing order and family-level preference rather than a sequence-specific determinant.


**Reason**

> The GDxHG motif and PPP-family membership provide concrete sequence-based reasoning to eliminate heme and Zn(2+). The preference for Mg(2+) over Mn(2+) in PPP phosphatases is well-established general biochemical knowledge, making D the best single answer. However, the C vs D distinction relies on family-level convention rather than a sequence-specific feature unique to this protein, and the annotation explicitly permits either metal.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C",
  "D"
]
```

> The UniProt annotation lists both Mg(2+) and Mn(2+) as cofactors with the note 'Binds 2 Mg(2+) or Mn(2+) cations per subunit,' giving them equal standing in the annotation. While Mg(2+) is conventionally the physiological metal for PPP-family phosphatases and is listed first, the annotation does not exclude Mn(2+). A model selecting C (Mn(2+)) could argue it is equally supported by the database annotation. The question asks for 'the specific cofactor' (singular), but the source data does not uniquely privilege one over the other.


### Important caveats

- The cofactor annotation carries evidence code ECO:0000250 (similarity/inferred by curator from P53041, human PPP5), not direct experimental determination for this Aspergillus oryzae protein. The PubMed reference (17475320) reports catalytic activity and biophysical properties but the specific metal preference data from that paper were not independently retrieved.
- The sequence is 478 aa and matches the UniProt entry exactly (SHA-256 confirmed). The protein is a PPP-family phosphatase with a TPR regulatory domain, consistent with PPP5-type architecture.
- The 'or' in 'Mg(2+) or Mn(2+)' in the annotation note implies functional interchangeability of the two metals, which complicates a single-answer format for this question.
- All reviewer-only evidence was absent from the evaluated model input; the model must rely solely on the 478-aa sequence and general biological knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the canonical PPP-family metal-binding motif 'GDxHG' (visible in 'TVCGDTHGQFFDL'), which is the hallmark of the PPP superfamily of metal-dependent phosphatases (PP1, PP2A, PP2B, PP4, PP5, PP6, PP7). This motif coordinates two divalent cations (Mg(2+)/Mn(2+)) at the active site and is structurally incompatible with heme (which requires a porphyrin-binding pocket with proximal His in a globin fold) or Zn(2+) (which is used by metalloproteases and other Zn-dependent enzymes with distinct Cys/His coordination geometry). This allows a knowledgeable model to eliminate A (heme) and B (Zn(2+)). For the C vs D distinction, general knowledge of the PPP family indicates Mg(2+) is the primary physiological metal, with Mn(2+) as a less-preferred substitute that can support activity in vitro. This family-level preference is a defensible biological argument favoring D over C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The annotation itself states 'Mg(2+) or Mn(2+),' implying both metals can serve as cofactors. No item-specific experimental data in the supplied evidence definitively establishes that Mg(2+) is uniquely required versus Mn(2+) for this particular Aspergillus oryzae PPT. The distinction between the two is based on the conventional listing order and family-level preference rather than a sequence-specific determinant.",
    "reason": "The GDxHG motif and PPP-family membership provide concrete sequence-based reasoning to eliminate heme and Zn(2+). The preference for Mg(2+) over Mn(2+) in PPP phosphatases is well-established general biochemical knowledge, making D the best single answer. However, the C vs D distinction relies on family-level convention rather than a sequence-specific feature unique to this protein, and the annotation explicitly permits either metal."
  },
  "case_id": "cofactor_0135",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation (C5/H4) explicitly lists Mg(2+) as a cofactor for this serine/threonine-protein phosphatase T (Q2U919, EC 3.1.3.16), stating 'Binds 2 Mg(2+) or Mn(2+) cations per subunit.' The evidence code is ECO:0000250 (similarity-based transfer from P53041, human PPP5), not direct experimental determination for this specific protein. However, a PubMed reference (17475320) reports catalytic activity and biophysical properties for this enzyme, lending indirect experimental support. Mg(2+) is indeed a valid cofactor, so D is supported. However, Mn(2+) (choice C) is equally listed in the same annotation, creating a parallel defensible answer."
  },
  "important_caveats": [
    "The cofactor annotation carries evidence code ECO:0000250 (similarity/inferred by curator from P53041, human PPP5), not direct experimental determination for this Aspergillus oryzae protein. The PubMed reference (17475320) reports catalytic activity and biophysical properties but the specific metal preference data from that paper were not independently retrieved.",
    "The sequence is 478 aa and matches the UniProt entry exactly (SHA-256 confirmed). The protein is a PPP-family phosphatase with a TPR regulatory domain, consistent with PPP5-type architecture.",
    "The 'or' in 'Mg(2+) or Mn(2+)' in the annotation note implies functional interchangeability of the two metals, which complicates a single-answer format for this question.",
    "All reviewer-only evidence was absent from the evaluated model input; the model must rely solely on the 478-aa sequence and general biological knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C",
      "D"
    ],
    "reason": "The UniProt annotation lists both Mg(2+) and Mn(2+) as cofactors with the note 'Binds 2 Mg(2+) or Mn(2+) cations per subunit,' giving them equal standing in the annotation. While Mg(2+) is conventionally the physiological metal for PPP-family phosphatases and is listed first, the annotation does not exclude Mn(2+). A model selecting C (Mn(2+)) could argue it is equally supported by the database annotation. The question asks for 'the specific cofactor' (singular), but the source data does not uniquely privilege one over the other."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0135",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation (C5/H4) explicitly lists Mg(2+) as a cofactor for this serine/threonine-protein phosphatase T (Q2U919, EC 3.1.3.16), stating 'Binds 2 Mg(2+) or Mn(2+) cations per subunit.' The evidence code is ECO:0000250 (similarity-based transfer from P53041, human PPP5), not direct experimental determination for this specific protein. However, a PubMed reference (17475320) reports catalytic activity and biophysical properties for this enzyme, lending indirect experimental support. Mg(2+) is indeed a valid cofactor, so D is supported. However, Mn(2+) (choice C) is equally listed in the same annotation, creating a parallel defensible answer.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the canonical PPP-family metal-binding motif 'GDxHG' (visible in 'TVCGDTHGQFFDL'), which is the hallmark of the PPP superfamily of metal-dependent phosphatases (PP1, PP2A, PP2B, PP4, PP5, PP6, PP7). This motif coordinates two divalent cations (Mg(2+)/Mn(2+)) at the active site and is structurally incompatible with heme (which requires a porphyrin-binding pocket with proximal His in a globin fold) or Zn(2+) (which is used by metalloproteases and other Zn-dependent enzymes with distinct Cys/His coordination geometry). This allows a knowledgeable model to eliminate A (heme) and B (Zn(2+)). For the C vs D distinction, general knowledge of the PPP family indicates Mg(2+) is the primary physiological metal, with Mn(2+) as a less-preferred substitute that can support activity in vitro. This family-level preference is a defensible biological argument favoring D over C.",
    "missing_item_specific_fact": "The annotation itself states 'Mg(2+) or Mn(2+),' implying both metals can serve as cofactors. No item-specific experimental data in the supplied evidence definitively establishes that Mg(2+) is uniquely required versus Mn(2+) for this particular Aspergillus oryzae PPT. The distinction between the two is based on the conventional listing order and family-level preference rather than a sequence-specific determinant.",
    "reason": "The GDxHG motif and PPP-family membership provide concrete sequence-based reasoning to eliminate heme and Zn(2+). The preference for Mg(2+) over Mn(2+) in PPP phosphatases is well-established general biochemical knowledge, making D the best single answer. However, the C vs D distinction relies on family-level convention rather than a sequence-specific feature unique to this protein, and the annotation explicitly permits either metal."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["C", "D"],
    "reason": "The UniProt annotation lists both Mg(2+) and Mn(2+) as cofactors with the note 'Binds 2 Mg(2+) or Mn(2+) cations per subunit,' giving them equal standing in the annotation. While Mg(2+) is conventionally the physiological metal for PPP-family phosphatases and is listed first, the annotation does not exclude Mn(2+). A model selecting C (Mn(2+)) could argue it is equally supported by the database annotation. The question asks for 'the specific cofactor' (singular), but the source data does not uniquely privilege one over the other."
  },
  "important_caveats": [
    "The cofactor annotation carries evidence code ECO:0000250 (similarity/inferred by curator from P53041, human PPP5), not direct experimental determination for this Aspergillus oryzae protein. The PubMed reference (17475320) reports catalytic activity and biophysical properties but the specific metal preference data from that paper were not independently retrieved.",
    "The sequence is 478 aa and matches the UniProt entry exactly (SHA-256 confirmed). The protein is a PPP-family phosphatase with a TPR regulatory domain, consistent with PPP5-type architecture.",
    "The 'or' in 'Mg(2+) or Mn(2+)' in the annotation note implies functional interchangeability of the two metals, which complicates a single-answer format for this question.",
    "All reviewer-only evidence was absent from the evaluated model input; the model must rely solely on the 478-aa sequence and general biological knowledge."
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

**Accession:** `Q2U919` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 127. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2U919.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:21.139726+00:00.  

```json
"Q2U919"
```

Source SHA-256: `6676178685d6229700b2ed516c3ca232d2558330a425e199b609fbecba8e2b23`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2U919.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:21.139726+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"17475320","source":"PubMed"}],"value":"AoPPT"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"17475320","source":"PubMed"}],"value":"3.1.3.16"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000250","id":"P53043","source":"UniProtKB"}],"value":"Serine/threonine-protein phosphatase T"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"P53043","source":"UniProtKB"}],"value":"PPT"}]}}
```

Source SHA-256: `6676178685d6229700b2ed516c3ca232d2558330a425e199b609fbecba8e2b23`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2U919.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:21.139726+00:00.  

```json
{"cofactors":[{"cofactorCrossReference":{"database":"ChEBI","id":"CHEBI:18420"},"evidences":[{"evidenceCode":"ECO:0000250","id":"P53041","source":"UniProtKB"}],"name":"Mg(2+)"},{"cofactorCrossReference":{"database":"ChEBI","id":"CHEBI:29035"},"evidences":[{"evidenceCode":"ECO:0000250","id":"P53041","source":"UniProtKB"}],"name":"Mn(2+)"}],"commentType":"COFACTOR","note":{"texts":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"P53041","source":"UniProtKB"}],"value":"Binds 2 Mg(2+) or Mn(2+) cations per subunit."}]}}
```

Source SHA-256: `6676178685d6229700b2ed516c3ca232d2558330a425e199b609fbecba8e2b23`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2U919.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:21.139726+00:00.  

```json
{"citation":{"authors":["Feng B.","Zhao C.H.","Tanaka S.","Imanaka H.","Imamura K.","Nakanishi K."],"citationCrossReferences":[{"database":"PubMed","id":"17475320"},{"database":"DOI","id":"10.1016/j.ijbiomac.2007.03.005"}],"citationType":"journal article","firstPage":"281","id":"17475320","journal":"Int. J. Biol. Macromol.","lastPage":"285","publicationDate":"2007","title":"TPR domain of Ser/Thr phosphatase of Aspergillus oryzae shows no auto-inhibitory effect on the dephosphorylation activity.","volume":"41"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceComments":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"17475320","source":"PubMed"}],"type":"STRAIN","value":"AGL142-72"}],"referenceNumber":2,"referencePositions":["CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES"]}
```

Source SHA-256: `6676178685d6229700b2ed516c3ca232d2558330a425e199b609fbecba8e2b23`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2U919?format=txt&versions=127)  
**Locator:** `lines 63-69`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 127 / 1.  
**Retrieved:** 2026-11-01T06:28:33.211950+00:00.  

```text
CC   -!- COFACTOR:
CC       Name=Mg(2+); Xref=ChEBI:CHEBI:18420;
CC         Evidence={ECO:0000250|UniProtKB:P53041};
CC       Name=Mn(2+); Xref=ChEBI:CHEBI:29035;
CC         Evidence={ECO:0000250|UniProtKB:P53041};
CC       Note=Binds 2 Mg(2+) or Mn(2+) cations per subunit.
CC       {ECO:0000250|UniProtKB:P53041};
```

Source SHA-256: `2651cbb7ccfd83249fbb6eae9366ac5480fd9278b87d40a7024c3dcc2b8c5a20`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 135. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
