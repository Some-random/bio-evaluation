# catalytic_activity_0016

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **A** — L-fucose + ATP = beta-L-fucose 1-phosphate + ADP + H(+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MQKLLSLPSNLVQSFHELERVNRTDWFCTSDPVGKKLGSGGGTSWLLEECYNEYSDGATFGEWLEKEKRILLHAGGQSRRLPGYAPSGKILTPVPVFRWERGQHLGQNLLSLQLPLYEKIMSLAPDKLHTLIASGDVYIRSEKPLQSIPEADVVCYGLWVDPSLATHHGVFASDRKHPEQLDFMLQKPSLAELESLSKTHLFLMDIGIWLLSDRAVEILMKRSHKESSEELKYYDLYSDFGLALGTHPRIEDEEVNTLSVAILPLPGGEFYHYGTSKELISSTLSVQNKVYDQRRIMHRKVKPNPAMFVQNAVVRIPLCAENADLWIENSHIGPKWKIASRHIITGVPENDWSLAVPAGVCVDVVPMGDKGFVARPYGLDDVFKGDLRDSKTTLTGIPFGEWMSKRGLSYTDLKGRTDDLQAVSVFPMVNSVEELGLVLRWMLSEPELEEGKNIWLRSEHFSADEISAGANLKRLYAQREEFRKGNWKALAVNHEKSVFYQLDLADAAEDFVRLGLDMPELLPEDALQMSRIHNRMLRARILKLDGKDYRPEEQAAFDLLRDGLLDGISNRKSTPKLDVYSDQIVWGRSPVRIDMAGGWTDTPPYSLYSGGNVVNLAIELNGQPPLQVYVKPCKDFHIVLRSIDMGAMEIVSTFDELQDYKKIGSPFSIPKAALSLAGFAPAFSAVSYASLEEQLKDFGAGIEVTLLAAIPAGSGLGTSSILASTVLGAINDFCGLAWDKNEICQRTLVLEQLLTTGGGWQDQYGGVLQGVKLLQTEAGFAQSPLVRWLPDHLFTHPEYKDCHLLYYTGITRTAKGILAEIVSSMFLNSSLHLNLLSEMKAHALDMNEAIQRGSFVEFGRLVGKTWEQNKALDSGTNPPAVEAIIDLIKDYTLGYKLPGAGGGGYLYMVAKDPQAAVRIRKILTENAPNPRARFVEMTLSDKGFQVSRS

[Multiple Choices]
A. L-fucose + ATP = beta-L-fucose 1-phosphate + ADP + H(+)
B. a cytidine in mRNA + acetyl-CoA + ATP + H2O = an N(4)-acetylcytidine in mRNA + ADP + phosphate + CoA + H(+)
C. Endonucleolytic cleavage to 5'-phosphomonoester.
D. N-[(R)-4-phosphopantothenoyl]-L-cysteine + H(+) = (R)-4'-phosphopantetheine + CO2
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzymatic Reaction Prediction, which is to identify the specific chemical reaction catalyzed by a given enzyme. This involves understanding the enzyme's function based on its amino acid sequence and then selecting the correct transformation of substrates into products from a list of possible reactions.. The inputs provided by the user for this task include:

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

> The supplied sequence exactly matches the annotated Bacteroides fragilis L-fucokinase/L-fucose-1-P guanylyltransferase. Its annotated, publication-supported catalytic activity includes the reaction in choice A.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The choices describe distinct enzyme reactions, but the sequence and prompt provide no organism, protein name, domain annotation, or other contextual clue that establishes which reaction this particular protein catalyzes.


**Missing item-specific fact**

> The protein-specific identification and functional annotation as L-fucokinase are needed to select A.


**Reason**

> The key is supported by reviewer-only annotations, but those annotations were not supplied to the evaluated model. Inferring this specific activity from the raw sequence would require protein-specific recognition or external functional annotation, not a general biological argument available from the question.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The annotated fucokinase reaction matches A; the protein's additional annotated guanylyltransferase reaction is not among the choices.


### Important caveats

- The sequence match is exact, and the catalytic-activity annotation cites a publication with experimental evidence code ECO:0000269.
- The evidence supports choice A as an activity of this bifunctional enzyme; it does not establish that A is its only catalytic activity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The choices describe distinct enzyme reactions, but the sequence and prompt provide no organism, protein name, domain annotation, or other contextual clue that establishes which reaction this particular protein catalyzes.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identification and functional annotation as L-fucokinase are needed to select A.",
    "reason": "The key is supported by reviewer-only annotations, but those annotations were not supplied to the evaluated model. Inferring this specific activity from the raw sequence would require protein-specific recognition or external functional annotation, not a general biological argument available from the question."
  },
  "case_id": "catalytic_activity_0016",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the annotated Bacteroides fragilis L-fucokinase/L-fucose-1-P guanylyltransferase. Its annotated, publication-supported catalytic activity includes the reaction in choice A."
  },
  "important_caveats": [
    "The sequence match is exact, and the catalytic-activity annotation cites a publication with experimental evidence code ECO:0000269.",
    "The evidence supports choice A as an activity of this bifunctional enzyme; it does not establish that A is its only catalytic activity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The annotated fucokinase reaction matches A; the protein's additional annotated guanylyltransferase reaction is not among the choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0016",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the annotated Bacteroides fragilis L-fucokinase/L-fucose-1-P guanylyltransferase. Its annotated, publication-supported catalytic activity includes the reaction in choice A.",
    "evidence_ids": ["C1", "C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The choices describe distinct enzyme reactions, but the sequence and prompt provide no organism, protein name, domain annotation, or other contextual clue that establishes which reaction this particular protein catalyzes.",
    "missing_item_specific_fact": "The protein-specific identification and functional annotation as L-fucokinase are needed to select A.",
    "reason": "The key is supported by reviewer-only annotations, but those annotations were not supplied to the evaluated model. Inferring this specific activity from the raw sequence would require protein-specific recognition or external functional annotation, not a general biological argument available from the question."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The annotated fucokinase reaction matches A; the protein's additional annotated guanylyltransferase reaction is not among the choices."
  },
  "important_caveats": [
    "The sequence match is exact, and the catalytic-activity annotation cites a publication with experimental evidence code ECO:0000269.",
    "The evidence supports choice A as an activity of this bifunctional enzyme; it does not establish that A is its only catalytic activity."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q58T34 (FKP_BACFG, 949 AA, sequence match confirmed) explicitly annotates the catalytic activity as 'L-fucose + ATP = beta-L-fucose 1-phosphate + ADP + H(+)' under EC 2.7.1.52, supported by experimental evidence (ECO:0000269, PubMed:30242642, cryo-EM structure and functional characterization). The expected answer text matches the UniProt annotation exactly.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [H1](#evidence-h1), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal region contains a glycine-rich nucleotide-binding motif (GSGGGTSWL) characteristic of kinase/phosphotransferase families, consistent with ATP-dependent phosphorylation (option A). The other three options represent fundamentally different enzyme classes: B (acetyltransferase) requires a GNAT or similar acetyl-CoA-binding fold absent here; C (nuclease) requires catalytic motifs such as ExoN, PD-(D/E)xK, or RNase-H-like residues not evident; D (PLP-dependent decarboxylase) requires a PLP-binding lysine and TIM-barrel architecture not matching this sequence. Elimination of B, C, and D based on the absence of their diagnostic motifs, combined with positive nucleotide-binding evidence, points to A as the only kinase/phosphotransferase option.


**Missing item-specific fact**

> The specific substrate identity (fucose vs. any other sugar) is not derivable from sequence alone; however, since only one option is a phosphotransferase, the question is answerable by enzyme-class identification without knowing the exact substrate.


**Reason**

> The four choices span four distinct enzyme classes (kinase, acetyltransferase, nuclease, decarboxylase). The GSGGG nucleotide-binding motif provides positive evidence for a phosphotransferase, while the absence of GNAT, nuclease, and PLP-decarboxylase signatures eliminates the other three. This elimination logic is accessible through general enzymology knowledge without requiring memorization of this specific protein's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent mutually exclusive enzyme classes with distinct mechanistic and structural signatures. Only one (A) is consistent with a nucleotide-dependent phosphotransferase motif. No other option is defensible given the sequence features.


### Important caveats

- The GSGGG motif is a common nucleotide-binding element found in many protein families beyond kinases; its presence is suggestive but not diagnostic of kinase activity alone.
- The protein is bifunctional (949 AA, kinase + pyrophosphorylase domains); the question asks about only one of its two catalytic activities (the kinase reaction, option A), while the pyrophosphorylase activity is not offered as a distractor.
- The specific identification of the substrate as fucose (rather than another sugar) cannot be derived from sequence alone; the question is answerable only because the other options are entirely different enzyme classes.
- The UniProt annotation is supported by experimental evidence (cryo-EM structure, mutagenesis, functional assays from PubMed:30242642), not merely computational transfer.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal region contains a glycine-rich nucleotide-binding motif (GSGGGTSWL) characteristic of kinase/phosphotransferase families, consistent with ATP-dependent phosphorylation (option A). The other three options represent fundamentally different enzyme classes: B (acetyltransferase) requires a GNAT or similar acetyl-CoA-binding fold absent here; C (nuclease) requires catalytic motifs such as ExoN, PD-(D/E)xK, or RNase-H-like residues not evident; D (PLP-dependent decarboxylase) requires a PLP-binding lysine and TIM-barrel architecture not matching this sequence. Elimination of B, C, and D based on the absence of their diagnostic motifs, combined with positive nucleotide-binding evidence, points to A as the only kinase/phosphotransferase option.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The specific substrate identity (fucose vs. any other sugar) is not derivable from sequence alone; however, since only one option is a phosphotransferase, the question is answerable by enzyme-class identification without knowing the exact substrate.",
    "reason": "The four choices span four distinct enzyme classes (kinase, acetyltransferase, nuclease, decarboxylase). The GSGGG nucleotide-binding motif provides positive evidence for a phosphotransferase, while the absence of GNAT, nuclease, and PLP-decarboxylase signatures eliminates the other three. This elimination logic is accessible through general enzymology knowledge without requiring memorization of this specific protein's annotation."
  },
  "case_id": "catalytic_activity_0016",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C7",
      "H1",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q58T34 (FKP_BACFG, 949 AA, sequence match confirmed) explicitly annotates the catalytic activity as 'L-fucose + ATP = beta-L-fucose 1-phosphate + ADP + H(+)' under EC 2.7.1.52, supported by experimental evidence (ECO:0000269, PubMed:30242642, cryo-EM structure and functional characterization). The expected answer text matches the UniProt annotation exactly."
  },
  "important_caveats": [
    "The GSGGG motif is a common nucleotide-binding element found in many protein families beyond kinases; its presence is suggestive but not diagnostic of kinase activity alone.",
    "The protein is bifunctional (949 AA, kinase + pyrophosphorylase domains); the question asks about only one of its two catalytic activities (the kinase reaction, option A), while the pyrophosphorylase activity is not offered as a distractor.",
    "The specific identification of the substrate as fucose (rather than another sugar) cannot be derived from sequence alone; the question is answerable only because the other options are entirely different enzyme classes.",
    "The UniProt annotation is supported by experimental evidence (cryo-EM structure, mutagenesis, functional assays from PubMed:30242642), not merely computational transfer."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent mutually exclusive enzyme classes with distinct mechanistic and structural signatures. Only one (A) is consistent with a nucleotide-dependent phosphotransferase motif. No other option is defensible given the sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0016",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q58T34 (FKP_BACFG, 949 AA, sequence match confirmed) explicitly annotates the catalytic activity as 'L-fucose + ATP = beta-L-fucose 1-phosphate + ADP + H(+)' under EC 2.7.1.52, supported by experimental evidence (ECO:0000269, PubMed:30242642, cryo-EM structure and functional characterization). The expected answer text matches the UniProt annotation exactly.",
    "evidence_ids": ["C1", "C4", "C5", "C7", "H1", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal region contains a glycine-rich nucleotide-binding motif (GSGGGTSWL) characteristic of kinase/phosphotransferase families, consistent with ATP-dependent phosphorylation (option A). The other three options represent fundamentally different enzyme classes: B (acetyltransferase) requires a GNAT or similar acetyl-CoA-binding fold absent here; C (nuclease) requires catalytic motifs such as ExoN, PD-(D/E)xK, or RNase-H-like residues not evident; D (PLP-dependent decarboxylase) requires a PLP-binding lysine and TIM-barrel architecture not matching this sequence. Elimination of B, C, and D based on the absence of their diagnostic motifs, combined with positive nucleotide-binding evidence, points to A as the only kinase/phosphotransferase option.",
    "missing_item_specific_fact": "The specific substrate identity (fucose vs. any other sugar) is not derivable from sequence alone; however, since only one option is a phosphotransferase, the question is answerable by enzyme-class identification without knowing the exact substrate.",
    "reason": "The four choices span four distinct enzyme classes (kinase, acetyltransferase, nuclease, decarboxylase). The GSGGG nucleotide-binding motif provides positive evidence for a phosphotransferase, while the absence of GNAT, nuclease, and PLP-decarboxylase signatures eliminates the other three. This elimination logic is accessible through general enzymology knowledge without requiring memorization of this specific protein's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent mutually exclusive enzyme classes with distinct mechanistic and structural signatures. Only one (A) is consistent with a nucleotide-dependent phosphotransferase motif. No other option is defensible given the sequence features."
  },
  "important_caveats": [
    "The GSGGG motif is a common nucleotide-binding element found in many protein families beyond kinases; its presence is suggestive but not diagnostic of kinase activity alone.",
    "The protein is bifunctional (949 AA, kinase + pyrophosphorylase domains); the question asks about only one of its two catalytic activities (the kinase reaction, option A), while the pyrophosphorylase activity is not offered as a distractor.",
    "The specific identification of the substrate as fucose (rather than another sugar) cannot be derived from sequence alone; the question is answerable only because the other options are entirely different enzyme classes.",
    "The UniProt annotation is supported by experimental evidence (cryo-EM structure, mutagenesis, functional assays from PubMed:30242642), not merely computational transfer."
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

**Accession:** `Q58T34` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 87. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q58T34.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:01.700323+00:00.  

```json
"Q58T34"
```

Source SHA-256: `613cb95f164460b198373fe8b1a0278d6f82b5f36a7ad73441bef68f5e41af74`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q58T34.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:01.700323+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"30242642","source":"PubMed"}],"value":"L-fucokinase/GDP-fucose pyrophosphorylase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"30242642","source":"PubMed"}],"value":"FKP"}]}],"includes":[{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"30242642","source":"PubMed"}],"value":"GDP-fucose pyrophosphorylase"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"30242642","source":"PubMed"}],"value":"2.7.7.30"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305","id":"30242642","source":"PubMed"}],"value":"Fucose-1-phosphate guanylyltransferase"}}},{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"30242642","source":"PubMed"}],"value":"2.7.1.52"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"30242642","source":"PubMed"}],"value":"L-fucokinase"}}}],"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305","id":"30242642","source":"PubMed"}],"value":"L-fucokinase/L-fucose-1-P guanylyltransferase"}}}
```

Source SHA-256: `613cb95f164460b198373fe8b1a0278d6f82b5f36a7ad73441bef68f5e41af74`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q58T34.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:01.700323+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000305","id":"30242642","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:13242"}}],"reaction":{"ecNumber":"2.7.1.52","evidences":[{"evidenceCode":"ECO:0000269","id":"30242642","source":"PubMed"}],"name":"beta-L-fucose + ATP = beta-L-fucose 1-phosphate + ADP + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:13241"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:30616"},{"database":"ChEBI","id":"CHEBI:42589"},{"database":"ChEBI","id":"CHEBI:57268"},{"database":"ChEBI","id":"CHEBI:456216"}]}}
```

