# GO_molecular_function_0075

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **D** — endo-1,4-beta-xylanase activity

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
A. oxidized pyrimidine nucleobase lesion DNA N-glycosylase activity
B. sphingomyelin transfer activity
C. beta-amyrin synthase activity
D. endo-1,4-beta-xylanase activity
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Molecular Function Prediction, which is to predict the fundamental activity of a protein at the molecular level, as defined by the Gene Ontology (GO) 'Molecular Function' branch. This describes the elemental tasks a protein performs, such as catalysis, transport, or binding to specific molecules. Based on the protein's amino acid sequence, you are to select the option that best describes its primary molecular function.. The inputs provided by the user for this task include:

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

> The historical UniProt record matches the supplied sequence and assigns endo-1,4-beta-xylanase activity. Its catalytic-activity annotation is based on a computational ProRule, and the function annotation is by similarity, so this supports D without establishing direct experimental confirmation of catalysis for this exact sequence.

Citations as saved: [H1](#evidence-h1), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal hydrophobic signal-peptide-like segment and compact, aromatic-rich sequence are consistent with a small secreted fungal carbohydrate-active enzyme. That architecture favors a xylanase over the unrelated DNA-repair enzyme, sphingomyelin-transfer protein, or oxidosqualene cyclase choices.


**Missing item-specific fact**

> Direct experimental confirmation of xylan hydrolysis by this exact protein is not supplied; the sequence-based distinction does not depend on knowing its database entry.


**Reason**

> The choices are biologically distinct, and the sequence provides meaningful localization and enzyme-family clues favoring a secreted polysaccharide hydrolase. These clues support D among the options, though they are not a substitute for a substrate assay.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No alternative listed choice is comparably supported by the sequence features.


### Important caveats

- The exact-sequence historical annotation supports D but cites similarity and computational catalytic inference; it is not, in the supplied evidence, direct experimental validation of xylanase catalysis for this exact sequence.
- Current UniProt excerpts refer to a sequence mismatch and should not be treated as direct evidence for the supplied sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic signal-peptide-like segment and compact, aromatic-rich sequence are consistent with a small secreted fungal carbohydrate-active enzyme. That architecture favors a xylanase over the unrelated DNA-repair enzyme, sphingomyelin-transfer protein, or oxidosqualene cyclase choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Direct experimental confirmation of xylan hydrolysis by this exact protein is not supplied; the sequence-based distinction does not depend on knowing its database entry.",
    "reason": "The choices are biologically distinct, and the sequence provides meaningful localization and enzyme-family clues favoring a secreted polysaccharide hydrolase. These clues support D among the options, though they are not a substitute for a substrate assay."
  },
  "case_id": "GO_molecular_function_0075",
  "expected_answer_check": {
    "evidence_ids": [
      "H1",
      "H3",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The historical UniProt record matches the supplied sequence and assigns endo-1,4-beta-xylanase activity. Its catalytic-activity annotation is based on a computational ProRule, and the function annotation is by similarity, so this supports D without establishing direct experimental confirmation of catalysis for this exact sequence."
  },
  "important_caveats": [
    "The exact-sequence historical annotation supports D but cites similarity and computational catalytic inference; it is not, in the supplied evidence, direct experimental validation of xylanase catalysis for this exact sequence.",
    "Current UniProt excerpts refer to a sequence mismatch and should not be treated as direct evidence for the supplied sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No alternative listed choice is comparably supported by the sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0075",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The historical UniProt record matches the supplied sequence and assigns endo-1,4-beta-xylanase activity. Its catalytic-activity annotation is based on a computational ProRule, and the function annotation is by similarity, so this supports D without establishing direct experimental confirmation of catalysis for this exact sequence.",
    "evidence_ids": ["H1", "H3", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal hydrophobic signal-peptide-like segment and compact, aromatic-rich sequence are consistent with a small secreted fungal carbohydrate-active enzyme. That architecture favors a xylanase over the unrelated DNA-repair enzyme, sphingomyelin-transfer protein, or oxidosqualene cyclase choices.",
    "missing_item_specific_fact": "Direct experimental confirmation of xylan hydrolysis by this exact protein is not supplied; the sequence-based distinction does not depend on knowing its database entry.",
    "reason": "The choices are biologically distinct, and the sequence provides meaningful localization and enzyme-family clues favoring a secreted polysaccharide hydrolase. These clues support D among the options, though they are not a substitute for a substrate assay."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No alternative listed choice is comparably supported by the sequence features."
  },
  "important_caveats": [
    "The exact-sequence historical annotation supports D but cites similarity and computational catalytic inference; it is not, in the supplied evidence, direct experimental validation of xylanase catalysis for this exact sequence.",
    "Current UniProt excerpts refer to a sequence mismatch and should not be treated as direct evidence for the supplied sequence."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The supplied 237 AA sequence matches UniProt G2X0L1 (EIX2_VERDV) at historical sequence version 1 (exact match confirmed). UniProt annotation identifies this protein as Ethylene-inducing xylanase 2 with EC 3.2.1.8 (Endo-1,4-beta-xylanase), catalytic activity 'Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans,' and GO:0031176 (endo-1,4-beta-xylanase activity). The EC assignment is supported by experimental evidence (PubMed:18720841, ECO:0000269) and PROSITE-ProRule. The GO annotation itself is IEA:UniProtKB-EC (inferred from EC), but the underlying EC assignment has experimental backing.

Citations as saved: [H1](#evidence-h1), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Multiple general biological arguments distinguish D from the other options: (1) The N-terminal hydrophobic stretch (MVSFKSLLLAASAFTAVLG) is a classic signal peptide indicating a secreted protein, which is incompatible with nuclear DNA repair enzymes (option A) and atypical for cytoplasmic/membrane lipid transfer proteins (option B). (2) Beta-amyrin synthase (EC 5.4.99.39) is an oxidosqualene cyclase requiring a large multi-domain membrane-anchored architecture (>700 AA); a 237 AA protein is far too small (option C eliminated). (3) A small (~237 AA) secreted fungal protein with a beta-rich composition (multiple Gly, Asn, Tyr clusters) is consistent with glycoside hydrolase family 11 xylanases, which are the predominant small secreted xylanases in fungi. The 'FDSFD' motif near the N-terminus is a recognized GH11 signature. (4) Fungal secreted enzymes targeting plant cell wall polysaccharides (xylan) are well-established in plant-pathogen biology.


**Missing item-specific fact**

> None critical. Specific GH11 active-site residue identification (catalytic Glu pair) would add confirmatory detail, but the elimination of A, B, and C through size, localization, and domain-architecture reasoning is sufficient to select D among the four choices.


**Reason**

> The four options span radically different protein classes (nuclear DNA repair enzyme, lipid transfer protein, large membrane cyclase, small secreted hydrolase). General knowledge of protein size constraints, signal peptide biology, and fungal secretome function provides a concrete, multi-step elimination pathway to D without requiring memorization of this specific UniProt entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A, B, and C are each eliminated by strong, independent biological constraints (subcellular localization incompatible with signal peptide; protein size far too small for oxidosqualene cyclase; lipid transfer proteins lack secretion signals and have distinct fold requirements). Only D is consistent with all observed sequence features.


### Important caveats

- The current UniProt entry (v62) has a 250 AA sequence that mismatches the supplied 237 AA sequence; the historical v60 (sequence version 1) matches exactly. Annotation applicability is qualified by this historical match.
- The GO annotation GO:0031176 is IEA:UniProtKB-EC (inferred from EC number), not a direct experimental GO annotation, though the EC assignment itself has experimental support (PubMed:18720841).
- The protein is also described as an 'ethylene-inducing' elicitor of plant defense, meaning it has a secondary biological role beyond xylan hydrolysis; however, its primary molecular function (catalytic activity) is endo-1,4-beta-xylanase.
- The reviewer-only accession and metadata were absent from the evaluated model input; reasoning must rely on the sequence and general biology alone.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Multiple general biological arguments distinguish D from the other options: (1) The N-terminal hydrophobic stretch (MVSFKSLLLAASAFTAVLG) is a classic signal peptide indicating a secreted protein, which is incompatible with nuclear DNA repair enzymes (option A) and atypical for cytoplasmic/membrane lipid transfer proteins (option B). (2) Beta-amyrin synthase (EC 5.4.99.39) is an oxidosqualene cyclase requiring a large multi-domain membrane-anchored architecture (>700 AA); a 237 AA protein is far too small (option C eliminated). (3) A small (~237 AA) secreted fungal protein with a beta-rich composition (multiple Gly, Asn, Tyr clusters) is consistent with glycoside hydrolase family 11 xylanases, which are the predominant small secreted xylanases in fungi. The 'FDSFD' motif near the N-terminus is a recognized GH11 signature. (4) Fungal secreted enzymes targeting plant cell wall polysaccharides (xylan) are well-established in plant-pathogen biology.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. Specific GH11 active-site residue identification (catalytic Glu pair) would add confirmatory detail, but the elimination of A, B, and C through size, localization, and domain-architecture reasoning is sufficient to select D among the four choices.",
    "reason": "The four options span radically different protein classes (nuclear DNA repair enzyme, lipid transfer protein, large membrane cyclase, small secreted hydrolase). General knowledge of protein size constraints, signal peptide biology, and fungal secretome function provides a concrete, multi-step elimination pathway to D without requiring memorization of this specific UniProt entry."
  },
  "case_id": "GO_molecular_function_0075",
  "expected_answer_check": {
    "evidence_ids": [
      "H1",
      "H3",
      "H4",
      "H5",
      "C4",
      "C5",
      "C6",
      "C7",
      "C8"
    ],
    "judgment": "supported",
    "reason": "The supplied 237 AA sequence matches UniProt G2X0L1 (EIX2_VERDV) at historical sequence version 1 (exact match confirmed). UniProt annotation identifies this protein as Ethylene-inducing xylanase 2 with EC 3.2.1.8 (Endo-1,4-beta-xylanase), catalytic activity 'Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans,' and GO:0031176 (endo-1,4-beta-xylanase activity). The EC assignment is supported by experimental evidence (PubMed:18720841, ECO:0000269) and PROSITE-ProRule. The GO annotation itself is IEA:UniProtKB-EC (inferred from EC), but the underlying EC assignment has experimental backing."
  },
  "important_caveats": [
    "The current UniProt entry (v62) has a 250 AA sequence that mismatches the supplied 237 AA sequence; the historical v60 (sequence version 1) matches exactly. Annotation applicability is qualified by this historical match.",
    "The GO annotation GO:0031176 is IEA:UniProtKB-EC (inferred from EC number), not a direct experimental GO annotation, though the EC assignment itself has experimental support (PubMed:18720841).",
    "The protein is also described as an 'ethylene-inducing' elicitor of plant defense, meaning it has a secondary biological role beyond xylan hydrolysis; however, its primary molecular function (catalytic activity) is endo-1,4-beta-xylanase.",
    "The reviewer-only accession and metadata were absent from the evaluated model input; reasoning must rely on the sequence and general biology alone."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and C are each eliminated by strong, independent biological constraints (subcellular localization incompatible with signal peptide; protein size far too small for oxidosqualene cyclase; lipid transfer proteins lack secretion signals and have distinct fold requirements). Only D is consistent with all observed sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0075",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied 237 AA sequence matches UniProt G2X0L1 (EIX2_VERDV) at historical sequence version 1 (exact match confirmed). UniProt annotation identifies this protein as Ethylene-inducing xylanase 2 with EC 3.2.1.8 (Endo-1,4-beta-xylanase), catalytic activity 'Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans,' and GO:0031176 (endo-1,4-beta-xylanase activity). The EC assignment is supported by experimental evidence (PubMed:18720841, ECO:0000269) and PROSITE-ProRule. The GO annotation itself is IEA:UniProtKB-EC (inferred from EC), but the underlying EC assignment has experimental backing.",
    "evidence_ids": ["H1", "H3", "H4", "H5", "C4", "C5", "C6", "C7", "C8"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Multiple general biological arguments distinguish D from the other options: (1) The N-terminal hydrophobic stretch (MVSFKSLLLAASAFTAVLG) is a classic signal peptide indicating a secreted protein, which is incompatible with nuclear DNA repair enzymes (option A) and atypical for cytoplasmic/membrane lipid transfer proteins (option B). (2) Beta-amyrin synthase (EC 5.4.99.39) is an oxidosqualene cyclase requiring a large multi-domain membrane-anchored architecture (>700 AA); a 237 AA protein is far too small (option C eliminated). (3) A small (~237 AA) secreted fungal protein with a beta-rich composition (multiple Gly, Asn, Tyr clusters) is consistent with glycoside hydrolase family 11 xylanases, which are the predominant small secreted xylanases in fungi. The 'FDSFD' motif near the N-terminus is a recognized GH11 signature. (4) Fungal secreted enzymes targeting plant cell wall polysaccharides (xylan) are well-established in plant-pathogen biology.",
    "missing_item_specific_fact": "None critical. Specific GH11 active-site residue identification (catalytic Glu pair) would add confirmatory detail, but the elimination of A, B, and C through size, localization, and domain-architecture reasoning is sufficient to select D among the four choices.",
    "reason": "The four options span radically different protein classes (nuclear DNA repair enzyme, lipid transfer protein, large membrane cyclase, small secreted hydrolase). General knowledge of protein size constraints, signal peptide biology, and fungal secretome function provides a concrete, multi-step elimination pathway to D without requiring memorization of this specific UniProt entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and C are each eliminated by strong, independent biological constraints (subcellular localization incompatible with signal peptide; protein size far too small for oxidosqualene cyclase; lipid transfer proteins lack secretion signals and have distinct fold requirements). Only D is consistent with all observed sequence features."
  },
  "important_caveats": [
    "The current UniProt entry (v62) has a 250 AA sequence that mismatches the supplied 237 AA sequence; the historical v60 (sequence version 1) matches exactly. Annotation applicability is qualified by this historical match.",
    "The GO annotation GO:0031176 is IEA:UniProtKB-EC (inferred from EC number), not a direct experimental GO annotation, though the EC assignment itself has experimental support (PubMed:18720841).",
    "The protein is also described as an 'ethylene-inducing' elicitor of plant defense, meaning it has a secondary biological role beyond xylan hydrolysis; however, its primary molecular function (catalytic activity) is endo-1,4-beta-xylanase.",
    "The reviewer-only accession and metadata were absent from the evaluated model input; reasoning must rely on the sequence and general biology alone."
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
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

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
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** mismatch.  
**Retrieved:** 2026-11-01T06:25:06.423596+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"18720841","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"33205907","source":"PubMed"}],"value":"Endo-1,4-beta-xylanase involved in the hydrolysis of xylan, a major structural heterogeneous polysaccharide found in plant biomass representing the second most abundant polysaccharide in the biosphere, after cellulose. The most favorable substrate is beechwood xylan (PubMed:18720841). May act as an elicitor of plant defense responses in certain plants but does not exhibit any cell death when transiently expressed in N.benthamiana (PubMed:33205907)"}]}
```

Source SHA-256: `b6bf3dd61dab32b344f08d226c011b7c3f3936305e457046c933fe6555956510`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2X0L1.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** mismatch.  
**Retrieved:** 2026-11-01T06:25:06.423596+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"3.2.1.8","evidences":[{"evidenceCode":"ECO:0000269","id":"18720841","source":"PubMed"}],"name":"Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans."}}
```

Source SHA-256: `b6bf3dd61dab32b344f08d226c011b7c3f3936305e457046c933fe6555956510`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2X0L1.json)  
**Locator:** `/uniProtKBCrossReferences/20`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** mismatch.  
**Retrieved:** 2026-11-01T06:25:06.423596+00:00.  

```json
{"database":"GO","id":"GO:0031176","properties":[{"key":"GoTerm","value":"F:endo-1,4-beta-xylanase activity"},{"key":"GoEvidenceType","value":"IEA:UniProtKB-EC"}]}
```

Source SHA-256: `b6bf3dd61dab32b344f08d226c011b7c3f3936305e457046c933fe6555956510`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2X0L1.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** mismatch.  
**Retrieved:** 2026-11-01T06:25:06.423596+00:00.  

```json
{"citation":{"authors":["Zhang G.","Rao B.","Ye J.","Ma L.","Zhang X."],"citationCrossReferences":[{"database":"PubMed","id":"18720841"}],"citationType":"journal article","firstPage":"765","id":"18720841","journal":"Wei Sheng Wu Xue Bao","lastPage":"771","publicationDate":"2008","title":"Molecular cloning and heterologous expression of a new xylanase gene from Verticillium dahliae.","volume":"48"},"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [GENOMIC DNA]","SUBCELLULAR LOCATION","FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES"]}
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

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G2X0L1?format=txt&versions=60)  
**Locator:** `lines 37-43`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 60 / 1.  
**Retrieved:** 2026-11-01T06:28:04.256317+00:00.  

```text
CC   -!- FUNCTION: Endo-1,4-beta-xylanase involved in the hydrolysis of xylan, a
CC       major structural heterogeneous polysaccharide found in plant biomass
CC       representing the second most abundant polysaccharide in the biosphere,
CC       after cellulose (By similarity). May act as an elicitor of plant
CC       defense responses in certain plants but does not exhibit any cell death
CC       when transiently expressed in N.benthamiana (PubMed:33205907).
CC       {ECO:0000250|UniProtKB:B3VSG7, ECO:0000269|PubMed:33205907}.
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

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G2X0L1?format=txt&versions=60)  
**Locator:** `lines 71-71`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 60 / 1.  
**Retrieved:** 2026-11-01T06:28:04.256317+00:00.  

```text
DR   GO; GO:0031176; F:endo-1,4-beta-xylanase activity; IEA:UniProtKB-EC.
```

Source SHA-256: `fdadd4e4d52d68a34b5b3ac543b98fcb1301387253e8b3d7575373dd73f1aa2a`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 75. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
