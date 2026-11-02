# GO_molecular_function_0086

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **C** — phosphoprotein phosphatase activity

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | contradicted | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | contradicted | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MRTTLTGTASVLDTTLTRLIDDVIENGSSFLADDENLQHYKQHLSHLETASKIALLRECLCVRPPLPLLPEDLLQNVDSILTRVRQHKILTPIFSLSPSRLIKHGDLGATRIHLWRGDITTLTGVTAITNAANSQGLGCFQPTHRCIDNIIHAEAGPRLREECFQRMQARGKELEPGEVLVTEGHALFASSVMHTVGPQLKRGASPTETERRQLAKCYESILEALELLPSDEDGSKSIALCCISTGLFAFPADEAAEIAVSTVTSWLQKHPSTTITDVIFNTFTQSDTEFYSKLLGPSHTKSISPVENTPQGSLSLAREWLSSADAVLVTAGAGLSAAEGLDYHSRDLFKRNFPGCLKFGLTSLYSVFGFNDWPSEEHRWGYFFTHLNMVANWSNTPTYQILIPWLRNFGQDAFVRTSNADGLFLANGWPKEQLSTPQGSYGYLQCLNNCRVDAVVPSAPLVADAMPHIDKATQKLMDPSKIPLCRFCGSKMSICVRAGSWFNQAPYQEGEAQWKAWKSRVLREKKNLVILELGVGMNTPGVLRWPNEDLVMRSDGRVKLIRVGMGPEAMVPWEQEDEGLSTCVQGDIGRAIPLLLE

[Multiple Choices]
A. glucose-6-phosphate isomerase activity
B. chromatin DNA binding
C. phosphoprotein phosphatase activity
D. protein heterodimerization activity
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

### Expected-answer support: contradicted

> The exact sequence match is annotated as a probable ADP-ribosyl hydrolase/transferase, with experimental evidence for hydrolysis of ADP-ribosyl-glutamate bonds. That reaction is not phosphoprotein dephosphorylation, so choice C is not supported as the answer. The evidence does not exhaustively rule out an additional activity.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence offers no clear general biological argument for phosphoprotein phosphatase activity over the other choices; identifying its particular enzyme function requires protein-specific knowledge. The documented activity is not represented among the options.


**Missing item-specific fact**

> The protein-specific ADP-ribosyl hydrolase/transferase activity, established by annotation and reported experimental evidence, is absent from the input.


**Reason**

> A precise assignment cannot be justified merely from broad sequence features. Recognizing this protein or consulting a function annotation would supply the needed item-specific information, and would show that none of the listed activities accurately describes the documented catalytic function.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No listed option matches the documented ADP-ribosyl hydrolase/transferase activity. The evidence does not establish that any option is a correct alternative.


### Important caveats

