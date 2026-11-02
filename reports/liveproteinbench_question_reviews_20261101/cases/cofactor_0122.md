# cofactor_0122

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `cofactor`  
**Author expected answer:** **A** — FAD

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MYMLRPSSLLLATGLLNQGSSVLAAVISRASNQTFDYVIVGGGTAGLVLANRLTEDSSVTVAVVEAGTFPEDVVGNVTQVPAYAPQFEGAELDLEWNFTTTPQAGLGNIPVSYYRAKALGGCSDINFMAYGRTSKGAHQLWADLVGDDSYTYDNMVKYYKKTMNFSPPNAETRLANATPMYDTVDTSTGGGIDVTFPSFAQSWSTWVSKGLAAIGLPQAHSFVDGNLLGHSWQMVGITQSTGIRSSAQAGYLRPVMSRPNLTILNGTFAERIIFNGDAASGVEVTAKGQTYTLTSKKELILSAGVFQSPQLLMVSGVGPKALLDKFNIPVVKDLPGVGQNMVDHITVPLSYQVDVVTSSTLAGSSLEEAITEWNTHGTGPLSNNGGDYIGMEKAPAEFRANFSAETVKQLSALPEDWPELQYNVLPATVSSTSIGGEGSVLGGNYGSMLASVIAPQSRGNVSIASASMSDAPLINPNIFTAQADIDLLLTAFKRVRQALQSSAMAPIMIGDEFFPGPTVQTDEQILDYLTETVRPFSHGFATCKMGKSSDPDAVIDSHGKVYGIKNLRVVDASSFPFLPPGPAPQIQVYTLAEKLADDIKQTKY

[Multiple Choices]
A. FAD
B. Mg(2+)
C. heme
D. pantetheine 4'-phosphate
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

> The exact sequence matches a UniProt record annotated with FAD as a cofactor. That annotation is transferred by similarity (ECO:0000250), not direct experimental evidence for this sequence.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has an N-terminal glycine-rich dinucleotide-binding motif (VIVGGGTAG), consistent with the FAD-binding region of a GMC-family oxidoreductase. This supports FAD over the listed metal, heme, and pantetheine-phosphate alternatives, though the motif alone is not conclusive.


**Missing item-specific fact**

> A direct cofactor measurement or protein-specific annotation is absent from the prompt; neither is necessary for a defensible sequence-based inference among these choices.


**Reason**

> The sequence contains a concrete cofactor-binding clue that meaningfully favors FAD among the options. The reviewer-only annotation supports the key but is not needed as input to that inference.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> FAD is the best-supported option; the other choices are not comparably supported by the sequence.


### Important caveats

