# catalytic_activity_0195

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **D** — L-threonyl-&#91;protein&#93; + ATP = O-phospho-L-threonyl-&#91;protein&#93; + ADP + H(+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MELVLCFVIITISGVIRESSALLLRSPTSNDVFGELVASAERAQPLATRLTKRISRLNFNDREDDFWEDHGDASWNNSYTLVNGRTTLGSENRRRPASHSLIERPYYRDGRLSPVLGVQERRGRSVHSYHEEPVSFFDQRAFDEYTFRRRSQLHRQRARAGLRSRIKQNVRRLWTSARGAVRGWGRRVRRKIGDLFVGHLMPQLRRLRFWDQGLPPVVPPLIGNEPGQASVALVAERMEARLREKTLTEKNPTEAQQAVGTYLINSAENTWFISIPGGRYILLKKRGFLGGGGFGLVYHVEHPTTGQPFALKIFVQRVMNNEVGDKISDLIEDEFGVMKYFPPEWTPARMYSELRFMVPLLKLRVLGKPEFQDARNHLRIFSVCALFPKAQGDLEEAAALLADMDRTNAYNMRMSSTIQMVKLLARFHAFGLVHGDVKLQNFLVDKSGLLLLSDFTQILRTNERRYPPVVTVLYMSPEIATCLITRLRNAIPYTAEIDSWMLGISLYRLWCGDFPFGITLDATALQVAGIVIRSSASSLDFASCHDIPEQFREMIVGFLRKTPGVRLSPQQALEQFSLLNWKGPSPASDTASESEPVSTEEAALLQKE

[Multiple Choices]
A. ATP + H2O = ADP + phosphate + H(+)
B. 2 a Fe(II)-siderophore + NAD(+) + H(+) = 2 a Fe(III)-siderophore + NADH
C. 3-hydroxy-4,5-dimethoxyphenethylamine + S-adenosyl-L-methionine = mescaline + S-adenosyl-L-homocysteine + H(+)
D. L-threonyl-[protein] + ATP = O-phospho-L-threonyl-[protein] + ADP + H(+)
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

> The exact sequence matches the UniProt entry for Toxoplasma gondii ROP17. That entry annotates the threonyl-protein phosphorylation reaction in D and cites experimental evidence (ECO:0000269, PubMed 24832449). This supports the key, though the cited paper was not independently reviewed here.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a kinase-like ATP-binding region, consistent with a protein kinase. Of the choices, D is the protein-phosphorylation reaction; the other options describe ATP hydrolysis, siderophore oxidation, or methyl transfer.


**Missing item-specific fact**

> The sequence alone does not establish this particular kinase's preference for threonine versus serine. That residue-level specificity is supported by the sequence-matched annotation, and the choices do not include a serine-phosphorylation alternative.


**Reason**

> The kinase-like sequence provides a biological basis to select the protein-phosphorylation reaction over the unrelated reaction classes. The precise threonine assignment is less directly inferable from sequence alone, but it does not create a competing listed choice.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> D is the only listed reaction consistent with a protein kinase; ATP use alone does not make the generic ATP-hydrolysis option A an equivalent reaction.


### Important caveats