Source SHA-256: `613cb95f164460b198373fe8b1a0278d6f82b5f36a7ad73441bef68f5e41af74`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q58T34.json)  
**Locator:** `/references/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:01.700323+00:00.  

```json
{"citation":{"authors":["Liu Y.","Hu H.","Wang J.","Zhou Q.","Wu P.","Yan N.","Wang H.W.","Wu J.W.","Sun L."],"citationCrossReferences":[{"database":"PubMed","id":"30242642"},{"database":"DOI","id":"10.1007/s13238-018-0576-x"}],"citationType":"journal article","firstPage":"365","id":"30242642","journal":"Protein Cell","lastPage":"369","publicationDate":"2019","title":"Cryo-EM structure of L-fucokinase/GDP-fucose pyrophosphorylase (FKP) in Bacteroides fragilis.","volume":"10"},"evidences":[{"evidenceCode":"ECO:0007744","id":"5YYS","source":"PDB"}],"referenceComments":[{"type":"STRAIN","value":"9343"}],"referenceNumber":3,"referencePositions":["STRUCTURE BY ELECTRON MICROSCOPY (4.20 ANGSTROMS)","FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","SUBUNIT","DOMAIN","MUTAGENESIS OF GLY-76; ARG-80; GLY-88; LYS-89; ARG-592; ASP-594; GLY-597; GLY-598; ASP-601; GLY-713; SER-714; GLY-715; GLY-717; SER-719; SER-720; ALA-723; GLY-758; GLY-759; GLN-761; ASP-762; GLY-899 AND GLY-901"]}
```

Source SHA-256: `613cb95f164460b198373fe8b1a0278d6f82b5f36a7ad73441bef68f5e41af74`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q58T34?format=txt&versions=87)  
**Locator:** `lines 1-21`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 87 / 1.  
**Retrieved:** 2026-11-02T04:31:04.760170+00:00.  

```text
ID   FKP_BACFG               Reviewed;         949 AA.
AC   Q58T34;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   26-APR-2005, sequence version 1.
DT   28-JAN-2026, entry version 87.
DE   RecName: Full=L-fucokinase/L-fucose-1-P guanylyltransferase {ECO:0000305|PubMed:30242642};
DE   AltName: Full=L-fucokinase/GDP-fucose pyrophosphorylase {ECO:0000303|PubMed:30242642};
DE            Short=FKP {ECO:0000303|PubMed:30242642};
DE   Includes:
DE     RecName: Full=Fucose-1-phosphate guanylyltransferase {ECO:0000305|PubMed:30242642};
DE              EC=2.7.7.30 {ECO:0000269|PubMed:30242642};
DE     AltName: Full=GDP-fucose pyrophosphorylase {ECO:0000303|PubMed:30242642};
DE   Includes:
DE     RecName: Full=L-fucokinase {ECO:0000303|PubMed:30242642};
DE              EC=2.7.1.52 {ECO:0000269|PubMed:30242642};
GN   Name=fkp {ECO:0000312|EMBL:AAX45030.1};
GN   ORFNames=HMPREF2533_03026 {ECO:0000312|EMBL:KXU43832.1};
OS   Bacteroides fragilis.
OC   Bacteria; Pseudomonadati; Bacteroidota; Bacteroidia; Bacteroidales;
OC   Bacteroidaceae; Bacteroides.
OX   NCBI_TaxID=817;
```

Source SHA-256: `3ecc50c16d349ff2fe2b86dd83a0288577ce5483563a520fae349796ac46e9a8`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q58T34?format=txt&versions=87)  
**Locator:** `lines 6-15`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 87 / 1.  
**Retrieved:** 2026-11-02T04:31:04.760170+00:00.  

```text
DE   RecName: Full=L-fucokinase/L-fucose-1-P guanylyltransferase {ECO:0000305|PubMed:30242642};
DE   AltName: Full=L-fucokinase/GDP-fucose pyrophosphorylase {ECO:0000303|PubMed:30242642};
DE            Short=FKP {ECO:0000303|PubMed:30242642};
DE   Includes:
DE     RecName: Full=Fucose-1-phosphate guanylyltransferase {ECO:0000305|PubMed:30242642};
DE              EC=2.7.7.30 {ECO:0000269|PubMed:30242642};
DE     AltName: Full=GDP-fucose pyrophosphorylase {ECO:0000303|PubMed:30242642};
DE   Includes:
DE     RecName: Full=L-fucokinase {ECO:0000303|PubMed:30242642};
DE              EC=2.7.1.52 {ECO:0000269|PubMed:30242642};
```

Source SHA-256: `3ecc50c16d349ff2fe2b86dd83a0288577ce5483563a520fae349796ac46e9a8`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q58T34?format=txt&versions=87)  
**Locator:** `lines 54-60`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 87 / 1.  
**Retrieved:** 2026-11-02T04:31:04.760170+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=L-fucose + ATP = beta-L-fucose 1-phosphate + ADP + H(+);
CC         Xref=Rhea:RHEA:13241, ChEBI:CHEBI:2181, ChEBI:CHEBI:15378,
CC         ChEBI:CHEBI:30616, ChEBI:CHEBI:57268, ChEBI:CHEBI:456216;
CC         EC=2.7.1.52; Evidence={ECO:0000269|PubMed:30242642};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:13242;
CC         Evidence={ECO:0000305|PubMed:30242642};
```

Source SHA-256: `3ecc50c16d349ff2fe2b86dd83a0288577ce5483563a520fae349796ac46e9a8`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 16. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
