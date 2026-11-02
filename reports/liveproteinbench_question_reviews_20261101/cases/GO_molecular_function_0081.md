# GO_molecular_function_0081

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **B** — calcium ion binding

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
GSITTVLNATDIAKALAQCAGSFNHKTFFVTSGLTNKSDANLAKVFDILDQDRSGFIEVDELKLFLQNFSATARELDETETNAFLAAGDSDHDGKIGVDEFKAMVKA

[Multiple Choices]
A. alpha-1,6-mannosyltransferase activity
B. calcium ion binding
C. oxidoreductase activity, acting on the CH-CH group of donors, NAD or NADP as acceptor
D. UMP/dUMP kinase activity
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

> The exact sequence match is annotated for calcium ion binding, with an experimental GO annotation (IDA). The entry also reports binding two calcium ions and cites a calcium-bound crystal structure.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The short, predominantly helical sequence is consistent with a small EF-hand calcium-binding protein; its calcium-binding loops provide a biological basis for choosing B over the listed enzyme activities, which would generally require catalytic and cofactor-binding features.


**Missing item-specific fact**

> The experimental calcium-binding annotation is not supplied, but is not necessary for a defensible sequence-based inference at this choice level.


**Reason**

> A recognizable calcium-binding protein motif and the sequence's compact, non-enzyme-like character meaningfully distinguish B without relying on remembering this exact protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed choices, calcium ion binding is the distinctively plausible function; the other choices describe unrelated catalytic activities.


### Important caveats

