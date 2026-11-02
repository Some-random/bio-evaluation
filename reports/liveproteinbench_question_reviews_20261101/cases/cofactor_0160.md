# cofactor_0160

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `cofactor`  
**Author expected answer:** **C** — &#91;4Fe-4S&#93; cluster

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | invalid_review |

**Paired comparison:** not comparable: one or both reviews invalid or missing. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MKSKILCNLFKGKSCICLYTNCLNENNVNKCYYNLVRNYSDHVKDHFNKPRNVGSFDKNEKNIGTSIVGKASCGDVIKLQLKIENDVIKDARFMAFGCGSAIASSSYATELIKGKTIDEALKIKNNDIASHLSLPPVKIHCSLLAEDAIKHAIKNYREKVLT

[Multiple Choices]
A. Zn(2+)
B. pantetheine 4'-phosphate
C. [4Fe-4S] cluster
D. NAD(+)
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

> The exact matched sequence is annotated as the iron-sulfur cluster assembly protein IscU, with a &#91;4Fe-4S&#93; cluster listed as its cofactor and evidence attributed to a 2021 publication. This supports choice C, though the cited primary study was not independently reviewed here.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The cysteine-rich sequence may suggest metal or iron-sulfur binding, but that pattern alone does not reliably distinguish a &#91;4Fe-4S&#93; cluster from other metal-binding possibilities.


**Missing item-specific fact**

> The protein-specific identification as IscU and its experimentally supported &#91;4Fe-4S&#93; cofactor annotation are not supplied in the question.


**Reason**

> Selecting C requires recognizing or identifying this particular protein and knowing its cofactor association; generic sequence reasoning does not establish the specific cluster.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The reviewer evidence supports C for this matched protein. The sequence alone is insufficient to resolve the cofactor, but that is missing item-specific information rather than evidence that multiple choices are correct.


### Important caveats

