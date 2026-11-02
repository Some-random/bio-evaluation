# pathway_0118

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `pathway`  
**Author expected answer:** **D** — Membrane lipid metabolism. .

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MKTEDMALVFSKLILNPITKRQILNLFKKDDNGNLIIENYIDAYMKGEDINSLGYKTLKSVLDNGLKTFAGEIYKENFKDFLKDPLFKKGLISVVRGLGYFGVKRPFVSGAPFLVVWDVTYACNLRCKHCYANAGKPLEDELNTEEALKTIDILANSGVVAIAFSGGEPLMRKDLFELIDRAKDYNMQVSIASNGTMLNKTNAKKLKEHKVDFVQISLDGTKETHEKFRGIKGIYDKTIEGIKNVVDEDIFCAIATTATKLNYRDVPKVMDLAEELNVNYFMLYNYIPVGVGDYDIDLSPEEREELLNLLWEKLNNDTGKKYRTAFLSTAPYYSRTALEHNKYYLASHFANVDLGENERLKSLANFIGGCGCGRFYLSLRANGDIQPCVFFPLKLGNIKSFKDENDFLEFWRNNKILNDLRDRDKLKICGSCMYKYVCGGCRARAYSYYDDYLREDPGCILTKNLK

[Multiple Choices]
A. Steroid biosynthesis
B. iron-sulfur cluster biosynthesis. .
C. IMP biosynthesis via de novo pathway
D. Membrane lipid metabolism. .
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

> The exact sequence matches UniProt entry F8AME3, whose pathway annotation is “Membrane lipid metabolism.” The entry identifies the protein as GMGT synthase and cites a 2024 publication on GMGT lipid biosynthesis. This supports D, while the excerpts do not independently establish the primary experimental results.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence has cysteine-rich motifs consistent with an iron-sulfur-binding radical SAM enzyme, but that does not identify its specific substrate or establish which pathway it functions in. The motif alone cannot distinguish membrane-lipid biosynthesis from other radical-SAM-associated functions.


**Missing item-specific fact**

> The protein-specific functional identification as GMGT synthase and its role in GMGT lipid biosynthesis, as supplied by the annotation and cited research.


**Reason**

> The pathway choice depends on protein-specific functional information absent from the sequence prompt; recognizing the exact sequence or recalling its database annotation would be lookup or memorization, not reasoning from the supplied input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied reviewer evidence supports membrane lipid metabolism. An iron-sulfur-binding motif would not by itself make iron-sulfur cluster biosynthesis a defensible pathway assignment.


### Important caveats