- The sequence alone supports an inference, not direct proof of experimentally measured calcium binding.
- The reviewer-only database and structural evidence supports the key but was not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The short, predominantly helical sequence is consistent with a small EF-hand calcium-binding protein; its calcium-binding loops provide a biological basis for choosing B over the listed enzyme activities, which would generally require catalytic and cofactor-binding features.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The experimental calcium-binding annotation is not supplied, but is not necessary for a defensible sequence-based inference at this choice level.",
    "reason": "A recognizable calcium-binding protein motif and the sequence's compact, non-enzyme-like character meaningfully distinguish B without relying on remembering this exact protein's database entry."
  },
  "case_id": "GO_molecular_function_0081",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence match is annotated for calcium ion binding, with an experimental GO annotation (IDA). The entry also reports binding two calcium ions and cites a calcium-bound crystal structure."
  },
  "important_caveats": [
    "The sequence alone supports an inference, not direct proof of experimentally measured calcium binding.",
    "The reviewer-only database and structural evidence supports the key but was not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, calcium ion binding is the distinctively plausible function; the other choices describe unrelated catalytic activities."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0081",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence match is annotated for calcium ion binding, with an experimental GO annotation (IDA). The entry also reports binding two calcium ions and cites a calcium-bound crystal structure.",
    "evidence_ids": ["C5", "C6", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The short, predominantly helical sequence is consistent with a small EF-hand calcium-binding protein; its calcium-binding loops provide a biological basis for choosing B over the listed enzyme activities, which would generally require catalytic and cofactor-binding features.",
    "missing_item_specific_fact": "The experimental calcium-binding annotation is not supplied, but is not necessary for a defensible sequence-based inference at this choice level.",
    "reason": "A recognizable calcium-binding protein motif and the sequence's compact, non-enzyme-like character meaningfully distinguish B without relying on remembering this exact protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, calcium ion binding is the distinctively plausible function; the other choices describe unrelated catalytic activities."
  },
  "important_caveats": [
    "The sequence alone supports an inference, not direct proof of experimentally measured calcium binding.",
    "The reviewer-only database and structural evidence supports the key but was not available to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A3F2YLV2 (Parvalbumin beta, Mustelus griseus) is annotated with GO:0005509 'calcium ion binding' with evidence code IDA (Inferred from Direct Assay, PubMed:29969026). The FUNCTION comment explicitly states 'It binds two calcium ions,' supported by X-ray crystallography at 1.54 Å in complex with Ca(2+). The sequence in the question matches the UniProt sequence exactly (SHA256 confirmed). This is strong experimental evidence, not mere computational inference.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C9](#evidence-c9), [H1](#evidence-h1), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a textbook EF-hand calcium-binding loop at the C-terminus: D(89)-S-D(91)-H-D(93)-G(94)-K-I-G-V-D(99), matching the canonical D-x-D-x-D-G-x-x-x-x-D consensus (Ca-coordinating positions 1,3,5,7,12). The protein is only 107 residues and rich in acidic residues (D, E), consistent with a small calcium-binding protein. All three distractors describe enzymatic activities (glycosyltransferase, NAD/NADP-dependent oxidoreductase, kinase) that require substantially larger proteins (typically 200–500+ residues) with specific catalytic folds: a Rossmann fold (GxGxxG) for NAD binding, kinase motifs (VAIK, HRD, DFG) for phosphoryl transfer, or glycosyltransferase catalytic domains. None of these motifs are present. The small size, acidic composition, and identifiable EF-hand motif collectively point to calcium ion binding and exclude all three enzymatic options.


**Missing item-specific fact**

> None required. While identifying the protein specifically as 'parvalbumin beta' would require database lookup, the GO molecular function 'calcium ion binding' is inferable from the EF-hand motif, protein size, and absence of catalytic features.


**Reason**

> A model with general knowledge of EF-hand structural motifs and the size/domain requirements of the three enzymatic distractors can eliminate options A, C, and D and select B without memorizing this particular UniProt entry. The EF-hand consensus D-x-D-x-D-G-x-x-x-x-D is clearly present in the sequence, and the 107-residue length is incompatible with any of the three enzyme activities listed.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The three distractors (mannosyltransferase, NAD/NADP oxidoreductase, UMP/dUMP kinase) all require catalytic domains and protein sizes far exceeding 107 residues. No sequence feature supports any of them. Only calcium ion binding is consistent with the observed EF-hand motif, small size, and acidic composition.


### Important caveats

- The reviewer evidence confirms the sequence matches UniProt A0A3F2YLV2 exactly (SHA256 verified), so the annotation applies directly to the supplied sequence.
- The GO annotation is IDA (Inferred from Direct Assay) backed by X-ray crystallography with Ca2+, representing the strongest experimental evidence tier.
- The EF-hand identification from sequence alone requires familiarity with the D-x-D-x-D-G-x-x-x-x-D consensus; a model without this structural biology knowledge might struggle, though the size and composition constraints still eliminate the enzymatic distractors.
- The UniProt entry also annotates identical protein binding (GO:00042802) and protein homodimerization (GO:00042803), but neither appears among the choices, so no ambiguity arises from those.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a textbook EF-hand calcium-binding loop at the C-terminus: D(89)-S-D(91)-H-D(93)-G(94)-K-I-G-V-D(99), matching the canonical D-x-D-x-D-G-x-x-x-x-D consensus (Ca-coordinating positions 1,3,5,7,12). The protein is only 107 residues and rich in acidic residues (D, E), consistent with a small calcium-binding protein. All three distractors describe enzymatic activities (glycosyltransferase, NAD/NADP-dependent oxidoreductase, kinase) that require substantially larger proteins (typically 200–500+ residues) with specific catalytic folds: a Rossmann fold (GxGxxG) for NAD binding, kinase motifs (VAIK, HRD, DFG) for phosphoryl transfer, or glycosyltransferase catalytic domains. None of these motifs are present. The small size, acidic composition, and identifiable EF-hand motif collectively point to calcium ion binding and exclude all three enzymatic options.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None required. While identifying the protein specifically as 'parvalbumin beta' would require database lookup, the GO molecular function 'calcium ion binding' is inferable from the EF-hand motif, protein size, and absence of catalytic features.",
    "reason": "A model with general knowledge of EF-hand structural motifs and the size/domain requirements of the three enzymatic distractors can eliminate options A, C, and D and select B without memorizing this particular UniProt entry. The EF-hand consensus D-x-D-x-D-G-x-x-x-x-D is clearly present in the sequence, and the 107-residue length is incompatible with any of the three enzyme activities listed."
  },
  "case_id": "GO_molecular_function_0081",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C9",
      "H1",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A3F2YLV2 (Parvalbumin beta, Mustelus griseus) is annotated with GO:0005509 'calcium ion binding' with evidence code IDA (Inferred from Direct Assay, PubMed:29969026). The FUNCTION comment explicitly states 'It binds two calcium ions,' supported by X-ray crystallography at 1.54 Å in complex with Ca(2+). The sequence in the question matches the UniProt sequence exactly (SHA256 confirmed). This is strong experimental evidence, not mere computational inference."
  },
  "important_caveats": [
    "The reviewer evidence confirms the sequence matches UniProt A0A3F2YLV2 exactly (SHA256 verified), so the annotation applies directly to the supplied sequence.",
    "The GO annotation is IDA (Inferred from Direct Assay) backed by X-ray crystallography with Ca2+, representing the strongest experimental evidence tier.",
    "The EF-hand identification from sequence alone requires familiarity with the D-x-D-x-D-G-x-x-x-x-D consensus; a model without this structural biology knowledge might struggle, though the size and composition constraints still eliminate the enzymatic distractors.",
    "The UniProt entry also annotates identical protein binding (GO:00042802) and protein homodimerization (GO:00042803), but neither appears among the choices, so no ambiguity arises from those."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors (mannosyltransferase, NAD/NADP oxidoreductase, UMP/dUMP kinase) all require catalytic domains and protein sizes far exceeding 107 residues. No sequence feature supports any of them. Only calcium ion binding is consistent with the observed EF-hand motif, small size, and acidic composition."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0081",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A3F2YLV2 (Parvalbumin beta, Mustelus griseus) is annotated with GO:0005509 'calcium ion binding' with evidence code IDA (Inferred from Direct Assay, PubMed:29969026). The FUNCTION comment explicitly states 'It binds two calcium ions,' supported by X-ray crystallography at 1.54 Å in complex with Ca(2+). The sequence in the question matches the UniProt sequence exactly (SHA256 confirmed). This is strong experimental evidence, not mere computational inference.",
    "evidence_ids": ["C4", "C5", "C6", "C9", "H1", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a textbook EF-hand calcium-binding loop at the C-terminus: D(89)-S-D(91)-H-D(93)-G(94)-K-I-G-V-D(99), matching the canonical D-x-D-x-D-G-x-x-x-x-D consensus (Ca-coordinating positions 1,3,5,7,12). The protein is only 107 residues and rich in acidic residues (D, E), consistent with a small calcium-binding protein. All three distractors describe enzymatic activities (glycosyltransferase, NAD/NADP-dependent oxidoreductase, kinase) that require substantially larger proteins (typically 200–500+ residues) with specific catalytic folds: a Rossmann fold (GxGxxG) for NAD binding, kinase motifs (VAIK, HRD, DFG) for phosphoryl transfer, or glycosyltransferase catalytic domains. None of these motifs are present. The small size, acidic composition, and identifiable EF-hand motif collectively point to calcium ion binding and exclude all three enzymatic options.",
    "missing_item_specific_fact": "None required. While identifying the protein specifically as 'parvalbumin beta' would require database lookup, the GO molecular function 'calcium ion binding' is inferable from the EF-hand motif, protein size, and absence of catalytic features.",
    "reason": "A model with general knowledge of EF-hand structural motifs and the size/domain requirements of the three enzymatic distractors can eliminate options A, C, and D and select B without memorizing this particular UniProt entry. The EF-hand consensus D-x-D-x-D-G-x-x-x-x-D is clearly present in the sequence, and the 107-residue length is incompatible with any of the three enzyme activities listed."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors (mannosyltransferase, NAD/NADP oxidoreductase, UMP/dUMP kinase) all require catalytic domains and protein sizes far exceeding 107 residues. No sequence feature supports any of them. Only calcium ion binding is consistent with the observed EF-hand motif, small size, and acidic composition."
  },
  "important_caveats": [
    "The reviewer evidence confirms the sequence matches UniProt A0A3F2YLV2 exactly (SHA256 verified), so the annotation applies directly to the supplied sequence.",
    "The GO annotation is IDA (Inferred from Direct Assay) backed by X-ray crystallography with Ca2+, representing the strongest experimental evidence tier.",
    "The EF-hand identification from sequence alone requires familiarity with the D-x-D-x-D-G-x-x-x-x-D consensus; a model without this structural biology knowledge might struggle, though the size and composition constraints still eliminate the enzymatic distractors.",
    "The UniProt entry also annotates identical protein binding (GO:00042802) and protein homodimerization (GO:00042803), but neither appears among the choices, so no ambiguity arises from those."
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

**Accession:** `A0A3F2YLV2` (recovered from dataset image-path metadata, not original question text).  
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A3F2YLV2.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:02.949899+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"29969026","source":"PubMed"}],"value":"Beta-parvalbumin"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"29969026","source":"PubMed"}],"value":"Beta-PV"}]},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"29969026","source":"PubMed"}],"value":"Parvalbumin SPV-II"}}],"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Parvalbumin beta"}}}
```

Source SHA-256: `44d775ef756532b6af4379bb6bc175aeb0e7547bd170093c7e087b74a15d5a50`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A3F2YLV2.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:02.949899+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000255","id":"RU368048","source":"RuleBase"},{"evidenceCode":"ECO:0000269","id":"29969026","source":"PubMed"}],"value":"In muscle, parvalbumin is thought to be involved in relaxation after contraction (By similarity). It binds two calcium ions (PubMed:29969026)"}]}
```

