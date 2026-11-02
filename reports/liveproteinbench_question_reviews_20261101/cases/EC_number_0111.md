# EC_number_0111

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **B** — 2.7.11.1

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MELVLCFVIITISGVIRESSALLLRSPTSNDVFGELVASAERAQPLATRLTKRISRLNFNDREDDFWEDHGDASWNNSYTLVNGRTTLGSENRRRPASHSLIERPYYRDGRLSPVLGVQERRGRSVHSYHEEPVSFFDQRAFDEYTFRRRSQLHRQRARAGLRSRIKQNVRRLWTSARGAVRGWGRRVRRKIGDLFVGHLMPQLRRLRFWDQGLPPVVPPLIGNEPGQASVALVAERMEARLREKTLTEKNPTEAQQAVGTYLINSAENTWFISIPGGRYILLKKRGFLGGGGFGLVYHVEHPTTGQPFALKIFVQRVMNNEVGDKISDLIEDEFGVMKYFPPEWTPARMYSELRFMVPLLKLRVLGKPEFQDARNHLRIFSVCALFPKAQGDLEEAAALLADMDRTNAYNMRMSSTIQMVKLLARFHAFGLVHGDVKLQNFLVDKSGLLLLSDFTQILRTNERRYPPVVTVLYMSPEIATCLITRLRNAIPYTAEIDSWMLGISLYRLWCGDFPFGITLDATALQVAGIVIRSSASSLDFASCHDIPEQFREMIVGFLRKTPGVRLSPQQALEQFSLLNWKGPSPASDTASESEPVSTEEAALLQKE

[Multiple Choices]
A. 2.7.11.24
B. 2.7.11.1
C. 3.2.1.55
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

> The exact sequence matches the UniProt entry for Toxoplasma gondii ROP17. That entry assigns EC 2.7.11.1 and records a protein-phosphorylation reaction with experimental evidence attribution (ECO:0000269). The cited primary study is identified in the annotation, though it was not independently reviewed here.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is consistent with a protein kinase, but that general inference does not distinguish EC 2.7.11.1 from the other kinase option, 2.7.11.24; the non-kinase options are less consistent with the sequence.


**Missing item-specific fact**

> The specific functional identification of this sequence as T. gondii ROP17 and its annotated catalytic activity are not supplied in the question.


**Reason**

> Choosing between the two kinase EC numbers requires protein-specific functional or homology information beyond the general kinase features inferable from the sequence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The matched-record annotation supports B. The sequence alone may not distinguish the kinase subclasses, but the reviewer evidence does not support another listed EC as an alternative for this protein.


### Important caveats

