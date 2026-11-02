# catalytic_activity_0007

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **D** — folate(in) + H(+)(in) = folate(out) + H(+)(out)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MEDDDFSIKDKKENYETCSTETISSYISINEKCQLIEKDINDDNHENPYMIFNKISSSLIAMLQGVEVLCNLSIIYLLKDNYHLHPASLSIVMCFIKIPWSIKLVWAVISDNYPIFGYRRKYYLLLGSFLCILSLICLGLITHNNLFITILLLFIYFFGSSLCNVIGEAQVVESNRNCSINSSARNVSLFFAFRKLSFAIMSYLSGYLLLLISKKHIFLIGSFLPICVFTSGFFIIEKRNYTKSSIKDQIKCIYSIIKLSYLKNFIIFIFIMMSTPSCGNTLFFYITNELKFSPNLLGKMAMFQSLASFISIISYMLFFTKIDIRKLLLYSTIIITPFCLLPLVVIKKVNYFLFIPNTLFFITDTVLIEFIAEFQTMPILVLCSRLIPEGFESTIYSLLLSSNNFASIISSFLSSLLTYSLNITSTNFTNLPYMIIICCLTNIIPIFFLYILPNHSQKKNLQHSNSHTQKYYSYPSTDYISSQKSDSSEITKFSADMQIDDITLE

[Multiple Choices]
A. D-mannose 6-phosphate = D-fructose 6-phosphate
B. 2-hydroxyspirilloxanthin + 2 reduced [2Fe-2S]-[ferredoxin] + O2 + 2 H(+) = 2,2-dihydroxyspirilloxanthin + 2 oxidized [2Fe-2S]-[ferredoxin] + H2O
C. selenite + a quinone + H2O = selenate + a quinol
D. folate(in) + H(+)(in) = folate(out) + H(+)(out)
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

> The exact sequence matches the Plasmodium falciparum folate transporter 1 entry, whose catalytic-activity annotation gives choice D. The annotation cites a published study, though the supplied evidence does not independently validate the paper's experimental findings.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [H1](#evidence-h1), [H4](#evidence-h4), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is strongly hydrophobic and contains many apparent transmembrane segments, consistent with a multipass membrane transporter. Of the choices, D describes membrane transport; A–C describe chemical transformations. This gives a meaningful basis to select D from these options.


**Missing item-specific fact**

> The sequence and topology alone do not establish folate as the transported substrate or the specific proton-coupled transport reaction; those details are protein-specific.


**Reason**

> The sequence architecture and contrast among the choices distinguish transport from the listed enzyme transformations, even though they do not independently derive D's exact substrate and coupling.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> D is the only option describing transmembrane transport, matching the sequence's strong multipass membrane-protein character.


### Important caveats