- The current and archived UniProt records both match the supplied sequence, but the author's exact data-source snapshot is unknown.
- The pathway annotation cites a publication; the provided excerpts do not independently validate that paper's experimental evidence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has cysteine-rich motifs consistent with an iron-sulfur-binding radical SAM enzyme, but that does not identify its specific substrate or establish which pathway it functions in. The motif alone cannot distinguish membrane-lipid biosynthesis from other radical-SAM-associated functions.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific functional identification as GMGT synthase and its role in GMGT lipid biosynthesis, as supplied by the annotation and cited research.",
    "reason": "The pathway choice depends on protein-specific functional information absent from the sequence prompt; recognizing the exact sequence or recalling its database annotation would be lookup or memorization, not reasoning from the supplied input."
  },
  "case_id": "pathway_0118",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches UniProt entry F8AME3, whose pathway annotation is “Membrane lipid metabolism.” The entry identifies the protein as GMGT synthase and cites a 2024 publication on GMGT lipid biosynthesis. This supports D, while the excerpts do not independently establish the primary experimental results."
  },
  "important_caveats": [
    "The current and archived UniProt records both match the supplied sequence, but the author's exact data-source snapshot is unknown.",
    "The pathway annotation cites a publication; the provided excerpts do not independently validate that paper's experimental evidence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied reviewer evidence supports membrane lipid metabolism. An iron-sulfur-binding motif would not by itself make iron-sulfur cluster biosynthesis a defensible pathway assignment."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0118",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches UniProt entry F8AME3, whose pathway annotation is “Membrane lipid metabolism.” The entry identifies the protein as GMGT synthase and cites a 2024 publication on GMGT lipid biosynthesis. This supports D, while the excerpts do not independently establish the primary experimental results.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence has cysteine-rich motifs consistent with an iron-sulfur-binding radical SAM enzyme, but that does not identify its specific substrate or establish which pathway it functions in. The motif alone cannot distinguish membrane-lipid biosynthesis from other radical-SAM-associated functions.",
    "missing_item_specific_fact": "The protein-specific functional identification as GMGT synthase and its role in GMGT lipid biosynthesis, as supplied by the annotation and cited research.",
    "reason": "The pathway choice depends on protein-specific functional information absent from the sequence prompt; recognizing the exact sequence or recalling its database annotation would be lookup or memorization, not reasoning from the supplied input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied reviewer evidence supports membrane lipid metabolism. An iron-sulfur-binding motif would not by itself make iron-sulfur cluster biosynthesis a defensible pathway assignment."
  },
  "important_caveats": [
    "The current and archived UniProt records both match the supplied sequence, but the author's exact data-source snapshot is unknown.",
    "The pathway annotation cites a publication; the provided excerpts do not independently validate that paper's experimental evidence."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry F8AME3 (GMGT synthase, Gms) explicitly annotates the pathway as 'Membrane lipid metabolism' (evidence C5, H3), based on experimental characterization in PubMed:38898040 (Nat. Commun. 2024). The enzyme catalyzes biosynthesis of GMGT lipids, which are membrane lipids in anaerobic archaea. The sequence matches exactly (466 AA, SHA256 confirmed).

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C4](#evidence-c4), [C6](#evidence-c6), [H2](#evidence-h2).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence prominently displays radical SAM motifs (CxxxCxxC pattern: 'CGSCMYKYVCGGCRARAY' near the C-terminus, plus additional cysteine-rich regions). These motifs are the hallmark of iron-sulfur cluster-dependent enzymes and are shared across hundreds of radical SAM enzymes in diverse pathways. Without knowing this specific enzyme's function, a model or biologist seeing these motifs would most naturally associate the protein with iron-sulfur cluster biosynthesis (choice B) or at minimum cannot distinguish D from B on sequence grounds alone. The actual function—synthesizing GMGT membrane lipids—was only characterized in a 2024 publication and is not inferable from general sequence features.


**Missing item-specific fact**

> The specific catalytic function of this radical SAM enzyme as a GMGT lipid synthase (published 2024, UniProt entry first released 2025-02-05). No lipid-binding domain, membrane-targeting signal, or pathway-specific structural motif in the sequence uniquely identifies 'membrane lipid metabolism' over 'iron-sulfur cluster biosynthesis.'


**Reason**

> The visible sequence features (radical SAM CxxxCxxC motifs, general α/β fold) are consistent with many radical SAM enzymes across multiple pathways. The distinction between 'uses Fe-S cluster as cofactor for lipid synthesis' (D) versus 'participates in Fe-S cluster biosynthesis' (B) requires protein-specific experimental knowledge (the 2024 Nat. Commun. paper). General biological reasoning from the sequence alone would more likely point toward B than D.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> The radical SAM motif (CxxxCxxC) is the most salient sequence feature and is classically associated with iron-sulfur cluster-dependent chemistry. Without external knowledge of this specific enzyme's lipid-synthesizing function, choice B (iron-sulfur cluster biosynthesis) is a defensible inference from the sequence. Choice D requires knowing the 2024 experimental characterization of GMGT lipid biosynthesis.


### Important caveats

- The UniProt annotation 'Membrane lipid metabolism' is supported by experimental evidence (ECO:0000305, PubMed:38898040, 2024), not merely computational inference.
- The radical SAM Fe-S cluster in this enzyme is a catalytic cofactor for lipid synthesis, not the pathway product—this distinction is subtle and not obvious from sequence alone.
- The function was only characterized in 2024 and the UniProt entry was first released in February 2025, making this knowledge very recent and unlikely to be embedded in most model training data at the time of benchmark construction.
- The organism (Methanothermococcus okinawensis, an archaeon) is not provided in the user input, removing a contextual clue that archaeal membrane lipid pathways are distinct from bacterial/eukaryotic ones.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence prominently displays radical SAM motifs (CxxxCxxC pattern: 'CGSCMYKYVCGGCRARAY' near the C-terminus, plus additional cysteine-rich regions). These motifs are the hallmark of iron-sulfur cluster-dependent enzymes and are shared across hundreds of radical SAM enzymes in diverse pathways. Without knowing this specific enzyme's function, a model or biologist seeing these motifs would most naturally associate the protein with iron-sulfur cluster biosynthesis (choice B) or at minimum cannot distinguish D from B on sequence grounds alone. The actual function—synthesizing GMGT membrane lipids—was only characterized in a 2024 publication and is not inferable from general sequence features.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific catalytic function of this radical SAM enzyme as a GMGT lipid synthase (published 2024, UniProt entry first released 2025-02-05). No lipid-binding domain, membrane-targeting signal, or pathway-specific structural motif in the sequence uniquely identifies 'membrane lipid metabolism' over 'iron-sulfur cluster biosynthesis.'",
    "reason": "The visible sequence features (radical SAM CxxxCxxC motifs, general α/β fold) are consistent with many radical SAM enzymes across multiple pathways. The distinction between 'uses Fe-S cluster as cofactor for lipid synthesis' (D) versus 'participates in Fe-S cluster biosynthesis' (B) requires protein-specific experimental knowledge (the 2024 Nat. Commun. paper). General biological reasoning from the sequence alone would more likely point toward B than D."
  },
  "case_id": "pathway_0118",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C4",
      "C6",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry F8AME3 (GMGT synthase, Gms) explicitly annotates the pathway as 'Membrane lipid metabolism' (evidence C5, H3), based on experimental characterization in PubMed:38898040 (Nat. Commun. 2024). The enzyme catalyzes biosynthesis of GMGT lipids, which are membrane lipids in anaerobic archaea. The sequence matches exactly (466 AA, SHA256 confirmed)."
  },
  "important_caveats": [
    "The UniProt annotation 'Membrane lipid metabolism' is supported by experimental evidence (ECO:0000305, PubMed:38898040, 2024), not merely computational inference.",
    "The radical SAM Fe-S cluster in this enzyme is a catalytic cofactor for lipid synthesis, not the pathway product—this distinction is subtle and not obvious from sequence alone.",
    "The function was only characterized in 2024 and the UniProt entry was first released in February 2025, making this knowledge very recent and unlikely to be embedded in most model training data at the time of benchmark construction.",
    "The organism (Methanothermococcus okinawensis, an archaeon) is not provided in the user input, removing a contextual clue that archaeal membrane lipid pathways are distinct from bacterial/eukaryotic ones."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "The radical SAM motif (CxxxCxxC) is the most salient sequence feature and is classically associated with iron-sulfur cluster-dependent chemistry. Without external knowledge of this specific enzyme's lipid-synthesizing function, choice B (iron-sulfur cluster biosynthesis) is a defensible inference from the sequence. Choice D requires knowing the 2024 experimental characterization of GMGT lipid biosynthesis."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0118",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry F8AME3 (GMGT synthase, Gms) explicitly annotates the pathway as 'Membrane lipid metabolism' (evidence C5, H3), based on experimental characterization in PubMed:38898040 (Nat. Commun. 2024). The enzyme catalyzes biosynthesis of GMGT lipids, which are membrane lipids in anaerobic archaea. The sequence matches exactly (466 AA, SHA256 confirmed).",
    "evidence_ids": ["C5", "H3", "C4", "C6", "H2"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence prominently displays radical SAM motifs (CxxxCxxC pattern: 'CGSCMYKYVCGGCRARAY' near the C-terminus, plus additional cysteine-rich regions). These motifs are the hallmark of iron-sulfur cluster-dependent enzymes and are shared across hundreds of radical SAM enzymes in diverse pathways. Without knowing this specific enzyme's function, a model or biologist seeing these motifs would most naturally associate the protein with iron-sulfur cluster biosynthesis (choice B) or at minimum cannot distinguish D from B on sequence grounds alone. The actual function—synthesizing GMGT membrane lipids—was only characterized in a 2024 publication and is not inferable from general sequence features.",
    "missing_item_specific_fact": "The specific catalytic function of this radical SAM enzyme as a GMGT lipid synthase (published 2024, UniProt entry first released 2025-02-05). No lipid-binding domain, membrane-targeting signal, or pathway-specific structural motif in the sequence uniquely identifies 'membrane lipid metabolism' over 'iron-sulfur cluster biosynthesis.'",
    "reason": "The visible sequence features (radical SAM CxxxCxxC motifs, general α/β fold) are consistent with many radical SAM enzymes across multiple pathways. The distinction between 'uses Fe-S cluster as cofactor for lipid synthesis' (D) versus 'participates in Fe-S cluster biosynthesis' (B) requires protein-specific experimental knowledge (the 2024 Nat. Commun. paper). General biological reasoning from the sequence alone would more likely point toward B than D."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "The radical SAM motif (CxxxCxxC) is the most salient sequence feature and is classically associated with iron-sulfur cluster-dependent chemistry. Without external knowledge of this specific enzyme's lipid-synthesizing function, choice B (iron-sulfur cluster biosynthesis) is a defensible inference from the sequence. Choice D requires knowing the 2024 experimental characterization of GMGT lipid biosynthesis."
  },
  "important_caveats": [
    "The UniProt annotation 'Membrane lipid metabolism' is supported by experimental evidence (ECO:0000305, PubMed:38898040, 2024), not merely computational inference.",
    "The radical SAM Fe-S cluster in this enzyme is a catalytic cofactor for lipid synthesis, not the pathway product—this distinction is subtle and not obvious from sequence alone.",
    "The function was only characterized in 2024 and the UniProt entry was first released in February 2025, making this knowledge very recent and unlikely to be embedded in most model training data at the time of benchmark construction.",
    "The organism (Methanothermococcus okinawensis, an archaeon) is not provided in the user input, removing a contextual clue that archaeal membrane lipid pathways are distinct from bacterial/eukaryotic ones."
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

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/F8AME3.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:17.852248+00:00.  

```json
"F8AME3"
```

Source SHA-256: `17353e74adf1b04760d092e7ccb20ff7b58fbb5dbf81cd35514ef3e267e3957b`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/F8AME3.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:17.852248+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"38898040","source":"PubMed"}],"value":"1.-.-.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"38898040","source":"PubMed"}],"value":"GMGT synthase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"38898040","source":"PubMed"}],"value":"Gms"}]}}
```

Source SHA-256: `17353e74adf1b04760d092e7ccb20ff7b58fbb5dbf81cd35514ef3e267e3957b`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/F8AME3.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:17.852248+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"38898040","source":"PubMed"}],"value":"Membrane lipid metabolism"}]}
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

### Evidence H2

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

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/F8AME3?format=txt&versions=63)  
**Locator:** `lines 56-56`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 63 / 1.  
**Retrieved:** 2026-11-02T04:28:22.053218+00:00.  

```text
CC   -!- PATHWAY: Membrane lipid metabolism. {ECO:0000305|PubMed:38898040}.
```

Source SHA-256: `ffeab1834d6d371a9d99d7ce477b3be2e5158fffdce4bcd9a0d81d96a004a88e`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 118. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
