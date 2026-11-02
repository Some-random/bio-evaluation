# cofactor_0094

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `cofactor`  
**Author expected answer:** **A** — &#91;4Fe-4S&#93; cluster

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MKTEDMALVFSKLILNPITKRQILNLFKKDDNGNLIIENYIDAYMKGEDINSLGYKTLKSVLDNGLKTFAGEIYKENFKDFLKDPLFKKGLISVVRGLGYFGVKRPFVSGAPFLVVWDVTYACNLRCKHCYANAGKPLEDELNTEEALKTIDILANSGVVAIAFSGGEPLMRKDLFELIDRAKDYNMQVSIASNGTMLNKTNAKKLKEHKVDFVQISLDGTKETHEKFRGIKGIYDKTIEGIKNVVDEDIFCAIATTATKLNYRDVPKVMDLAEELNVNYFMLYNYIPVGVGDYDIDLSPEEREELLNLLWEKLNNDTGKKYRTAFLSTAPYYSRTALEHNKYYLASHFANVDLGENERLKSLANFIGGCGCGRFYLSLRANGDIQPCVFFPLKLGNIKSFKDENDFLEFWRNNKILNDLRDRDKLKICGSCMYKYVCGGCRARAYSYYDDYLREDPGCILTKNLK

[Multiple Choices]
A. [4Fe-4S] cluster
B. Fe(2+)
C. Co(2+)
D. [2Fe-2S] cluster
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

> The supplied sequence exactly matches the UniProt entry for this protein. Its cofactor annotation identifies &#91;4Fe-4S&#93; clusters and cites ECO:0000269 evidence from a 2024 publication; the annotation says the protein binds three such clusters. This supports A, while retaining the qualification that the evidence is reported through the database annotation rather than independently assessed here.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a CxxxCxxC motif (in the segment ACNLRCKHC), a characteristic cysteine motif of radical-SAM enzymes. Radical-SAM chemistry commonly uses a &#91;4Fe-4S&#93; cluster, making A a biologically grounded choice over iron or cobalt ions and a &#91;2Fe-2S&#93; cluster.


**Missing item-specific fact**

> The exact experimentally established cofactor and number of clusters bound by this particular protein are not supplied; the sequence motif supports an inference, not those precise experimental details.


**Reason**

> A recognizable radical-SAM motif in the supplied sequence gives a concrete biological basis for selecting &#91;4Fe-4S&#93;. The inference is not equivalent to direct evidence about this specific protein, but the choices permit a meaningful sequence-based distinction.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The radical-SAM motif supports &#91;4Fe-4S&#93; as the best choice among the listed options; no alternative is comparably supported by the supplied sequence.


### Important caveats