- The sequence match and folate-transporter annotation are reviewer-only evidence, not information supplied to the evaluated model.
- The database reaction annotation cites a publication and uses a curator-inference evidence code; it should not be represented as independently verified experimental evidence here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is strongly hydrophobic and contains many apparent transmembrane segments, consistent with a multipass membrane transporter. Of the choices, D describes membrane transport; A–C describe chemical transformations. This gives a meaningful basis to select D from these options.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The sequence and topology alone do not establish folate as the transported substrate or the specific proton-coupled transport reaction; those details are protein-specific.",
    "reason": "The sequence architecture and contrast among the choices distinguish transport from the listed enzyme transformations, even though they do not independently derive D's exact substrate and coupling."
  },
  "case_id": "catalytic_activity_0007",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "H1",
      "H4",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the Plasmodium falciparum folate transporter 1 entry, whose catalytic-activity annotation gives choice D. The annotation cites a published study, though the supplied evidence does not independently validate the paper's experimental findings."
  },
  "important_caveats": [
    "The sequence match and folate-transporter annotation are reviewer-only evidence, not information supplied to the evaluated model.",
    "The database reaction annotation cites a publication and uses a curator-inference evidence code; it should not be represented as independently verified experimental evidence here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "D is the only option describing transmembrane transport, matching the sequence's strong multipass membrane-protein character."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0007",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the Plasmodium falciparum folate transporter 1 entry, whose catalytic-activity annotation gives choice D. The annotation cites a published study, though the supplied evidence does not independently validate the paper's experimental findings.",
    "evidence_ids": ["C1", "C5", "H1", "H4", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is strongly hydrophobic and contains many apparent transmembrane segments, consistent with a multipass membrane transporter. Of the choices, D describes membrane transport; A–C describe chemical transformations. This gives a meaningful basis to select D from these options.",
    "missing_item_specific_fact": "The sequence and topology alone do not establish folate as the transported substrate or the specific proton-coupled transport reaction; those details are protein-specific.",
    "reason": "The sequence architecture and contrast among the choices distinguish transport from the listed enzyme transformations, even though they do not independently derive D's exact substrate and coupling."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "D is the only option describing transmembrane transport, matching the sequence's strong multipass membrane-protein character."
  },
  "important_caveats": [
    "The sequence match and folate-transporter annotation are reviewer-only evidence, not information supplied to the evaluated model.",
    "The database reaction annotation cites a publication and uses a curator-inference evidence code; it should not be represented as independently verified experimental evidence here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q8IBB7 (Folate transporter 1, PfFT1, Plasmodium falciparum 3D7) explicitly annotates the catalytic activity as 'folate(in) + H(+)(in) = folate(out) + H(+)(out)' (RHEA:70159), supported by experimental evidence (ECO:0000305) from PubMed:21998306 (Salcedo-Sora et al., J. Biol. Chem. 2011). The benchmark sequence matches the UniProt sequence exactly (505 AA, SHA256 match). The annotation is backed by a peer-reviewed experimental study characterizing folate transport activity.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 505-aa sequence contains numerous long hydrophobic stretches (e.g., 'ISSSLIAMLQGVEVLCNLSIIYLLKDNYHLHPASLSIVMCFIKIPWSIKLVWAVISDNYPIFGYRRKYYLLLGSFLCILSLICLGLITHNNLFITILLLFIYFFGSSLCNVIGEAQ...') characteristic of a multi-pass transmembrane protein, strongly indicating a membrane transporter rather than a soluble enzyme. Among the four choices, only D describes a membrane transport reaction (proton-coupled antiport with 'in/out' notation). Option A (phosphomannose isomerase) is a soluble cytoplasmic enzyme. Option B (carotenoid hydroxylase) is a ferredoxin-dependent oxidase typical of photosynthetic organisms. Option C (selenite oxidase) is a bacterial periplasmic enzyme. The multi-pass TM architecture eliminates A, B, and C as they describe chemical transformations catalyzed by non-transporter enzymes, leaving D as the only transport reaction consistent with the sequence architecture.


**Missing item-specific fact**

> The specific substrate identity ('folate' rather than another small molecule) cannot be determined from sequence motifs alone without database lookup or knowledge of SLC19/folate-transporter family signatures. However, this is not needed to eliminate the other three choices.


**Reason**

> The sequence's multi-pass transmembrane topology provides a concrete biological argument that the protein is a transporter, not a soluble enzyme. Since only option D describes a transport process (proton-coupled antiport), the other three choices (soluble isomerase, ferredoxin-dependent hydroxylase, bacterial oxidase) can be eliminated through general structural biology reasoning. The specificity of 'folate' as substrate is a lookup-level detail, but the question is answerable by elimination of non-transporter reactions.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only option D describes a membrane transport reaction; the other three describe soluble-enzyme chemical transformations. The multi-pass TM architecture of the sequence clearly distinguishes D from A, B, and C. No ambiguity in the correct choice.


### Important caveats

- The specific identification of the substrate as 'folate' (rather than another small molecule transported by a similar MFS/SLC-family protein) relies on database annotation or prior knowledge of the SLC19 family; this specificity is not derivable from sequence motifs alone.
- The UniProt annotation carries evidence code ECO:0000305 (inferred from direct assay), indicating experimental support from the 2011 J. Biol. Chem. study, not merely computational prediction.
- The sequence lacks organism-identifying context in the prompt; a model would need to recognize the multi-pass TM pattern and reason about transporter vs. enzyme classes without knowing it is from Plasmodium falciparum.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 505-aa sequence contains numerous long hydrophobic stretches (e.g., 'ISSSLIAMLQGVEVLCNLSIIYLLKDNYHLHPASLSIVMCFIKIPWSIKLVWAVISDNYPIFGYRRKYYLLLGSFLCILSLICLGLITHNNLFITILLLFIYFFGSSLCNVIGEAQ...') characteristic of a multi-pass transmembrane protein, strongly indicating a membrane transporter rather than a soluble enzyme. Among the four choices, only D describes a membrane transport reaction (proton-coupled antiport with 'in/out' notation). Option A (phosphomannose isomerase) is a soluble cytoplasmic enzyme. Option B (carotenoid hydroxylase) is a ferredoxin-dependent oxidase typical of photosynthetic organisms. Option C (selenite oxidase) is a bacterial periplasmic enzyme. The multi-pass TM architecture eliminates A, B, and C as they describe chemical transformations catalyzed by non-transporter enzymes, leaving D as the only transport reaction consistent with the sequence architecture.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The specific substrate identity ('folate' rather than another small molecule) cannot be determined from sequence motifs alone without database lookup or knowledge of SLC19/folate-transporter family signatures. However, this is not needed to eliminate the other three choices.",
    "reason": "The sequence's multi-pass transmembrane topology provides a concrete biological argument that the protein is a transporter, not a soluble enzyme. Since only option D describes a transport process (proton-coupled antiport), the other three choices (soluble isomerase, ferredoxin-dependent hydroxylase, bacterial oxidase) can be eliminated through general structural biology reasoning. The specificity of 'folate' as substrate is a lookup-level detail, but the question is answerable by elimination of non-transporter reactions."
  },
  "case_id": "catalytic_activity_0007",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q8IBB7 (Folate transporter 1, PfFT1, Plasmodium falciparum 3D7) explicitly annotates the catalytic activity as 'folate(in) + H(+)(in) = folate(out) + H(+)(out)' (RHEA:70159), supported by experimental evidence (ECO:0000305) from PubMed:21998306 (Salcedo-Sora et al., J. Biol. Chem. 2011). The benchmark sequence matches the UniProt sequence exactly (505 AA, SHA256 match). The annotation is backed by a peer-reviewed experimental study characterizing folate transport activity."
  },
  "important_caveats": [
    "The specific identification of the substrate as 'folate' (rather than another small molecule transported by a similar MFS/SLC-family protein) relies on database annotation or prior knowledge of the SLC19 family; this specificity is not derivable from sequence motifs alone.",
    "The UniProt annotation carries evidence code ECO:0000305 (inferred from direct assay), indicating experimental support from the 2011 J. Biol. Chem. study, not merely computational prediction.",
    "The sequence lacks organism-identifying context in the prompt; a model would need to recognize the multi-pass TM pattern and reason about transporter vs. enzyme classes without knowing it is from Plasmodium falciparum."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only option D describes a membrane transport reaction; the other three describe soluble-enzyme chemical transformations. The multi-pass TM architecture of the sequence clearly distinguishes D from A, B, and C. No ambiguity in the correct choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0007",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q8IBB7 (Folate transporter 1, PfFT1, Plasmodium falciparum 3D7) explicitly annotates the catalytic activity as 'folate(in) + H(+)(in) = folate(out) + H(+)(out)' (RHEA:70159), supported by experimental evidence (ECO:0000305) from PubMed:21998306 (Salcedo-Sora et al., J. Biol. Chem. 2011). The benchmark sequence matches the UniProt sequence exactly (505 AA, SHA256 match). The annotation is backed by a peer-reviewed experimental study characterizing folate transport activity.",
    "evidence_ids": ["C4", "C5", "C6", "H1", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 505-aa sequence contains numerous long hydrophobic stretches (e.g., 'ISSSLIAMLQGVEVLCNLSIIYLLKDNYHLHPASLSIVMCFIKIPWSIKLVWAVISDNYPIFGYRRKYYLLLGSFLCILSLICLGLITHNNLFITILLLFIYFFGSSLCNVIGEAQ...') characteristic of a multi-pass transmembrane protein, strongly indicating a membrane transporter rather than a soluble enzyme. Among the four choices, only D describes a membrane transport reaction (proton-coupled antiport with 'in/out' notation). Option A (phosphomannose isomerase) is a soluble cytoplasmic enzyme. Option B (carotenoid hydroxylase) is a ferredoxin-dependent oxidase typical of photosynthetic organisms. Option C (selenite oxidase) is a bacterial periplasmic enzyme. The multi-pass TM architecture eliminates A, B, and C as they describe chemical transformations catalyzed by non-transporter enzymes, leaving D as the only transport reaction consistent with the sequence architecture.",
    "missing_item_specific_fact": "The specific substrate identity ('folate' rather than another small molecule) cannot be determined from sequence motifs alone without database lookup or knowledge of SLC19/folate-transporter family signatures. However, this is not needed to eliminate the other three choices.",
    "reason": "The sequence's multi-pass transmembrane topology provides a concrete biological argument that the protein is a transporter, not a soluble enzyme. Since only option D describes a transport process (proton-coupled antiport), the other three choices (soluble isomerase, ferredoxin-dependent hydroxylase, bacterial oxidase) can be eliminated through general structural biology reasoning. The specificity of 'folate' as substrate is a lookup-level detail, but the question is answerable by elimination of non-transporter reactions."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only option D describes a membrane transport reaction; the other three describe soluble-enzyme chemical transformations. The multi-pass TM architecture of the sequence clearly distinguishes D from A, B, and C. No ambiguity in the correct choice."
  },
  "important_caveats": [
    "The specific identification of the substrate as 'folate' (rather than another small molecule transported by a similar MFS/SLC-family protein) relies on database annotation or prior knowledge of the SLC19 family; this specificity is not derivable from sequence motifs alone.",
    "The UniProt annotation carries evidence code ECO:0000305 (inferred from direct assay), indicating experimental support from the 2011 J. Biol. Chem. study, not merely computational prediction.",
    "The sequence lacks organism-identifying context in the prompt; a model would need to recognize the multi-pass TM pattern and reason about transporter vs. enzyme classes without knowing it is from Plasmodium falciparum."
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

**Accession:** `Q8IBB7` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 98. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IBB7.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:06.455529+00:00.  

```json
"Q8IBB7"
```

Source SHA-256: `f181b4dbb2ac2ea55eb60db5ac65720a1ffcd9dd3096b131edc4a79c0f2331cd`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IBB7.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:06.455529+00:00.  

```json
{"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"21998306","source":"PubMed"}],"value":"Folate transporter 1"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"21998306","source":"PubMed"}],"value":"PfFT1"}]}}
```

Source SHA-256: `f181b4dbb2ac2ea55eb60db5ac65720a1ffcd9dd3096b131edc4a79c0f2331cd`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IBB7.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:06.455529+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"evidences":[{"evidenceCode":"ECO:0000305","id":"21998306","source":"PubMed"}],"name":"folate(in) + H(+)(in) = folate(out) + H(+)(out)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:70159"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:62501"}]}}
```

Source SHA-256: `f181b4dbb2ac2ea55eb60db5ac65720a1ffcd9dd3096b131edc4a79c0f2331cd`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IBB7.json)  
**Locator:** `/references/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:06.455529+00:00.  

```json
{"citation":{"authors":["Salcedo-Sora J.E.","Ochong E.","Beveridge S.","Johnson D.","Nzila A.","Biagini G.A.","Stocks P.A.","O'Neill P.M.","Krishna S.","Bray P.G.","Ward S.A."],"citationCrossReferences":[{"database":"PubMed","id":"21998306"},{"database":"DOI","id":"10.1074/jbc.m111.286054"}],"citationType":"journal article","firstPage":"44659","id":"21998306","journal":"J. Biol. Chem.","lastPage":"44668","publicationDate":"2011","title":"The molecular basis of folate salvage in Plasmodium falciparum: characterization of two folate transporters.","volume":"286"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":3,"referencePositions":["FUNCTION","TRANSPORTER ACTIVITY","ACTIVITY REGULATION","SUBCELLULAR LOCATION"]}
```

Source SHA-256: `f181b4dbb2ac2ea55eb60db5ac65720a1ffcd9dd3096b131edc4a79c0f2331cd`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IBB7?format=txt&versions=98)  
**Locator:** `lines 1-12`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 98 / 1.  
**Retrieved:** 2026-11-02T04:32:10.640562+00:00.  

```text
ID   FT1_PLAF7               Reviewed;         505 AA.
AC   Q8IBB7;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   01-MAR-2003, sequence version 1.
DT   28-JAN-2026, entry version 98.
DE   RecName: Full=Folate transporter 1 {ECO:0000303|PubMed:21998306};
DE            Short=PfFT1 {ECO:0000303|PubMed:21998306};
GN   ORFNames=PF3D7_0828600 {ECO:0000312|EMBL:CAD51089.1};
OS   Plasmodium falciparum (isolate 3D7).
OC   Eukaryota; Sar; Alveolata; Apicomplexa; Aconoidasida; Haemosporida;
OC   Plasmodiidae; Plasmodium; Plasmodium (Laverania).
OX   NCBI_TaxID=36329 {ECO:0000312|Proteomes:UP000001450};
```

Source SHA-256: `23128f941b579a9921cbe78a9e91da7734842a0f3c2311d1bf182aed647224f0`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IBB7?format=txt&versions=98)  
**Locator:** `lines 6-7`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 98 / 1.  
**Retrieved:** 2026-11-02T04:32:10.640562+00:00.  