- The database cofactor annotation is similarity-transferred rather than direct experimental evidence for this exact protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has an N-terminal glycine-rich dinucleotide-binding motif (VIVGGGTAG), consistent with the FAD-binding region of a GMC-family oxidoreductase. This supports FAD over the listed metal, heme, and pantetheine-phosphate alternatives, though the motif alone is not conclusive.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "A direct cofactor measurement or protein-specific annotation is absent from the prompt; neither is necessary for a defensible sequence-based inference among these choices.",
    "reason": "The sequence contains a concrete cofactor-binding clue that meaningfully favors FAD among the options. The reviewer-only annotation supports the key but is not needed as input to that inference."
  },
  "case_id": "cofactor_0122",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt record annotated with FAD as a cofactor. That annotation is transferred by similarity (ECO:0000250), not direct experimental evidence for this sequence."
  },
  "important_caveats": [
    "The database cofactor annotation is similarity-transferred rather than direct experimental evidence for this exact protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "FAD is the best-supported option; the other choices are not comparably supported by the sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0122",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt record annotated with FAD as a cofactor. That annotation is transferred by similarity (ECO:0000250), not direct experimental evidence for this sequence.",
    "evidence_ids": ["C1", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has an N-terminal glycine-rich dinucleotide-binding motif (VIVGGGTAG), consistent with the FAD-binding region of a GMC-family oxidoreductase. This supports FAD over the listed metal, heme, and pantetheine-phosphate alternatives, though the motif alone is not conclusive.",
    "missing_item_specific_fact": "A direct cofactor measurement or protein-specific annotation is absent from the prompt; neither is necessary for a defensible sequence-based inference among these choices.",
    "reason": "The sequence contains a concrete cofactor-binding clue that meaningfully favors FAD among the options. The reviewer-only annotation supports the key but is not needed as input to that inference."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "FAD is the best-supported option; the other choices are not comparably supported by the sequence."
  },
  "important_caveats": [
    "The database cofactor annotation is similarity-transferred rather than direct experimental evidence for this exact protein."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry P0DY22 explicitly annotates FAD (CHEBI:57692) as the cofactor (evidence_id C5/H4). The evidence code is ECO:0000250 (inferred by similarity to UniProtKB:E4QP00), meaning the FAD assignment is transferred by homology rather than from a direct binding assay. However, the protein is named 'Glucose-methanol-choline family oxidoreductase' (EC 1.1.-.-), a family that is universally FAD-dependent across all characterized members. The EC number itself carries experimental evidence (ECO:0000269, PubMed:38404388). The annotation is well-supported by family-level biochemistry.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4), [C4](#evidence-c4), [H2](#evidence-h2), [C6](#evidence-c6), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal region contains 'GGGTAGLVLANRL', a glycine-rich motif (GxGxxG-like) characteristic of Rossmann-fold dinucleotide-binding domains, which in oxidoreductases of this size and architecture points to FAD rather than NAD/NADP (not offered as choices). The ~604-residue multi-domain architecture with catalytic His residues (e.g., 'HGFATCKMG') is consistent with GMC-family oxidoreductases. Critically, the sequence lacks hallmarks of the other three options: no Cys-X-X-Cys or bis-His heme-coordination motifs (rules out heme), no kinase/polymerase Mg-binding loops or DxE motifs (rules out Mg2+), and no ACP/CoA synthetase or phosphopantetheinyl-transferase domains (rules out pantetheine 4'-phosphate). The combination of a dinucleotide-binding Rossmann motif + oxidoreductase architecture + absence of alternative cofactor-binding features meaningfully distinguishes FAD.


**Missing item-specific fact**

> None strictly required. Identifying the exact GMC family membership adds confidence but the sequence-level features (Rossmann motif, domain architecture, absence of heme/Mg/ACP motifs) are sufficient to select FAD over the three distractors through general biochemical reasoning.


**Reason**

> A knowledgeable reader can reason from the glycine-rich dinucleotide-binding motif, the overall oxidoreductase architecture, and the absence of structural signatures for heme, Mg2+, or pantetheine 4'-phosphate to select FAD. This does not require memorizing the specific UniProt entry for P0DY22.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The three distractors (Mg2+, heme, pantetheine 4'-phosphate) each have well-defined structural/biochemical signatures absent from this sequence, while the Rossmann-fold motif and oxidoreductase architecture point unambiguously to FAD among the four choices.


### Important caveats

- The FAD annotation carries evidence code ECO:0000250 (similarity-based transfer from E4QP00), not a direct experimental binding measurement. The assignment is nonetheless highly reliable given the universal FAD dependence of the GMC oxidoreductase family.
- The protein is a precursor (signal peptide present); the mature form's cofactor binding is inferred from the full-length annotation.
- The glycine-rich motif 'GGGTAG' is a general Rossmann-fold feature and not unique to FAD-binding proteins; the argument gains strength from the absence of alternative cofactor motifs and the overall architecture.
- The UniProt entry was first released in April 2025 (Swiss-Prot), so the author's data-construction snapshot is unknown; however, sequence match is confirmed across versions.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal region contains 'GGGTAGLVLANRL', a glycine-rich motif (GxGxxG-like) characteristic of Rossmann-fold dinucleotide-binding domains, which in oxidoreductases of this size and architecture points to FAD rather than NAD/NADP (not offered as choices). The ~604-residue multi-domain architecture with catalytic His residues (e.g., 'HGFATCKMG') is consistent with GMC-family oxidoreductases. Critically, the sequence lacks hallmarks of the other three options: no Cys-X-X-Cys or bis-His heme-coordination motifs (rules out heme), no kinase/polymerase Mg-binding loops or DxE motifs (rules out Mg2+), and no ACP/CoA synthetase or phosphopantetheinyl-transferase domains (rules out pantetheine 4'-phosphate). The combination of a dinucleotide-binding Rossmann motif + oxidoreductase architecture + absence of alternative cofactor-binding features meaningfully distinguishes FAD.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required. Identifying the exact GMC family membership adds confidence but the sequence-level features (Rossmann motif, domain architecture, absence of heme/Mg/ACP motifs) are sufficient to select FAD over the three distractors through general biochemical reasoning.",
    "reason": "A knowledgeable reader can reason from the glycine-rich dinucleotide-binding motif, the overall oxidoreductase architecture, and the absence of structural signatures for heme, Mg2+, or pantetheine 4'-phosphate to select FAD. This does not require memorizing the specific UniProt entry for P0DY22."
  },
  "case_id": "cofactor_0122",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4",
      "C4",
      "H2",
      "C6",
      "H3"
    ],
    "judgment": "supported",
    "reason": "UniProt entry P0DY22 explicitly annotates FAD (CHEBI:57692) as the cofactor (evidence_id C5/H4). The evidence code is ECO:0000250 (inferred by similarity to UniProtKB:E4QP00), meaning the FAD assignment is transferred by homology rather than from a direct binding assay. However, the protein is named 'Glucose-methanol-choline family oxidoreductase' (EC 1.1.-.-), a family that is universally FAD-dependent across all characterized members. The EC number itself carries experimental evidence (ECO:0000269, PubMed:38404388). The annotation is well-supported by family-level biochemistry."
  },
  "important_caveats": [
    "The FAD annotation carries evidence code ECO:0000250 (similarity-based transfer from E4QP00), not a direct experimental binding measurement. The assignment is nonetheless highly reliable given the universal FAD dependence of the GMC oxidoreductase family.",
    "The protein is a precursor (signal peptide present); the mature form's cofactor binding is inferred from the full-length annotation.",
    "The glycine-rich motif 'GGGTAG' is a general Rossmann-fold feature and not unique to FAD-binding proteins; the argument gains strength from the absence of alternative cofactor motifs and the overall architecture.",
    "The UniProt entry was first released in April 2025 (Swiss-Prot), so the author's data-construction snapshot is unknown; however, sequence match is confirmed across versions."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors (Mg2+, heme, pantetheine 4'-phosphate) each have well-defined structural/biochemical signatures absent from this sequence, while the Rossmann-fold motif and oxidoreductase architecture point unambiguously to FAD among the four choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0122",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry P0DY22 explicitly annotates FAD (CHEBI:57692) as the cofactor (evidence_id C5/H4). The evidence code is ECO:0000250 (inferred by similarity to UniProtKB:E4QP00), meaning the FAD assignment is transferred by homology rather than from a direct binding assay. However, the protein is named 'Glucose-methanol-choline family oxidoreductase' (EC 1.1.-.-), a family that is universally FAD-dependent across all characterized members. The EC number itself carries experimental evidence (ECO:0000269, PubMed:38404388). The annotation is well-supported by family-level biochemistry.",
    "evidence_ids": ["C5", "H4", "C4", "H2", "C6", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal region contains 'GGGTAGLVLANRL', a glycine-rich motif (GxGxxG-like) characteristic of Rossmann-fold dinucleotide-binding domains, which in oxidoreductases of this size and architecture points to FAD rather than NAD/NADP (not offered as choices). The ~604-residue multi-domain architecture with catalytic His residues (e.g., 'HGFATCKMG') is consistent with GMC-family oxidoreductases. Critically, the sequence lacks hallmarks of the other three options: no Cys-X-X-Cys or bis-His heme-coordination motifs (rules out heme), no kinase/polymerase Mg-binding loops or DxE motifs (rules out Mg2+), and no ACP/CoA synthetase or phosphopantetheinyl-transferase domains (rules out pantetheine 4'-phosphate). The combination of a dinucleotide-binding Rossmann motif + oxidoreductase architecture + absence of alternative cofactor-binding features meaningfully distinguishes FAD.",
    "missing_item_specific_fact": "None strictly required. Identifying the exact GMC family membership adds confidence but the sequence-level features (Rossmann motif, domain architecture, absence of heme/Mg/ACP motifs) are sufficient to select FAD over the three distractors through general biochemical reasoning.",
    "reason": "A knowledgeable reader can reason from the glycine-rich dinucleotide-binding motif, the overall oxidoreductase architecture, and the absence of structural signatures for heme, Mg2+, or pantetheine 4'-phosphate to select FAD. This does not require memorizing the specific UniProt entry for P0DY22."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors (Mg2+, heme, pantetheine 4'-phosphate) each have well-defined structural/biochemical signatures absent from this sequence, while the Rossmann-fold motif and oxidoreductase architecture point unambiguously to FAD among the four choices."
  },
  "important_caveats": [
    "The FAD annotation carries evidence code ECO:0000250 (similarity-based transfer from E4QP00), not a direct experimental binding measurement. The assignment is nonetheless highly reliable given the universal FAD dependence of the GMC oxidoreductase family.",
    "The protein is a precursor (signal peptide present); the mature form's cofactor binding is inferred from the full-length annotation.",
    "The glycine-rich motif 'GGGTAG' is a general Rossmann-fold feature and not unique to FAD-binding proteins; the argument gains strength from the absence of alternative cofactor motifs and the overall architecture.",
    "The UniProt entry was first released in April 2025 (Swiss-Prot), so the author's data-construction snapshot is unknown; however, sequence match is confirmed across versions."
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

**Accession:** `P0DY22` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 3. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY22.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:17.365835+00:00.  

```json
"P0DY22"
```

Source SHA-256: `0a1030215a4e72e1b46a0225b21493f9f6dfce6601da454f77118372813fe32b`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY22.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:17.365835+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"38404388","source":"PubMed"}],"value":"11'-O-desmethylfendlerol biosynthesis cluster protein G"}}],"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"38404388","source":"PubMed"}],"value":"1.1.-.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"38404388","source":"PubMed"}],"value":"Glucose-methanol-choline family oxidoreductase mfmG"}}}
```

Source SHA-256: `0a1030215a4e72e1b46a0225b21493f9f6dfce6601da454f77118372813fe32b`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY22.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:17.365835+00:00.  

```json
{"cofactors":[{"cofactorCrossReference":{"database":"ChEBI","id":"CHEBI:57692"},"evidences":[{"evidenceCode":"ECO:0000250","id":"E4QP00","source":"UniProtKB"}],"name":"FAD"}],"commentType":"COFACTOR"}
```

Source SHA-256: `0a1030215a4e72e1b46a0225b21493f9f6dfce6601da454f77118372813fe32b`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY22.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:17.365835+00:00.  

```json
{"citation":{"authors":["Yan D.","Matsuda Y."],"citationCrossReferences":[{"database":"PubMed","id":"38404388"},{"database":"DOI","id":"10.1039/d3sc06001b"}],"citationType":"journal article","firstPage":"3011","id":"38404388","journal":"Chem. Sci.","lastPage":"3017","publicationDate":"2024","title":"Global genome mining-driven discovery of an unusual biosynthetic logic for fungal polyketide-terpenoid hybrids.","volume":"15"},"referenceComments":[{"type":"STRAIN","value":"CBS 123579"}],"referenceNumber":2,"referencePositions":["FUNCTION"]}
```

Source SHA-256: `0a1030215a4e72e1b46a0225b21493f9f6dfce6601da454f77118372813fe32b`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DY22?format=txt&versions=3)  
**Locator:** `lines 6-9`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 3 / 1.  
**Retrieved:** 2026-11-01T06:28:24.566799+00:00.  

```text
DE   RecName: Full=Glucose-methanol-choline family oxidoreductase mfmG {ECO:0000303|PubMed:38404388};
DE            EC=1.1.-.- {ECO:0000269|PubMed:38404388};
DE   AltName: Full=11'-O-desmethylfendlerol biosynthesis cluster protein G {ECO:0000303|PubMed:38404388};
DE   Flags: Precursor;
```

Source SHA-256: `d2ebe5fbb151283783c913740097fccd492619e1a926b895e190197148649337`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DY22?format=txt&versions=3)  
**Locator:** `lines 29-36`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 3 / 1.  
**Retrieved:** 2026-11-01T06:28:24.566799+00:00.  

```text
RN   [2]
RP   FUNCTION.
RC   STRAIN=CBS 123579;
RX   PubMed=38404388; DOI=10.1039/d3sc06001b;
RA   Yan D., Matsuda Y.;
RT   "Global genome mining-driven discovery of an unusual biosynthetic logic for
RT   fungal polyketide-terpenoid hybrids.";
RL   Chem. Sci. 15:3011-3017(2024).
```

Source SHA-256: `d2ebe5fbb151283783c913740097fccd492619e1a926b895e190197148649337`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DY22?format=txt&versions=3)  
**Locator:** `lines 56-58`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 3 / 1.  
**Retrieved:** 2026-11-01T06:28:24.566799+00:00.  

```text
CC   -!- COFACTOR:
CC       Name=FAD; Xref=ChEBI:CHEBI:57692;
CC         Evidence={ECO:0000250|UniProtKB:E4QP00};
```

Source SHA-256: `d2ebe5fbb151283783c913740097fccd492619e1a926b895e190197148649337`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 122. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
