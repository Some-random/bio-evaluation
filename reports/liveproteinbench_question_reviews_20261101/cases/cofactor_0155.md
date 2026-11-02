# cofactor_0155

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `cofactor`  
**Author expected answer:** **C** — &#91;4Fe-4S&#93; cluster

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MTVPAARSGRKVYFIGLNAVPFLPLVAGLLRTYAEQDPRVAAGYDFQEPVFLVDGVQEMAAGITDPDVLALSCYVWNFRRQMKVARLVKERHPGMLVVAGGPHVPDRPGDFFARHPYVDVLVHGEGETAFRELLIERLADHPDYTRVPGVSVRHGTEAVPGRPAERLPRRIETPSPYLLGVMDGAVATCRQRDLRFYALWETNRGCPYSCAFCDWGSATMSALRLFDAERLQEEIEWFAEHDVEDLFVCDANFGILPRDLEIARALADARAATGAPKLIRVNFAKNSNDRVFEISKTWHDADLLMGTTLSMQSTDLDVLEAIDRKNIGLENYRKLQQRYATENIHTYTELILGLPLESPRSFRDGIGSLLEAGNHEDIRVYEFGILPNAPINTPEKIAGYGLRTVPKRLYVEEPGTPDDEAETVDMVMETNAMSRDEWVDCFGFVQAVQFLHNGCYTRYLSMYLRQRHDIGYTAFYERLQQYFGARPDTVLGSIYLRMRKLYHDYIDIPELPLANLVASQPDMAADLARYGKRRGWTIDNWGWLRIANDFERTYTELRDFVAALGVDDTSDPDLAEVFRFQQDVMLRPDYDPAAGRTTEYTADWPGYFTTGELRRRPVRMRLADQRFGANGRYTPVPGDLKAFARAAIGPSYPVSRIGHYRHRFEAAEVTSPAEPVLTEQR

[Multiple Choices]
A. Co(2+)
B. FAD
C. [4Fe-4S] cluster
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

> The exact sequence matches the UniProt entry, which annotates a &#91;4Fe-4S&#93; cluster with experimental evidence attributed to a cited publication. The archived entry also records this annotation. The entry lists cob(II)alamin as another cofactor, but that is not equivalent to any other listed choice.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C6](#evidence-c6), [H7](#evidence-h7), [H8](#evidence-h8).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a CxxxCxxC motif (in “CPYSCAF C”, with the intervening sequence forming the motif), characteristic of radical SAM enzymes that bind a &#91;4Fe-4S&#93; cluster. That provides a concrete sequence-based reason to favor C over the offered alternatives.


**Missing item-specific fact**

> The protein’s exact identity and full cofactor set are not supplied; in particular, its separate cob(II)alamin cofactor is not among the choices. Those facts are not needed to distinguish the listed &#91;4Fe-4S&#93; option.


**Reason**

> The recognizable cluster-binding motif meaningfully supports C using the supplied sequence and choices; this is more than recall of a database entry or a generic predictor’s output.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although the protein is also annotated with cob(II)alamin, none of the other choices names that cofactor. Cob(II)alamin is not interchangeable with free Co(2+), just as an iron atom within an iron-sulfur cluster is not the same cofactor as the cluster.


### Important caveats