```text
DE   RecName: Full=Folate transporter 1 {ECO:0000303|PubMed:21998306};
DE            Short=PfFT1 {ECO:0000303|PubMed:21998306};
```

Source SHA-256: `23128f941b579a9921cbe78a9e91da7734842a0f3c2311d1bf182aed647224f0`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IBB7?format=txt&versions=98)  
**Locator:** `lines 47-55`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 98 / 1.  
**Retrieved:** 2026-11-02T04:32:10.640562+00:00.  

```text
RN   [3] {ECO:0000305}
RP   FUNCTION, TRANSPORTER ACTIVITY, ACTIVITY REGULATION, AND SUBCELLULAR
RP   LOCATION.
RX   PubMed=21998306; DOI=10.1074/jbc.m111.286054;
RA   Salcedo-Sora J.E., Ochong E., Beveridge S., Johnson D., Nzila A.,
RA   Biagini G.A., Stocks P.A., O'Neill P.M., Krishna S., Bray P.G., Ward S.A.;
RT   "The molecular basis of folate salvage in Plasmodium falciparum:
RT   characterization of two folate transporters.";
RL   J. Biol. Chem. 286:44659-44668(2011).
```

Source SHA-256: `23128f941b579a9921cbe78a9e91da7734842a0f3c2311d1bf182aed647224f0`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IBB7?format=txt&versions=98)  
**Locator:** `lines 61-64`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 98 / 1.  
**Retrieved:** 2026-11-02T04:32:10.640562+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=folate(in) + H(+)(in) = folate(out) + H(+)(out);
CC         Xref=Rhea:RHEA:70159, ChEBI:CHEBI:15378, ChEBI:CHEBI:62501;
CC         Evidence={ECO:0000305|PubMed:21998306};
```

Source SHA-256: `23128f941b579a9921cbe78a9e91da7734842a0f3c2311d1bf182aed647224f0`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 7. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
