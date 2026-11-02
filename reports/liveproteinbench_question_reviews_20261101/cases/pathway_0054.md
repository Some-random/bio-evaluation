# pathway_0054

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `pathway`  
**Author expected answer:** **C** — Alkaloid biosynthesis. .

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MEAIAQEIQKLHANTDEAGRGKINHDLSVLLASFDTDWEKILKLAAGPLRLALVKVGVDQGIFHALNERSHTLPELIEKTGVAPYLLERILRGQASFGMIKEEGAKGFAANRFTTLLAGPNTSGAVTYIFDILRPIASAIPGFLSERNNPAITSTHDTVFQRAFNTELGGFEWMTGHPEHYGNLFQFLALRPNCEWVDAFPIEAEIGSFTNDPHVEKVLLVDVGGGTGAQSVAFRKKLPHVKGRVIVQEIAETLIHVGAKAPAGIEFMEYDCFTPQPIRGAKFYYLRYVMHLWQDERCVEALKVIITAMGPESRLIIDEAVIPDRDVPWQAACQSILMTAALAGAERTLTEWHNLLDAAGLKILNIFPYDLNMQSVIIAVPK

[Multiple Choices]
A. chorismate from D-erythrose 4-phosphate and phosphoenolpyruvate: step 7/7. .
B. Cell wall biogenesis
C. Alkaloid biosynthesis. .
D. L-homoserine from L-aspartate: step 2/3. .
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Protein Pathway Prediction, which is to predict the primary metabolic or signaling pathway in which a given protein functions. Biological pathways are series of chemical reactions occurring within a cell that are essential for life. Based on the protein's amino acid sequence, you should identify the most relevant pathway from the given options.. The inputs provided by the user for this task include:

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

> The sequence-matched UniProt record identifies this protein as O-methyltransferase OkaF and annotates its pathway as alkaloid biosynthesis. The pathway annotation cites experimental evidence, although the cited papers were not independently reviewed here.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may suggest an enzyme, but the input supplies no organism, pathway-cluster context, substrate, or experimental role that establishes which pathway this particular protein serves.


**Missing item-specific fact**

> That this protein is OkaF, an O-methyltransferase associated with okaramine alkaloid biosynthesis.


**Reason**

> Assigning the specific pathway requires a protein-specific functional annotation or equivalent experimental/contextual information absent from the question. Recognizing the sequence or recalling its database entry would be lookup or memorization, not reasoning from the supplied input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The choices name distinct pathways or processes; the supplied evidence supports C, and no competing option is supported by the sequence-specific annotation.


### Important caveats

