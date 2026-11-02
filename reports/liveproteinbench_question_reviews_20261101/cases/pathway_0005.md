# pathway_0005

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `pathway`  
**Author expected answer:** **D** — Alkaloid biosynthesis. .

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MEFSFSSPLLYILYFLLFFIVRQLLKPKSNRKLPPGPRTLPIIGNLHQLRGSLPHRTLKKLSDKHGPLMHLKMGERSAIIVSDARMAKIVLHNHGLAVADRSVNTVASIMTYNSLGVTFAQYGDYLTKLRQIYTLELLSPKKVRSFYNCFEDELDVFVKSIRSQVGQPMVLYEKVSTYLYATICRTIFGSVCKEREKMIKIVKRTSLLSGTPLRMEDLFPSMRVFCRFSKTLNQLRGLLQEMDGILEDIIVEREKTTEILKEAKDDEDMLSVLLRHKWYNPSGARFRITNADIKAIIFELILAATLSVADVVEWAMVEILRHPAILKKVYDEGRGICKEKKRVTGYDVEKMEYMRLCVKESTRVHPAAPLLVPRECREDFEVDGYTVPKGAWVLTNCWAIQMDPEIWPEPEKFDPERYIRNPMDFYGSNFELIPFGTGRRGCPGILYGVTNAELLLAAMFYHFDWEIADGKKPEDIDLTENFGAGCIMKYPLTLVPHLANE

[Multiple Choices]
A. capsule polysaccharide biosynthesis. .
B. chorismate from D-erythrose 4-phosphate and phosphoenolpyruvate: step 7/7. .
C. L-cystathionine from O-succinyl-L-homoserine: step 1/1. .
D. Alkaloid biosynthesis. .
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

> The sequence exactly matches the cited UniProt entry for geissoschizine oxidase, whose pathway annotation is alkaloid biosynthesis and is attributed to experimental evidence (ECO:0000269) in a cited publication. This supports choice D for this sequence, though the primary paper was not independently reviewed here.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Sequence features may suggest a membrane-associated cytochrome P450, which is compatible with oxidative metabolism, but that broad enzyme-family inference does not identify alkaloid biosynthesis over other possible P450 functions.


**Missing item-specific fact**

> The protein-specific identity and function as geissoschizine oxidase, including its role in alkaloid biosynthesis, are not supplied.


**Reason**

> Choosing the specific pathway requires protein-specific functional knowledge or annotation; recognizing a likely P450 fold does not establish its pathway.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The specific pathway is supported by the matched-sequence annotation, while the other choices are not comparably supported by the supplied sequence alone.


### Important caveats