- The experimental evidence supports ADP-ribosyl hydrolase activity in vitro; the bifunctional hydrolase/transferase designation is qualified as probable.
- The sequence matches the cited UniProt record, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence offers no clear general biological argument for phosphoprotein phosphatase activity over the other choices; identifying its particular enzyme function requires protein-specific knowledge. The documented activity is not represented among the options.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific ADP-ribosyl hydrolase/transferase activity, established by annotation and reported experimental evidence, is absent from the input.",
    "reason": "A precise assignment cannot be justified merely from broad sequence features. Recognizing this protein or consulting a function annotation would supply the needed item-specific information, and would show that none of the listed activities accurately describes the documented catalytic function."
  },
  "case_id": "GO_molecular_function_0086",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "contradicted",
    "reason": "The exact sequence match is annotated as a probable ADP-ribosyl hydrolase/transferase, with experimental evidence for hydrolysis of ADP-ribosyl-glutamate bonds. That reaction is not phosphoprotein dephosphorylation, so choice C is not supported as the answer. The evidence does not exhaustively rule out an additional activity."
  },
  "important_caveats": [
    "The experimental evidence supports ADP-ribosyl hydrolase activity in vitro; the bifunctional hydrolase/transferase designation is qualified as probable.",
    "The sequence matches the cited UniProt record, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No listed option matches the documented ADP-ribosyl hydrolase/transferase activity. The evidence does not establish that any option is a correct alternative."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0086",
  "expected_answer_check": {
    "judgment": "contradicted",
    "reason": "The exact sequence match is annotated as a probable ADP-ribosyl hydrolase/transferase, with experimental evidence for hydrolysis of ADP-ribosyl-glutamate bonds. That reaction is not phosphoprotein dephosphorylation, so choice C is not supported as the answer. The evidence does not exhaustively rule out an additional activity.",
    "evidence_ids": ["C4", "C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence offers no clear general biological argument for phosphoprotein phosphatase activity over the other choices; identifying its particular enzyme function requires protein-specific knowledge. The documented activity is not represented among the options.",
    "missing_item_specific_fact": "The protein-specific ADP-ribosyl hydrolase/transferase activity, established by annotation and reported experimental evidence, is absent from the input.",
    "reason": "A precise assignment cannot be justified merely from broad sequence features. Recognizing this protein or consulting a function annotation would supply the needed item-specific information, and would show that none of the listed activities accurately describes the documented catalytic function."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No listed option matches the documented ADP-ribosyl hydrolase/transferase activity. The evidence does not establish that any option is a correct alternative."
  },
  "important_caveats": [
    "The experimental evidence supports ADP-ribosyl hydrolase activity in vitro; the bifunctional hydrolase/transferase designation is qualified as probable.",
    "The sequence matches the cited UniProt record, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: contradicted

> The protein A0A559KX76 (Foc1Mfs1) is annotated as a 'Probable bifunctional ADP-ribose hydrolase/ADP-ribosyltransferase' with experimentally verified ADP-ribosylhydrolase activity (ECO:0000269, PubMed:39270823). Its catalytic reaction is: 5-O-(ADP-D-ribosyl)-L-glutamyl-&#91;protein&#93; + H2O → L-glutamyl-&#91;protein&#93; + ADP-D-ribose + H+. This is mechanistically and chemically distinct from phosphoprotein phosphatase activity (GO:0004721), which catalyzes: phosphoprotein + H2O → protein + phosphate (EC 3.1.3.55). The protein removes ADP-ribose groups, not phosphate groups. The UniProt GO annotations (GO:0016757, GO:0016798, GO:0046872, GO:0016779) do not include GO:0004721. The expected answer C is not supported by any annotation or experimental evidence for this protein.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8), [GO2](#evidence-go2).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> None of the four options accurately describes the protein's actual molecular function (ADP-ribosylhydrolase activity). From the sequence alone, one might identify macrodomain-fold features suggesting ADP-ribose processing, but this would NOT lead to 'phosphoprotein phosphatase activity' — it would lead to 'hydrolase acting on glycosyl bonds' or 'ADP-ribosylhydrolase activity,' neither of which is offered. Distinguishing C from the other options requires knowing the specific protein identity and its (incorrect) benchmark annotation rather than reasoning from sequence features.


**Missing item-specific fact**

> The benchmark's assignment of GO:0004721 (phosphoprotein phosphatase activity) to this protein is not supported by any database annotation or experimental evidence. The actual function is ADP-ribosylhydrolase (EC 3.2.1.-). To select C, a model would need the benchmark's erroneous item-specific label rather than any defensible biological argument from the sequence.


**Reason**

> The protein is a macrodomain-fused SirTM ADP-ribose hydrolase. None of the four choices matches its true function. Selecting C requires accepting an annotation that contradicts the experimental evidence (PubMed:39270823, PDB:8RSN). A model reasoning from sequence would identify macrodomain/ADP-ribose-processing features, not phosphatase activity. The question depends on an item-specific (and apparently erroneous) database assignment.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> None of the four options correctly describes the protein's molecular function. Option C (phosphoprotein phosphatase) is the closest in the very broad sense of 'hydrolase acting on a protein modification,' but it is mechanistically wrong (phosphate removal vs. ADP-ribose removal). Options A, B, and D are clearly unrelated. The question lacks a correct answer among the choices.


### Important caveats

- The expected answer C (phosphoprotein phosphatase activity, GO:0004721) is contradicted by the protein's experimentally verified ADP-ribosylhydrolase activity (PubMed:39270823, PDB:8RSN, 2.22 Å crystal structure with Zn2+).
- The UniProt entry (Swiss-Prot ADRHT_FUSOC) lists no GO:0004721 annotation; the closest listed GO terms are GO:0016798 (hydrolase activity, acting on glycosyl bonds) and GO:0016757 (glycosyltransferase activity).
- The benchmark's correct answer appears to be an annotation error: ADP-ribosylhydrolysis (cleaving ADP-ribose from protein) is fundamentally different from phosphoprotein phosphatase activity (cleaving phosphate from protein).
- The sequence match is confirmed (SHA256 match to A0A559KX76, 597 aa), so the evidence applies to the exact protein in the question.
- The entry was first public 2025-06-18; the benchmark's source snapshot is unknown, but even the earliest Swiss-Prot release (v22, Jan 2026) contains the same ADP-ribosylhydrolase annotation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "None of the four options accurately describes the protein's actual molecular function (ADP-ribosylhydrolase activity). From the sequence alone, one might identify macrodomain-fold features suggesting ADP-ribose processing, but this would NOT lead to 'phosphoprotein phosphatase activity' — it would lead to 'hydrolase acting on glycosyl bonds' or 'ADP-ribosylhydrolase activity,' neither of which is offered. Distinguishing C from the other options requires knowing the specific protein identity and its (incorrect) benchmark annotation rather than reasoning from sequence features.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The benchmark's assignment of GO:0004721 (phosphoprotein phosphatase activity) to this protein is not supported by any database annotation or experimental evidence. The actual function is ADP-ribosylhydrolase (EC 3.2.1.-). To select C, a model would need the benchmark's erroneous item-specific label rather than any defensible biological argument from the sequence.",
    "reason": "The protein is a macrodomain-fused SirTM ADP-ribose hydrolase. None of the four choices matches its true function. Selecting C requires accepting an annotation that contradicts the experimental evidence (PubMed:39270823, PDB:8RSN). A model reasoning from sequence would identify macrodomain/ADP-ribose-processing features, not phosphatase activity. The question depends on an item-specific (and apparently erroneous) database assignment."
  },
  "case_id": "GO_molecular_function_0086",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H3",
      "H4",
      "H5",
      "H6",
      "H7",
      "H8",
      "GO2"
    ],
    "judgment": "contradicted",
    "reason": "The protein A0A559KX76 (Foc1Mfs1) is annotated as a 'Probable bifunctional ADP-ribose hydrolase/ADP-ribosyltransferase' with experimentally verified ADP-ribosylhydrolase activity (ECO:0000269, PubMed:39270823). Its catalytic reaction is: 5-O-(ADP-D-ribosyl)-L-glutamyl-[protein] + H2O → L-glutamyl-[protein] + ADP-D-ribose + H+. This is mechanistically and chemically distinct from phosphoprotein phosphatase activity (GO:0004721), which catalyzes: phosphoprotein + H2O → protein + phosphate (EC 3.1.3.55). The protein removes ADP-ribose groups, not phosphate groups. The UniProt GO annotations (GO:0016757, GO:0016798, GO:0046872, GO:0016779) do not include GO:0004721. The expected answer C is not supported by any annotation or experimental evidence for this protein."
  },
  "important_caveats": [
    "The expected answer C (phosphoprotein phosphatase activity, GO:0004721) is contradicted by the protein's experimentally verified ADP-ribosylhydrolase activity (PubMed:39270823, PDB:8RSN, 2.22 Å crystal structure with Zn2+).",
    "The UniProt entry (Swiss-Prot ADRHT_FUSOC) lists no GO:0004721 annotation; the closest listed GO terms are GO:0016798 (hydrolase activity, acting on glycosyl bonds) and GO:0016757 (glycosyltransferase activity).",
    "The benchmark's correct answer appears to be an annotation error: ADP-ribosylhydrolysis (cleaving ADP-ribose from protein) is fundamentally different from phosphoprotein phosphatase activity (cleaving phosphate from protein).",
    "The sequence match is confirmed (SHA256 match to A0A559KX76, 597 aa), so the evidence applies to the exact protein in the question.",
    "The entry was first public 2025-06-18; the benchmark's source snapshot is unknown, but even the earliest Swiss-Prot release (v22, Jan 2026) contains the same ADP-ribosylhydrolase annotation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "None of the four options correctly describes the protein's molecular function. Option C (phosphoprotein phosphatase) is the closest in the very broad sense of 'hydrolase acting on a protein modification,' but it is mechanistically wrong (phosphate removal vs. ADP-ribose removal). Options A, B, and D are clearly unrelated. The question lacks a correct answer among the choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0086",
  "expected_answer_check": {
    "judgment": "contradicted",
    "reason": "The protein A0A559KX76 (Foc1Mfs1) is annotated as a 'Probable bifunctional ADP-ribose hydrolase/ADP-ribosyltransferase' with experimentally verified ADP-ribosylhydrolase activity (ECO:0000269, PubMed:39270823). Its catalytic reaction is: 5-O-(ADP-D-ribosyl)-L-glutamyl-[protein] + H2O → L-glutamyl-[protein] + ADP-D-ribose + H+. This is mechanistically and chemically distinct from phosphoprotein phosphatase activity (GO:0004721), which catalyzes: phosphoprotein + H2O → protein + phosphate (EC 3.1.3.55). The protein removes ADP-ribose groups, not phosphate groups. The UniProt GO annotations (GO:0016757, GO:0016798, GO:0046872, GO:0016779) do not include GO:0004721. The expected answer C is not supported by any annotation or experimental evidence for this protein.",
    "evidence_ids": ["C4", "C5", "C6", "H3", "H4", "H5", "H6", "H7", "H8", "GO2"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "None of the four options accurately describes the protein's actual molecular function (ADP-ribosylhydrolase activity). From the sequence alone, one might identify macrodomain-fold features suggesting ADP-ribose processing, but this would NOT lead to 'phosphoprotein phosphatase activity' — it would lead to 'hydrolase acting on glycosyl bonds' or 'ADP-ribosylhydrolase activity,' neither of which is offered. Distinguishing C from the other options requires knowing the specific protein identity and its (incorrect) benchmark annotation rather than reasoning from sequence features.",
    "missing_item_specific_fact": "The benchmark's assignment of GO:0004721 (phosphoprotein phosphatase activity) to this protein is not supported by any database annotation or experimental evidence. The actual function is ADP-ribosylhydrolase (EC 3.2.1.-). To select C, a model would need the benchmark's erroneous item-specific label rather than any defensible biological argument from the sequence.",
    "reason": "The protein is a macrodomain-fused SirTM ADP-ribose hydrolase. None of the four choices matches its true function. Selecting C requires accepting an annotation that contradicts the experimental evidence (PubMed:39270823, PDB:8RSN). A model reasoning from sequence would identify macrodomain/ADP-ribose-processing features, not phosphatase activity. The question depends on an item-specific (and apparently erroneous) database assignment."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "None of the four options correctly describes the protein's molecular function. Option C (phosphoprotein phosphatase) is the closest in the very broad sense of 'hydrolase acting on a protein modification,' but it is mechanistically wrong (phosphate removal vs. ADP-ribose removal). Options A, B, and D are clearly unrelated. The question lacks a correct answer among the choices."
  },
  "important_caveats": [
    "The expected answer C (phosphoprotein phosphatase activity, GO:0004721) is contradicted by the protein's experimentally verified ADP-ribosylhydrolase activity (PubMed:39270823, PDB:8RSN, 2.22 Å crystal structure with Zn2+).",
    "The UniProt entry (Swiss-Prot ADRHT_FUSOC) lists no GO:0004721 annotation; the closest listed GO terms are GO:0016798 (hydrolase activity, acting on glycosyl bonds) and GO:0016757 (glycosyltransferase activity).",
    "The benchmark's correct answer appears to be an annotation error: ADP-ribosylhydrolysis (cleaving ADP-ribose from protein) is fundamentally different from phosphoprotein phosphatase activity (cleaving phosphate from protein).",
    "The sequence match is confirmed (SHA256 match to A0A559KX76, 597 aa), so the evidence applies to the exact protein in the question.",
    "The entry was first public 2025-06-18; the benchmark's source snapshot is unknown, but even the earliest Swiss-Prot release (v22, Jan 2026) contains the same ADP-ribosylhydrolase annotation."
  ]
}
```

</details>

## Existing project source checks of Luna’s review

The notes below were prepared for specific claims in the Luna review. They are not independent validation of Qwen’s claims, expert adjudication, or replacement verdicts.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

### Source check 1

**Check:** `reaction_definition_difference_traced`.

> C5/C6 and H3/H4 describe hydrolysis of ADP-ribosyl-glutamate, with explicit inability to hydrolyze an ADP-ribosyl-aspartate bond. This differs from phosphoprotein dephosphorylation.

**Remaining uncertainty:** The reported reaction is relevant; the supplied negative result concerns a different ADP-ribosyl bond, not an exhaustive phosphatase assay.

Evidence checked: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

## Reviewer-only source evidence

**Both reviewers received this source evidence separately from the original question. It was not available to the original evaluated model.** Source support and reasoning from the original sequence/choices are distinct assessments.

**Accession:** `A0A559KX76` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 22. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A559KX76.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:25.184799+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39270823","source":"PubMed"}],"value":"Foc1Mfs1"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000312","id":"WZU87063.1","source":"EMBL"}],"value":"Macrodomain-fused SirTM 1"}}],"includes":[{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39270823","source":"PubMed"}],"value":"3.2.1.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Protein-ADP-ribose hydrolase"}}},{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"P0DN71","source":"UniProtKB"}],"value":"2.4.2.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Probable protein ADP-ribosyltransferase"}}}],"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Probable bifunctional ADP-ribose hydrolase/ADP-ribosyltransferase"}}}
```

Source SHA-256: `52b8d79f7061ab8ceea42642d265f006efbce4efe152e77f8ff22f5e291de2e2`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A559KX76.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:25.184799+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39270823","source":"PubMed"},{"evidenceCode":"ECO:0000305"}],"value":"Is probably a bifunctional enzyme with ADP-ribosyltransferase and ADP-ribosylhydrolase activities (Probable). In vitro, can act as an ADP-ribosylhydrolase that hydrolyzes ADP-ribosyl-glutamate bonds (PubMed:39270823). It can remove the ADP-ribosyl modification from the human mono-ADP-ribosylated PARP1 E988Q mutant, which is primarily modified on glutamate site with only minor aspartate contribution (PubMed:39270823). It cannot hydrolyze the ADP-ribosyl-arpartate bond in ribosylated S.pyogenes GcvH-L (PubMed:39270823)"}]}
```

Source SHA-256: `52b8d79f7061ab8ceea42642d265f006efbce4efe152e77f8ff22f5e291de2e2`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A559KX76.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:25.184799+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"evidences":[{"evidenceCode":"ECO:0000269","id":"39270823","source":"PubMed"}],"name":"5-O-(ADP-D-ribosyl)-L-glutamyl-[protein] + H2O = L-glutamyl-[protein] + ADP-D-ribose + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:58248"},{"database":"Rhea","id":"RHEA-COMP:10208"},{"database":"Rhea","id":"RHEA-COMP:15089"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:29973"},{"database":"ChEBI","id":"CHEBI:57967"},{"database":"ChEBI","id":"CHEBI:142540"}]}}
```

Source SHA-256: `52b8d79f7061ab8ceea42642d265f006efbce4efe152e77f8ff22f5e291de2e2`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A559KX76?format=txt&versions=22)  
**Locator:** `lines 40-48`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 22 / 1.  
**Retrieved:** 2026-11-02T04:25:28.054482+00:00.  