- The cofactor annotations are database records with evidence attribution to cited publications; the supplied excerpts do not independently establish the experimental details.
- The sequence match establishes applicability to this protein sequence, but the exact author source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a CxxxCxxC motif (in “CPYSCAF C”, with the intervening sequence forming the motif), characteristic of radical SAM enzymes that bind a [4Fe-4S] cluster. That provides a concrete sequence-based reason to favor C over the offered alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The protein’s exact identity and full cofactor set are not supplied; in particular, its separate cob(II)alamin cofactor is not among the choices. Those facts are not needed to distinguish the listed [4Fe-4S] option.",
    "reason": "The recognizable cluster-binding motif meaningfully supports C using the supplied sequence and choices; this is more than recall of a database entry or a generic predictor’s output."
  },
  "case_id": "cofactor_0155",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C6",
      "H7",
      "H8"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry, which annotates a [4Fe-4S] cluster with experimental evidence attributed to a cited publication. The archived entry also records this annotation. The entry lists cob(II)alamin as another cofactor, but that is not equivalent to any other listed choice."
  },
  "important_caveats": [
    "The cofactor annotations are database records with evidence attribution to cited publications; the supplied excerpts do not independently establish the experimental details.",
    "The sequence match establishes applicability to this protein sequence, but the exact author source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the protein is also annotated with cob(II)alamin, none of the other choices names that cofactor. Cob(II)alamin is not interchangeable with free Co(2+), just as an iron atom within an iron-sulfur cluster is not the same cofactor as the cluster."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0155",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry, which annotates a [4Fe-4S] cluster with experimental evidence attributed to a cited publication. The archived entry also records this annotation. The entry lists cob(II)alamin as another cofactor, but that is not equivalent to any other listed choice.",
    "evidence_ids": ["C1", "C5", "C6", "H7", "H8"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a CxxxCxxC motif (in “CPYSCAF C”, with the intervening sequence forming the motif), characteristic of radical SAM enzymes that bind a [4Fe-4S] cluster. That provides a concrete sequence-based reason to favor C over the offered alternatives.",
    "missing_item_specific_fact": "The protein’s exact identity and full cofactor set are not supplied; in particular, its separate cob(II)alamin cofactor is not among the choices. Those facts are not needed to distinguish the listed [4Fe-4S] option.",
    "reason": "The recognizable cluster-binding motif meaningfully supports C using the supplied sequence and choices; this is more than recall of a database entry or a generic predictor’s output."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the protein is also annotated with cob(II)alamin, none of the other choices names that cofactor. Cob(II)alamin is not interchangeable with free Co(2+), just as an iron atom within an iron-sulfur cluster is not the same cofactor as the cluster."
  },
  "important_caveats": [
    "The cofactor annotations are database records with evidence attribution to cited publications; the supplied excerpts do not independently establish the experimental details.",
    "The sequence match establishes applicability to this protein sequence, but the exact author source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q83XP3 (ThnK) explicitly annotates a &#91;4Fe-4S&#93; cluster as a cofactor with experimental evidence (ECO:0000269, PubMed:26240322). The note specifies 'Binds 1 &#91;4Fe-4S&#93; cluster. The cluster is coordinated with 3 cysteines and an exchangeable S-adenosyl-L-methionine.' The protein is a radical SAM enzyme (EC 2.1.1.394), for which the &#91;4Fe-4S&#93; cluster is the defining catalytic cofactor. A second cofactor, cob(II)alamin, is also annotated (ECO:0000305), but this does not contradict the &#91;4Fe-4S&#93; assignment. Among the given choices, Co(2+) (free cobalt ion) is not equivalent to cob(II)alamin (a cobalt-containing corrin complex), so no listed alternative correctly captures the second cofactor.

Citations as saved: [C5](#evidence-c5), [C7](#evidence-c7), [C4](#evidence-c4), [H7](#evidence-h7), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the canonical radical SAM CX3CX2C motif (C-P-Y-S-C-A-F-C-D-W, i.e., Cys-X3-Cys-X2-Cys) within the region '…GCPYSCAFCDWGSATMSAL…'. This motif is the diagnostic signature of radical S-adenosylmethionine (SAM) enzymes, which are defined by their requirement for a &#91;4Fe-4S&#93; cluster coordinated by the three cysteines of this motif plus an exchangeable SAM ligand. Recognizing this motif and applying the general biochemical principle that radical SAM enzymes require a &#91;4Fe-4S&#93; cluster (not free Fe²⁺, not FAD, not free Co²⁺) allows a knowledgeable model to select C without memorizing this specific protein's annotation. The distinction between a &#91;4Fe-4S&#93; cluster and free Fe(2+) (choice D) is a standard biochemistry point: the motif coordinates an iron-sulfur cluster, not a mononuclear iron ion.


**Missing item-specific fact**

> None strictly required. The CX3CX2C motif is present in the supplied sequence and its connection to &#91;4Fe-4S&#93; clusters is textbook biochemistry. The second cofactor (cob(II)alamin) is not among the choices in a form that would create ambiguity (Co(2+) ≠ cob(II)alamin).


**Reason**

> A model with general knowledge of radical SAM enzyme biochemistry can scan the 681-residue sequence, identify the CX3CX2C motif, and infer &#91;4Fe-4S&#93; as the required cofactor. This is a concrete, sequence-grounded biological argument rather than pure lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The protein does bind cob(II)alamin as a second cofactor, but choice A lists 'Co(2+)' (free cobalt ion), which is biochemically distinct from cob(II)alamin (Co(II) within a corrin ring). No other choice (FAD, Fe(2+)) matches the protein's cofactor profile. The &#91;4Fe-4S&#93; cluster is the only correct answer among the four options.


### Important caveats

- The protein has two annotated cofactors: &#91;4Fe-4S&#93; cluster (experimental, ECO:0000269) and cob(II)alamin (inferred by similarity, ECO:0000305). The question's singular phrasing ('the specific cofactor') could be seen as slightly imprecise, but among the given choices only &#91;4Fe-4S&#93; is valid.
- The cob(II)alamin annotation carries ECO:0000305 (inferred from similar proteins), a weaker evidence level than the experimental ECO:0000269 supporting the &#91;4Fe-4S&#93; cluster.
- Identifying the CX3CX2C motif in a 681-residue sequence requires careful scanning; the motif is not trivially obvious at a glance, though it is present and identifiable.
- Choice A (Co(2+)) could tempt a model that conflates the cobalt in cob(II)alamin with free Co(2+), but these are biochemically distinct entities.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the canonical radical SAM CX3CX2C motif (C-P-Y-S-C-A-F-C-D-W, i.e., Cys-X3-Cys-X2-Cys) within the region '…GCPYSCAFCDWGSATMSAL…'. This motif is the diagnostic signature of radical S-adenosylmethionine (SAM) enzymes, which are defined by their requirement for a [4Fe-4S] cluster coordinated by the three cysteines of this motif plus an exchangeable SAM ligand. Recognizing this motif and applying the general biochemical principle that radical SAM enzymes require a [4Fe-4S] cluster (not free Fe²⁺, not FAD, not free Co²⁺) allows a knowledgeable model to select C without memorizing this specific protein's annotation. The distinction between a [4Fe-4S] cluster and free Fe(2+) (choice D) is a standard biochemistry point: the motif coordinates an iron-sulfur cluster, not a mononuclear iron ion.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required. The CX3CX2C motif is present in the supplied sequence and its connection to [4Fe-4S] clusters is textbook biochemistry. The second cofactor (cob(II)alamin) is not among the choices in a form that would create ambiguity (Co(2+) ≠ cob(II)alamin).",
    "reason": "A model with general knowledge of radical SAM enzyme biochemistry can scan the 681-residue sequence, identify the CX3CX2C motif, and infer [4Fe-4S] as the required cofactor. This is a concrete, sequence-grounded biological argument rather than pure lookup."
  },
  "case_id": "cofactor_0155",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C7",
      "C4",
      "H7",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q83XP3 (ThnK) explicitly annotates a [4Fe-4S] cluster as a cofactor with experimental evidence (ECO:0000269, PubMed:26240322). The note specifies 'Binds 1 [4Fe-4S] cluster. The cluster is coordinated with 3 cysteines and an exchangeable S-adenosyl-L-methionine.' The protein is a radical SAM enzyme (EC 2.1.1.394), for which the [4Fe-4S] cluster is the defining catalytic cofactor. A second cofactor, cob(II)alamin, is also annotated (ECO:0000305), but this does not contradict the [4Fe-4S] assignment. Among the given choices, Co(2+) (free cobalt ion) is not equivalent to cob(II)alamin (a cobalt-containing corrin complex), so no listed alternative correctly captures the second cofactor."
  },
  "important_caveats": [
    "The protein has two annotated cofactors: [4Fe-4S] cluster (experimental, ECO:0000269) and cob(II)alamin (inferred by similarity, ECO:0000305). The question's singular phrasing ('the specific cofactor') could be seen as slightly imprecise, but among the given choices only [4Fe-4S] is valid.",
    "The cob(II)alamin annotation carries ECO:0000305 (inferred from similar proteins), a weaker evidence level than the experimental ECO:0000269 supporting the [4Fe-4S] cluster.",
    "Identifying the CX3CX2C motif in a 681-residue sequence requires careful scanning; the motif is not trivially obvious at a glance, though it is present and identifiable.",
    "Choice A (Co(2+)) could tempt a model that conflates the cobalt in cob(II)alamin with free Co(2+), but these are biochemically distinct entities."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein does bind cob(II)alamin as a second cofactor, but choice A lists 'Co(2+)' (free cobalt ion), which is biochemically distinct from cob(II)alamin (Co(II) within a corrin ring). No other choice (FAD, Fe(2+)) matches the protein's cofactor profile. The [4Fe-4S] cluster is the only correct answer among the four options."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0155",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q83XP3 (ThnK) explicitly annotates a [4Fe-4S] cluster as a cofactor with experimental evidence (ECO:0000269, PubMed:26240322). The note specifies 'Binds 1 [4Fe-4S] cluster. The cluster is coordinated with 3 cysteines and an exchangeable S-adenosyl-L-methionine.' The protein is a radical SAM enzyme (EC 2.1.1.394), for which the [4Fe-4S] cluster is the defining catalytic cofactor. A second cofactor, cob(II)alamin, is also annotated (ECO:0000305), but this does not contradict the [4Fe-4S] assignment. Among the given choices, Co(2+) (free cobalt ion) is not equivalent to cob(II)alamin (a cobalt-containing corrin complex), so no listed alternative correctly captures the second cofactor.",
    "evidence_ids": ["C5", "C7", "C4", "H7", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the canonical radical SAM CX3CX2C motif (C-P-Y-S-C-A-F-C-D-W, i.e., Cys-X3-Cys-X2-Cys) within the region '…GCPYSCAFCDWGSATMSAL…'. This motif is the diagnostic signature of radical S-adenosylmethionine (SAM) enzymes, which are defined by their requirement for a [4Fe-4S] cluster coordinated by the three cysteines of this motif plus an exchangeable SAM ligand. Recognizing this motif and applying the general biochemical principle that radical SAM enzymes require a [4Fe-4S] cluster (not free Fe²⁺, not FAD, not free Co²⁺) allows a knowledgeable model to select C without memorizing this specific protein's annotation. The distinction between a [4Fe-4S] cluster and free Fe(2+) (choice D) is a standard biochemistry point: the motif coordinates an iron-sulfur cluster, not a mononuclear iron ion.",
    "missing_item_specific_fact": "None strictly required. The CX3CX2C motif is present in the supplied sequence and its connection to [4Fe-4S] clusters is textbook biochemistry. The second cofactor (cob(II)alamin) is not among the choices in a form that would create ambiguity (Co(2+) ≠ cob(II)alamin).",
    "reason": "A model with general knowledge of radical SAM enzyme biochemistry can scan the 681-residue sequence, identify the CX3CX2C motif, and infer [4Fe-4S] as the required cofactor. This is a concrete, sequence-grounded biological argument rather than pure lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein does bind cob(II)alamin as a second cofactor, but choice A lists 'Co(2+)' (free cobalt ion), which is biochemically distinct from cob(II)alamin (Co(II) within a corrin ring). No other choice (FAD, Fe(2+)) matches the protein's cofactor profile. The [4Fe-4S] cluster is the only correct answer among the four options."
  },
  "important_caveats": [
    "The protein has two annotated cofactors: [4Fe-4S] cluster (experimental, ECO:0000269) and cob(II)alamin (inferred by similarity, ECO:0000305). The question's singular phrasing ('the specific cofactor') could be seen as slightly imprecise, but among the given choices only [4Fe-4S] is valid.",
    "The cob(II)alamin annotation carries ECO:0000305 (inferred from similar proteins), a weaker evidence level than the experimental ECO:0000269 supporting the [4Fe-4S] cluster.",
    "Identifying the CX3CX2C motif in a 681-residue sequence requires careful scanning; the motif is not trivially obvious at a glance, though it is present and identifiable.",
    "Choice A (Co(2+)) could tempt a model that conflates the cobalt in cob(II)alamin with free Co(2+), but these are biochemically distinct entities."
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

**Accession:** `Q83XP3` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 74. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q83XP3.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:53.086451+00:00.  

```json
"Q83XP3"
```

Source SHA-256: `7c691f44889f41a52c576e4cd1ae8e11c3cf7188b087ddf90064e3b8af6124a1`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q83XP3.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:53.086451+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"26240322","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"31774078","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"36042702","source":"PubMed"}],"value":"2.1.1.394"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"2-(S-pantetheinyl)-carbapenam-3-carboxylate methyltransferase"}}}
```

Source SHA-256: `7c691f44889f41a52c576e4cd1ae8e11c3cf7188b087ddf90064e3b8af6124a1`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q83XP3.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:53.086451+00:00.  

```json
{"cofactors":[{"cofactorCrossReference":{"database":"ChEBI","id":"CHEBI:49883"},"evidences":[{"evidenceCode":"ECO:0000269","id":"26240322","source":"PubMed"}],"name":"[4Fe-4S] cluster"}],"commentType":"COFACTOR","note":{"texts":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"A0A6B9HEI0","source":"UniProtKB"}],"value":"Binds 1 [4Fe-4S] cluster. The cluster is coordinated with 3 cysteines and an exchangeable S-adenosyl-L-methionine."}]}}
```

Source SHA-256: `7c691f44889f41a52c576e4cd1ae8e11c3cf7188b087ddf90064e3b8af6124a1`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q83XP3.json)  
**Locator:** `/comments/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:53.086451+00:00.  