Source SHA-256: `44d775ef756532b6af4379bb6bc175aeb0e7547bd170093c7e087b74a15d5a50`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A3F2YLV2.json)  
**Locator:** `/uniProtKBCrossReferences/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:02.949899+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000314","id":"29969026","source":"PubMed"}],"id":"GO:0005509","properties":[{"key":"GoTerm","value":"F:calcium ion binding"},{"key":"GoEvidenceType","value":"IDA:UniProtKB"}]}
```

Source SHA-256: `44d775ef756532b6af4379bb6bc175aeb0e7547bd170093c7e087b74a15d5a50`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A3F2YLV2.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:02.949899+00:00.  

```json
{"citation":{"authors":["Yang R.Q.","Chen Y.L.","Chen F.","Wang H.","Zhang Q.","Liu G.M.","Jin T.","Cao M.J."],"citationCrossReferences":[{"database":"PubMed","id":"29969026"},{"database":"DOI","id":"10.1021/acs.jafc.8b01889"}],"citationType":"journal article","firstPage":"8150","id":"29969026","journal":"J. Agric. Food Chem.","lastPage":"8159","publicationDate":"2018","title":"Purification, Characterization, and Crystal Structure of Parvalbumins, the Major Allergens in Mustelus griseus.","volume":"66"},"evidences":[{"evidenceCode":"ECO:0000312","id":"5ZH6","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"5ZH6","source":"PDB"}],"referenceComments":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"29969026","source":"PubMed"}],"type":"TISSUE","value":"Muscle"}],"referenceNumber":1,"referencePositions":["PROTEIN SEQUENCE OF 64-74","X-RAY CRYSTALLOGRAPHY (1.54 ANGSTROMS) IN COMPLEX WITH CA(2+)","BIOPHYSICOCHEMICAL PROPERTIES","SUBUNIT","TISSUE SPECIFICITY","IDENTIFICATION BY MASS SPECTROMETRY","ALLERGEN","DISULFIDE BOND","CIRCULAR DICHROISM ANALYSIS"]}
```

