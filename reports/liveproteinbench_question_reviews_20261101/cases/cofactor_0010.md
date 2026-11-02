# cofactor_0010

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `cofactor`  
**Author expected answer:** **C** — Zn(2+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MAGKSPEEQHPVKAYGWAATDSSGILSPFKFSRRATGDHDVRVKILYAGVCHSDLQSARNDMGCFTYPLVPGFETVGTATEVGSKVTKVKVGDKVAVGIMVGSCGKCDECVNDRECYCPEVITSYGRIDHDGTPTYGGFSSETVANEKFVFCFPEKLPMAAGAPLLNAGVSVYSAMRFYGLDKPGMHLGVVGLGGLGHLAVKFAKAFGVKVTVISTSTSKKGEAINDLGADAFLVSTDAEQMQAGSGTLDGILDTVPVVHPIEALLGLLKNHTKLVLVGATMGSFELPILPLGVGRKSVVSTIGGSTKETQEMLDFAAEHDITASVEIIPMDYVNTAMERIEKGDVRYRFVIDIGNTLTPPES

[Multiple Choices]
A. heme
B. Fe cation
C. Zn(2+)
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

> The sequence-matched UniProt annotation assigns Zn(2+) and says two zinc ions bind per subunit. This supports the key, although the cofactor annotation is transferred by similarity from UniProtKB:P06525 (ECO:0000250), not presented as a direct measurement on this protein.

Citations as saved: [C5](#evidence-c5), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a conspicuous cysteine-rich region, a plausible metal-binding motif; in the context of a dehydrogenase-like protein, this supports zinc over the heme and iron alternatives.


**Missing item-specific fact**

> The sequence alone does not establish the precise metal-binding role or directly demonstrate that zinc is required for this protein's activity; the available zinc assignment is transferred from a homolog.


**Reason**

> The cysteine-rich sequence gives a meaningful biological clue favoring zinc, even though confirming the specific cofactor assignment requires protein-specific annotation or experimental evidence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Zn(2+) is the only listed choice matching the supported metal-cofactor assignment; the two heme choices and Fe cation are distinct alternatives.


### Important caveats

- The reviewer evidence matches the supplied sequence, but the cofactor evidence is annotation transferred by similarity rather than a direct cofactor measurement on this protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a conspicuous cysteine-rich region, a plausible metal-binding motif; in the context of a dehydrogenase-like protein, this supports zinc over the heme and iron alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The sequence alone does not establish the precise metal-binding role or directly demonstrate that zinc is required for this protein's activity; the available zinc assignment is transferred from a homolog.",
    "reason": "The cysteine-rich sequence gives a meaningful biological clue favoring zinc, even though confirming the specific cofactor assignment requires protein-specific annotation or experimental evidence."
  },
  "case_id": "cofactor_0010",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation assigns Zn(2+) and says two zinc ions bind per subunit. This supports the key, although the cofactor annotation is transferred by similarity from UniProtKB:P06525 (ECO:0000250), not presented as a direct measurement on this protein."
  },
  "important_caveats": [
    "The reviewer evidence matches the supplied sequence, but the cofactor evidence is annotation transferred by similarity rather than a direct cofactor measurement on this protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Zn(2+) is the only listed choice matching the supported metal-cofactor assignment; the two heme choices and Fe cation are distinct alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0010",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation assigns Zn(2+) and says two zinc ions bind per subunit. This supports the key, although the cofactor annotation is transferred by similarity from UniProtKB:P06525 (ECO:0000250), not presented as a direct measurement on this protein.",
    "evidence_ids": ["C5", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a conspicuous cysteine-rich region, a plausible metal-binding motif; in the context of a dehydrogenase-like protein, this supports zinc over the heme and iron alternatives.",
    "missing_item_specific_fact": "The sequence alone does not establish the precise metal-binding role or directly demonstrate that zinc is required for this protein's activity; the available zinc assignment is transferred from a homolog.",
    "reason": "The cysteine-rich sequence gives a meaningful biological clue favoring zinc, even though confirming the specific cofactor assignment requires protein-specific annotation or experimental evidence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Zn(2+) is the only listed choice matching the supported metal-cofactor assignment; the two heme choices and Fe cation are distinct alternatives."
  },
  "important_caveats": [
    "The reviewer evidence matches the supplied sequence, but the cofactor evidence is annotation transferred by similarity rather than a direct cofactor measurement on this protein."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A0U3S9Q3 (1,2-Dihydrovomilenine reductase, EC 1.3.1.73, sequence matched) annotates Zn(2+) as the cofactor with note 'Binds 2 Zn(2+) ions per subunit.' The evidence code is ECO:0000250 (inferred by similarity to P06525, horse liver alcohol dehydrogenase), which is computational transfer rather than direct experimental measurement on this specific protein. However, the protein is experimentally characterized as a cinnamyl alcohol dehydrogenase (CAD)-like reductase (PubMed 26715562, 38212296, 12391554), and CAD-family enzymes are well-established Zn(2+)-dependent oxidoreductases. The Zn(2+) assignment is therefore a sound inference consistent with the protein's experimentally confirmed family membership.

Citations as saved: [C5](#evidence-c5), [H6](#evidence-h6), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 363-aa sequence contains recognizable medium-chain dehydrogenase/reductase architecture: a putative Rossmann-fold NAD-binding region (e.g., 'GGLGHLAVKF' pattern) and a cysteine-rich catalytic motif ('GSCGKCDECVNDRECYCPE') consistent with Zn(2+) coordination by two Cys residues. NAD-dependent alcohol dehydrogenase/reductase enzymes characteristically employ a catalytic Zn(2+) ion coordinated by cysteine ligands. The distractors—heme, Fe cation, and heme b—are cofactors for cytochromes, peroxidases, and other heme-dependent oxidoreductases, which have entirely different sequence signatures (histidine-rich heme-binding motifs, no Rossmann fold). A biologist recognizing the dehydrogenase fold and Cys-based metal-binding site can eliminate heme/Fe options and infer Zn(2+).


**Missing item-specific fact**

> None strictly required. Family-level recognition from sequence motifs plus general knowledge of Zn-dependent alcohol dehydrogenases suffices to distinguish the choices.


**Reason**

> The sequence provides identifiable structural motifs (Rossmann-fold-like NAD-binding segment, Cys-containing Zn-binding region) that map to the alcohol dehydrogenase/reductase superfamily, for which Zn(2+) is the canonical catalytic cofactor. This constitutes a concrete biological argument from the supplied sequence rather than a lookup of a database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Heme, heme b, and Fe cation are cofactors for structurally distinct enzyme classes (cytochromes, peroxidases, iron-sulfur proteins) with no sequence resemblance to the supplied dehydrogenase. Zn(2+) is the only option consistent with the observed Cys-rich catalytic motif and NAD-binding architecture. No ambiguity among the four choices.


### Important caveats

- The UniProt cofactor annotation uses ECO:0000250 (inferred by similarity to P06525), not direct experimental measurement on RsDHVR itself. The Zn(2+) assignment rests on homology-based transfer, though it is well-supported by the protein's experimentally confirmed CAD-like reductase identity.
- The sequence-match is exact (SHA-256 confirmed) between the benchmark input and UniProt entry A0A0U3S9Q3.
- The reviewer-only evidence was not available to the evaluated model; the reasoning argument relies solely on general biochemical knowledge applied to the sequence features visible in the prompt.
- The cofactor is annotated as 'Binds 2 Zn(2+) ions per subunit,' which is consistent with the two-cysteine coordination pattern visible in the sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 363-aa sequence contains recognizable medium-chain dehydrogenase/reductase architecture: a putative Rossmann-fold NAD-binding region (e.g., 'GGLGHLAVKF' pattern) and a cysteine-rich catalytic motif ('GSCGKCDECVNDRECYCPE') consistent with Zn(2+) coordination by two Cys residues. NAD-dependent alcohol dehydrogenase/reductase enzymes characteristically employ a catalytic Zn(2+) ion coordinated by cysteine ligands. The distractors—heme, Fe cation, and heme b—are cofactors for cytochromes, peroxidases, and other heme-dependent oxidoreductases, which have entirely different sequence signatures (histidine-rich heme-binding motifs, no Rossmann fold). A biologist recognizing the dehydrogenase fold and Cys-based metal-binding site can eliminate heme/Fe options and infer Zn(2+).",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required. Family-level recognition from sequence motifs plus general knowledge of Zn-dependent alcohol dehydrogenases suffices to distinguish the choices.",
    "reason": "The sequence provides identifiable structural motifs (Rossmann-fold-like NAD-binding segment, Cys-containing Zn-binding region) that map to the alcohol dehydrogenase/reductase superfamily, for which Zn(2+) is the canonical catalytic cofactor. This constitutes a concrete biological argument from the supplied sequence rather than a lookup of a database entry."
  },
  "case_id": "cofactor_0010",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H6",
      "C6",
      "C7",
      "C8"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A0U3S9Q3 (1,2-Dihydrovomilenine reductase, EC 1.3.1.73, sequence matched) annotates Zn(2+) as the cofactor with note 'Binds 2 Zn(2+) ions per subunit.' The evidence code is ECO:0000250 (inferred by similarity to P06525, horse liver alcohol dehydrogenase), which is computational transfer rather than direct experimental measurement on this specific protein. However, the protein is experimentally characterized as a cinnamyl alcohol dehydrogenase (CAD)-like reductase (PubMed 26715562, 38212296, 12391554), and CAD-family enzymes are well-established Zn(2+)-dependent oxidoreductases. The Zn(2+) assignment is therefore a sound inference consistent with the protein's experimentally confirmed family membership."
  },
  "important_caveats": [
    "The UniProt cofactor annotation uses ECO:0000250 (inferred by similarity to P06525), not direct experimental measurement on RsDHVR itself. The Zn(2+) assignment rests on homology-based transfer, though it is well-supported by the protein's experimentally confirmed CAD-like reductase identity.",
    "The sequence-match is exact (SHA-256 confirmed) between the benchmark input and UniProt entry A0A0U3S9Q3.",
    "The reviewer-only evidence was not available to the evaluated model; the reasoning argument relies solely on general biochemical knowledge applied to the sequence features visible in the prompt.",
    "The cofactor is annotated as 'Binds 2 Zn(2+) ions per subunit,' which is consistent with the two-cysteine coordination pattern visible in the sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Heme, heme b, and Fe cation are cofactors for structurally distinct enzyme classes (cytochromes, peroxidases, iron-sulfur proteins) with no sequence resemblance to the supplied dehydrogenase. Zn(2+) is the only option consistent with the observed Cys-rich catalytic motif and NAD-binding architecture. No ambiguity among the four choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0010",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A0U3S9Q3 (1,2-Dihydrovomilenine reductase, EC 1.3.1.73, sequence matched) annotates Zn(2+) as the cofactor with note 'Binds 2 Zn(2+) ions per subunit.' The evidence code is ECO:0000250 (inferred by similarity to P06525, horse liver alcohol dehydrogenase), which is computational transfer rather than direct experimental measurement on this specific protein. However, the protein is experimentally characterized as a cinnamyl alcohol dehydrogenase (CAD)-like reductase (PubMed 26715562, 38212296, 12391554), and CAD-family enzymes are well-established Zn(2+)-dependent oxidoreductases. The Zn(2+) assignment is therefore a sound inference consistent with the protein's experimentally confirmed family membership.",
    "evidence_ids": ["C5", "H6", "C6", "C7", "C8"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 363-aa sequence contains recognizable medium-chain dehydrogenase/reductase architecture: a putative Rossmann-fold NAD-binding region (e.g., 'GGLGHLAVKF' pattern) and a cysteine-rich catalytic motif ('GSCGKCDECVNDRECYCPE') consistent with Zn(2+) coordination by two Cys residues. NAD-dependent alcohol dehydrogenase/reductase enzymes characteristically employ a catalytic Zn(2+) ion coordinated by cysteine ligands. The distractors—heme, Fe cation, and heme b—are cofactors for cytochromes, peroxidases, and other heme-dependent oxidoreductases, which have entirely different sequence signatures (histidine-rich heme-binding motifs, no Rossmann fold). A biologist recognizing the dehydrogenase fold and Cys-based metal-binding site can eliminate heme/Fe options and infer Zn(2+).",
    "missing_item_specific_fact": "None strictly required. Family-level recognition from sequence motifs plus general knowledge of Zn-dependent alcohol dehydrogenases suffices to distinguish the choices.",
    "reason": "The sequence provides identifiable structural motifs (Rossmann-fold-like NAD-binding segment, Cys-containing Zn-binding region) that map to the alcohol dehydrogenase/reductase superfamily, for which Zn(2+) is the canonical catalytic cofactor. This constitutes a concrete biological argument from the supplied sequence rather than a lookup of a database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Heme, heme b, and Fe cation are cofactors for structurally distinct enzyme classes (cytochromes, peroxidases, iron-sulfur proteins) with no sequence resemblance to the supplied dehydrogenase. Zn(2+) is the only option consistent with the observed Cys-rich catalytic motif and NAD-binding architecture. No ambiguity among the four choices."
  },
  "important_caveats": [
    "The UniProt cofactor annotation uses ECO:0000250 (inferred by similarity to P06525), not direct experimental measurement on RsDHVR itself. The Zn(2+) assignment rests on homology-based transfer, though it is well-supported by the protein's experimentally confirmed CAD-like reductase identity.",
    "The sequence-match is exact (SHA-256 confirmed) between the benchmark input and UniProt entry A0A0U3S9Q3.",
    "The reviewer-only evidence was not available to the evaluated model; the reasoning argument relies solely on general biochemical knowledge applied to the sequence features visible in the prompt.",
    "The cofactor is annotated as 'Binds 2 Zn(2+) ions per subunit,' which is consistent with the two-cysteine coordination pattern visible in the sequence."
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

**Accession:** `A0A0U3S9Q3` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 32. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3S9Q3.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:41.228210+00:00.  

```json
{"cofactors":[{"cofactorCrossReference":{"database":"ChEBI","id":"CHEBI:29105"},"evidences":[{"evidenceCode":"ECO:0000250","id":"P06525","source":"UniProtKB"}],"name":"Zn(2+)"}],"commentType":"COFACTOR","note":{"texts":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"P06525","source":"UniProtKB"}],"value":"Binds 2 Zn(2+) ions per subunit."}]}}
```

Source SHA-256: `ee30accdc431e8b63f4d222bad60253967328240f6c83fd47b2627281e1afe10`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3S9Q3.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:41.228210+00:00.  

```json
{"citation":{"authors":["Geissler M.","Burghard M.","Volk J.","Staniek A.","Warzecha H."],"citationCrossReferences":[{"database":"PubMed","id":"26715562"},{"database":"DOI","id":"10.1007/s00425-015-2446-6"}],"citationType":"journal article","firstPage":"813","id":"26715562","journal":"Planta","lastPage":"824","publicationDate":"2016","title":"A novel cinnamyl alcohol dehydrogenase (CAD)-like reductase contributes to the structural diversity of monoterpenoid indole alkaloids in Rauvolfia.","volume":"243"},"evidences":[{"evidenceCode":"ECO:0000312","id":"ALW82981.1","source":"EMBL"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [MRNA] (ISOFORM 1)","PROTEIN SEQUENCE OF 5-13 AND 298-308","FUNCTION","CATALYTIC ACTIVITY","PATHWAY","TISSUE SPECIFICITY","BIOPHYSICOCHEMICAL PROPERTIES"]}
```

Source SHA-256: `ee30accdc431e8b63f4d222bad60253967328240f6c83fd47b2627281e1afe10`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3S9Q3.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:41.228210+00:00.  

```json
{"citation":{"authors":["Guo J.","Gao D.","Lian J.","Qu Y."],"citationCrossReferences":[{"database":"PubMed","id":"38212296"},{"database":"DOI","id":"10.1038/s41467-024-44797-z"}],"citationType":"journal article","firstPage":"457","id":"38212296","journal":"Nat. Commun.","lastPage":"457","publicationDate":"2024","title":"De novo biosynthesis of antiarrhythmic alkaloid ajmaline.","volume":"15"},"evidences":[{"evidenceCode":"ECO:0000312","id":"WKU61918.1","source":"EMBL"}],"referenceNumber":2,"referencePositions":["NUCLEOTIDE SEQUENCE [MRNA] (ISOFORM 2)","FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","PATHWAY","TISSUE SPECIFICITY","BIOTECHNOLOGY"]}
```

Source SHA-256: `ee30accdc431e8b63f4d222bad60253967328240f6c83fd47b2627281e1afe10`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3S9Q3.json)  
**Locator:** `/references/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:41.228210+00:00.  

```json
{"citation":{"authors":["Gao S.","von Schumann G.","Stoeckigt J."],"citationCrossReferences":[{"database":"PubMed","id":"12391554"},{"database":"DOI","id":"10.1055/s-2002-34935"}],"citationType":"journal article","firstPage":"906","id":"12391554","journal":"Planta Med.","lastPage":"911","publicationDate":"2002","title":"A newly-detected reductase from Rauvolfia closes a gap in the biosynthesis of the antiarrhythmic alkaloid ajmaline.","volume":"68"},"referenceNumber":3,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","PATHWAY"]}
```

Source SHA-256: `ee30accdc431e8b63f4d222bad60253967328240f6c83fd47b2627281e1afe10`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0U3S9Q3?format=txt&versions=32)  
**Locator:** `lines 72-75`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 32 / 1.  
**Retrieved:** 2026-11-01T06:27:20.990872+00:00.  

```text
CC   -!- COFACTOR:
CC       Name=Zn(2+); Xref=ChEBI:CHEBI:29105;
CC         Evidence={ECO:0000250|UniProtKB:P06525};
CC       Note=Binds 2 Zn(2+) ions per subunit. {ECO:0000250|UniProtKB:P06525};
```

Source SHA-256: `d736edca11739beb62ca2d5765f93a0db6fdd42ef122f9711acacccadcaabc22`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 10. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
