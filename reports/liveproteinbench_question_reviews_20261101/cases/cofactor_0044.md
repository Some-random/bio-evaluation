# cofactor_0044

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `cofactor`  
**Author expected answer:** **A** — FMN

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MDNSSRLFSPLRLGKCQLRHRVAMSPLTRFRADDLSVQMPFAKEYYAQRASVPGTFLVSEATSISRESVGFSNVPGIWNAEQVRAWKEIADDVHCKGSFLFLQLWATGRSATPERLQSGDFDFASSSAVPMEPGGAVPRELTEEDIHDLIARFAEAARRAIDAGMDGIELHAANGYLIDQFTQASCNQRTDRWGGSIENRARFAIEVTRSVVAAVGADRVGVKLSPWGKIQGMGTMQDLVPQFQYLVSELRDMGLAYLRLSNSRWIDGVPQEEEDNSIYVHTWGASRPVLLEGGYDPISAQKEADIRFNGYDAVIAFGRFFISNPDLPFRIKAGVDLQKYNRDTFYTPISEKGYIDYPFSTAFLEEHSSKASLKL

[Multiple Choices]
A. FMN
B. Fe cation
C. Na(+)
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

> The exact sequence matches a UniProt entry annotated with FMN as its cofactor. That annotation is explicitly transferred from a homolog (ECO:0000250), so it supports FMN but is not direct experimental evidence for this sequence.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> No supplied context or unambiguous sequence feature establishes the cofactor. Identifying the protein as a flavin-dependent old-yellow enzyme would favor FMN, but that protein-family identification is not provided and cannot be treated as a general inference from the sequence alone.


**Missing item-specific fact**

> The protein's identity or family annotation, or a validated cofactor-binding/experimental characterization establishing FMN.


**Reason**

> The key is supported by a sequence-matched database annotation, but the annotation is reviewer-only; selecting FMN from the input requires protein-specific identification or external cofactor knowledge.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The available sequence alone does not establish an alternative cofactor, while the matched annotation supports FMN.


### Important caveats

