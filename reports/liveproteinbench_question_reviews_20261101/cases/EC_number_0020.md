# EC_number_0020

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **A** — 1.14.14.187

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
A. 1.14.14.187
B. 1.14.14.154
C. 3.6.1.74
D. 1.14.14.104
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzyme Commission (EC) Number Prediction, which is to predict the complete 4-digit Enzyme Commission (EC) number for a given protein. The EC number is a numerical classification that categorizes enzymes based on the chemical reactions they catalyze. You should select the most accurate EC number from the provided options based on the protein's sequence.. The inputs provided by the user for this task include:

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

> The exact sequence matches the UniProt entry annotated as rhazimal synthase, EC 1.14.14.187. That entry cites experimental evidence for the reaction producing rhazimal, supporting choice A. This supports the key based on the protein-specific annotation and cited evidence, not on sequence-only deductions.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is consistent with a membrane-associated cytochrome P450 oxygenase, which provides broad functional-class information but does not identify the particular substrate or reaction distinguishing the P450 choices.


**Missing item-specific fact**

> The protein's experimentally established catalytic reaction—geissoschizine conversion to rhazimal, rather than a different P450-catalyzed reaction—is not provided in the question.


**Reason**

> Choosing the complete EC number requires protein-specific catalytic specificity absent from the sequence prompt. Recognizing the sequence or retrieving its functional annotation would supply that fact, but would be lookup or memorization rather than reasoning from the supplied input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B",
  "D"
]
```

> The sequence supports a broad P450-like assignment but does not, from the information supplied, distinguish among the listed P450 EC numbers. The protein-specific evidence supports A, but that evidence is not included in the original question.


### Important caveats

- The reviewer-only UniProt record and its cited experimental evidence match the supplied sequence; they were not available to the evaluated model.
- The source annotation also assigns the protein EC 1.14.19.80 for a second catalytic activity, which is not among the answer choices.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a membrane-associated cytochrome P450 oxygenase, which provides broad functional-class information but does not identify the particular substrate or reaction distinguishing the P450 choices.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's experimentally established catalytic reaction—geissoschizine conversion to rhazimal, rather than a different P450-catalyzed reaction—is not provided in the question.",
    "reason": "Choosing the complete EC number requires protein-specific catalytic specificity absent from the sequence prompt. Recognizing the sequence or retrieving its functional annotation would supply that fact, but would be lookup or memorization rather than reasoning from the supplied input."
  },
  "case_id": "EC_number_0020",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C7"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry annotated as rhazimal synthase, EC 1.14.14.187. That entry cites experimental evidence for the reaction producing rhazimal, supporting choice A. This supports the key based on the protein-specific annotation and cited evidence, not on sequence-only deductions."
  },
  "important_caveats": [
    "The reviewer-only UniProt record and its cited experimental evidence match the supplied sequence; they were not available to the evaluated model.",
    "The source annotation also assigns the protein EC 1.14.19.80 for a second catalytic activity, which is not among the answer choices."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B",
      "D"
    ],
    "reason": "The sequence supports a broad P450-like assignment but does not, from the information supplied, distinguish among the listed P450 EC numbers. The protein-specific evidence supports A, but that evidence is not included in the original question."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0020",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry annotated as rhazimal synthase, EC 1.14.14.187. That entry cites experimental evidence for the reaction producing rhazimal, supporting choice A. This supports the key based on the protein-specific annotation and cited evidence, not on sequence-only deductions.",
    "evidence_ids": ["C1", "C4", "C5", "C7"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is consistent with a membrane-associated cytochrome P450 oxygenase, which provides broad functional-class information but does not identify the particular substrate or reaction distinguishing the P450 choices.",
    "missing_item_specific_fact": "The protein's experimentally established catalytic reaction—geissoschizine conversion to rhazimal, rather than a different P450-catalyzed reaction—is not provided in the question.",
    "reason": "Choosing the complete EC number requires protein-specific catalytic specificity absent from the sequence prompt. Recognizing the sequence or retrieving its functional annotation would supply that fact, but would be lookup or memorization rather than reasoning from the supplied input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B", "D"],
    "reason": "The sequence supports a broad P450-like assignment but does not, from the information supplied, distinguish among the listed P450 EC numbers. The protein-specific evidence supports A, but that evidence is not included in the original question."
  },
  "important_caveats": [
    "The reviewer-only UniProt record and its cited experimental evidence match the supplied sequence; they were not available to the evaluated model.",
    "The source annotation also assigns the protein EC 1.14.19.80 for a second catalytic activity, which is not among the answer choices."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A9E7S4M3 (Rhazimal synthase, AsRHS) from Alstonia scholaris assigns EC 1.14.14.187 as the recommended EC number with evidence code ECO:0000269 (inferred from direct assay, PubMed:36349266). The catalytic reaction is (19E)-geissoschizine + reduced NADPH-hemoprotein reductase + O2 → rhazimal + oxidized reductase + 2 H2O + H+. The sequence SHA256 matches exactly. The protein also carries EC 1.14.19.80 as an alternative name, but that number is not among the choices. Among the four options, only 1.14.14.187 matches the UniProt-annotated primary EC number.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [H1](#evidence-h1), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains the canonical P450 heme-binding motif (FGTGRRGC with the invariant Cys ligand), which identifies the protein as a cytochrome P450 monooxygenase (EC class 1.14.14.x). This reasoning eliminates choice C (3.6.1.74, a nucleotidase/hydrolase). However, choices A (1.14.14.187), B (1.14.14.154), and D (1.14.14.104) are all P450 monooxygenases differing only in their 4th-digit substrate specificity. Distinguishing among them requires knowing the exact substrate (geissoschizine → rhazimal for .187) and the specific active-site residues that confer that selectivity—information not derivable from general sequence features without a structural model or database comparison.


**Missing item-specific fact**

> The specific substrate specificity of this P450 (i.e., that it converts (19E)-geissoschizine to rhazimal rather than to other monoterpene indole alkaloid intermediates targeted by EC 1.14.14.154 or 1.14.14.104) is an experimentally determined, protein-specific fact not encoded in the sequence in a way accessible through general biological reasoning.


**Reason**

> While P450 identification from the heme-binding motif is a valid reasoning step that eliminates the hydrolase distractor, the final discrimination among three P450 EC numbers (1.14.14.187 vs .154 vs .104) depends entirely on knowing the specific substrate-product pair, which is an item-specific experimental annotation absent from the input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The protein also carries EC 1.14.19.80 as an alternative EC number (geissoschizine → akuammicine + formate), but that number does not appear among the four choices, so it does not create ambiguity within the given option set. Among A, B, C, D, only A is supported by UniProt.


### Important caveats

- The UniProt annotation for EC 1.14.14.187 is based on experimental evidence (ECO:0000269, PubMed:36349266, Wang et al. 2022, Chem. Sci.), not purely computational inference.
- The protein is bifunctional (EC 1.14.14.187 and EC 1.14.19.80); the question's phrasing 'the complete 4-digit EC number' is slightly imprecise for a multi-EC enzyme, but the recommended name EC is 1.14.14.187.
- The organism (Alstonia scholaris) and pathway context (monoterpene indole alkaloid biosynthesis) are not provided in the question input, further limiting reasoning-based discrimination among P450 subclasses.
- The historical UniProt entry (version 13, Swiss-Prot, first released 2026-01) confirms the annotation predates the benchmark cutoff of 2026-05-07.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the canonical P450 heme-binding motif (FGTGRRGC with the invariant Cys ligand), which identifies the protein as a cytochrome P450 monooxygenase (EC class 1.14.14.x). This reasoning eliminates choice C (3.6.1.74, a nucleotidase/hydrolase). However, choices A (1.14.14.187), B (1.14.14.154), and D (1.14.14.104) are all P450 monooxygenases differing only in their 4th-digit substrate specificity. Distinguishing among them requires knowing the exact substrate (geissoschizine → rhazimal for .187) and the specific active-site residues that confer that selectivity—information not derivable from general sequence features without a structural model or database comparison.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific substrate specificity of this P450 (i.e., that it converts (19E)-geissoschizine to rhazimal rather than to other monoterpene indole alkaloid intermediates targeted by EC 1.14.14.154 or 1.14.14.104) is an experimentally determined, protein-specific fact not encoded in the sequence in a way accessible through general biological reasoning.",
    "reason": "While P450 identification from the heme-binding motif is a valid reasoning step that eliminates the hydrolase distractor, the final discrimination among three P450 EC numbers (1.14.14.187 vs .154 vs .104) depends entirely on knowing the specific substrate-product pair, which is an item-specific experimental annotation absent from the input."
  },
  "case_id": "EC_number_0020",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C7",
      "H1",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A9E7S4M3 (Rhazimal synthase, AsRHS) from Alstonia scholaris assigns EC 1.14.14.187 as the recommended EC number with evidence code ECO:0000269 (inferred from direct assay, PubMed:36349266). The catalytic reaction is (19E)-geissoschizine + reduced NADPH-hemoprotein reductase + O2 → rhazimal + oxidized reductase + 2 H2O + H+. The sequence SHA256 matches exactly. The protein also carries EC 1.14.19.80 as an alternative name, but that number is not among the choices. Among the four options, only 1.14.14.187 matches the UniProt-annotated primary EC number."
  },
  "important_caveats": [
    "The UniProt annotation for EC 1.14.14.187 is based on experimental evidence (ECO:0000269, PubMed:36349266, Wang et al. 2022, Chem. Sci.), not purely computational inference.",
    "The protein is bifunctional (EC 1.14.14.187 and EC 1.14.19.80); the question's phrasing 'the complete 4-digit EC number' is slightly imprecise for a multi-EC enzyme, but the recommended name EC is 1.14.14.187.",
    "The organism (Alstonia scholaris) and pathway context (monoterpene indole alkaloid biosynthesis) are not provided in the question input, further limiting reasoning-based discrimination among P450 subclasses.",
    "The historical UniProt entry (version 13, Swiss-Prot, first released 2026-01) confirms the annotation predates the benchmark cutoff of 2026-05-07."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein also carries EC 1.14.19.80 as an alternative EC number (geissoschizine → akuammicine + formate), but that number does not appear among the four choices, so it does not create ambiguity within the given option set. Among A, B, C, D, only A is supported by UniProt."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0020",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A9E7S4M3 (Rhazimal synthase, AsRHS) from Alstonia scholaris assigns EC 1.14.14.187 as the recommended EC number with evidence code ECO:0000269 (inferred from direct assay, PubMed:36349266). The catalytic reaction is (19E)-geissoschizine + reduced NADPH-hemoprotein reductase + O2 → rhazimal + oxidized reductase + 2 H2O + H+. The sequence SHA256 matches exactly. The protein also carries EC 1.14.19.80 as an alternative name, but that number is not among the choices. Among the four options, only 1.14.14.187 matches the UniProt-annotated primary EC number.",
    "evidence_ids": ["C4", "C5", "C7", "H1", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains the canonical P450 heme-binding motif (FGTGRRGC with the invariant Cys ligand), which identifies the protein as a cytochrome P450 monooxygenase (EC class 1.14.14.x). This reasoning eliminates choice C (3.6.1.74, a nucleotidase/hydrolase). However, choices A (1.14.14.187), B (1.14.14.154), and D (1.14.14.104) are all P450 monooxygenases differing only in their 4th-digit substrate specificity. Distinguishing among them requires knowing the exact substrate (geissoschizine → rhazimal for .187) and the specific active-site residues that confer that selectivity—information not derivable from general sequence features without a structural model or database comparison.",
    "missing_item_specific_fact": "The specific substrate specificity of this P450 (i.e., that it converts (19E)-geissoschizine to rhazimal rather than to other monoterpene indole alkaloid intermediates targeted by EC 1.14.14.154 or 1.14.14.104) is an experimentally determined, protein-specific fact not encoded in the sequence in a way accessible through general biological reasoning.",
    "reason": "While P450 identification from the heme-binding motif is a valid reasoning step that eliminates the hydrolase distractor, the final discrimination among three P450 EC numbers (1.14.14.187 vs .154 vs .104) depends entirely on knowing the specific substrate-product pair, which is an item-specific experimental annotation absent from the input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein also carries EC 1.14.19.80 as an alternative EC number (geissoschizine → akuammicine + formate), but that number does not appear among the four choices, so it does not create ambiguity within the given option set. Among A, B, C, D, only A is supported by UniProt."
  },
  "important_caveats": [
    "The UniProt annotation for EC 1.14.14.187 is based on experimental evidence (ECO:0000269, PubMed:36349266, Wang et al. 2022, Chem. Sci.), not purely computational inference.",
    "The protein is bifunctional (EC 1.14.14.187 and EC 1.14.19.80); the question's phrasing 'the complete 4-digit EC number' is slightly imprecise for a multi-EC enzyme, but the recommended name EC is 1.14.14.187.",
    "The organism (Alstonia scholaris) and pathway context (monoterpene indole alkaloid biosynthesis) are not provided in the question input, further limiting reasoning-based discrimination among P450 subclasses.",
    "The historical UniProt entry (version 13, Swiss-Prot, first released 2026-01) confirms the annotation predates the benchmark cutoff of 2026-05-07."
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

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7S4M3.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:52.188259+00:00.  

```json
"A0A9E7S4M3"
```

Source SHA-256: `c1fd8e022ffe05c9bfa24ba7a6386335a6a1b24a47d508aaaf7d09452928adf5`.

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
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:52.188259+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"36349266","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:79620"}}],"reaction":{"ecNumber":"1.14.14.187","evidences":[{"evidenceCode":"ECO:0000269","id":"36349266","source":"PubMed"}],"name":"(19E)-geissoschizine + reduced [NADPH--hemoprotein reductase] + O2 = rhazimal + oxidized [NADPH--hemoprotein reductase] + 2 H2O + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:79619"},{"database":"Rhea","id":"RHEA-COMP:11964"},{"database":"Rhea","id":"RHEA-COMP:11965"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:15379"},{"database":"ChEBI","id":"CHEBI:17037"},{"database":"ChEBI","id":"CHEBI:57618"},{"database":"ChEBI","id":"CHEBI:58210"},{"database":"ChEBI","id":"CHEBI:230473"}]}}
```

