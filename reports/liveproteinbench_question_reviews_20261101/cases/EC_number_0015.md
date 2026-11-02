# EC_number_0015

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **B** — 3.2.1.8

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MVSFKSLLLAASAFTAVLGRPFDSFDGPDVNITDADELLVRRQVTANSEGTHNGYFYSWWSDGGGQVTYTMGAGSRYSVTWKDTGNFVGGKGWNPGTGRTINYGGSFSPQGNGYLAVYGWTRNPLIEYYVVESYGTYNPGSGGQLKGTVTTDGGTYNVYVSTRTNQPSIDGTRTFQQYWSVRTSKRVGGAVTMQNHFNAWAQFGMNLGAHYYQIVATEGNGDFVGTEIWGLARGCRR

[Multiple Choices]
A. 3.2.1.20
B. 3.2.1.8
C. 2.1.1.353
D. 1.14.13.238
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

> The supplied sequence exactly matches a historical UniProtKB/Swiss-Prot record annotated as EC 3.2.1.8, endo-1,4-beta-xylanase. The cited EC assignment is computationally supported by a PROSITE rule, rather than established by the excerpts as a direct experimental assay.

Citations as saved: [H1](#evidence-h1), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal hydrophobic signal-peptide-like region and the subsequent compact, aromatic-rich sequence are consistent with a secreted fungal glycoside hydrolase. Its sequence pattern is consistent with a GH11-like endo-xylanase, which supports EC 3.2.1.8 over the alpha-glucosidase, methyltransferase, and oxidase choices.


**Missing item-specific fact**

> A direct activity assay or a protein-specific annotation would confirm the exact substrate specificity, but is not necessary for a defensible sequence-family-based choice among these options.


**Reason**

> The sequence offers a biologically meaningful family-level basis for selecting the xylanase option; this does not depend solely on recognizing the exact sequence or recalling its database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence supports a secreted xylanase interpretation, while the other options describe substantially different catalytic activities.


### Important caveats

- The sequence match is to a historical UniProtKB record; the current record's sequence differs.
- The matched record's EC assignment is supported by a computational PROSITE rule in the cited excerpts; those excerpts do not independently establish experimental validation.
- The author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic signal-peptide-like region and the subsequent compact, aromatic-rich sequence are consistent with a secreted fungal glycoside hydrolase. Its sequence pattern is consistent with a GH11-like endo-xylanase, which supports EC 3.2.1.8 over the alpha-glucosidase, methyltransferase, and oxidase choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "A direct activity assay or a protein-specific annotation would confirm the exact substrate specificity, but is not necessary for a defensible sequence-family-based choice among these options.",
    "reason": "The sequence offers a biologically meaningful family-level basis for selecting the xylanase option; this does not depend solely on recognizing the exact sequence or recalling its database entry."
  },
  "case_id": "EC_number_0015",
  "expected_answer_check": {
    "evidence_ids": [
      "H1",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches a historical UniProtKB/Swiss-Prot record annotated as EC 3.2.1.8, endo-1,4-beta-xylanase. The cited EC assignment is computationally supported by a PROSITE rule, rather than established by the excerpts as a direct experimental assay."
  },
  "important_caveats": [
    "The sequence match is to a historical UniProtKB record; the current record's sequence differs.",
    "The matched record's EC assignment is supported by a computational PROSITE rule in the cited excerpts; those excerpts do not independently establish experimental validation.",
    "The author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence supports a secreted xylanase interpretation, while the other options describe substantially different catalytic activities."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0015",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches a historical UniProtKB/Swiss-Prot record annotated as EC 3.2.1.8, endo-1,4-beta-xylanase. The cited EC assignment is computationally supported by a PROSITE rule, rather than established by the excerpts as a direct experimental assay.",
    "evidence_ids": ["H1", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal hydrophobic signal-peptide-like region and the subsequent compact, aromatic-rich sequence are consistent with a secreted fungal glycoside hydrolase. Its sequence pattern is consistent with a GH11-like endo-xylanase, which supports EC 3.2.1.8 over the alpha-glucosidase, methyltransferase, and oxidase choices.",
    "missing_item_specific_fact": "A direct activity assay or a protein-specific annotation would confirm the exact substrate specificity, but is not necessary for a defensible sequence-family-based choice among these options.",
    "reason": "The sequence offers a biologically meaningful family-level basis for selecting the xylanase option; this does not depend solely on recognizing the exact sequence or recalling its database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence supports a secreted xylanase interpretation, while the other options describe substantially different catalytic activities."
  },
  "important_caveats": [
    "The sequence match is to a historical UniProtKB record; the current record's sequence differs.",
    "The matched record's EC assignment is supported by a computational PROSITE rule in the cited excerpts; those excerpts do not independently establish experimental validation.",
    "The author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The supplied 237-AA sequence exactly matches UniProt entry G2X0L1 (EIX2_VERDV, sequence_version 1, historical entry version 60). That entry annotates EC 3.2.1.8 (Endohydrolysis of (1→4)-β-D-xylosidic linkages in xylans) with evidence code ECO:0000255|PROSITE-ProRule:PRU01097, a computational pattern-match inference for Glycoside Hydrolase family 11. The protein is named 'Ethylene-inducing xylanase 2' from Verticillium dahliae. The EC assignment is thus supported by the matching database record, though the evidence is computational (PROSITE-ProRule), not direct experimental measurement of xylanase activity on this specific protein.

Citations as saved: [H1](#evidence-h1), [H2](#evidence-h2), [H4](#evidence-h4), [C4](#evidence-c4), [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> A multi-step reasoning chain is available from the sequence itself: (1) The sequence lacks Rossmann-fold / SAM-binding motifs expected of methyltransferases (EC 2.1.1.x) and lacks heme-binding (FxxGxxxCxG) or flavin-binding motifs expected of monooxygenases (EC 1.14.13.x), eliminating C and D. (2) The sequence contains motifs characteristic of glycoside hydrolases (e.g., 'ITD' near position 30, a β-jelly-roll-like arrangement of conserved aromatic/glycine-rich stretches such as 'GGGQVTYTMGAGSRYSVTWKDTGNFVGGKGWNPGTGRTINYGGSFSPQGNGYLAVYGWTRNPLIEYY'), narrowing to the 3.2.1.x glycosidase class. (3) The small mature size (~210 AA after signal peptide cleavage) and the GH11-specific PROSITE-ProRule PRU01097 signature (ITD catalytic nucleophile motif, YNT/related catalytic acid motif, β-jelly roll topology) are hallmarks of GH11 endo-β-xylanases (EC 3.2.1.8), whereas GH67 α-glucuronidases (EC 3.2.1.20) are typically 400–500 AA with an entirely different α/β-sandwich fold. This size and fold distinction meaningfully separates A from B.


**Missing item-specific fact**

> None strictly missing; however, recognizing the GH11 PROSITE-ProRule pattern and its EC 3.2.1.8 assignment requires specialized knowledge of glycoside hydrolase family signatures, which is domain expertise rather than general biology.


**Reason**

> The sequence provides concrete structural and size cues (small ~237 AA, signal peptide, GH11-typical motifs, β-jelly-roll architecture) that allow a knowledgeable model to eliminate methyltransferase and monooxygenase classes and to distinguish GH11 xylanase (EC 3.2.1.8) from GH67 α-glucuronidase (EC 3.2.1.20) based on fold type and expected size. This constitutes a defensible reasoning chain, though it relies on specialized enzymology knowledge.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options span three distinct EC top-level classes (hydrolase, transferase, oxidoreductase), and within the hydrolase class the two glycosidase options (GH11 vs GH67) are distinguishable by sequence size and fold. No two options are genuinely indistinguishable from the supplied sequence.


### Important caveats

- The EC 3.2.1.8 annotation in the matching UniProt entry carries evidence code ECO:0000255|PROSITE-ProRule:PRU01097, i.e., computational pattern-match inference, not direct experimental verification of xylanase activity on this specific protein.
- The current UniProt record (version 62, sequence_version 2, 250 AA) differs from the supplied 237-AA sequence; the annotation applies via the historical version-1 sequence match (H1, H2, H4), not the current sequence.
- The protein is also described as an 'Ethylene-inducing xylanase 2' with a separate PubMed reference (33205907) for its elicitor function; its xylanase catalytic activity per se is annotated computationally.
- The PROSITE-ProRule PRU01097 pattern is specific to GH11; a model without access to PROSITE family definitions would need to rely on general size/fold heuristics, which are less precise.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A multi-step reasoning chain is available from the sequence itself: (1) The sequence lacks Rossmann-fold / SAM-binding motifs expected of methyltransferases (EC 2.1.1.x) and lacks heme-binding (FxxGxxxCxG) or flavin-binding motifs expected of monooxygenases (EC 1.14.13.x), eliminating C and D. (2) The sequence contains motifs characteristic of glycoside hydrolases (e.g., 'ITD' near position 30, a β-jelly-roll-like arrangement of conserved aromatic/glycine-rich stretches such as 'GGGQVTYTMGAGSRYSVTWKDTGNFVGGKGWNPGTGRTINYGGSFSPQGNGYLAVYGWTRNPLIEYY'), narrowing to the 3.2.1.x glycosidase class. (3) The small mature size (~210 AA after signal peptide cleavage) and the GH11-specific PROSITE-ProRule PRU01097 signature (ITD catalytic nucleophile motif, YNT/related catalytic acid motif, β-jelly roll topology) are hallmarks of GH11 endo-β-xylanases (EC 3.2.1.8), whereas GH67 α-glucuronidases (EC 3.2.1.20) are typically 400–500 AA with an entirely different α/β-sandwich fold. This size and fold distinction meaningfully separates A from B.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly missing; however, recognizing the GH11 PROSITE-ProRule pattern and its EC 3.2.1.8 assignment requires specialized knowledge of glycoside hydrolase family signatures, which is domain expertise rather than general biology.",
    "reason": "The sequence provides concrete structural and size cues (small ~237 AA, signal peptide, GH11-typical motifs, β-jelly-roll architecture) that allow a knowledgeable model to eliminate methyltransferase and monooxygenase classes and to distinguish GH11 xylanase (EC 3.2.1.8) from GH67 α-glucuronidase (EC 3.2.1.20) based on fold type and expected size. This constitutes a defensible reasoning chain, though it relies on specialized enzymology knowledge."
  },
  "case_id": "EC_number_0015",
  "expected_answer_check": {
    "evidence_ids": [
      "H1",
      "H2",
      "H4",
      "C4",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The supplied 237-AA sequence exactly matches UniProt entry G2X0L1 (EIX2_VERDV, sequence_version 1, historical entry version 60). That entry annotates EC 3.2.1.8 (Endohydrolysis of (1→4)-β-D-xylosidic linkages in xylans) with evidence code ECO:0000255|PROSITE-ProRule:PRU01097, a computational pattern-match inference for Glycoside Hydrolase family 11. The protein is named 'Ethylene-inducing xylanase 2' from Verticillium dahliae. The EC assignment is thus supported by the matching database record, though the evidence is computational (PROSITE-ProRule), not direct experimental measurement of xylanase activity on this specific protein."
  },
  "important_caveats": [
    "The EC 3.2.1.8 annotation in the matching UniProt entry carries evidence code ECO:0000255|PROSITE-ProRule:PRU01097, i.e., computational pattern-match inference, not direct experimental verification of xylanase activity on this specific protein.",
    "The current UniProt record (version 62, sequence_version 2, 250 AA) differs from the supplied 237-AA sequence; the annotation applies via the historical version-1 sequence match (H1, H2, H4), not the current sequence.",
    "The protein is also described as an 'Ethylene-inducing xylanase 2' with a separate PubMed reference (33205907) for its elicitor function; its xylanase catalytic activity per se is annotated computationally.",
    "The PROSITE-ProRule PRU01097 pattern is specific to GH11; a model without access to PROSITE family definitions would need to rely on general size/fold heuristics, which are less precise."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span three distinct EC top-level classes (hydrolase, transferase, oxidoreductase), and within the hydrolase class the two glycosidase options (GH11 vs GH67) are distinguishable by sequence size and fold. No two options are genuinely indistinguishable from the supplied sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0015",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied 237-AA sequence exactly matches UniProt entry G2X0L1 (EIX2_VERDV, sequence_version 1, historical entry version 60). That entry annotates EC 3.2.1.8 (Endohydrolysis of (1→4)-β-D-xylosidic linkages in xylans) with evidence code ECO:0000255|PROSITE-ProRule:PRU01097, a computational pattern-match inference for Glycoside Hydrolase family 11. The protein is named 'Ethylene-inducing xylanase 2' from Verticillium dahliae. The EC assignment is thus supported by the matching database record, though the evidence is computational (PROSITE-ProRule), not direct experimental measurement of xylanase activity on this specific protein.",
    "evidence_ids": ["H1", "H2", "H4", "C4", "C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "A multi-step reasoning chain is available from the sequence itself: (1) The sequence lacks Rossmann-fold / SAM-binding motifs expected of methyltransferases (EC 2.1.1.x) and lacks heme-binding (FxxGxxxCxG) or flavin-binding motifs expected of monooxygenases (EC 1.14.13.x), eliminating C and D. (2) The sequence contains motifs characteristic of glycoside hydrolases (e.g., 'ITD' near position 30, a β-jelly-roll-like arrangement of conserved aromatic/glycine-rich stretches such as 'GGGQVTYTMGAGSRYSVTWKDTGNFVGGKGWNPGTGRTINYGGSFSPQGNGYLAVYGWTRNPLIEYY'), narrowing to the 3.2.1.x glycosidase class. (3) The small mature size (~210 AA after signal peptide cleavage) and the GH11-specific PROSITE-ProRule PRU01097 signature (ITD catalytic nucleophile motif, YNT/related catalytic acid motif, β-jelly roll topology) are hallmarks of GH11 endo-β-xylanases (EC 3.2.1.8), whereas GH67 α-glucuronidases (EC 3.2.1.20) are typically 400–500 AA with an entirely different α/β-sandwich fold. This size and fold distinction meaningfully separates A from B.",
    "missing_item_specific_fact": "None strictly missing; however, recognizing the GH11 PROSITE-ProRule pattern and its EC 3.2.1.8 assignment requires specialized knowledge of glycoside hydrolase family signatures, which is domain expertise rather than general biology.",
    "reason": "The sequence provides concrete structural and size cues (small ~237 AA, signal peptide, GH11-typical motifs, β-jelly-roll architecture) that allow a knowledgeable model to eliminate methyltransferase and monooxygenase classes and to distinguish GH11 xylanase (EC 3.2.1.8) from GH67 α-glucuronidase (EC 3.2.1.20) based on fold type and expected size. This constitutes a defensible reasoning chain, though it relies on specialized enzymology knowledge."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span three distinct EC top-level classes (hydrolase, transferase, oxidoreductase), and within the hydrolase class the two glycosidase options (GH11 vs GH67) are distinguishable by sequence size and fold. No two options are genuinely indistinguishable from the supplied sequence."
  },
  "important_caveats": [
    "The EC 3.2.1.8 annotation in the matching UniProt entry carries evidence code ECO:0000255|PROSITE-ProRule:PRU01097, i.e., computational pattern-match inference, not direct experimental verification of xylanase activity on this specific protein.",
    "The current UniProt record (version 62, sequence_version 2, 250 AA) differs from the supplied 237-AA sequence; the annotation applies via the historical version-1 sequence match (H1, H2, H4), not the current sequence.",
    "The protein is also described as an 'Ethylene-inducing xylanase 2' with a separate PubMed reference (33205907) for its elicitor function; its xylanase catalytic activity per se is annotated computationally.",
    "The PROSITE-ProRule PRU01097 pattern is specific to GH11; a model without access to PROSITE family definitions would need to rely on general size/fold heuristics, which are less precise."
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

**Accession:** `G2X0L1` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current mismatch.  
**Historical cutoff:** 2026-05-07; archived entry version 60. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- The current UniProt sequence differs from the supplied sequence; applicability of current annotation excerpts is qualified by that mismatch.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2X0L1.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** mismatch.  
**Retrieved:** 2026-11-01T06:25:06.423596+00:00.  

```json
{"alternativeNames":[{"fullName":{"value":"1,4-beta-D-xylan xylanohydrolase G"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"18720841","source":"PubMed"}],"value":"Endo-1,4-beta-xylanase G"},"shortNames":[{"value":"Xylanase G"}]}],"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"18720841","source":"PubMed"}],"value":"3.2.1.8"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33205907","source":"PubMed"}],"value":"Ethylene-inducing xylanase 2"}}}
```

Source SHA-256: `b6bf3dd61dab32b344f08d226c011b7c3f3936305e457046c933fe6555956510`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2X0L1.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** mismatch.  
**Retrieved:** 2026-11-01T06:25:06.423596+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"3.2.1.8","evidences":[{"evidenceCode":"ECO:0000269","id":"18720841","source":"PubMed"}],"name":"Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans."}}
```

Source SHA-256: `b6bf3dd61dab32b344f08d226c011b7c3f3936305e457046c933fe6555956510`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G2X0L1?format=txt&versions=60)  
**Locator:** `lines 1-16`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 60 / 1.  
**Retrieved:** 2026-11-01T06:28:04.256317+00:00.  

```text
ID   EIX2_VERDV              Reviewed;         237 AA.
AC   G2X0L1;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   16-NOV-2011, sequence version 1.
DT   28-JAN-2026, entry version 60.
DE   RecName: Full=Ethylene-inducing xylanase 2 {ECO:0000303|PubMed:33205907};
DE            Short=EIX2 {ECO:0000303|PubMed:33205907};
DE            EC=3.2.1.8 {ECO:0000255|PROSITE-ProRule:PRU01097};
DE   AltName: Full=Endo-1,4-beta-xylanase EIX2 {ECO:0000303|PubMed:33205907};
DE   Flags: Precursor;
GN   Name=EIX2 {ECO:0000303|PubMed:33205907}; ORFNames=VDAG_03790;
OS   Verticillium dahliae (strain VdLs.17 / ATCC MYA-4575 / FGSC 10137)
OS   (Verticillium wilt).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;
OC   Hypocreomycetidae; Glomerellales; Plectosphaerellaceae; Verticillium.
OX   NCBI_TaxID=498257;
```

Source SHA-256: `fdadd4e4d52d68a34b5b3ac543b98fcb1301387253e8b3d7575373dd73f1aa2a`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G2X0L1?format=txt&versions=60)  
**Locator:** `lines 6-10`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 60 / 1.  
**Retrieved:** 2026-11-01T06:28:04.256317+00:00.  

```text
DE   RecName: Full=Ethylene-inducing xylanase 2 {ECO:0000303|PubMed:33205907};
DE            Short=EIX2 {ECO:0000303|PubMed:33205907};
DE            EC=3.2.1.8 {ECO:0000255|PROSITE-ProRule:PRU01097};
DE   AltName: Full=Endo-1,4-beta-xylanase EIX2 {ECO:0000303|PubMed:33205907};
DE   Flags: Precursor;
```

Source SHA-256: `fdadd4e4d52d68a34b5b3ac543b98fcb1301387253e8b3d7575373dd73f1aa2a`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G2X0L1?format=txt&versions=60)  
**Locator:** `lines 44-46`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 60 / 1.  
**Retrieved:** 2026-11-01T06:28:04.256317+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.;
CC         EC=3.2.1.8; Evidence={ECO:0000255|PROSITE-ProRule:PRU01097};
```

Source SHA-256: `fdadd4e4d52d68a34b5b3ac543b98fcb1301387253e8b3d7575373dd73f1aa2a`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 15. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