- IscU is an iron-sulfur cluster assembly scaffold; describing its cofactor as required for catalytic activity may not precisely describe its role.
- The cofactor annotation is experimental-evidence-coded and cites a publication, but the primary study was not independently validated here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The cysteine-rich sequence may suggest metal or iron-sulfur binding, but that pattern alone does not reliably distinguish a [4Fe-4S] cluster from other metal-binding possibilities.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identification as IscU and its experimentally supported [4Fe-4S] cofactor annotation are not supplied in the question.",
    "reason": "Selecting C requires recognizing or identifying this particular protein and knowing its cofactor association; generic sequence reasoning does not establish the specific cluster."
  },
  "case_id": "cofactor_0160",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact matched sequence is annotated as the iron-sulfur cluster assembly protein IscU, with a [4Fe-4S] cluster listed as its cofactor and evidence attributed to a 2021 publication. This supports choice C, though the cited primary study was not independently reviewed here."
  },
  "important_caveats": [
    "IscU is an iron-sulfur cluster assembly scaffold; describing its cofactor as required for catalytic activity may not precisely describe its role.",
    "The cofactor annotation is experimental-evidence-coded and cites a publication, but the primary study was not independently validated here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer evidence supports C for this matched protein. The sequence alone is insufficient to resolve the cofactor, but that is missing item-specific information rather than evidence that multiple choices are correct."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0160",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact matched sequence is annotated as the iron-sulfur cluster assembly protein IscU, with a [4Fe-4S] cluster listed as its cofactor and evidence attributed to a 2021 publication. This supports choice C, though the cited primary study was not independently reviewed here.",
    "evidence_ids": ["C4", "C5", "C6", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The cysteine-rich sequence may suggest metal or iron-sulfur binding, but that pattern alone does not reliably distinguish a [4Fe-4S] cluster from other metal-binding possibilities.",
    "missing_item_specific_fact": "The protein-specific identification as IscU and its experimentally supported [4Fe-4S] cofactor annotation are not supplied in the question.",
    "reason": "Selecting C requires recognizing or identifying this particular protein and knowing its cofactor association; generic sequence reasoning does not establish the specific cluster."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer evidence supports C for this matched protein. The sequence alone is insufficient to resolve the cofactor, but that is missing item-specific information rather than evidence that multiple choices are correct."
  },
  "important_caveats": [
    "IscU is an iron-sulfur cluster assembly scaffold; describing its cofactor as required for catalytic activity may not precisely describe its role.",
    "The cofactor annotation is experimental-evidence-coded and cites a publication, but the primary study was not independently validated here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `invalid_review`.

**This result is not a valid structured review.** Any saved labels below remain the model’s original values; they are excluded from label distributions and paired agreement. No field or option ID has been repaired.

**Validation errors:** `question_ambiguity:invalid_option_ids`.

### Expected-answer support: supported

> UniProt entry Q8IKT4 (PfIscU, Iron-sulfur cluster assembly protein IscU from Plasmodium falciparum 3D7) annotates the cofactor as &#91;4Fe-4S&#93; cluster (ChEBI:CHEBI:49883) with evidence code ECO:0000269 linked to experimental literature (PubMed:34032321, Sadik et al. 2021, Mol Microbiol). The sequence matches exactly (SHA256 confirmed). The protein name itself ('Iron-sulfur cluster assembly protein') directly implies Fe-S cluster involvement, and the cited paper specifically addresses &#91;Fe-S&#93; biogenesis and ISC scaffold assembly in P. falciparum.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal region contains an unusually dense cysteine cluster (C7, C15, C18, C21, C29 — five Cys in ~30 residues) with tight spacing (C-X3-C-X3-C at positions 15-18-21). This C-X3-C-X3-C motif is characteristic of Fe-S cluster coordination in scaffold proteins, whereas Zn(2+) coordination typically follows C-X2,4-C patterns embedded in defined structural motifs (zinc fingers, metalloprotease sites) with intervening His residues. The sequence lacks any GxGxxG Rossmann-fold motif (eliminating NAD+), lacks ACP-like β-turn/α-helix motifs with a Ser-Pantetheine attachment site (eliminating pantetheine 4'-phosphate), and lacks the compact C2H2/C4 zinc-finger architecture expected for Zn(2+). The small size (162 aa) and cysteine-rich N-terminal architecture are consistent with a scaffold-type Fe-S assembly protein.


**Missing item-specific fact**

> The specific designation &#91;4Fe-4S&#93; versus &#91;2Fe-2S&#93; for this particular IscU variant may require knowledge of the published experimental characterization; however, the question only offers &#91;4Fe-4S&#93; among Fe-S options, and the general Fe-S assignment is inferable from the cysteine motif.


**Reason**

> A knowledgeable biologist can eliminate NAD+ (no Rossmann fold), pantetheine 4'-phosphate (no ACP motif), and argue against Zn(2+) based on the atypical cysteine spacing and absence of zinc-finger architecture. The tight C-X3-C-X3-C cluster is a recognized Fe-S coordination signature. The remaining choice &#91;4Fe-4S&#93; is the only Fe-S option provided.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A (Zn2+)"
]
```

> In principle, a cysteine-rich protein could bind Zn(2+), and without knowing the specific protein identity, one might tentatively assign Zn(2+) to a Cys-rich region. However, the tight C-X3-C-X3-C spacing and absence of any His residues in the N-terminal Cys cluster make Zn(2+) coordination structurally implausible, and no other option (B, D) is defensible. The ambiguity is minor and resolvable with standard bioinorganic reasoning.


### Important caveats

- The UniProt annotation uses ECO:0000269 (evidence used in automatic assertion) linked to a specific PubMed paper, indicating the annotation was derived from literature rather than a direct biochemical assay of this exact protein's cofactor in isolation.
- The historical UniProt entry (version 123, released 2026-01) already contains the &#91;4Fe-4S&#93; annotation, so this was available before the benchmark construction cutoff.
- The specific cluster nuclearity (&#91;4Fe-4S&#93; vs &#91;2Fe-2S&#93;) for PfIscU may reflect the predominant form reported in the cited study; IscU scaffold proteins can transiently carry different cluster types.
- The reviewer-only evidence was not available to the evaluated model; the reasoning assessment is based solely on the sequence and general biological knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal region contains an unusually dense cysteine cluster (C7, C15, C18, C21, C29 — five Cys in ~30 residues) with tight spacing (C-X3-C-X3-C at positions 15-18-21). This C-X3-C-X3-C motif is characteristic of Fe-S cluster coordination in scaffold proteins, whereas Zn(2+) coordination typically follows C-X2,4-C patterns embedded in defined structural motifs (zinc fingers, metalloprotease sites) with intervening His residues. The sequence lacks any GxGxxG Rossmann-fold motif (eliminating NAD+), lacks ACP-like β-turn/α-helix motifs with a Ser-Pantetheine attachment site (eliminating pantetheine 4'-phosphate), and lacks the compact C2H2/C4 zinc-finger architecture expected for Zn(2+). The small size (162 aa) and cysteine-rich N-terminal architecture are consistent with a scaffold-type Fe-S assembly protein.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The specific designation [4Fe-4S] versus [2Fe-2S] for this particular IscU variant may require knowledge of the published experimental characterization; however, the question only offers [4Fe-4S] among Fe-S options, and the general Fe-S assignment is inferable from the cysteine motif.",
    "reason": "A knowledgeable biologist can eliminate NAD+ (no Rossmann fold), pantetheine 4'-phosphate (no ACP motif), and argue against Zn(2+) based on the atypical cysteine spacing and absence of zinc-finger architecture. The tight C-X3-C-X3-C cluster is a recognized Fe-S coordination signature. The remaining choice [4Fe-4S] is the only Fe-S option provided."
  },
  "case_id": "cofactor_0160",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4",
      "H3"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q8IKT4 (PfIscU, Iron-sulfur cluster assembly protein IscU from Plasmodium falciparum 3D7) annotates the cofactor as [4Fe-4S] cluster (ChEBI:CHEBI:49883) with evidence code ECO:0000269 linked to experimental literature (PubMed:34032321, Sadik et al. 2021, Mol Microbiol). The sequence matches exactly (SHA256 confirmed). The protein name itself ('Iron-sulfur cluster assembly protein') directly implies Fe-S cluster involvement, and the cited paper specifically addresses [Fe-S] biogenesis and ISC scaffold assembly in P. falciparum."
  },
  "important_caveats": [
    "The UniProt annotation uses ECO:0000269 (evidence used in automatic assertion) linked to a specific PubMed paper, indicating the annotation was derived from literature rather than a direct biochemical assay of this exact protein's cofactor in isolation.",
    "The historical UniProt entry (version 123, released 2026-01) already contains the [4Fe-4S] annotation, so this was available before the benchmark construction cutoff.",
    "The specific cluster nuclearity ([4Fe-4S] vs [2Fe-2S]) for PfIscU may reflect the predominant form reported in the cited study; IscU scaffold proteins can transiently carry different cluster types.",
    "The reviewer-only evidence was not available to the evaluated model; the reasoning assessment is based solely on the sequence and general biological knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A (Zn2+)"
    ],
    "reason": "In principle, a cysteine-rich protein could bind Zn(2+), and without knowing the specific protein identity, one might tentatively assign Zn(2+) to a Cys-rich region. However, the tight C-X3-C-X3-C spacing and absence of any His residues in the N-terminal Cys cluster make Zn(2+) coordination structurally implausible, and no other option (B, D) is defensible. The ambiguity is minor and resolvable with standard bioinorganic reasoning."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0160",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q8IKT4 (PfIscU, Iron-sulfur cluster assembly protein IscU from Plasmodium falciparum 3D7) annotates the cofactor as [4Fe-4S] cluster (ChEBI:CHEBI:49883) with evidence code ECO:0000269 linked to experimental literature (PubMed:34032321, Sadik et al. 2021, Mol Microbiol). The sequence matches exactly (SHA256 confirmed). The protein name itself ('Iron-sulfur cluster assembly protein') directly implies Fe-S cluster involvement, and the cited paper specifically addresses [Fe-S] biogenesis and ISC scaffold assembly in P. falciparum.",
    "evidence_ids": ["C4", "C5", "H2", "H4", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal region contains an unusually dense cysteine cluster (C7, C15, C18, C21, C29 — five Cys in ~30 residues) with tight spacing (C-X3-C-X3-C at positions 15-18-21). This C-X3-C-X3-C motif is characteristic of Fe-S cluster coordination in scaffold proteins, whereas Zn(2+) coordination typically follows C-X2,4-C patterns embedded in defined structural motifs (zinc fingers, metalloprotease sites) with intervening His residues. The sequence lacks any GxGxxG Rossmann-fold motif (eliminating NAD+), lacks ACP-like β-turn/α-helix motifs with a Ser-Pantetheine attachment site (eliminating pantetheine 4'-phosphate), and lacks the compact C2H2/C4 zinc-finger architecture expected for Zn(2+). The small size (162 aa) and cysteine-rich N-terminal architecture are consistent with a scaffold-type Fe-S assembly protein.",
    "missing_item_specific_fact": "The specific designation [4Fe-4S] versus [2Fe-2S] for this particular IscU variant may require knowledge of the published experimental characterization; however, the question only offers [4Fe-4S] among Fe-S options, and the general Fe-S assignment is inferable from the cysteine motif.",
    "reason": "A knowledgeable biologist can eliminate NAD+ (no Rossmann fold), pantetheine 4'-phosphate (no ACP motif), and argue against Zn(2+) based on the atypical cysteine spacing and absence of zinc-finger architecture. The tight C-X3-C-X3-C cluster is a recognized Fe-S coordination signature. The remaining choice [4Fe-4S] is the only Fe-S option provided."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A (Zn2+)"],
    "reason": "In principle, a cysteine-rich protein could bind Zn(2+), and without knowing the specific protein identity, one might tentatively assign Zn(2+) to a Cys-rich region. However, the tight C-X3-C-X3-C spacing and absence of any His residues in the N-terminal Cys cluster make Zn(2+) coordination structurally implausible, and no other option (B, D) is defensible. The ambiguity is minor and resolvable with standard bioinorganic reasoning."
  },
  "important_caveats": [
    "The UniProt annotation uses ECO:0000269 (evidence used in automatic assertion) linked to a specific PubMed paper, indicating the annotation was derived from literature rather than a direct biochemical assay of this exact protein's cofactor in isolation.",
    "The historical UniProt entry (version 123, released 2026-01) already contains the [4Fe-4S] annotation, so this was available before the benchmark construction cutoff.",
    "The specific cluster nuclearity ([4Fe-4S] vs [2Fe-2S]) for PfIscU may reflect the predominant form reported in the cited study; IscU scaffold proteins can transiently carry different cluster types.",
    "The reviewer-only evidence was not available to the evaluated model; the reasoning assessment is based solely on the sequence and general biological knowledge."
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

**Accession:** `Q8IKT4` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 123. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IKT4.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:18.665288+00:00.  

```json
{"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Iron-sulfur cluster assembly protein IscU"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"34032321","source":"PubMed"}],"value":"PfIscU"}]}}
```

Source SHA-256: `df58165e5cdc69c588b06d5dc2395f0f91c8805f9c6fc3461d14468ea7329d6f`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IKT4.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:18.665288+00:00.  

```json
{"cofactors":[{"cofactorCrossReference":{"database":"ChEBI","id":"CHEBI:49883"},"evidences":[{"evidenceCode":"ECO:0000269","id":"34032321","source":"PubMed"}],"name":"[4Fe-4S] cluster"}],"commentType":"COFACTOR"}
```

Source SHA-256: `df58165e5cdc69c588b06d5dc2395f0f91c8805f9c6fc3461d14468ea7329d6f`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IKT4.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:18.665288+00:00.  

```json
{"citation":{"authors":["Sadik M.","Afsar M.","Ramachandran R.","Habib S."],"citationCrossReferences":[{"database":"PubMed","id":"34032321"},{"database":"DOI","id":"10.1111/mmi.14735"}],"citationType":"journal article","firstPage":"606","id":"34032321","journal":"Mol. Microbiol.","lastPage":"623","publicationDate":"2021","title":"[Fe-S] biogenesis and unusual assembly of the ISC scaffold complex in the Plasmodium falciparum mitochondrion.","volume":"116"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":2,"referencePositions":["FUNCTION","COFACTOR","SUBUNIT","INTERACTION WITH ISCS","SUBCELLULAR LOCATION"]}
```

Source SHA-256: `df58165e5cdc69c588b06d5dc2395f0f91c8805f9c6fc3461d14468ea7329d6f`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IKT4?format=txt&versions=123)  
**Locator:** `lines 6-7`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 123 / 1.  
**Retrieved:** 2026-11-02T04:32:21.146174+00:00.  

```text
DE   RecName: Full=Iron-sulfur cluster assembly protein IscU {ECO:0000305};
DE            Short=PfIscU {ECO:0000303|PubMed:34032321};
```

Source SHA-256: `1486d63f9113029908bdb3693392d31626d9b2ff299d97715a630df1a14b4181`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IKT4?format=txt&versions=123)  
**Locator:** `lines 28-35`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 123 / 1.  
**Retrieved:** 2026-11-02T04:32:21.146174+00:00.  

```text
RN   [2] {ECO:0000305}
RP   FUNCTION, COFACTOR, SUBUNIT, INTERACTION WITH ISCS, AND SUBCELLULAR
RP   LOCATION.
RX   PubMed=34032321; DOI=10.1111/mmi.14735;
RA   Sadik M., Afsar M., Ramachandran R., Habib S.;
RT   "[Fe-S] biogenesis and unusual assembly of the ISC scaffold complex in the
RT   Plasmodium falciparum mitochondrion.";
RL   Mol. Microbiol. 116:606-623(2021).
```

Source SHA-256: `1486d63f9113029908bdb3693392d31626d9b2ff299d97715a630df1a14b4181`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IKT4?format=txt&versions=123)  
**Locator:** `lines 52-54`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 123 / 1.  
**Retrieved:** 2026-11-02T04:32:21.146174+00:00.  

```text
CC   -!- COFACTOR:
CC       Name=[4Fe-4S] cluster; Xref=ChEBI:CHEBI:49883;
CC         Evidence={ECO:0000269|PubMed:34032321};
```

Source SHA-256: `1486d63f9113029908bdb3693392d31626d9b2ff299d97715a630df1a14b4181`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 160. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