- The reviewer-only evidence matches the supplied 382-residue sequence, but the author's exact data-source snapshot is unknown.
- The pathway annotation cites experimental evidence, but the cited primary studies were not independently validated in this review.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence may suggest an enzyme, but the input supplies no organism, pathway-cluster context, substrate, or experimental role that establishes which pathway this particular protein serves.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "That this protein is OkaF, an O-methyltransferase associated with okaramine alkaloid biosynthesis.",
    "reason": "Assigning the specific pathway requires a protein-specific functional annotation or equivalent experimental/contextual information absent from the question. Recognizing the sequence or recalling its database entry would be lookup or memorization, not reasoning from the supplied input."
  },
  "case_id": "pathway_0054",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record identifies this protein as O-methyltransferase OkaF and annotates its pathway as alkaloid biosynthesis. The pathway annotation cites experimental evidence, although the cited papers were not independently reviewed here."
  },
  "important_caveats": [
    "The reviewer-only evidence matches the supplied 382-residue sequence, but the author's exact data-source snapshot is unknown.",
    "The pathway annotation cites experimental evidence, but the cited primary studies were not independently validated in this review."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices name distinct pathways or processes; the supplied evidence supports C, and no competing option is supported by the sequence-specific annotation."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0054",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record identifies this protein as O-methyltransferase OkaF and annotates its pathway as alkaloid biosynthesis. The pathway annotation cites experimental evidence, although the cited papers were not independently reviewed here.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may suggest an enzyme, but the input supplies no organism, pathway-cluster context, substrate, or experimental role that establishes which pathway this particular protein serves.",
    "missing_item_specific_fact": "That this protein is OkaF, an O-methyltransferase associated with okaramine alkaloid biosynthesis.",
    "reason": "Assigning the specific pathway requires a protein-specific functional annotation or equivalent experimental/contextual information absent from the question. Recognizing the sequence or recalling its database entry would be lookup or memorization, not reasoning from the supplied input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices name distinct pathways or processes; the supplied evidence supports C, and no competing option is supported by the sequence-specific annotation."
  },
  "important_caveats": [
    "The reviewer-only evidence matches the supplied 382-residue sequence, but the author's exact data-source snapshot is unknown.",
    "The pathway annotation cites experimental evidence, but the cited primary studies were not independently validated in this review."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A2Z5UFJ1 (OKAF_PENOH) annotates this 382-aa protein as 'O-methyltransferase okaF' / 'Okaramines biosynthesis cluster protein F' with pathway 'Alkaloid biosynthesis' supported by direct experimental evidence (ECO:0000269, PubMed:28631282 and PubMed:29384650). The sequence matches exactly (SHA256 confirmed). Okaramines are indole alkaloids, so the pathway assignment to alkaloid biosynthesis is experimentally validated.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the canonical SAM-dependent methyltransferase motif 'DVGGGTG' (in 'LLVDVGGGTGAQSVAFRKK') and the class I methyltransferase catalytic region 'IIDEAVIPDRDVPWQAACQSILMTAAL', identifying this as an O-methyltransferase. This immediately eliminates Choice A (chorismate synthase, a flavin-dependent enzyme with entirely different catalytic machinery) and Choice D (homoserine dehydrogenase, an NAD(P)-dependent dehydrogenase). Between B (cell wall biogenesis) and C (alkaloid biosynthesis): cell wall biogenesis is primarily driven by glycosyltransferases, cellulose synthases, and polysaccharide-modifying enzymes, not O-methyltransferases. In contrast, O-methyltransferases are well-known tailoring enzymes in alkaloid biosynthetic pathways (e.g., methylation of indole, isoquinoline, and other alkaloid intermediates). Thus the methyltransferase identification provides a concrete biological argument favoring C over all other options.


**Missing item-specific fact**

> The exact substrate identity (okaramine intermediate) and organism context (Penicillium ochrochloron) are not derivable from sequence alone, but are not strictly needed to distinguish among the four given choices.


**Reason**

> The DVGG/SAM-methyltransferase motif is directly readable from the sequence and eliminates A and D by enzyme-class mismatch. The association of O-methyltransferases with alkaloid tailoring (rather than cell wall assembly) is general biochemical knowledge that meaningfully distinguishes C from B. The reasoning is not perfect (methyltransferases exist in many pathways), but among the four provided options, the argument is concrete and defensible.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Choices A and D are eliminable by enzyme-class identification (flavin-dependent vs. dehydrogenase vs. methyltransferase). Choice B is eliminable because cell wall biogenesis does not typically feature O-methyltransferases as pathway-defining enzymes. Choice C is the only option consistent with an O-methyltransferase serving as a biosynthetic tailoring enzyme.


### Important caveats

- The reviewer-only UniProt annotation confirms the key with experimental evidence (ECO:0000269), but this annotation was not available to the evaluated model.
- The reasoning argument (methyltransferase → alkaloid biosynthesis) is probabilistic rather than deductive; O-methyltransferases also participate in flavonoid, lignin, and other secondary-metabolite pathways not offered as distractors here.
- The specific identification as okaF (okaramine biosynthesis) requires knowledge of the Penicillium ochrochloron gene cluster, but the question's answer choice 'Alkaloid biosynthesis' is broad enough that general methyltransferase-in-secondary-metabolism reasoning suffices to select C among the given options.
- Sequence identity confirmed: benchmark sequence (382 aa) matches UniProt A0A2Z5UFJ1 sequence version 1 exactly.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the canonical SAM-dependent methyltransferase motif 'DVGGGTG' (in 'LLVDVGGGTGAQSVAFRKK') and the class I methyltransferase catalytic region 'IIDEAVIPDRDVPWQAACQSILMTAAL', identifying this as an O-methyltransferase. This immediately eliminates Choice A (chorismate synthase, a flavin-dependent enzyme with entirely different catalytic machinery) and Choice D (homoserine dehydrogenase, an NAD(P)-dependent dehydrogenase). Between B (cell wall biogenesis) and C (alkaloid biosynthesis): cell wall biogenesis is primarily driven by glycosyltransferases, cellulose synthases, and polysaccharide-modifying enzymes, not O-methyltransferases. In contrast, O-methyltransferases are well-known tailoring enzymes in alkaloid biosynthetic pathways (e.g., methylation of indole, isoquinoline, and other alkaloid intermediates). Thus the methyltransferase identification provides a concrete biological argument favoring C over all other options.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The exact substrate identity (okaramine intermediate) and organism context (Penicillium ochrochloron) are not derivable from sequence alone, but are not strictly needed to distinguish among the four given choices.",
    "reason": "The DVGG/SAM-methyltransferase motif is directly readable from the sequence and eliminates A and D by enzyme-class mismatch. The association of O-methyltransferases with alkaloid tailoring (rather than cell wall assembly) is general biochemical knowledge that meaningfully distinguishes C from B. The reasoning is not perfect (methyltransferases exist in many pathways), but among the four provided options, the argument is concrete and defensible."
  },
  "case_id": "pathway_0054",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A2Z5UFJ1 (OKAF_PENOH) annotates this 382-aa protein as 'O-methyltransferase okaF' / 'Okaramines biosynthesis cluster protein F' with pathway 'Alkaloid biosynthesis' supported by direct experimental evidence (ECO:0000269, PubMed:28631282 and PubMed:29384650). The sequence matches exactly (SHA256 confirmed). Okaramines are indole alkaloids, so the pathway assignment to alkaloid biosynthesis is experimentally validated."
  },
  "important_caveats": [
    "The reviewer-only UniProt annotation confirms the key with experimental evidence (ECO:0000269), but this annotation was not available to the evaluated model.",
    "The reasoning argument (methyltransferase → alkaloid biosynthesis) is probabilistic rather than deductive; O-methyltransferases also participate in flavonoid, lignin, and other secondary-metabolite pathways not offered as distractors here.",
    "The specific identification as okaF (okaramine biosynthesis) requires knowledge of the Penicillium ochrochloron gene cluster, but the question's answer choice 'Alkaloid biosynthesis' is broad enough that general methyltransferase-in-secondary-metabolism reasoning suffices to select C among the given options.",
    "Sequence identity confirmed: benchmark sequence (382 aa) matches UniProt A0A2Z5UFJ1 sequence version 1 exactly."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choices A and D are eliminable by enzyme-class identification (flavin-dependent vs. dehydrogenase vs. methyltransferase). Choice B is eliminable because cell wall biogenesis does not typically feature O-methyltransferases as pathway-defining enzymes. Choice C is the only option consistent with an O-methyltransferase serving as a biosynthetic tailoring enzyme."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0054",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A2Z5UFJ1 (OKAF_PENOH) annotates this 382-aa protein as 'O-methyltransferase okaF' / 'Okaramines biosynthesis cluster protein F' with pathway 'Alkaloid biosynthesis' supported by direct experimental evidence (ECO:0000269, PubMed:28631282 and PubMed:29384650). The sequence matches exactly (SHA256 confirmed). Okaramines are indole alkaloids, so the pathway assignment to alkaloid biosynthesis is experimentally validated.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the canonical SAM-dependent methyltransferase motif 'DVGGGTG' (in 'LLVDVGGGTGAQSVAFRKK') and the class I methyltransferase catalytic region 'IIDEAVIPDRDVPWQAACQSILMTAAL', identifying this as an O-methyltransferase. This immediately eliminates Choice A (chorismate synthase, a flavin-dependent enzyme with entirely different catalytic machinery) and Choice D (homoserine dehydrogenase, an NAD(P)-dependent dehydrogenase). Between B (cell wall biogenesis) and C (alkaloid biosynthesis): cell wall biogenesis is primarily driven by glycosyltransferases, cellulose synthases, and polysaccharide-modifying enzymes, not O-methyltransferases. In contrast, O-methyltransferases are well-known tailoring enzymes in alkaloid biosynthetic pathways (e.g., methylation of indole, isoquinoline, and other alkaloid intermediates). Thus the methyltransferase identification provides a concrete biological argument favoring C over all other options.",
    "missing_item_specific_fact": "The exact substrate identity (okaramine intermediate) and organism context (Penicillium ochrochloron) are not derivable from sequence alone, but are not strictly needed to distinguish among the four given choices.",
    "reason": "The DVGG/SAM-methyltransferase motif is directly readable from the sequence and eliminates A and D by enzyme-class mismatch. The association of O-methyltransferases with alkaloid tailoring (rather than cell wall assembly) is general biochemical knowledge that meaningfully distinguishes C from B. The reasoning is not perfect (methyltransferases exist in many pathways), but among the four provided options, the argument is concrete and defensible."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choices A and D are eliminable by enzyme-class identification (flavin-dependent vs. dehydrogenase vs. methyltransferase). Choice B is eliminable because cell wall biogenesis does not typically feature O-methyltransferases as pathway-defining enzymes. Choice C is the only option consistent with an O-methyltransferase serving as a biosynthetic tailoring enzyme."
  },
  "important_caveats": [
    "The reviewer-only UniProt annotation confirms the key with experimental evidence (ECO:0000269), but this annotation was not available to the evaluated model.",
    "The reasoning argument (methyltransferase → alkaloid biosynthesis) is probabilistic rather than deductive; O-methyltransferases also participate in flavonoid, lignin, and other secondary-metabolite pathways not offered as distractors here.",
    "The specific identification as okaF (okaramine biosynthesis) requires knowledge of the Penicillium ochrochloron gene cluster, but the question's answer choice 'Alkaloid biosynthesis' is broad enough that general methyltransferase-in-secondary-metabolism reasoning suffices to select C among the given options.",
    "Sequence identity confirmed: benchmark sequence (382 aa) matches UniProt A0A2Z5UFJ1 sequence version 1 exactly."
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

**Accession:** `A0A2Z5UFJ1` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 21. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2Z5UFJ1.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:55.698053+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"28631282","source":"PubMed"}],"value":"Okaramines biosynthesis cluster protein F"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"28631282","source":"PubMed"}],"value":"2.1.1.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"28631282","source":"PubMed"}],"value":"O-methyltransferase okaF"}}}
```

Source SHA-256: `1c40d9c24a5fbe42fadb160394d41d0c1f4f16e074c83ea5d3aad3451b0a1c99`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2Z5UFJ1.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:55.698053+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"28631282","source":"PubMed"},{"evidenceCode":"ECO:0000305","id":"29384650","source":"PubMed"}],"value":"Alkaloid biosynthesis"}]}
```