Source SHA-256: `c1fd8e022ffe05c9bfa24ba7a6386335a6a1b24a47d508aaaf7d09452928adf5`.

### Evidence C7

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
**Locator:** `lines 6-11`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 13 / 1.  
**Retrieved:** 2026-11-01T06:27:36.950799+00:00.  

```text
DE   RecName: Full=Rhazimal synthase {ECO:0000303|PubMed:36349266};
DE            Short=AsRHS {ECO:0000303|PubMed:36349266};
DE            EC=1.14.14.187 {ECO:0000269|PubMed:36349266};
DE   AltName: Full=Cytochrome P450 RHS {ECO:0000303|PubMed:36349266};
DE   AltName: Full=Geissoschizine oxidase RHS {ECO:0000303|PubMed:36349266};
DE            EC=1.14.19.80 {ECO:0000269|PubMed:36349266};
```

Source SHA-256: `15ff37b3545781cd88f01534156171f4c96185b4b173d077dc54ff75075b22b3`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9E7S4M3?format=txt&versions=13)  
**Locator:** `lines 36-45`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 13 / 1.  
**Retrieved:** 2026-11-01T06:27:36.950799+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=(19E)-geissoschizine + reduced [NADPH--hemoprotein reductase]
CC         + O2 = rhazimal + oxidized [NADPH--hemoprotein reductase] + 2 H2O +
CC         H(+); Xref=Rhea:RHEA:79619, Rhea:RHEA-COMP:11964, Rhea:RHEA-
CC         COMP:11965, ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:15379,
CC         ChEBI:CHEBI:17037, ChEBI:CHEBI:57618, ChEBI:CHEBI:58210,
CC         ChEBI:CHEBI:230473; EC=1.14.14.187;
CC         Evidence={ECO:0000269|PubMed:36349266};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:79620;
CC         Evidence={ECO:0000269|PubMed:36349266};
```

Source SHA-256: `15ff37b3545781cd88f01534156171f4c96185b4b173d077dc54ff75075b22b3`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 20. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
