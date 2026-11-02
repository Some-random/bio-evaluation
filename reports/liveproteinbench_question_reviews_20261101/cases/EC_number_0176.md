# EC_number_0176

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **A** — 1.14.19.80

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
A. 1.14.19.80
B. 1.14.15.9
C. 2.1.1.27
D. 4.1.1.25
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

> The exact sequence matches the UniProt entry annotated as geissoschizine oxidase, EC 1.14.19.80. Its catalytic reaction and EC assignment cite experimental evidence (ECO:0000269) from a publication, supporting choice A for this protein.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal hydrophobic segment and sequence features are consistent with a membrane-associated cytochrome P450, which can help distinguish an oxygenase from the methyltransferase and lyase distractors. They do not establish this enzyme's specific substrate reaction or distinguish the two oxygenase EC choices.


**Missing item-specific fact**

> The protein-specific catalytic activity—oxidation of (19E)-geissoschizine to akuammicine—and its associated EC assignment are not provided in the input.


**Reason**

> General sequence knowledge may narrow the enzyme class, but selecting the complete EC number requires the substrate specificity and reaction assignment, an item-specific fact absent from the question.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The matched sequence has a literature-supported EC assignment corresponding to choice A; the evidence identifies no competing listed EC number for this protein.


### Important caveats