- The cited UniProt cofactor annotation is transferred from a homolog rather than direct evidence for this protein.
- The historical sequence match supports applicability, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "No supplied context or unambiguous sequence feature establishes the cofactor. Identifying the protein as a flavin-dependent old-yellow enzyme would favor FMN, but that protein-family identification is not provided and cannot be treated as a general inference from the sequence alone.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's identity or family annotation, or a validated cofactor-binding/experimental characterization establishing FMN.",
    "reason": "The key is supported by a sequence-matched database annotation, but the annotation is reviewer-only; selecting FMN from the input requires protein-specific identification or external cofactor knowledge."
  },
  "case_id": "cofactor_0044",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated with FMN as its cofactor. That annotation is explicitly transferred from a homolog (ECO:0000250), so it supports FMN but is not direct experimental evidence for this sequence."
  },
  "important_caveats": [
    "The cited UniProt cofactor annotation is transferred from a homolog rather than direct evidence for this protein.",
    "The historical sequence match supports applicability, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The available sequence alone does not establish an alternative cofactor, while the matched annotation supports FMN."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0044",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated with FMN as its cofactor. That annotation is explicitly transferred from a homolog (ECO:0000250), so it supports FMN but is not direct experimental evidence for this sequence.",
    "evidence_ids": ["C1", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "No supplied context or unambiguous sequence feature establishes the cofactor. Identifying the protein as a flavin-dependent old-yellow enzyme would favor FMN, but that protein-family identification is not provided and cannot be treated as a general inference from the sequence alone.",
    "missing_item_specific_fact": "The protein's identity or family annotation, or a validated cofactor-binding/experimental characterization establishing FMN.",
    "reason": "The key is supported by a sequence-matched database annotation, but the annotation is reviewer-only; selecting FMN from the input requires protein-specific identification or external cofactor knowledge."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The available sequence alone does not establish an alternative cofactor, while the matched annotation supports FMN."
  },
  "important_caveats": [
    "The cited UniProt cofactor annotation is transferred from a homolog rather than direct evidence for this protein.",
    "The historical sequence match supports applicability, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A7T8F1M9 explicitly annotates FMN (ChEBI:CHEBI:58210) as the cofactor (evidence C5, H4). The protein is named 'Flavin-dependent old-yellow enzyme FrzD' (OYE family), EC 1.3.1.-, and the associated experimental paper (PubMed 33372776) characterizes its catalytic activity. The cofactor evidence code is ECO:0000250 (similarity to Q4WZ70), so the FMN assignment is inferred by family homology rather than a direct binding assay on FrzD itself. However, the OYE family is universally FMN-dependent, and the protein name and family classification are experimentally grounded (ECO:0000269 for EC number, ECO:0000303 for name). The answer FMN is well-supported.

Citations as saved: [C5](#evidence-c5), [C4](#evidence-c4), [H4](#evidence-h4), [H2](#evidence-h2), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence (~375 aa) exhibits hallmarks of the Old Yellow Enzyme (OYE) family: a TIM-barrel oxidoreductase fold with a conserved 'GAD' motif followed by a GxGxxG-type flavin-binding loop (GADRVGVKLSPWGKIQGMGTMQDLVPQFQYLVSELRDMGLAYLRLSNSRWIDG), the classic WGASRPVLLEGGYDP active-site region, and overall architecture consistent with FMN-dependent enoate reductases. The OYE family is a textbook example of FMN-dependent oxidoreductases. The distractors can be eliminated: no CxxCPxxC or CxxC motifs indicative of &#91;4Fe-4S&#93; clusters; no iron-binding His/Asp/Glu triads for a mononuclear Fe center; no sodium-binding DxDxDG or analogous motifs. Recognizing the OYE fold and knowing that OYEs specifically bind FMN (not FAD) is standard biochemistry knowledge.


**Missing item-specific fact**

> None strictly required. The OYE family is among the most extensively characterized flavoprotein families, and its FMN dependence is general textbook knowledge. The sequence-level OYE motifs (TIM barrel, GAD, flavin-binding loop) provide concrete grounds for family assignment.


**Reason**

> A knowledgeable biochemist can identify the OYE fold from conserved sequence motifs and length, then apply general knowledge that OYEs are FMN-dependent. The distractors lack structural motifs for their respective cofactors. This is family-level recognition using general enzymology, not memorization of a single protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices are mechanistically distinct cofactor classes. The sequence lacks motifs for Fe, Na+, or &#91;4Fe-4S&#93; clusters, and positively displays OYE flavin-binding architecture. FMN is the only defensible answer.


### Important caveats

- The UniProt FMN cofactor annotation uses evidence code ECO:0000250 (similarity), meaning it is inferred from homology to Q4WZ70 rather than a direct FMN-binding assay on FrzD. This is standard for well-characterized enzyme families and does not undermine the answer.
- The protein was first publicly released in UniProt in June 2025; the original dataset construction date is unknown. If the benchmark was constructed before this release, the author may have relied on the primary paper (PubMed 33372776, 2021) or family assignment.
- Distinguishing FMN from FAD at the sequence level relies on recognizing the specific OYE flavin-binding motif; without OYE family knowledge, a generic flavoprotein could use either FMN or FAD. However, the OYE family is sufficiently well-characterized that this is general biochemistry, not item-specific lookup.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence (~375 aa) exhibits hallmarks of the Old Yellow Enzyme (OYE) family: a TIM-barrel oxidoreductase fold with a conserved 'GAD' motif followed by a GxGxxG-type flavin-binding loop (GADRVGVKLSPWGKIQGMGTMQDLVPQFQYLVSELRDMGLAYLRLSNSRWIDG), the classic WGASRPVLLEGGYDP active-site region, and overall architecture consistent with FMN-dependent enoate reductases. The OYE family is a textbook example of FMN-dependent oxidoreductases. The distractors can be eliminated: no CxxCPxxC or CxxC motifs indicative of [4Fe-4S] clusters; no iron-binding His/Asp/Glu triads for a mononuclear Fe center; no sodium-binding DxDxDG or analogous motifs. Recognizing the OYE fold and knowing that OYEs specifically bind FMN (not FAD) is standard biochemistry knowledge.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required. The OYE family is among the most extensively characterized flavoprotein families, and its FMN dependence is general textbook knowledge. The sequence-level OYE motifs (TIM barrel, GAD, flavin-binding loop) provide concrete grounds for family assignment.",
    "reason": "A knowledgeable biochemist can identify the OYE fold from conserved sequence motifs and length, then apply general knowledge that OYEs are FMN-dependent. The distractors lack structural motifs for their respective cofactors. This is family-level recognition using general enzymology, not memorization of a single protein's database entry."
  },
  "case_id": "cofactor_0044",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C4",
      "H4",
      "H2",
      "C6"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A7T8F1M9 explicitly annotates FMN (ChEBI:CHEBI:58210) as the cofactor (evidence C5, H4). The protein is named 'Flavin-dependent old-yellow enzyme FrzD' (OYE family), EC 1.3.1.-, and the associated experimental paper (PubMed 33372776) characterizes its catalytic activity. The cofactor evidence code is ECO:0000250 (similarity to Q4WZ70), so the FMN assignment is inferred by family homology rather than a direct binding assay on FrzD itself. However, the OYE family is universally FMN-dependent, and the protein name and family classification are experimentally grounded (ECO:0000269 for EC number, ECO:0000303 for name). The answer FMN is well-supported."
  },
  "important_caveats": [
    "The UniProt FMN cofactor annotation uses evidence code ECO:0000250 (similarity), meaning it is inferred from homology to Q4WZ70 rather than a direct FMN-binding assay on FrzD. This is standard for well-characterized enzyme families and does not undermine the answer.",
    "The protein was first publicly released in UniProt in June 2025; the original dataset construction date is unknown. If the benchmark was constructed before this release, the author may have relied on the primary paper (PubMed 33372776, 2021) or family assignment.",
    "Distinguishing FMN from FAD at the sequence level relies on recognizing the specific OYE flavin-binding motif; without OYE family knowledge, a generic flavoprotein could use either FMN or FAD. However, the OYE family is sufficiently well-characterized that this is general biochemistry, not item-specific lookup."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices are mechanistically distinct cofactor classes. The sequence lacks motifs for Fe, Na+, or [4Fe-4S] clusters, and positively displays OYE flavin-binding architecture. FMN is the only defensible answer."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0044",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A7T8F1M9 explicitly annotates FMN (ChEBI:CHEBI:58210) as the cofactor (evidence C5, H4). The protein is named 'Flavin-dependent old-yellow enzyme FrzD' (OYE family), EC 1.3.1.-, and the associated experimental paper (PubMed 33372776) characterizes its catalytic activity. The cofactor evidence code is ECO:0000250 (similarity to Q4WZ70), so the FMN assignment is inferred by family homology rather than a direct binding assay on FrzD itself. However, the OYE family is universally FMN-dependent, and the protein name and family classification are experimentally grounded (ECO:0000269 for EC number, ECO:0000303 for name). The answer FMN is well-supported.",
    "evidence_ids": ["C5", "C4", "H4", "H2", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence (~375 aa) exhibits hallmarks of the Old Yellow Enzyme (OYE) family: a TIM-barrel oxidoreductase fold with a conserved 'GAD' motif followed by a GxGxxG-type flavin-binding loop (GADRVGVKLSPWGKIQGMGTMQDLVPQFQYLVSELRDMGLAYLRLSNSRWIDG), the classic WGASRPVLLEGGYDP active-site region, and overall architecture consistent with FMN-dependent enoate reductases. The OYE family is a textbook example of FMN-dependent oxidoreductases. The distractors can be eliminated: no CxxCPxxC or CxxC motifs indicative of [4Fe-4S] clusters; no iron-binding His/Asp/Glu triads for a mononuclear Fe center; no sodium-binding DxDxDG or analogous motifs. Recognizing the OYE fold and knowing that OYEs specifically bind FMN (not FAD) is standard biochemistry knowledge.",
    "missing_item_specific_fact": "None strictly required. The OYE family is among the most extensively characterized flavoprotein families, and its FMN dependence is general textbook knowledge. The sequence-level OYE motifs (TIM barrel, GAD, flavin-binding loop) provide concrete grounds for family assignment.",
    "reason": "A knowledgeable biochemist can identify the OYE fold from conserved sequence motifs and length, then apply general knowledge that OYEs are FMN-dependent. The distractors lack structural motifs for their respective cofactors. This is family-level recognition using general enzymology, not memorization of a single protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices are mechanistically distinct cofactor classes. The sequence lacks motifs for Fe, Na+, or [4Fe-4S] clusters, and positively displays OYE flavin-binding architecture. FMN is the only defensible answer."
  },
  "important_caveats": [
    "The UniProt FMN cofactor annotation uses evidence code ECO:0000250 (similarity), meaning it is inferred from homology to Q4WZ70 rather than a direct FMN-binding assay on FrzD. This is standard for well-characterized enzyme families and does not undermine the answer.",
    "The protein was first publicly released in UniProt in June 2025; the original dataset construction date is unknown. If the benchmark was constructed before this release, the author may have relied on the primary paper (PubMed 33372776, 2021) or family assignment.",
    "Distinguishing FMN from FAD at the sequence level relies on recognizing the specific OYE flavin-binding motif; without OYE family knowledge, a generic flavoprotein could use either FMN or FAD. However, the OYE family is sufficiently well-characterized that this is general biochemistry, not item-specific lookup."
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

**Accession:** `A0A7T8F1M9` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 11. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1M9.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:51.159757+00:00.  

```json
"A0A7T8F1M9"
```

Source SHA-256: `c38628844912ac2c4aa489f4067b5327e7aad3e6384ffb308551b50b6f0b30ee`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1M9.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:51.159757+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33372776","source":"PubMed"}],"value":"FR901483 biosynthesis cluster protein D"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33372776","source":"PubMed"}],"value":"Flavin-dependent old-yellow enzyme FrzD"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"33372776","source":"PubMed"}],"value":"Flavin-dependent OYE"}]}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"33372776","source":"PubMed"}],"value":"1.3.1.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33372776","source":"PubMed"}],"value":"Aldehyde reductase FrzD"}}}
```

Source SHA-256: `c38628844912ac2c4aa489f4067b5327e7aad3e6384ffb308551b50b6f0b30ee`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1M9.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:51.159757+00:00.  

```json
{"cofactors":[{"cofactorCrossReference":{"database":"ChEBI","id":"CHEBI:58210"},"evidences":[{"evidenceCode":"ECO:0000250","id":"Q4WZ70","source":"UniProtKB"}],"name":"FMN"}],"commentType":"COFACTOR"}
```

Source SHA-256: `c38628844912ac2c4aa489f4067b5327e7aad3e6384ffb308551b50b6f0b30ee`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1M9.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:51.159757+00:00.  

```json
{"citation":{"authors":["Zhang Z.","Tamura Y.","Tang M.","Qiao T.","Sato M.","Otsu Y.","Sasamura S.","Taniguchi M.","Watanabe K.","Tang Y."],"citationCrossReferences":[{"database":"PubMed","id":"33372776"},{"database":"DOI","id":"10.1021/jacs.0c12352"}],"citationType":"journal article","firstPage":"132","id":"33372776","journal":"J. Am. Chem. Soc.","lastPage":"136","publicationDate":"2021","title":"Biosynthesis of the Immunosuppressant (-)-FR901483.","volume":"143"},"referenceComments":[{"type":"STRAIN","value":"11231"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [GENOMIC DNA]","FUNCTION","CATALYTIC ACTIVITY","PATHWAY"]}
```

Source SHA-256: `c38628844912ac2c4aa489f4067b5327e7aad3e6384ffb308551b50b6f0b30ee`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8F1M9?format=txt&versions=11)  
**Locator:** `lines 6-10`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 11 / 1.  
**Retrieved:** 2026-11-01T06:27:35.126419+00:00.  

```text
DE   RecName: Full=Aldehyde reductase FrzD {ECO:0000303|PubMed:33372776};
DE            EC=1.3.1.- {ECO:0000269|PubMed:33372776};
DE   AltName: Full=FR901483 biosynthesis cluster protein D {ECO:0000303|PubMed:33372776};
DE   AltName: Full=Flavin-dependent old-yellow enzyme FrzD {ECO:0000303|PubMed:33372776};
DE            Short=Flavin-dependent OYE {ECO:0000303|PubMed:33372776};
```

Source SHA-256: `fd48d108f45a92963462c2f0a750dcecfac5cc36c43941b4ca5d31b971333839`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8F1M9?format=txt&versions=11)  
**Locator:** `lines 66-68`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 11 / 1.  
**Retrieved:** 2026-11-01T06:27:35.126419+00:00.  

```text
CC   -!- COFACTOR:
CC       Name=FMN; Xref=ChEBI:CHEBI:58210;
CC         Evidence={ECO:0000250|UniProtKB:Q4WZ70};
```

Source SHA-256: `fd48d108f45a92963462c2f0a750dcecfac5cc36c43941b4ca5d31b971333839`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 44. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