```json
{"cofactors":[{"cofactorCrossReference":{"database":"ChEBI","id":"CHEBI:16304"},"evidences":[{"evidenceCode":"ECO:0000305","id":"26240322","source":"PubMed"}],"name":"cob(II)alamin"}],"commentType":"COFACTOR"}
```

Source SHA-256: `7c691f44889f41a52c576e4cd1ae8e11c3cf7188b087ddf90064e3b8af6124a1`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q83XP3.json)  
**Locator:** `/references/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:53.086451+00:00.  

```json
{"citation":{"authors":["Marous D.R.","Lloyd E.P.","Buller A.R.","Moshos K.A.","Grove T.L.","Blaszczyk A.J.","Booker S.J.","Townsend C.A."],"citationCrossReferences":[{"database":"PubMed","id":"26240322"},{"database":"DOI","id":"10.1073/pnas.1508615112"}],"citationType":"journal article","firstPage":"10354","id":"26240322","journal":"Proc. Natl. Acad. Sci. U.S.A.","lastPage":"10358","publicationDate":"2015","title":"Consecutive radical S-adenosylmethionine methylations form the ethyl side chain in thienamycin biosynthesis.","volume":"112"},"referenceComments":[{"type":"STRAIN","value":"ATCC 35852 / DSM 46488 / JCM 4925 / NBRC 14057 / NCIMB 11928 / NRRL 8057 / MA-4297"}],"referenceNumber":4,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","COFACTOR","PATHWAY"]}
```

Source SHA-256: `7c691f44889f41a52c576e4cd1ae8e11c3cf7188b087ddf90064e3b8af6124a1`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q83XP3?format=txt&versions=74)  
**Locator:** `lines 42-51`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 74 / 1.  
**Retrieved:** 2026-11-02T04:31:56.526994+00:00.  

```text
RN   [4]
RP   FUNCTION, CATALYTIC ACTIVITY, COFACTOR, AND PATHWAY.
RC   STRAIN=ATCC 35852 / DSM 46488 / JCM 4925 / NBRC 14057 / NCIMB 11928 / NRRL
RC   8057 / MA-4297;
RX   PubMed=26240322; DOI=10.1073/pnas.1508615112;
RA   Marous D.R., Lloyd E.P., Buller A.R., Moshos K.A., Grove T.L.,
RA   Blaszczyk A.J., Booker S.J., Townsend C.A.;
RT   "Consecutive radical S-adenosylmethionine methylations form the ethyl side
RT   chain in thienamycin biosynthesis.";
RL   Proc. Natl. Acad. Sci. U.S.A. 112:10354-10358(2015).
```

Source SHA-256: `c71dc726e36b019728f318f6abb151a59107da10d242b3c7f4b371257db94606`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q83XP3?format=txt&versions=74)  
**Locator:** `lines 101-106`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 74 / 1.  
**Retrieved:** 2026-11-02T04:31:56.526994+00:00.  

```text
CC   -!- COFACTOR:
CC       Name=[4Fe-4S] cluster; Xref=ChEBI:CHEBI:49883;
CC         Evidence={ECO:0000269|PubMed:26240322};
CC       Note=Binds 1 [4Fe-4S] cluster. The cluster is coordinated with 3
CC       cysteines and an exchangeable S-adenosyl-L-methionine.
CC       {ECO:0000250|UniProtKB:A0A6B9HEI0};
```

Source SHA-256: `c71dc726e36b019728f318f6abb151a59107da10d242b3c7f4b371257db94606`.

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q83XP3?format=txt&versions=74)  
**Locator:** `lines 107-109`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 74 / 1.  
**Retrieved:** 2026-11-02T04:31:56.526994+00:00.  

```text
CC   -!- COFACTOR:
CC       Name=cob(II)alamin; Xref=ChEBI:CHEBI:16304;
CC         Evidence={ECO:0000305|PubMed:26240322};
```

Source SHA-256: `c71dc726e36b019728f318f6abb151a59107da10d242b3c7f4b371257db94606`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 155. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