- The UniProt record and its evidence attribution support the key, but the cited primary paper was not independently assessed.
- The reviewer-only accession and annotations were not provided to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a protein kinase, but that general inference does not distinguish EC 2.7.11.1 from the other kinase option, 2.7.11.24; the non-kinase options are less consistent with the sequence.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific functional identification of this sequence as T. gondii ROP17 and its annotated catalytic activity are not supplied in the question.",
    "reason": "Choosing between the two kinase EC numbers requires protein-specific functional or homology information beyond the general kinase features inferable from the sequence."
  },
  "case_id": "EC_number_0111",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H1",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry for Toxoplasma gondii ROP17. That entry assigns EC 2.7.11.1 and records a protein-phosphorylation reaction with experimental evidence attribution (ECO:0000269). The cited primary study is identified in the annotation, though it was not independently reviewed here."
  },
  "important_caveats": [
    "The UniProt record and its evidence attribution support the key, but the cited primary paper was not independently assessed.",
    "The reviewer-only accession and annotations were not provided to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched-record annotation supports B. The sequence alone may not distinguish the kinase subclasses, but the reviewer evidence does not support another listed EC as an alternative for this protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0111",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry for Toxoplasma gondii ROP17. That entry assigns EC 2.7.11.1 and records a protein-phosphorylation reaction with experimental evidence attribution (ECO:0000269). The cited primary study is identified in the annotation, though it was not independently reviewed here.",
    "evidence_ids": ["C1", "C4", "C5", "H1", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is consistent with a protein kinase, but that general inference does not distinguish EC 2.7.11.1 from the other kinase option, 2.7.11.24; the non-kinase options are less consistent with the sequence.",
    "missing_item_specific_fact": "The specific functional identification of this sequence as T. gondii ROP17 and its annotated catalytic activity are not supplied in the question.",
    "reason": "Choosing between the two kinase EC numbers requires protein-specific functional or homology information beyond the general kinase features inferable from the sequence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched-record annotation supports B. The sequence alone may not distinguish the kinase subclasses, but the reviewer evidence does not support another listed EC as an alternative for this protein."
  },
  "important_caveats": [
    "The UniProt record and its evidence attribution support the key, but the cited primary paper was not independently assessed.",
    "The reviewer-only accession and annotations were not provided to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q2PAY3 (ROP17_TOXGO) assigns EC 2.7.11.1 (Serine/threonine-protein kinase) with evidence code ECO:0000269 (inferred from direct assay) from PubMed 24832449 (Etheridge et al. 2014, Cell Host Microbe). Catalytic activity reactions for both Ser and Thr phosphorylation with ATP are annotated. The sequence (608 AA) matches the benchmark input exactly. This is experimental evidence, not merely computational inference.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H2](#evidence-h2), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> In principle, a model could attempt to identify kinase-like features (glycine-rich loop, catalytic domain architecture) to eliminate C (glycosidase) and D (monooxygenase), and note the absence of MEKK4-specific domains (SH3, CRD) to argue against A (2.7.11.24). However, ROP17 is a pseudokinase with highly divergent catalytic residues: the canonical VAIK lysine is absent, HRD→HGD, and DFG→DFP substitutions are present. This makes reliable kinase-motif recognition from sequence alone unreliable.


**Missing item-specific fact**

> The specific experimental demonstration (Etheridge et al. 2014) that ROP17 phosphorylates IRG proteins (Irga6, Irgb6) and the resulting EC 2.7.11.1 assignment. Without knowing this is ROP17 and its characterized substrates, the distinction between 2.7.11.1 (general Ser/Thr kinase) and 2.7.11.24 (MEKK4/MAP3K4) cannot be resolved from sequence alone, especially given the pseudokinase divergence.


**Reason**

> While options C and D (glycosidase, monooxygenase) could potentially be eliminated by recognizing any kinase-like fold, the critical A-vs-B distinction (general Ser/Thr kinase vs. MEKK4) requires knowledge that ROP17 is not a MAP-kinase-pathway component and its specific experimental characterization. The pseudokinase nature of ROP17 means canonical kinase motifs are absent or highly modified, undermining sequence-based reasoning for even the broad kinase classification.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> Both A (2.7.11.24, MEKK4) and B (2.7.11.1, general Ser/Thr kinase) are Ser/Thr protein kinases. Without clear MEKK4-specific domain architecture visible in the sequence (the protein lacks SH3 and CRD domains typical of MEKK4), and given the pseudokinase divergence, a model could reasonably hesitate between these two kinase EC numbers. The distinction ultimately rests on substrate specificity knowledge not derivable from the sequence.


### Important caveats

- ROP17 is classified as a pseudokinase with non-canonical catalytic residues (HGD instead of HRD, DFP instead of DFG), making standard kinase-motif detection unreliable.
- The EC 2.7.11.1 assignment is based on experimental kinase assay data (ECO:0000269), not sequence homology or computational prediction.
- The sequence is 608 AA and includes an N-terminal signal peptide and rhoptry-targeting region, with the kinase-like domain in the C-terminal portion.
- EC 2.7.11.1 is the 'default' Ser/Thr kinase EC number used when no more specific subclassification applies; this is a database classification convention rather than a mechanistically distinct reaction.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "In principle, a model could attempt to identify kinase-like features (glycine-rich loop, catalytic domain architecture) to eliminate C (glycosidase) and D (monooxygenase), and note the absence of MEKK4-specific domains (SH3, CRD) to argue against A (2.7.11.24). However, ROP17 is a pseudokinase with highly divergent catalytic residues: the canonical VAIK lysine is absent, HRD→HGD, and DFG→DFP substitutions are present. This makes reliable kinase-motif recognition from sequence alone unreliable.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific experimental demonstration (Etheridge et al. 2014) that ROP17 phosphorylates IRG proteins (Irga6, Irgb6) and the resulting EC 2.7.11.1 assignment. Without knowing this is ROP17 and its characterized substrates, the distinction between 2.7.11.1 (general Ser/Thr kinase) and 2.7.11.24 (MEKK4/MAP3K4) cannot be resolved from sequence alone, especially given the pseudokinase divergence.",
    "reason": "While options C and D (glycosidase, monooxygenase) could potentially be eliminated by recognizing any kinase-like fold, the critical A-vs-B distinction (general Ser/Thr kinase vs. MEKK4) requires knowledge that ROP17 is not a MAP-kinase-pathway component and its specific experimental characterization. The pseudokinase nature of ROP17 means canonical kinase motifs are absent or highly modified, undermining sequence-based reasoning for even the broad kinase classification."
  },
  "case_id": "EC_number_0111",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "H2",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q2PAY3 (ROP17_TOXGO) assigns EC 2.7.11.1 (Serine/threonine-protein kinase) with evidence code ECO:0000269 (inferred from direct assay) from PubMed 24832449 (Etheridge et al. 2014, Cell Host Microbe). Catalytic activity reactions for both Ser and Thr phosphorylation with ATP are annotated. The sequence (608 AA) matches the benchmark input exactly. This is experimental evidence, not merely computational inference."
  },
  "important_caveats": [
    "ROP17 is classified as a pseudokinase with non-canonical catalytic residues (HGD instead of HRD, DFP instead of DFG), making standard kinase-motif detection unreliable.",
    "The EC 2.7.11.1 assignment is based on experimental kinase assay data (ECO:0000269), not sequence homology or computational prediction.",
    "The sequence is 608 AA and includes an N-terminal signal peptide and rhoptry-targeting region, with the kinase-like domain in the C-terminal portion.",
    "EC 2.7.11.1 is the 'default' Ser/Thr kinase EC number used when no more specific subclassification applies; this is a database classification convention rather than a mechanistically distinct reaction."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "Both A (2.7.11.24, MEKK4) and B (2.7.11.1, general Ser/Thr kinase) are Ser/Thr protein kinases. Without clear MEKK4-specific domain architecture visible in the sequence (the protein lacks SH3 and CRD domains typical of MEKK4), and given the pseudokinase divergence, a model could reasonably hesitate between these two kinase EC numbers. The distinction ultimately rests on substrate specificity knowledge not derivable from the sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0111",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q2PAY3 (ROP17_TOXGO) assigns EC 2.7.11.1 (Serine/threonine-protein kinase) with evidence code ECO:0000269 (inferred from direct assay) from PubMed 24832449 (Etheridge et al. 2014, Cell Host Microbe). Catalytic activity reactions for both Ser and Thr phosphorylation with ATP are annotated. The sequence (608 AA) matches the benchmark input exactly. This is experimental evidence, not merely computational inference.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H2", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "In principle, a model could attempt to identify kinase-like features (glycine-rich loop, catalytic domain architecture) to eliminate C (glycosidase) and D (monooxygenase), and note the absence of MEKK4-specific domains (SH3, CRD) to argue against A (2.7.11.24). However, ROP17 is a pseudokinase with highly divergent catalytic residues: the canonical VAIK lysine is absent, HRD→HGD, and DFG→DFP substitutions are present. This makes reliable kinase-motif recognition from sequence alone unreliable.",
    "missing_item_specific_fact": "The specific experimental demonstration (Etheridge et al. 2014) that ROP17 phosphorylates IRG proteins (Irga6, Irgb6) and the resulting EC 2.7.11.1 assignment. Without knowing this is ROP17 and its characterized substrates, the distinction between 2.7.11.1 (general Ser/Thr kinase) and 2.7.11.24 (MEKK4/MAP3K4) cannot be resolved from sequence alone, especially given the pseudokinase divergence.",
    "reason": "While options C and D (glycosidase, monooxygenase) could potentially be eliminated by recognizing any kinase-like fold, the critical A-vs-B distinction (general Ser/Thr kinase vs. MEKK4) requires knowledge that ROP17 is not a MAP-kinase-pathway component and its specific experimental characterization. The pseudokinase nature of ROP17 means canonical kinase motifs are absent or highly modified, undermining sequence-based reasoning for even the broad kinase classification."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "Both A (2.7.11.24, MEKK4) and B (2.7.11.1, general Ser/Thr kinase) are Ser/Thr protein kinases. Without clear MEKK4-specific domain architecture visible in the sequence (the protein lacks SH3 and CRD domains typical of MEKK4), and given the pseudokinase divergence, a model could reasonably hesitate between these two kinase EC numbers. The distinction ultimately rests on substrate specificity knowledge not derivable from the sequence."
  },
  "important_caveats": [
    "ROP17 is classified as a pseudokinase with non-canonical catalytic residues (HGD instead of HRD, DFP instead of DFG), making standard kinase-motif detection unreliable.",
    "The EC 2.7.11.1 assignment is based on experimental kinase assay data (ECO:0000269), not sequence homology or computational prediction.",
    "The sequence is 608 AA and includes an N-terminal signal peptide and rhoptry-targeting region, with the kinase-like domain in the C-terminal portion.",
    "EC 2.7.11.1 is the 'default' Ser/Thr kinase EC number used when no more specific subclassification applies; this is a database classification convention rather than a mechanistically distinct reaction."
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

**Accession:** `Q2PAY3` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 86. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2PAY3.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:36.273311+00:00.  

```json
"Q2PAY3"
```

Source SHA-256: `6706ba31663e0eeb6d66fbdf81baeb771e31266ea82e6b187e4763189ddeb230`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2PAY3.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:36.273311+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000312","id":"CAJ27112.1","source":"EMBL"}],"value":"Rhoptry protein 17"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"34180401","source":"PubMed"}],"value":"TgROP17"}}],"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"24832449","source":"PubMed"}],"value":"2.7.11.1"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Serine/threonine-protein kinase ROP17"}}}
```

Source SHA-256: `6706ba31663e0eeb6d66fbdf81baeb771e31266ea82e6b187e4763189ddeb230`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2PAY3.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:36.273311+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"2.7.11.1","evidences":[{"evidenceCode":"ECO:0000269","id":"24832449","source":"PubMed"}],"name":"L-threonyl-[protein] + ATP = O-phospho-L-threonyl-[protein] + ADP + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:46608"},{"database":"Rhea","id":"RHEA-COMP:11060"},{"database":"Rhea","id":"RHEA-COMP:11605"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:30013"},{"database":"ChEBI","id":"CHEBI:30616"},{"database":"ChEBI","id":"CHEBI:61977"},{"database":"ChEBI","id":"CHEBI:456216"}]}}
```