Source SHA-256: `44d775ef756532b6af4379bb6bc175aeb0e7547bd170093c7e087b74a15d5a50`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A3F2YLV2?format=txt&versions=22)  
**Locator:** `lines 1-14`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 22 / 1.  
**Retrieved:** 2026-11-02T04:25:04.740743+00:00.  

```text
ID   PRVB_MUSGR              Reviewed;         107 AA.
AC   A0A3F2YLV2;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   16-JAN-2019, sequence version 1.
DT   28-JAN-2026, entry version 22.
DE   RecName: Full=Parvalbumin beta {ECO:0000305};
DE   AltName: Full=Beta-parvalbumin {ECO:0000303|PubMed:29969026};
DE            Short=Beta-PV {ECO:0000303|PubMed:29969026};
DE   AltName: Full=Parvalbumin SPV-II {ECO:0000303|PubMed:29969026};
OS   Mustelus griseus (Spotless smooth-hound).
OC   Eukaryota; Metazoa; Chordata; Craniata; Vertebrata; Chondrichthyes;
OC   Elasmobranchii; Galeomorphii; Galeoidea; Carcharhiniformes; Triakidae;
OC   Mustelus.
OX   NCBI_TaxID=89020;
```

Source SHA-256: `046970c8aae1fad2c2c1e167bb041031876576f5b9c4cd5d7fed73b8632fa281`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A3F2YLV2?format=txt&versions=22)  
**Locator:** `lines 15-26`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 22 / 1.  
**Retrieved:** 2026-11-02T04:25:04.740743+00:00.  