```text
CC   -!- FUNCTION: Is probably a bifunctional enzyme with ADP-ribosyltransferase
CC       and ADP-ribosylhydrolase activities (Probable). In vitro, can act as an
CC       ADP-ribosylhydrolase that hydrolyzes ADP-ribosyl-glutamate bonds
CC       (PubMed:39270823). It can remove the ADP-ribosyl modification from the
CC       human mono-ADP-ribosylated PARP1 E988Q mutant, which is primarily
CC       modified on glutamate site with only minor aspartate contribution
CC       (PubMed:39270823). It cannot hydrolyze the ADP-ribosyl-arpartate bond
CC       in ribosylated S.pyogenes GcvH-L (PubMed:39270823).
CC       {ECO:0000269|PubMed:39270823, ECO:0000305}.
```

Source SHA-256: `ccc24bde8b49d7a5bb0c8ef22b62f586b11fd80f8a26f4fbd799761ee5448140`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A559KX76?format=txt&versions=22)  
**Locator:** `lines 49-54`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 22 / 1.  
**Retrieved:** 2026-11-02T04:25:28.054482+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=5-O-(ADP-D-ribosyl)-L-glutamyl-[protein] + H2O = L-glutamyl-
CC         [protein] + ADP-D-ribose + H(+); Xref=Rhea:RHEA:58248, Rhea:RHEA-
CC         COMP:10208, Rhea:RHEA-COMP:15089, ChEBI:CHEBI:15377,
CC         ChEBI:CHEBI:15378, ChEBI:CHEBI:29973, ChEBI:CHEBI:57967,
CC         ChEBI:CHEBI:142540; Evidence={ECO:0000269|PubMed:39270823};
```

Source SHA-256: `ccc24bde8b49d7a5bb0c8ef22b62f586b11fd80f8a26f4fbd799761ee5448140`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A559KX76?format=txt&versions=22)  
**Locator:** `lines 75-75`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 22 / 1.  
**Retrieved:** 2026-11-02T04:25:28.054482+00:00.  

```text
DR   GO; GO:0016757; F:glycosyltransferase activity; IEA:UniProtKB-KW.
```

Source SHA-256: `ccc24bde8b49d7a5bb0c8ef22b62f586b11fd80f8a26f4fbd799761ee5448140`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A559KX76?format=txt&versions=22)  
**Locator:** `lines 76-76`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 22 / 1.  
**Retrieved:** 2026-11-02T04:25:28.054482+00:00.  

```text
DR   GO; GO:0016798; F:hydrolase activity, acting on glycosyl bonds; IEA:UniProtKB-KW.
```

Source SHA-256: `ccc24bde8b49d7a5bb0c8ef22b62f586b11fd80f8a26f4fbd799761ee5448140`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A559KX76?format=txt&versions=22)  
**Locator:** `lines 77-77`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 22 / 1.  
**Retrieved:** 2026-11-02T04:25:28.054482+00:00.  

```text
DR   GO; GO:0046872; F:metal ion binding; IEA:UniProtKB-KW.
```

Source SHA-256: `ccc24bde8b49d7a5bb0c8ef22b62f586b11fd80f8a26f4fbd799761ee5448140`.

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A559KX76?format=txt&versions=22)  
**Locator:** `lines 78-78`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 22 / 1.  
**Retrieved:** 2026-11-02T04:25:28.054482+00:00.  

```text
DR   GO; GO:0016779; F:nucleotidyltransferase activity; IEA:UniProtKB-KW.
```

Source SHA-256: `ccc24bde8b49d7a5bb0c8ef22b62f586b11fd80f8a26f4fbd799761ee5448140`.

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 48508-48537`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0004721
name: phosphoprotein phosphatase activity
namespace: molecular_function
def: "Catalysis of the reaction: a phosphoprotein + H2O = a protein + phosphate. Together with protein kinases, these enzymes control the state of phosphorylation of cellular proteins and thereby provide an important mechanism for regulating cellular activity." [ISBN:0198547684]
synonym: "phosphoprotein phosphohydrolase activity" EXACT []
synonym: "protein phosphatase activity" EXACT []
synonym: "protein phosphatase-1 activity" NARROW []
synonym: "protein phosphatase-2A activity" NARROW []
synonym: "protein phosphatase-2B activity" NARROW []
synonym: "protein phosphatase-2C activity" NARROW []
xref: EC:3.1.3.55
xref: Reactome:R-HSA-112383 "Hypophosphorylation of RNA Pol II CTD by FCP1P protein"
xref: Reactome:R-HSA-113503 "PP2A mediated localization of RB1 protein in chromatin"
xref: Reactome:R-HSA-1363274 "Dephosphorylation of p107 (RBL1) by PP2A"
xref: Reactome:R-HSA-1363276 "Dephosphorylation of p130 (RBL2) by PP2A"
xref: Reactome:R-HSA-167072 "Hypophosphorylation of RNA Pol II CTD by FCP1P protein"
xref: Reactome:R-HSA-170153 "Dephosphorylation of nuclear Cyclin B1:phospho-Cdc2 (Thr 14, Tyr15) complexes by Cdc25 phosphatases"
xref: Reactome:R-HSA-170158 "CDC25A dephosphorylates CCNA:CDK1"
xref: Reactome:R-HSA-170161 "Dephosphorylation of cytoplasmic Cyclin B1/B2:phospho-Cdc2 (Thr 14, Tyr 15) complexes by CDC25B"
xref: Reactome:R-HSA-174110 "Cdc25A mediated dephosphorylation of Cyclin A:phospho-Cdk2"
xref: Reactome:R-HSA-174124 "Dephosphorylation of phospho-Cdh1"
xref: Reactome:R-HSA-178178 "PP1 dephosphorylates TGFBR1"
xref: Reactome:R-HSA-2529015 "Dephosphorylation of CK2-modified condensin I"
xref: Reactome:R-HSA-69199 "Dephosphorylation of Cyclin E:Cdk2 complexes by Cdc25A"
xref: Reactome:R-HSA-9636684 "NdkA dephosphorylates RAB5A:GTP,RAB7A:GTP"
is_a: GO:0016791 ! phosphatase activity
is_a: GO:0140096 ! catalytic activity, acting on a protein
property_value: skos:narrowMatch EC:3.1.3.55

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 86. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