Source SHA-256: `6706ba31663e0eeb6d66fbdf81baeb771e31266ea82e6b187e4763189ddeb230`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2PAY3.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:36.273311+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"2.7.11.1","evidences":[{"evidenceCode":"ECO:0000305","id":"24832449","source":"PubMed"}],"name":"L-seryl-[protein] + ATP = O-phospho-L-seryl-[protein] + ADP + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:17989"},{"database":"Rhea","id":"RHEA-COMP:9863"},{"database":"Rhea","id":"RHEA-COMP:11604"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:29999"},{"database":"ChEBI","id":"CHEBI:30616"},{"database":"ChEBI","id":"CHEBI:83421"},{"database":"ChEBI","id":"CHEBI:456216"}]}}
```

Source SHA-256: `6706ba31663e0eeb6d66fbdf81baeb771e31266ea82e6b187e4763189ddeb230`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2PAY3.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:36.273311+00:00.  

```json
{"citation":{"authors":["Etheridge R.D.","Alaganan A.","Tang K.","Lou H.J.","Turk B.E.","Sibley L.D."],"citationCrossReferences":[{"database":"PubMed","id":"24832449"},{"database":"DOI","id":"10.1016/j.chom.2014.04.002"}],"citationType":"journal article","firstPage":"537","id":"24832449","journal":"Cell Host Microbe","lastPage":"550","publicationDate":"2014","title":"The Toxoplasma pseudokinase ROP5 forms complexes with ROP18 and ROP17 kinases that synergize to control acute virulence in mice.","volume":"15"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":2,"referencePositions":["IDENTIFICATION BY MASS SPECTROMETRY","FUNCTION","CATALYTIC ACTIVITY","INTERACTION WITH ROP5","SUBCELLULAR LOCATION","DISRUPTION PHENOTYPE"]}
```

Source SHA-256: `6706ba31663e0eeb6d66fbdf81baeb771e31266ea82e6b187e4763189ddeb230`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2PAY3?format=txt&versions=86)  
**Locator:** `lines 1-15`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 86 / 1.  
**Retrieved:** 2026-11-02T04:30:38.452820+00:00.  

```text
ID   ROP17_TOXGO             Reviewed;         608 AA.
AC   Q2PAY3;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   07-FEB-2006, sequence version 1.
DT   28-JAN-2026, entry version 86.
DE   RecName: Full=Serine/threonine-protein kinase ROP17 {ECO:0000305};
DE            EC=2.7.11.1 {ECO:0000269|PubMed:24832449};
DE   AltName: Full=Rhoptry protein 17 {ECO:0000312|EMBL:CAJ27112.1};
DE   AltName: Full=TgROP17 {ECO:0000303|PubMed:34180401};
DE   Flags: Precursor;
GN   Name=rop17 {ECO:0000312|EMBL:CAJ27112.1};
OS   Toxoplasma gondii.
OC   Eukaryota; Sar; Alveolata; Apicomplexa; Conoidasida; Coccidia;
OC   Eucoccidiorida; Eimeriorina; Sarcocystidae; Toxoplasma.
OX   NCBI_TaxID=5811 {ECO:0000312|EMBL:CAJ27112.1};
```

Source SHA-256: `b556cca06da62f63e90c588009b9095a040ad3bb5a30da56151ae475acf8019a`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2PAY3?format=txt&versions=86)  
**Locator:** `lines 6-10`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 86 / 1.  
**Retrieved:** 2026-11-02T04:30:38.452820+00:00.  

```text
DE   RecName: Full=Serine/threonine-protein kinase ROP17 {ECO:0000305};
DE            EC=2.7.11.1 {ECO:0000269|PubMed:24832449};
DE   AltName: Full=Rhoptry protein 17 {ECO:0000312|EMBL:CAJ27112.1};
DE   AltName: Full=TgROP17 {ECO:0000303|PubMed:34180401};
DE   Flags: Precursor;
```

Source SHA-256: `b556cca06da62f63e90c588009b9095a040ad3bb5a30da56151ae475acf8019a`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2PAY3?format=txt&versions=86)  
**Locator:** `lines 85-90`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 86 / 1.  
**Retrieved:** 2026-11-02T04:30:38.452820+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=L-threonyl-[protein] + ATP = O-phospho-L-threonyl-[protein] +
CC         ADP + H(+); Xref=Rhea:RHEA:46608, Rhea:RHEA-COMP:11060, Rhea:RHEA-
CC         COMP:11605, ChEBI:CHEBI:15378, ChEBI:CHEBI:30013, ChEBI:CHEBI:30616,
CC         ChEBI:CHEBI:61977, ChEBI:CHEBI:456216; EC=2.7.11.1;
CC         Evidence={ECO:0000269|PubMed:24832449};
```

Source SHA-256: `b556cca06da62f63e90c588009b9095a040ad3bb5a30da56151ae475acf8019a`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2PAY3?format=txt&versions=86)  
**Locator:** `lines 91-96`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 86 / 1.  
**Retrieved:** 2026-11-02T04:30:38.452820+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=L-seryl-[protein] + ATP = O-phospho-L-seryl-[protein] + ADP +
CC         H(+); Xref=Rhea:RHEA:17989, Rhea:RHEA-COMP:9863, Rhea:RHEA-
CC         COMP:11604, ChEBI:CHEBI:15378, ChEBI:CHEBI:29999, ChEBI:CHEBI:30616,
CC         ChEBI:CHEBI:83421, ChEBI:CHEBI:456216; EC=2.7.11.1;
CC         Evidence={ECO:0000305|PubMed:24832449};
```

Source SHA-256: `b556cca06da62f63e90c588009b9095a040ad3bb5a30da56151ae475acf8019a`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 111. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