- The cited annotation provides experimental-evidence attribution, but the underlying primary study was not independently validated here.
- The same entry also annotates serine phosphorylation, which is not offered as a choice.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a kinase-like ATP-binding region, consistent with a protein kinase. Of the choices, D is the protein-phosphorylation reaction; the other options describe ATP hydrolysis, siderophore oxidation, or methyl transfer.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The sequence alone does not establish this particular kinase's preference for threonine versus serine. That residue-level specificity is supported by the sequence-matched annotation, and the choices do not include a serine-phosphorylation alternative.",
    "reason": "The kinase-like sequence provides a biological basis to select the protein-phosphorylation reaction over the unrelated reaction classes. The precise threonine assignment is less directly inferable from sequence alone, but it does not create a competing listed choice."
  },
  "case_id": "catalytic_activity_0195",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry for Toxoplasma gondii ROP17. That entry annotates the threonyl-protein phosphorylation reaction in D and cites experimental evidence (ECO:0000269, PubMed 24832449). This supports the key, though the cited paper was not independently reviewed here."
  },
  "important_caveats": [
    "The cited annotation provides experimental-evidence attribution, but the underlying primary study was not independently validated here.",
    "The same entry also annotates serine phosphorylation, which is not offered as a choice."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "D is the only listed reaction consistent with a protein kinase; ATP use alone does not make the generic ATP-hydrolysis option A an equivalent reaction."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0195",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry for Toxoplasma gondii ROP17. That entry annotates the threonyl-protein phosphorylation reaction in D and cites experimental evidence (ECO:0000269, PubMed 24832449). This supports the key, though the cited paper was not independently reviewed here.",
    "evidence_ids": ["C1", "C5", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a kinase-like ATP-binding region, consistent with a protein kinase. Of the choices, D is the protein-phosphorylation reaction; the other options describe ATP hydrolysis, siderophore oxidation, or methyl transfer.",
    "missing_item_specific_fact": "The sequence alone does not establish this particular kinase's preference for threonine versus serine. That residue-level specificity is supported by the sequence-matched annotation, and the choices do not include a serine-phosphorylation alternative.",
    "reason": "The kinase-like sequence provides a biological basis to select the protein-phosphorylation reaction over the unrelated reaction classes. The precise threonine assignment is less directly inferable from sequence alone, but it does not create a competing listed choice."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "D is the only listed reaction consistent with a protein kinase; ATP use alone does not make the generic ATP-hydrolysis option A an equivalent reaction."
  },
  "important_caveats": [
    "The cited annotation provides experimental-evidence attribution, but the underlying primary study was not independently validated here.",
    "The same entry also annotates serine phosphorylation, which is not offered as a choice."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q2PAY3 (Toxoplasma gondii ROP17, EC 2.7.11.1) explicitly lists 'L-threonyl-&#91;protein&#93; + ATP = O-phospho-L-threonyl-&#91;protein&#93; + ADP + H(+)' as a CATALYTIC ACTIVITY with evidence code ECO:0000269 (direct assay) from PubMed:24832449. The supplied sequence matches the entry exactly (608 aa, SHA256 confirmed). The expected answer D is a verbatim match to the annotated reaction.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [H2](#evidence-h2), [H3](#evidence-h3), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains recognizable protein kinase domain architecture: a glycine-rich loop region, a VAIK-like lysine motif, an HRD-like catalytic motif (HGD variant), and a canonical DFG motif ('DFGVMKYFPPE'). These conserved kinase motifs, together with the bilobal fold arrangement, allow a trained biologist to identify this as a protein kinase (EC 2.7.11.1) rather than a simple ATPase (option A), a siderophore oxidase (option B), or a methyltransferase (option C). The kinase reaction specifically transfers phosphate to a protein hydroxyl group (Thr/Ser), distinguishing it from ATP hydrolysis.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Recognition of the protein kinase fold from conserved sequence motifs (DFG, HRD-like, glycine-rich loop, catalytic lysine) is a general biochemistry skill that meaningfully distinguishes option D from the other three choices. The oxidase (B) and methyltransferase (C) reactions involve entirely different cofactors and domain architectures absent from this sequence. While distinguishing a kinase from an ATPase (A) requires domain-level recognition rather than trivial motif matching, the presence of substrate-binding groove features and the complete kinase catalytic machinery supports the kinase assignment over simple hydrolysis.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although the UniProt entry also lists L-seryl-&#91;protein&#93; phosphorylation (C6/H6), this reaction is not among the answer choices, so no ambiguity arises. Option A (ATP hydrolysis) is a standard distractor: while kinases do consume ATP, the annotated catalytic activity is phosphotransfer to a protein substrate, not free hydrolysis. Options B and C involve unrelated cofactors (NAD+, SAM) and domain types clearly absent from this sequence.


### Important caveats

- The serine phosphorylation reaction (EC 2.7.11.1, ECO:0000305) is also annotated for this protein but is not offered as a choice, so it does not create answer ambiguity.
- ROP17 is related to the ROP pseudokinase family (ROP5 is a pseudokinase); ROP17 retains genuine kinase activity per PubMed:24832449, but the motifs are somewhat degenerate, which could make domain recognition marginally harder for a model.
- The accession Q2PAY3 was inferred by the reviewer from dataset metadata; it was not provided to the evaluated model. The model must rely on sequence-based reasoning alone.
- Evidence code for the threonine reaction is ECO:0000269 (direct assay), while the serine reaction carries ECO:0000305 (inferred), indicating the threonine activity has stronger experimental support.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains recognizable protein kinase domain architecture: a glycine-rich loop region, a VAIK-like lysine motif, an HRD-like catalytic motif (HGD variant), and a canonical DFG motif ('DFGVMKYFPPE'). These conserved kinase motifs, together with the bilobal fold arrangement, allow a trained biologist to identify this as a protein kinase (EC 2.7.11.1) rather than a simple ATPase (option A), a siderophore oxidase (option B), or a methyltransferase (option C). The kinase reaction specifically transfers phosphate to a protein hydroxyl group (Thr/Ser), distinguishing it from ATP hydrolysis.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Recognition of the protein kinase fold from conserved sequence motifs (DFG, HRD-like, glycine-rich loop, catalytic lysine) is a general biochemistry skill that meaningfully distinguishes option D from the other three choices. The oxidase (B) and methyltransferase (C) reactions involve entirely different cofactors and domain architectures absent from this sequence. While distinguishing a kinase from an ATPase (A) requires domain-level recognition rather than trivial motif matching, the presence of substrate-binding groove features and the complete kinase catalytic machinery supports the kinase assignment over simple hydrolysis."
  },
  "case_id": "catalytic_activity_0195",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C7",
      "H2",
      "H3",
      "H5"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q2PAY3 (Toxoplasma gondii ROP17, EC 2.7.11.1) explicitly lists 'L-threonyl-[protein] + ATP = O-phospho-L-threonyl-[protein] + ADP + H(+)' as a CATALYTIC ACTIVITY with evidence code ECO:0000269 (direct assay) from PubMed:24832449. The supplied sequence matches the entry exactly (608 aa, SHA256 confirmed). The expected answer D is a verbatim match to the annotated reaction."
  },
  "important_caveats": [
    "The serine phosphorylation reaction (EC 2.7.11.1, ECO:0000305) is also annotated for this protein but is not offered as a choice, so it does not create answer ambiguity.",
    "ROP17 is related to the ROP pseudokinase family (ROP5 is a pseudokinase); ROP17 retains genuine kinase activity per PubMed:24832449, but the motifs are somewhat degenerate, which could make domain recognition marginally harder for a model.",
    "The accession Q2PAY3 was inferred by the reviewer from dataset metadata; it was not provided to the evaluated model. The model must rely on sequence-based reasoning alone.",
    "Evidence code for the threonine reaction is ECO:0000269 (direct assay), while the serine reaction carries ECO:0000305 (inferred), indicating the threonine activity has stronger experimental support."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the UniProt entry also lists L-seryl-[protein] phosphorylation (C6/H6), this reaction is not among the answer choices, so no ambiguity arises. Option A (ATP hydrolysis) is a standard distractor: while kinases do consume ATP, the annotated catalytic activity is phosphotransfer to a protein substrate, not free hydrolysis. Options B and C involve unrelated cofactors (NAD+, SAM) and domain types clearly absent from this sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0195",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q2PAY3 (Toxoplasma gondii ROP17, EC 2.7.11.1) explicitly lists 'L-threonyl-[protein] + ATP = O-phospho-L-threonyl-[protein] + ADP + H(+)' as a CATALYTIC ACTIVITY with evidence code ECO:0000269 (direct assay) from PubMed:24832449. The supplied sequence matches the entry exactly (608 aa, SHA256 confirmed). The expected answer D is a verbatim match to the annotated reaction.",
    "evidence_ids": ["C4", "C5", "C7", "H2", "H3", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains recognizable protein kinase domain architecture: a glycine-rich loop region, a VAIK-like lysine motif, an HRD-like catalytic motif (HGD variant), and a canonical DFG motif ('DFGVMKYFPPE'). These conserved kinase motifs, together with the bilobal fold arrangement, allow a trained biologist to identify this as a protein kinase (EC 2.7.11.1) rather than a simple ATPase (option A), a siderophore oxidase (option B), or a methyltransferase (option C). The kinase reaction specifically transfers phosphate to a protein hydroxyl group (Thr/Ser), distinguishing it from ATP hydrolysis.",
    "missing_item_specific_fact": "",
    "reason": "Recognition of the protein kinase fold from conserved sequence motifs (DFG, HRD-like, glycine-rich loop, catalytic lysine) is a general biochemistry skill that meaningfully distinguishes option D from the other three choices. The oxidase (B) and methyltransferase (C) reactions involve entirely different cofactors and domain architectures absent from this sequence. While distinguishing a kinase from an ATPase (A) requires domain-level recognition rather than trivial motif matching, the presence of substrate-binding groove features and the complete kinase catalytic machinery supports the kinase assignment over simple hydrolysis."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the UniProt entry also lists L-seryl-[protein] phosphorylation (C6/H6), this reaction is not among the answer choices, so no ambiguity arises. Option A (ATP hydrolysis) is a standard distractor: while kinases do consume ATP, the annotated catalytic activity is phosphotransfer to a protein substrate, not free hydrolysis. Options B and C involve unrelated cofactors (NAD+, SAM) and domain types clearly absent from this sequence."
  },
  "important_caveats": [
    "The serine phosphorylation reaction (EC 2.7.11.1, ECO:0000305) is also annotated for this protein but is not offered as a choice, so it does not create answer ambiguity.",
    "ROP17 is related to the ROP pseudokinase family (ROP5 is a pseudokinase); ROP17 retains genuine kinase activity per PubMed:24832449, but the motifs are somewhat degenerate, which could make domain recognition marginally harder for a model.",
    "The accession Q2PAY3 was inferred by the reviewer from dataset metadata; it was not provided to the evaluated model. The model must rely on sequence-based reasoning alone.",
    "Evidence code for the threonine reaction is ECO:0000269 (direct assay), while the serine reaction carries ECO:0000305 (inferred), indicating the threonine activity has stronger experimental support."
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

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2PAY3?format=txt&versions=86)  
**Locator:** `lines 24-31`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 86 / 1.  
**Retrieved:** 2026-11-02T04:30:38.452820+00:00.  

```text
RN   [2] {ECO:0000305}
RP   IDENTIFICATION BY MASS SPECTROMETRY, FUNCTION, CATALYTIC ACTIVITY,
RP   INTERACTION WITH ROP5, SUBCELLULAR LOCATION, AND DISRUPTION PHENOTYPE.
RX   PubMed=24832449; DOI=10.1016/j.chom.2014.04.002;
RA   Etheridge R.D., Alaganan A., Tang K., Lou H.J., Turk B.E., Sibley L.D.;
RT   "The Toxoplasma pseudokinase ROP5 forms complexes with ROP18 and ROP17
RT   kinases that synergize to control acute virulence in mice.";
RL   Cell Host Microbe 15:537-550(2014).
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

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 195. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