```text
RN   [1] {ECO:0000312|PDB:5ZH6, ECO:0007744|PDB:5ZH6}
RP   PROTEIN SEQUENCE OF 64-74, X-RAY CRYSTALLOGRAPHY (1.54 ANGSTROMS) IN
RP   COMPLEX WITH CA(2+), BIOPHYSICOCHEMICAL PROPERTIES, SUBUNIT, TISSUE
RP   SPECIFICITY, IDENTIFICATION BY MASS SPECTROMETRY, ALLERGEN, DISULFIDE BOND,
RP   AND CIRCULAR DICHROISM ANALYSIS.
RC   TISSUE=Muscle {ECO:0000303|PubMed:29969026};
RX   PubMed=29969026; DOI=10.1021/acs.jafc.8b01889;
RA   Yang R.Q., Chen Y.L., Chen F., Wang H., Zhang Q., Liu G.M., Jin T.,
RA   Cao M.J.;
RT   "Purification, Characterization, and Crystal Structure of Parvalbumins, the
RT   Major Allergens in Mustelus griseus.";
RL   J. Agric. Food Chem. 66:8150-8159(2018).
```

Source SHA-256: `046970c8aae1fad2c2c1e167bb041031876576f5b9c4cd5d7fed73b8632fa281`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A3F2YLV2?format=txt&versions=22)  
**Locator:** `lines 27-30`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 22 / 1.  
**Retrieved:** 2026-11-02T04:25:04.740743+00:00.  

```text
CC   -!- FUNCTION: In muscle, parvalbumin is thought to be involved in
CC       relaxation after contraction (By similarity). It binds two calcium ions
CC       (PubMed:29969026). {ECO:0000255|RuleBase:RU368048,
CC       ECO:0000269|PubMed:29969026}.
```

Source SHA-256: `046970c8aae1fad2c2c1e167bb041031876576f5b9c4cd5d7fed73b8632fa281`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A3F2YLV2?format=txt&versions=22)  
**Locator:** `lines 62-62`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 22 / 1.  
**Retrieved:** 2026-11-02T04:25:04.740743+00:00.  

```text
DR   GO; GO:0005509; F:calcium ion binding; IDA:UniProtKB.
```

Source SHA-256: `046970c8aae1fad2c2c1e167bb041031876576f5b9c4cd5d7fed73b8632fa281`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 81. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
