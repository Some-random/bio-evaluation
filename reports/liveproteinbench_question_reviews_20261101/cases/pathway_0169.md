# pathway_0169

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `pathway`  
**Author expected answer:** **B** — Alkaloid biosynthesis. .

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MEMMQLSFASAVVYSLIFFVFLLVKQLLKPKSHKKLPPGPWTLPIIGNLHQILGALPHRIFKDLSDKYGPLMRIMMGERTTIIVSSATMAKVVLHTHGLAVANRPINSVAKVICYNNLGVTFAEYGEYLKQLRQLYMLELLSPKRVQSFSAVFEDELQTFVKSIKSEVGQPMIIYEKSVTYLYSTICRVMLGNVCNEREKLIKICKKVSFYSAAPIRIEDLFPSMKFIISRIFSTNSILKDLLKDLDDVLDIVIAERENSQYAQEEEDMLGILLKHKRSDGNNSKLKITNKDIKAIIFELLLAATLSVADVVEWAMVEILRHPKVLKQVHDEVRQAFKGQKTITGSDLGKLEYLHMCFKESTRLHPAAPLLFPREAREEFEIDGYTIPKGSWVLTNYWAVGRDPRIWPKPDEFDPERFRNSDIEFYGNHFELIPFGTGRRGCPGILFGITEALYLLAALFYHFDWKLAGGITPEEIDMTEVFGAGCILKNPLNLIPRLAEN

[Multiple Choices]
A. Pigment biosynthesis. .
B. Alkaloid biosynthesis. .
C. iron-sulfur cluster biosynthesis. .
D. peptidoglycan biosynthesis. .
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

> The exact input sequence matches the UniProt entry for rhazimal synthase, which annotates its pathway as alkaloid biosynthesis and cites PubMed 36349266 with experimental evidence (ECO:0000269). The linked paper concerns indole alkaloid biosynthesis. This supports choice B, while the primary paper has not been independently reviewed here.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is consistent with a membrane-associated cytochrome P450, but that protein-family-level clue does not distinguish alkaloid biosynthesis from other specialized plant pathways in the choices.


**Missing item-specific fact**

> The protein-specific identity and experimentally characterized function as rhazimal synthase in alkaloid biosynthesis are needed to select B.


**Reason**

> The pathway annotation supports the key, but the supplied sequence and choices do not provide a sufficiently specific biological argument to identify this particular P450 pathway without protein-specific knowledge or an external annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied evidence supports B for this sequence. The input alone does not meaningfully distinguish the choices, but that is missing information rather than evidence that multiple choices are equally correct.


### Important caveats