- Reviewer-only database and publication information supports the key but was not available to the evaluated model.
- The exact author source snapshot is unknown; the sequence match is established for the cited current and historical UniProt records.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Sequence features may suggest a membrane-associated cytochrome P450, which is compatible with oxidative metabolism, but that broad enzyme-family inference does not identify alkaloid biosynthesis over other possible P450 functions.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identity and function as geissoschizine oxidase, including its role in alkaloid biosynthesis, are not supplied.",
    "reason": "Choosing the specific pathway requires protein-specific functional knowledge or annotation; recognizing a likely P450 fold does not establish its pathway."
  },
  "case_id": "pathway_0005",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence exactly matches the cited UniProt entry for geissoschizine oxidase, whose pathway annotation is alkaloid biosynthesis and is attributed to experimental evidence (ECO:0000269) in a cited publication. This supports choice D for this sequence, though the primary paper was not independently reviewed here."
  },
  "important_caveats": [
    "Reviewer-only database and publication information supports the key but was not available to the evaluated model.",
    "The exact author source snapshot is unknown; the sequence match is established for the cited current and historical UniProt records."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The specific pathway is supported by the matched-sequence annotation, while the other choices are not comparably supported by the supplied sequence alone."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0005",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence exactly matches the cited UniProt entry for geissoschizine oxidase, whose pathway annotation is alkaloid biosynthesis and is attributed to experimental evidence (ECO:0000269) in a cited publication. This supports choice D for this sequence, though the primary paper was not independently reviewed here.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Sequence features may suggest a membrane-associated cytochrome P450, which is compatible with oxidative metabolism, but that broad enzyme-family inference does not identify alkaloid biosynthesis over other possible P450 functions.",
    "missing_item_specific_fact": "The protein-specific identity and function as geissoschizine oxidase, including its role in alkaloid biosynthesis, are not supplied.",
    "reason": "Choosing the specific pathway requires protein-specific functional knowledge or annotation; recognizing a likely P450 fold does not establish its pathway."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The specific pathway is supported by the matched-sequence annotation, while the other choices are not comparably supported by the supplied sequence alone."
  },
  "important_caveats": [
    "Reviewer-only database and publication information supports the key but was not available to the evaluated model.",
    "The exact author source snapshot is unknown; the sequence match is established for the cited current and historical UniProt records."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt A0A9E7S4M4 (Geissoschizine oxidase, EC 1.14.19.80) from Alstonia scholaris. The UniProt PATHWAY annotation states 'Alkaloid biosynthesis' with experimental evidence code ECO:0000269 linked to PubMed:36349266 (Wang et al., Chem. Sci. 2022, 'Deciphering and reprogramming the cyclization regioselectivity in bifurcation of indole alkaloid biosynthesis'). The sequence SHA-256 matches in both current and historical (v13) snapshots.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the canonical cytochrome P450 heme-binding signature (FGSGRRGCPGILYG near the C-terminus) and ER-targeting signal peptide, identifying it as a plant microsomal P450. Among the four choices: (A) capsule polysaccharide biosynthesis is a bacterial pathway with no P450 involvement; (B) chorismate synthase (shikimate pathway step 7) is a flavin-dependent enzyme, structurally and mechanistically incompatible with a P450; (C) L-cystathionine from O-succinyl-L-homoserine is a PLP-dependent bacterial transaminase/synthase reaction. Only (D) alkaloid biosynthesis routinely employs cytochrome P450 enzymes as key oxidative steps. Thus, recognizing the enzyme class as a P450 and eliminating the three mechanistically incompatible distractors provides a general-knowledge route to D.


**Missing item-specific fact**

> Positive identification of this specific P450 as geissoschizine oxidase acting on the indole alkaloid geissoschizine requires substrate-level knowledge not derivable from the sequence alone. However, the question only asks to select among four options, and the elimination argument suffices.


**Reason**

> A model that recognizes the P450 fold and heme-binding motif can eliminate A (bacterial), B (flavin enzyme), and C (PLP enzyme) using general enzymology and pathway knowledge, leaving D as the only option consistent with a cytochrome P450. This is a concrete biological argument from the sequence and choices, not mere memorization of the UniProt entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The three distractors are mechanistically incompatible with a cytochrome P450 (bacterial polysaccharide synthesis, flavin-dependent chorismate synthase, PLP-dependent cystathionine synthase), leaving only D as a viable pathway for a P450. No other option is defensible given the enzyme class.


### Important caveats

- The reasoning support relies on elimination of clearly mismatched enzyme classes rather than positive identification of the alkaloid substrate; a model that fails to recognize the P450 signature would lack grounds to choose D.
- The UniProt annotation carries experimental evidence (ECO:0000269, PubMed:36349266), strengthening the key.
- The entry was first publicly released 2025-06-18 (Swiss-Prot 2026_01); the author's source snapshot date is unknown, so the annotation may not have existed at benchmark construction time.
- P450s participate in many plant secondary-metabolism pathways (terpenoid, phenylpropanoid, fatty acid); the question is answerable here only because the distractors are all non-P450 pathways.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the canonical cytochrome P450 heme-binding signature (FGSGRRGCPGILYG near the C-terminus) and ER-targeting signal peptide, identifying it as a plant microsomal P450. Among the four choices: (A) capsule polysaccharide biosynthesis is a bacterial pathway with no P450 involvement; (B) chorismate synthase (shikimate pathway step 7) is a flavin-dependent enzyme, structurally and mechanistically incompatible with a P450; (C) L-cystathionine from O-succinyl-L-homoserine is a PLP-dependent bacterial transaminase/synthase reaction. Only (D) alkaloid biosynthesis routinely employs cytochrome P450 enzymes as key oxidative steps. Thus, recognizing the enzyme class as a P450 and eliminating the three mechanistically incompatible distractors provides a general-knowledge route to D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Positive identification of this specific P450 as geissoschizine oxidase acting on the indole alkaloid geissoschizine requires substrate-level knowledge not derivable from the sequence alone. However, the question only asks to select among four options, and the elimination argument suffices.",
    "reason": "A model that recognizes the P450 fold and heme-binding motif can eliminate A (bacterial), B (flavin enzyme), and C (PLP enzyme) using general enzymology and pathway knowledge, leaving D as the only option consistent with a cytochrome P450. This is a concrete biological argument from the sequence and choices, not mere memorization of the UniProt entry."
  },
  "case_id": "pathway_0005",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt A0A9E7S4M4 (Geissoschizine oxidase, EC 1.14.19.80) from Alstonia scholaris. The UniProt PATHWAY annotation states 'Alkaloid biosynthesis' with experimental evidence code ECO:0000269 linked to PubMed:36349266 (Wang et al., Chem. Sci. 2022, 'Deciphering and reprogramming the cyclization regioselectivity in bifurcation of indole alkaloid biosynthesis'). The sequence SHA-256 matches in both current and historical (v13) snapshots."
  },
  "important_caveats": [
    "The reasoning support relies on elimination of clearly mismatched enzyme classes rather than positive identification of the alkaloid substrate; a model that fails to recognize the P450 signature would lack grounds to choose D.",
    "The UniProt annotation carries experimental evidence (ECO:0000269, PubMed:36349266), strengthening the key.",
    "The entry was first publicly released 2025-06-18 (Swiss-Prot 2026_01); the author's source snapshot date is unknown, so the annotation may not have existed at benchmark construction time.",
    "P450s participate in many plant secondary-metabolism pathways (terpenoid, phenylpropanoid, fatty acid); the question is answerable here only because the distractors are all non-P450 pathways."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors are mechanistically incompatible with a cytochrome P450 (bacterial polysaccharide synthesis, flavin-dependent chorismate synthase, PLP-dependent cystathionine synthase), leaving only D as a viable pathway for a P450. No other option is defensible given the enzyme class."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0005",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt A0A9E7S4M4 (Geissoschizine oxidase, EC 1.14.19.80) from Alstonia scholaris. The UniProt PATHWAY annotation states 'Alkaloid biosynthesis' with experimental evidence code ECO:0000269 linked to PubMed:36349266 (Wang et al., Chem. Sci. 2022, 'Deciphering and reprogramming the cyclization regioselectivity in bifurcation of indole alkaloid biosynthesis'). The sequence SHA-256 matches in both current and historical (v13) snapshots.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the canonical cytochrome P450 heme-binding signature (FGSGRRGCPGILYG near the C-terminus) and ER-targeting signal peptide, identifying it as a plant microsomal P450. Among the four choices: (A) capsule polysaccharide biosynthesis is a bacterial pathway with no P450 involvement; (B) chorismate synthase (shikimate pathway step 7) is a flavin-dependent enzyme, structurally and mechanistically incompatible with a P450; (C) L-cystathionine from O-succinyl-L-homoserine is a PLP-dependent bacterial transaminase/synthase reaction. Only (D) alkaloid biosynthesis routinely employs cytochrome P450 enzymes as key oxidative steps. Thus, recognizing the enzyme class as a P450 and eliminating the three mechanistically incompatible distractors provides a general-knowledge route to D.",
    "missing_item_specific_fact": "Positive identification of this specific P450 as geissoschizine oxidase acting on the indole alkaloid geissoschizine requires substrate-level knowledge not derivable from the sequence alone. However, the question only asks to select among four options, and the elimination argument suffices.",
    "reason": "A model that recognizes the P450 fold and heme-binding motif can eliminate A (bacterial), B (flavin enzyme), and C (PLP enzyme) using general enzymology and pathway knowledge, leaving D as the only option consistent with a cytochrome P450. This is a concrete biological argument from the sequence and choices, not mere memorization of the UniProt entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors are mechanistically incompatible with a cytochrome P450 (bacterial polysaccharide synthesis, flavin-dependent chorismate synthase, PLP-dependent cystathionine synthase), leaving only D as a viable pathway for a P450. No other option is defensible given the enzyme class."
  },
  "important_caveats": [
    "The reasoning support relies on elimination of clearly mismatched enzyme classes rather than positive identification of the alkaloid substrate; a model that fails to recognize the P450 signature would lack grounds to choose D.",
    "The UniProt annotation carries experimental evidence (ECO:0000269, PubMed:36349266), strengthening the key.",
    "The entry was first publicly released 2025-06-18 (Swiss-Prot 2026_01); the author's source snapshot date is unknown, so the annotation may not have existed at benchmark construction time.",
    "P450s participate in many plant secondary-metabolism pathways (terpenoid, phenylpropanoid, fatty acid); the question is answerable here only because the distractors are all non-P450 pathways."
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

**Accession:** `A0A9E7S4M4` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 13. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7S4M4.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:10.590145+00:00.  

```json
"A0A9E7S4M4"
```

Source SHA-256: `46ad776fdc05519a00fc1e3ad670aab0d6ffb16716259d92b4fdf67dfd72535d`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7S4M4.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:10.590145+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"36349266","source":"PubMed"}],"value":"Cytochrome P450 GO"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"36349266","source":"PubMed"}],"value":"1.14.19.80"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"36349266","source":"PubMed"}],"value":"Geissoschizine oxidase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"36349266","source":"PubMed"}],"value":"AsGO"}]}}
```

Source SHA-256: `46ad776fdc05519a00fc1e3ad670aab0d6ffb16716259d92b4fdf67dfd72535d`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7S4M4.json)  
**Locator:** `/comments/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:10.590145+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"36349266","source":"PubMed"}],"value":"Alkaloid biosynthesis"}]}
```

Source SHA-256: `46ad776fdc05519a00fc1e3ad670aab0d6ffb16716259d92b4fdf67dfd72535d`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7S4M4.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:10.590145+00:00.  

```json
{"citation":{"authors":["Wang Z.","Xiao Y.","Wu S.","Chen J.","Li A.","Tatsis E.C."],"citationCrossReferences":[{"database":"PubMed","id":"36349266"},{"database":"DOI","id":"10.1039/d2sc03612f"}],"citationType":"journal article","firstPage":"12389","id":"36349266","journal":"Chem. Sci.","lastPage":"12395","publicationDate":"2022","title":"Deciphering and reprogramming the cyclization regioselectivity in bifurcation of indole alkaloid biosynthesis.","volume":"13"},"evidences":[{"evidenceCode":"ECO:0000312","id":"URS65383.1","source":"EMBL"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [MRNA]","FUNCTION","MUTAGENESIS OF ILE-109; VAL-202; THR-205; SER-209 AND VAL-372","CATALYTIC ACTIVITY","PATHWAY","BIOPHYSICOCHEMICAL PROPERTIES"]}
```

Source SHA-256: `46ad776fdc05519a00fc1e3ad670aab0d6ffb16716259d92b4fdf67dfd72535d`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9E7S4M4?format=txt&versions=13)  
**Locator:** `lines 1-16`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 13 / 1.  
**Retrieved:** 2026-11-02T04:26:14.830408+00:00.  

```text
ID   GO_ALSSC                Reviewed;         501 AA.
AC   A0A9E7S4M4;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   03-MAY-2023, sequence version 1.
DT   28-JAN-2026, entry version 13.
DE   RecName: Full=Geissoschizine oxidase {ECO:0000303|PubMed:36349266};
DE            Short=AsGO {ECO:0000303|PubMed:36349266};
DE            EC=1.14.19.80 {ECO:0000269|PubMed:36349266};
DE   AltName: Full=Cytochrome P450 GO {ECO:0000303|PubMed:36349266};
GN   Name=GO {ECO:0000303|PubMed:36349266};
OS   Alstonia scholaris (Dogbane) (Echites scholaris).
OC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;
OC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;
OC   asterids; lamiids; Gentianales; Apocynaceae; Rauvolfioideae; Alstonieae;
OC   Alstonia.
OX   NCBI_TaxID=52822;
```

Source SHA-256: `991588eea7e058afe44fddcc48282d5e07529aa26a2d5757e5dbab96577b2d25`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9E7S4M4?format=txt&versions=13)  
**Locator:** `lines 17-25`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 13 / 1.  
**Retrieved:** 2026-11-02T04:26:14.830408+00:00.  

```text
RN   [1] {ECO:0000312|EMBL:URS65383.1}
RP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, MUTAGENESIS OF ILE-109; VAL-202;
RP   THR-205; SER-209 AND VAL-372, CATALYTIC ACTIVITY, PATHWAY, AND
RP   BIOPHYSICOCHEMICAL PROPERTIES.
RX   PubMed=36349266; DOI=10.1039/d2sc03612f;
RA   Wang Z., Xiao Y., Wu S., Chen J., Li A., Tatsis E.C.;
RT   "Deciphering and reprogramming the cyclization regioselectivity in
RT   bifurcation of indole alkaloid biosynthesis.";
RL   Chem. Sci. 13:12389-12395(2022).
```

Source SHA-256: `991588eea7e058afe44fddcc48282d5e07529aa26a2d5757e5dbab96577b2d25`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9E7S4M4?format=txt&versions=13)  
**Locator:** `lines 52-52`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 13 / 1.  
**Retrieved:** 2026-11-02T04:26:14.830408+00:00.  

```text
CC   -!- PATHWAY: Alkaloid biosynthesis. {ECO:0000269|PubMed:36349266}.
```

Source SHA-256: `991588eea7e058afe44fddcc48282d5e07529aa26a2d5757e5dbab96577b2d25`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 5. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