- The experimental-support conclusion relies on reviewer-only UniProt evidence linked to a cited publication; the primary paper was not independently retrieved or validated here.
- The source snapshot used by the question author is unknown, although the sequence matches both the archived and current records.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic segment and sequence features are consistent with a membrane-associated cytochrome P450, which can help distinguish an oxygenase from the methyltransferase and lyase distractors. They do not establish this enzyme's specific substrate reaction or distinguish the two oxygenase EC choices.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific catalytic activity—oxidation of (19E)-geissoschizine to akuammicine—and its associated EC assignment are not provided in the input.",
    "reason": "General sequence knowledge may narrow the enzyme class, but selecting the complete EC number requires the substrate specificity and reaction assignment, an item-specific fact absent from the question."
  },
  "case_id": "EC_number_0176",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H1",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry annotated as geissoschizine oxidase, EC 1.14.19.80. Its catalytic reaction and EC assignment cite experimental evidence (ECO:0000269) from a publication, supporting choice A for this protein."
  },
  "important_caveats": [
    "The experimental-support conclusion relies on reviewer-only UniProt evidence linked to a cited publication; the primary paper was not independently retrieved or validated here.",
    "The source snapshot used by the question author is unknown, although the sequence matches both the archived and current records."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched sequence has a literature-supported EC assignment corresponding to choice A; the evidence identifies no competing listed EC number for this protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0176",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry annotated as geissoschizine oxidase, EC 1.14.19.80. Its catalytic reaction and EC assignment cite experimental evidence (ECO:0000269) from a publication, supporting choice A for this protein.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal hydrophobic segment and sequence features are consistent with a membrane-associated cytochrome P450, which can help distinguish an oxygenase from the methyltransferase and lyase distractors. They do not establish this enzyme's specific substrate reaction or distinguish the two oxygenase EC choices.",
    "missing_item_specific_fact": "The protein-specific catalytic activity—oxidation of (19E)-geissoschizine to akuammicine—and its associated EC assignment are not provided in the input.",
    "reason": "General sequence knowledge may narrow the enzyme class, but selecting the complete EC number requires the substrate specificity and reaction assignment, an item-specific fact absent from the question."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched sequence has a literature-supported EC assignment corresponding to choice A; the evidence identifies no competing listed EC number for this protein."
  },
  "important_caveats": [
    "The experimental-support conclusion relies on reviewer-only UniProt evidence linked to a cited publication; the primary paper was not independently retrieved or validated here.",
    "The source snapshot used by the question author is unknown, although the sequence matches both the archived and current records."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The supplied sequence matches UniProt entry A0A9E7S4M4 (Geissoschizine oxidase, AsGO) from Alstonia scholaris. The EC number 1.14.19.80 is assigned with experimental evidence (ECO:0000269, PubMed:36349266). The catalytic activity (geissoschizine → akuammicine + formate) confirms the P450 oxidase classification. The sequence comparison is 'matched' in both current and historical (v13) UniProt records.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the highly conserved cytochrome P450 heme-binding motif FGTGRRGCPG (FxxGxxxCxG pattern), identifying this as a heme-containing P450 monooxygenase. Among the four choices: (C) 2.1.1.27 is a methyltransferase (EC class 2), (D) 4.1.1.25 is a decarboxylase (EC class 4), and (B) 1.14.15.9 belongs to the copper-dependent monooxygenase subclass (1.14.15.-, requiring copper as a cofactor, not heme). Only (A) 1.14.19.80 falls in the 1.14.19.- subclass (NADPH-dependent P450 with single oxygen atom incorporation), consistent with the heme-binding motif. Thus, recognizing the P450 signature and the EC class hierarchy eliminates three of four options.


**Missing item-specific fact**

> The specific substrate (geissoschizine) and product (akuammicine) that define EC 1.14.19.80 versus other P450 EC numbers cannot be determined from sequence alone. However, since only one P450 option is presented among the four choices, the heme-motif identification suffices to select the correct answer.


**Reason**

> A model with general knowledge of the P450 heme-binding motif and the EC classification hierarchy can eliminate the transferase, lyase, and copper-monooxygenase options, leaving the P450 EC number. This is a concrete biological argument from the sequence, not mere database lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices span three different EC main classes (oxidoreductase, transferase, lyase) and two different oxidoreductase subclasses (heme-P450 vs. copper-dependent). The P450 heme-binding motif unambiguously selects option A over B, C, and D.


### Important caveats

- The EC assignment is based on experimental evidence (ECO:0000269) from Wang et al. 2022, Chem. Sci. 13:12389-12395.
- While the P450 motif distinguishes A from B/C/D among these choices, the specific 4th digit (.80) encoding geissoschizine oxidase activity cannot be derived from sequence alone; it requires knowledge of the specific substrate/product pair.
- The UniProt entry was first public on 2025-06-18; the author's source snapshot date is unknown, so the annotation may not have been available when the benchmark was constructed.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the highly conserved cytochrome P450 heme-binding motif FGTGRRGCPG (FxxGxxxCxG pattern), identifying this as a heme-containing P450 monooxygenase. Among the four choices: (C) 2.1.1.27 is a methyltransferase (EC class 2), (D) 4.1.1.25 is a decarboxylase (EC class 4), and (B) 1.14.15.9 belongs to the copper-dependent monooxygenase subclass (1.14.15.-, requiring copper as a cofactor, not heme). Only (A) 1.14.19.80 falls in the 1.14.19.- subclass (NADPH-dependent P450 with single oxygen atom incorporation), consistent with the heme-binding motif. Thus, recognizing the P450 signature and the EC class hierarchy eliminates three of four options.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The specific substrate (geissoschizine) and product (akuammicine) that define EC 1.14.19.80 versus other P450 EC numbers cannot be determined from sequence alone. However, since only one P450 option is presented among the four choices, the heme-motif identification suffices to select the correct answer.",
    "reason": "A model with general knowledge of the P450 heme-binding motif and the EC classification hierarchy can eliminate the transferase, lyase, and copper-monooxygenase options, leaving the P450 EC number. This is a concrete biological argument from the sequence, not mere database lookup."
  },
  "case_id": "EC_number_0176",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence matches UniProt entry A0A9E7S4M4 (Geissoschizine oxidase, AsGO) from Alstonia scholaris. The EC number 1.14.19.80 is assigned with experimental evidence (ECO:0000269, PubMed:36349266). The catalytic activity (geissoschizine → akuammicine + formate) confirms the P450 oxidase classification. The sequence comparison is 'matched' in both current and historical (v13) UniProt records."
  },
  "important_caveats": [
    "The EC assignment is based on experimental evidence (ECO:0000269) from Wang et al. 2022, Chem. Sci. 13:12389-12395.",
    "While the P450 motif distinguishes A from B/C/D among these choices, the specific 4th digit (.80) encoding geissoschizine oxidase activity cannot be derived from sequence alone; it requires knowledge of the specific substrate/product pair.",
    "The UniProt entry was first public on 2025-06-18; the author's source snapshot date is unknown, so the annotation may not have been available when the benchmark was constructed."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices span three different EC main classes (oxidoreductase, transferase, lyase) and two different oxidoreductase subclasses (heme-P450 vs. copper-dependent). The P450 heme-binding motif unambiguously selects option A over B, C, and D."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0176",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence matches UniProt entry A0A9E7S4M4 (Geissoschizine oxidase, AsGO) from Alstonia scholaris. The EC number 1.14.19.80 is assigned with experimental evidence (ECO:0000269, PubMed:36349266). The catalytic activity (geissoschizine → akuammicine + formate) confirms the P450 oxidase classification. The sequence comparison is 'matched' in both current and historical (v13) UniProt records.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the highly conserved cytochrome P450 heme-binding motif FGTGRRGCPG (FxxGxxxCxG pattern), identifying this as a heme-containing P450 monooxygenase. Among the four choices: (C) 2.1.1.27 is a methyltransferase (EC class 2), (D) 4.1.1.25 is a decarboxylase (EC class 4), and (B) 1.14.15.9 belongs to the copper-dependent monooxygenase subclass (1.14.15.-, requiring copper as a cofactor, not heme). Only (A) 1.14.19.80 falls in the 1.14.19.- subclass (NADPH-dependent P450 with single oxygen atom incorporation), consistent with the heme-binding motif. Thus, recognizing the P450 signature and the EC class hierarchy eliminates three of four options.",
    "missing_item_specific_fact": "The specific substrate (geissoschizine) and product (akuammicine) that define EC 1.14.19.80 versus other P450 EC numbers cannot be determined from sequence alone. However, since only one P450 option is presented among the four choices, the heme-motif identification suffices to select the correct answer.",
    "reason": "A model with general knowledge of the P450 heme-binding motif and the EC classification hierarchy can eliminate the transferase, lyase, and copper-monooxygenase options, leaving the P450 EC number. This is a concrete biological argument from the sequence, not mere database lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices span three different EC main classes (oxidoreductase, transferase, lyase) and two different oxidoreductase subclasses (heme-P450 vs. copper-dependent). The P450 heme-binding motif unambiguously selects option A over B, C, and D."
  },
  "important_caveats": [
    "The EC assignment is based on experimental evidence (ECO:0000269) from Wang et al. 2022, Chem. Sci. 13:12389-12395.",
    "While the P450 motif distinguishes A from B/C/D among these choices, the specific 4th digit (.80) encoding geissoschizine oxidase activity cannot be derived from sequence alone; it requires knowledge of the specific substrate/product pair.",
    "The UniProt entry was first public on 2025-06-18; the author's source snapshot date is unknown, so the annotation may not have been available when the benchmark was constructed."
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
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:10.590145+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"36349266","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:58521"}}],"reaction":{"ecNumber":"1.14.19.80","evidences":[{"evidenceCode":"ECO:0000269","id":"36349266","source":"PubMed"}],"name":"(19E)-geissoschizine + reduced [NADPH--hemoprotein reductase] + O2 = akuammicine + formate + oxidized [NADPH--hemoprotein reductase] + H2O + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:58520"},{"database":"Rhea","id":"RHEA-COMP:11964"},{"database":"Rhea","id":"RHEA-COMP:11965"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:15379"},{"database":"ChEBI","id":"CHEBI:15740"},{"database":"ChEBI","id":"CHEBI:17037"},{"database":"ChEBI","id":"CHEBI:57618"},{"database":"ChEBI","id":"CHEBI:58210"},{"database":"ChEBI","id":"CHEBI:142754"}]}}
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
**Locator:** `lines 6-9`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 13 / 1.  
**Retrieved:** 2026-11-02T04:26:14.830408+00:00.  

```text
DE   RecName: Full=Geissoschizine oxidase {ECO:0000303|PubMed:36349266};
DE            Short=AsGO {ECO:0000303|PubMed:36349266};
DE            EC=1.14.19.80 {ECO:0000269|PubMed:36349266};
DE   AltName: Full=Cytochrome P450 GO {ECO:0000303|PubMed:36349266};
```

Source SHA-256: `991588eea7e058afe44fddcc48282d5e07529aa26a2d5757e5dbab96577b2d25`.

### Evidence H3

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

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9E7S4M4?format=txt&versions=13)  
**Locator:** `lines 31-40`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 13 / 1.  
**Retrieved:** 2026-11-02T04:26:14.830408+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=(19E)-geissoschizine + reduced [NADPH--hemoprotein reductase]
CC         + O2 = akuammicine + formate + oxidized [NADPH--hemoprotein
CC         reductase] + H2O + H(+); Xref=Rhea:RHEA:58520, Rhea:RHEA-COMP:11964,
CC         Rhea:RHEA-COMP:11965, ChEBI:CHEBI:15377, ChEBI:CHEBI:15378,
CC         ChEBI:CHEBI:15379, ChEBI:CHEBI:15740, ChEBI:CHEBI:17037,
CC         ChEBI:CHEBI:57618, ChEBI:CHEBI:58210, ChEBI:CHEBI:142754;
CC         EC=1.14.19.80; Evidence={ECO:0000269|PubMed:36349266};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:58521;
CC         Evidence={ECO:0000269|PubMed:36349266};
```

Source SHA-256: `991588eea7e058afe44fddcc48282d5e07529aa26a2d5757e5dbab96577b2d25`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 176. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