- The reviewer-only database evidence was not available to the evaluated model and supports the key without establishing that the original author used the same source snapshot.
- The cited database annotation reports three &#91;4Fe-4S&#93; clusters, whereas the choices ask only which cofactor is required.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a CxxxCxxC motif (in the segment ACNLRCKHC), a characteristic cysteine motif of radical-SAM enzymes. Radical-SAM chemistry commonly uses a [4Fe-4S] cluster, making A a biologically grounded choice over iron or cobalt ions and a [2Fe-2S] cluster.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The exact experimentally established cofactor and number of clusters bound by this particular protein are not supplied; the sequence motif supports an inference, not those precise experimental details.",
    "reason": "A recognizable radical-SAM motif in the supplied sequence gives a concrete biological basis for selecting [4Fe-4S]. The inference is not equivalent to direct evidence about this specific protein, but the choices permit a meaningful sequence-based distinction."
  },
  "case_id": "cofactor_0094",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry for this protein. Its cofactor annotation identifies [4Fe-4S] clusters and cites ECO:0000269 evidence from a 2024 publication; the annotation says the protein binds three such clusters. This supports A, while retaining the qualification that the evidence is reported through the database annotation rather than independently assessed here."
  },
  "important_caveats": [
    "The reviewer-only database evidence was not available to the evaluated model and supports the key without establishing that the original author used the same source snapshot.",
    "The cited database annotation reports three [4Fe-4S] clusters, whereas the choices ask only which cofactor is required."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The radical-SAM motif supports [4Fe-4S] as the best choice among the listed options; no alternative is comparably supported by the supplied sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0094",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry for this protein. Its cofactor annotation identifies [4Fe-4S] clusters and cites ECO:0000269 evidence from a 2024 publication; the annotation says the protein binds three such clusters. This supports A, while retaining the qualification that the evidence is reported through the database annotation rather than independently assessed here.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a CxxxCxxC motif (in the segment ACNLRCKHC), a characteristic cysteine motif of radical-SAM enzymes. Radical-SAM chemistry commonly uses a [4Fe-4S] cluster, making A a biologically grounded choice over iron or cobalt ions and a [2Fe-2S] cluster.",
    "missing_item_specific_fact": "The exact experimentally established cofactor and number of clusters bound by this particular protein are not supplied; the sequence motif supports an inference, not those precise experimental details.",
    "reason": "A recognizable radical-SAM motif in the supplied sequence gives a concrete biological basis for selecting [4Fe-4S]. The inference is not equivalent to direct evidence about this specific protein, but the choices permit a meaningful sequence-based distinction."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The radical-SAM motif supports [4Fe-4S] as the best choice among the listed options; no alternative is comparably supported by the supplied sequence."
  },
  "important_caveats": [
    "The reviewer-only database evidence was not available to the evaluated model and supports the key without establishing that the original author used the same source snapshot.",
    "The cited database annotation reports three [4Fe-4S] clusters, whereas the choices ask only which cofactor is required."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry F8AME3 (GMGT synthase from Methanothermococcus okinawensis) explicitly annotates the cofactor as &#91;4Fe-4S&#93; cluster (ChEBI:CHEBI:49883) with evidence code ECO:0000269 (direct experimental assay, PubMed:38898040, Li et al. Nat. Commun. 2024). The note specifies the protein binds 3 &#91;4Fe-4S&#93; clusters, with the first coordinated by 3 cysteines and an exchangeable S-adenosyl-L-methionine — the hallmark of a radical SAM enzyme. Mutagenesis of Cys-123, Cys-127, Cys-370, Cys-372, and Cys-438 confirms cluster coordination. The sequence matches the benchmark input exactly (SHA-256 verified).

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The canonical radical SAM motif CX3CX2C is identifiable in the sequence at positions 123–130: C(123)-N(124)-L(125)-R(126)-C(127)-K(128)-H(129)-C(130). This CxxxCxxC pattern is the defining signature of the radical SAM superfamily, which by established biochemistry uses a &#91;4Fe-4S&#93; cluster (the SAM-cleaving cluster) rather than &#91;2Fe-2S&#93;. A model recognizing this motif can eliminate &#91;2Fe-2S&#93; (D), Co(2+) (C, associated with cobalamin/corrinoid enzymes), and simple Fe(2+) (B), arriving at &#91;4Fe-4S&#93; (A) through general knowledge of Fe-S cluster biochemistry and the radical SAM family.


**Missing item-specific fact**

> None required. The radical SAM motif is a general, well-known sequence feature, and its association with &#91;4Fe-4S&#93; is textbook biochemistry. Knowledge of this specific protein's identity (GMGT synthase, 2024 characterization) is not needed to reason from the motif to the cofactor.


**Reason**

> The CX3CX2C motif at Cys-123/127/130 is present in the supplied sequence and is a widely recognized, general biochemical signature. Distinguishing &#91;4Fe-4S&#93; from &#91;2Fe-2S&#93; via the radical SAM assignment is standard knowledge, not an item-specific database lookup. The distractors (Co²⁺, Fe²⁺) are eliminated by the presence of multiple Cys residues in a CxxxCxxC arrangement, which is incompatible with simple metal-ion or &#91;2Fe-2S&#93; coordination.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The CX3CX2C radical SAM motif uniquely points to &#91;4Fe-4S&#93;. &#91;2Fe-2S&#93; (D) requires a different Cys₂Cys₂ or Cys₂His₂ coordination geometry incompatible with the observed CxxxCxxC spacing. Co(2+) (C) and Fe(2+) (B) are not consistent with the multi-cysteine cluster-binding architecture. Only option A is defensible.


### Important caveats

- The protein (GMGT synthase) was characterized experimentally only in 2024 (PubMed:38898040). If the benchmark was constructed before this publication, the &#91;4Fe-4S&#93; annotation would not have been available in databases, though the radical SAM motif reasoning would still be valid.
- The reviewer-only evidence confirms the UniProt annotation is based on direct experimental evidence (ECO:0000269), not computational prediction or similarity transfer.
- The protein binds 3 &#91;4Fe-4S&#93; clusters; the question asks for the cofactor type (singular category), and all three are &#91;4Fe-4S&#93;, so no ambiguity in the answer choice.
- Identifying the CX3CX2C motif in a 466-residue sequence requires careful scanning; a model might miss it, but the reasoning pathway is valid and does not require memorizing this specific protein's entry.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The canonical radical SAM motif CX3CX2C is identifiable in the sequence at positions 123–130: C(123)-N(124)-L(125)-R(126)-C(127)-K(128)-H(129)-C(130). This CxxxCxxC pattern is the defining signature of the radical SAM superfamily, which by established biochemistry uses a [4Fe-4S] cluster (the SAM-cleaving cluster) rather than [2Fe-2S]. A model recognizing this motif can eliminate [2Fe-2S] (D), Co(2+) (C, associated with cobalamin/corrinoid enzymes), and simple Fe(2+) (B), arriving at [4Fe-4S] (A) through general knowledge of Fe-S cluster biochemistry and the radical SAM family.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None required. The radical SAM motif is a general, well-known sequence feature, and its association with [4Fe-4S] is textbook biochemistry. Knowledge of this specific protein's identity (GMGT synthase, 2024 characterization) is not needed to reason from the motif to the cofactor.",
    "reason": "The CX3CX2C motif at Cys-123/127/130 is present in the supplied sequence and is a widely recognized, general biochemical signature. Distinguishing [4Fe-4S] from [2Fe-2S] via the radical SAM assignment is standard knowledge, not an item-specific database lookup. The distractors (Co²⁺, Fe²⁺) are eliminated by the presence of multiple Cys residues in a CxxxCxxC arrangement, which is incompatible with simple metal-ion or [2Fe-2S] coordination."
  },
  "case_id": "cofactor_0094",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry F8AME3 (GMGT synthase from Methanothermococcus okinawensis) explicitly annotates the cofactor as [4Fe-4S] cluster (ChEBI:CHEBI:49883) with evidence code ECO:0000269 (direct experimental assay, PubMed:38898040, Li et al. Nat. Commun. 2024). The note specifies the protein binds 3 [4Fe-4S] clusters, with the first coordinated by 3 cysteines and an exchangeable S-adenosyl-L-methionine — the hallmark of a radical SAM enzyme. Mutagenesis of Cys-123, Cys-127, Cys-370, Cys-372, and Cys-438 confirms cluster coordination. The sequence matches the benchmark input exactly (SHA-256 verified)."
  },
  "important_caveats": [
    "The protein (GMGT synthase) was characterized experimentally only in 2024 (PubMed:38898040). If the benchmark was constructed before this publication, the [4Fe-4S] annotation would not have been available in databases, though the radical SAM motif reasoning would still be valid.",
    "The reviewer-only evidence confirms the UniProt annotation is based on direct experimental evidence (ECO:0000269), not computational prediction or similarity transfer.",
    "The protein binds 3 [4Fe-4S] clusters; the question asks for the cofactor type (singular category), and all three are [4Fe-4S], so no ambiguity in the answer choice.",
    "Identifying the CX3CX2C motif in a 466-residue sequence requires careful scanning; a model might miss it, but the reasoning pathway is valid and does not require memorizing this specific protein's entry."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The CX3CX2C radical SAM motif uniquely points to [4Fe-4S]. [2Fe-2S] (D) requires a different Cys₂Cys₂ or Cys₂His₂ coordination geometry incompatible with the observed CxxxCxxC spacing. Co(2+) (C) and Fe(2+) (B) are not consistent with the multi-cysteine cluster-binding architecture. Only option A is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0094",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry F8AME3 (GMGT synthase from Methanothermococcus okinawensis) explicitly annotates the cofactor as [4Fe-4S] cluster (ChEBI:CHEBI:49883) with evidence code ECO:0000269 (direct experimental assay, PubMed:38898040, Li et al. Nat. Commun. 2024). The note specifies the protein binds 3 [4Fe-4S] clusters, with the first coordinated by 3 cysteines and an exchangeable S-adenosyl-L-methionine — the hallmark of a radical SAM enzyme. Mutagenesis of Cys-123, Cys-127, Cys-370, Cys-372, and Cys-438 confirms cluster coordination. The sequence matches the benchmark input exactly (SHA-256 verified).",
    "evidence_ids": ["C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The canonical radical SAM motif CX3CX2C is identifiable in the sequence at positions 123–130: C(123)-N(124)-L(125)-R(126)-C(127)-K(128)-H(129)-C(130). This CxxxCxxC pattern is the defining signature of the radical SAM superfamily, which by established biochemistry uses a [4Fe-4S] cluster (the SAM-cleaving cluster) rather than [2Fe-2S]. A model recognizing this motif can eliminate [2Fe-2S] (D), Co(2+) (C, associated with cobalamin/corrinoid enzymes), and simple Fe(2+) (B), arriving at [4Fe-4S] (A) through general knowledge of Fe-S cluster biochemistry and the radical SAM family.",
    "missing_item_specific_fact": "None required. The radical SAM motif is a general, well-known sequence feature, and its association with [4Fe-4S] is textbook biochemistry. Knowledge of this specific protein's identity (GMGT synthase, 2024 characterization) is not needed to reason from the motif to the cofactor.",
    "reason": "The CX3CX2C motif at Cys-123/127/130 is present in the supplied sequence and is a widely recognized, general biochemical signature. Distinguishing [4Fe-4S] from [2Fe-2S] via the radical SAM assignment is standard knowledge, not an item-specific database lookup. The distractors (Co²⁺, Fe²⁺) are eliminated by the presence of multiple Cys residues in a CxxxCxxC arrangement, which is incompatible with simple metal-ion or [2Fe-2S] coordination."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The CX3CX2C radical SAM motif uniquely points to [4Fe-4S]. [2Fe-2S] (D) requires a different Cys₂Cys₂ or Cys₂His₂ coordination geometry incompatible with the observed CxxxCxxC spacing. Co(2+) (C) and Fe(2+) (B) are not consistent with the multi-cysteine cluster-binding architecture. Only option A is defensible."
  },
  "important_caveats": [
    "The protein (GMGT synthase) was characterized experimentally only in 2024 (PubMed:38898040). If the benchmark was constructed before this publication, the [4Fe-4S] annotation would not have been available in databases, though the radical SAM motif reasoning would still be valid.",
    "The reviewer-only evidence confirms the UniProt annotation is based on direct experimental evidence (ECO:0000269), not computational prediction or similarity transfer.",
    "The protein binds 3 [4Fe-4S] clusters; the question asks for the cofactor type (singular category), and all three are [4Fe-4S], so no ambiguity in the answer choice.",
    "Identifying the CX3CX2C motif in a 466-residue sequence requires careful scanning; a model might miss it, but the reasoning pathway is valid and does not require memorizing this specific protein's entry."
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

**Accession:** `F8AME3` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 63. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/F8AME3.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:17.852248+00:00.  

```json
{"cofactors":[{"cofactorCrossReference":{"database":"ChEBI","id":"CHEBI:49883"},"evidences":[{"evidenceCode":"ECO:0000269","id":"38898040","source":"PubMed"}],"name":"[4Fe-4S] cluster"}],"commentType":"COFACTOR","note":{"texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"38898040","source":"PubMed"}],"value":"Binds 3 [4Fe-4S] clusters (PubMed:38898040). The first cluster is coordinated with 3 cysteines and an exchangeable S-adenosyl-L-methionine (PubMed:38898040)."}]}}
```

Source SHA-256: `17353e74adf1b04760d092e7ccb20ff7b58fbb5dbf81cd35514ef3e267e3957b`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/F8AME3.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:17.852248+00:00.  

```json
{"citation":{"authors":["Li Y.","Yu T.","Feng X.","Zhao B.","Chen H.","Yang H.","Chen X.","Zhang X.H.","Anderson H.R.","Burns N.Z.","Zeng F.","Tao L.","Zeng Z."],"citationCrossReferences":[{"database":"PubMed","id":"38898040"},{"database":"DOI","id":"10.1038/s41467-024-49650-x"}],"citationType":"journal article","firstPage":"5256","id":"38898040","journal":"Nat. Commun.","lastPage":"5256","publicationDate":"2024","title":"Biosynthesis of GMGT lipids by a radical SAM enzyme associated with anaerobic archaea and oxygen-deficient environments.","volume":"15"},"referenceNumber":2,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","COFACTOR","DOMAIN","MUTAGENESIS OF CYS-123; CYS-127; CYS-370; CYS-372 AND CYS-438"]}
```

Source SHA-256: `17353e74adf1b04760d092e7ccb20ff7b58fbb5dbf81cd35514ef3e267e3957b`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/F8AME3?format=txt&versions=63)  
**Locator:** `lines 25-33`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 63 / 1.  
**Retrieved:** 2026-11-02T04:28:22.053218+00:00.  

```text
RN   [2]
RP   FUNCTION, CATALYTIC ACTIVITY, COFACTOR, DOMAIN, AND MUTAGENESIS OF CYS-123;
RP   CYS-127; CYS-370; CYS-372 AND CYS-438.
RX   PubMed=38898040; DOI=10.1038/s41467-024-49650-x;
RA   Li Y., Yu T., Feng X., Zhao B., Chen H., Yang H., Chen X., Zhang X.H.,
RA   Anderson H.R., Burns N.Z., Zeng F., Tao L., Zeng Z.;
RT   "Biosynthesis of GMGT lipids by a radical SAM enzyme associated with
RT   anaerobic archaea and oxygen-deficient environments.";
RL   Nat. Commun. 15:5256-5256(2024).
```

Source SHA-256: `ffeab1834d6d371a9d99d7ce477b3be2e5158fffdce4bcd9a0d81d96a004a88e`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/F8AME3?format=txt&versions=63)  
**Locator:** `lines 50-55`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 63 / 1.  
**Retrieved:** 2026-11-02T04:28:22.053218+00:00.  

```text
CC   -!- COFACTOR:
CC       Name=[4Fe-4S] cluster; Xref=ChEBI:CHEBI:49883;
CC         Evidence={ECO:0000269|PubMed:38898040};
CC       Note=Binds 3 [4Fe-4S] clusters (PubMed:38898040). The first cluster is
CC       coordinated with 3 cysteines and an exchangeable S-adenosyl-L-
CC       methionine (PubMed:38898040). {ECO:0000269|PubMed:38898040};
```

Source SHA-256: `ffeab1834d6d371a9d99d7ce477b3be2e5158fffdce4bcd9a0d81d96a004a88e`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 94. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