- The sequence match is exact; reviewer-only accession and annotation information was not supplied to the evaluated model.
- The cited pathway annotation is experimental-evidence-coded, but the primary publication was not independently validated here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a membrane-associated cytochrome P450, but that protein-family-level clue does not distinguish alkaloid biosynthesis from other specialized plant pathways in the choices.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identity and experimentally characterized function as rhazimal synthase in alkaloid biosynthesis are needed to select B.",
    "reason": "The pathway annotation supports the key, but the supplied sequence and choices do not provide a sufficiently specific biological argument to identify this particular P450 pathway without protein-specific knowledge or an external annotation."
  },
  "case_id": "pathway_0169",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact input sequence matches the UniProt entry for rhazimal synthase, which annotates its pathway as alkaloid biosynthesis and cites PubMed 36349266 with experimental evidence (ECO:0000269). The linked paper concerns indole alkaloid biosynthesis. This supports choice B, while the primary paper has not been independently reviewed here."
  },
  "important_caveats": [
    "The sequence match is exact; reviewer-only accession and annotation information was not supplied to the evaluated model.",
    "The cited pathway annotation is experimental-evidence-coded, but the primary publication was not independently validated here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports B for this sequence. The input alone does not meaningfully distinguish the choices, but that is missing information rather than evidence that multiple choices are equally correct."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0169",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact input sequence matches the UniProt entry for rhazimal synthase, which annotates its pathway as alkaloid biosynthesis and cites PubMed 36349266 with experimental evidence (ECO:0000269). The linked paper concerns indole alkaloid biosynthesis. This supports choice B, while the primary paper has not been independently reviewed here.",
    "evidence_ids": ["C4", "C5", "C6", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is consistent with a membrane-associated cytochrome P450, but that protein-family-level clue does not distinguish alkaloid biosynthesis from other specialized plant pathways in the choices.",
    "missing_item_specific_fact": "The protein-specific identity and experimentally characterized function as rhazimal synthase in alkaloid biosynthesis are needed to select B.",
    "reason": "The pathway annotation supports the key, but the supplied sequence and choices do not provide a sufficiently specific biological argument to identify this particular P450 pathway without protein-specific knowledge or an external annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports B for this sequence. The input alone does not meaningfully distinguish the choices, but that is missing information rather than evidence that multiple choices are equally correct."
  },
  "important_caveats": [
    "The sequence match is exact; reviewer-only accession and annotation information was not supplied to the evaluated model.",
    "The cited pathway annotation is experimental-evidence-coded, but the primary publication was not independently validated here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A9E7S4M3 (Rhazimal synthase, Cytochrome P450 RHS from Alstonia scholaris) explicitly annotates the pathway as 'Alkaloid biosynthesis' with experimental evidence (ECO:0000269, PubMed:36349266). The protein is EC 1.14.14.187, a P450 involved in indole alkaloid biosynthesis. The sequence matches exactly (501 AA, SHA256 confirmed). The expected answer B is directly and experimentally supported.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains the canonical cytochrome P450 heme-binding motif 'FGTGRRGCPG' (the FxxGxxxCxG signature), definitively identifying this as a P450 monooxygenase. This allows confident elimination of C (iron-sulfur cluster biosynthesis, which uses ISC/NIF assembly machinery, not P450s) and D (peptidoglycan biosynthesis, a bacterial pathway using transpeptidases/Mur enzymes, not P450s). However, distinguishing A (pigment biosynthesis) from B (alkaloid biosynthesis) requires knowing which P450 subfamily or substrate class this enzyme belongs to, which is not reliably extractable from sequence alone.


**Missing item-specific fact**

> The specific P450 subfamily assignment and substrate specificity (indole alkaloid cyclization/oxidation vs. flavonoid/pigment hydroxylation) cannot be determined from the sequence without database lookup or memorization of this particular enzyme's identity. Plant P450s participate in both alkaloid and pigment pathways, and general sequence features do not unambiguously assign a P450 to one over the other.


**Reason**

> While the P450 identification eliminates options C and D through general biological reasoning, the critical discrimination between A (pigment biosynthesis) and B (alkaloid biosynthesis) depends on knowing the specific P450 family/substrate, which is an item-specific fact not derivable from the sequence alone. A model could reason that plant P450s are commonly in alkaloid pathways, but this is a probabilistic heuristic, not a definitive sequence-based argument.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> Both pigment biosynthesis (e.g., flavonoid 3'-hydroxylase, a plant P450) and alkaloid biosynthesis (e.g., terpenoid indole alkaloid pathway P450s) involve plant cytochrome P450 enzymes of similar size and architecture. Without subfamily-specific sequence knowledge or the actual protein identity, a knowledgeable reasoner could not definitively exclude A in favor of B based solely on the provided sequence.


### Important caveats

- The UniProt annotation is backed by experimental evidence (ECO:0000269) from a 2022 publication, making the key scientifically well-supported.
- The sequence was first publicly released in UniProt on 2025-06-18 (entry A0A9E7S4M3), meaning it is relatively recent and less likely to be memorized by training data cutoffs.
- Elimination of C and D is strongly reasoning-supported; the A vs. B discrimination is the weak point.
- The reviewer-only evidence was not available to the evaluated model at inference time.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the canonical cytochrome P450 heme-binding motif 'FGTGRRGCPG' (the FxxGxxxCxG signature), definitively identifying this as a P450 monooxygenase. This allows confident elimination of C (iron-sulfur cluster biosynthesis, which uses ISC/NIF assembly machinery, not P450s) and D (peptidoglycan biosynthesis, a bacterial pathway using transpeptidases/Mur enzymes, not P450s). However, distinguishing A (pigment biosynthesis) from B (alkaloid biosynthesis) requires knowing which P450 subfamily or substrate class this enzyme belongs to, which is not reliably extractable from sequence alone.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific P450 subfamily assignment and substrate specificity (indole alkaloid cyclization/oxidation vs. flavonoid/pigment hydroxylation) cannot be determined from the sequence without database lookup or memorization of this particular enzyme's identity. Plant P450s participate in both alkaloid and pigment pathways, and general sequence features do not unambiguously assign a P450 to one over the other.",
    "reason": "While the P450 identification eliminates options C and D through general biological reasoning, the critical discrimination between A (pigment biosynthesis) and B (alkaloid biosynthesis) depends on knowing the specific P450 family/substrate, which is an item-specific fact not derivable from the sequence alone. A model could reason that plant P450s are commonly in alkaloid pathways, but this is a probabilistic heuristic, not a definitive sequence-based argument."
  },
  "case_id": "pathway_0169",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A9E7S4M3 (Rhazimal synthase, Cytochrome P450 RHS from Alstonia scholaris) explicitly annotates the pathway as 'Alkaloid biosynthesis' with experimental evidence (ECO:0000269, PubMed:36349266). The protein is EC 1.14.14.187, a P450 involved in indole alkaloid biosynthesis. The sequence matches exactly (501 AA, SHA256 confirmed). The expected answer B is directly and experimentally supported."
  },
  "important_caveats": [
    "The UniProt annotation is backed by experimental evidence (ECO:0000269) from a 2022 publication, making the key scientifically well-supported.",
    "The sequence was first publicly released in UniProt on 2025-06-18 (entry A0A9E7S4M3), meaning it is relatively recent and less likely to be memorized by training data cutoffs.",
    "Elimination of C and D is strongly reasoning-supported; the A vs. B discrimination is the weak point.",
    "The reviewer-only evidence was not available to the evaluated model at inference time."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "Both pigment biosynthesis (e.g., flavonoid 3'-hydroxylase, a plant P450) and alkaloid biosynthesis (e.g., terpenoid indole alkaloid pathway P450s) involve plant cytochrome P450 enzymes of similar size and architecture. Without subfamily-specific sequence knowledge or the actual protein identity, a knowledgeable reasoner could not definitively exclude A in favor of B based solely on the provided sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0169",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A9E7S4M3 (Rhazimal synthase, Cytochrome P450 RHS from Alstonia scholaris) explicitly annotates the pathway as 'Alkaloid biosynthesis' with experimental evidence (ECO:0000269, PubMed:36349266). The protein is EC 1.14.14.187, a P450 involved in indole alkaloid biosynthesis. The sequence matches exactly (501 AA, SHA256 confirmed). The expected answer B is directly and experimentally supported.",
    "evidence_ids": ["C4", "C5", "C6", "H1", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains the canonical cytochrome P450 heme-binding motif 'FGTGRRGCPG' (the FxxGxxxCxG signature), definitively identifying this as a P450 monooxygenase. This allows confident elimination of C (iron-sulfur cluster biosynthesis, which uses ISC/NIF assembly machinery, not P450s) and D (peptidoglycan biosynthesis, a bacterial pathway using transpeptidases/Mur enzymes, not P450s). However, distinguishing A (pigment biosynthesis) from B (alkaloid biosynthesis) requires knowing which P450 subfamily or substrate class this enzyme belongs to, which is not reliably extractable from sequence alone.",
    "missing_item_specific_fact": "The specific P450 subfamily assignment and substrate specificity (indole alkaloid cyclization/oxidation vs. flavonoid/pigment hydroxylation) cannot be determined from the sequence without database lookup or memorization of this particular enzyme's identity. Plant P450s participate in both alkaloid and pigment pathways, and general sequence features do not unambiguously assign a P450 to one over the other.",
    "reason": "While the P450 identification eliminates options C and D through general biological reasoning, the critical discrimination between A (pigment biosynthesis) and B (alkaloid biosynthesis) depends on knowing the specific P450 family/substrate, which is an item-specific fact not derivable from the sequence alone. A model could reason that plant P450s are commonly in alkaloid pathways, but this is a probabilistic heuristic, not a definitive sequence-based argument."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "Both pigment biosynthesis (e.g., flavonoid 3'-hydroxylase, a plant P450) and alkaloid biosynthesis (e.g., terpenoid indole alkaloid pathway P450s) involve plant cytochrome P450 enzymes of similar size and architecture. Without subfamily-specific sequence knowledge or the actual protein identity, a knowledgeable reasoner could not definitively exclude A in favor of B based solely on the provided sequence."
  },
  "important_caveats": [
    "The UniProt annotation is backed by experimental evidence (ECO:0000269) from a 2022 publication, making the key scientifically well-supported.",
    "The sequence was first publicly released in UniProt on 2025-06-18 (entry A0A9E7S4M3), meaning it is relatively recent and less likely to be memorized by training data cutoffs.",
    "Elimination of C and D is strongly reasoning-supported; the A vs. B discrimination is the weak point.",
    "The reviewer-only evidence was not available to the evaluated model at inference time."
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

**Accession:** `A0A9E7S4M3` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 13. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7S4M3.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:52.188259+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"36349266","source":"PubMed"}],"value":"Cytochrome P450 RHS"}},{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"36349266","source":"PubMed"}],"value":"1.14.19.80"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"36349266","source":"PubMed"}],"value":"Geissoschizine oxidase RHS"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"36349266","source":"PubMed"}],"value":"1.14.14.187"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"36349266","source":"PubMed"}],"value":"Rhazimal synthase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"36349266","source":"PubMed"}],"value":"AsRHS"}]}}
```

Source SHA-256: `c1fd8e022ffe05c9bfa24ba7a6386335a6a1b24a47d508aaaf7d09452928adf5`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7S4M3.json)  
**Locator:** `/comments/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:52.188259+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"36349266","source":"PubMed"}],"value":"Alkaloid biosynthesis"}]}
```

Source SHA-256: `c1fd8e022ffe05c9bfa24ba7a6386335a6a1b24a47d508aaaf7d09452928adf5`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7S4M3.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:52.188259+00:00.  

```json
{"citation":{"authors":["Wang Z.","Xiao Y.","Wu S.","Chen J.","Li A.","Tatsis E.C."],"citationCrossReferences":[{"database":"PubMed","id":"36349266"},{"database":"DOI","id":"10.1039/d2sc03612f"}],"citationType":"journal article","firstPage":"12389","id":"36349266","journal":"Chem. Sci.","lastPage":"12395","publicationDate":"2022","title":"Deciphering and reprogramming the cyclization regioselectivity in bifurcation of indole alkaloid biosynthesis.","volume":"13"},"evidences":[{"evidenceCode":"ECO:0000312","id":"URS65384.1","source":"EMBL"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [MRNA]","FUNCTION","MUTAGENESIS OF VAL-112; CYS-205; VAL-208; SER-212 AND PHE-372","CATALYTIC ACTIVITY","PATHWAY","BIOPHYSICOCHEMICAL PROPERTIES"]}
```

Source SHA-256: `c1fd8e022ffe05c9bfa24ba7a6386335a6a1b24a47d508aaaf7d09452928adf5`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9E7S4M3?format=txt&versions=13)  
**Locator:** `lines 1-18`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 13 / 1.  
**Retrieved:** 2026-11-01T06:27:36.950799+00:00.  

```text
ID   RHS_ALSSC               Reviewed;         501 AA.
AC   A0A9E7S4M3;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   03-MAY-2023, sequence version 1.
DT   28-JAN-2026, entry version 13.
DE   RecName: Full=Rhazimal synthase {ECO:0000303|PubMed:36349266};
DE            Short=AsRHS {ECO:0000303|PubMed:36349266};
DE            EC=1.14.14.187 {ECO:0000269|PubMed:36349266};
DE   AltName: Full=Cytochrome P450 RHS {ECO:0000303|PubMed:36349266};
DE   AltName: Full=Geissoschizine oxidase RHS {ECO:0000303|PubMed:36349266};
DE            EC=1.14.19.80 {ECO:0000269|PubMed:36349266};
GN   Name=RHS {ECO:0000303|PubMed:36349266};
OS   Alstonia scholaris (Dogbane) (Echites scholaris).
OC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;
OC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;
OC   asterids; lamiids; Gentianales; Apocynaceae; Rauvolfioideae; Alstonieae;
OC   Alstonia.
OX   NCBI_TaxID=52822;
```

Source SHA-256: `15ff37b3545781cd88f01534156171f4c96185b4b173d077dc54ff75075b22b3`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9E7S4M3?format=txt&versions=13)  
**Locator:** `lines 19-27`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 13 / 1.  
**Retrieved:** 2026-11-01T06:27:36.950799+00:00.  

```text
RN   [1] {ECO:0000312|EMBL:URS65384.1}
RP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, MUTAGENESIS OF VAL-112; CYS-205;
RP   VAL-208; SER-212 AND PHE-372, CATALYTIC ACTIVITY, PATHWAY, AND
RP   BIOPHYSICOCHEMICAL PROPERTIES.
RX   PubMed=36349266; DOI=10.1039/d2sc03612f;
RA   Wang Z., Xiao Y., Wu S., Chen J., Li A., Tatsis E.C.;
RT   "Deciphering and reprogramming the cyclization regioselectivity in
RT   bifurcation of indole alkaloid biosynthesis.";
RL   Chem. Sci. 13:12389-12395(2022).
```

Source SHA-256: `15ff37b3545781cd88f01534156171f4c96185b4b173d077dc54ff75075b22b3`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9E7S4M3?format=txt&versions=13)  
**Locator:** `lines 67-67`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 13 / 1.  
**Retrieved:** 2026-11-01T06:27:36.950799+00:00.  

```text
CC   -!- PATHWAY: Alkaloid biosynthesis. {ECO:0000269|PubMed:36349266}.
```

Source SHA-256: `15ff37b3545781cd88f01534156171f4c96185b4b173d077dc54ff75075b22b3`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 169. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