Source SHA-256: `1c40d9c24a5fbe42fadb160394d41d0c1f4f16e074c83ea5d3aad3451b0a1c99`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2Z5UFJ1.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:55.698053+00:00.  

```json
{"citation":{"authors":["Kato N.","Furutani S.","Otaka J.","Noguchi A.","Kinugasa K.","Kai K.","Hayashi H.","Ihara M.","Takahashi S.","Matsuda K.","Osada H."],"citationCrossReferences":[{"database":"PubMed","id":"29384650"},{"database":"DOI","id":"10.1021/acschembio.7b00878"}],"citationType":"journal article","firstPage":"561","id":"29384650","journal":"ACS Chem. Biol.","lastPage":"566","publicationDate":"2018","title":"Biosynthesis and Structure-Activity Relationship Studies of Okaramines That Target Insect Glutamate-Gated Chloride Channels.","volume":"13"},"referenceComments":[{"type":"STRAIN","value":"ATCC 90288 / AK-40"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [GENOMIC DNA]","FUNCTION","PATHWAY"]}
```

Source SHA-256: `1c40d9c24a5fbe42fadb160394d41d0c1f4f16e074c83ea5d3aad3451b0a1c99`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2Z5UFJ1.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:55.698053+00:00.  

```json
{"citation":{"authors":["Lai C.Y.","Lo I.W.","Hewage R.T.","Chen Y.C.","Chen C.T.","Lee C.F.","Lin S.","Tang M.C.","Lin H.C."],"citationCrossReferences":[{"database":"PubMed","id":"28631282"},{"database":"DOI","id":"10.1002/anie.201705501"}],"citationType":"journal article","firstPage":"9478","id":"28631282","journal":"Angew. Chem. Int. Ed.","lastPage":"9482","publicationDate":"2017","title":"Biosynthesis of Complex Indole Alkaloids: Elucidation of the Concise Pathway of Okaramines.","volume":"56"},"referenceNumber":2,"referencePositions":["FUNCTION","DISRUPTION PHENOTYPE","CATALYTIC ACTIVITY","PATHWAY"]}
```

Source SHA-256: `1c40d9c24a5fbe42fadb160394d41d0c1f4f16e074c83ea5d3aad3451b0a1c99`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2Z5UFJ1?format=txt&versions=21)  
**Locator:** `lines 66-67`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 21 / 1.  
**Retrieved:** 2026-11-02T04:24:57.706737+00:00.  

```text
CC   -!- PATHWAY: Alkaloid biosynthesis. {ECO:0000269|PubMed:28631282,
CC       ECO:0000305|PubMed:29384650}.
```

Source SHA-256: `1a62de7f3d5b2124ffd30a7c9e4b82e694d58188d716a4429114528e9f01ce3f`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 54. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
